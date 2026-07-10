# arXiv Data Access Methods

Overview of all programmatic access paths to arXiv content.
(source: arxiv-bulk-data-access.md, arxiv-api-user-manual.md, arxiv-rss-feeds.md, arxiv-oai-pmh.md)

## Comparison

| Method | Best for | Update frequency | Rate limit |
|--------|----------|-----------------|------------|
| [[arxiv-rss-feeds]] | Daily new papers by category | Midnight ET daily | 2000 items/request |
| [[arxiv-api]] | Targeted search queries | Real-time (but results update daily) | 3s between requests, 30K max |
| [[arxiv-oai-pmh]] | Bulk harvesting, local mirrors | ~10:30pm ET daily | 4 req/s bursts |
| S3 bulk | Complete corpus download | Periodic | N/A (direct download) |
| Kaggle dataset | Full metadata + PDFs | Snapshot | N/A |

## Which to Use

**Daily digest of new papers** → RSS feeds. One request per category per day,
get everything new. Parse with feedparser.

**Search for specific topics/authors** → Search API via [[arxiv-py]]. Good for
backfilling or finding papers matching specific criteria.

**Build a local index** → OAI-PMH for initial harvest + incremental updates.
Or Kaggle/S3 for the full corpus snapshot.

**Get embeddings/citations** → [[semantic-scholar]] API gives SPECTER2
embeddings and citation data. arXiv itself has no embedding endpoint.

## General Policies

- Use `export.arxiv.org` for programmatic access, not the main site
- Do not attempt to download the complete corpus programmatically — use S3
- arXiv license permits distribution by arXiv but does not grant
  redistribution rights; link back to arXiv
- Review the Terms of Use for arXiv APIs

(source: arxiv-bulk-data-access.md)
