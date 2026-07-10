# arxiv.py

Python wrapper for the [[arxiv-api]]. Version 4.0.0 (May 2026). MIT license.
Requires Python >= 3.10. (source: arxiv-py-library.md)

## Install

```bash
pip install arxiv
```

## Core Objects

**Client** — manages connection pooling, pagination, retry, rate limiting.

```python
client = arxiv.Client(
    page_size=1000,
    delay_seconds=10.0,
    num_retries=5,
)
```

**Search** — defines a query.

```python
search = arxiv.Search(
    query="cat:cs.AI AND ti:transformer",
    max_results=100,
    sort_by=arxiv.SortCriterion.SubmittedDate,
)
```

Supports the same query syntax as the raw API: field prefixes (`ti:`, `au:`,
`abs:`, `cat:`), boolean operators (`AND`, `OR`, `ANDNOT`).

Also supports ID-based lookup: `id_list=["1605.08386v1"]`.

**Result** — paper metadata. Fields: `title`, `summary`, `authors`,
`categories`, `published`, `updated`, `pdf_url`, `entry_id`.

## Usage Pattern

```python
import arxiv

client = arxiv.Client()
search = arxiv.Search(query="quantum", max_results=10)

for paper in client.results(search):
    print(paper.title)
    print(paper.summary)
    print(paper.pdf_url)
```

Results are generators — memory-efficient for large result sets.
(source: arxiv-py-library.md)

## Best Practices

- Reuse a single `Client` instance (connection pooling + rate compliance)
- Default `delay_seconds` respects arXiv rate limits
- Enable DEBUG logging to inspect API calls

## See Also

- [[arxiv-api]] — the underlying HTTP API
- [[curation-pipeline]] — where arxiv.py fits in a digest tool
