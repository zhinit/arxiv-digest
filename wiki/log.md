# Wiki Log

## 2026-07-10 — Keyword ranking research

**Sources archived:**
- elastic-practical-bm25-part2.md — BM25 formula breakdown with parameter tuning examples
- tfidf-bm25-rag-guide.md — TF-IDF vs BM25 comparison with Python code
- lucene-scoring.md — Apache Lucene scoring architecture
- lucene-search-and-ranking-blaszyk.md — Lucene BM25 internals
- rank-bm25-library.md — Pure Python BM25 library (5 variants)
- bm25s-library.md — High-performance BM25 via sparse matrices
- keyword-search-implementation-guide.md — Full implementation guide: tokenization, inverted indexes, hybrid retrieval, RRF
- robertson-zaragoza-bm25-2009.md — Foundational BM25 paper reference (paywalled)

**Wiki pages created:**
- bm25 — formula, parameters, variants, usage in search systems
- tfidf — formula, limitations, relationship to BM25
- keyword-search — how it works, strengths/weaknesses, when to use
- inverted-index — data structure, optimizations, implementations
- tokenization — preprocessing steps, order considerations, library support
- bm25-python-libraries — rank-bm25 vs bm25s comparison with code examples
- hybrid-retrieval — architecture, RRF, weighted fusion, query routing

---

## 2026-07-10 — Claude Code skills/commands research

**Sources archived:**
- claude-code-skills-official-docs.md — Official Anthropic docs: skill format, frontmatter, substitutions, invocation control, lifecycle, subagents
- claude-code-skill-authoring-best-practices.md — Official Anthropic best practices: conciseness, descriptions, progressive disclosure, patterns, evaluation
- claude-code-system-prompt-architecture.md — How Claude Code assembles its system prompt and surfaces skills

**Wiki pages created:**
- claude-code-skills — overview of skills/commands system
- skill-frontmatter-reference — complete YAML frontmatter field reference
- writing-effective-skills — authoring best practices and patterns
- skill-discovery-and-context — system prompt assembly and context budgets

---

## 2026-07-10

**Research: how to build an arXiv curation tool**

Sources archived (10):
- arxiv-api-user-manual.md — arXiv API User's Manual
- arxiv-api-basics.md — arXiv API Basics
- arxiv-rss-feeds.md — arXiv RSS Feeds + RSS Specifications
- arxiv-bulk-data-access.md — arXiv Bulk Data Access
- arxiv-oai-pmh.md — arXiv OAI-PMH Interface
- arxiv-py-library.md — arxiv.py Python wrapper
- awesome-arxiv.md — Curated list of arXiv tools and resources
- arxiv-sanity-lite.md — Karpathy's arxiv-sanity-lite architecture
- flexible-arxiv-rss.md — flexible-arxiv-rss filtered feed tool
- semantic-scholar-api.md — Semantic Scholar API and SPECTER embeddings

Wiki pages created (11):
- curation-pipeline — end-to-end pipeline architecture
- paper-ranking — ranking approaches (TF-IDF, embeddings, LLM)
- arxiv-api — search API reference
- arxiv-rss-feeds — daily RSS feeds
- arxiv-oai-pmh — bulk harvesting
- arxiv-data-access — access methods overview
- arxiv-py — Python wrapper
- semantic-scholar — Semantic Scholar API
- arxiv-sanity-lite-reference — reference implementation
- flexible-arxiv-rss-reference — reference implementation
- existing-tools — tool landscape and gap analysis

---

## 2026-07-10 — Wiki lint fixes

- Fixed broken link: `[[flexible-arxiv-rss]]` → `[[flexible-arxiv-rss-reference]]` in arxiv-rss-feeds
- Defined wiki page format in CLAUDE.md (title, lead, body with inline citations, See also, Last updated)
- Standardized cross-reference sections to `## See also` across all 22 pages
- Added `Last updated: 2026-07-10` to all pages
- Added `(source: ...)` to uncited claims in bm25 (BM25L/BM25+), tfidf (limitation 1), keyword-search (weaknesses)
- Removed separation-of-concerns violations: stripped "Recommended approach" language and project-specific config/cost/tech-stack from curation-pipeline; removed "Relevance to This Project" from flexible-arxiv-rss-reference; neutralized "Use for Curation" / "Which to Use" sections in arxiv-rss-feeds, semantic-scholar, arxiv-oai-pmh, arxiv-data-access; neutralized recommendation language in paper-ranking
- Moved project-specific pipeline config, cost estimates, and tech stack to docs/pipeline-design.md
