# Tokenization

The process of splitting text into individual terms (tokens) for indexing and
search. Tokenization quality directly determines [[keyword-search]] quality —
the same tokenization must be applied to both documents and queries.

## Common Steps

1. **Lowercasing** — normalize case
2. **Punctuation removal**
3. **Stopword removal** — drop common words ("the", "and", "is") that carry
   little discriminative signal
4. **Stemming** — reduce words to root forms (e.g., "running" → "run").
   Porter Stemmer is the standard choice.
5. **N-gram generation** — optional, enables partial matching

(source: keyword-search-implementation-guide.md)

## Order Matters

Preserve technical identifiers (error codes, version numbers, SKUs) before
lowercasing, or they lose their discriminative value.
(source: keyword-search-implementation-guide.md)

## Implementation Notes

- `rank-bm25` does no tokenization — all preprocessing must be done externally
  and applied identically to documents and queries.
  (source: rank-bm25-library.md)
- `bm25s` includes a built-in tokenizer with optional stopword removal.
  (source: bm25s-library.md)
- Elasticsearch/Lucene provide configurable analyzers that handle
  tokenization, stemming, and stopword removal as part of the index pipeline.
  (source: lucene-search-and-ranking-blaszyk.md)

See also: [[keyword-search]], [[bm25-python-libraries]]
