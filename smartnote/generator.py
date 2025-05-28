import os
from pathlib import Path
from typing import List, Dict, Optional
from loguru import logger
from github import Github
from github.GithubException import GithubException, UnknownObjectException
import re
from dacite import from_dict
import pandas as pd

from .config import settings, init_env
from .dtypes import CONVENTIONAL_COMMITS_TYPE, PROJECT_DOMAIN_TYPE, STRUCTURE_TYPE, WRITING_STYLE_TYPE
from .dtypes import ReleaseNoteEntry, ReleaseNotePrEntry, ReleaseNoteCommitEntry, OpenAIConfig, CommitData
from .commit_analyzer import CommitAnalyzer
from .collector import get_prompt_commits
from .prompts_manager import PromptsManager


DEFAULT_WRITING_STYLE: Dict[PROJECT_DOMAIN_TYPE, WRITING_STYLE_TYPE] = {
    "System": "Persuasive",
    "Tool": "Descriptive",
    "Library": "Expository",
    "Application": "Expository",
}

DEFAULT_COMMIT_CATE_TO_EMOJI: Dict[CONVENTIONAL_COMMITS_TYPE, str] = {
    "build": "📦",
    "chore": "🔧",
    "ci": "👷",
    "refactor": "♻️",
    "perf": "🚀",
    "style": "🎨",
    "test": "🧪",
    "feat": "✨",
    "fix": "🐛",
    "docs": "📚",
    "revert": "⏪"
}

# DEFAULT_COMMIT_CATE_PRIORITY: Dict[CONVENTIONAL_COMMITS_TYPE, int] = {
#     "build": 1,
#     "chore": 1,
#     "ci": 1,
#     "refactor": 2,
#     "perf": 3,
#     "style": 2,
#     "test": 3,
#     "feat": 5,
#     "fix": 4,
#     "docs": 2,
#     "revert": 3
# }

def get_writing_style(project_domain: PROJECT_DOMAIN_TYPE) -> WRITING_STYLE_TYPE:
    if project_domain in DEFAULT_WRITING_STYLE:
        return DEFAULT_WRITING_STYLE[project_domain]
    return 'Automatic'

_GITHUB_NAME_WITH_OWNER_REGEX = re.compile(r"([a-zA-Z0-9-]+/[a-zA-Z0-9-]+)$")
def to_name_with_owner(repo_url: str) -> str:
    repo_url = repo_url.replace(".git", "")
    _matched = _GITHUB_NAME_WITH_OWNER_REGEX.match(repo_url)
    if not _matched:
        raise ValueError(f"Invalid GitHub repository URL: {repo_url}")
    return _matched.group(1)

def merge_prs(
    pr_commits: dict[int, ReleaseNotePrEntry],
    generated_entry: dict[str, ReleaseNoteEntry],
) -> dict[str, ReleaseNoteEntry]:
    """
    Merge pull request grouped commits into one release note entry.

    :param pr_commits: {pr_number: ReleaseNotePrEntry}
    :param generated_entry: {commit_sha: ReleaseNoteEntry}
    :return: {commit_sha: ReleaseNoteEntry}
    """
    # The commits that constitute the PR and PR details (title and body) which are used to form one entry in the RN documentation.
    merged_entries: dict[str, ReleaseNoteEntry] = {}

    # Merge pull request grouped commits into one release note entry
    for pr in pr_commits:
        # Some PRs were squashed or contain only one commit, skip those.
        if len(pr_commits[pr].commits) == 1:
            continue
        release_note_entries: list[ReleaseNoteEntry] = []
        for commit_sha in pr_commits[pr].commits:  # For each commit in the PR
            if commit_sha in generated_entry:
                release_note_entries.append(generated_entry[commit_sha])
                del generated_entry[commit_sha]  # Remove the commit entry

        mse = release_note_entries[0]  # Most significant entry
        sha_list = []
        commit_pr_set = set()
        for entry in release_note_entries:
            sha_list.append(entry.sha[0])
            commit_pr_set = commit_pr_set.union(entry.associated_prs)
            if entry.significance > mse.significance:
                mse = entry

        if mse.sha[0] not in merged_entries:
            merged_entries[mse.sha[0]] = ReleaseNoteEntry(
                sha_list,
                pr_commits[pr].title,
                mse.type,
                mse.significance,
                commit_pr_set,
                mse.date_time,
                mse.affected_module,
            )
    return merged_entries | generated_entry

