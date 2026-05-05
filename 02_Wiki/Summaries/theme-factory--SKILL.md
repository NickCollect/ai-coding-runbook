---
type: summary
source: 01_Raw/github/anthropics/skills/skills/theme-factory/SKILL.md
title: "theme-factory (Anthropic Skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill providing 10 pre-set themes (color palettes + font pairings) for styling artifacts (slide decks, docs, reports, HTML landing pages). Can also generate custom themes on the fly.

**Usage flow**:
1. Show `theme-showcase.pdf` (visual catalog of all 10) — display, do not modify.
2. Ask user which theme to apply.
3. Wait for explicit confirmation.
4. Apply chosen theme's colors + fonts to the artifact.

**10 themes**: Ocean Depths (corporate maritime), Sunset Boulevard (warm vibrant), Forest Canopy (earth tones), Modern Minimalist (grayscale), Golden Hour (autumnal), Arctic Frost (cool winter), Desert Rose (soft dusty), Tech Innovation (bold modern), Botanical Garden (organic green), Midnight Galaxy (cosmic deep).

Each theme defined in `themes/<name>.md` with: cohesive color palette (hex codes), complementary header + body font pairings, distinct visual identity for context/audience.

**Application**: read theme file → apply colors + fonts consistently → ensure contrast/readability → maintain identity across all slides/sections.

**Custom theme creation**: when none of the 10 fit, generate a new one in the same shape, name it descriptively (after font/color combo), show for review, then apply.
