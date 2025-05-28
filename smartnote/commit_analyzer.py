import os
from typing import Optional
from github import Github
from tqdm import tqdm
import pandas as pd
from loguru import logger
import torch

from .dtypes import CONVENTIONAL_COMMITS_TYPE, PROJECT_DOMAIN_TYPE, RELEASE_TYPE, WRITING_STYLE_TYPE, STRUCTURE_TYPE
from .dtypes import ReleaseNoteEntry, ReleaseNotePrEntry, ReleaseNoteCommitEntry, PersonalizationConfig
from .config import settings, init_env
from .embedder import SentenceEmbedder
from .collector import collect_commits
from .classifier import XGBoostCommitFilter, XGBoostCommitClassifier

_ablate_release_type = True

class CommitAnalyzer:
    def __init__(self):
        """
        Initialize CommitAnalyzer object.
        """
        self._flt = XGBoostCommitFilter(
            model_path=settings.rngen.flt_model_path, 
        )
        self._cls = XGBoostCommitClassifier(
            model_path=settings.rngen.cls_model_path, labels=settings.categories.conventional_commits
        )
        self._emb = SentenceEmbedder(**settings.embed)

    def analyze(self, 
            repo_url: str,
            project_domain: PROJECT_DOMAIN_TYPE,
            previous_release: Optional[str],
            current_release: Optional[str],
    ):
        """
        Analyze commits between two releases and predict the type and significance of each commit.

        :param repo_url: URL of the GitHub repository.
        :param project_domain: Project domain, one of Application, System, Library, Tool.
        :param previous_release: Previous release tag. If None, the first release will be used.
        :param current_release: Current release tag. If None, the latest release will be used.
        :return: DataFrame containing the predictions for each commit.
          (columns: sha, type, body, isMergeCommit, mergeFrom, label, labelConfidence, includeConfidence).
        """

        df_commits = collect_commits(
            repo_url, 
            project_domain=project_domain,
            prev_release=previous_release,
            cur_release=current_release
        )
        global _ablate_release_type
        if _ablate_release_type:
            df_commits['releaseType'] = 'Unknown'
        if df_commits.empty:
            logger.warning(f"Skipping {repo_url}")
            return
        df_emb = self._emb.encode(df_commits['body'])
        df_commits = pd.concat([df_commits, df_emb], axis=1)
        df_X = self._flt.transform(df_commits)

        _flt_labels = pd.DataFrame(self._flt.predict_proba(df_X)[:, 1], columns=['includeConfidence'])
        _cls_labels = pd.DataFrame(self._cls.predict_labels(df_X), columns=['label', 'labelConfidence'])
        _predictions = pd.concat([_flt_labels, _cls_labels, df_commits[['sha', 'type', 'body', "isMergeCommit", 'mergeFrom']]], axis=1)
        _predictions.set_index('sha', inplace=True)
        if not all(_predictions['type'].isna()):
            # calculate the accuracy of the labels
            _accuracy = (_predictions['type'] == _predictions['label']).sum() / sum(~_predictions['type'].isna())
            logger.debug(f"Accuracy of labels: {_accuracy}")
        logger.debug(f"Predictions:\n {_predictions}")
        
        # # save the predictions for debugging
        # _fname = '_'.join(repo_url.split('/')[-2:])
        # if previous_release is not None:
        #     _fname += f'_{previous_release}_{current_release}'
        # _predictions.to_csv(settings.CACHE_PATH / f'{_fname}.csv')

        return _predictions

if __name__ == '__main__':
    import argparse

    init_env('repo')
    gh = Github(settings.GITHUB_TOKEN)
    cmta = CommitAnalyzer()

    argparser = argparse.ArgumentParser(description="Analyze commits between two releases")
    argparser.add_argument("repo_url", type=str, help="URL of the GitHub repository")
    argparser.add_argument("project_domain", type=str, help="Project domain")
    argparser.add_argument("previous_release", type=str, nargs='?', help="Previous release tag", default=None)
    argparser.add_argument("current_release", type=str, nargs='?', help="Current release tag", default=None)
    args = argparser.parse_args()

    # a magic entry point to run the analyzer on all repositories
    if (args.repo_url == 'eval') and (args.project_domain == 'all'):
        logger.info("Running the analyzer on all evaluation repositories")

        df_repos = pd.read_csv(settings.DATASETS_PATH / 'eval_gh_repos.csv')
        repos = df_repos['URL'].apply(lambda x: '/'.join(x.split('/')[-2:])).tolist()
        domains = df_repos['Project Domain'].tolist()

        # map full domains to short domains
        _map = {
            'Application Software': 'Application',
            'System Software': 'System',
            'Libraries & Frameworks': 'Library',
            'Software Tool': 'Tool'
        }
        domains = [_map[_] for _ in domains]

        for name_with_owner, domain in zip(repos, domains):
            cmta.analyze(name_with_owner, domain, None, None)
        exit(0)

    assert args.project_domain in settings.categories.project_domains, \
        f"Invalid project domain: {args.project_domain}, must be one of {settings.categories.project_domains}"

    cmta.analyze(
        repo_url=args.repo_url, 
        previous_release=args.previous_release, 
        current_release=args.current_release, 
        project_domain=args.project_domain
    )