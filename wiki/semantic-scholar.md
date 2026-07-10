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

Given a seed paper ID, returns similar papers. Can be used to expand from
known-good papers to find related work.

## Use for Curation

Semantic Scholar complements arXiv in two ways:

1. **Embeddings for ranking** — fetch SPECTER2 embeddings for candidate papers,
   compute cosine similarity against a "seed set" of papers you like. More
   semantic than TF-IDF, catches papers with different vocabulary but similar
   ideas.

2. **Citation signals** — citation count and velocity as quality proxies
   (with the caveat that new papers have no citations yet).

The Recommendations API is less useful for a daily digest (it's paper→paper,
not profile→papers), but good for seeding an interest profile.

## See Also

- [[paper-ranking]] — ranking approaches compared
- [[curation-pipeline]] — where Semantic Scholar fits
- [[arxiv-data-access]] — arXiv's own access methods
