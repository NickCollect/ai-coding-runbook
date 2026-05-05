---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-typescript/CONTRIBUTING.md
source_url: https://github.com/anthropics/anthropic-sdk-typescript/blob/main/CONTRIBUTING.md
title: "Anthropic SDK TypeScript — CONTRIBUTING"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-TypeScript]
concepts_referenced: []
---

Contributor guide for `anthropic-sdk-typescript`.

**Documentation.** Lives at platform.claude.com/docs/en/api/sdks/typescript — open an issue to suggest changes.

**Environment setup.** The repo uses `yarn@v1` (other package managers may work but are not officially supported). Run `yarn` then `yarn build` to install deps and produce `dist/`.

**Generated code.** Most of the SDK is generated. Modifications persist between generations but may merge-conflict on re-generation. The generator never modifies `src/lib/` or `examples/` — those are safe for hand-edits.

**Examples.** Files in `examples/` can be freely edited. Make example scripts executable (`chmod +x`) and run with `yarn tsn -T examples/<your-example>.ts`. Example shebang: `#!/usr/bin/env -S npm run tsn -T`.

**Using from source.** Either install via git (`npm install git+ssh://git@github.com:anthropics/anthropic-sdk-typescript.git`) or link a local clone with `yarn link` / `pnpm link --global`.

**Tests.** Most tests need a mock OpenAPI server — start with `./scripts/mock`, run with `yarn run test`.

**Lint and format.** Uses `prettier` and `eslint`. Lint with `yarn lint`. Auto-fix and format with `yarn fix`.

**Publishing.** The automated release-PR pipeline publishes to npm. Manual options: the `Publish NPM` GitHub action, or running `bin/publish-npm` with `NPM_TOKEN` set.
