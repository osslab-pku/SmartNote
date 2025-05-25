import os
import github
from github import Github, GithubException
import re
from typing import Literal, Optional, Tuple, List, Union
from math import log
import pandas as pd
import numpy as np
import git
import shutil
from tqdm import tqdm
from semver import VersionInfo
from pydriller import Repository, ModificationType, Git as PyGit
from loguru import logger
from dacite import from_dict
from smartdraft.prompts_manager import PromptsManager

from .config import settings
from .languages import get_lang_names, infer_langids_onehot
from .dtypes import PROJECT_DOMAIN_TYPE, CommitData, OpenAIConfig, ReleaseNoteCommitEntry, ReleaseNotePrEntry

def clone_repo(
    url: str,
    dest_dir: str,
    branch=None,
    force=False,
    proxy=None,
):
    # if url is name with owner, it is a github repo
    if re.match(r"^[\w-]+/[\w._-]+$", url):
        url = f"https://github.com/{url}"
    config = f"http.proxy={proxy}" if proxy else None
    try:
        if os.path.exists(dest_dir):
            if not force:
                # pull the latest
                logger.info(f"Pulling {url} to {dest_dir}")
                repo = git.Repo(dest_dir)
                repo.remotes.origin.pull(allow_unsafe_options=True)
                return
            else:
                logger.warning("Removing {} from {}".format(url, dest_dir))
                shutil.rmtree(dest_dir)
        logger.info(f"Cloning {url} to {dest_dir}")
        git.Repo.clone_from(
            url, dest_dir, branch=branch, config=config, allow_unsafe_options=True
        )
    except Exception as e:  # can also be AttributeError, ...
        try:
            # remove the corrupted repo and try again
            logger.error(f"Error cloning {url}: {e}")
            if os.path.exists(dest_dir):
                shutil.rmtree(dest_dir)
            git.Repo.clone_from(
                url, dest_dir, branch=branch, config=config, allow_unsafe_options=True
            )
        except Exception as e:
            logger.error(f"Error cloning {url}: {e}")
            raise e


def get_stats_ghapi(
    gh: Github,
    repo_name: str,
):
    try:
        repo = gh.get_repo(repo_name)
        _prs = repo.get_pulls(state="all").totalCount
        return dict(
            name=repo.full_name,
            commits=repo.get_commits().totalCount,
            contributors=repo.get_contributors().totalCount,
            issues=repo.get_issues(state="all").totalCount - _prs,
            prs=_prs,
            stars=repo.stargazers_count,
            comments=repo.get_issues_comments().totalCount,
            # releases=repo.get_releases().totalCount,
        )

    except GithubException as e:
        logger.error(f"{repo_name}: {e}")
        repo = gh.get_repo(repo)
        _prs = repo.get_pulls(state="all").totalCount
        return dict(
            name=repo,
            commits=repo.get_commits().totalCount,
            contributors=repo.get_contributors().totalCount,
            issues=repo.get_issues(state="all").totalCount - _prs,
            prs=_prs,
            stars=repo.stargazers_count,
            comments=repo.get_issues_comments().totalCount,
            # releases=repo.get_releases().totalCount,
        )


def get_release_dates(
    gh: Github,
    repo_name: str,
):
    try:
        repo = gh.get_repo(repo_name)
        releases = repo.get_releases()
        _ret = []
        for release in tqdm(
            releases, desc="Fetching releases", total=releases.totalCount
        ):
            _ret.append(
                {
                    "name": repo_name,
                    "currentName": repo.full_name,
                    "tag": release.tag_name,
                    "createdAt": release.created_at,
                    "publishedAt": release.published_at,
                    "target": release.target_commitish,
                }
            )
        return _ret
    except Exception as e:
        logger.error(f"{repo}: {e}", exc_info=True)
        return []


# strip everything before the occurance of \d+\.
def _strip_version(s):
    # if s is not str, e.g. 1.0
    if not isinstance(s, str):
        return str(s)
    return re.sub(r"^.*?(\d+\..*)$", r"\1", s)


