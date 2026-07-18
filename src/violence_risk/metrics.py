from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score


def calibration_parameters(y, p):
    p = np.clip(np.asarray(p), 1e-6, 1 - 1e-6)
    logits = np.log(p / (1 - p)).reshape(-1, 1)
    model = LogisticRegression(C=1e6).fit(logits, y)
    return float(model.intercept_[0]), float(model.coef_[0, 0])


def evaluate(y, p):
    intercept, slope = calibration_parameters(y, p)
    return {
        "n": int(len(y)),
        "events": int(np.sum(y)),
        "prevalence": float(np.mean(y)),
        "auroc": float(roc_auc_score(y, p)),
        "auprc": float(average_precision_score(y, p)),
        "brier": float(brier_score_loss(y, p)),
        "calibration_intercept": intercept,
        "calibration_slope": slope,
    }
