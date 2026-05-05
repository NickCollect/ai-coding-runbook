---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/plugin-features-reference.md
title: "Plugin-specific command features reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent, Skill, Hooks]
concepts_referenced: []
---

Reference doc inside `plugin-dev/skills/command-development/` covering plugin-bundled command behaviors.

**Plugin command discovery**: commands in `<plugin>/commands/` are auto-discovered at plugin load time. No registration. Appear as `(plugin:plugin-name)` in `/help`. Subdirectories create namespaces (`commands/review/security.md` → `/security (plugin:plugin-name:review)`). Use namespacing when plugin has 5+ commands.

**Naming conventions**: descriptive + action-oriented, hyphens for multi-word, consider plugin-name prefix to avoid conflicts. Avoid generic names (`/test`, `/run`, `/do-stuff`).

**`${CLAUDE_PLUGIN_ROOT}`** — env var resolving to plugin's absolute path; portable across installations. Common patterns:
- Execute plugin scripts: `!\`node ${CLAUDE_PLUGIN_ROOT}/scripts/x.js $1\``
- Load config: `@${CLAUDE_PLUGIN_ROOT}/config/deploy.json`
- Templates: `@${CLAUDE_PLUGIN_ROOT}/templates/report.md`
- Multi-step: combine bash + `@`-references in sequence

Best practices: always use for plugin-internal paths (NOT `@./templates/foo.md` which resolves relative to cwd), validate file existence with `!\`test -f ${CLAUDE_PLUGIN_ROOT}/config.json && echo "exists" || echo "missing"\``, document plugin file structure in HTML comments, combine with positional args `${CLAUDE_PLUGIN_ROOT}/bin/process.sh $1 $2`.

**Five plugin command patterns**:
1. **Configuration-based**: load `@${CLAUDE_PLUGIN_ROOT}/deploy-config.json` and apply consistent settings
2. **Template-based generation**: read `@${CLAUDE_PLUGIN_ROOT}/templates/component-docs.md` and generate output in same shape
3. **Multi-script workflow**: chain `!\`bash ${CLAUDE_PLUGIN_ROOT}/scripts/{build,validate,test}.sh\`` and report aggregated status
4. **Environment-aware**: load `@${CLAUDE_PLUGIN_ROOT}/config/$1.json` to switch behavior per env
5. **Plugin data management**: write to `${CLAUDE_PLUGIN_ROOT}/cache/` for persistent plugin state

**Integration with other plugin components**:
- **Agents**: command mentions agent name → Claude uses Task tool to launch the plugin's agent (must exist in `agents/`)
- **Skills**: command mentions skill by name to hint invocation (must exist in `skills/`)
- **Hooks**: hooks fire automatically on events; commands can prepare state, document expected hook output
- **Multi-component**: combine static analysis script → agent for deep review → skill for standards → template for report

**Validation patterns**: input validation (grep regex), file existence checks (`test -f`), required arg checks (`test -n "$1" -a -n "$2"`), plugin resource validation (`test -x ${CLAUDE_PLUGIN_ROOT}/bin/x`), output validation (exit code + dir contents), graceful error handling (`2>&1 || echo "ERROR: $?"` then explain causes + troubleshooting + alternatives).

**Best practices summary**: use `${CLAUDE_PLUGIN_ROOT}` for all internal paths, validate inputs early, document plugin structure, integrate with agents/skills/hooks, helpful error messages, handle edge cases (missing files, invalid args, failed scripts, missing deps), one purpose per command, test across installations.
