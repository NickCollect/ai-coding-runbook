---
type: summary
source: 01_Raw/github/anthropics/skills/skills/web-artifacts-builder/SKILL.md
title: "anthropics/skills: web-artifacts-builder SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill for creating elaborate multi-component claude.ai HTML artifacts using modern frontend stack. Use for complex artifacts requiring state mgmt, routing, or shadcn/ui — NOT for simple single-file HTML/JSX artifacts.

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui.

**Anti-AI-slop guidance** (VERY IMPORTANT): avoid excessive centered layouts, purple gradients, uniform rounded corners, Inter font.

**Workflow**:

1. **Initialize**: `bash scripts/init-artifact.sh <project-name>` — creates fully configured project with React+TS via Vite, Tailwind 3.4.1 + shadcn/ui theming, `@/` path aliases, 40+ pre-installed shadcn/ui components, all Radix UI deps, Parcel via `.parcelrc`, Node 18+ compat (auto-detects + pins Vite version).

2. **Develop**: edit generated files — see "Common Development Tasks" in skill.

3. **Bundle**: `bash scripts/bundle-artifact.sh` → produces `bundle.html` self-contained artifact (all JS/CSS/deps inlined). Requires `index.html` in root. Script installs parcel + @parcel/config-default + parcel-resolver-tspaths + html-inline, creates `.parcelrc` with path alias support, builds without source maps, inlines via html-inline.

4. **Share**: post bundled `bundle.html` in conversation as artifact.

5. **Test (optional)**: avoid upfront testing (adds latency). Use Playwright/Puppeteer/other tools later if requested or issues arise.

**Reference**: shadcn/ui components docs at https://ui.shadcn.com/docs/components.