def sort_entries_by_significance(
    rn_entries: dict[str, ReleaseNoteEntry]
) -> List[ReleaseNoteEntry]:
    sorted_rn_entries: list[ReleaseNoteEntry] = []
    # Sort in descending order.
    all_rn_entries_list = list(rn_entries.values())
    while len(sorted_rn_entries) < len(rn_entries):
        mse: ReleaseNoteEntry = all_rn_entries_list[0]
        for i in range(len(all_rn_entries_list)):
            current_entry: ReleaseNoteEntry = all_rn_entries_list[i]
            if mse.sha == current_entry.sha:
                continue
            if current_entry.significance > mse.significance:
                mse = current_entry
        sorted_rn_entries.append(mse)
        all_rn_entries_list.remove(mse)
    return sorted_rn_entries

def sort_entries_by_type(
    rn_entries: dict[str, ReleaseNoteEntry]
) -> dict[str, list[ReleaseNoteEntry]]:
    sorted_entries: dict[str, list[ReleaseNoteEntry]] = {}
    for commit_sha in rn_entries:
        rn_entry = rn_entries[commit_sha]
        if rn_entry.type in sorted_entries:
            sorted_entries[rn_entry.type].append(rn_entry)
        else:
            sorted_entries[rn_entry.type] = [rn_entry]

    return sorted_entries
    # # sort the sorted_entries by priority
    # return dict(
    #     sorted(
    #         sorted_entries.items(),
    #         key=lambda item: DEFAULT_COMMIT_CATE_PRIORITY[item[0]],
    #         reverse=True,
    #     )
    # )

def sort_entries_by_module(
    rn_entries: dict[str, ReleaseNoteEntry]
) -> dict[str, list[ReleaseNoteEntry]]:
    sorted_entries: dict[str, list[ReleaseNoteEntry]] = {}
    for commit_sha in rn_entries:
        rn_entry = rn_entries[commit_sha]
        if rn_entry.affected_module in sorted_entries:
            sorted_entries[rn_entry.affected_module].append(rn_entry)
        else:
            sorted_entries[rn_entry.affected_module] = [rn_entry]
    return sorted_entries

# https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting
# We use 72 as that is enough characters to best describe the change.
def get_commit_msg_title(message: str) -> str:
    newline_pos = message.find("\n")
    if (
        newline_pos != -1
    ):  # If there is a newline then return the text before the newline char.
        return message[:newline_pos].strip()
    return message[:72].strip()

# def generate_rn_entries_from_commit_entries(
#     self,
#     commit_pr: dict[str, ReleaseNoteCommitEntry],
#     ignore_merge_commits: bool = True,
# ) -> dict[str, ReleaseNoteEntry]:
#     generated_entry: dict[str, ReleaseNoteEntry] = {}

#     for commit_sha in commit_pr:
#         commit_type, commit_significance = self._commit_analyzer.get_analysis(
#             commit_sha
#         )
#         # Ignore commits which simply merged branches.
#         if ignore_merge_commits and self.is_merge_commit(
#             commit_pr[commit_sha].message
#         ):
#             continue
#         generated_entry[commit_sha] = ReleaseNoteEntry(
#             [commit_sha],
#             self.get_commit_msg_title(commit_pr[commit_sha].message),
#             commit_type,
#             commit_significance,
#             commit_pr[commit_sha].prs,
#             commit_pr[commit_sha].date_time,
#         )
#     return generated_entry

