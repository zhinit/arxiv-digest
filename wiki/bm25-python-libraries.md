# BM25 Python Libraries

Two main options for [[bm25]] scoring in Python without an external search
server.

## rank-bm25

Pure Python. Simple API, no dependencies beyond standard library.

```python
from rank_bm25 import BM25Okapi

tokenized_corpus = [doc.split() for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

scores = bm25.get_scores(query.split())
top_docs = bm25.get_top_n(query.split(), corpus, n=5)
```

Variants: BM25Okapi, BM25L, BM25+, BM25-Adpt, BM25T.
No built-in tokenization — preprocessing is the caller's responsibility.
Install: `pip install rank_bm25`
(source: rank-bm25-library.md)

## bm25s

High-performance. Uses SciPy sparse matrices for 100–1000× faster retrieval
than rank-bm25 on large corpora. Built-in tokenizer with stopword removal.
Supports index persistence (save/load).

```python
import bm25s

corpus_tokens = bm25s.tokenize(corpus)
retriever = bm25s.BM25(corpus=corpus)
retriever.index(corpus_tokens)

query_tokens = bm25s.tokenize("search query")
docs, scores = retriever.retrieve(query_tokens, k=5)

retriever.save("my_index")
```

Variants: robertson, atire, bm25l, bm25+, lucene.
Install: `pip install bm25s[full]`
(source: bm25s-library.md)

## Comparison

| Aspect | rank-bm25 | bm25s |
|--------|-----------|-------|
| Speed (queries/sec on NQ) | 0.10 | 41.85 |
| Dependencies | None | NumPy, SciPy |
| Built-in tokenizer | No | Yes |
| Index persistence | No | Yes |
| Memory mapping | No | Yes |
| Package size | 99MB | 479MB |

(source: bm25s-library.md)

## When to Use Which

- **rank-bm25**: Small corpora (< 10k docs), prototyping, minimal
  dependencies preferred.
- **bm25s**: Larger corpora, production-adjacent use, need for persistence
  or fast batch queries.
- **Elasticsearch**: Distributed, multi-tenant, need monitoring/dashboards,
  or non-BM25 retrieval modes.

See also: [[bm25]], [[tokenization]], [[keyword-search]]
