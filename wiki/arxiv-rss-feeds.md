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

## Use for Curation

RSS is the natural ingestion path for a daily digest tool:

1. Subscribe to categories of interest
2. Parse the feed (feedparser in Python, or any RSS library)
3. Filter on `arxiv:announce_type` — typically want `new` only, skip
   `replacement` and `cross` unless tracking updates
4. Extract abstract from `description` field for downstream scoring

Compared to the [[arxiv-api]]: RSS is push-style (daily batch), the API is
pull-style (search queries). RSS is better for "everything new in cs.AI
today"; the API is better for "papers about transformers by author X."

## See Also

- [[arxiv-api]] — query-based search
- [[arxiv-oai-pmh]] — bulk harvesting with selective sets
- [[flexible-arxiv-rss]] — open-source tool that adds filtering on top of arXiv RSS/OAI
