---
type: summary
source: 01_Raw/github/anthropics/skills/skills/frontend-design/SKILL.md
title: "frontend-design (anthropics/skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill in the Anthropic skills repo (separate copy from the same-named skill in `claude-code/plugins/frontend-design`). Same content, slightly different description (adds "artifacts, posters" to triggers and explicitly lists examples like landing pages, dashboards, React components).

Both versions guide creation of distinctive, production-grade frontend interfaces avoiding generic "AI slop" aesthetics.

**Design thinking**: pick BOLD aesthetic direction (brutally minimal, maximalist chaos, retro-futuristic, organic, luxury, playful, editorial, brutalist, art deco, soft/pastel, industrial). Bold maximalism + refined minimalism both work — key is intentionality, not intensity.

**Aesthetics rules**:
- Typography: avoid Arial/Inter; pair distinctive display + refined body
- Color: cohesive aesthetic via CSS variables; dominant + sharp accents
- Motion: CSS-only for HTML, Motion library for React; high-impact moments (orchestrated page load, staggered reveals); scroll-triggering + surprising hovers
- Spatial composition: asymmetry, overlap, diagonal flow, grid-breaking, generous negative space OR controlled density
- Backgrounds: atmosphere + depth; gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, grain overlays

**Banned**: Inter, Roboto, Arial, system fonts, purple gradients on white, predictable layouts, generic patterns. NEVER converge on common choices (e.g., Space Grotesk) across generations.

Match implementation complexity to aesthetic vision. Maximalist needs elaborate code; minimalist needs restraint + precision in spacing/typography/subtle details.

**See also**: `frontend-design--plugin-skill.md` (the equivalent plugin shipped with claude-code; same contract, slightly different description).