RELEASE_TYPES = ["Major", "Minor", "Patch", "Unknown"]


def infer_release_type(
    prev_version: str,
    new_version: str,
) -> Literal["Major", "Minor", "Patch", "Unknown"]:
    prev_version = _strip_version(prev_version)
    new_version = _strip_version(new_version)
    try:
        _pre = VersionInfo.parse(prev_version)
        _new = VersionInfo.parse(new_version)
        if _new.major > _pre.major:
            return "Major"
        elif _new.minor > _pre.minor:
            return "Minor"
        else:
            return "Patch"
    except ValueError:
        logger.debug(
            f"Error in parsing version: {prev_version}, {new_version}, leave as Unknown"
        )
        return "Unknown"


CONVENTIONAL_REGEX = re.compile(r"^([a-z]+)[:\(].*")
CONVENTIONAL_CATES = {
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
}
# Some repositories prefer to use emojis for commit category headers
# conventional: https://gist.github.com/parmentf/359667bf23e08a1bd8241fbf47ecdef0
# devmoji: https://github.com/folke/devmoji
EMOJI_TO_CONVENTIONAL_CATES = {
    "✨": "feat",
    "🐛": "fix",
    "📚": "docs",
    "💎": "style",
    "🎨": "style",
    "🔨": "refactor",
    "♻️": "refactor",
    "🚀": "perf",
    "⚡": "perf",
    "🚨": "test",
    "🧪": "test",
    "📦": "build",
    "👷": "ci",
    "🔧": "chore",
    "🔗": "chore", # deps
    "🗑️": "chore", # cleanup code
}

def parse_commit_message(message: str) -> Tuple[Optional[str], str]:
    """A naive parser for conventional commit messages."""
    # translate emoji to textual conventional categories
    for k, v in EMOJI_TO_CONVENTIONAL_CATES.items():
        if message.startswith(k):
            message = f"{v}: {message.replace(k, '', 1).strip()}"
            break

    _match = CONVENTIONAL_REGEX.match(message)
    if _match and _match.group(1) in CONVENTIONAL_CATES:
        _type = _match.group(1)
        if len(message) <= _match.end(1) + 1:
            return _type, ""
        _message = message[_match.end(1) :]
        if _message[0] == "(":  # scoped, like feat(scope): message
            _next = max(_message.find(")") + 2, 1)
        elif _message[0] == ":":  # no scope, like feat: message
            _next = 1
        else:
            return _type, _message
        return _type, _message[_next:].strip()
    return None, message


MERGE_PR_REGEX = re.compile(r"Merge pull request (#\d+)")
MERGE_BRANCH_REGEX = re.compile(r"Merge branch '(.+)'")

def get_commit_merge_from(message: str) -> str:
    _matched = MERGE_PR_REGEX.match(message)
    if _matched:
        return _matched.group(1)
    _matched = MERGE_BRANCH_REGEX.match(message)
    if _matched:
        return _matched.group(1)
    return ""


SHA_REGEX = re.compile(r"[0-9a-f]{7-40}")


def process_releases(
    repo: git.Repo,
    releases: List[dict],
):
    _releases = []
    for rel in releases:
        try:
            _commit = repo.commit(rel["tag"])  # rev-parse
        except Exception as e:
            if SHA_REGEX.match(rel["target"]):
                _commit = repo.commit(rel["target"])
            else:
                logger.error(f"Error in {os.path.basename(repo.working_dir)}: {e}")
                continue

        _sha = _commit.hexsha
        _date = _commit.authored_datetime
        _releases.append(
            {
                "tag": rel["tag"],
                "sha": _sha,
                "tagAuthoredAt": _date,
                "releaseCreatedAt": rel["createdAt"],
            }
        )

    return (
        pd.DataFrame(
            _releases, columns=["tag", "sha", "tagAuthoredAt", "releaseCreatedAt"]
        )
        .sort_values("releaseCreatedAt", ascending=False)
        .set_index("sha")
    )