def remove_insignificant_commits(
    rn_entries: dict[str, ReleaseNoteEntry],
    min_significance: float = 0.15,
) -> dict[str, list[ReleaseNoteEntry]]:
    cleaned_entries: dict[str, ReleaseNoteEntry] = {}
    for sha in rn_entries:
        entry = rn_entries[sha]
        if (
            entry.significance >= min_significance
        ):  # ignore commits with a low significance score
            cleaned_entries[sha] = entry
    return cleaned_entries


def get_pr_links(entry: ReleaseNoteEntry, repo_name: str) -> str:
    pr_links = ""
    for pr in entry.associated_prs:
        pr_links += f"[#{pr}](https://github.com/{repo_name}/pull/{pr}) "
    return pr_links

def get_commit_links(entry: ReleaseNoteEntry, repo_name: str) -> str:
    commit_links = ""
    for commit in entry.sha:
        commit_links += f"[{commit[:7]}](https://github.com/{repo_name}/commit/{commit}) "
    return commit_links

def format_entry(entry: ReleaseNoteEntry, repo_name: str, show_significance: bool = False) -> str:
    logger.debug(f"entry: {entry}")
    formatted_rn = f"- {entry.summary.strip()}"

    pr_links = get_pr_links(entry, repo_name)
    if pr_links != "":
        logger.debug(f"pr_links: {pr_links}")
        formatted_rn += f" {pr_links}"
    else:
        commit_links = get_commit_links(entry, repo_name)
        if commit_links != "":
            logger.debug(f"commit_links: {commit_links}")
            formatted_rn += f" {commit_links}"

    if (entry.significance != 0.0) and (show_significance is True):
        formatted_rn += f"(significance={entry.significance:.2f})"

    formatted_rn += "\n"

    logger.debug(f"formatted_rn, nolink: {formatted_rn}")
    return formatted_rn

