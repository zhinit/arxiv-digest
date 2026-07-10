# arxiv-digest

A personal arXiv curation tool. Searches arXiv for papers matching your
interests, scores them by keyword relevance, and produces a short digest of
things worth reading.

Designed to run as a [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
slash command. Python handles fetching and filtering; Claude handles
summarization and presentation. No external API keys required.

## How it works

1. **Fetch** — queries the arXiv search API for recent papers
2. **Filter** — keeps papers whose title or abstract matches at least one keyword
3. **Score** — 3 points per title hit, 1 per abstract hit
4. **Select** — takes the top-ranked papers plus a random sample from the rest
5. **Summarize** — Claude generates a 2–4 sentence summary of each paper

## Setup

Python 3.10+. No external dependencies (stdlib only).

```
git clone <repo-url>
cd arxiv-digest
```

## Configuration

Edit `config.json`:

| Field | Type | Description |
|-------|------|-------------|
| `topics` | list of strings | Keywords/phrases to match against titles and abstracts |
| `date_range` | string | `"past week"`, `"past month"`, or an explicit date range |
| `top_n` | integer | Number of top-ranked papers to return |
| `random_n` | integer | Number of random papers from the remaining matches |

## Usage

### As a Claude Code command

```
/digest
```

Runs the full pipeline and presents a formatted digest in chat.

```
/expand-keywords
```

Uses Claude to suggest synonyms and related terms for your topic list, then
writes accepted terms back to `config.json`.

### Standalone

```
uv run python -m src.main [config.json]
```

Outputs scored papers as JSON. Summaries are not included (those are generated
by Claude during `/digest`).

## Tests

```
uv run python -m pytest tests/
```

## Project structure

```
config.json          — user configuration (topics, date range, limits)
src/
  main.py            — pipeline entry point
  config.py          — config loading/validation
  fetch.py           — arXiv API client
  score.py           — keyword matching and scoring
  select.py          — top-N and random selection
tests/               — unit tests
docs/spec.md         — detailed spec
wiki/                — research notes on arXiv APIs, ranking, etc.
.claude/commands/    — Claude Code slash commands
```
