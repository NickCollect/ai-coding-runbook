---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/references/real-world-examples.md
title: "Real-World Plugin Settings Examples"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks, Subagent, Settings, Agent-team]
concepts_referenced: [Agent-team]
---

Reference doc for the `plugin-settings` skill. Detailed analysis of how production plugins use the `.claude/plugin-name.local.md` pattern. Note: only first ~120 lines sampled — covers the multi-agent-swarm example.

**multi-agent-swarm Plugin example**:

**Settings file** `.claude/multi-agent-swarm.local.md`:
```yaml
agent_name: auth-implementation
task_number: 3.5
pr_number: 1234
coordinator_session: team-leader
enabled: true
dependencies: ["Task 3.4"]
additional_instructions: "Use JWT tokens, not sessions"
```
Body contains task description, requirements, success criteria, coordination notes.

**Hook usage** (`hooks/agent-stop-notification.sh`): sends notification to coordinator tmux session when agent goes idle. Pattern:
1. Quick exit if state file missing (`[[ ! -f "$SWARM_STATE_FILE" ]] && exit 0`)
2. Parse frontmatter via `sed`
3. Extract fields per-line via `grep | sed`
4. Respect `enabled: true` flag
5. `tmux has-session -t "$COORDINATOR_SESSION"` → `tmux send-keys` notification

**Creation via slash command** (`commands/launch-swarm.md`): heredoc to write settings file at swarm-launch time, populating fields like `agent_name`, `task_number`, `coordinator_session`, `dependencies`, `additional_instructions` from command arguments.

**Updates**: PR number updated after PR creation (logic continues in raw — not sampled).

(Remainder of raw likely covers more plugins: hookify, similar production examples.)
