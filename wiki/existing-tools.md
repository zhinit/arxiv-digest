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

## See also

- [[curation-pipeline]] — curation pipeline architecture
- [[paper-ranking]] — ranking approaches compared

Last updated: 2026-07-10
