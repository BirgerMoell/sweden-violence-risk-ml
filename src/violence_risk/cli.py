from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from .data import FEATURES, assert_no_temporal_leakage, make_synthetic_landmarks
from .metrics import evaluate
from .model import boosting_pipeline, logistic_pipeline
from .split import partition


def main():
    parser = argparse.ArgumentParser(description="Run the SÄKER-ML synthetic demonstration")
    parser.add_argument("--config", default="configs/demo.yaml")
    args = parser.parse_args()
    config = yaml.safe_load(Path(args.config).read_text())
    frame = make_synthetic_landmarks(config["n_people"], config["landmarks_per_person"], config["seed"])
    assert_no_temporal_leakage(frame)
    parts = partition(frame, config["external_region"], config["temporal_cutoff"])
    train = parts["development"]
    results = {}
    models = {"logistic": logistic_pipeline(), "boosting": boosting_pipeline()}
    for name, model in models.items():
        model.fit(train[FEATURES], train.outcome_30d)
        results[name] = {}
        for split_name, split in parts.items():
            if split.empty:
                continue
            predictions = model.predict_proba(split[FEATURES])[:, 1]
            results[name][split_name] = evaluate(split.outcome_30d.to_numpy(), predictions)
    output = Path(config["output_dir"])
    output.mkdir(parents=True, exist_ok=True)
    (output / "metrics.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
