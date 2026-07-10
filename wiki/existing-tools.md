# Existing arXiv Curation Tools

Landscape of tools for discovering, filtering, and recommending arXiv papers.
(source: awesome-arxiv.md)

## Recommender Services

| Tool | Approach | Notes |
|------|----------|-------|
| [[arxiv-sanity-lite-reference]] | TF-IDF + SVM | Self-hosted, $5/mo, ~30K papers |
| Scholar Inbox (scholar-inbox.com) | Personal recommender | Indexes arXiv/bioRxiv/medRxiv/ChemRxiv daily |
| Benty Fields (benty-fields.com) | Personalized recs + email | Author/topic alerts |
| AlphaSignal (alphasignal.ai) | Newsletter | 5-minute daily summaries of trending AI |
| HuggingFace Daily Papers | Community-curated | Human upvotes, not algorithmic |

## Search Engines

| Tool | Approach |
|------|----------|
| [[semantic-scholar]] | 200M+ papers, SPECTER2 embeddings, recs API |
| searchthearXiv | Semantic search over 300K+ ML papers |
| PaperMatch (papermatch.me) | Semantic search by NL or arXiv ID |
| Connected Papers | Citation graph visualization |
| Elicit (elicit.com) | LLM-powered research assistant, 125M+ papers |

## SDKs & Libraries

| Tool | Language | Purpose |
|------|----------|---------|
| [[arxiv-py]] | Python | API wrapper, metadata + PDF download |
| arXivScraper | Python | Category/date metadata scraping |
| arxiv_summarizer | Python | Fetch + LLM summarization |
| ArXiv MCP Server | Python | AI assistant integration via MCP |
| Docling | Python | PDF → Markdown/JSON/HTML conversion |
| cli-arxiv | Python | Terminal search + management |

## Datasets

| Dataset | Scale | License |
|---------|-------|---------|
| Cornell arXiv (Kaggle) | 1.7M+ articles | CC0 |
| S2ORC (AllenAI) | 81.1M+ papers, 8.1M full-text | ODC-By |
| arxiv-summarisation (HF) | 431K articles | — |
| unarXive | 1.9M LaTeX papers | MIT |

(source: awesome-arxiv.md)

## Gap Analysis

What existing tools don't do well (and what this project should address):

1. **Personalized daily digest as CLI output** — most tools are web apps or
   newsletters, not command-line tools
2. **LLM-based relevance scoring** — most use TF-IDF or embeddings; none
   combine cheap pre-filtering with LLM scoring for nuanced relevance
3. **Configurable interest profiles** — most require manual tagging; a config
   file defining interests declaratively would be more ergonomic
4. **Explain why** — most tools rank without explanation; an LLM can say
   *why* a paper is interesting

## See Also

- [[curation-pipeline]] — the architecture this project will use
- [[paper-ranking]] — ranking approaches compared
