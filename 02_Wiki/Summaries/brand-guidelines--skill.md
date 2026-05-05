---
type: summary
source: 01_Raw/github/anthropics/skills/skills/brand-guidelines/SKILL.md
title: "brand-guidelines (Anthropic skill)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill in `anthropics/skills` repo. Applies Anthropic's official brand colors and typography to artifacts that benefit from Anthropic's look-and-feel.

**Frontmatter**: `name: brand-guidelines`, `license: Complete terms in LICENSE.txt`. Description triggers on brand colors / style guidelines / visual formatting / company design standards.

**Brand colors**:
- Main: Dark `#141413`, Light `#faf9f5`, Mid Gray `#b0aea5`, Light Gray `#e8e6dc`
- Accent: Orange `#d97757` (primary), Blue `#6a9bcc` (secondary), Green `#788c5d` (tertiary)

**Typography**: Headings = Poppins (fallback Arial); Body = Lora (fallback Georgia). Pre-install fonts for best results.

**Features**:
- Smart font application: Poppins for headings ≥24pt, Lora for body, auto-fallback if unavailable
- Smart color selection based on background; preserves text hierarchy
- Non-text shapes use accent colors, cycling through orange/blue/green
- Uses RGB color values via python-pptx's RGBColor class for precise brand match

(Remainder of file likely covers integration patterns + technical PPTX-specific guidance.)
