import re

TITLE_WEIGHT = 3
ABSTRACT_WEIGHT = 1


def score_paper(paper: dict, topics: list[str]) -> int:
    score = 0
    title = paper.get("title", "")
    abstract = paper.get("abstract", "")

    for topic in topics:
        pattern = re.compile(r"\b" + re.escape(topic) + r"\b", re.IGNORECASE)
        if pattern.search(title):
            score += TITLE_WEIGHT
        if pattern.search(abstract):
            score += ABSTRACT_WEIGHT

    return score


def filter_and_score(papers: list[dict], topics: list[str]) -> list[dict]:
    scored = []
    for paper in papers:
        s = score_paper(paper, topics)
        if s > 0:
            scored.append({**paper, "score": s})

    scored.sort(key=lambda p: p["score"], reverse=True)
    return scored
