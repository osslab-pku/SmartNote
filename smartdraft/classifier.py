import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

from .config import settings

class BaseClassifier:
    def __init__(self, labels, *args, **kwargs) -> None:
        self.encoder_label = LabelEncoder()
        self.encoder_label.fit(labels)
        self.encoder_release_type = LabelEncoder()
        self.encoder_release_type.fit(settings.categories.release_types)
        self.encoder_project_domain = LabelEncoder()
        self.encoder_project_domain.fit(settings.categories.project_domains)

        self.feature_names = []
        self.labels = labels
        self.model: Optional[xgb.XGBClassifier] = None

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.drop(
            columns=['nameWithOwner', 'sha', 'authorName', 'authorEmail', 'date', 'releaseTag', 'body']
        )
        
        X['releaseType'] = pd.Series(self.encoder_release_type.transform(X['releaseType'])).astype('category')
        X['domain'] = pd.Series(self.encoder_project_domain.transform(X['domain'])).astype('category')

        # align the order of features with the models
        X = X[self.feature_names]
        return X

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict_proba(X)


    def predict_labels(self, X: pd.DataFrame) -> List[Tuple[str, float]]:
        """
        Predict the most probable label with its probability.
        """
        _predicted = self.model.predict_proba(X)
        _predicted_idx = np.argmax(_predicted, axis=1)
        _predicted_proba = _predicted[np.arange(len(_predicted)), _predicted_idx]
        # replace the predicted labels with the actual labels
        return [
            (self.labels[pred], proba) for pred, proba in zip(_predicted_idx, _predicted_proba)
        ]
    

class XGBoostCommitFilter(BaseClassifier):
    def __init__(self, 
                 labels = ['filtered', 'included'],
                 model_path = "xgb_model.json", 
                 *args, **kwargs) -> None:
        super().__init__(labels, *args, **kwargs)
        self.labels = labels
        self.model = xgb.XGBClassifier(
                        objective="binary:logistic",
                        tree_method="hist", 
                        enable_categorical=True, 
                        device="cuda",
                        eval_metric="logloss",
                        early_stopping_rounds=10,
                        random_state=settings.SEED,
                    )
        self.model.load_model(model_path)
        self.feature_names = self.model.get_booster().feature_names
    

class XGBoostCommitClassifier(BaseClassifier):
    def __init__(self, 
                 labels: List[str] = settings.categories.conventional_commits,
                 model_path = "xgb_model.json", 
                 *args, **kwargs) -> None:
        super().__init__(labels, *args, **kwargs)
        self.model = xgb.XGBClassifier(
                        objective="binary:logistic",
                        tree_method="hist", 
                        enable_categorical=True, 
                        device="cuda",
                        eval_metric="logloss",
                        early_stopping_rounds=10,
                        random_state=settings.SEED,
                    )
        self.model.load_model(model_path)
        self.feature_names = self.model.get_booster().feature_names
        self.labels = labels