---
type: summary
source: 01_Raw/github/anthropics/claude-code/.github/ISSUE_TEMPLATE/model_behavior.yml
title: "Model Behavior Issue (GitHub issue template)"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Subagent]
concepts_referenced: []
---

GitHub issue form (`model_behavior.yml`) for reporting unexpected Claude model behavior, incorrect actions, or permission violations. Title prefix `[MODEL]`, label `model`. **Distinct from Bug Report** — for unexpected actions / out-of-scope file mods / ignored instructions / unwanted assumptions, NOT for crashes / API errors / install issues.

**Preflight**: searched existing model-tagged issues, no sensitive info (API keys, passwords).

**Behavior type categories** (dropdown):
- Modified files I didn't ask it to modify
- Accessed files outside the working directory
- Ignored my instructions or configuration
- Reverted/undid previous changes without asking
- Made incorrect assumptions about my project
- Refused a reasonable request
- Behavior changed between sessions
- Subagent behaved unexpectedly
- Other

**Required fields**: what you asked Claude to do, what Claude actually did (step-by-step), expected behavior, permission mode (Accept Edits ON/OFF/unknown), reproducibility (consistent / sometimes / once / not tried), Claude model (Sonnet / Opus / Haiku / Not sure / Other), Claude Code Version, Platform (Anthropic API / Bedrock / Vertex / Other), Impact (Critical = data loss / High / Medium / Low).

**Optional fields**: files affected (shell-rendered), repro steps, relevant conversation log (markdown-rendered), additional context (patterns, file types, project structures triggering behavior).
