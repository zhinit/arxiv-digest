# Paper Ranking Approaches

Methods for scoring and ranking candidate papers by relevance to a user's
interests. Three tiers, from cheapest to most expensive.

## Tier 1: Keyword / TF-IDF

**How it works**: Represent papers as [[tfidf]] vectors over abstracts. Score
against a user interest vector (built from keywords or liked-paper abstracts).
Cosine similarity for ranking. For term-frequency-based ranking with
saturation and length normalization, use [[bm25]] instead of raw TF-IDF.

**Pros**: Fast, free, no external dependencies. arxiv-sanity-lite proves this
works at scale — runs on a $5/month VPS indexing 30K papers.
(source: arxiv-sanity-lite.md)

**Cons**: Purely lexical. Misses papers that describe the same ideas with
different vocabulary. Can't distinguish quality or novelty.

**Implementation**: scikit-learn `TfidfVectorizer` over abstracts, or
[[bm25-python-libraries]] (rank-bm25, bm25s) for BM25 scoring with proper
saturation and document length normalization. Optionally train an SVM on
user-tagged papers (positive = interesting, rest = negative) for a
personalized decision boundary. (source: arxiv-sanity-lite.md)

## Tier 2: Embedding Similarity

**How it works**: Represent papers as dense vectors via a pretrained model
(SPECTER, SPECTER2, or a general sentence transformer). Compute cosine
similarity against seed papers or an averaged interest embedding.

**Pros**: Captures semantic similarity across vocabulary differences. SPECTER2
is specifically trained on scientific papers via citation graph signal.
(source: semantic-scholar-api.md)

**Cons**: Requires an embedding model or API calls. Still doesn't understand
nuanced interest criteria ("I want papers that apply X to domain Y").

**Implementation**: Fetch SPECTER2 embeddings from [[semantic-scholar]] API,
or run a local sentence-transformers model. Build a FAISS index for fast
nearest-neighbor lookup.

## Tier 3: LLM Scoring

**How it works**: Give an LLM the paper abstract + a description of user
interests, ask it to rate relevance (e.g., 1–5 scale with justification).

**Pros**: Understands nuanced criteria. Can explain why a paper is relevant.
Can filter on subjective qualities ("novel approach" vs. "incremental").

**Cons**: Expensive per paper. At ~$0.003/abstract (Claude Haiku on a short
prompt), scoring 200 papers/day costs ~$0.60/day or ~$18/month. Slower.
Non-deterministic.

**Implementation**: Two-stage approach to control cost:
1. Cheap pre-filter (TF-IDF or embeddings) cuts 200 papers to ~30 candidates
2. LLM scores the 30 candidates with a structured prompt

This reduces LLM cost by ~85% while keeping quality high on the long tail.

## Hybrid Approach

The practical architecture combines tiers:

```
All new papers (RSS)
  → Tier 1: keyword/category filter (remove obvious noise)
  → Tier 2: embedding similarity (rank by topic relevance)
  → Top N → Tier 3: LLM scoring (nuanced relevance + quality)
  → Final digest
```

Each tier is optional — a minimal tool can work with just Tier 1 (TF-IDF
keywords), and you can add tiers incrementally.

## See Also

- [[curation-pipeline]] — full pipeline architecture
- [[arxiv-sanity-lite-reference]] — TF-IDF + SVM in practice
- [[semantic-scholar]] — source of SPECTER2 embeddings
- [[bm25]] — BM25 ranking formula and parameters
- [[keyword-search]] — lexical retrieval end-to-end
- [[hybrid-retrieval]] — combining keyword and semantic search (RRF, fusion)
