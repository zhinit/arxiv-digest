# Writing Effective Skills

Best practices for authoring Claude Code skills that Claude can discover and use
successfully. (source: claude-code-skill-authoring-best-practices.md)

## Core principles

### Conciseness

The context window is a public good. Once Claude loads SKILL.md, every token
competes with conversation history and other context. Default assumption: Claude
is already smart. Only add context it doesn't already have.
(source: claude-code-skill-authoring-best-practices.md)

Challenge each piece of information:
- "Does Claude really need this explanation?"
- "Can I assume Claude knows this?"
- "Does this paragraph justify its token cost?"

Keep SKILL.md body under 500 lines. Move detailed reference material to
separate files. (source: claude-code-skill-authoring-best-practices.md)

### Degrees of freedom

Match specificity to the task's fragility and variability
(source: claude-code-skill-authoring-best-practices.md):

- **High freedom** (text-based instructions): multiple approaches valid,
  decisions depend on context. Example: code review checklists.
- **Medium freedom** (pseudocode/scripts with parameters): preferred pattern
  exists, some variation acceptable. Example: report generation templates.
- **Low freedom** (specific scripts, few parameters): operations fragile,
  consistency critical. Example: database migrations, deploy scripts.

### Test across models

What works for Opus might need more detail for Haiku. Test with all models you
plan to use. (source: claude-code-skill-authoring-best-practices.md)

## Writing the description

The `description` field is the single most important field. Claude uses it to
select skills from potentially 100+ available. Write it for Claude, not for
humans — concrete trigger phrases, not marketing copy.
(source: claude-code-skill-authoring-best-practices.md)

Rules:
- **Third person always.** The description is injected into the system prompt;
  inconsistent POV causes discovery problems.
  - Good: "Processes Excel files and generates reports"
  - Bad: "I can help you process Excel files"
- **Include both what and when.** First sentence: what. Second: trigger phrases.
- **Be specific.** "Extract text and tables from PDF files, fill forms, merge
  documents. Use when working with PDF files or when the user mentions PDFs,
  forms, or document extraction." — not "Helps with documents."

(source: claude-code-skill-authoring-best-practices.md)

## Naming conventions

Consider gerund form (verb + -ing): `processing-pdfs`,
`analyzing-spreadsheets`, `managing-databases`. Acceptable alternatives:
noun phrases (`pdf-processing`) or action-oriented (`process-pdfs`). Avoid
vague names (`helper`, `utils`) and overly generic (`documents`, `data`).
(source: claude-code-skill-authoring-best-practices.md)

## Progressive disclosure

SKILL.md serves as an overview pointing Claude to detailed materials. Three
patterns (source: claude-code-skill-authoring-best-practices.md):

1. **High-level guide with references**: SKILL.md has quick start; links to
   FORMS.md, REFERENCE.md, EXAMPLES.md for advanced features.
2. **Domain-specific organization**: `reference/finance.md`,
   `reference/sales.md`, etc. Claude reads only the relevant domain file.
3. **Conditional details**: basic content inline, advanced content linked.

Keep references **one level deep** from SKILL.md. Nested references cause
Claude to partially read files. For files >100 lines, include a table of
contents at the top. (source: claude-code-skill-authoring-best-practices.md)

## Common patterns

### Template pattern
Provide output format templates. Match strictness to requirements — strict for
data formats, flexible for analysis reports.
(source: claude-code-skill-authoring-best-practices.md)

### Examples pattern
Input/output pairs, just like in regular prompting. Help Claude understand
desired style and detail level more clearly than descriptions alone.
(source: claude-code-skill-authoring-best-practices.md)

### Conditional workflow
Guide Claude through decision points: "Creating new content? → Creation
workflow. Editing existing? → Editing workflow."
(source: claude-code-skill-authoring-best-practices.md)

### Checklists for complex tasks
Provide checklists Claude can copy into its response and track progress through.
Prevents Claude from skipping critical validation steps.
(source: claude-code-skill-authoring-best-practices.md)

### Feedback loops
Run validator → fix errors → repeat. This pattern greatly improves output
quality. Works with scripts (run validate.py) or reference docs (check against
STYLE_GUIDE.md). (source: claude-code-skill-authoring-best-practices.md)

## Dynamic context injection

The `` !`command` `` syntax preprocesses shell commands before Claude sees the
content. Use this to ground skills in live data — git diffs, PR metadata, system
state. Claude receives actual data, not placeholders.
(source: claude-code-skills-official-docs.md)

## Evaluation and iteration

### Evaluation-driven development

Create evaluations BEFORE writing documentation
(source: claude-code-skill-authoring-best-practices.md):

1. Identify gaps — run Claude without the skill, document failures
2. Create evaluations — three scenarios testing those gaps
3. Establish baseline — measure performance without the skill
4. Write minimal instructions — just enough to pass evaluations
5. Iterate — evaluate, compare, refine

### Iterative development with Claude

Use "Claude A" to create/refine, "Claude B" to test
(source: claude-code-skill-authoring-best-practices.md):

1. Complete a task without the skill (notice what you repeatedly provide)
2. Ask Claude A to create a skill capturing the pattern
3. Review for conciseness (remove explanations Claude doesn't need)
4. Test with Claude B on real tasks
5. Observe behavior, bring insights back to Claude A
6. Repeat

### Observe navigation patterns

Watch for: unexpected exploration paths, missed connections to referenced files,
overreliance on certain sections, ignored content. Iterate based on observation,
not assumptions. (source: claude-code-skill-authoring-best-practices.md)

## Anti-patterns

- **Too verbose**: explaining what Claude already knows (e.g., what PDFs are)
- **Too many options**: present a default with escape hatch, not a laundry list
- **Time-sensitive info**: use "old patterns" sections instead of date conditionals
- **Inconsistent terminology**: pick one term and use it throughout
- **Deeply nested references**: keep one level deep from SKILL.md
- **Windows-style paths**: always use forward slashes
- **Voodoo constants**: justify all magic numbers in scripts
- **Punting errors to Claude**: handle error conditions in scripts explicitly

(source: claude-code-skill-authoring-best-practices.md)

## Checklist

Core quality: description specific with key terms; includes what and when; body
under 500 lines; consistent terminology; concrete examples; references one level
deep; workflows with clear steps.

Scripts: solve problems rather than punt; explicit error handling; no magic
numbers; packages listed; validation/verification steps; feedback loops.

Testing: at least three evaluations; tested with target models; real scenarios;
team feedback if applicable.

(source: claude-code-skill-authoring-best-practices.md)

## See also

- [[claude-code-skills]] — overview and file format
- [[skill-frontmatter-reference]] — complete frontmatter field reference
- [[skill-discovery-and-context]] — how skills are surfaced in the system prompt

Last updated: 2026-07-10
