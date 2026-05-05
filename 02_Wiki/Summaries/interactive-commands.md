---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/interactive-commands.md
title: "Interactive Command Patterns"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin]
concepts_referenced: []
---

Reference for slash commands that gather user feedback via the `AskUserQuestion` tool instead of relying on simple arguments.

**When to use AskUserQuestion**: complex multi-choice with explanations, multi-select scenarios, preference gathering, interactive workflows that adapt. **Use args instead** for known simple values, scriptable workflows, fast invocations.

**AskUserQuestion shape**:
```typescript
{
  questions: [{
    question: "...",
    header: "Auth method",   // max 12 chars
    multiSelect: false,
    options: [
      {label: "OAuth 2.0", description: "..."},
      ...   // 2-4 options recommended
    ]
  }]
  // 1-4 questions per call. "Other" automatically provided.
}
```

**Patterns shown** (each as full command markdown):
1. **Basic interactive setup** — gather config in 3 questions, generate `.claude/plugin-name.local.md`.
2. **Multi-stage workflow** — adapt later questions based on earlier answers; final confirmation step.
3. **Yes/No confirmation** — destructive operation gate.
4. **Multi-question config** — language→framework→CI/CD→features (multi-select).
5. **Conditional question flow** — branches based on complexity selection (Simple skips advanced; Complex asks orchestration/mesh/monitoring).
6. **Iterative collection** — ask team size, then loop N times collecting role per member.
7. **Dependency selection** — multi-select feature picker with description per option.

**Question/option design**:
- Specific question text ("Which database should we use for this project?" not "DB?").
- Header ≤12 chars.
- 2–4 options per question; descriptions explain trade-offs in 1–2 sentences.
- multiSelect ONLY for genuinely multi-pickable (features) — never for mutually-exclusive (database engine).

**Advanced**:
- Validation loop: collect → validate → if fail → AskUserQuestion (Fix/Override/Cancel).
- Incremental builder: phases with intermediate review and confirmation.
- Context-aware questions: detect language/frameworks/tools first, then ask relevant questions only.

**Real-world example** (multi-agent-swarm plugin): agent count → task definition approach (File/Guided/Custom) → coordination mode (TeamLeader/Collaborative/Autonomous), then iterative per-agent: name → task type → dependencies (multi-select) → base branch.

**Combining args + questions**: use args for known values (`/cmd $project_name`), use AskUserQuestion for choices needing explanation.

Troubleshooting: questions not appearing → check `allowed-tools: AskUserQuestion`; user can't select → check option clarity; flow confusing → reduce question count, group related, show progress.
