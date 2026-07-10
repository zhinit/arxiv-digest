# Curation Pipeline Architecture

The end-to-end architecture for scanning arXiv and producing a curated digest.
Synthesized from the approaches in [[arxiv-sanity-lite-reference]],
[[flexible-arxiv-rss-reference]], and [[paper-ranking]].

## Pipeline Stages

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────┐
│   Ingest    │ →  │  Pre-filter  │ →  │    Rank      │ →  │ Output │
│  (RSS/API)  │    │ (keyword/cat)│    │ (embed/LLM)  │    │(digest)│
└─────────────┘    └──────────────┘    └──────────────┘    └────────┘
  ~200 papers        ~50 papers         ~10 papers        markdown/CLI
```

### Stage 1: Ingest

**Goal**: Get today's new papers in categories of interest.

[[arxiv-rss-feeds]] provides one HTTP request per category, returning all new
papers with titles, abstracts, authors, categories.

- Parse with `feedparser` (Python)
- Filter to `announce_type == "new"` (skip replacements/cross-lists)
- For backfill or targeted search: use [[arxiv-py]] against the [[arxiv-api]]

(source: arxiv-rss-feeds.md, arxiv-py-library.md)

### Stage 2: Pre-filter

**Goal**: Remove obvious noise cheaply. Reduce candidate set by ~75%.

**Approaches** (in order of simplicity):

1. **Category filter** — only keep papers in target categories
2. **Keyword filter** — require/exclude keywords in title or abstract
   (regex or simple substring matching)
3. **TF-IDF similarity** — score against a reference set of liked papers;
   drop anything below a threshold

This stage should be fast and local — no API calls or LLM inference.
(source: arxiv-sanity-lite.md, flexible-arxiv-rss.md)

### Stage 3: Rank

**Goal**: Score remaining candidates by relevance and quality.

LLM scoring uses a structured prompt with the paper's title + abstract +
categories and a user interest profile (topics, keywords, what makes a paper
interesting). Output: relevance score (1–5) + one-line justification.
(source: semantic-scholar-api.md)

SPECTER2 embeddings from [[semantic-scholar]] provide an alternative for
semantic similarity ranking without LLM cost.

### Stage 4: Output

**Goal**: Render the top N papers as a readable digest.

Formats:
- **CLI/terminal** — richly formatted with title, score, reason,
  abstract snippet, arXiv link
- **Markdown file** — for archiving or publishing
- **Email** — via SendGrid or similar (as in arxiv-sanity-lite)

## See also

- [[arxiv-rss-feeds]] — stage 1 data source
- [[arxiv-py]] — stage 1 alternative (search queries)
- [[paper-ranking]] — stage 3 approaches in depth
- [[existing-tools]] — landscape of arXiv curation tools
- [[arxiv-data-access]] — all access methods compared

Last updated: 2026-07-10
