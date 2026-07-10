# arXiv Data Access Methods

Overview of all programmatic access paths to arXiv content.
(source: arxiv-bulk-data-access.md, arxiv-api-user-manual.md, arxiv-rss-feeds.md, arxiv-oai-pmh.md)

## Comparison

| Method | What it provides | Update frequency | Rate limit |
|--------|-----------------|-----------------|------------|
| [[arxiv-rss-feeds]] | Daily batch of all new papers in a category | Midnight ET daily | 2000 items/request |
| [[arxiv-api]] | Query-based search by topic, author, date, category | Real-time (but results update daily) | 3s between requests, 30K max |
| [[arxiv-oai-pmh]] | Bulk metadata harvest with incremental updates | ~10:30pm ET daily | 4 req/s bursts |
| S3 bulk | Complete corpus download | Periodic | N/A (direct download) |
| Kaggle dataset | Full metadata + PDFs | Snapshot | N/A |

(source: arxiv-bulk-data-access.md, arxiv-api-user-manual.md, arxiv-rss-feeds.md, arxiv-oai-pmh.md)

## General Policies

- Use `export.arxiv.org` for programmatic access, not the main site
- Do not attempt to download the complete corpus programmatically — use S3
- arXiv license permits distribution by arXiv but does not grant
  redistribution rights; link back to arXiv
- Review the Terms of Use for arXiv APIs

(source: arxiv-bulk-data-access.md)

## See also

- [[arxiv-rss-feeds]], [[arxiv-api]], [[arxiv-oai-pmh]], [[arxiv-py]], [[semantic-scholar]]

Last updated: 2026-07-10
