# arXiv API

The arXiv search API provides programmatic access to paper metadata via HTTP
GET/POST requests. No authentication required.

## Endpoint

```
http://export.arxiv.org/api/query
```

Use `export.arxiv.org`, not the main site — it's the designated endpoint for
programmatic access. (source: arxiv-bulk-data-access.md)

## Query Parameters

| Parameter | Default | Notes |
|-----------|---------|-------|
| `search_query` | — | Field-prefixed search string |
| `id_list` | — | Comma-delimited arXiv IDs |
| `start` | 0 | 0-based result offset |
| `max_results` | 10 | Max 2000 per request |
| `sortBy` | relevance | `relevance`, `lastUpdatedDate`, `submittedDate` |
| `sortOrder` | descending | `ascending` or `descending` |

(source: arxiv-api-user-manual.md)

## Search Fields

| Prefix | Searches |
|--------|----------|
| `ti:` | Title |
| `au:` | Author |
| `abs:` | Abstract |
| `co:` | Comment |
| `jr:` | Journal reference |
| `cat:` | Category |
| `all:` | All fields |

Boolean operators: `AND`, `OR`, `ANDNOT`. Parentheses via `%28`/`%29`.
Phrases via `%22`: `ti:%22quantum+criticality%22`.

Date filtering: `submittedDate:[YYYYMMDDTTTT+TO+YYYYMMDDTTTT]` (24-hour GMT).
(source: arxiv-api-user-manual.md)

## Response Format

Atom 1.0 XML. Each entry contains:

- `<title>`, `<summary>` (abstract), `<author>` (with `<name>`)
- `<id>` — abstract URL: `http://arxiv.org/abs/{id}`
- `<published>` (v1 date), `<updated>` (this version's date)
- `<link>` — up to 3: abstract, PDF, DOI
- `<category>`, `<arxiv:primary_category>`
- `<arxiv:comment>`, `<arxiv:journal_ref>`, `<arxiv:doi>`

Feed-level: `<opensearch:totalResults>`, `<opensearch:startIndex>`,
`<opensearch:itemsPerPage>`. (source: arxiv-api-user-manual.md)

## Pagination and Rate Limits

- Max 2,000 results per request, 30,000 total per query
- 3-second delay between consecutive requests
- Results don't update intra-day; caching recommended
- Exceeding 30,000 results returns HTTP 400

(source: arxiv-api-user-manual.md)

## Versioning

Omit version suffix for latest: `cond-mat/0207270`. Append `v{n}` for
specific version: `cond-mat/0207270v1`. (source: arxiv-api-user-manual.md)

## See also

- [[arxiv-py]] — Python wrapper for this API
- [[arxiv-rss-feeds]] — daily new-paper feeds (simpler for "what's new")
- [[arxiv-oai-pmh]] — bulk metadata harvesting
- [[arxiv-data-access]] — overview of all access methods

Last updated: 2026-07-10
