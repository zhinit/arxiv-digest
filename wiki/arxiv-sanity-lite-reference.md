# arxiv-sanity-lite

Andrej Karpathy's paper curation tool. Reference implementation of TF-IDF +
SVM recommendations for arXiv papers. (source: arxiv-sanity-lite.md)

## Architecture

```
arxiv_daemon.py (cron) → arXiv API → papers.db (SQLite)
compute.py              → TF-IDF vectors → features.p (pickle)
Flask app               → SVM scoring → ranked UI
send_emails.py (cron)   → SendGrid → daily digest emails
```

(source: arxiv-sanity-lite.md)

## Data Pipeline

1. `arxiv_daemon.py` polls arXiv API periodically (via cron)
2. Papers stored in SQLite via `sqlitedict`
3. `compute.py` computes TF-IDF features from abstracts, serializes to
   `features.p` pickle file

## Recommendation Engine

- TF-IDF vectorization of abstracts (scikit-learn)
- SVM classifiers trained on user-tagged papers
- User tags = positive examples; untagged = implicit negatives
- SVM learns preference boundary in TF-IDF space

(source: arxiv-sanity-lite.md)

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| TF-IDF over abstracts only | Fast, sufficient for topic matching |
| SVM for personalization | Works well with small labeled sets |
| SQLite | Single file, no server, runs on $5 VPS |
| Daemon + cron | Simple polling, no event system |
| feedparser for API | Parses Atom XML responses |

## Scale

Runs on Linode Nanode 1 GB ($5/month). Indexes ~30K papers.
(source: arxiv-sanity-lite.md)

## Tech Stack

Python, Flask, feedparser, scikit-learn, sqlitedict, numpy, SendGrid.

## Limitations

- No semantic understanding (vocabulary mismatch problem with TF-IDF)
- No quality or novelty scoring
- No explanation of why a paper was recommended

(source: arxiv-sanity-lite.md)

## See also

- [[paper-ranking]] — comparison of ranking approaches
- [[curation-pipeline]] — pipeline architecture

Last updated: 2026-07-10
