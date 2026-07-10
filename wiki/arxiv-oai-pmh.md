# arXiv OAI-PMH

The Open Archives Initiative Protocol for Metadata Harvesting. The preferred
method for bulk metadata download or maintaining a local mirror.
(source: arxiv-oai-pmh.md)

## Endpoint

```
https://oaipmh.arxiv.org/oai
```

Updated March 2025 from legacy `http://export.arxiv.org/oai2`.
(source: arxiv-oai-pmh.md)

## Verbs

| Verb | Purpose |
|------|---------|
| `ListRecords` | Retrieve multiple records |
| `GetRecord` | Fetch single record |
| `ListMetadataFormats` | View available formats |
| `ListSets` | Browse category sets |
| `Identify` | Repository info |

## Metadata Formats

1. **oai_dc** — Simple Dublin Core. Basic fields.
2. **arXiv** — Author names, categories, license. Latest version only.
3. **arXivRaw** — Close to internal format. Includes complete version history.

(source: arxiv-oai-pmh.md)

## Selective Harvesting

Hierarchical set pattern: `group:archive:CATEGORY`

- `cs:cs:AI` — single category
- `physics:hep-th` — entire archive
- `physics` — all physics
- Omit set — all content

(source: arxiv-oai-pmh.md)

## Incremental Harvesting

After initial harvest, maintain with `from` parameter set to date of last
harvest. Metadata available after announcement (~10:30pm ET, Sun–Thu).

Resumption tokens expire daily. (source: arxiv-oai-pmh.md)

## Caveats

- Datestamps don't correspond to original submission times for older articles
- `earliestDatestamp` is 2005-09-16 (expanded March 2025)
- Rate limit: bursts of 4 req/sec with 1-second sleep per burst

(source: arxiv-oai-pmh.md, arxiv-bulk-data-access.md)

## Use for Curation

OAI-PMH is overkill for a daily digest tool — it's designed for bulk
harvesting or maintaining a local mirror. For daily new papers, [[arxiv-rss-feeds]]
or the [[arxiv-api]] are simpler. OAI-PMH becomes relevant if you want to
build a local index of all papers in a category over time (e.g., to compute
embeddings across the full corpus).

## See Also

- [[arxiv-data-access]] — comparison of all access methods
- [[arxiv-rss-feeds]] — lighter-weight daily feeds
