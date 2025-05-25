import logging
import re
from typing import Literal, Optional, Tuple, List
from subprocess import check_output
from math import log
import pandas as pd
import numpy as np
import git
import os
from tqdm import tqdm
from semver import VersionInfo
from pydriller import Repository, ModificationType
from loguru import logger

from languages import infer_langids_onehot, get_lang_names


# strip everything before the occurance of \d+\.
def _strip_version(s):
    # if s is not str, e.g. 1.0
    if not isinstance(s, str):
        return str(s)
    return re.sub(r'^.*?(\d+\..*)$', r'\1', s)


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
        logger.debug(f"Error in parsing version: {prev_version}, {new_version}, leave as Unknown")
        return "Unknown"
    

CONVENTIONAL_REGEX = re.compile(r'^([a-z]+)[:\(].*')
CONVENTIONAL_CATES = {'build', 'chore', 'ci', 'docs', 'feat', 'fix', 'perf', 'refactor', 'revert','style', 'test'}
def parse_commit_message(
    message: str
) -> Tuple[Optional[str], str]:
    """A naive parser for conventional commit messages."""
    _match = CONVENTIONAL_REGEX.match(message)
    if _match and _match.group(1) in CONVENTIONAL_CATES:
        _type = _match.group(1)
        if len(message) <= _match.end(1) + 1:
            return _type, ''
        _message = message[_match.end(1):]
        if _message[0] == '(':  # scoped, like feat(scope): message
            _next = max(_message.find(')') + 2, 1)
        elif _message[0] == ':':  # no scope, like feat: message
            _next = 1
        else:
            return _type, _message
        return _type, _message[_next:].strip()        
    return None, message

MERGE_REGEX = re.compile(r'Merge pull request #\d+ from')
def is_merge_commit(
    message: str
) -> bool:
    return MERGE_REGEX.match(message) is not None

SHA_REGEX = re.compile(r'[0-9a-f]{7-40}')
def process_releases(
        repo: git.Repo,
        releases: List[dict],
):
    _releases = []
    for rel in releases:
        try:
            _commit = repo.commit(rel['tag'])  # rev-parse
        except Exception as e:
            if SHA_REGEX.match(rel['target']):
                _commit = repo.commit(rel['target'])
            else:
                logger.error(f'Error in {os.path.basename(repo.working_dir)}: {e}')
                continue
        
        _sha = _commit.hexsha
        _date = _commit.authored_datetime
        _releases.append({
            'tag': rel['tag'],
            'sha': _sha,
            'tagAuthoredAt': _date,
            'releaseCreatedAt': rel['createdAt'],
        })

    return pd.DataFrame(
            _releases, columns=['tag', 'sha', 'tagAuthoredAt', 'releaseCreatedAt']
        ).sort_values('releaseCreatedAt', ascending=False).set_index('sha')


def get_commit_stats(
    repo: git.Repo,
    df_releases: pd.DataFrame,
) -> pd.DataFrame:
    repo_name = os.path.basename(repo.working_dir)
    logger.warning(f"Found {len(df_releases)} releases in {repo_name}")
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
                repo.working_dir, from_commit=_from_sha, to_commit=_to_sha, order="reverse"
            )
            _commits = list(repo_miner.traverse_commits())
            _l_commits = []

            logger.info(
                f"{repo_name}: Analyzing "
                f"{_prev_tag_name}...{_tag_name} ({i+1}/{len(df_releases)-1}): {len(_commits)} commits"
            )
            
            # CodeChurn
            renamed_files = {}
            file_edit_lines = {}
            # ChangeSet
            n_files = []
            # HistoryComplexity
            file_edit_entropy = {}
            # uniqueAuthors
            commit_authors = set()

            for commit in tqdm(_commits, desc=f"{_prev_tag_name}...{_tag_name}"):
                try:
                    _adds = 0
                    _dels = 0
                    _filenames = []

                    for modified_file in commit.modified_files:
                        # CodeChurn
                        filepath = renamed_files.get(modified_file.new_path, modified_file.new_path)
                        if modified_file.change_type == ModificationType.RENAME:
                            renamed_files[modified_file.old_path] = filepath
                        churn = modified_file.added_lines + modified_file.deleted_lines
                        file_edit_lines.setdefault(filepath, []).append(churn)
                        # ModLines
                        _adds += modified_file.added_lines
                        _dels += modified_file.deleted_lines
                        # LangEdited
                        _filenames.append(filepath if filepath else modified_file.old_path)
                    
                    # ChangeSet
                    n_files.append(len(commit.modified_files))

                    # authors
                    commit_authors.add(commit.author.name)

                    # langs
                    _langids = infer_langids_onehot([f.split('/')[-1] for f in _filenames])
                    # transform to dict
                    langs = {k: v for k, v in zip(_lang_names, _langids)}

                    _l_commits.append({
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
                            **langs
                        })
                except Exception as e:
                    logger.error(f"Error in {repo_name} - {commit.hash}: {e}")

            # if empty
            if len(_l_commits) == 0:
                logger.warning(f"No commits in {repo_name} - {_prev_tag_name}...{_tag_name}")
                continue

            df_commits = pd.DataFrame(_l_commits).convert_dtypes().set_index('sha')
            release_stats = pd.Series()
            # ReleaseType
            release_stats['releaseTag'] = _tag_name
            release_stats['releaseType'] = infer_release_type(_prev_tag_name, _tag_name)
            
            # uniqueAuthors
            release_stats['releaseAuthors'] = len(commit_authors)

            # number of commits
            release_stats['releaseCommits'] = len(_l_commits)

            # ChangeSet
            release_stats['avgChangeset'] = np.mean(n_files) if len(n_files) > 0 else 0

            # CodeChurn
            _codechurns = [np.mean(v) for v in file_edit_lines.values() if len(v) > 0]
            release_stats['avgCodeChurn'] = np.mean(_codechurns) if len(_codechurns) > 0 else 0

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
                entropy = -sum(p*log(p+1/1e10, n_files) for p in file_edit_entropy.values())
            for filepath in file_edit_entropy:
                file_edit_entropy[filepath] *= entropy
                file_edit_entropy[filepath] = round(file_edit_entropy[filepath] * 100, 2)
            release_stats['avgHistoryComplexity'] = np.mean(list(file_edit_entropy.values())) if len(file_edit_entropy) > 0 else 0

            # set release stats
            df_commits = df_commits.assign(**release_stats)

            _l_releases.append(df_commits)
        
        except Exception as e:
            logger.error(f"Error in {repo_name} - {df_releases.iloc[i]['tag']}: {e}", exc_info=True)

    return pd.concat(_l_releases) if len(_l_releases) > 0 else pd.DataFrame()