def get_commit_stats(
    repo: git.Repo,
    df_releases: pd.DataFrame,
    gh: Optional[Github] = None,
) -> pd.DataFrame:
    repo_name = os.path.basename(repo.working_dir)
    logger.info(f"Found {len(df_releases)} releases in {repo_name}")
    if len(df_releases) < 2:
        logger.warning(f"Less than 2 releases in {repo_name}")
        return pd.DataFrame()

    _lang_names = get_lang_names()

    # iterate over releases
    _l_releases = []
    for i in range(len(df_releases) - 1):
        try:
            _from_sha = df_releases.index[i + 1]
            _to_sha = df_releases.index[i]
            _prev_tag_name = df_releases.iloc[i + 1]["tag"]
            _tag_name = df_releases.iloc[i]["tag"]
            
            repo_miner = Repository(
                repo.working_dir,
                from_commit=_from_sha,
                to_commit=_to_sha,
                order="reverse",
            )
            
            # _commits = list(repo_miner.traverse_commits())
            # if len(_commits) == 0:
            #     logger.warning(f"No commits in {repo_name} - {_prev_tag_name}...{_tag_name}. "
            #                     "This is usually due to git tags pointing to off-branch commits. "
            #                     "Falling back to GitHub API.")
            
            if gh is None:
                logger.warning("No GitHub API instance provided, skipping")
                continue
            try:
                _repo = gh.get_repo(repo_name.replace("_", "/"))
                _commits_gh = _repo.compare(_prev_tag_name, _tag_name).commits
                
                # logger.info(
                #     f"{repo_name}: Fetched {_prev_tag_name}...{_tag_name} from GitHub API: {_commits_gh.totalCount} commits"
                # )

                # convert github commits to pydriller commits
                with repo_miner._prep_repo(path_repo=repo.working_dir) as git:
                    _commits = [git.get_commit(_c.sha) for _c in _commits_gh]
                    # reverse it
                    _commits = _commits[::-1]
                
            except GithubException as e:
                logger.error(f"Error in GitHub API: {repo_name} - {_prev_tag_name}...{_tag_name}: {e}")
                continue

            logger.info(
                f"{repo_name}: Analyzing "
                f"{_prev_tag_name}...{_tag_name} ({i+1}/{len(df_releases)-1}): {len(_commits)} commits"
            )

            _l_commits = []
            # CodeChurn
            renamed_files = {}
            file_edit_lines = {}
            # ChangeSet
            n_files = []
            # HistoryComplexity
            file_edit_entropy = {}
            # uniqueAuthors
            commit_authors = set()

            for commit in tqdm(_commits, desc="Analyzing commits"):
                try:
                    _adds = 0
                    _dels = 0
                    _filenames = []

                    for modified_file in commit.modified_files:
                        # CodeChurn
                        filepath = renamed_files.get(
                            modified_file.new_path, modified_file.new_path
                        )
                        if modified_file.change_type == ModificationType.RENAME:
                            renamed_files[modified_file.old_path] = filepath
                        churn = modified_file.added_lines + modified_file.deleted_lines
                        file_edit_lines.setdefault(filepath, []).append(churn)
                        # ModLines
                        _adds += modified_file.added_lines
                        _dels += modified_file.deleted_lines
                        # LangEdited
                        _filenames.append(
                            filepath if filepath else modified_file.old_path
                        )

                    # ChangeSet
                    n_files.append(len(commit.modified_files))

                    # authors
                    commit_authors.add(commit.author.name)

                    # langs
                    _langids = infer_langids_onehot(
                        [f.split("/")[-1] for f in _filenames]
                    )
                    # transform to dict
                    langs = {k: v for k, v in zip(_lang_names, _langids)}

                    _l_commits.append(
                        {
                            "nameWithOwner": repo_name,
                            "sha": commit.hash,
                            "authorName": commit.author.name,
                            "authorEmail": commit.author.email,
                            "date": commit.committer_date,
                            "message": commit.msg,
                            "files": _filenames,
                            "nFiles": len(commit.modified_files),
                            "addLines": _adds,
                            "delLines": _dels,
                            **langs,
                        }
                    )
                except Exception as e:
                    logger.error(f"Error in {repo_name} - {commit.hash}: {e}")

            # if empty
            if len(_l_commits) == 0:
                logger.warning(
                    f"No commits in {repo_name} - {_prev_tag_name}...{_tag_name}"
                )
                continue

            df_commits = pd.DataFrame(_l_commits).convert_dtypes().set_index("sha")
            release_stats = pd.Series()
            # ReleaseType
            release_stats["releaseTag"] = _tag_name
            release_stats["releaseType"] = infer_release_type(_prev_tag_name, _tag_name)

            # uniqueAuthors
            release_stats["releaseAuthors"] = len(commit_authors)

            # number of commits
            release_stats["releaseCommits"] = len(_l_commits)

            # ChangeSet
            release_stats["avgChangeset"] = np.mean(n_files) if len(n_files) > 0 else 0

            # CodeChurn
            _codechurns = [np.mean(v) for v in file_edit_lines.values() if len(v) > 0]
            release_stats["avgCodeChurn"] = (
                np.mean(_codechurns) if len(_codechurns) > 0 else 0
            )

            # HistoryComplexity
            file_edit_entropy = {k: sum(v) for k, v in file_edit_lines.items()}
            # Total lines modified in the period
            total_modifications = sum(file_edit_entropy.values())
            # Number of modified files in the period
            n_files = len(file_edit_entropy)
            # From absolute number of changes to relative number of changes
            for filepath in file_edit_entropy:
                file_edit_entropy[filepath] /= total_modifications
            # Normalized entropy
            entropy = 0
            if len(file_edit_entropy.values()) > 1:
                entropy = -sum(
                    p * log(p + 1 / 1e10, n_files) for p in file_edit_entropy.values()
                )
            for filepath in file_edit_entropy:
                file_edit_entropy[filepath] *= entropy
                file_edit_entropy[filepath] = round(
                    file_edit_entropy[filepath] * 100, 2
                )
            release_stats["avgHistoryComplexity"] = (
                np.mean(list(file_edit_entropy.values()))
                if len(file_edit_entropy) > 0
                else 0
            )

            # set release stats
            df_commits = df_commits.assign(**release_stats)

            _l_releases.append(df_commits)

        except Exception as e:
            logger.error(
                f"Error in {repo_name} - {df_releases.iloc[i]['tag']}: {e}",
                exc_info=True,
            )

    return pd.concat(_l_releases) if len(_l_releases) > 0 else pd.DataFrame()


