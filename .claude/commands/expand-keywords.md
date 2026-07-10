# expand-keywords

Expand the topic keyword list in `config.json` with synonyms, morphological
variants, and related terms.

## 1. Read current topics

```!
cat ${CLAUDE_PROJECT_DIR}/config.json
```

## 2. Generate suggestions

For each topic in the `topics` list, suggest:

- **Synonyms** — alternative names for the same concept
- **Morphological variants** — different word forms (e.g. "convolution" →
  "convolutional", "convolved")
- **Abbreviation expansions** — if the topic is an abbreviation, expand it
  (e.g. "DSP" → "digital signal processing"), and vice versa
- **Related terms** — closely related concepts that would appear in papers
  the user would want to read

Present a table with columns: Original Topic | Suggested Addition | Type
(synonym/variant/expansion/related).

## 3. Get approval

Ask the user which suggestions to accept. They can accept all, reject all,
or pick individually.

## 4. Update config

Add the accepted terms to the `topics` list in `config.json`. Do not remove
any existing topics. Write the updated file.

Show the final topic list after updating.
