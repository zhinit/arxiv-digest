import json
import pytest
from src.config import load_config


@pytest.fixture
def valid_config(tmp_path):
    config = {
        "topics": ["AI", "DSP"],
        "date_range": "past week",
        "top_n": 5,
        "random_n": 2,
    }
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    return path


def test_load_valid_config(valid_config):
    config = load_config(valid_config)
    assert config["topics"] == ["AI", "DSP"]
    assert config["date_range"] == "past week"
    assert config["top_n"] == 5
    assert config["random_n"] == 2


@pytest.mark.parametrize("missing_field", ["topics", "date_range", "top_n", "random_n"])
def test_missing_field(tmp_path, missing_field):
    config = {
        "topics": ["AI"],
        "date_range": "past week",
        "top_n": 5,
        "random_n": 2,
    }
    del config[missing_field]
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(ValueError, match=f"Missing required field: {missing_field}"):
        load_config(path)


def test_bad_type_topics(tmp_path):
    config = {"topics": "not a list", "date_range": "past week", "top_n": 5, "random_n": 2}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(TypeError, match="topics.*must be list"):
        load_config(path)


def test_bad_type_top_n(tmp_path):
    config = {"topics": ["AI"], "date_range": "past week", "top_n": "five", "random_n": 2}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(TypeError, match="top_n.*must be int"):
        load_config(path)


def test_empty_topics(tmp_path):
    config = {"topics": [], "date_range": "past week", "top_n": 5, "random_n": 2}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(ValueError, match="must not be empty"):
        load_config(path)


def test_non_string_topic_items(tmp_path):
    config = {"topics": [123], "date_range": "past week", "top_n": 5, "random_n": 2}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(TypeError, match="must be strings"):
        load_config(path)


def test_negative_top_n(tmp_path):
    config = {"topics": ["AI"], "date_range": "past week", "top_n": -1, "random_n": 2}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config))
    with pytest.raises(ValueError, match="non-negative"):
        load_config(path)
