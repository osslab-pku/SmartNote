# %%
from config import init_env, settings

init_env("repo", cuda_devices=3)

import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

# %%
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# %%
from fetch_github import *
from calculate_stats import *
from github import Github
from typing import Literal
import numpy as np
import git
from loguru import logger

def collect_features(name_with_owner: str, domain: Literal['Application', 'Library', 'System', 'Tool']) -> pd.DataFrame:
    url = f"https://github.com/{name_with_owner}"
    dest_dir = settings.CACHE_PATH / name_with_owner.replace("/", "_")
    clone_repo(url, dest_dir)

    gh = Github(settings.GITHUB_TOKEN)
    repo = git.Repo(dest_dir)

    _repo_stats = get_stats_ghapi(gh, name_with_owner)
    _releases = get_release_dates(gh, name_with_owner)
    
    if len(_releases) == 0:
        return pd.DataFrame()
    
    df_releases = process_releases(repo, _releases)
    df_commits = get_commit_stats(repo, df_releases)

    del _repo_stats['name']
    _repo_stats['domain'] = domain
    df_commits = df_commits.assign(**_repo_stats)

    df_commits[['type', 'body']] = \
        df_commits['message'].apply(lambda x: pd.Series(parse_commit_message(x), index=['type', 'body']))

    df_commits['isMergeCommit'] = df_commits['message'].apply(is_merge_commit)
    df_commits.reset_index(inplace=True)
    df_commits.drop(columns=['files', 'message'], inplace=True)
    return df_commits
# %%
import xgboost as xgb
from sklearn.metrics import classification_report

clf = xgb.XGBClassifier(
        objective="multi:softmax",
        tree_method="hist", 
        enable_categorical=True, 
        device="cuda",
        eval_metric="mlogloss",
        random_state=settings.SEED,
        early_stopping_rounds=10,
    )

clf.load_model('../models/cls_gte_xgb/xgb_gridsearch_best.json')
clf

# %%
flt = xgb.XGBClassifier(
    objective="binary:logistic",
    tree_method="hist", 
    enable_categorical=True, 
    device="cuda",
    eval_metric="logloss",
    early_stopping_rounds=10,
    random_state=settings.SEED,
)

flt.load_model('../models/flt_gte_xgb/xgb_gridsearch_best.json')
flt

# %%
import torch
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

# why gte?
# 1. top 20 on mteb classification https://huggingface.co/BAAI/bge-base-en-v1.5
# 2. very small model (137M parameters) for fast training and inference
model_path = 'Alibaba-NLP/gte-base-en-v1.5'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True)\
    .to(settings.TORCH_DEVICE)
model.eval()

# %%
settings.BATCH_SIZE = 32

# %%
from sklearn.preprocessing import LabelEncoder

_encode_releaseType = LabelEncoder()
_encode_releaseType.fit(settings.categories.release_types)

_encoder_domain = LabelEncoder()
_encoder_domain.fit(settings.categories.project_domains)

_encoder_type = LabelEncoder()
_encoder_type.fit(settings.categories.conventional_commits)

# %%
def get_embeddings(df_s):
    with torch.no_grad():
        _df_embs = []
        # chunk df['body']
        for _texts in tqdm(np.array_split(
            df_s, len(df_s) // settings.BATCH_SIZE), desc="Embedding messages"):
            _texts = _texts.tolist()
            batch_dict = tokenizer(
                _texts, max_length=8192, padding=True, truncation=True, return_tensors='pt'
            ).to(settings.TORCH_DEVICE)
            outputs = model(**batch_dict)
            embeddings = outputs.last_hidden_state[:, 0].cpu().detach().numpy()
            _df_embs.append(embeddings)
    _df = pd.concat(
        [pd.DataFrame(_embs) for _embs in _df_embs], 
        ignore_index=True,
    )
    # set column names
    _df.columns = [f'emb{i}' for i in range(_df.shape[1])]
    # clean up
    del _df_embs
    torch.cuda.empty_cache()
    return _df

# # %%
# def worker(name_with_owner: str, domain: Literal['Application', 'Library', 'System', 'Tool']) -> pd.DataFrame:
#     _output_path = settings.DATASETS_PATH / f'eval_{name_with_owner.replace("/", "_")}.parquet'

#     if _output_path.exists():
#         return
    
#     df_commits = collect_features(name_with_owner, domain)
#     if len(df_commits) == 0:
#         return
    
#     df_embs = get_embeddings(df_commits['body'])
#     df_ds = pd.concat([df_commits, df_embs], axis=1)\
#         .drop(columns=['nameWithOwner', 'sha', 'authorName', 'authorEmail', 'date', 'releaseTag', 'body'])

#     df_ds['releaseType'] = pd.Series(_encode_releaseType.transform(df_ds['releaseType'])).astype('category')
#     df_ds['domain'] = pd.Series(_encoder_domain.transform(df_ds['domain'])).astype('category')

#     y_pred = clf.predict(df_ds.drop(columns=['type']))
#     df_commits['predictedType'] = _encoder_type.inverse_transform(y_pred)
#     df_commits['predictedScore'] = flt.predict_proba(df_ds.drop(columns=['type']))[:, 1]

#     df_commits.to_parquet(_output_path)

# %%
import multiprocess
from tqdm.auto import tqdm

df_repos = pd.read_csv(settings.DATASETS_PATH / 'eval_gh_repos.csv')
repos = df_repos['URL'].apply(lambda x: '/'.join(x.split('/')[-2:])).tolist()
domains = df_repos['Project Domain'].tolist()

# map full domaains to short domains
_map = {
    'Application Software': 'Application',
    'System Software': 'System',
    'Libraries & Frameworks': 'Library',
    'Software Tool': 'Tool'
}
domains = [_map[_] for _ in domains]

for name_with_owner, domain in zip(repos, domains):
    _output_path = settings.DATASETS_PATH / f'eval_{name_with_owner.replace("/", "_")}.parquet'

    if _output_path.exists():
        continue
    
    df_commits = collect_features(name_with_owner, domain)
    if len(df_commits) == 0:
        continue
    
    df_embs = get_embeddings(df_commits['body'])
    X = pd.concat([df_commits, df_embs], axis=1)\
        .drop(columns=['nameWithOwner', 'sha', 'authorName', 'authorEmail', 'date', 'releaseTag', 'body'])
    
    X['releaseType'] = pd.Series(_encode_releaseType.transform(X['releaseType'])).astype('category')
    X['domain'] = pd.Series(_encoder_domain.transform(X['domain'])).astype('category')

    # align the order of features with the models
    X = X[clf.get_booster().feature_names]

    y_pred = clf.predict(X)
    df_commits['predictedType'] = _encoder_type.inverse_transform(y_pred)
    df_commits['predictedScore'] = flt.predict_proba(X)[:, 1]

    df_commits.to_parquet(_output_path)

    # calculate accuracy
    _df = df_commits[df_commits['type'].notna()]
    if len(_df) == 0:
        continue
    logger.info(f"Accuracy for {name_with_owner}: {(_df['type'] == _df['predictedType']).mean()}")

