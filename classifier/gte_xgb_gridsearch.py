# %%
from config import init_env, settings
init_env(name='cls_gte_xgb', cuda_devices=1)
settings.MODEL_NAME = 'Alibaba-NLP/gte-base-en-v1.5'
settings.MODELS_PATH

# %%
import pandas as pd

df_commits = pd.read_parquet(settings.DATASETS_PATH / 'dataset_cls.parquet')
df_repos = pd.read_csv(settings.DATASETS_PATH / 'repos_cls.csv', on_bad_lines='skip')
print(df_commits.shape, df_repos.shape)
df_commits

# %%
LABEL_COL = 'type'
# count distinct
NUM_LABELS = len(df_commits[LABEL_COL].unique())
# select columns starting with 'lang'
CATE_COLS = ['domain', 'releaseType']
# columns with type 'number' or 'bool'
NUM_COLS = df_commits.select_dtypes(include=['number', 'bool']).columns.tolist()
# drop isInRN from NUM_COLS
NUM_COLS.remove('isInRN')

(LABEL_COL, NUM_LABELS, CATE_COLS, NUM_COLS)

# %%
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

# why gte?
# 1. top 20 on mteb classification https://huggingface.co/BAAI/bge-base-en-v1.5
# 2. very small model (137M parameters) for fast training and inference
model_path = 'Alibaba-NLP/gte-base-en-v1.5'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).to(settings.TORCH_DEVICE)
model

# %%
# Sanity check
input_texts = [
    "what is the capital of China?",
    "how to implement quick sort in python?",
    "Beijing",
    "sorting algorithms"
]
batch_dict = tokenizer(
    input_texts, max_length=8192, padding=True, truncation=True, return_tensors='pt'
).to(settings.TORCH_DEVICE)
outputs = model(**batch_dict)
embeddings = outputs.last_hidden_state[:, 0]
 
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
scores

# %%
import numpy as np
import torch
import os
from tqdm.auto import tqdm

settings.BATCH_SIZE = 320
model.eval()

if os.path.exists(settings.CACHE_PATH / 'df_embs.parquet'):
    df_embs = pd.read_parquet(settings.CACHE_PATH / 'df_embs.parquet')
    print(df_embs.shape)
else:
    with torch.no_grad():
        _df_embs = []
        # chunk df['body']
        for _texts in tqdm(np.array_split(
            df_commits['body'], len(df_commits) // settings.BATCH_SIZE)):
            _texts = _texts.tolist()
            batch_dict = tokenizer(
                _texts, max_length=8192, padding=True, truncation=True, return_tensors='pt'
            ).to(settings.TORCH_DEVICE)
            outputs = model(**batch_dict)
            embeddings = outputs.last_hidden_state[:, 0].cpu().detach().numpy()
            _df_embs.append(embeddings)

    # concatenate all embeddings
    df_embs = pd.concat([pd.DataFrame(_embs) for _embs in _df_embs], ignore_index=True)
    # name the columns: emb0, emb1, ..., emb767
    df_embs.columns = [f'emb{i}' for i in range(df_embs.shape[1])]
    df_embs.to_parquet(settings.CACHE_PATH / 'df_embs.parquet', index=False)
df_embs

# %%
# naive split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# _df_cls = pd.read_parquet('../temp/cls_bge_emb.parquet')
df_ds = pd.concat([df_commits, df_embs], axis=1)\
    .drop(columns=['nameWithOwner', 'sha', 'authorName', 'authorEmail', 'date', 'releaseTag', 'body', 'isInRN'])

_encoder_type = LabelEncoder()
_encoder_type.fit(settings.categories.conventional_commits)
df_ds['type'] = pd.Series(_encoder_type.transform(df_ds['type'])).astype('category')

_encode_releaseType = LabelEncoder()
_encode_releaseType.fit(settings.categories.release_types)
df_ds['releaseType'] = pd.Series(_encode_releaseType.transform(df_ds['releaseType'])).astype('category')

_encoder_domain = LabelEncoder()
_encoder_domain.fit(settings.categories.project_domains)
df_ds['domain'] = pd.Series(_encoder_domain.transform(df_ds['domain'])).astype('category')

ds_train, ds_test = train_test_split(
    df_ds, test_size=0.3, random_state=settings.seed, stratify=df_ds['type']
)
ds_test, ds_valid = train_test_split(
    ds_test, test_size=0.33, random_state=settings.seed, stratify=ds_test['type']
)

# ds_train.to_parquet('../temp/cls_train.parquet')
# ds_test.to_parquet('../temp/cls_test.parquet')
# ds_valid.to_parquet('../temp/cls_valid.parquet')

X_train, y_train = ds_train.drop(columns=['type']), ds_train['type']
X_test, y_test = ds_test.drop(columns=['type']), ds_test['type']
X_valid, y_valid = ds_valid.drop(columns=['type']), ds_valid['type']

print(ds_train.shape, ds_test.shape, ds_valid.shape)

# %%
import xgboost as xgb
from sklearn.metrics import classification_report
import json
from sklearn.model_selection import GridSearchCV

param_grid = {
    "max_depth": [3, 5, 7, 9],
    "learning_rate": [0.01, 0.03, 0.1, 0.3],
    "n_estimators": [200, 300, 400, 500, 600],
}
clf = xgb.XGBClassifier(
        objective="multi:softmax",
        tree_method="hist", 
        enable_categorical=True, 
        device="cuda",
        eval_metric="mlogloss",
        early_stopping_rounds=10,
        random_state=settings.SEED,
    )
grid_search = GridSearchCV(clf, param_grid, cv=3, n_jobs=1, verbose=4, scoring="f1_weighted",)
grid_search.fit(X_train, y_train, eval_set=[(X_valid, y_valid)], verbose=False)
                
print('best params', grid_search.best_params_)
_best_clf = grid_search.best_estimator_
_best_clf.save_model(settings.MODELS_PATH / "xgb_gridsearch_best.json")
print('best it', _best_clf.best_iteration, 'best score', _best_clf.best_score)

# print perf
y_pred = _best_clf.predict(X_test)
print(classification_report(y_test, y_pred))
with open(settings.MODELS_PATH / 'xgb_gridsearch_best.perf.json', 'w') as f:
    json.dump(classification_report(y_test, y_pred, output_dict=True), f, indent=2)

# Get feature importances
importances = _best_clf.get_booster().get_score(importance_type="gain")
plt = xgb.plot_importance(importances, max_num_features=20, importance_type="gain")
plt.figure.savefig(settings.PLOTS_PATH / 'xgb_gridsearch_importance.pdf')