def collect_commits(
    repo_url: str,
    project_domain: Union[
        Literal[
            "System Software",
            "Software Tool",
            "Libraries&Framework",
            "Application Software",
        ],
        PROJECT_DOMAIN_TYPE,
    ],
    prev_release: Optional[str] = None,
    cur_release: Optional[str] = None,
) -> pd.DataFrame:
    """
    Collect commit data from a github repository.

    :param repo_url: github repository url
    :param prev_release: Git tag for previous release
    :param new_release: git tag for new release
    :param project_domain: the domain of the project
    :return: DataFrame of commit data
    """

    # map full domaains to short domains used by the new classifier
    _map = {
        "Application Software": "Application",
        "System Software": "System",
        "Libraries & Frameworks": "Library",
        "Software Tool": "Tool",
    }
    if project_domain in _map:
        project_domain = _map[project_domain]

    GITHUB_NAME_REGEX = re.compile(r"^[\w-]+/[\w._-]+$")
    if GITHUB_NAME_REGEX.match(repo_url):
        name_with_owner = repo_url
        repo_url = f"https://github.com/{repo_url}"
    else:
        GITHUB_REPO_REGEX = re.compile(r"^http?s://github.com/([\w-]+/[\w._-]+)(.git)?$")
        _matched = GITHUB_REPO_REGEX.match(repo_url)
        if not _matched:
            raise ValueError(f"Invalid Github repository URL: {repo_url}")
        name_with_owner = _matched.group(1)

    dest_dir = settings.CACHE_PATH / name_with_owner.replace("/", "_")
    clone_repo(repo_url, dest_dir)

    gh = Github(settings.GITHUB_TOKEN)
    repo = git.Repo(dest_dir)

    _repo_stats = get_stats_ghapi(gh, name_with_owner)

    repo_gh = gh.get_repo(name_with_owner)
    if prev_release is None or cur_release is None:
        _gh_releases = list(tqdm(
                repo_gh.get_releases(),
                desc="Fetching releases",
                total=repo_gh.get_releases().totalCount,
            ))
    else:
        logger.info(f"Fetching {prev_release}, {cur_release} for {name_with_owner}")
        _gh_releases = [
            repo_gh.get_release(prev_release),
            repo_gh.get_release(cur_release),
        ]
    
    _releases = []
    for release in _gh_releases:
        try:
            _releases.append(
                {
                    "name": name_with_owner,
                    "currentName": repo_gh.full_name,
                    "tag": release.tag_name,
                    "createdAt": release.created_at,
                    "publishedAt": release.published_at,
                    "target": release.target_commitish,
                }
            )
        except GithubException as e:
            logger.error(f"{name_with_owner}: {e}")
            raise e
        
    if len(_releases) < 2:
        logger.warning(f"Less than 2 releases in {name_with_owner}, cannot compare")
        return pd.DataFrame()

    df_releases = process_releases(repo, _releases)
    df_commits = get_commit_stats(repo, df_releases, gh)

    del _repo_stats["name"]
    _repo_stats["domain"] = project_domain
    df_commits = df_commits.assign(**_repo_stats)

    df_commits[["type", "body"]] = df_commits["message"].apply(
        lambda x: pd.Series(parse_commit_message(x), index=["type", "body"])
    )

    df_commits["mergeFrom"] = df_commits["message"].apply(get_commit_merge_from)
    df_commits["isMergeCommit"] = df_commits["mergeFrom"].apply(lambda x: True if x else False)
    df_commits.reset_index(inplace=True)
    df_commits.drop(columns=["files", "message"], inplace=True)
    return df_commits.convert_dtypes()


