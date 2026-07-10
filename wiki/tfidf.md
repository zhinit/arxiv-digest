# TF-IDF (Term Frequency–Inverse Document Frequency)

A numerical statistic that reflects how important a word is to a document
within a corpus. The foundational technique for keyword-based relevance
scoring, predating [[bm25]].

## Formula

```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

### Term Frequency (TF)
Raw count of term t in document d. The more a term appears in a document, the
more relevant that document is considered for that term.
(source: tfidf-bm25-rag-guide.md)

### Inverse Document Frequency (IDF)
```
IDF(t) = log(N / df(t))
```
Where N is total documents and df(t) is the number of documents containing
term t. Terms that appear in many documents are considered less informative
and receive low weight. (source: tfidf-bm25-rag-guide.md)

### Combined
Higher scores go to terms that are frequent in a specific document but rare
across the corpus. (source: tfidf-bm25-rag-guide.md)

## Limitations

1. **No saturation**: Score grows linearly with term frequency. A term
   appearing 100 times gets 100× the weight of a single occurrence, which
   overstates the relevance of keyword-stuffed or repetitive documents.
   (source: tfidf-bm25-rag-guide.md)

2. **No document length normalization**: A 10,000-word document has more
   opportunity to contain a term than a 50-word abstract, but TF-IDF does
   not correct for this. (source: tfidf-bm25-rag-guide.md)

Both limitations are addressed by [[bm25]].

## Python Implementation

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
```

(source: tfidf-bm25-rag-guide.md)

## Usage

TF-IDF remains the basis for Lucene's scoring model, though modern versions
use [[bm25]] by default. Still used directly in lightweight applications and
as a feature in ML pipelines. (source: lucene-scoring.md)

## See also

- [[keyword-search]]
- [[inverted-index]]

Last updated: 2026-07-10
