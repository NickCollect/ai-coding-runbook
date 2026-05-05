---
type: summary
source: 01_Raw/github/anthropics/skills/skills/algorithmic-art/SKILL.md
title: "algorithmic-art (Anthropic Skills)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill from the public `anthropics/skills` repo. Trigger: requests for "algorithmic art / generative art / flow fields / particle systems" using p5.js. Aimed at avoiding copyright issues from copying existing artists' work — mandates ORIGINAL algorithmic art with seeded randomness.

**Two-step process**:
1. **Algorithmic Philosophy creation** — write a 4–6 paragraph computational manifesto (stored as `.md`). Movement name (1–2 words) + philosophy framed around computational processes, noise, particle behaviors, parametric variation. Examples given: "Organic Turbulence" (Perlin-noise flow fields), "Quantum Harmonics" (sine wave interference), "Recursive Whispers" (L-systems / self-similarity), "Field Dynamics" (vector fields), "Stochastic Crystallization" (Voronoi/relaxation). Critical guideline: REPEATEDLY emphasize craftsmanship ("meticulously crafted algorithm", "master-level implementation") so subsequent Claude invocations preserve that framing.
2. **Conceptual seed deduction** — identify a subtle niche reference from the user's request, embed invisibly in algorithm parameters/behaviors. "Like a jazz musician quoting another song" — only those who know catch it.

**P5.js implementation rules**:
- **STEP 0**: read `templates/viewer.html` FIRST. It's the literal starting point — keep header/sidebar/Anthropic branding (Poppins/Lora fonts, light colors, gradient backdrop), seed controls, action buttons EXACTLY. Replace only the algorithm + parameter controls.
- Always seed: `randomSeed(seed); noiseSeed(seed)`.
- Parameters object includes seed + colors + algorithm-specific tunables (quantities/scales/probabilities/ratios/angles/thresholds).
- Algorithm flows from philosophy, not from a pattern menu.
- Canvas 1200x1200 default.

**Single self-contained HTML artifact** with p5.js from CDN. Required features: parameter sliders, color pickers (optional), seed navigation (Prev/Next/Random/Jump), Regenerate / Reset / Download PNG actions.

**Output**: 1) algorithmic philosophy `.md` file, 2) single interactive HTML artifact built from `templates/viewer.html`.

Resources bundled: `templates/viewer.html` (REQUIRED foundation), `templates/generator_template.js` (p5.js best practices reference, NOT a pattern menu — embed inline in HTML).