def get_prompt_commits(
    repo_name: str,
    prev_release: str,
    cur_release: str,
    use_prs: bool = True,
    pm: Optional[PromptsManager] = None,
    gh: Optional[Github] = None,
) -> tuple[
    dict[str, list[str]],
    str,
    dict[int, ReleaseNotePrEntry],
    dict[str, set[int]],
    dict[str, CommitData],
]:
    if pm is None:
        oai_conf = from_dict(OpenAIConfig, {k.lower(): v for k, v in settings.openai.items()})
        pm = PromptsManager(oai_conf)
    else:
        oai_conf = pm.get_openai_config()

    if gh is None:
        gh = Github(settings.GITHUB_TOKEN)

    # Retrieve the repository
    gh_repo = gh.get_repo(repo_name)
    # Compare the 2 mentioned tags
    comparison = gh_repo.compare(prev_release, cur_release)

    entire_tcr: str = ""  # TCR: Tag Comparison Results (i.e., all of the changes in every commit produced from the tag comparison)
    tcr_dict: dict[
        str, str
    ] = {}  # dict[commit_sha, tcr for individual commit (aka commit_changes)]

    pr_commits: dict[
        int, ReleaseNotePrEntry
    ] = {}  # dict[pr_number, ReleaseNotePrEntry(pr.title, pr.body, list[commit_sha])]
    commit_pr: dict[str, set[int]] = {}  # dict[commit_sha, set[pr_number]]
    commit_raw: dict[str, CommitData] = {}  # dict[commit_sha, CommitData]

    # print(
    #     f"There are a total of {comparison.commits.totalCount} commits in the comparison between {prev_release} and {cur_release}."
    # )

    # logger.info(f"{prev_release} ... {cur_release}: {comparison.commits.totalCount} commits")
    # Create a combined comparison result

    for commit in tqdm(comparison.commits, desc="Collecting PRs", total=comparison.commits.totalCount):
        # if (len(commit.raw_data["parents"]) > 1): # Skip commits which were merges.
        #    print(f"Skipped Commit: {commit.sha}")
        #    continue

        commit_raw[commit.sha] = CommitData.from_gh_response(commit.raw_data)
        if len(commit.parents) > 1:
            commit_raw[commit.sha].is_merge_commit = True

        # Get commit PR
        if use_prs:
            for pr in commit.get_pulls():
                # print(f"Commit: {commit.sha}, PR: {pr.number}")

                # Dict of PRs with value being a set of commit SHA
                if pr.number in pr_commits:
                    pr_entry = pr_commits.get(pr.number, None)
                    if pr_entry is None:
                        logger.warning(f"PR {repo_name}#{pr.number} not found in pr_commits")
                    pr_entry.commits.add(commit.sha)
                else:
                    pr_entry = ReleaseNotePrEntry(
                        pr.title, pr.body, {commit.sha}, pr.raw_data["merged_at"]
                    )
                    pr_commits[pr.number] = pr_entry

                # Dict of Commit SHAs with value a set of PR number
                if commit.sha in commit_pr:
                    commit_pr.get(commit.sha).add(pr.number)
                else:
                    commit_pr[commit.sha] = {pr.number}

            # debug print the PRs
            if commit.sha in commit_pr:
                logger.debug(f"Found {len(commit_pr[commit.sha])} PRs for commit {commit.sha}: {commit_pr[commit.sha]}")

        # Tag Comparison Results
        tcr = f"""<commit_details>Commit SHA: {commit.sha}
    Author: {commit.raw_data["commit"]["author"]["name"]} <{commit.raw_data["commit"]["author"]["email"]}>
    Date: {commit.raw_data["commit"]["author"]["date"]}
    Commit Message: \"{commit.raw_data["commit"]["message"]}\"</commit_details>\n\n"""

        entire_tcr += tcr

        # n_tokens = pm.get_num_tokens(tcr)

        # Holds the concatanation of the patch data for each file per commit
        combined_patch = ""

        for file_patch in commit.raw_data["files"]:
            file_diff = ""
            if "patch" in file_patch:
                file_diff = file_patch["patch"]

            previous_filename = ""
            if file_patch["status"] == "renamed":
                previous_filename = (
                    f"""\nprevious_filename: {file_patch["previous_filename"]}"""
                )

            patch = f'''<file_change>filename: {file_patch["filename"]}{previous_filename}
    status: {file_patch["status"]}\n
    """{file_diff}"""</file_change>\n\n'''

            # # If the length of the total string or token (ASCII len / 4) is greater than the maximum string length accepted by OpenAI API then skip the rest of the code.
            # current_result_len = PromptUtil.calculate_token_length(
            #     tcr, self._oai_conf.ascii_token_len
            # )
            # new_result_len = PromptUtil.calculate_token_length(
            #     patch, self._oai_conf.ascii_token_len
            # ) + PromptUtil.calculate_token_length(
            #     combined_patch, self._oai_conf.ascii_token_len
            # )
            # if (
            #     current_result_len + new_result_len
            #     > self._oai_conf.max_model_context_length
            # ) or (len(patch) + len(tcr) > self._oai_conf.max_string_length):

            _num_tokens = pm.count_tokens(tcr + combined_patch + patch)
            if _num_tokens > oai_conf.max_model_context_length:
                logger.warning(
                    f"Skipping commit {commit.sha} due to exceeding maximum token length"
                )
                continue
            if len(patch) + len(tcr) > oai_conf.max_string_length:
                logger.warning(
                    f"Skipping commit {commit.sha} due to exceeding maximum string length"
                )
                continue


            tcr_part = tcr + f"{combined_patch}"
            if commit.sha in tcr_dict:
                tcr_dict.get(commit.sha).append(tcr_part)
            else:
                tcr_dict[commit.sha] = [tcr_part]
            combined_patch = ""

            combined_patch += patch
            entire_tcr += patch

        tcr_part = tcr + f"{combined_patch}"
        if commit.sha in tcr_dict:
            tcr_dict.get(commit.sha).append(tcr_part)
        else:
            tcr_dict[commit.sha] = [tcr_part]

    

    return tcr_dict, entire_tcr, pr_commits, commit_pr, commit_raw