class ReleaseNoteGenerator:
    def __init__(
            self,
            log_dir: str = './log',
            openai_config: Optional[OpenAIConfig] = None,
    ):
        self._cmta = CommitAnalyzer()
        self._gh_pool = [
            Github(token) for token in settings.GITHUB_TOKENS
        ]
        self._gh = self._gh_pool[0]
        if openai_config is None:
            openai_config = from_dict(OpenAIConfig, {k.lower(): v for k, v in settings.openai.items()})
        self._oai_conf = openai_config
        self._pm = PromptsManager(self._oai_conf)

        self._log_dir = log_dir

    def summarize_commit(
        self,
        sha_combined_tcr: str,
        technical_prompt: bool,
    ) -> str:
        entry_result = self._pm.summarize_commit(sha_combined_tcr, technical_prompt)
        entry_result = self._pm.rewrite_for_conciseness(entry_result)
        return entry_result

    def summarize_pr(
        self,
        release_note_entries: List[ReleaseNoteEntry],
        commit_dt: str,
        pr_title: str,
        pr_body: str,
        technical_prompt: bool,
    ) -> str:
        entry_result = self._pm.summarize_pr(
            release_note_entries, commit_dt, pr_title, pr_body, technical_prompt
        )
        merged_entry_result = self._pm.rewrite_for_conciseness(entry_result)
        return merged_entry_result

    def determine_commit_module(
        self, sha_combined_tcr: str
    ) -> str:
        result = self._pm.determine_commit_module(sha_combined_tcr)
        return result

    def refine_module_categories(self,release_note: str) -> str:
        """
        Refine the module categories in the release note.
        """
        response = self._pm.refine_module_categories(release_note)
        return response
    

    def adjust_for_target(
        self,
        release_note: str,
        project_domain: PROJECT_DOMAIN_TYPE,
        structure_type: STRUCTURE_TYPE,
    ) -> str:
        """
        Adjust the release note based on the project domain and target audience.
        """
        # Rewrite the Release Note based on the project domain and target audience.
        # logger.info("Info (fine-tuning): Rewrite the Release Note based on the project domain and target audience.")
        result = self._pm.rewrite_to_suit_pd(release_note, project_domain, structure_type)
        # Rewrite it while merging similar entries into one.
        # logger.info("Info (fine-tuning): Rewrite it while merging similar entries into one.")
        if structure_type != 'Change Priority':
            result = self._pm.combine_similar_entries(result)

        result = self._pm.rewrite_name_refs(result)
        result = self._pm.rewrite_func_info(result)

        return result

    def collect_dataset(
        self,
        repo_name: str,
        previous_release: str,
        current_release: str,
        group_commits: bool,
        project_domain: PROJECT_DOMAIN_TYPE,
        writing_style: WRITING_STYLE_TYPE,
        structure_type: STRUCTURE_TYPE,
    ):
        # classify the commits
        df_predictions = self._cmta.analyze(
            repo_name, project_domain, previous_release, current_release
        )
        df_predictions['type'] = df_predictions['type'].fillna('').astype(str)

        # collect dataset for RN generation
        commit_raw: dict[str, CommitData] = {}
        tcr_dict, entire_tcr, pr_commits, commit_pr, commit_raw = get_prompt_commits(
                repo_name=repo_name,
                prev_release=previous_release,
                cur_release=current_release,
                use_prs=group_commits,
                gh=self._gh,
                pm=self._pm
            )
        
        if hasattr(self, '_auto_writing_style') and writing_style == 'Expository':
            # see if we need to switch to another style
            _all_messages = []
            for cmt in commit_raw:
                _all_messages.append(commit_raw[cmt].message.splitlines()[0])
            for pr in pr_commits.values():
                _all_messages.append(pr.title)
            _are_msgs_good = self._pm.are_commit_messages_good(_all_messages)
            if _are_msgs_good:
                logger.debug("Messages are good, keeping the Expository style.")
            else:
                logger.info("Messages are not good, switching to the Persuasive style.")
                writing_style = 'Persuasive'
                self._auto_writing_style = 'Persuasive'
        
        use_technical_prompt = writing_style == 'Descriptive'
        # Release note entry by commit
        generated_entry: dict[str, ReleaseNoteEntry] = {}

        # Generate release note entry for every commit
        for sha in tcr_dict:  # For every commit
            try:
                _row = df_predictions.loc[sha]
            except KeyError:
                logger.info(f"Warning: Missing commit prediction for {sha}")
                continue

            commit_type: CONVENTIONAL_COMMITS_TYPE = _row['type'] if _row['type'] else _row['label']
            commit_significance: float = float(_row['includeConfidence'])

            if sha in generated_entry:
                logger.info(f"Warning: Duplicated commit in release note entry: {sha}")
                continue

            if (writing_style == 'Expository') and (structure_type != 'Affected Module'):
                entry_result = get_commit_msg_title(commit_raw[sha].message)

                associated_prs = commit_pr.get(sha, set())
                generated_entry[sha] = ReleaseNoteEntry(
                    [sha],
                    entry_result,
                    commit_type,
                    commit_significance,
                    associated_prs,
                    commit_raw[sha].author_date,
                )
            else:
                sha_combined_tcr = ""
                _ntokens = 0

                for tcr in tcr_dict[sha]:  
                    # For every file change in that commit up to the max string or context length.
                    _str_len = len(sha_combined_tcr) + len(tcr)
                    _ntokens += self._pm.count_tokens(tcr)
                    _max_str_len = self._oai_conf.max_string_length
                    _max_ntokens = max(self._oai_conf.max_model_context_length, self._oai_conf.tpm)
                    if (_ntokens > _max_ntokens) or (_str_len > _max_str_len):
                        logger.warning(
                            f"Commit {sha} patch exceeding max length: "
                            f"({_str_len}/{_max_str_len} chars, {_ntokens}/{_max_ntokens} tokens)"
                        )
                        # This event is unlikely unless there is a massive refactor or project restructing, 
                        # in which case we argue that this commit shouldn't be part of the release anyway.
                        break
                    sha_combined_tcr += tcr

                # Send Commit to OpenAI
                if len(sha_combined_tcr) != 0:
                    entry_result: str = ""
                    if writing_style == 'Expository':
                        entry_result = get_commit_msg_title(commit_raw[sha].message)
                    else:
                        entry_result = self.summarize_commit(
                            sha_combined_tcr,
                            use_technical_prompt,
                        )
                    
                    associated_prs = commit_pr.get(sha, set())
                    affected_module: str = ""
                    if structure_type == 'Affected Module':
                        affected_module = self.determine_commit_module(sha_combined_tcr)
                    generated_entry[sha] = ReleaseNoteEntry(
                        [sha],
                        entry_result,
                        commit_type,
                        commit_significance,
                        associated_prs,
                        commit_raw[sha].author_date,
                        affected_module,
                    )

        return generated_entry, pr_commits, df_predictions

    @logger.catch(reraise=True)
    def generate(
        self,
        repo_name: str,
        project_domain: PROJECT_DOMAIN_TYPE,
        previous_release: str,
        current_release: str,
        group_commits: bool = True,
        writing_style: WRITING_STYLE_TYPE = 'Automatic',
        structure_type: STRUCTURE_TYPE = 'Change Type',
        min_significance: float = 0.15,
        show_significance: bool = False
    ) -> str:
        
        # logging helper
        _task_id = f"{repo_name.split('/')[-1]}_{previous_release}_{current_release}_{time.strftime('%m%d%H%M%S')}"
        _results_path = Path(self._log_dir) / _task_id
        os.makedirs(_results_path, exist_ok=True)
        _logger_sinkid = logger.add(_results_path / 'generator.log', colorize=False, level="DEBUG")

        # print config
        logger.info(f"Parameters: repo_name={repo_name}, project_domain={project_domain}, "
                    f"previous_release={previous_release}, current_release={current_release}, "
                    f"group_commits={group_commits}, writing_style={writing_style}, "
                    f"structure_type={structure_type}, min_significance={min_significance}")
        
        if project_domain == 'Automatic':
            try:
                gh_repo = self._gh.get_repo(repo_name)
            except GithubException as e:
                if e.status == 404:
                    logger.error(f"Repository '{repo_name}' not found (404).")
                    exit()
                else:
                    logger.error(f"GitHub API error: {e.status} - {e.data.get('message')}")
                    exit()
            # get description and readme
            repo_desc = gh_repo.description
            repo_readme = ""
            try:
                repo_readme = gh_repo.get_readme().decoded_content.decode()
            except UnknownObjectException as e:
                if e.status == 404:
                    logger.error(f"No README found for repository '{gh_repo.full_name}', unable to automatically determine project domain. Please re-run and manually specify the domain.")
                    exit()
                else:
                    raise  # re-raise if it's not a 404
            # send for classification
            project_domain = self._pm.determine_project_domain(repo_desc, repo_readme)
        
        if writing_style == 'Automatic':
            writing_style = get_writing_style(project_domain)
            # TODO: this is utterly stupid and should be refactored
            self._auto_writing_style = writing_style
        
        generated_entry, pr_commits, df_predictions = self.collect_dataset(
            repo_name,
            previous_release,
            current_release,
            group_commits,
            project_domain,
            writing_style,
            structure_type,
        )

        if hasattr(self, '_auto_writing_style') and writing_style == 'Expository':
            writing_style = self._auto_writing_style

        if df_predictions is not None and not df_predictions.empty:
            df_predictions.to_csv(_results_path / 'predictions.csv')

        use_technical_prompt = writing_style == 'Descriptive'
        logger.info("Use technical prompt: ", use_technical_prompt)

        merged_entries: dict[
            str, ReleaseNoteEntry
        ] = {}  # The commits that constitute the PR and PR details (title and body) which are used to form one entry in the RN documentation.

        if group_commits:
            logger.info("Grouping commits by PR and summarising message.")
            # Merge pull request grouped commits into one release note entry
            for pr in pr_commits:
                # Some PRs were squashed or contain only one commit, skip those.
                if len(pr_commits[pr].commits) == 1:
                    continue
                release_note_entries: list[ReleaseNoteEntry] = []
                for commit_sha in pr_commits[pr].commits:  # For each commit in the PR
                    if commit_sha in generated_entry:
                        release_note_entries.append(generated_entry[commit_sha])
                        del generated_entry[commit_sha]  # Remove the commit entry

                merged_entry_result: str = ""
                if writing_style == 'Expository':
                    merged_entry_result = pr_commits[pr].title
                else:
                    # Call chatgpt to merge several release note entries into one entry
                    merged_entry_result = self.summarize_pr(
                        release_note_entries,
                        pr_commits[pr].date_time,
                        pr_commits[pr].title,
                        pr_commits[pr].body,
                        use_technical_prompt,
                    )

                if len(release_note_entries) == 0:
                    continue

                # Save the merged release note entries (which constitutes the PR) in merged_entries.
                mse = release_note_entries[0]  # Most significant entry
                sha_list = []
                commit_pr_set = set()
                for entry in release_note_entries:
                    sha_list.append(entry.sha[0])
                    commit_pr_set = commit_pr_set.union(entry.associated_prs)
                    if entry.significance > mse.significance:
                        mse = entry

                if mse.sha[0] in merged_entries:
                    logger.warning(f"Duplicated commit in release note MERGED entry: {mse.sha[0]}")
                else:
                    merged_entries[mse.sha[0]] = ReleaseNoteEntry(
                        sha_list,
                        merged_entry_result,
                        mse.type,
                        mse.significance,
                        commit_pr_set,
                        mse.date_time,
                        mse.affected_module,
                    )

        logger.info("Generating release note file.")
        all_rn_entries = merged_entries | generated_entry

        # pretty print the entries
        for k, v in all_rn_entries.items():
            logger.debug(f"{k}: {v}")

        # logger.info("Removing insignificant commits.")
        # all_rn_entries = remove_insignificant_commits(
        #     all_rn_entries, 
        #     min_significance
        # )

        if (len(all_rn_entries) == 0):
            logger.info("Warning: There are no changes in this release. Exiting early.")
            return
        if (len(all_rn_entries) < 10):
            logger.info("Warning: Ignoring minimum significance threshold because the commit list is sparse.")
        else:
            logger.info("Removing insignificant commits.")
            min_sig_threshold = min_significance

            while(True):
                cleaned_rn_entries = remove_insignificant_commits(
                    all_rn_entries, min_sig_threshold
                )
                if (min_sig_threshold == 0.0 and len(cleaned_rn_entries) == 0):
                    logger.warning("There are no commits even after at minimum significance threshold to 0. "
                                   "Exiting early.")
                    return

                if (len(cleaned_rn_entries) == 0):
                    min_sig_threshold -= 0.05
                if (min_sig_threshold < 0.0):
                    min_sig_threshold = 0.0
                logger.warning(f"There are no commits left after removing insignificant commits, "
                               f" reducing minimum significance threshold to {min_sig_threshold:.2f}")

                if (len(cleaned_rn_entries) > 0):
                    all_rn_entries = cleaned_rn_entries
                    break

        for k, v in all_rn_entries.items():
            logger.debug(f"{k}: {v}")

        logger.info("Sorting release note entries.")
        formatted_rn = f"# {current_release}\n"
        logger.debug(f"structure_type: {structure_type}")
        if structure_type == 'Plain List':
            for entry in all_rn_entries:
                formatted_rn += format_entry(all_rn_entries[entry], repo_name, show_significance)
        elif structure_type == 'Change Priority':
            sorted_rn_entries: list[ReleaseNoteEntry] = (
                sort_entries_by_significance(all_rn_entries)
            )
            for entry in sorted_rn_entries:
                _ent = format_entry(entry, repo_name, show_significance)
                formatted_rn += _ent
        elif structure_type == 'Change Type':
            sorted_entries: dict[str, list[ReleaseNoteEntry]] = (
                sort_entries_by_type(all_rn_entries)
            )
            logger.debug(f"sorted_entries: {sorted_entries}")
            for commit_type in sorted_entries:
                formatted_rn += f"## {DEFAULT_COMMIT_CATE_TO_EMOJI[commit_type]} {commit_type}\n"
                for rn_entry in sorted_entries[commit_type]:
                    formatted_rn += format_entry(rn_entry, repo_name, show_significance)
        elif structure_type == 'Affected Module':
            sorted_entries: dict[str, list[ReleaseNoteEntry]] = (
                sort_entries_by_module(all_rn_entries)
            )
            for module in sorted_entries:
                formatted_rn += f"## {module}\n"
                for rn_entry in sorted_entries[module]:
                    formatted_rn += format_entry(rn_entry, repo_name, show_significance)
            formatted_rn = self.refine_module_categories(formatted_rn)
        else:
            raise ValueError(f"Unknown structure type: {structure_type}")

        logger.info("Adjusting for target.")
        if writing_style != 'Expository':
            formatted_rn = self.adjust_for_target(
                formatted_rn, project_domain, structure_type
            )

        # reorder the change types
        if structure_type == 'Change Type':
            formatted_rn = self._pm.reorder_rn_categories(formatted_rn)

        # find significance items and wrap them in a span
        if (show_significance):
            formatted_rn = re.sub(
                r"\(significance=[0-9.]+\)", lambda m: f"<span style='color:grey;'>{m.group(0)}</span>", formatted_rn
            )

        with open(_results_path / 'release_note.md', 'w') as f:
            f.write(formatted_rn)
        logger.info(f"Release note generated: {_results_path / 'release_note.md'}")

        # remove the logger sink
        logger.remove(_logger_sinkid)

        return formatted_rn



