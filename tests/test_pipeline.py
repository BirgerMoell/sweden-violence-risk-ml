import pandas as pd
import pytest

from violence_risk.data import assert_no_temporal_leakage, make_synthetic_landmarks
from violence_risk.metrics import evaluate
from violence_risk.split import partition


def test_features_precede_landmark():
    frame = make_synthetic_landmarks(100, 2, 1)
    assert_no_temporal_leakage(frame)
    frame.loc[0, "feature_available_at"] = frame.loc[0, "landmark_at"] + pd.Timedelta(days=1)
    with pytest.raises(ValueError):
        assert_no_temporal_leakage(frame)


def test_people_do_not_cross_partitions():
    parts = partition(make_synthetic_landmarks(500, 2, 2), "north", "2024-01-01")
    ids = {name: set(part.person_id) for name, part in parts.items()}
    assert not ids["development"] & ids["temporal"]
    assert not ids["development"] & ids["external"]
    assert not ids["temporal"] & ids["external"]


def test_metrics_are_finite():
    result = evaluate([0, 0, 1, 1], [0.1, 0.2, 0.7, 0.9])
    assert 0 <= result["brier"] <= 1
    assert result["auroc"] > 0.5
