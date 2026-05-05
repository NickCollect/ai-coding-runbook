---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/documentation-patterns.md
title: "Command documentation patterns (plugin-dev reference)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin]
concepts_referenced: []
---

Reference doc inside `plugin-dev/skills/command-development/`. Strategies for self-documenting, maintainable slash commands.

**Self-documenting command template**: include a long HTML comment block at the top with `COMMAND`, `VERSION`, `AUTHOR`, `LAST UPDATED`, `PURPOSE`, `USAGE`, `ARGUMENTS`, `EXAMPLES`, `REQUIREMENTS`, `RELATED COMMANDS`, `TROUBLESHOOTING`, `CHANGELOG`. The comment is invisible to users but visible to maintainers reading the file.

**In-line documentation patterns**:
- **Commented sections**: `<!-- SECTION 1: VALIDATION -->` etc. to break a long command into named blocks
- **Inline explanations**: comments around bash invocations explaining WHY (`<!-- We check branch status to prevent deploying from wrong branch -->`)
- **Decision-point documentation**: comment around interactive checkpoints explaining why automation can't proceed and what user input is expected

**Help text patterns**:
- **Built-in help subcommand**: `if [ "$1" = "help" ] || [ "$1" = "--help" ] || [ "$1" = "-h" ]; then ... Exit. fi` at top of command, with usage / subcommands / examples
- **Contextual help**: when no args provided, list available operations + usage + examples + exit

**Error message patterns** with helpful structure: `❌ ERROR: ...` + USAGE + EXAMPLE + suggested action + Exit. For recovery: WHAT HAPPENED, WHAT THIS MEANS, RECOVERY STEPS (numbered), NEED HELP? section.

**Usage example styles**:
- **Embedded examples**: explicit "Basic Usage" / "Advanced Usage" / "Use Cases" sections inside the command file
- **Example-driven documentation**: lead with concrete input/output pairs before describing what the command does

**Maintenance documentation in HTML comments**:
- VERSION + CHANGELOG (semver entries with dates)
- MIGRATION NOTES (old vs new command shape)
- DEPRECATION WARNINGS (which flag, when removed)
- KNOWN ISSUES (issue numbers + workarounds)
- MAINTENANCE NOTES (CODE STRUCTURE / DEPENDENCIES / PERFORMANCE / SECURITY / TESTING / FUTURE / RELATED FILES)

**Companion README** structure: brief description, install (via plugin), usage, arguments, examples (basic + advanced), configuration (`.claude/command-name.local.md`), requirements, troubleshooting (Issue → Solution), contributing, license, support.

**Documentation principles**: write for your future self, examples before explanations, progressive disclosure, keep current with code, test the docs (verify examples work).

**Documentation locations**: command file (core usage + inline), README (install/config/troubleshoot), separate docs (deep guides/tutorials), comments (maintainer details).

**Pre-release checklist** (12 items): description clear, argument-hint complete, usage examples, error messages helpful, requirements documented, related commands listed, changelog maintained, version updated, README current, examples actually work, troubleshooting complete.
