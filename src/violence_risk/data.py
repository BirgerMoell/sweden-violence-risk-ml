from __future__ import annotations

import numpy as np
import pandas as pd


FEATURES = [
    "age",
    "recorded_sex",
    "recent_emergency_contacts_30d",
    "recent_inpatient_days_30d",
    "prior_violence_count",
    "substance_use_dx",
    "care_intensity_change_14d",
]


def make_synthetic_landmarks(n_people: int = 5000, landmarks_per_person: int = 4, seed: int = 7) -> pd.DataFrame:
    """Create structurally realistic but entirely artificial landmark data."""
    rng = np.random.default_rng(seed)
    people = np.repeat(np.arange(n_people), landmarks_per_person)
    n = people.size
    base_dates = pd.Timestamp("2020-01-01") + pd.to_timedelta(rng.integers(0, 1826, n_people), unit="D")
    dates = np.repeat(base_dates.to_numpy(), landmarks_per_person) + np.tile(
        pd.to_timedelta(np.arange(landmarks_per_person) * 28, unit="D"), n_people
    )
    region_person = rng.choice(["central", "south", "west", "north"], n_people, p=[0.28, 0.27, 0.27, 0.18])
    region = np.repeat(region_person, landmarks_per_person)
    age_person = rng.integers(18, 82, n_people)
    age = np.repeat(age_person, landmarks_per_person)
    sex_person = rng.binomial(1, 0.49, n_people)
    sex = np.repeat(sex_person, landmarks_per_person)
    emergency = rng.poisson(0.35, n)
    inpatient = np.minimum(rng.negative_binomial(1, 0.75, n), 30)
    prior = np.repeat(rng.poisson(0.16, n_people), landmarks_per_person)
    substance = np.repeat(rng.binomial(1, 0.22, n_people), landmarks_per_person)
    intensity = rng.normal(0, 1, n)
    linear = -4.1 + 0.50 * emergency + 0.045 * inpatient + 0.72 * prior + 0.62 * substance + 0.25 * intensity
    linear += np.where(region == "north", 0.12, 0) + 0.10 * sex - 0.009 * (age - 40)
    risk = 1 / (1 + np.exp(-linear))
    outcome = rng.binomial(1, risk)
    landmark_at = pd.to_datetime(dates)
    return pd.DataFrame(
        {
            "person_id": people.astype(str),
            "region": region,
            "landmark_at": landmark_at,
            "feature_available_at": landmark_at - pd.to_timedelta(rng.integers(0, 15, n), unit="D"),
            "age": age,
            "recorded_sex": sex,
            "recent_emergency_contacts_30d": emergency,
            "recent_inpatient_days_30d": inpatient,
            "prior_violence_count": prior,
            "substance_use_dx": substance,
            "care_intensity_change_14d": intensity,
            "outcome_30d": outcome,
        }
    )


def assert_no_temporal_leakage(frame: pd.DataFrame) -> None:
    bad = frame["feature_available_at"] > frame["landmark_at"]
    if bad.any():
        raise ValueError(f"{int(bad.sum())} rows contain predictors unavailable at the landmark")