def get_pull_requests(
    repo_name: str, prev_release: str, cur_release: str, gh: Optional[Github] = None
) -> tuple[dict[str, set]]:
    if not gh:
        gh = Github(settings.GITHUB_TOKEN)
    gh_repo = gh.get_repo(repo_name)

    # Compare the 2 mentioend tags
    comparison = gh_repo.compare(prev_release, cur_release)

    pr_commits = {}
    pr_commits_trimmed = {}

    # Sort commits by PR
    for commit in comparison.commits:
        for pr in commit.get_pulls():
            print(f"Commit: {commit.sha}, PR: {pr.number}")
            if pr.number in pr_commits:
                pr_commits.get(pr.number).add(commit.sha)
            else:
                pr_commits[pr.number] = {commit.sha}

    # Some commits were squashed, remove those from the list.
    for pr in pr_commits:
        if len(pr_commits[pr]) != 1:
            pr_commits_trimmed[pr] = pr_commits[pr]

    return pr_commits_trimmed


def get_pr_and_commits(
    repo_name: str, prev_release: str, cur_release: str, gh: Optional[Github] = None
) -> tuple[dict[int, list[ReleaseNotePrEntry]], dict[str, ReleaseNoteCommitEntry]]:
    # Retrieve the repository
    if gh is None:
        gh = Github(settings.GITHUB_TOKEN)
    gh_repo = gh.get_repo(repo_name)

    # Compare the 2 mentioned tags
    comparison = gh_repo.compare(prev_release, cur_release)

    pr_commits: dict[
        int, list[ReleaseNotePrEntry]
    ] = {}  # dict[pr_number, ReleaseNotePrEntry(pr.title, pr.body, list[commit_sha])]
    commit_pr: dict[
        str, ReleaseNoteCommitEntry
    ] = {}  # dict[commit_sha, ReleaseNoteCommitEntry]

    print(
        f"There are a total of {comparison.commits.totalCount} commits in the comparison between {prev_release} and {cur_release}."
    )

    # Create a combined comparison result
    for commit in comparison.commits:
        commit_pr[commit.sha] = ReleaseNoteCommitEntry(
            commit.raw_data["commit"]["message"],
            set(),
            commit.sha,
            commit.raw_data["commit"]["author"]["date"],
        )
        # Get commit PR
        for pr in commit.get_pulls():
            # print(f"Commit: {commit.sha}, PR: {pr.number}")
            # Dict of PRs with value being a set of commit SHA
            if pr.number in pr_commits:
                pr_commits.get(pr.number).commits.append(commit.sha)
            else:
                pr_entry = ReleaseNotePrEntry(
                    pr.title, pr.body, [commit.sha], pr.raw_data["merged_at"]
                )
                pr_commits[pr.number] = pr_entry
            # Dict of Commit SHAs with value a set of PR number
            if commit.sha in commit_pr:
                commit_pr.get(commit.sha).prs.add(pr.number)
            else:
                print(f"Commit ({commit.sha}) entry doesn't exist.")

    return pr_commits, commit_pr
