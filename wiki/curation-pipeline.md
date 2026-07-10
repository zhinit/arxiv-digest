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

**Recommended approach**: [[arxiv-rss-feeds]]. One HTTP request per category,
returns all new papers with titles, abstracts, authors, categories.

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

**Recommended approach**: LLM scoring with a structured prompt.

Input per paper: title + abstract + categories.
Prompt includes: user interest profile (topics, keywords, what makes a paper
interesting to this user).
Output: relevance score (1–5) + one-line justification.

At ~30 candidates and ~$0.003/call (Haiku-class model on short prompt),
this costs ~$0.09/day.

**Alternative/supplement**: SPECTER2 embeddings from [[semantic-scholar]] for
semantic similarity ranking without LLM cost. Good for a free tier.

(source: semantic-scholar-api.md)

### Stage 4: Output

**Goal**: Render the top N papers as a readable digest.

Formats:
- **CLI/terminal** — default, richly formatted with title, score, reason,
  abstract snippet, arXiv link
- **Markdown file** — for archiving or publishing
- **Email** — via SendGrid or similar (as in arxiv-sanity-lite)

## Configuration

A user interest profile drives stages 2–3. Minimum viable config:

```yaml
categories:
  - cs.AI
  - cs.CL
  - cs.LG

keywords:
  include:
    - transformer
    - reasoning
    - retrieval augmented
  exclude:
    - survey
    - benchmark

interests: |
  I'm interested in novel architectures for language model reasoning,
  retrieval-augmented generation, and tool use in LLM agents. I prefer
  papers with experiments over pure theory. I don't care about benchmark
  papers or survey papers unless they introduce a new taxonomy.

top_n: 10
```

`categories` and `keywords` drive stage 2. `interests` drives the LLM
prompt in stage 3. `top_n` caps the output.

## Cost Estimates

| Tier | Monthly cost | Quality |
|------|-------------|---------|
| RSS + keywords only | Free | Coarse, misses novel framing |
| + TF-IDF/embeddings | Free (local) or ~$0 (S2 API) | Better semantic matching |
| + LLM scoring (Haiku) | ~$3/month | Nuanced, with explanations |
| + LLM scoring (Sonnet) | ~$15/month | Highest quality judgments |

## Tech Stack

Minimal dependencies:
- `arxiv` (PyPI) — API wrapper
- `feedparser` — RSS parsing
- `anthropic` or `openai` — LLM scoring (optional)
- `scikit-learn` — TF-IDF (optional)
- `pyyaml` — config parsing

## See Also

- [[arxiv-rss-feeds]] — stage 1 data source
- [[arxiv-py]] — stage 1 alternative (search queries)
- [[paper-ranking]] — stage 3 approaches in depth
- [[existing-tools]] — what's already out there
- [[arxiv-data-access]] — all access methods compared
