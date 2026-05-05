---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/financial-data-analyst/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/financial-data-analyst/README.md
title: "Claude Quickstarts — financial-data-analyst README"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-TypeScript, Vision, PDF-support]
concepts_referenced: []
---

Sophisticated Next.js application combining Claude with interactive data visualization to analyze financial data via chat.

**Features.**

- **Intelligent data analysis** powered by Claude (uses Claude 3 Haiku and Claude 3.5 Sonnet).
- **Multi-format file upload** — text/code (`.txt`, `.md`, `.html`, `.py`, `.csv`, …), regular PDFs (scanned not supported), images.
- **Interactive data visualization** — Claude can generate Line Charts (time series), Bar Charts (single metric), Multi-Bar (multi-metric), Area (volume over time), Stacked Area (component breakdowns), Pie Charts (distribution).

**Setup.** Node.js 18+ and a Claude API key. Clone, `npm install`, `.env.local` with `ANTHROPIC_API_KEY`, `npm run dev`, open http://localhost:3000.

**Stack.**

- Frontend: Next.js 14, React, TailwindCSS, Shadcn/ui components, Recharts (visualization), PDF.js (PDF processing).
- Backend: Next.js API routes, Edge Runtime, Anthropic SDK.

**Usage examples.** Data extraction & analysis (upload financial documents, extract metrics, analyze trends/patterns). Visualization creation (generate charts based on data, customize visualizations). Continues with deployment notes and customization guidance.
