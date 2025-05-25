# %%
from config import init_env, settings
init_env(name='cls_gte_xgb_norm', cuda_devices=1)
settings.MODEL_NAME = 'Alibaba-NLP/gte-base-en-v1.5'
settings.MODELS_PATH

# %%
import pandas as pd

df_commits = pd.read_parquet(settings.DATASETS_PATH / 'dataset_cls.parquet')
df_repos = pd.read_csv(settings.DATASETS_PATH / 'repos_cls.csv', on_bad_lines='skip')
print(df_commits.shape, df_repos.shape)
df_commits

# %%
from typing import Optional, List
from loguru import logger
from tqdm.auto import tqdm
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

from config import settings

class SentenceDataset(Dataset):
    def __init__(self, sentences, tokenizer, max_length):
        self.sentences = sentences
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, idx):
        sentence = self.sentences[idx]
        inputs = self.tokenizer(sentence, return_tensors="pt", max_length=self.max_length, 
                                padding="max_length", truncation=True)
        return inputs


class SentenceEmbedder:
    def __init__(
            self,
            model_name: Optional[str] = None,
            # dtype: Optional[torch.dtype] = None,
            batch_size: int = 32,
            max_length: int = 128,
            l2_normalize: bool = True
    ):
        """
        Initialize SentenceEmbedder object.

        :param model_name: huggingface model name, required if not set in settings
        # :param dtype: convert model to this dtype, e.g. torch.bfloat16, to save memory
        :param batch_size: batch size for inference
        :param max_length: max length of input sentence
        :param l2_normalize: whether to normalize embeddings to unit length
        """
        assert hasattr(settings, "TORCH_DEVICE"), "run init_env() first"
        if model_name is None:
            model_name = settings.rngen.embed_model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name, trust_remote_code=True)
        if settings.TORCH_DEVICE.type != 'cpu':
            model = model.to(settings.TORCH_DEVICE)
        if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
            logger.info("Device supports BF16, using BF16 to save VRAM")
            model = model.to(dtype=torch.bfloat16)
        model.eval()

        self.model = model
        self.tokenizer = tokenizer
        self.batch_size = batch_size
        self.max_length = max_length
        self.l2_normalize = l2_normalize

    def encode(self, sentences: List[str]) -> pd.DataFrame:
        """
        Encode list of sentences into embeddings.

        :param sentences: list of sentences to encode
        :return: DataFrame of embeddings
        """
        dataset = SentenceDataset(sentences, self.tokenizer, self.max_length)
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)

        embeddings = []
        with torch.no_grad():
            for batch in tqdm(dataloader, desc="Generating embeddings"):
                input_ids = batch['input_ids'].to(settings.TORCH_DEVICE).squeeze()
                attention_mask = batch['attention_mask'].to(settings.TORCH_DEVICE).squeeze()
                outputs = self.model(input_ids, attention_mask=attention_mask)
                _emb = outputs.last_hidden_state[:, 0]
                # l2 normalization
                if self.l2_normalize:
                    _emb = F.normalize(_emb, p=2, dim=1)
                # numpy doesn't support bfloat16
                embeddings.append(_emb.cpu().detach().float().numpy())

        df_embs = pd.DataFrame(
            np.vstack(embeddings), 
            columns=[f'emb{i}' for i in range(embeddings[0].shape[1])]
        )
        return df_embs

# %%
import numpy as np
import torch
import os
from tqdm.auto import tqdm

if os.path.exists(settings.CACHE_PATH / 'df_embs.parquet'):
    df_embs = pd.read_parquet(settings.CACHE_PATH / 'df_embs.parquet')
    print(df_embs.shape)
else:
    embedder = SentenceEmbedder(model_name=settings.MODEL_NAME)
    df_embs = embedder.encode(df_commits['body'].tolist())
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
    'colsample_bytree': [0.3, 0.7],
    'subsample': [0.7, 1],
    'gamma': [0, 0.1, 0.2]
}
clf = xgb.XGBClassifier(
        objective="multi:softmax",
        tree_method="hist", 
        enable_categorical=True, 
        device="cuda",
        eval_metric="mlogloss",
        early_stopping_rounds=10,
        random_state=settings.SEED,
        # limit max iterations
        # n_estimators=1000,
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
