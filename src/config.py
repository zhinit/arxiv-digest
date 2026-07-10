import json
from pathlib import Path

REQUIRED_FIELDS = {
    "topics": list,
    "date_range": str,
    "top_n": int,
    "random_n": int,
}


def load_config(path: str | Path = "config.json") -> dict:
    with open(path) as f:
        config = json.load(f)

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
        if not isinstance(config[field], expected_type):
            raise TypeError(
                f"Field '{field}' must be {expected_type.__name__}, "
                f"got {type(config[field]).__name__}"
            )

    if not config["topics"]:
        raise ValueError("'topics' must not be empty")
    if not all(isinstance(t, str) for t in config["topics"]):
        raise TypeError("All items in 'topics' must be strings")
    if config["top_n"] < 0:
        raise ValueError("'top_n' must be non-negative")
    if config["random_n"] < 0:
        raise ValueError("'random_n' must be non-negative")

    return config