if __name__ == '__main__':
    import argparse
    import loguru
    import sys
    import time
    from .config import get_path

    argparser = argparse.ArgumentParser(description="Generate release notes from a GitHub repository")
    argparser.add_argument("repo_url", type=str, help="URL of the GitHub repository")
    argparser.add_argument("--previous-release", type=str, help="Previous release tag", default=None)
    argparser.add_argument("--current-release", type=str, help="Current release tag", default=None)
    argparser.add_argument("--project-domain", type=str, help="Project domain", default='Automatic')
    argparser.add_argument("--group-commits", required=False, help="Group commits by PR", default=False, action='store_true')
    argparser.add_argument("--writing-style", type=str, required=False, help="Writing style", default="Automatic")
    argparser.add_argument("--structure-type", type=str, required=False, help="Structure type", default="Change Type")
    argparser.add_argument("--min-significance", type=float, required=False, help="Minimum significance score of commits", default=0.15)
    argparser.add_argument("--show-significance", required=False, help="Show the significance score in the generated release note", default=False, action='store_true')
    args = argparser.parse_args()

    # assert args.project_domain in settings.categories.project_domains, \
    #     f"Invalid project domain: {args.project_domain}, must be one of {settings.categories.project_domains}"
    
    # _task_id = args.repo_url.split('/')[-1] + "_" + args.current_release + "_" + time.strftime("%m%d%H%M%S")
    # _base_path = get_path('results') / _task_id

    # FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | " \
    #          "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"
    
    # def format_message(record) -> str:
    #     if len(record['message']) > 1000:
    #         record['message'] = record['message'][:500] + "..." + \
    #         f"{len(record['message']) - 1000} more characters ..." + \
    #         record['message'][-500:]
    #     return FORMAT.format(**record)
    # logger.remove()
    # logger.add(sys.stderr, format=format_message, level="DEBUG")
    # logger.add(_base_path / 'generator.log', colorize=False, level="DEBUG")

    init_env('repo')
    gh = Github(settings.GITHUB_TOKEN)
    rngen = ReleaseNoteGenerator(log_dir=get_path('results'))

    rn = rngen.generate(
            repo_name=args.repo_url,
            project_domain=args.project_domain,
            previous_release=args.previous_release,
            current_release=args.current_release,
            group_commits=args.group_commits,
            writing_style=args.writing_style,
            structure_type=args.structure_type,
            min_significance=args.min_significance,
            show_significance=args.show_significance
    )

    print(rn)