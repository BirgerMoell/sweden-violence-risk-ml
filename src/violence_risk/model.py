from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .data import FEATURES


def logistic_pipeline():
    numeric = [f for f in FEATURES if f != "recorded_sex"]
    preprocess = ColumnTransformer(
        [
            ("num", Pipeline([("impute", SimpleImputer()), ("scale", StandardScaler())]), numeric),
            ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), ["recorded_sex"]),
        ]
    )
    return Pipeline([("preprocess", preprocess), ("model", LogisticRegression(C=0.5, max_iter=2000))])


def boosting_pipeline():
    return Pipeline(
        [
            ("impute", SimpleImputer()),
            ("model", HistGradientBoostingClassifier(max_iter=150, learning_rate=0.05, max_leaf_nodes=15, l2_regularization=1.0)),
        ]
    )
