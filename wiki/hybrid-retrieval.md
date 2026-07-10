# Hybrid Retrieval

Combining [[keyword-search]] (lexical) and semantic (dense vector) retrieval
to get the strengths of both. The current state of the art for production
search and RAG systems.

## Why Hybrid

Keyword search handles exact terms, identifiers, and out-of-vocabulary tokens.
Semantic search handles synonyms, paraphrases, and conceptual similarity.
Neither alone covers all query types.
(source: keyword-search-implementation-guide.md)

## Architecture

Two-stage pattern:

1. **First stage** — run [[bm25]] and dense vector search in parallel as
   independent retrievers. Each returns a ranked list of candidates.
2. **Fusion** — combine the two ranked lists into a single ranking.
3. **Reranking** (optional) — a cross-encoder scores the fused shortlist
   for higher precision.

## Fusion Methods

### Reciprocal Rank Fusion (RRF)

Parameter-free. Operates on ranks, not raw scores (which avoids the problem
of incompatible score scales between retrievers).

```
RRF_score(d) = Σ 1 / (k + rank_i(d))
```

Where k is a constant (typically 60) and rank_i(d) is document d's rank in
retriever i's list. (source: keyword-search-implementation-guide.md)

### Weighted Score Fusion

Normalize scores from each retriever to [0, 1], then combine with weights:

```
score(d) = α × bm25_score(d) + (1 - α) × semantic_score(d)
```

Requires tuning α. (source: keyword-search-implementation-guide.md)

## Query Routing

An alternative to always running both retrievers: classify the query and
route to the appropriate method.

- Exact identifiers, codes → [[keyword-search]] only
- Conceptual/natural language → semantic only
- Ambiguous or mixed → hybrid

(source: keyword-search-implementation-guide.md)

See also: [[bm25]], [[keyword-search]]
