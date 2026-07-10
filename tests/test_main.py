import json
from unittest.mock import patch
from src.main import run

MOCK_PAPERS = [
    {
        "title": "AI and Deep Learning",
        "abstract": "A study of AI techniques in deep learning for DSP applications",
        "authors": ["Alice"],
        "link": "http://arxiv.org/abs/0001",
        "categories": ["cs.AI"],
        "published": "2023-01-01T00:00:00Z",
    },
    {
        "title": "DSP Signal Processing",
        "abstract": "Novel DSP methods for audio processing",
        "authors": ["Bob"],
        "link": "http://arxiv.org/abs/0002",
        "categories": ["eess.SP"],
        "published": "2023-01-02T00:00:00Z",
    },
    {
        "title": "Psychology of Gambling",
        "abstract": "How gambling affects decision making in predictive markets",
        "authors": ["Carol"],
        "link": "http://arxiv.org/abs/0003",
        "categories": ["q-bio.NC"],
        "published": "2023-01-03T00:00:00Z",
    },
    {
        "title": "Quantum Computing Advances",
        "abstract": "Superconducting qubits and quantum error correction",
        "authors": ["Dave"],
        "link": "http://arxiv.org/abs/0004",
        "categories": ["quant-ph"],
        "published": "2023-01-04T00:00:00Z",
    },
]


def test_end_to_end(tmp_path):
    config = {
        "topics": ["AI", "DSP", "psychology", "gambling", "predictive markets"],
        "date_range": "past week",
        "top_n": 2,
        "random_n": 1,
    }
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(config))

    with patch("src.main.fetch_papers", return_value=MOCK_PAPERS):
        result = run(str(config_path))

    assert "top_ranked" in result
    assert "random_picks" in result
    assert "total_fetched" in result
    assert "total_matched" in result

    assert result["total_fetched"] == 4
    assert result["total_matched"] == 3  # quantum paper excluded
    assert len(result["top_ranked"]) == 2
    assert len(result["random_picks"]) == 1

    # top papers should have scores and be sorted descending
    assert result["top_ranked"][0]["score"] >= result["top_ranked"][1]["score"]

    # no overlap between top and random
    top_links = {p["link"] for p in result["top_ranked"]}
    rand_links = {p["link"] for p in result["random_picks"]}
    assert top_links.isdisjoint(rand_links)


def test_no_matches(tmp_path):
    config = {
        "topics": ["nonexistent_topic_xyz"],
        "date_range": "past week",
        "top_n": 5,
        "random_n": 3,
    }
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(config))

    with patch("src.main.fetch_papers", return_value=MOCK_PAPERS):
        result = run(str(config_path))

    assert result["total_matched"] == 0
    assert result["top_ranked"] == []
    assert result["random_picks"] == []
