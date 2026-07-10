# flexible-arxiv-rss

Self-hosted arXiv filtering tool. Polls arXiv via OAI-PMH, applies keyword
and category filters, outputs a filtered RSS feed.
(source: flexible-arxiv-rss.md)

## Architecture

```
poll_arxiv_oai.sh (cron) → arXiv OAI → raw metadata
C++ filter engine         → preferences.xml → filtered papers
nginx                     → RSS feed on port 8080
```

(source: flexible-arxiv-rss.md)

## Filtering

Configured via `preferences.xml`:

| Setting | Purpose |
|---------|---------|
| `star_include` | Keywords to star/highlight |
| `content_exclude` | Keywords to remove papers |
| `categories_must_include` | Required arXiv categories |
| `categories_exclude` | Blocked categories |
| `allow_crosspost` | Show multi-category papers |
| `allow_replacements` | Show revisions |
| `only_accepted` | Only show published papers |
| `keep_history` | How long to retain papers (e.g., "3 days ago") |

(source: flexible-arxiv-rss.md)

## Polling

Uses OAI-PMH interface (not RSS or search API). First run fetches past 5
days. Subsequent runs get daily updates. Maintains up to 2 weeks of history.
(source: flexible-arxiv-rss.md)

## Relevance to This Project

Demonstrates a keyword-based filtering approach. The configuration model
(include/exclude keywords + categories) is a useful pattern, though the C++
implementation and nginx dependency are heavier than needed for a CLI tool.

The key lesson: **category + keyword filtering is the minimum viable
pipeline**. It removes the bulk of irrelevant papers before any ML scoring.

## See Also

- [[curation-pipeline]] — where keyword filtering fits
- [[arxiv-oai-pmh]] — the data source it uses
- [[arxiv-rss-feeds]] — lighter-weight alternative to OAI-PMH for daily papers
