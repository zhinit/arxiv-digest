# digest

Run the arXiv digest pipeline: fetch recent papers, filter by keywords, rank,
select top + random picks, and present a curated reading list.

## 1. Run the pipeline

Execute the Python pipeline to fetch and filter papers:

```
cd ${CLAUDE_PROJECT_DIR} && .venv/bin/python -m src.main
```

## 2. Parse and summarize

Parse the JSON output from the pipeline. For each paper in both `top_ranked`
and `random_picks`, generate a 2–4 sentence summary from the paper's abstract.
The summary should explain what the paper does and why it matters — do not
just repeat the abstract verbatim.

## 3. Present the digest

Display the results as two markdown sections. Use this format:

### Top Ranked

For each paper in `top_ranked` (in order):

**{title}**
*{authors joined by ", "}* | {categories joined by ", "} | Score: {score}
[arXiv link]({link})

{2–4 sentence summary}

---

### Random Picks

Same format as above for each paper in `random_picks`.

### Stats

At the end, show: total papers fetched, total matching keywords, number
presented.

## Notes

- If the pipeline returns zero matches, say so and suggest running
  `/expand-keywords` to broaden the keyword list.
- If the pipeline errors, show the error message.
