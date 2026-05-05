---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/learning-output-style/.claude-plugin/plugin.json
title: "learning-output-style plugin manifest"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Output-style]
concepts_referenced: []
---

Plugin manifest for `learning-output-style`:
- `name`: `learning-output-style`
- `version`: `1.0.0`
- `description`: "Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style)"
- `author`: Boris Cherny (boris@anthropic.com)

Implementation: SessionStart hook injecting context that prompts user to write meaningful 5-10 line code contributions at decision points while receiving educational insights. Mimics an output-style feature that wasn't shipped.
