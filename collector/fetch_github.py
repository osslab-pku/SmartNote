import re
import os
import git
import shutil
from tqdm import tqdm
from github import Github, GithubException
from loguru import logger

def clone_repo(
    url: str,
    dest_dir: str,
    branch=None,
    force=False,
    proxy=None,
):
    # if url is name with owner, it is a github repo
    if re.match(r'^[\w-]+/[\w._-]+$', url):
        url = f'https://github.com/{url}'
    config=f"http.proxy={proxy}" if proxy else None
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
        git.Repo.clone_from(url, dest_dir, branch=branch, config=config, allow_unsafe_options=True)
    except Exception as e:  # can also be AttributeError, ...
        try:
            # remove the corrupted repo and try again
            logger.error(f"Error cloning {url}: {e}")
            if os.path.exists(dest_dir):
                shutil.rmtree(dest_dir)
            git.Repo.clone_from(url, dest_dir, branch=branch, config=config, allow_unsafe_options=True)
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
        logger.error(f"{repo}: {e}")
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
        for release in tqdm(releases, desc="Fetching releases", total=releases.totalCount):
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