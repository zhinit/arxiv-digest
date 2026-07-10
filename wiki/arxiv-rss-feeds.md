# arXiv RSS Feeds

Daily feeds of new, replacement, and cross-listed papers per category. The
simplest way to get "what was posted today." Updated at midnight ET.
(source: arxiv-rss-feeds.md)

## URLs

- RSS 2.0: `https://rss.arxiv.org/rss/{category}`
- Atom: `https://rss.arxiv.org/atom/{category}`

Examples:
- All CS: `https://rss.arxiv.org/rss/cs`
- Just AI: `https://rss.arxiv.org/rss/cs.AI`
- AI + Neuroscience: `https://rss.arxiv.org/rss/cs.AI+q-bio.NC`

Limit: 2000 results per request. (source: arxiv-rss-feeds.md)

## Entry Fields

Each item includes:

| Field | Content |
|-------|---------|
| `title` | Paper title |
| `link` | Abstract page URL |
| `description` | arXiv ID + announce type + full abstract |
| `dc:creator` | Authors (comma-separated) |
| `category` | Subject classifications (multiple allowed) |
| `arxiv:announce_type` | `new`, `replacement`, or `cross` |
| `arxiv:DOI` | DOI if published (optional) |
| `arxiv:journal_reference` | Journal citation (optional) |

(source: arxiv-rss-feeds.md)

## Schedule

- Updated daily at midnight EST
- No feeds on Saturdays, Sundays, or occasional holidays
- New articles announced ~10:30pm ET Sun–Thu, appear in next day's feed

(source: arxiv-rss-feeds.md)

## Comparison with Other Access Methods

RSS is a push-style daily batch: everything new in a category, once per day.
The [[arxiv-api]] is pull-style: search queries against the full corpus.
[[arxiv-oai-pmh]] is designed for bulk harvesting or maintaining local mirrors.
(source: arxiv-rss-feeds.md)

## See also

- [[arxiv-api]] — query-based search
- [[arxiv-oai-pmh]] — bulk harvesting with selective sets
- [[flexible-arxiv-rss-reference]] — open-source tool that adds filtering on top of arXiv RSS/OAI
- [[arxiv-data-access]] — overview of all access methods

Last updated: 2026-07-10
