# Wiki Index

## Information Retrieval & Ranking

- [[bm25]] — BM25 ranking algorithm: formula, parameters (k1, b), saturation, length normalization
- [[tfidf]] — TF-IDF scoring: term frequency × inverse document frequency
- [[keyword-search]] — Lexical retrieval: tokenization → inverted index → scoring → ranking
- [[inverted-index]] — Data structure mapping terms to document posting lists
- [[tokenization]] — Text preprocessing: lowercasing, stemming, stopwords, n-grams
- [[hybrid-retrieval]] — Combining keyword and semantic search (RRF, weighted fusion, reranking)
- [[bm25-python-libraries]] — rank-bm25 (simple) vs bm25s (fast) vs Elasticsearch (production)

## Architecture

- [[curation-pipeline]] — End-to-end pipeline: ingest → pre-filter → rank → output
- [[paper-ranking]] — Ranking approaches compared: TF-IDF, embeddings, LLM scoring

## arXiv Data Access

- [[arxiv-data-access]] — Overview of all programmatic access methods
- [[arxiv-api]] — Search API: query syntax, response format, rate limits
- [[arxiv-rss-feeds]] — Daily new-paper feeds by category
- [[arxiv-oai-pmh]] — OAI-PMH bulk metadata harvesting
- [[arxiv-py]] — Python wrapper for the arXiv API (v4.0.0)

## External Services

- [[semantic-scholar]] — Semantic Scholar API: SPECTER2 embeddings, recommendations, citations

## Claude Code Skills & Commands

- [[claude-code-skills]] — Skills/commands overview: file format, locations, substitutions, invocation control, lifecycle
- [[skill-frontmatter-reference]] — Complete YAML frontmatter field reference for SKILL.md
- [[writing-effective-skills]] — Best practices: conciseness, descriptions, progressive disclosure, patterns, evaluation
- [[skill-discovery-and-context]] — How skills are surfaced in the system prompt, context budgets, compaction behavior

## Reference Implementations

- [[arxiv-sanity-lite-reference]] — Karpathy's TF-IDF + SVM recommender
- [[flexible-arxiv-rss-reference]] — OAI-based polling with keyword/category filters
- [[existing-tools]] — Landscape of arXiv curation tools, SDKs, and datasets
