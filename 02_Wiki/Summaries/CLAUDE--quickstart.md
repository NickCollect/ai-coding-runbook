---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/CLAUDE.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/CLAUDE.md
title: "Claude Quickstarts — root CLAUDE.md (development guide)"
summarized_at: 2026-05-05
entities_referenced: [Computer-use]
concepts_referenced: []
---

Repository-level Claude Code project guide for the `claude-quickstarts` repo.

**Legal.** When changes are made to files with copyright notices, add an entry to that subdirectory's `CHANGELOG.md`.

**Computer-Use Demo.** Setup with `./setup.sh`. Build Docker image: `docker build . -t computer-use-demo:local`. Run container with `-e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY`, mounting `computer_use_demo/` and `$HOME/.anthropic`, exposing ports 5900/8501/6080/8080. Lint `ruff check .`, format `ruff format .`, typecheck `pyright`, tests `pytest`. Single test: `pytest tests/path_to_test.py::test_name -v`. Style: snake_case functions, PascalCase classes, isort with combine-as-imports, custom `ToolError` for tool errors, type annotations on all parameters/returns, dataclasses + ABCs.

**Customer Support Agent.** `npm install`. `npm run dev` runs the full UI; variants: `dev:left` (left sidebar), `dev:right` (right sidebar), `dev:chat` (chat only). `npm run lint`, `npm run build` (variants in package.json). Style: TypeScript strict mode with proper interfaces, function components with React hooks, ESLint Next.js config, shadcn/ui components.

**Financial Data Analyst.** `npm install`, `npm run dev`, `npm run lint`, `npm run build`. Style: TypeScript strict mode with proper type definitions, function components with type annotations, Recharts for data visualization, React hooks for state management.

The file is intentionally a per-subproject command/style cheat sheet — Claude Code reads it to know the right commands for each subdirectory without exploring.
