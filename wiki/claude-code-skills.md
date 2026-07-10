# Claude Code Skills (Commands)

Skills extend Claude Code's capabilities via reusable prompt templates stored as
markdown files. Custom commands (`.claude/commands/`) have been merged into skills
(`.claude/skills/`); both formats work identically, but skills add optional
features: supporting files, YAML frontmatter, and automatic invocation by Claude.
(source: claude-code-skills-official-docs.md)

## When to create a skill

Create a skill when you keep pasting the same instructions, checklist, or
multi-step procedure into chat, or when a section of CLAUDE.md has grown into a
procedure rather than a fact. Unlike CLAUDE.md content, a skill's body loads only
when used, so long reference material costs almost nothing until needed.
(source: claude-code-skills-official-docs.md)

## File format

A skill is a directory with `SKILL.md` as the entrypoint. The filename for
commands (`.claude/commands/deploy.md`) or directory name for skills
(`.claude/skills/deploy/`) becomes the command name you type after `/`.

```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output
└── scripts/
    └── validate.sh    # Script Claude can execute
```

(source: claude-code-skills-official-docs.md)

## Where skills live

| Location   | Path                                     | Applies to                     |
|:-----------|:-----------------------------------------|:-------------------------------|
| Enterprise | Managed settings                         | All users in your organization |
| Personal   | `~/.claude/skills/<name>/SKILL.md`       | All your projects              |
| Project    | `.claude/skills/<name>/SKILL.md`         | This project only              |
| Plugin     | `<plugin>/skills/<name>/SKILL.md`        | Where plugin is enabled        |

Priority: enterprise > personal > project. A skill at any level overrides a
bundled skill with the same name. If a skill and a command share the same name,
the skill takes precedence. (source: claude-code-skills-official-docs.md)

## YAML frontmatter

All fields are optional. Only `description` is recommended. See
[[skill-frontmatter-reference]] for the complete field list.

```yaml
---
name: my-skill
description: What this skill does and when to use it
disable-model-invocation: true
allowed-tools: Read Grep
---
```

(source: claude-code-skills-official-docs.md)

## String substitutions

| Variable              | Description                                    |
|:----------------------|:-----------------------------------------------|
| `$ARGUMENTS`          | All arguments passed when invoking             |
| `$ARGUMENTS[N]` / `$N` | Specific argument by 0-based index           |
| `$name`               | Named argument from `arguments` frontmatter    |
| `${CLAUDE_SESSION_ID}` | Current session ID                            |
| `${CLAUDE_EFFORT}`    | Current effort level                           |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md              |
| `${CLAUDE_PROJECT_DIR}` | Project root directory                       |

Indexed arguments use shell-style quoting. Escape literal `$` with backslash.
(source: claude-code-skills-official-docs.md)

## Dynamic context injection

The `` !`command` `` syntax runs shell commands before content is sent to Claude.
Output replaces the placeholder. Multi-line commands use fenced blocks with
` ```! `. (source: claude-code-skills-official-docs.md)

## Invocation control

| Frontmatter                      | You invoke | Claude invokes | Context behavior |
|:---------------------------------|:-----------|:---------------|:-----------------|
| (default)                        | Yes        | Yes            | Description always loaded; full body on invocation |
| `disable-model-invocation: true` | Yes        | No             | Description not loaded; body on your invocation |
| `user-invocable: false`          | No         | Yes            | Description always loaded; body when Claude invokes |

(source: claude-code-skills-official-docs.md)

## Skill content lifecycle

Rendered SKILL.md enters conversation as a single message and stays for the rest
of the session. Claude Code does not re-read the file on later turns.
Auto-compaction re-attaches the most recent invocation of each skill (first 5,000
tokens each, 25,000 tokens combined budget), starting from most recently invoked.
(source: claude-code-skills-official-docs.md)

## Subagent execution (context: fork)

Set `context: fork` to run in isolation. Skill content becomes the subagent's
prompt; it won't have access to conversation history. Only works for skills with
explicit task instructions — guidelines without a task produce no output. The
`agent` field specifies which subagent: Explore, Plan, general-purpose, or custom.
(source: claude-code-skills-official-docs.md)

## Skill stacking

Up to six skills can be chained: `/skill-a /skill-b do XYZ` loads both and
passes trailing text as `$ARGUMENTS` to each. (source: claude-code-skills-official-docs.md)

## See also

- [[writing-effective-skills]] — best practices for authoring skills
- [[skill-frontmatter-reference]] — complete frontmatter field reference
- [[skill-discovery-and-context]] — how skills are surfaced in the system prompt

Last updated: 2026-07-10
