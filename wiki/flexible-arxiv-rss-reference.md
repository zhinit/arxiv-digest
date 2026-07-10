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

## See also

- [[curation-pipeline]] — pipeline architecture
- [[arxiv-oai-pmh]] — the data source it uses
- [[arxiv-rss-feeds]] — lighter-weight alternative to OAI-PMH for daily papers

Last updated: 2026-07-10
