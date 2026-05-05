---
type: summary
source: 01_Raw/github/anthropics/skills/skills/canvas-design/SKILL.md
title: "Skill: canvas-design"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill from `anthropics/skills` repo. Triggers when the user asks to create a poster, design, or piece of static visual art. Outputs only `.md`, `.pdf`, `.png` files. License: Complete terms in `LICENSE.txt`.

**Two-step workflow**:

**Step 1: Design philosophy creation (.md)**: write a 4-6 paragraph **VISUAL PHILOSOPHY** (not layouts or templates) — an aesthetic worldview that another Claude instance will then interpret visually. Format: name the movement (1-2 words like "Brutalist Joy" / "Chromatic Silence"), articulate philosophy across space/form, color/material, scale/rhythm, composition/balance, visual hierarchy.

Critical guidelines:
- Avoid redundancy (each design aspect mentioned once)
- Emphasize craftsmanship REPEATEDLY ("meticulously crafted", "deep expertise", "painstaking attention", "master-level execution")
- Leave creative space for next interpreter
- Philosophy must guide the next Claude to express VISUALLY, not through text — "Information lives in design, not paragraphs"

Five worked examples in raw: Concrete Poetry, Chromatic Language, Analog Meditation, Organic Systems, Geometric Silence.

**Sub-step "Deduce subtle reference"**: identify a niche, sophisticated conceptual thread from the original request — embed as the soul of the work. "Like a jazz musician quoting another song — only those who know catch it, but everyone appreciates the music."

**Step 2: Canvas creation (.pdf or .png)**: create a single-page design-forward output (unless asked for more). Use repeating patterns, perfect shapes, dense accumulation of marks, layered patterns, sparse clinical typography, systematic reference markers. Treat the topic with reverence reserved for documenting observable phenomena.

Text rules: minimal, visual-first, never overlap, never falls off page, proper margins. Use `./canvas-fonts` directory for fonts. Make typography part of the art if abstract.

**Final refinement step**: assume user has already said "It isn't perfect enough — must be a museum-quality masterpiece." DON'T add more graphics; refine what's there. Ask "How can I make what's already here more of a piece of art?" Take a second pass focused on cohesion.

**Multi-page mode**: bundle additional pages along the same philosophy but with distinct twists — coffee-table-book pacing.

Skill is unusual in that **it instructs Claude to instruct itself** — Step 1's output becomes Step 2's input, with the design philosophy serving as a prompt for the canvas-execution step.
