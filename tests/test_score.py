from src.score import score_paper, filter_and_score


def make_paper(title="", abstract=""):
    return {"title": title, "abstract": abstract, "authors": [], "link": "", "categories": [], "published": ""}


class TestScorePaper:
    def test_title_only(self):
        paper = make_paper(title="Advances in AI research")
        assert score_paper(paper, ["AI"]) == 3

    def test_abstract_only(self):
        paper = make_paper(abstract="We study AI models")
        assert score_paper(paper, ["AI"]) == 1

    def test_both_title_and_abstract(self):
        paper = make_paper(title="AI systems", abstract="AI is transformative")
        assert score_paper(paper, ["AI"]) == 4

    def test_multiple_keywords(self):
        paper = make_paper(title="AI and DSP", abstract="Audio processing with AI")
        assert score_paper(paper, ["AI", "DSP"]) == 7  # AI: 3+1, DSP: 3

    def test_case_insensitive(self):
        paper = make_paper(title="advances in ai", abstract="AI is great")
        assert score_paper(paper, ["AI"]) == 4

    def test_phrase_matching(self):
        paper = make_paper(title="predictive markets analysis")
        assert score_paper(paper, ["predictive markets"]) == 3

    def test_no_match(self):
        paper = make_paper(title="Quantum computing", abstract="Superconducting qubits")
        assert score_paper(paper, ["AI", "DSP"]) == 0

    def test_word_boundary(self):
        paper = make_paper(title="SAID something", abstract="Contains SAID")
        assert score_paper(paper, ["AI"]) == 0

    def test_word_boundary_dsp(self):
        paper = make_paper(title="DSP techniques", abstract="modern DSP")
        assert score_paper(paper, ["DSP"]) == 4


class TestFilterAndScore:
    def test_filters_and_sorts(self):
        papers = [
            make_paper(title="Quantum computing"),
            make_paper(title="AI and DSP", abstract="AI models"),
            make_paper(title="Psychology today", abstract="gambling behavior"),
        ]
        result = filter_and_score(papers, ["AI", "DSP", "psychology", "gambling"])
        assert len(result) == 2
        assert result[0]["title"] == "AI and DSP"
        assert result[0]["score"] == 7  # AI: 3+1, DSP: 3
        assert result[1]["title"] == "Psychology today"
        assert result[1]["score"] == 4  # psychology: 3, gambling: 1

    def test_empty_input(self):
        assert filter_and_score([], ["AI"]) == []

    def test_no_matches(self):
        papers = [make_paper(title="Unrelated paper")]
        assert filter_and_score(papers, ["AI"]) == []

    def test_preserves_paper_fields(self):
        paper = {
            "title": "AI paper",
            "abstract": "about AI",
            "authors": ["Author"],
            "link": "http://example.com",
            "categories": ["cs.AI"],
            "published": "2023-01-01",
        }
        result = filter_and_score([paper], ["AI"])
        assert len(result) == 1
        assert result[0]["authors"] == ["Author"]
        assert result[0]["link"] == "http://example.com"
        assert "score" in result[0]
