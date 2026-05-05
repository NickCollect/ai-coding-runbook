---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/references/prompt-snippets.md
title: "claude-opus-4-5-migration: prompt-snippets reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Skill]
concepts_referenced: [Extended-thinking]
---

Reference doc inside the `claude-opus-4-5-migration` plugin's skill. Snippets to add to system prompts ONLY when user explicitly requests them or reports specific issues — by default migration only updates model strings.

**5 snippet sets**:

1. **Tool Overtriggering** — Opus 4.5 may overtrigger tools where prior models needed aggressive language. Replace with normal phrasing:
   - `CRITICAL: You MUST use this tool when...` → `Use this tool when...`
   - `ALWAYS call X before...` → `Call X before...`
   - `You are REQUIRED to...` → `You should...`
   - `NEVER skip this step` → `Don't skip this step`

2. **Over-Engineering Prevention** — Opus 4.5 may create extra files, abstractions, or hypothetical-future flexibility. Snippet (paraphrased): only make changes directly requested or clearly necessary; don't add features/refactor beyond the ask; don't add error handling or backward-compat shims for impossible cases (validate at system boundaries only); don't create helpers/abstractions for one-time operations; reuse existing abstractions, follow DRY.

3. **Code Exploration** — Opus 4.5 may propose fixes without reading code. Snippet: ALWAYS read and understand relevant files before proposing edits; don't speculate about uninspected code; if user references file/path, MUST open and inspect first; thoroughly review style, conventions, abstractions before implementing.

4. **Frontend Design Quality** — default outputs may be "AI slop" generic. XML-tagged snippet `<frontend_aesthetics>` prescribes:
   - Distinctive typography (avoid Arial/Inter/system fonts; tip: avoid Space Grotesk too — model converges on it)
   - Cohesive theme via CSS variables; dominant colors with sharp accents > timid palettes
   - Motion via CSS-only or Motion library (React); prefer one well-orchestrated page-load reveal over scattered micro-interactions
   - Layered backgrounds (gradients, geometric patterns) over solid colors
   - Avoid overused fonts, purple-on-white, predictable layouts

5. **Thinking Sensitivity** — when extended thinking is NOT enabled (no `thinking` API param), Opus 4.5 is sensitive to "think" word. Replace:
   - `think about` → `consider`
   - `think through` → `evaluate`
   - `I think` → `I believe`
   - `think carefully` → `consider carefully`
   - `thinking` → `reasoning`/`considering`

**Usage guidelines**: integrate thoughtfully (weave, don't append); use XML tags matching existing structure; trim if prompt concise, expand if verbose; place coding snippets near coding instructions; preserve existing content; summarize all changes after migration.
