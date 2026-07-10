from unittest.mock import patch
from src.select import select_papers


def make_scored(n):
    return [{"title": f"Paper {i}", "score": n - i} for i in range(n)]


class TestSelectPapers:
    def test_basic_selection(self):
        papers = make_scored(10)
        top, rand = select_papers(papers, 3, 2)
        assert len(top) == 3
        assert len(rand) == 2
        assert top == papers[:3]

    def test_random_from_remainder(self):
        papers = make_scored(10)
        with patch("src.select.random.sample", return_value=[papers[5], papers[8]]):
            top, rand = select_papers(papers, 3, 2)
        assert rand == [papers[5], papers[8]]

    def test_mutually_exclusive(self):
        papers = make_scored(10)
        top, rand = select_papers(papers, 3, 2)
        top_titles = {p["title"] for p in top}
        rand_titles = {p["title"] for p in rand}
        assert top_titles.isdisjoint(rand_titles)

    def test_fewer_than_top_n(self):
        papers = make_scored(3)
        top, rand = select_papers(papers, 5, 2)
        assert len(top) == 3
        assert len(rand) == 0

    def test_fewer_remainder_than_random_n(self):
        papers = make_scored(5)
        top, rand = select_papers(papers, 3, 5)
        assert len(top) == 3
        assert len(rand) == 2
        assert rand == papers[3:]

    def test_zero_matches(self):
        top, rand = select_papers([], 5, 3)
        assert top == []
        assert rand == []

    def test_exact_top_n(self):
        papers = make_scored(5)
        top, rand = select_papers(papers, 5, 3)
        assert len(top) == 5
        assert len(rand) == 0

    def test_zero_random_n(self):
        papers = make_scored(10)
        top, rand = select_papers(papers, 3, 0)
        assert len(top) == 3
        assert len(rand) == 0
