import random


def select_papers(
    scored_papers: list[dict], top_n: int, random_n: int
) -> tuple[list[dict], list[dict]]:
    top = scored_papers[:top_n]
    remainder = scored_papers[top_n:]

    if random_n >= len(remainder):
        random_picks = remainder
    else:
        random_picks = random.sample(remainder, random_n)

    return top, random_picks
