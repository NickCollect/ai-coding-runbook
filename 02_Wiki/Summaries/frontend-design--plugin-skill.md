---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/frontend-design/skills/frontend-design/SKILL.md
title: "frontend-design (plugin skill)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill (`SKILL.md`) shipped in the `frontend-design` plugin. Guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics.

**Frontmatter**:
- `name: frontend-design`
- `description`: invoked when user asks to build web components/pages/apps
- `license`: complete terms in LICENSE.txt

**Design thinking** (before coding):
- Purpose: what problem? Who uses it?
- Tone — pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian
- Constraints: framework, performance, accessibility
- Differentiation: what's UNFORGETTABLE?

**CRITICAL principle**: bold maximalism and refined minimalism both work — key is intentionality, not intensity.

**Implementation**: production-grade + functional, visually striking + memorable, cohesive aesthetic POV, meticulously refined.

**Aesthetics guidelines**:
- **Typography**: avoid generic (Arial/Inter), pick distinctive characterful fonts; pair distinctive display + refined body
- **Color & Theme**: cohesive aesthetic via CSS variables; dominant colors with sharp accents over timid even palettes
- **Motion**: CSS-only for HTML, Motion library for React. Focus on high-impact moments — one orchestrated page load with staggered reveals beats scattered micro-interactions. Use scroll-triggering and surprising hover states.
- **Spatial composition**: unexpected layouts, asymmetry, overlap, diagonal flow, grid-breaking, generous negative space OR controlled density
- **Backgrounds & visual details**: atmosphere + depth (not solid colors). Gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, grain overlays.

**NEVER use generic AI aesthetics**: overused fonts (Inter, Roboto, Arial, system), cliched schemes (purple gradient on white), predictable layouts/components. Vary between light/dark themes and aesthetics across generations. NEVER converge on common choices like Space Grotesk.

Match implementation complexity to aesthetic vision: maximalist needs elaborate code + extensive animation; minimalist needs restraint + precision in spacing/typography/subtle details. Elegance = executing the vision well.
