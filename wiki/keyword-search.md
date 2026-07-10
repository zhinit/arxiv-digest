# Keyword Search

Retrieval method that matches query terms against document terms using lexical
(exact string) matching. The dominant approach for text search before neural
methods, and still the standard first-stage retriever in production systems.

## How It Works

1. **Tokenization** — split text into terms (words). Quality directly impacts
   results. Common steps: lowercasing, punctuation removal, stopword removal,
   optional stemming. Domain-specific patterns (error codes, identifiers) may
   need special handling. (source: keyword-search-implementation-guide.md)

2. **Indexing** — build an [[inverted-index]]: a mapping from each term to the
   list of documents containing it, with term frequencies. Enables sub-linear
   lookup. (source: keyword-search-implementation-guide.md)

3. **Scoring** — for a query, look up each query term in the index, retrieve
   candidate documents, and score them using [[bm25]] or [[tfidf]].
   (source: keyword-search-implementation-guide.md)

4. **Ranking** — sort candidates by score, return top-k.

## Strengths

- Precision for known-item searches and exact identifiers
- Handles out-of-vocabulary terms (no training needed)
- Fast via [[inverted-index]] structure
- Interpretable — scores trace directly to term matches
- No infrastructure beyond a tokenizer and an index

(source: keyword-search-implementation-guide.md)

## Weaknesses

- No synonym handling (must match exact terms)
- No semantic understanding ("car" won't match "automobile")
- Sensitive to tokenization choices

## When to Use

- Exact identifiers, error codes, technical jargon
- Known-item retrieval (user knows what they're looking for)
- First-stage retrieval in a [[hybrid-retrieval]] pipeline
- Lightweight applications where neural models are overkill

(source: keyword-search-implementation-guide.md)

See also: [[bm25]], [[tokenization]], [[hybrid-retrieval]]
