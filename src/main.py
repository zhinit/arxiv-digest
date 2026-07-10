import json
import sys
from pathlib import Path

from src.config import load_config
from src.fetch import fetch_papers
from src.score import filter_and_score
from src.select import select_papers


def run(config_path: str = "config.json") -> dict:
    config = load_config(config_path)

    papers = fetch_papers(config["topics"], config["date_range"])
    scored = filter_and_score(papers, config["topics"])
    top, random_picks = select_papers(scored, config["top_n"], config["random_n"])

    return {
        "top_ranked": top,
        "random_picks": random_picks,
        "total_fetched": len(papers),
        "total_matched": len(scored),
    }


def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    result = run(config_path)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
