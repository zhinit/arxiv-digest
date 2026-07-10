# Build v1 plan

Implementation plan for arxiv-digest based on `docs/spec.md`.

## Step 1: Config file

Create `config.json` at the repo root with the schema from the spec.

```json
{
  "topics": ["predictive markets", "gambling", "psychology", "AI", "DSP", "Audio", "convolution"],
  "date_range": "past week",
  "top_n": 7,
  "random_n": 3
}
```

**Test:** Write a Python function that loads and validates the config (required
fields present, correct types). Unit test with valid config, missing fields,
and bad types.

---

## Step 2: arXiv API fetch module

Python module (`src/fetch.py` or similar) that:
- Translates `date_range` into an arXiv `submittedDate` range. Support
  `"past week"`, `"past month"`, and explicit `YYYYMMDD-YYYYMMDD` ranges.
- Builds the arXiv API query URL.
- Fetches results with pagination (max 2,000 per request), respecting the
  3-second delay between paginated requests.
- Parses the Atom XML response into a list of paper dicts: `title`, `authors`,
  `abstract`, `link`, `categories`, `published`.

**Test:** Unit test the date range parser (all three formats, edge cases like
month boundaries). Unit test the XML parser against a saved sample response.
Integration test with a small live query (1-2 results) to verify the API
contract hasn't changed.

---

## Step 3: Keyword filter and scoring module

Python module (`src/score.py` or similar) that:
- Takes a list of paper dicts and a list of keywords.
- For each paper, runs case-insensitive `\b`-bounded regex matching against
  title and abstract.
- Scores: 3 points per title keyword hit, 1 point per abstract keyword hit.
- Returns papers with score > 0, sorted descending by score.

**Test:** Unit test scoring with known inputs:
- Keyword in title only, abstract only, both.
- Multiple keywords matching the same paper.
- Case variation (e.g. "ai" matching "AI").
- Phrase matching (e.g. "predictive markets" as a whole phrase).
- Paper with no matches is excluded.

---

## Step 4: Selection logic

Python function that takes the scored/sorted paper list and `top_n` /
`random_n` config values. Returns two lists: top-ranked and random picks.

- Top list: first `top_n` papers from the sorted list.
- Random list: sample `random_n` from the remainder.
- Edge cases: fewer papers than `top_n`, fewer remainder than `random_n`,
  zero matches.

**Test:** Unit test all edge cases. Mock `random.sample` to make random
selection deterministic in tests. Verify the two lists are mutually exclusive.

---

## Step 5: CLI entry point

Python script (`src/digest.py` or `src/main.py`) that wires steps 2-4:
1. Load and validate config.
2. Fetch papers from arXiv.
3. Filter and score.
4. Select top + random.
5. Print results as JSON (or structured output) for Claude to consume.

This script is what the `/digest` command shells out to. It handles data
retrieval and filtering; Claude handles summarization and presentation.

**Test:** End-to-end test with a mock arXiv response to verify the full
pipeline produces expected output structure.

---

## Step 6: `/digest` slash command

Create `.claude/commands/digest.md`. The command:
1. Reads `config.json`.
2. Shells out to the Python pipeline from step 5.
3. Takes the returned papers and generates a 2-4 sentence summary for each
   from its abstract.
4. Presents two markdown sections ("Top Ranked" and "Random Picks") inline
   in the chat. Each entry: title, authors, arXiv link, categories, summary.

**Test:** Manual test — run `/digest` and verify output formatting, link
correctness, and summary quality.

---

## Step 7: `/expand-keywords` slash command

Create `.claude/commands/expand-keywords.md`. The command:
1. Reads `topics` from `config.json`.
2. For each topic, generates synonyms, morphological variants, and related
   terms.
3. Presents suggestions to the user for approval.
4. Writes accepted terms back to `config.json`.

**Test:** Manual test — run `/expand-keywords`, verify suggestions are
reasonable, accept some, reject some, confirm `config.json` is updated
correctly.

---

## Step 8: Integration testing

Run the full `/digest` flow end-to-end against live arXiv with the default
config. Verify:
- Papers returned are within the configured date range.
- All papers match at least one keyword.
- Top list is sorted by score descending.
- Random picks don't overlap with top list.
- Summaries are coherent and based on the abstracts.

---

## File structure (expected)

```
arxiv-digest/
├── config.json
├── src/
│   ├── fetch.py
│   ├── score.py
│   └── main.py
├── tests/
│   ├── test_config.py
│   ├── test_fetch.py
│   ├── test_score.py
│   └── test_selection.py
├── .claude/commands/
│   ├── digest.md
│   └── expand-keywords.md
├── docs/
│   └── spec.md
└── plans/
    └── build-v1-plan.md
```
