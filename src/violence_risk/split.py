from __future__ import annotations

import pandas as pd


def partition(frame: pd.DataFrame, external_region: str, temporal_cutoff: str):
    cutoff = pd.Timestamp(temporal_cutoff)
    external = frame[frame.region.eq(external_region)].copy()
    remaining = frame[~frame.region.eq(external_region)].copy()
    temporal = remaining[remaining.landmark_at.ge(cutoff)].copy()
    development = remaining[remaining.landmark_at.lt(cutoff)].copy()
    sets = {"development": development, "temporal": temporal, "external": external}
    identities = {name: set(part.person_id) for name, part in sets.items()}
    # A person belongs to one region in the synthetic/common data model. Remove any
    # future landmarks for development people to enforce person-level isolation.
    temporal = temporal[~temporal.person_id.isin(identities["development"])].copy()
    sets["temporal"] = temporal
    for left, right in [("development", "temporal"), ("development", "external"), ("temporal", "external")]:
        if set(sets[left].person_id) & set(sets[right].person_id):
            raise ValueError(f"person leakage between {left} and {right}")
    return sets
