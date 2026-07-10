# Skill Discovery and Context Engineering

How Claude Code loads, surfaces, and manages skills within its system prompt.
(source: claude-code-system-prompt-architecture.md, claude-code-skills-official-docs.md)

## System prompt assembly

Claude Code dynamically assembles its system prompt from ~30 conditional
sections. Skills are one layer in a multi-layer context system
(source: claude-code-system-prompt-architecture.md):

- **System prompt sections** (~30, conditionally included)
- **Tool definitions** (~50, conditionally included)
- **User instructions** (CLAUDE.md / AGENT.md)
- **Conversation history** (managed via compaction/summarization)
- **Attachments** (behaviors, files, MCPs, agents, skills)

## How skills enter context

At startup, only the `name` and `description` from all skills' YAML frontmatter
are loaded into the system prompt as a listing. Full SKILL.md content loads only
when invoked — either by the user typing `/skill-name` or by Claude deciding
the skill is relevant to the current request.
(source: claude-code-skills-official-docs.md)

This means description quality directly determines whether a skill gets used.
Claude matches the user's prompt against descriptions to decide which skills to
load. (source: claude-code-skill-authoring-best-practices.md)

## Context budget for skill listings

The skill listing has a character budget that scales at 1% of the model's
context window. When the listing overflows, descriptions are dropped starting
with the least-invoked skills — most-used skills keep their full text.
(source: claude-code-skills-official-docs.md)

Each entry's combined `description` + `when_to_use` text is capped at 1,536
characters regardless of budget. Both limits are configurable:
- `skillListingBudgetFraction` — fraction of context (e.g., `0.02` = 2%)
- `skillListingMaxDescChars` — per-entry character cap
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` — env var for fixed character count

(source: claude-code-skills-official-docs.md)

## Skill surfacing mechanisms

The system includes three mechanisms for surfacing skills
(source: claude-code-system-prompt-architecture.md):

1. **Startup listing**: name + description of all skills loaded into system prompt
2. **Automatic surfacing**: each turn, "Skills relevant to your task" reminders
3. **DiscoverSkills**: function for finding skills related to mid-task pivots

## Lifecycle after invocation

Once invoked, rendered SKILL.md enters the conversation as a single message and
stays for the rest of the session. Claude Code does not re-read the file on
later turns. (source: claude-code-skills-official-docs.md)

If the same skill is re-invoked with identical rendered content, a short note
replaces the duplicate. If content differs (different arguments, changed dynamic
context output), the full content appends again.
(source: claude-code-skills-official-docs.md)

## Behavior during compaction

When conversation is summarized to free context, Claude Code re-attaches the
most recent invocation of each skill after the summary
(source: claude-code-skills-official-docs.md):

- First 5,000 tokens of each skill retained
- Combined budget of 25,000 tokens across all skills
- Budget fills from most recently invoked; older skills may be dropped
- Re-invoke a skill after compaction to restore full content

## Implications for skill authors

1. **Description is the trigger.** Write it for Claude, not humans. Include
   concrete trigger phrases matching what users would naturally say.
2. **Conciseness matters.** Once loaded, every token competes with conversation
   context. State what to do, not how or why.
3. **Standing instructions, not one-time.** Content persists across turns, so
   write guidance as ongoing rules.
4. **Strengthening over strengthening.** If a skill stops influencing behavior,
   strengthen the description and instructions — the content is usually still
   present but Claude is choosing other approaches.

(source: claude-code-skills-official-docs.md, claude-code-skill-authoring-best-practices.md)

## See also

- [[claude-code-skills]] — overview and file format
- [[writing-effective-skills]] — best practices for authoring
- [[skill-frontmatter-reference]] — complete frontmatter field reference

Last updated: 2026-07-10
