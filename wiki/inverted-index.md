# Inverted Index

The core data structure behind [[keyword-search]]. Maps each term in a corpus
to a list of documents (and positions) where it appears.

## Structure

```
term → [(doc_id, term_frequency), ...]
```

Each entry is called a "posting list." To score a query, look up each query
term's posting list and compute [[bm25]] or [[tfidf]] scores for the
candidate documents. (source: keyword-search-implementation-guide.md)

## Performance Optimizations

- Pre-computed IDF values and document length normalization factors
- Sorted posting lists enabling binary search or skip lists
- Candidate set filtering — only score documents that contain at least one
  query term

(source: keyword-search-implementation-guide.md)

## Implementations

Apache Lucene (and by extension Elasticsearch) uses an inverted index as its
primary data structure. The Boolean model narrows candidate documents via the
index before the scoring model (typically [[bm25]]) ranks them.
(source: lucene-search-and-ranking-blaszyk.md)

See also: [[keyword-search]], [[bm25]]
