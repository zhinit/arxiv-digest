# Skill Frontmatter Reference

Complete reference for YAML frontmatter fields in SKILL.md files.
(source: claude-code-skills-official-docs.md)

## All fields

| Field                      | Required    | Description |
|:---------------------------|:------------|:------------|
| `name`                     | No          | Display name in skill listings. Defaults to directory name. Does not change what you type after `/` (that comes from directory name). |
| `description`              | Recommended | What the skill does and when to use it. Claude uses this for auto-invocation. Put key use case first. Combined with `when_to_use`, truncated at 1,536 chars. Max 1,024 chars on platform.claude.com. |
| `when_to_use`              | No          | Additional activation context. Appended to description, shares the 1,536-char cap. |
| `argument-hint`            | No          | Autocomplete hint, e.g. `[issue-number]` or `[filename] [format]`. |
| `arguments`                | No          | Named positional arguments for `$name` substitution. Space-separated string or YAML list. Maps to positions in order. |
| `disable-model-invocation` | No          | `true` prevents Claude from auto-loading. For manual-only workflows (deploy, commit). Default: `false`. |
| `user-invocable`           | No          | `false` hides from `/` menu. For background knowledge Claude should know but users shouldn't invoke directly. Default: `true`. |
| `allowed-tools`            | No          | Pre-approved tools (no permission prompt). Space- or comma-separated, or YAML list. Does not restrict — other tools remain callable. |
| `disallowed-tools`         | No          | Tools removed from Claude's pool while skill active. Clears on next user message. |
| `model`                    | No          | Model override for current turn only. Session model resumes on next prompt. |
| `effort`                   | No          | Effort level override: `low`, `medium`, `high`, `xhigh`, `max`. |
| `context`                  | No          | `fork` runs in isolated subagent. |
| `agent`                    | No          | Subagent type when `context: fork`. Options: Explore, Plan, general-purpose, or custom from `.claude/agents/`. |
| `hooks`                    | No          | Hooks scoped to skill lifecycle. |
| `paths`                    | No          | Glob patterns limiting auto-activation to matching files. |
| `shell`                    | No          | Shell for `!` commands: `bash` (default) or `powershell`. |

(source: claude-code-skills-official-docs.md)

## Platform naming requirements

On platform.claude.com, the `name` field has stricter validation
(source: claude-code-skill-authoring-best-practices.md):

- Maximum 64 characters
- Lowercase letters, numbers, hyphens only
- No XML tags
- Cannot contain reserved words: "anthropic", "claude"

## Visibility overrides from settings

The `skillOverrides` setting controls visibility without editing SKILL.md:

| Value                 | Listed to Claude     | In `/` menu |
|:----------------------|:---------------------|:------------|
| `"on"`                | Name and description | Yes         |
| `"name-only"`         | Name only            | Yes         |
| `"user-invocable-only"` | Hidden            | Yes         |
| `"off"`               | Hidden               | Hidden      |

(source: claude-code-skills-official-docs.md)

## Context budget

Skill listing character budget scales at 1% of the model's context window. When
it overflows, descriptions are dropped starting with least-invoked skills.
Configurable via `skillListingBudgetFraction` setting. Each entry's combined
`description` + `when_to_use` is capped at 1,536 characters (configurable via
`skillListingMaxDescChars`). (source: claude-code-skills-official-docs.md)

## See also

- [[claude-code-skills]] — overview and file format
- [[writing-effective-skills]] — best practices

Last updated: 2026-07-10
