---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/examples/plugin-commands.md
title: "plugin-dev: command-development plugin-commands examples"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent, Skill]
concepts_referenced: []
---

Examples doc inside `plugin-dev`'s `command-development` skill. 10 plugin command patterns with frontmatter + body.

**Patterns**:
1. **Simple plugin command**: `!`node ${CLAUDE_PLUGIN_ROOT}/scripts/quality-check.js $1`` — uses `${CLAUDE_PLUGIN_ROOT}` for portable path.
2. **Script-based analysis**: multiple sequential plugin script executions (security, perf, best-practices) with comprehensive report.
3. **Template-based generation**: `@${CLAUDE_PLUGIN_ROOT}/templates/api-documentation.md` + `@$1` source file → standardized output.
4. **Multi-script workflow**: orchestrate build/test/deploy with numbered steps.
5. **Configuration-driven deployment**: `@${CLAUDE_PLUGIN_ROOT}/config/$1-deploy.json` env-specific config.
6. **Agent integration**: command launches plugin agent for complex task (delegates via Task/Agent tool).
7. **Skill integration**: command leverages plugin skill ("Use the api-documentation-standards skill to...").
8. **Multi-component workflow**: 5-phase combining scripts + agent + skill + template.
9. **Validated input**: `!`echo "$1" | grep -E "^pattern$" && echo "VALID" || echo "INVALID"`` for arg validation, resource existence checks.
10. **Environment-aware**: conditional behavior per env (full prod checks vs basic dev).

**Common patterns**:
- Plugin script: `!`node ${CLAUDE_PLUGIN_ROOT}/scripts/X.js $1``
- Plugin config: `@${CLAUDE_PLUGIN_ROOT}/config/X.json`
- Plugin template: `@${CLAUDE_PLUGIN_ROOT}/templates/X.md`
- Agent: "Launch the [agent-name] agent for [task]."
- Skill: "Use the [skill-name] skill to ensure [requirements]."
- Input validation: `!`echo "$1" | grep -E "^pattern$" && ... || ...``
- Resource check: `!`test -f ${CLAUDE_PLUGIN_ROOT}/path && ... || ...``

**Common mistakes to avoid**:
- Relative paths (`!`node ./scripts/X.js``) → use `${CLAUDE_PLUGIN_ROOT}`.
- Missing `allowed-tools` for Bash → command fails.
- Not validating inputs → risky.
- Hardcoding plugin paths (`/home/user/.claude/plugins/...`) → breaks across installations.

**Testing tips**: install plugin, test with `claude /command-name args`, verify `${CLAUDE_PLUGIN_ROOT}` expansion via debug echo, test from different cwd.
