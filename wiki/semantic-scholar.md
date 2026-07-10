# Semantic Scholar API

Free API from Allen Institute for AI. 214M papers, 2.49B citations, 79M
authors. Useful for enriching arXiv papers with citation data and embeddings.
(source: semantic-scholar-api.md)

## Services

| Service | Endpoint | Purpose |
|---------|----------|---------|
| Academic Graph | `/api-docs/graph` | Papers, authors, citations, SPECTER2 embeddings |
| Recommendations | `/api-docs/recommendations` | Papers similar to a seed paper |
| Datasets | `/api-docs/datasets` | Bulk download (S2AG, S2ORC) |

## Rate Limits

- Unauthenticated: 1000 req/s shared pool (subject to throttling)
- Authenticated (API key): 1 RPS introductory, higher limits available
- API keys via email application

(source: semantic-scholar-api.md)

## SPECTER Embeddings

**SPECTER**: Document-level embeddings from SciBERT pretrained on citation
graph. Input: title + abstract. Output: dense vector for similarity search.

**SPECTER 2.0**: Successor trained on post-2018 papers. Generates
task-specific embeddings via adapters (search, classification, proximity).

Available through the Academic Graph API. (source: semantic-scholar-api.md)

## Recommendations API

Given a seed paper ID, returns similar papers. Operates paper→paper (not
profile→papers). (source: semantic-scholar-api.md)

## See also

- [[paper-ranking]] — ranking approaches compared
- [[curation-pipeline]] — pipeline architecture
- [[arxiv-data-access]] — arXiv's own access methods

Last updated: 2026-07-10
