# Changelog

## 0.93.0 (2026-05-04)

Full Changelog: [sdk-v0.92.0...sdk-v0.93.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.92.0...sdk-v0.93.0)

### Features

* **client:** add Workload Identity Federation, interactive OAuth, and auth profiles ([d5d6abd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d5d6abd))

## 0.92.0 (2026-04-30)

Full Changelog: [sdk-v0.91.1...sdk-v0.92.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.91.1...sdk-v0.92.0)

### Features

* **api:** improve Managed Agents APIs ([ca1bf4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ca1bf4a))
* support setting headers via env ([32f67d4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/32f67d4))

### Bug Fixes

* **bedrock:** throw APIError for error events delivered in chunk frames ([#1021](https://github.com/anthropics/anthropic-sdk-typescript/issues/1021)) ([3ae887b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3ae887b))

### Chores

* **format:** run eslint and prettier separately ([7ce257c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7ce257c))
* **internal:** codegen related update ([f08cc77](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f08cc77))

## 0.91.1 (2026-04-24)

Full Changelog: [sdk-v0.91.0...sdk-v0.91.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.91.0...sdk-v0.91.1)

### Bug Fixes

* **memory:** use restrictive file mode for memory files ([#901](https://github.com/anthropics/anthropic-sdk-typescript/issues/901)) ([6db3b7e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6db3b7e))

### Chores

* **formatter:** run prettier and eslint separately ([974d22f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/974d22f))

## 0.91.0 (2026-04-23)

Full Changelog: [sdk-v0.90.0...sdk-v0.91.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.90.0...sdk-v0.91.0)

### Features

* **api:** CMA Memory public beta ([ddf732f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ddf732f))
* **bedrock:** use auth header for mantle client ([#866](https://github.com/anthropics/anthropic-sdk-typescript/issues/866)) ([aec801a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/aec801a))

### Bug Fixes

* **api:** fix errors in api spec ([ae10768](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ae10768))
* **api:** restore missing features ([1a5b47b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1a5b47b))

### Chores

* **internal:** more robust bootstrap script ([7716e19](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7716e19))
* **tests:** bump steady to v0.22.1 ([219a971](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/219a971))

## 0.90.0 (2026-04-16)

Full Changelog: [sdk-v0.89.0...sdk-v0.90.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.89.0...sdk-v0.90.0)

### Features

* **api:** add claude-opus-4-7, token budgets and user_profiles ([b26134b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b26134b))

### Chores

* actually delete release-doctor.yml ([0fe984d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0fe984d))
* **ci:** remove release-doctor workflow ([08e58bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/08e58bd))

## 0.89.0 (2026-04-14)

Full Changelog: [sdk-v0.88.0...sdk-v0.89.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.88.0...sdk-v0.89.0)

### Features

* **api:** manual updates ([57c2a11](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/57c2a11))
* **api:** mark Sonnet and Opus 4 as deprecated ([eff41b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/eff41b7))

### Bug Fixes

* **streaming:** add missing events ([4c52919](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c52919))

## 0.88.0 (2026-04-10)

Full Changelog: [sdk-v0.87.0...sdk-v0.88.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.87.0...sdk-v0.88.0)

### Features

* vertex eu region ([#882](https://github.com/anthropics/anthropic-sdk-typescript/issues/882)) ([1933857](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1933857))

### Documentation

* improve examples ([de4f483](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/de4f483))
* update examples ([454e1c5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/454e1c5))

## 0.87.0 (2026-04-09)

Full Changelog: [sdk-v0.86.1...sdk-v0.87.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.86.1...sdk-v0.87.0)

### Features

* **api:** Add beta advisor tool ([1e99a8d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1e99a8d))

## 0.86.1 (2026-04-08)

Full Changelog: [sdk-v0.86.0...sdk-v0.86.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.86.0...sdk-v0.86.1)

### Chores

* update @anthropic-ai/sdk dependency version ([#870](https://github.com/anthropics/anthropic-sdk-typescript/issues/870)) ([036342b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/036342b))

## 0.86.0 (2026-04-08)

Full Changelog: [sdk-v0.85.0...sdk-v0.86.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.85.0...sdk-v0.86.0)

### Features

* **api:** add support for Claude Managed Agents ([2ef732a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2ef732a))

### Chores

* **internal:** codegen related update ([d644830](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d644830))

## 0.85.0 (2026-04-07)

Full Changelog: [sdk-v0.84.0...sdk-v0.85.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.84.0...sdk-v0.85.0)

### Features

* **client:** Create Bedrock Mantle client ([#810](https://github.com/anthropics/anthropic-sdk-typescript/issues/810)) ([2f1f4a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2f1f4a1))

## 0.84.0 (2026-04-07)

Full Changelog: [sdk-v0.83.0...sdk-v0.84.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.83.0...sdk-v0.84.0)

### Features

* **api:** Add support for claude-mythos-preview ([d4057b0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d4057b0))
* **tools:** add AbortSignal support for tool runner ([#848](https://github.com/anthropics/anthropic-sdk-typescript/issues/848)) ([972d591](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/972d591))

## 0.83.0 (2026-04-03)

Full Changelog: [sdk-v0.82.0...sdk-v0.83.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.82.0...sdk-v0.83.0)

### Features

* **vertex:** add support for US multi-region endpoint ([5e5aea7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5e5aea7))
* **vertex:** add support for US multi-region endpoint ([0de0e98](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0de0e98))

### Bug Fixes

* **client:** dont upload aws artifact ([#844](https://github.com/anthropics/anthropic-sdk-typescript/issues/844)) ([d1a31fc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d1a31fc))

### Chores

* **client:** deprecate client-side compaction helpers ([1926e87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1926e87))
* **client:** internal updates ([3d64763](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3d64763))

## 0.82.0 (2026-04-01)

Full Changelog: [sdk-v0.81.0...sdk-v0.82.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.81.0...sdk-v0.82.0)

### Features

* **api:** add structured stop_details to message responses ([031328a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/031328a))
* prepare aws package ([#782](https://github.com/anthropics/anthropic-sdk-typescript/issues/782)) ([f351d4d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f351d4d))
* support API keys in Bedrock SDK ([#824](https://github.com/anthropics/anthropic-sdk-typescript/issues/824)) ([be6c608](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/be6c608))

### Chores

* **tests:** bump steady to v0.20.2 ([6cf12cc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6cf12cc))

## 0.81.0 (2026-03-31)

Full Changelog: [sdk-v0.80.0...sdk-v0.81.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.80.0...sdk-v0.81.0)

### Features

* add .type field to APIError for error kind identification ([#790](https://github.com/anthropics/anthropic-sdk-typescript/issues/790)) ([4bf637d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4bf637d))

### Bug Fixes

* **memory:** append path separator in validatePath prefix check ([0ac69b3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0ac69b3))

### Chores

* **ci:** run builds on CI even if only spec metadata changed ([70b657a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/70b657a))
* **ci:** skip lint on metadata-only changes ([69bdc94](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/69bdc94))
* **internal:** codegen related update ([7ff7390](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7ff7390))
* **internal:** update gitignore ([46d6667](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/46d6667))
* **internal:** update multipart form array serialization ([d55b07d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d55b07d))
* **tests:** bump steady to v0.19.4 ([4957a5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4957a5e))
* **tests:** bump steady to v0.19.5 ([c511ae0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c511ae0))
* **tests:** bump steady to v0.19.6 ([6d2b4b9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6d2b4b9))
* **tests:** bump steady to v0.19.7 ([d6cff9d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d6cff9d))
* **tests:** bump steady to v0.20.1 ([284561f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/284561f))

## 0.80.0 (2026-03-18)

Full Changelog: [sdk-v0.79.0...sdk-v0.80.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.79.0...sdk-v0.80.0)

### Features

* **api:** manual updates ([dd12f1a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dd12f1a))
* **api:** manual updates ([9c0a077](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9c0a077))

### Chores

* **internal:** tweak CI branches ([4a5819e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4a5819e))

## 0.79.0 (2026-03-16)

Full Changelog: [sdk-v0.78.0...sdk-v0.79.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.78.0...sdk-v0.79.0)

### Features

* add support for filesystem memory tools ([#599](https://github.com/anthropics/anthropic-sdk-typescript/issues/599)) ([1064199](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1064199))
* **api:** chore(config): clean up model enum list ([#31](https://github.com/anthropics/anthropic-sdk-typescript/issues/31)) ([07727a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/07727a6))
* **api:** GA thinking-display-setting ([4dc8df4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4dc8df4))
* **tests:** update mock server ([e5c3be9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e5c3be9))

### Bug Fixes

* **docs/contributing:** correct pnpm link command ([16bf66c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/16bf66c))
* **internal:** skip tests that depend on mock server ([07417e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/07417e5))
* **zod:** use v4 import path for Zod ^3.25 compatibility ([#925](https://github.com/anthropics/anthropic-sdk-typescript/issues/925)) ([c6c0ac8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c6c0ac8))

### Chores

* **client:** remove unused import ([3827ab5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3827ab5))
* **internal:** codegen related update ([2c1fc10](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c1fc10))
* **internal:** improve import alias names ([5b9615b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5b9615b))
* **internal:** move stringifyQuery implementation to internal function ([16239f3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/16239f3))
* **internal:** update dependencies to address dependabot vulnerabilities ([6fdea5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6fdea5e))
* **mcp-server:** improve instructions ([66e5363](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/66e5363))
* remove accidentally committed file ([#929](https://github.com/anthropics/anthropic-sdk-typescript/issues/929)) ([0989113](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0989113))
* **tests:** unskip tests that are now supported in steady ([616a98a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/616a98a))

### Documentation

* streamline and standardize docs ([#687](https://github.com/anthropics/anthropic-sdk-typescript/issues/687)) ([dbdc5d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dbdc5d3))

## 0.78.0 (2026-02-19)

Full Changelog: [sdk-v0.77.0...sdk-v0.78.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.77.0...sdk-v0.78.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([1e2f83d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1e2f83d))

### Bug Fixes

* **bedrock:** eliminate race condition in AWS credential resolution ([#901](https://github.com/anthropics/anthropic-sdk-typescript/issues/901)) ([e5a101d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e5a101d))
* **client:** format batches test file ([821e9bf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/821e9bf))
* **tests:** fix issue in batches test ([5f4ccf8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5f4ccf8))

### Chores

* update mock server docs ([25d337f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/25d337f))

## 0.77.0 (2026-02-18)

Full Changelog: [sdk-v0.76.0...sdk-v0.77.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.76.0...sdk-v0.77.0)

### Features

* **api:** fix shared UserLocation and error code types ([c84038f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c84038f))

### Bug Fixes

* add backward-compat namespace re-exports for UserLocation ([#706](https://github.com/anthropics/anthropic-sdk-typescript/issues/706)) ([b88834f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b88834f))

## 0.76.0 (2026-02-18)

Full Changelog: [sdk-v0.75.0...sdk-v0.76.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.75.0...sdk-v0.76.0)

### Features

* **api:** manual updates ([25fe41c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/25fe41c))

## 0.75.0 (2026-02-17)

Full Changelog: [sdk-v0.74.0...sdk-v0.75.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.74.0...sdk-v0.75.0)

### Features

* **api:** Releasing claude-sonnet-4-6 ([d75e1c0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d75e1c0))

### Bug Fixes

* **api:** fix spec errors ([aa99e46](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/aa99e46))
* **tests:** fix erroneous speed tests  ([#699](https://github.com/anthropics/anthropic-sdk-typescript/issues/699)) ([fcac1ca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fcac1ca))

### Chores

* **internal/client:** fix form-urlencoded requests ([cba82b4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cba82b4))
* **internal:** avoid type checking errors with ts-reset ([c723296](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c723296))
* **readme:** change badge color to blue ([3f7e788](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3f7e788))

## 0.74.0 (2026-02-07)

Full Changelog: [sdk-v0.73.0...sdk-v0.74.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.73.0...sdk-v0.74.0)

### Features

* **api:** enabling fast-mode in claude-opus-4-6 ([e337981](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e337981))

## 0.73.0 (2026-02-05)

Full Changelog: [sdk-v0.72.1...sdk-v0.73.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.72.1...sdk-v0.73.0)

### Features

* **api:** Release Claude Opus 4.6, adaptive thinking, and other features ([f741f92](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f741f92))

### Bug Fixes

* **client:** avoid memory leak in abort signal listener ([#895](https://github.com/anthropics/anthropic-sdk-typescript/issues/895)) ([3bdd153](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3bdd153))
* **client:** avoid memory leak with abort signals ([53e47df](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/53e47df))
* **client:** avoid removing abort listener too early ([cd6e832](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cd6e832))

### Chores

* **client:** do not parse responses with empty content-length ([2be2df9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2be2df9))
* **client:** restructure abort controller binding ([0eeacb6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0eeacb6))
* **internal:** fix pagination internals not accepting option promises ([7c23a3f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7c23a3f))
* remove claude-code-review workflow ([#644](https://github.com/anthropics/anthropic-sdk-typescript/issues/644)) ([ad09c76](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ad09c76))

## 0.72.1 (2026-01-30)

Full Changelog: [sdk-v0.72.0...sdk-v0.72.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.72.0...sdk-v0.72.1)

### Bug Fixes

* **client:** remove OutputFormat exports from index.ts ([bf2cf08](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bf2cf08))

## 0.72.0 (2026-01-29)

Full Changelog: [sdk-v0.71.2...sdk-v0.72.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.71.2...sdk-v0.72.0)

### Features

* **api:** add support for Structured Outputs in the Messages API ([eeb7fab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/eeb7fab))
* **api:** migrate sending message format in output_config rather than output_format ([99f4066](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/99f4066))
* **ci:** add breaking change detection workflow ([b181568](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b181568))
* **client:** migrate structured output format ([#625](https://github.com/anthropics/anthropic-sdk-typescript/issues/625)) ([abcdddc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/abcdddc))
* **helpers:** add MCP SDK helper functions ([#610](https://github.com/anthropics/anthropic-sdk-typescript/issues/610)) ([b6c3963](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b6c3963))

### Bug Fixes

* **mcp:** correct code tool API endpoint ([4bd6ad6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4bd6ad6))
* **mcp:** return correct lines on typescript errors ([c425959](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c425959))

### Chores

* break long lines in snippets into multiline ([2c44e2d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c44e2d))
* **ci:** Add Claude Code GitHub Workflow ([#612](https://github.com/anthropics/anthropic-sdk-typescript/issues/612)) ([28a9a00](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/28a9a00))
* **ci:** fix multi package publishing ([b9e3ab9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b9e3ab9))
* **ci:** upgrade `actions/github-script` ([ff9dd44](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ff9dd44))
* **internal:** codegen related update ([754de58](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/754de58))
* **internal:** codegen related update ([cb411e4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cb411e4))
* **internal:** update `actions/checkout` version ([c0057be](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c0057be))
* **internal:** upgrade babel, qs, js-yaml ([494d9ed](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/494d9ed))
* **internal:** version bump ([24ecc83](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/24ecc83))
* **tests:** remove extraneous header test ([076a87c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/076a87c))

### Documentation

* tool use documentation link ([#873](https://github.com/anthropics/anthropic-sdk-typescript/issues/873)) ([664cdd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/664cdd6))
* update import paths for beta helpers ([#834](https://github.com/anthropics/anthropic-sdk-typescript/issues/834)) ([d08fd40](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d08fd40))
* update README with Claude branding ([#611](https://github.com/anthropics/anthropic-sdk-typescript/issues/611)) ([2a9a5f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2a9a5f7))

## 0.71.2 (2025-12-05)

Full Changelog: [sdk-v0.71.1...sdk-v0.71.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.71.1...sdk-v0.71.2)

### Bug Fixes

* **streams:** ensure errors are catchable ([#856](https://github.com/anthropics/anthropic-sdk-typescript/issues/856)) ([a480eaf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a480eaf))

## 0.71.1 (2025-12-04)

Full Changelog: [sdk-v0.71.0...sdk-v0.71.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.71.0...sdk-v0.71.1)

### Bug Fixes

* **parser:** use correct naming for parsed text blocks ([6472bcd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6472bcd))
* **structured outputs:** ensure parsed is not enumerable ([860175f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/860175f)), closes [#857](https://github.com/anthropics/anthropic-sdk-typescript/issues/857)

### Chores

* add deprecation warnings for accessing .parsed ([ae7a637](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ae7a637))
* **client:** fix logger property type ([e3e4d7c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e3e4d7c))
* **internal:** upgrade eslint ([5fbe661](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5fbe661))

## 0.71.0 (2025-11-24)

Full Changelog: [sdk-v0.70.1...sdk-v0.71.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.70.1...sdk-v0.71.0)

### Features

* **api:** adds support for Claude Opus 4.5, Effort, Advance Tool Use Features, Autocompaction, and Computer Use v5 ([f3a0dac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f3a0dac))

### Chores

* fix ci errors ([8d96290](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8d96290))
* include publishConfig in all package.json files ([4c72960](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c72960))
* **readme:** fix example import ([4e8983a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4e8983a))

## 0.70.1 (2025-11-20)

Full Changelog: [sdk-v0.70.0...sdk-v0.70.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.70.0...sdk-v0.70.1)

### Bug Fixes

* **structured outputs:** use correct beta header ([626662c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/626662c))

## 0.70.0 (2025-11-18)

Full Changelog: [sdk-v0.69.0...sdk-v0.70.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.69.0...sdk-v0.70.0)

### Features

* add Foundry SDK ([40b0e87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/40b0e87))

## 0.69.0 (2025-11-14)

Full Changelog: [sdk-v0.68.0...sdk-v0.69.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.68.0...sdk-v0.69.0)

### Features

* **api:** add support for structured outputs beta ([e6562d7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e6562d7))

## 0.68.0 (2025-10-28)

Full Changelog: [sdk-v0.67.1...sdk-v0.68.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.67.1...sdk-v0.68.0)

### Features

* **api:** add ability to clear thinking in context management ([d8707d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d8707d3))

## 0.67.1 (2025-10-28)

Full Changelog: [sdk-v0.67.0...sdk-v0.67.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.67.0...sdk-v0.67.1)

### Chores

* **api:** mark older sonnet models as deprecated ([64ad72d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/64ad72d))

## 0.67.0 (2025-10-16)

Full Changelog: [sdk-v0.66.0...sdk-v0.67.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.66.0...sdk-v0.67.0)

### Features

* **api:** adding support for agent skills ([0b7d97f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0b7d97f))

## 0.66.0 (2025-10-15)

Full Changelog: [sdk-v0.65.0...sdk-v0.66.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.65.0...sdk-v0.66.0)

### Features

* **api:** manual updates ([7605d04](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7605d04))

### Bug Fixes

* **tool-runner:** fix unhandled promise error for streams ([4f6bc94](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4f6bc94))

### Chores

* **client:** add context-management-2025-06-27 beta header ([c6efc98](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c6efc98))
* **client:** add model-context-window-exceeded-2025-08-26 beta header ([06d2513](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/06d2513))
* **internal:** use npm pack for build uploads ([55c0ad7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/55c0ad7))
* **jsdoc:** fix [@link](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/@link) annotations to refer only to parts of the package‘s public interface ([62c1b5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/62c1b5e))

## 0.65.0 (2025-09-29)

Full Changelog: [sdk-v0.64.0...sdk-v0.65.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.64.0...sdk-v0.65.0)

### Features

* **api:** adds support for Claude Sonnet 4.5 and context management features ([3f0b0fb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3f0b0fb))

### Chores

* **internal:** codegen related update ([724a2b1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/724a2b1))
* **internal:** ignore .eslintcache ([56a5f30](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/56a5f30))

## 0.64.0 (2025-09-26)

Full Changelog: [sdk-v0.63.1...sdk-v0.64.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.63.1...sdk-v0.64.0)

### Features

* **toolRunner:** support custom headers ([ac6a7a3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ac6a7a3))

### Performance Improvements

* faster formatting ([32d6185](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/32d6185))

### Chores

* **internal:** fix incremental formatting in some cases ([2bdf8ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2bdf8ee))
* **internal:** remove deprecated `compilerOptions.baseUrl` from tsconfig.json ([2817c45](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2817c45))

## 0.63.1 (2025-09-23)

Full Changelog: [sdk-v0.63.0...sdk-v0.63.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.63.0...sdk-v0.63.1)

### Bug Fixes

* **helpers/zod:** fix compat with zod 3 ([a2952e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a2952e1))

### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([115d81a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/115d81a))
* **internal:** update CI ([dfa991a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dfa991a))
* **package:** lower zod peer dependency constraints ([b40cfec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b40cfec))

## 0.63.0 (2025-09-17)

Full Changelog: [sdk-v0.62.0...sdk-v0.63.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.62.0...sdk-v0.63.0)

### Features

* **client:** add support for toolRunner helpers ([28f5837](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/28f5837))

### Chores

* **internal:** fix tests ([003617d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/003617d))
* **vertex:** update model string to valid example ([7b77da0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7b77da0))

## 0.62.0 (2025-09-10)

Full Changelog: [sdk-v0.61.0...sdk-v0.62.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.61.0...sdk-v0.62.0)

### Features

* **api:** adds support for Documents in tool results ([5d971f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5d971f9))
* **api:** adds support for web_fetch_20250910 tool ([c663898](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c663898))

## 0.61.0 (2025-09-02)

Full Changelog: [sdk-v0.60.0...sdk-v0.61.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.60.0...sdk-v0.61.0)

### Features

* **client:** adds support for code-execution-2025-08-26 tool ([91dd1bb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/91dd1bb))
* **mcp:** add code execution tool ([2f9cfba](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2f9cfba))

### Chores

* add package to package.json ([3ee3632](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3ee3632))
* **client:** qualify global Blob ([e6bfd68](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e6bfd68))
* **deps:** update dependency @types/node to v20.17.58 ([e3577f1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e3577f1))
* **internal:** formatting change ([c8f4029](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c8f4029))
* **internal:** update global Error reference ([c82be0d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c82be0d))
* update CI script ([92f4e99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/92f4e99))

### Documentation

* fix default timeout comment ([#812](https://github.com/anthropics/anthropic-sdk-typescript/issues/812)) ([a59964d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a59964d))

## 0.60.0 (2025-08-13)

Full Changelog: [sdk-v0.59.0...sdk-v0.60.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.59.0...sdk-v0.60.0)

### Features

* **api:** makes 1 hour TTL Cache Control generally available ([b3c97bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b3c97bd))
* **betas:** add context-1m-2025-08-07 ([a5f6db8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a5f6db8))

### Chores

* deprecate older claude-3-5 sonnet models ([#488](https://github.com/anthropics/anthropic-sdk-typescript/issues/488)) ([4fc9f76](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4fc9f76))
* **internal:** update comment in script ([8157062](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8157062))
* **internal:** update test skipping reason ([4ea623a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4ea623a))
* update @stainless-api/prism-cli to v5.15.0 ([43616bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/43616bd))

### Documentation

* **readme:** clarify beta feature usage ([3196064](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3196064))

## 0.59.0 (2025-08-08)

Full Changelog: [sdk-v0.58.0...sdk-v0.59.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.58.0...sdk-v0.59.0)

### Features

* **api:** search result content blocks ([f372c0d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f372c0d))

### Chores

* **internal:** move publish config ([5c1689e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5c1689e))

## 0.58.0 (2025-08-05)

Full Changelog: [sdk-v0.57.0...sdk-v0.58.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.57.0...sdk-v0.58.0)

### Features

* **api:** add claude-opus-4-1-20250805 ([08c61db](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/08c61db))
* **api:** adds support for text_editor_20250728 tool ([ca57d74](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ca57d74))
* **api:** removed older deprecated models ([352a5fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/352a5fd))
* update streaming error message to say 'required' not 'recommended' ([ffac3e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ffac3e0))
* update streaming error message to say 'required' not 'recommended' ([82a9ae5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/82a9ae5))
* **vertex:** support global endpoint ([#449](https://github.com/anthropics/anthropic-sdk-typescript/issues/449)) ([1c42030](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1c42030))

### Bug Fixes

* **internal/bootstrap:** install dependencies for all packages ([d3734f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d3734f9))
* **internal/bootstrap:** only build main package ([82428c7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/82428c7))
* **internal/bootstrap:** run build before installing other packages ([301f504](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/301f504))
* **internal/test:** use jest directly ([dab423b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dab423b))

### Chores

* **client:** add TextEditor_20250429 tool ([bcb557d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bcb557d))
* **internal:** remove redundant imports config ([555769d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/555769d))
* **internal:** version bump ([eb97e85](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/eb97e85))

## 0.57.0 (2025-07-21)

Full Changelog: [sdk-v0.56.0...sdk-v0.57.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.56.0...sdk-v0.57.0)

### Features

* **bedrock:** better edge runtime support ([#462](https://github.com/anthropics/anthropic-sdk-typescript/issues/462)) ([5f8d1bb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5f8d1bb))
* **client:** add breaking change detection to CI ([04332aa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/04332aa))

### Bug Fixes

* **bedrock:** fix lint errors ([aa40e9c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/aa40e9c))
* **internal:** fix type error for fromSSEResponse call ([2405664](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2405664))
* **vertex:** fix lint errors ([7772f78](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7772f78))

### Chores

* make some internal functions async ([9cc6c55](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9cc6c55))
* **ts:** reorder package.json imports ([e02b0a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e02b0a1))

## 0.56.0 (2025-07-03)

Full Changelog: [sdk-v0.55.1...sdk-v0.56.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.55.1...sdk-v0.56.0)

### Features

* **api:** add support for Search Result Content Blocks ([2910b28](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2910b28))
* **tests:** add fixture-based streaming tests and improve test coverage ([00424bc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/00424bc))
* **vertex:** add AuthClient interface support for improved auth flexibility ([b6f86e2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b6f86e2))

### Bug Fixes

* avoid console usage ([e5ab01d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e5ab01d))
* **bedrock:** fix bedrock logger ([f183bc9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f183bc9))

### Chores

* add docs to RequestOptions type ([38cb967](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/38cb967))
* **api:** update BetaCitationSearchResultLocation ([760be6b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/760be6b))

### Documentation

* model in examples ([9385376](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9385376))
* more beta updates ([7d8b8ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7d8b8ac))
* update model in readme ([b1799f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b1799f7))
* update models and non-beta batches ([5305cdb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5305cdb))

## 0.55.1 (2025-06-30)

Full Changelog: [sdk-v0.55.0...sdk-v0.55.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.55.0...sdk-v0.55.1)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([5fa2ebf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5fa2ebf))
* **client:** get fetchOptions type more reliably ([60673ab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/60673ab))
* **client:** use proxy in bedrock when requesting credentials from AWS ([8cfd227](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8cfd227))

### Chores

* **ci:** only run for pushes and fork pull requests ([3d1c911](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3d1c911))
* **client:** improve path param validation ([1638f13](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1638f13))

## 0.55.0 (2025-06-24)

Full Changelog: [sdk-v0.54.0...sdk-v0.55.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.54.0...sdk-v0.55.0)

### Features

* **client:** add support for endpoint-specific base URLs ([9be46a8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9be46a8))

### Bug Fixes

* **client:** explicitly copy fetch in withOptions ([3a5909b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3a5909b))
* **internal:** resolve conflict ([acfff05](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/acfff05))
* publish script — handle NPM errors correctly ([c4a6666](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c4a6666))
* **stream:** avoid event listener leak ([eb272af](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/eb272af))

### Chores

* **ci:** enable for pull requests ([8505818](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8505818))
* **client:** refactor imports ([d5dff04](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d5dff04))
* **internal:** add pure annotations, make base APIResource abstract ([183d39c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/183d39c))
* **readme:** update badges ([147f321](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/147f321))
* **readme:** use better example snippet for undocumented params ([5beafd5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5beafd5))

## 0.54.0 (2025-06-11)

Full Changelog: [sdk-v0.53.0...sdk-v0.54.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.53.0...sdk-v0.54.0)

### Features

* **api:** api update ([e923aa1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e923aa1))
* **api:** api update ([4877181](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4877181))
* **api:** manual updates ([99b0111](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/99b0111))
* **client:** add support for fine-grained-tool-streaming-2025-05-14 ([6b35dd9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6b35dd9))

### Bug Fixes

* **client:** deprecate BetaBase64PDFBlock in favor of BetaRequestDocumentBlock ([7fa10db](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7fa10db))
* **client:** improve error message in parsing JSON ([7c0cb84](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7c0cb84))
* **internal:** revert unintentional changes ([28dccec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/28dccec))

### Chores

* avoid type error in certain environments ([48c1a41](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/48c1a41))
* **tests:** add testing for invalid json raising ([52260c1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/52260c1))

## 0.53.0 (2025-06-04)

Full Changelog: [sdk-v0.52.0...sdk-v0.53.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.52.0...sdk-v0.53.0)

### Features

* **client:** add support for new text_editor_20250429 tool ([e49ebfb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e49ebfb))

### Bug Fixes

* **client:** correctly track input from server_tool_use input deltas ([4a14253](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4a14253))
* **client:** fix link to streaming responses docs ([2ad98be](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2ad98be))
* compat with more runtimes ([3c70ae3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3c70ae3))

### Chores

* adjust eslint.config.mjs ignore pattern ([ab404cf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ab404cf))
* **ci:** fix release workflow ([7e2e566](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7e2e566))
* **deps:** bump eslint-plugin-prettier ([8f973c4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8f973c4))
* **docs:** use top-level-await in example snippets ([b4a60ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b4a60ee))
* **examples:** show how to pass an authorization token to an MCP server ([340461b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/340461b))
* improve publish-npm script --latest tag logic ([4a7bdc0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4a7bdc0))
* **internal:** codegen related update ([345af47](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/345af47))
* **internal:** codegen related update ([6d924ef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6d924ef))
* **internal:** fix readablestream types in node 20 ([b68745b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b68745b))
* **internal:** fix release workflows ([a8da56f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a8da56f))

### Documentation

* **pagination:** improve naming ([8e62803](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8e62803))

## 0.52.0 (2025-05-22)

Full Changelog: [sdk-v0.51.0...sdk-v0.52.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.51.0...sdk-v0.52.0)

### Features

* **api:** add claude 4 models, files API, code execution tool, MCP connector and more ([769f9da](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/769f9da))

### Chores

* **internal:** codegen related update ([2ed236d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2ed236d))
* **internal:** version bump ([8ebaf61](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8ebaf61))

## 0.51.0 (2025-05-15)

Full Changelog: [sdk-v0.50.4...sdk-v0.51.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.50.4...sdk-v0.51.0)

### Features

* **bedrock:** support skipAuth on Bedrock client to bypass local auth requirements ([b661c5f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b661c5f))

### Bug Fixes

* **bedrock:** support model names with slashes ([cb5fa8a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cb5fa8a))

### Chores

* **package:** remove engines ([f0378ec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f0378ec))

## 0.50.4 (2025-05-12)

Full Changelog: [sdk-v0.50.3...sdk-v0.50.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.50.3...sdk-v0.50.4)

### Bug Fixes

* **stream:** correctly accumulate usage ([c55b4f0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c55b4f0))

## 0.50.3 (2025-05-09)

Full Changelog: [sdk-v0.50.2...sdk-v0.50.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.50.2...sdk-v0.50.3)

### Bug Fixes

* **client:** always overwrite when merging headers ([657912a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/657912a))
* **client:** always overwrite when merging headers ([bf70c9f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bf70c9f))

## 0.50.2 (2025-05-09)

Full Changelog: [sdk-v0.50.1...sdk-v0.50.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.50.1...sdk-v0.50.2)

### Bug Fixes

* **ci:** bump publish workflow to node 20 ([306a081](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/306a081))

### Chores

* **internal:** minor sync ([d89476f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d89476f))
* sync repo ([508e385](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/508e385))

### Documentation

* update readme ([ef0c60a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ef0c60a))

## 0.50.1 (2025-05-09)

Full Changelog: [sdk-v0.50.0...sdk-v0.50.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.50.0...sdk-v0.50.1)

## 0.50.0 (2025-05-09)

Full Changelog: [sdk-v0.41.0...sdk-v0.50.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.41.0...sdk-v0.50.0)

### Features

* **api:** adds web search capabilities to the Claude API ([b36623f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b36623f))
* **api:** manual updates ([80d5daa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/80d5daa))
* **api:** manual updates ([3124e2b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3124e2b))
* **client:** add withOptions helper ([caab783](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/caab783))

### Bug Fixes

* **bedrock,vertex:** update to new SDK version ([cb620bb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cb620bb))
* **client:** send all configured auth headers ([3961628](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3961628))
* **internal:** fix file uploads in node 18 jest ([1071b34](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1071b34))
* **mcp:** remove unused tools.ts ([4c4d763](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c4d763))
* **messages:** updates for server tools ([c2709b2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c2709b2))
* update old links ([f33a68a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f33a68a))
* **vertex,bedrock:** correct build script ([df895a7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/df895a7))

### Chores

* **bedrock:** add `skipAuth` option to allow users to let authorization be handled elsewhere ([ee58772](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ee58772))
* **bedrock:** bump [@aws-sdk](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/@aws-sdk) dependencies ([ff925db](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ff925db))
* **bedrock:** bump @aws-sdk/credential-providers ([9f611d6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9f611d6))
* **ci:** add timeout thresholds for CI jobs ([385f900](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/385f900))
* **ci:** only use depot for staging repos ([1f05880](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1f05880))
* **ci:** run on more branches and use depot runners ([7176150](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7176150))
* **client:** drop support for EOL node versions ([ffbb2da](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ffbb2da))
* **client:** minor internal fixes ([595678f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/595678f))
* **internal:** codegen related update ([a6ae129](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a6ae129))
* **internal:** fix format script ([9ce30ba](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9ce30ba))
* **internal:** formatting fixes ([7bd4594](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7bd4594))
* **internal:** improve index signature formatting ([7dc3e19](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7dc3e19))
* **internal:** improve node 18 shims ([c6780dd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c6780dd))
* **internal:** reduce CI branch coverage ([464431d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/464431d))
* **internal:** refactor utils ([b3dee57](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b3dee57))
* **internal:** share typescript helpers ([74187db](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/74187db))
* **internal:** upload builds and expand CI branch coverage ([bbda5d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bbda5d3))
* **perf:** faster base64 decoding ([975795a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/975795a))
* **tests:** improve enum examples ([66cf6d4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/66cf6d4))

### Documentation

* **readme:** fix typo ([6f8fce9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6f8fce9))

## 0.41.0 (2025-05-07)

Full Changelog: [sdk-v0.40.1...sdk-v0.41.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.40.1...sdk-v0.41.0)

### Features

* **api:** adds web search capabilities to the Claude API ([fae7e52](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fae7e52))

### Chores

* **ci:** bump node version for release workflows ([3502747](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3502747))

### Documentation

* add examples to tsdocs ([19a9285](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/19a9285))
* **readme:** fix typo ([735574e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/735574e))

## 0.40.1 (2025-04-28)

Full Changelog: [sdk-v0.40.0...sdk-v0.40.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.40.0...sdk-v0.40.1)

### Chores

* **bedrock:** bump [@aws-sdk](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/@aws-sdk) dependencies ([6440e1d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6440e1d))

## 0.40.0 (2025-04-25)

Full Changelog: [sdk-v0.39.0...sdk-v0.40.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.39.0...sdk-v0.40.0)

### Features

* add SKIP_BREW env var to ./scripts/bootstrap ([#710](https://github.com/anthropics/anthropic-sdk-typescript/issues/710)) ([1b8376a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1b8376a))
* **api:** extract ContentBlockDelta events into their own schemas ([#732](https://github.com/anthropics/anthropic-sdk-typescript/issues/732)) ([fd0ec83](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fd0ec83))
* **api:** manual updates ([39b64c9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/39b64c9))
* **api:** manual updates ([771e05b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/771e05b))
* **api:** manual updates ([ca6dbd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ca6dbd6))
* **api:** manual updates ([14df8cc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/14df8cc))
* **client:** accept RFC6838 JSON content types ([#713](https://github.com/anthropics/anthropic-sdk-typescript/issues/713)) ([fc32787](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fc32787))
* **mcp:** allow opt-in mcp resources and endpoints ([#720](https://github.com/anthropics/anthropic-sdk-typescript/issues/720)) ([9f3a54e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9f3a54e))

### Bug Fixes

* **api:** improve type resolution when importing as a package ([#738](https://github.com/anthropics/anthropic-sdk-typescript/issues/738)) ([8992ed4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8992ed4))
* avoid type error in certain environments ([#723](https://github.com/anthropics/anthropic-sdk-typescript/issues/723)) ([208fdaf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/208fdaf))
* **client:** deduplicate stop reason type ([#726](https://github.com/anthropics/anthropic-sdk-typescript/issues/726)) ([2d7cef1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2d7cef1))
* **client:** send `X-Stainless-Timeout` in seconds ([#733](https://github.com/anthropics/anthropic-sdk-typescript/issues/733)) ([cae4f77](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cae4f77))
* **client:** send all configured auth headers ([#742](https://github.com/anthropics/anthropic-sdk-typescript/issues/742)) ([86708b4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/86708b4))
* **exports:** ensure resource imports don't require /index ([#717](https://github.com/anthropics/anthropic-sdk-typescript/issues/717)) ([56b2a80](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/56b2a80))
* **internal:** work around https://github.com/vercel/next.js/issues/76881 ([#727](https://github.com/anthropics/anthropic-sdk-typescript/issues/727)) ([36ea0ef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/36ea0ef))
* **mcp:** remove unused tools.ts ([#740](https://github.com/anthropics/anthropic-sdk-typescript/issues/740)) ([26793e7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/26793e7))
* remove duplicate exports ([2df4cdd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2df4cdd))

### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([#725](https://github.com/anthropics/anthropic-sdk-typescript/issues/725)) ([271be7d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/271be7d))
* **bedrock:** bump @aws-sdk/credential-providers ([a4d88d7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a4d88d7))
* **ci:** add timeout thresholds for CI jobs ([1080c70](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1080c70))
* **ci:** only use depot for staging repos ([359dafa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/359dafa))
* **ci:** run on more branches and use depot runners ([3331315](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3331315))
* **client:** minor internal fixes ([fcf3e35](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fcf3e35))
* **internal:** add aliases for Record and Array ([#735](https://github.com/anthropics/anthropic-sdk-typescript/issues/735)) ([e0a4bec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e0a4bec))
* **internal:** add back release workflow ([68d54e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/68d54e5))
* **internal:** codegen related update ([#737](https://github.com/anthropics/anthropic-sdk-typescript/issues/737)) ([2a368bb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2a368bb))
* **internal:** fix lint ([2cf3641](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2cf3641))
* **internal:** import ordering changes ([#708](https://github.com/anthropics/anthropic-sdk-typescript/issues/708)) ([a5680e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a5680e1))
* **internal:** improve index signature formatting ([#739](https://github.com/anthropics/anthropic-sdk-typescript/issues/739)) ([627c5fa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/627c5fa))
* **internal:** reduce CI branch coverage ([6ed0bd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6ed0bd6))
* **internal:** remove CI condition ([#730](https://github.com/anthropics/anthropic-sdk-typescript/issues/730)) ([cc31518](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cc31518))
* **internal:** remove extra empty newlines ([#716](https://github.com/anthropics/anthropic-sdk-typescript/issues/716)) ([4d3c024](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4d3c024))
* **internal:** update config ([#728](https://github.com/anthropics/anthropic-sdk-typescript/issues/728)) ([ababd80](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ababd80))
* **internal:** upload builds and expand CI branch coverage ([#744](https://github.com/anthropics/anthropic-sdk-typescript/issues/744)) ([0b7432a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0b7432a))
* **tests:** improve enum examples ([#743](https://github.com/anthropics/anthropic-sdk-typescript/issues/743)) ([c1c93a7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c1c93a7))

## 0.39.0 (2025-02-28)

Full Changelog: [sdk-v0.38.0...sdk-v0.39.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.38.0...sdk-v0.39.0)

### Features

* **api:** add support for disabling tool calls ([#701](https://github.com/anthropics/anthropic-sdk-typescript/issues/701)) ([1602b51](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1602b51))

### Documentation

* update URLs from stainlessapi.com to stainless.com ([#699](https://github.com/anthropics/anthropic-sdk-typescript/issues/699)) ([05e33b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/05e33b7))

## 0.38.0 (2025-02-27)

Full Changelog: [sdk-v0.37.0...sdk-v0.38.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.37.0...sdk-v0.38.0)

### Features

* **api:** add URL source blocks for images and PDFs ([#698](https://github.com/anthropics/anthropic-sdk-typescript/issues/698)) ([16e7336](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/16e7336))

### Chores

* **internal:** update spec ([#692](https://github.com/anthropics/anthropic-sdk-typescript/issues/692)) ([142f221](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/142f221))

### Documentation

* add thinking examples ([db6f761](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/db6f761))

## 0.37.0 (2025-02-24)

Full Changelog: [sdk-v0.36.3...sdk-v0.37.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.36.3...sdk-v0.37.0)

### Features

* **api:** add claude-3.7 + support for thinking ([ffab311](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ffab311))
* **client:** send `X-Stainless-Timeout` header ([#679](https://github.com/anthropics/anthropic-sdk-typescript/issues/679)) ([1172430](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1172430))
* **pagination:** avoid fetching when has_more: false ([#680](https://github.com/anthropics/anthropic-sdk-typescript/issues/680)) ([d4df248](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d4df248))

### Bug Fixes

* **client:** fix export map for index exports ([#684](https://github.com/anthropics/anthropic-sdk-typescript/issues/684)) ([56d9c7a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/56d9c7a))
* correctly decode multi-byte characters over multiple chunks ([#681](https://github.com/anthropics/anthropic-sdk-typescript/issues/681)) ([e369e3d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e369e3d))
* optimize sse chunk reading off-by-one error ([#686](https://github.com/anthropics/anthropic-sdk-typescript/issues/686)) ([53669af](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/53669af))

### Chores

* **api:** update openapi spec url ([#678](https://github.com/anthropics/anthropic-sdk-typescript/issues/678)) ([84401b1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/84401b1))
* **internal:** add missing return type annotation ([#685](https://github.com/anthropics/anthropic-sdk-typescript/issues/685)) ([a8862b9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a8862b9))
* **internal:** fix devcontainers setup ([#689](https://github.com/anthropics/anthropic-sdk-typescript/issues/689)) ([8665946](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8665946))
* **internal:** reorder model constants ([#676](https://github.com/anthropics/anthropic-sdk-typescript/issues/676)) ([52a2a11](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/52a2a11))
* **internal:** update models used in tests ([52a2a11](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/52a2a11))

## 0.36.3 (2025-01-27)

Full Changelog: [sdk-v0.36.2...sdk-v0.36.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.36.2...sdk-v0.36.3)

### Bug Fixes

* **streaming:** accumulate citations ([#675](https://github.com/anthropics/anthropic-sdk-typescript/issues/675)) ([522118f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/522118f))

### Chores

* **docs:** updates ([#673](https://github.com/anthropics/anthropic-sdk-typescript/issues/673)) ([751ecd0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/751ecd0))

## 0.36.2 (2025-01-23)

Full Changelog: [sdk-v0.36.1...sdk-v0.36.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.36.1...sdk-v0.36.2)

### Bug Fixes

* **bedrock:** update streaming util import ([255c059](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/255c059))

## 0.36.1 (2025-01-23)

Full Changelog: [sdk-v0.36.0...sdk-v0.36.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.36.0...sdk-v0.36.1)

### Chores

* **tests:** fix types ([9efe3ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9efe3ee))

## 0.36.0 (2025-01-23)

Full Changelog: [sdk-v0.35.0...sdk-v0.36.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.35.0...sdk-v0.36.0)

### Features

* **api:** add citations ([#668](https://github.com/anthropics/anthropic-sdk-typescript/issues/668)) ([1fef177](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1fef177))
* **client:** support results endpoint ([#666](https://github.com/anthropics/anthropic-sdk-typescript/issues/666)) ([db5fffe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/db5fffe))
* **stream:** expose `response` property as well ([b0235c7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b0235c7))

### Chores

* **bedrock:** bump dependency on @anthropic-ai/sdk ([8745ca2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8745ca2))
* **internal:** fix import ([628b55e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/628b55e))
* **internal:** minor restructuring ([#664](https://github.com/anthropics/anthropic-sdk-typescript/issues/664)) ([57aefa7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/57aefa7))
* **vertex:** bump dependency on @anthropic-ai/sdk ([a1c7fcd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a1c7fcd))

## 0.35.0 (2025-01-21)

Full Changelog: [sdk-v0.34.0...sdk-v0.35.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.34.0...sdk-v0.35.0)

### Features

* add beta message streaming helpers ([#655](https://github.com/anthropics/anthropic-sdk-typescript/issues/655)) ([d7b5af1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d7b5af1))
* **stream:** add `.withResponse()` ([#654](https://github.com/anthropics/anthropic-sdk-typescript/issues/654)) ([b54477f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b54477f))
* **streaming:** add `.request_id` getter ([4572478](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4572478))

### Bug Fixes

* **docs:** correct results return type ([#657](https://github.com/anthropics/anthropic-sdk-typescript/issues/657)) ([4e6d031](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4e6d031))
* **examples:** add token counting example ([2498e2e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2498e2e))
* send correct Accept header for certain endpoints ([#651](https://github.com/anthropics/anthropic-sdk-typescript/issues/651)) ([17ffaeb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/17ffaeb))
* **vertex:** add beta.messages.countTokens method ([51d3f23](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/51d3f23))

### Chores

* deprecate more models ([661f5f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/661f5f9))
* **internal:** add test ([#660](https://github.com/anthropics/anthropic-sdk-typescript/issues/660)) ([3ec7d1a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3ec7d1a))
* **internal:** temporary revert commit ([#643](https://github.com/anthropics/anthropic-sdk-typescript/issues/643)) ([43dd43c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/43dd43c))
* **internal:** update examples ([#649](https://github.com/anthropics/anthropic-sdk-typescript/issues/649)) ([036a239](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/036a239))
* **types:** add `| undefined` to client options properties ([#656](https://github.com/anthropics/anthropic-sdk-typescript/issues/656)) ([d642298](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d642298))

### Documentation

* **readme:** fix misplaced period ([#650](https://github.com/anthropics/anthropic-sdk-typescript/issues/650)) ([8754744](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8754744))
* **readme:** fix Request IDs example ([#659](https://github.com/anthropics/anthropic-sdk-typescript/issues/659)) ([6d3162d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6d3162d))

## 0.34.0 (2024-12-20)

Full Changelog: [sdk-v0.33.1...sdk-v0.34.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.33.1...sdk-v0.34.0)

### Features

* **api:** add message batch delete endpoint ([#640](https://github.com/anthropics/anthropic-sdk-typescript/issues/640)) ([54f7e1f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/54f7e1f))

### Bug Fixes

* **client:** normalize method ([#639](https://github.com/anthropics/anthropic-sdk-typescript/issues/639)) ([384bb04](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/384bb04))

### Chores

* bump testing data uri ([#637](https://github.com/anthropics/anthropic-sdk-typescript/issues/637)) ([3f23530](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3f23530))
* **internal:** temporary revert commit ([#643](https://github.com/anthropics/anthropic-sdk-typescript/issues/643)) ([8057b1e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8057b1e))

### Documentation

* minor formatting changes ([#641](https://github.com/anthropics/anthropic-sdk-typescript/issues/641)) ([8b362ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8b362ee))
* **readme:** add alpha callout ([#646](https://github.com/anthropics/anthropic-sdk-typescript/issues/646)) ([640304c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/640304c))

## 0.33.1 (2024-12-17)

Full Changelog: [sdk-v0.33.0...sdk-v0.33.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.33.0...sdk-v0.33.1)

### Bug Fixes

* **vertex:** remove `anthropic_version` deletion for token counting ([88221be](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/88221be))

### Chores

* **internal:** fix some typos ([#633](https://github.com/anthropics/anthropic-sdk-typescript/issues/633)) ([a0298f5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a0298f5))

## 0.33.0 (2024-12-17)

Full Changelog: [sdk-v0.32.1...sdk-v0.33.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.32.1...sdk-v0.33.0)

### Features

* **api:** general availability updates ([93d1316](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/93d1316))
* **api:** general availability updates ([#631](https://github.com/anthropics/anthropic-sdk-typescript/issues/631)) ([b5c92e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b5c92e5))
* **client:** add ._request_id property to object responses ([#596](https://github.com/anthropics/anthropic-sdk-typescript/issues/596)) ([9d6d584](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9d6d584))
* **internal:** make git install file structure match npm ([#617](https://github.com/anthropics/anthropic-sdk-typescript/issues/617)) ([d3dd7d5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d3dd7d5))
* **vertex:** support token counting ([9e76b4d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9e76b4d))

### Bug Fixes

* **docs:** add missing await to pagination example ([#609](https://github.com/anthropics/anthropic-sdk-typescript/issues/609)) ([e303077](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e303077))
* **types:** remove anthropic-instant-1.2 model ([#599](https://github.com/anthropics/anthropic-sdk-typescript/issues/599)) ([e222a4d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e222a4d))

### Chores

* **api:** update spec version ([#607](https://github.com/anthropics/anthropic-sdk-typescript/issues/607)) ([ea44f9a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ea44f9a))
* **api:** update spec version ([#629](https://github.com/anthropics/anthropic-sdk-typescript/issues/629)) ([a25295c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a25295c))
* **bedrock,vertex:** remove unsupported countTokens method ([#597](https://github.com/anthropics/anthropic-sdk-typescript/issues/597)) ([17b7da5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/17b7da5))
* **bedrock:** remove unsupported methods ([6458dc1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6458dc1))
* **ci:** remove unneeded workflow ([#594](https://github.com/anthropics/anthropic-sdk-typescript/issues/594)) ([7572e48](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7572e48))
* **client:** drop unused devDependency ([#610](https://github.com/anthropics/anthropic-sdk-typescript/issues/610)) ([5d0d523](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5d0d523))
* improve browser error message ([#613](https://github.com/anthropics/anthropic-sdk-typescript/issues/613)) ([c26121e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c26121e))
* **internal:** bump cross-spawn to v7.0.6 ([#624](https://github.com/anthropics/anthropic-sdk-typescript/issues/624)) ([e58ba9a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e58ba9a))
* **internal:** remove unnecessary getRequestClient function ([#623](https://github.com/anthropics/anthropic-sdk-typescript/issues/623)) ([882c45f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/882c45f))
* **internal:** update isAbsoluteURL ([#627](https://github.com/anthropics/anthropic-sdk-typescript/issues/627)) ([2528ea0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2528ea0))
* **internal:** update spec ([#630](https://github.com/anthropics/anthropic-sdk-typescript/issues/630)) ([82cac06](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/82cac06))
* **internal:** use reexports not destructuring ([#604](https://github.com/anthropics/anthropic-sdk-typescript/issues/604)) ([e4daff2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e4daff2))
* remove redundant word in comment ([#615](https://github.com/anthropics/anthropic-sdk-typescript/issues/615)) ([ef57a10](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ef57a10))
* **tests:** limit array example length ([#611](https://github.com/anthropics/anthropic-sdk-typescript/issues/611)) ([91dc181](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/91dc181))
* **types:** nicer error class types + jsdocs ([#626](https://github.com/anthropics/anthropic-sdk-typescript/issues/626)) ([0287993](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0287993))

### Documentation

* remove suggestion to use `npm` call out ([#614](https://github.com/anthropics/anthropic-sdk-typescript/issues/614)) ([6369261](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6369261))
* use latest sonnet in example snippets ([#625](https://github.com/anthropics/anthropic-sdk-typescript/issues/625)) ([f70882b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f70882b))

## 0.32.1 (2024-11-05)

Full Changelog: [sdk-v0.32.0...sdk-v0.32.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.32.0...sdk-v0.32.1)

### Bug Fixes

* **bedrock:** don't mutate request body inputs ([f83b535](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f83b535))
* **vertex:** don't mutate request body inputs ([e9a82e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e9a82e5))

## 0.32.0 (2024-11-04)

Full Changelog: [sdk-v0.31.0...sdk-v0.32.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.31.0...sdk-v0.32.0)

### Features

* **api:** add new haiku model ([#587](https://github.com/anthropics/anthropic-sdk-typescript/issues/587)) ([983b13c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/983b13c))

### Bug Fixes

* don't require deno to run build-deno ([#586](https://github.com/anthropics/anthropic-sdk-typescript/issues/586)) ([0e431d6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0e431d6))
* **types:** add missing token-counting-2024-11-01 ([#583](https://github.com/anthropics/anthropic-sdk-typescript/issues/583)) ([13d629c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/13d629c))

### Chores

* remove unused build-deno condition ([#585](https://github.com/anthropics/anthropic-sdk-typescript/issues/585)) ([491e8fe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/491e8fe))

## 0.31.0 (2024-11-01)

Full Changelog: [sdk-v0.30.1...sdk-v0.31.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.30.1...sdk-v0.31.0)

### Features

* **api:** add message token counting & PDFs support ([#582](https://github.com/anthropics/anthropic-sdk-typescript/issues/582)) ([b593837](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b593837))

### Bug Fixes

* **countTokens:** correctly set beta header ([1680757](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1680757))
* **internal:** support pnpm git installs ([#579](https://github.com/anthropics/anthropic-sdk-typescript/issues/579)) ([86bb102](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/86bb102))
* **types:** add missing token-counting-2024-11-01 ([aff1546](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/aff1546))

### Reverts

* disable isolatedModules and change imports ([#575](https://github.com/anthropics/anthropic-sdk-typescript/issues/575)) ([2c3b176](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c3b176))

### Chores

* **internal:** update spec version ([#571](https://github.com/anthropics/anthropic-sdk-typescript/issues/571)) ([5760012](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5760012))

### Documentation

* **readme:** minor typo fixes ([#577](https://github.com/anthropics/anthropic-sdk-typescript/issues/577)) ([8412854](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8412854))

### Refactors

* enable isolatedModules and change imports ([#573](https://github.com/anthropics/anthropic-sdk-typescript/issues/573)) ([9068b4b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9068b4b))
* use type imports for type-only imports ([#580](https://github.com/anthropics/anthropic-sdk-typescript/issues/580)) ([2c8a337](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c8a337))

## 0.30.1 (2024-10-23)

Full Changelog: [sdk-v0.30.0...sdk-v0.30.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.30.0...sdk-v0.30.1)

### Bug Fixes

* **bedrock:** correct messages beta handling ([9b57586](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9b57586))
* **vertex:** correct messages beta handling ([26f21ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/26f21ee))

### Chores

* **internal:** bumps eslint and related dependencies ([#570](https://github.com/anthropics/anthropic-sdk-typescript/issues/570)) ([0b3ebb0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0b3ebb0))

## 0.30.0 (2024-10-22)

Full Changelog: [sdk-v0.29.2...sdk-v0.30.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.29.2...sdk-v0.30.0)

### Features

* **api:** add new model and `computer-use-2024-10-22` beta ([6981d89](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6981d89))
* **bedrock:** add beta.messages.create() method ([6317592](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6317592))
* **vertex:** add beta.messages.create() ([22cfdba](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/22cfdba))

### Bug Fixes

* **client:** respect x-stainless-retry-count default headers ([#562](https://github.com/anthropics/anthropic-sdk-typescript/issues/562)) ([274573f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/274573f))

### Chores

* **api:** add title ([#564](https://github.com/anthropics/anthropic-sdk-typescript/issues/564)) ([a8b7544](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a8b7544))
* **internal:** update spec ([#566](https://github.com/anthropics/anthropic-sdk-typescript/issues/566)) ([5b998ea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5b998ea))

## 0.29.2 (2024-10-17)

Full Changelog: [sdk-v0.29.1...sdk-v0.29.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.29.1...sdk-v0.29.2)

### Bug Fixes

* **types:** remove misleading betas TypedDict property for the Batch API ([#559](https://github.com/anthropics/anthropic-sdk-typescript/issues/559)) ([4de5d0a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4de5d0a))

## 0.29.1 (2024-10-15)

Full Changelog: [sdk-v0.29.0...sdk-v0.29.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.29.0...sdk-v0.29.1)

### Bug Fixes

* **beta:** merge betas param with the default value ([#556](https://github.com/anthropics/anthropic-sdk-typescript/issues/556)) ([5520bbc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5520bbc))

### Chores

* **internal:** update spec URL ([#554](https://github.com/anthropics/anthropic-sdk-typescript/issues/554)) ([1fb6448](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1fb6448))

## 0.29.0 (2024-10-08)

Full Changelog: [sdk-v0.28.0...sdk-v0.29.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.28.0...sdk-v0.29.0)

### Features

* **api:** add message batches api ([4f114d5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4f114d5))

### Chores

* **internal:** move LineDecoder to a separate file ([#541](https://github.com/anthropics/anthropic-sdk-typescript/issues/541)) ([fd42469](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fd42469))
* **internal:** pass props through internal parser ([#549](https://github.com/anthropics/anthropic-sdk-typescript/issues/549)) ([dd71955](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dd71955))

### Refactors

* **types:** improve metadata type names ([#547](https://github.com/anthropics/anthropic-sdk-typescript/issues/547)) ([cef499c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cef499c))
* **types:** improve metadata types ([#546](https://github.com/anthropics/anthropic-sdk-typescript/issues/546)) ([3fe538b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3fe538b))
* **types:** improve tool type names ([#543](https://github.com/anthropics/anthropic-sdk-typescript/issues/543)) ([18dbe77](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/18dbe77))
* **types:** improve tool type names ([#544](https://github.com/anthropics/anthropic-sdk-typescript/issues/544)) ([fc2d823](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fc2d823))

## 0.28.0 (2024-10-04)

Full Changelog: [sdk-v0.27.3...sdk-v0.28.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.27.3...sdk-v0.28.0)

### Features

* **api:** support disabling parallel tool use ([#540](https://github.com/anthropics/anthropic-sdk-typescript/issues/540)) ([df0032f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/df0032f))
* **client:** allow overriding retry count header ([#536](https://github.com/anthropics/anthropic-sdk-typescript/issues/536)) ([ec11f91](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ec11f91))
* **client:** send retry count header ([#533](https://github.com/anthropics/anthropic-sdk-typescript/issues/533)) ([401b81c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/401b81c))

### Bug Fixes

* **types:** remove leftover polyfill usage ([#532](https://github.com/anthropics/anthropic-sdk-typescript/issues/532)) ([ac188b2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ac188b2))

### Chores

* better object fallback behaviour for casting errors ([#503](https://github.com/anthropics/anthropic-sdk-typescript/issues/503)) ([3660e97](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3660e97))
* better object fallback behaviour for casting errors ([#526](https://github.com/anthropics/anthropic-sdk-typescript/issues/526)) ([4ffb2e4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4ffb2e4))
* **internal:** add dev dependency ([#531](https://github.com/anthropics/anthropic-sdk-typescript/issues/531)) ([a9c127b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a9c127b))

### Documentation

* improve and reference contributing documentation ([#539](https://github.com/anthropics/anthropic-sdk-typescript/issues/539)) ([cbef925](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cbef925))
* update CONTRIBUTING.md ([#528](https://github.com/anthropics/anthropic-sdk-typescript/issues/528)) ([2609dec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2609dec))

## 0.27.3 (2024-09-09)

Full Changelog: [sdk-v0.27.2...sdk-v0.27.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.27.2...sdk-v0.27.3)

### Bug Fixes

* **streaming:** correct error message serialisation ([#524](https://github.com/anthropics/anthropic-sdk-typescript/issues/524)) ([e150fa4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e150fa4))
* **uploads:** avoid making redundant memory copies ([#520](https://github.com/anthropics/anthropic-sdk-typescript/issues/520)) ([b6d2638](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b6d2638))

### Chores

* **docs:** update browser support information ([#522](https://github.com/anthropics/anthropic-sdk-typescript/issues/522)) ([ce7aeb5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ce7aeb5))

## 0.27.2 (2024-09-04)

Full Changelog: [sdk-v0.27.1...sdk-v0.27.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.27.1...sdk-v0.27.2)

### Bug Fixes

* **client:** correct File construction from node-fetch Responses ([#518](https://github.com/anthropics/anthropic-sdk-typescript/issues/518)) ([62ae46f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/62ae46f))

### Chores

* **api:** deprecate claude-1 models ([53644d2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/53644d2))
* **ci:** install deps via ./script/bootstrap ([#515](https://github.com/anthropics/anthropic-sdk-typescript/issues/515)) ([90a8da1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/90a8da1))
* **internal:** dependency updates ([#519](https://github.com/anthropics/anthropic-sdk-typescript/issues/519)) ([b7b0cd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b7b0cd6))
* run tsc as part of lint script ([#513](https://github.com/anthropics/anthropic-sdk-typescript/issues/513)) ([c8127cf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c8127cf))

## 0.27.1 (2024-08-27)

Full Changelog: [sdk-v0.27.0...sdk-v0.27.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.27.0...sdk-v0.27.1)

### Chores

* **ci:** check for build errors ([#511](https://github.com/anthropics/anthropic-sdk-typescript/issues/511)) ([3ab1d3d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3ab1d3d))

## 0.27.0 (2024-08-21)

Full Changelog: [sdk-v0.26.1...sdk-v0.27.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.26.1...sdk-v0.27.0)

### Features

* **client:** add support for browser usage ([#504](https://github.com/anthropics/anthropic-sdk-typescript/issues/504)) ([93c5f16](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/93c5f16))

### Documentation

* **readme:** update formatting and clarity for CORS flag ([9cb2c35](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9cb2c35))

## 0.26.1 (2024-08-15)

Full Changelog: [sdk-v0.26.0...sdk-v0.26.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.26.0...sdk-v0.26.1)

### Chores

* **ci:** add CODEOWNERS file ([#498](https://github.com/anthropics/anthropic-sdk-typescript/issues/498)) ([c34433f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c34433f))
* **docs/api:** update prompt caching helpers ([04195a3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/04195a3))

## 0.26.0 (2024-08-14)

Full Changelog: [sdk-v0.25.2...sdk-v0.26.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.25.2...sdk-v0.26.0)

### Features

* **api:** add prompt caching beta ([c920b77](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c920b77))
* **client:** add streaming helpers ([39abc26](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/39abc26))

### Chores

* **examples:** minor formatting changes ([#491](https://github.com/anthropics/anthropic-sdk-typescript/issues/491)) ([8afef58](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8afef58))

## 0.25.2 (2024-08-12)

Full Changelog: [sdk-v0.25.1...sdk-v0.25.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.25.1...sdk-v0.25.2)

### Chores

* **ci:** bump prism mock server version ([#490](https://github.com/anthropics/anthropic-sdk-typescript/issues/490)) ([bfb27f5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bfb27f5))
* **ci:** minor changes ([#488](https://github.com/anthropics/anthropic-sdk-typescript/issues/488)) ([747fd97](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/747fd97))

## 0.25.1 (2024-08-09)

Full Changelog: [sdk-v0.25.0...sdk-v0.25.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.25.0...sdk-v0.25.1)

### Chores

* **internal:** update publish npm script ([#483](https://github.com/anthropics/anthropic-sdk-typescript/issues/483)) ([fb862ff](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fb862ff))
* **internal:** updates ([#487](https://github.com/anthropics/anthropic-sdk-typescript/issues/487)) ([67a3325](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/67a3325))
* sync openapi version ([#481](https://github.com/anthropics/anthropic-sdk-typescript/issues/481)) ([5fd7e21](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5fd7e21))
* sync openapi version ([#485](https://github.com/anthropics/anthropic-sdk-typescript/issues/485)) ([e74c522](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e74c522))
* sync openapi version ([#486](https://github.com/anthropics/anthropic-sdk-typescript/issues/486)) ([ad98e9e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ad98e9e))

## 0.25.0 (2024-07-29)

Full Changelog: [sdk-v0.24.3...sdk-v0.25.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.24.3...sdk-v0.25.0)

### Features

* add back compat alias for InputJsonDelta ([8b08161](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8b08161))
* **client:** make request-id header more accessible ([#462](https://github.com/anthropics/anthropic-sdk-typescript/issues/462)) ([5ea6f8b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5ea6f8b))

### Bug Fixes

* **compat:** remove ReadableStream polyfill redundant since node v16 ([#478](https://github.com/anthropics/anthropic-sdk-typescript/issues/478)) ([75f5710](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/75f5710))
* use relative paths ([#475](https://github.com/anthropics/anthropic-sdk-typescript/issues/475)) ([a8ca93c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a8ca93c))

### Chores

* **bedrock:** use `chunk` for internal SSE parsing instead of `completion` ([#472](https://github.com/anthropics/anthropic-sdk-typescript/issues/472)) ([0f6190a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0f6190a))
* **ci:** also run workflows for PRs targeting `next` ([#464](https://github.com/anthropics/anthropic-sdk-typescript/issues/464)) ([cc405a8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cc405a8))
* **docs:** fix incorrect client var names ([#479](https://github.com/anthropics/anthropic-sdk-typescript/issues/479)) ([a247935](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a247935))
* **docs:** mention lack of support for web browser runtimes ([#468](https://github.com/anthropics/anthropic-sdk-typescript/issues/468)) ([968a7fb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/968a7fb))
* **docs:** minor update to formatting of API link in README ([#467](https://github.com/anthropics/anthropic-sdk-typescript/issues/467)) ([50b9f2b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/50b9f2b))
* **docs:** rename anthropic const to client ([#471](https://github.com/anthropics/anthropic-sdk-typescript/issues/471)) ([e1a7f9f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e1a7f9f))
* **docs:** use client instead of package name in Node examples ([#469](https://github.com/anthropics/anthropic-sdk-typescript/issues/469)) ([8961ebf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8961ebf))
* **internal:** add constant for default timeout ([#480](https://github.com/anthropics/anthropic-sdk-typescript/issues/480)) ([dc89753](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dc89753))
* **internal:** minor changes to tests ([#465](https://github.com/anthropics/anthropic-sdk-typescript/issues/465)) ([c1fd563](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c1fd563))
* **internal:** remove old reference to check-test-server ([8dc9afc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8dc9afc))
* sync spec ([#470](https://github.com/anthropics/anthropic-sdk-typescript/issues/470)) ([b493aa4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b493aa4))
* **tests:** update prism version ([#473](https://github.com/anthropics/anthropic-sdk-typescript/issues/473)) ([6f21ecf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6f21ecf))

### Refactors

* extract model out to a named type and rename partialjson ([#477](https://github.com/anthropics/anthropic-sdk-typescript/issues/477)) ([d2d4e36](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d2d4e36))

## 0.24.3 (2024-07-01)

Full Changelog: [sdk-v0.24.2...sdk-v0.24.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.24.2...sdk-v0.24.3)

### Bug Fixes

* **types:** avoid errors on certain TS versions ([dd6aca5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dd6aca5))

## 0.24.2 (2024-06-28)

Full Changelog: [sdk-v0.24.1...sdk-v0.24.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.24.1...sdk-v0.24.2)

### Bug Fixes

* **partial-json:** don't error on unknown tokens ([d212ce1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d212ce1))
* **partial-json:** handle `null` token properly ([f53742f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f53742f))

### Chores

* gitignore test server logs ([#451](https://github.com/anthropics/anthropic-sdk-typescript/issues/451)) ([ee1308f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ee1308f))
* **tests:** add unit tests for partial-json-parser ([4fb3bea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4fb3bea))

## 0.24.1 (2024-06-25)

Full Changelog: [sdk-v0.24.0...sdk-v0.24.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.24.0...sdk-v0.24.1)

### Bug Fixes

* **api:** add string to tool result block ([#448](https://github.com/anthropics/anthropic-sdk-typescript/issues/448)) ([87af4e9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/87af4e9))

### Chores

* **internal:** minor reformatting ([#444](https://github.com/anthropics/anthropic-sdk-typescript/issues/444)) ([46790bb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/46790bb))
* **internal:** replace deprecated aws-sdk packages with [@smithy](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/@smithy) ([#447](https://github.com/anthropics/anthropic-sdk-typescript/issues/447)) ([4328cbf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4328cbf))

## 0.24.0 (2024-06-20)

Full Changelog: [sdk-v0.23.0...sdk-v0.24.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.23.0...sdk-v0.24.0)

### Features

* **api:** add new claude-3-5-sonnet-20240620 model ([#438](https://github.com/anthropics/anthropic-sdk-typescript/issues/438)) ([8d60d1b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8d60d1b))

## 0.23.0 (2024-06-14)

Full Changelog: [sdk-v0.22.0...sdk-v0.23.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.22.0...sdk-v0.23.0)

### Features

* support `application/octet-stream` request bodies ([#436](https://github.com/anthropics/anthropic-sdk-typescript/issues/436)) ([3a8e6ed](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3a8e6ed))

### Bug Fixes

* allow git imports for pnpm ([#433](https://github.com/anthropics/anthropic-sdk-typescript/issues/433)) ([a4f5263](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a4f5263))

## 0.22.0 (2024-05-30)

Full Changelog: [sdk-v0.21.1...sdk-v0.22.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.21.1...sdk-v0.22.0)

### Features

* **api/types:** add stream event type aliases with a Raw prefix ([#428](https://github.com/anthropics/anthropic-sdk-typescript/issues/428)) ([1e367e4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1e367e4))
* **api:** tool use is GA and available on 3P ([#429](https://github.com/anthropics/anthropic-sdk-typescript/issues/429)) ([2decf85](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2decf85))
* **bedrock:** support tools ([91fc61a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/91fc61a))
* **streaming:** add tools support ([4c83bb1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c83bb1))
* **vertex:** support tools ([acf0aa7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/acf0aa7))

### Documentation

* **helpers:** mention inputJson event ([0ef0e39](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0ef0e39))
* **readme:** add bundle size badge ([#426](https://github.com/anthropics/anthropic-sdk-typescript/issues/426)) ([bf7c1fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bf7c1fd))

## 0.21.1 (2024-05-21)

Full Changelog: [sdk-v0.21.0...sdk-v0.21.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.21.0...sdk-v0.21.1)

### Chores

* **docs:** fix typo ([#423](https://github.com/anthropics/anthropic-sdk-typescript/issues/423)) ([d42f458](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d42f458))
* **internal:** run build script over sub-packages ([6f04f66](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6f04f66))

## 0.21.0 (2024-05-16)

Full Changelog: [sdk-v0.20.9...sdk-v0.21.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.9...sdk-v0.21.0)

### Features

* **api:** add `tool_choice` param, image block params inside `tool_result.content`, and streaming for `tool_use` blocks ([#418](https://github.com/anthropics/anthropic-sdk-typescript/issues/418)) ([421a1e6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/421a1e6))

### Chores

* **docs:** add SECURITY.md ([#411](https://github.com/anthropics/anthropic-sdk-typescript/issues/411)) ([bf2ad84](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bf2ad84))
* **internal:** add slightly better logging to scripts ([#415](https://github.com/anthropics/anthropic-sdk-typescript/issues/415)) ([7a042d2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7a042d2))
* **internal:** fix generated version numbers ([#413](https://github.com/anthropics/anthropic-sdk-typescript/issues/413)) ([ea77063](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ea77063))

## 0.20.9 (2024-05-07)

Full Changelog: [sdk-v0.20.8...sdk-v0.20.9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.8...sdk-v0.20.9)

### Bug Fixes

* **package:** revert recent client file change ([#409](https://github.com/anthropics/anthropic-sdk-typescript/issues/409)) ([9054249](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9054249))

### Chores

* **internal:** add link to openapi spec ([#406](https://github.com/anthropics/anthropic-sdk-typescript/issues/406)) ([39c856d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/39c856d))
* **internal:** bump prism version ([#407](https://github.com/anthropics/anthropic-sdk-typescript/issues/407)) ([0c1eb5d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0c1eb5d))
* **internal:** move client class to separate file ([#408](https://github.com/anthropics/anthropic-sdk-typescript/issues/408)) ([b5e1e4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b5e1e4a))
* **internal:** refactor scripts ([#404](https://github.com/anthropics/anthropic-sdk-typescript/issues/404)) ([f60e2d8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f60e2d8))

## 0.20.8 (2024-04-29)

Full Changelog: [sdk-v0.20.7...sdk-v0.20.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.7...sdk-v0.20.8)

### Chores

* **internal:** add scripts/test and scripts/mock ([#403](https://github.com/anthropics/anthropic-sdk-typescript/issues/403)) ([bdc6011](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bdc6011))
* **internal:** use actions/checkout@v4 for codeflow ([#400](https://github.com/anthropics/anthropic-sdk-typescript/issues/400)) ([6d565d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6d565d3))

## 0.20.7 (2024-04-24)

Full Changelog: [sdk-v0.20.6...sdk-v0.20.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.6...sdk-v0.20.7)

### Chores

* **internal:** use @swc/jest for running tests ([#397](https://github.com/anthropics/anthropic-sdk-typescript/issues/397)) ([0dbca67](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0dbca67))

## 0.20.6 (2024-04-17)

Full Changelog: [sdk-v0.20.5...sdk-v0.20.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.5...sdk-v0.20.6)

### Build System

* configure UTF-8 locale in devcontainer ([#393](https://github.com/anthropics/anthropic-sdk-typescript/issues/393)) ([db10244](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/db10244))

## 0.20.5 (2024-04-15)

Full Changelog: [sdk-v0.20.4...sdk-v0.20.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.4...sdk-v0.20.5)

### Chores

* **internal:** formatting ([#390](https://github.com/anthropics/anthropic-sdk-typescript/issues/390)) ([b7861b9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b7861b9))

## 0.20.4 (2024-04-11)

Full Changelog: [sdk-v0.20.3...sdk-v0.20.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.3...sdk-v0.20.4)

### Chores

* **internal:** update gitignore ([#388](https://github.com/anthropics/anthropic-sdk-typescript/issues/388)) ([03f03a2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/03f03a2))

## 0.20.3 (2024-04-10)

Full Changelog: [sdk-v0.20.2...sdk-v0.20.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.2...sdk-v0.20.3)

### Bug Fixes

* **vertex:** correct core client dependency constraint ([#384](https://github.com/anthropics/anthropic-sdk-typescript/issues/384)) ([de29699](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/de29699))

## 0.20.2 (2024-04-09)

Full Changelog: [sdk-v0.20.1...sdk-v0.20.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.1...sdk-v0.20.2)

### Chores

* **internal:** update lock files ([#377](https://github.com/anthropics/anthropic-sdk-typescript/issues/377)) ([6d239ef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6d239ef))

## 0.20.1 (2024-04-04)

Full Changelog: [sdk-v0.20.0...sdk-v0.20.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.20.0...sdk-v0.20.1)

### Documentation

* **readme:** mention tool use ([#375](https://github.com/anthropics/anthropic-sdk-typescript/issues/375)) ([72356dd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/72356dd))

## 0.20.0 (2024-04-04)

Full Changelog: [sdk-v0.19.2...sdk-v0.20.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.19.2...sdk-v0.20.0)

### Features

* **api:** tool use beta ([#374](https://github.com/anthropics/anthropic-sdk-typescript/issues/374)) ([e28514a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e28514a))

### Bug Fixes

* **types:** correctly mark type as a required property in requests ([#371](https://github.com/anthropics/anthropic-sdk-typescript/issues/371)) ([a04edd8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a04edd8))

### Chores

* **types:** consistent naming for text block types ([#373](https://github.com/anthropics/anthropic-sdk-typescript/issues/373)) ([84a6a58](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/84a6a58))

## 0.19.2 (2024-04-04)

Full Changelog: [sdk-v0.19.1...sdk-v0.19.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.19.1...sdk-v0.19.2)

### Bug Fixes

* **streaming:** handle special line characters and fix multi-byte character decoding ([#370](https://github.com/anthropics/anthropic-sdk-typescript/issues/370)) ([7a97b38](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7a97b38))

### Chores

* **deps:** bump yarn to v1.22.22 ([#369](https://github.com/anthropics/anthropic-sdk-typescript/issues/369)) ([603d7b1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/603d7b1))
* **deps:** remove unused dependency digest-fetch ([#368](https://github.com/anthropics/anthropic-sdk-typescript/issues/368)) ([df1df0f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/df1df0f))

### Documentation

* **readme:** change undocumented params wording ([#363](https://github.com/anthropics/anthropic-sdk-typescript/issues/363)) ([4222e08](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4222e08))

## 0.19.1 (2024-03-29)

Full Changelog: [sdk-v0.19.0...sdk-v0.19.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.19.0...sdk-v0.19.1)

### Bug Fixes

* **client:** correctly send deno version header ([#354](https://github.com/anthropics/anthropic-sdk-typescript/issues/354)) ([ad5162b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ad5162b))
* handle process.env being undefined in debug func ([#351](https://github.com/anthropics/anthropic-sdk-typescript/issues/351)) ([3b0f38a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3b0f38a))
* **streaming:** correct accumulation of output tokens ([#361](https://github.com/anthropics/anthropic-sdk-typescript/issues/361)) ([76af283](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/76af283))
* **types:** correct typo claude-2.1' to claude-2.1 ([#352](https://github.com/anthropics/anthropic-sdk-typescript/issues/352)) ([0d5efb9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0d5efb9))

### Chores

* **internal:** add type ([#359](https://github.com/anthropics/anthropic-sdk-typescript/issues/359)) ([9456414](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9456414))

### Documentation

* **bedrock:** fix dead link ([#356](https://github.com/anthropics/anthropic-sdk-typescript/issues/356)) ([a953e00](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a953e00))
* **readme:** consistent use of sentence case in headings ([#347](https://github.com/anthropics/anthropic-sdk-typescript/issues/347)) ([30f45d1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/30f45d1))
* **readme:** document how to make undocumented requests ([#349](https://github.com/anthropics/anthropic-sdk-typescript/issues/349)) ([f92c50a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f92c50a))

## 0.19.0 (2024-03-19)

Full Changelog: [sdk-v0.18.0...sdk-v0.19.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.18.0...sdk-v0.19.0)

### Features

* **vertex:** add support for overriding google auth ([#338](https://github.com/anthropics/anthropic-sdk-typescript/issues/338)) ([28d98c4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/28d98c4))
* **vertex:** api is no longer in private beta ([#344](https://github.com/anthropics/anthropic-sdk-typescript/issues/344)) ([892127c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/892127c))

### Bug Fixes

* **internal:** make toFile use input file's options ([#343](https://github.com/anthropics/anthropic-sdk-typescript/issues/343)) ([2dc2174](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2dc2174))

### Chores

* **internal:** update generated pragma comment ([#341](https://github.com/anthropics/anthropic-sdk-typescript/issues/341)) ([fd60f63](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fd60f63))

### Documentation

* fix typo in CONTRIBUTING.md ([#340](https://github.com/anthropics/anthropic-sdk-typescript/issues/340)) ([ba9f3fa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ba9f3fa))

## 0.18.0 (2024-03-13)

Full Changelog: [sdk-v0.17.2...sdk-v0.18.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.17.2...sdk-v0.18.0)

### Features

* **api:** add haiku model ([#333](https://github.com/anthropics/anthropic-sdk-typescript/issues/333)) ([11becc6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/11becc6))

### Documentation

* update models in vertex examples ([#331](https://github.com/anthropics/anthropic-sdk-typescript/issues/331)) ([3d139b3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3d139b3))

## 0.17.2 (2024-03-12)

Full Changelog: [sdk-v0.17.1...sdk-v0.17.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.17.1...sdk-v0.17.2)

### Chores

* **internal:** add explicit type annotation to decoder ([#324](https://github.com/anthropics/anthropic-sdk-typescript/issues/324)) ([7e172c7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7e172c7))

## 0.17.1 (2024-03-06)

Full Changelog: [sdk-v0.17.0...sdk-v0.17.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.17.0...sdk-v0.17.1)

### Documentation

* deprecate old access token getter ([#322](https://github.com/anthropics/anthropic-sdk-typescript/issues/322)) ([1110548](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1110548))
* remove extraneous --save and yarn install instructions ([#323](https://github.com/anthropics/anthropic-sdk-typescript/issues/323)) ([775ecb9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/775ecb9))

## 0.17.0 (2024-03-06)

Full Changelog: [sdk-v0.16.1...sdk-v0.17.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.16.1...sdk-v0.17.0)

### Features

* **api:** add enum to model param for message ([#315](https://github.com/anthropics/anthropic-sdk-typescript/issues/315)) ([0c44de0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0c44de0))

### Bug Fixes

* **streaming:** correctly handle trailing new lines in byte chunks ([#317](https://github.com/anthropics/anthropic-sdk-typescript/issues/317)) ([0147b46](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0147b46))

### Chores

* **types:** fix accidental exposure of Buffer type to cloudflare ([#319](https://github.com/anthropics/anthropic-sdk-typescript/issues/319)) ([a5e4462](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a5e4462))

### Documentation

* **readme:** fix https proxy example ([#310](https://github.com/anthropics/anthropic-sdk-typescript/issues/310)) ([99d3c54](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/99d3c54))
* **readme:** fix https proxy example ([#311](https://github.com/anthropics/anthropic-sdk-typescript/issues/311)) ([ffb603c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ffb603c))

## 0.16.1 (2024-03-04)

Full Changelog: [sdk-v0.16.0...sdk-v0.16.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.16.0...sdk-v0.16.1)

### Chores

* fix error handler in readme ([#307](https://github.com/anthropics/anthropic-sdk-typescript/issues/307)) ([5007a1e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5007a1e))

### Documentation

* **readme:** reference bedrock sdk ([#309](https://github.com/anthropics/anthropic-sdk-typescript/issues/309)) ([0fd0416](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0fd0416))

## 0.16.0 (2024-03-04)

Full Changelog: [sdk-v0.15.0...sdk-v0.16.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.15.0...sdk-v0.16.0)

### Features

* **bedrock:** add messages API ([#305](https://github.com/anthropics/anthropic-sdk-typescript/issues/305)) ([8b7f89e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8b7f89e))

### Chores

* update examples ([459956a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/459956a))

## 0.15.0 (2024-03-04)

Full Changelog: [sdk-v0.14.1...sdk-v0.15.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.14.1...sdk-v0.15.0)

### Features

* **messages:** add support for image inputs ([#303](https://github.com/anthropics/anthropic-sdk-typescript/issues/303)) ([7663bd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7663bd6))

### Bug Fixes

* **MessageStream:** handle errors more gracefully in async iterator ([#301](https://github.com/anthropics/anthropic-sdk-typescript/issues/301)) ([9cc0daa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9cc0daa))

### Chores

* **docs:** mention install from git repo ([#302](https://github.com/anthropics/anthropic-sdk-typescript/issues/302)) ([dd2627b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dd2627b))
* **internal:** update deps ([#296](https://github.com/anthropics/anthropic-sdk-typescript/issues/296)) ([8804a92](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8804a92))

### Documentation

* **contributing:** improve wording ([#299](https://github.com/anthropics/anthropic-sdk-typescript/issues/299)) ([7697fa1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7697fa1))
* **readme:** fix typo in custom fetch implementation ([#300](https://github.com/anthropics/anthropic-sdk-typescript/issues/300)) ([a4974c3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a4974c3))

## 0.14.1 (2024-02-22)

Full Changelog: [sdk-v0.14.0...sdk-v0.14.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.14.0...sdk-v0.14.1)

### Chores

* **ci:** update actions/setup-node action to v4 ([#295](https://github.com/anthropics/anthropic-sdk-typescript/issues/295)) ([359a856](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/359a856))
* **docs:** remove references to old bedrock package ([#289](https://github.com/anthropics/anthropic-sdk-typescript/issues/289)) ([33b935e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/33b935e))
* **internal:** refactor release environment script ([#294](https://github.com/anthropics/anthropic-sdk-typescript/issues/294)) ([b7f8714](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b7f8714))

### Documentation

* **readme:** fix header for streaming helpers ([#293](https://github.com/anthropics/anthropic-sdk-typescript/issues/293)) ([7278e6f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7278e6f))

### Refactors

* **api:** mark completions API as legacy ([#291](https://github.com/anthropics/anthropic-sdk-typescript/issues/291)) ([c78e2e2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c78e2e2))

## 0.14.0 (2024-02-13)

Full Changelog: [sdk-v0.13.1...sdk-v0.14.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.13.1...sdk-v0.14.0)

### ⚠ BREAKING CHANGES

* **api:** messages is generally available ([#287](https://github.com/anthropics/anthropic-sdk-typescript/issues/287))

### Features

* **api:** messages is generally available ([#287](https://github.com/anthropics/anthropic-sdk-typescript/issues/287)) ([be0a828](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/be0a828))

## 0.13.1 (2024-02-07)

Full Changelog: [sdk-v0.13.0...sdk-v0.13.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.13.0...sdk-v0.13.1)

### Chores

* **internal:** reformat pacakge.json ([#284](https://github.com/anthropics/anthropic-sdk-typescript/issues/284)) ([3760c68](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3760c68))
* respect `application/vnd.api+json` content-type header ([#286](https://github.com/anthropics/anthropic-sdk-typescript/issues/286)) ([daf0cae](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/daf0cae))

## 0.13.0 (2024-02-02)

Full Changelog: [sdk-v0.12.8...sdk-v0.13.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.8...sdk-v0.13.0)

### Features

* **api:** add new usage response fields ([#281](https://github.com/anthropics/anthropic-sdk-typescript/issues/281)) ([77bd18f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/77bd18f))

### Chores

* **package:** fix formatting ([#283](https://github.com/anthropics/anthropic-sdk-typescript/issues/283)) ([f88579a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f88579a))

## 0.12.8 (2024-02-02)

Full Changelog: [sdk-v0.12.7...sdk-v0.12.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.7...sdk-v0.12.8)

### Chores

* **interal:** make link to api.md relative ([#278](https://github.com/anthropics/anthropic-sdk-typescript/issues/278)) ([46f8c28](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/46f8c28))
* **internal:** enable building when git installed ([#279](https://github.com/anthropics/anthropic-sdk-typescript/issues/279)) ([3065001](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3065001))

### Documentation

* add a CONTRIBUTING.md ([#280](https://github.com/anthropics/anthropic-sdk-typescript/issues/280)) ([5b53551](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5b53551))

## 0.12.7 (2024-01-31)

Full Changelog: [sdk-v0.12.6...sdk-v0.12.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.6...sdk-v0.12.7)

### Chores

* **bedrock:** move bedrock SDK to the main repo ([#274](https://github.com/anthropics/anthropic-sdk-typescript/issues/274)) ([b4ef3a8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b4ef3a8))
* **ci:** fix publish packages script ([#272](https://github.com/anthropics/anthropic-sdk-typescript/issues/272)) ([db3585d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/db3585d))

## 0.12.6 (2024-01-30)

Full Changelog: [sdk-v0.12.5...sdk-v0.12.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.5...sdk-v0.12.6)

### Chores

* **internal:** support pre-release versioning ([#270](https://github.com/anthropics/anthropic-sdk-typescript/issues/270)) ([566069d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/566069d))

## 0.12.5 (2024-01-25)

Full Changelog: [sdk-v0.12.4...sdk-v0.12.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.4...sdk-v0.12.5)

### Chores

* **internal:** don't re-export streaming type ([#267](https://github.com/anthropics/anthropic-sdk-typescript/issues/267)) ([bcae5a9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bcae5a9))
* **internal:** update release-please config ([#269](https://github.com/anthropics/anthropic-sdk-typescript/issues/269)) ([80952e6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/80952e6))

## 0.12.4 (2024-01-23)

Full Changelog: [sdk-v0.12.3...sdk-v0.12.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/sdk-v0.12.3...sdk-v0.12.4)

### Chores

* **internal:** add internal helpers & improve build scripts ([#261](https://github.com/anthropics/anthropic-sdk-typescript/issues/261)) ([4c1504a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c1504a))
* **internal:** minor streaming updates ([#264](https://github.com/anthropics/anthropic-sdk-typescript/issues/264)) ([d4414ff](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d4414ff))
* **internal:** update resource client type ([#263](https://github.com/anthropics/anthropic-sdk-typescript/issues/263)) ([bc4f115](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bc4f115))

## 0.12.3 (2024-01-19)

Full Changelog: [v0.12.2...v0.12.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.12.2...v0.12.3)

### Bug Fixes

* allow body type in RequestOptions to be null ([#259](https://github.com/anthropics/anthropic-sdk-typescript/issues/259)) ([2f98de1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2f98de1))

## 0.12.2 (2024-01-18)

Full Changelog: [v0.12.1...v0.12.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.12.1...v0.12.2)

### Bug Fixes

* **ci:** ignore stainless-app edits to release PR title ([#258](https://github.com/anthropics/anthropic-sdk-typescript/issues/258)) ([87e4ba8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/87e4ba8))
* **types:** accept undefined for optional client options ([#257](https://github.com/anthropics/anthropic-sdk-typescript/issues/257)) ([a0e2c4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a0e2c4a))
* use default base url if BASE_URL env var is blank ([#250](https://github.com/anthropics/anthropic-sdk-typescript/issues/250)) ([e38f32f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e38f32f))

### Chores

* **internal:** debug logging for retries; speculative retry-after-ms support ([#256](https://github.com/anthropics/anthropic-sdk-typescript/issues/256)) ([b4b70fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b4b70fd))
* **internal:** narrow type into stringifyQuery ([#253](https://github.com/anthropics/anthropic-sdk-typescript/issues/253)) ([3f42e07](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3f42e07))

### Documentation

* fix missing async in readme code sample ([#255](https://github.com/anthropics/anthropic-sdk-typescript/issues/255)) ([553fb37](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/553fb37))
* **readme:** improve api reference ([#254](https://github.com/anthropics/anthropic-sdk-typescript/issues/254)) ([3721927](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3721927))

## 0.12.1 (2024-01-08)

Full Changelog: [v0.12.0...v0.12.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.12.0...v0.12.1)

### Bug Fixes

* **headers:** always send lowercase headers and strip undefined (BREAKING in rare cases) ([#245](https://github.com/anthropics/anthropic-sdk-typescript/issues/245)) ([7703066](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7703066))

### Chores

* add .keep files for examples and custom code directories ([#249](https://github.com/anthropics/anthropic-sdk-typescript/issues/249)) ([26b9062](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/26b9062))
* **internal:** improve type signatures ([#247](https://github.com/anthropics/anthropic-sdk-typescript/issues/247)) ([40edd29](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/40edd29))

## 0.12.0 (2023-12-21)

Full Changelog: [v0.11.0...v0.12.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.11.0...v0.12.0)

### ⚠ BREAKING CHANGES

* remove anthropic-beta and x-api-key headers from param types ([#243](https://github.com/anthropics/anthropic-sdk-typescript/issues/243))

### Bug Fixes

* remove anthropic-beta and x-api-key headers from param types ([#243](https://github.com/anthropics/anthropic-sdk-typescript/issues/243)) ([60f67ae](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/60f67ae))

### Documentation

* **readme:** add streaming helper documentation ([#238](https://github.com/anthropics/anthropic-sdk-typescript/issues/238)) ([d74ee71](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d74ee71))
* **readme:** remove old migration guide ([#236](https://github.com/anthropics/anthropic-sdk-typescript/issues/236)) ([65dff0a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/65dff0a))
* reformat README.md ([#241](https://github.com/anthropics/anthropic-sdk-typescript/issues/241)) ([eb12705](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/eb12705))

### Refactors

* write jest config in typescript ([#239](https://github.com/anthropics/anthropic-sdk-typescript/issues/239)) ([7c87f24](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7c87f24))

## 0.11.0 (2023-12-19)

Full Changelog: [v0.10.2...v0.11.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.10.2...v0.11.0)

### Features

* **api:** add messages endpoint with streaming helpers ([#235](https://github.com/anthropics/anthropic-sdk-typescript/issues/235)) ([12b914f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/12b914f))
* **client:** support reading the base url from an env variable ([#223](https://github.com/anthropics/anthropic-sdk-typescript/issues/223)) ([5bc3600](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5bc3600))

### Chores

* **ci:** run release workflow once per day ([#232](https://github.com/anthropics/anthropic-sdk-typescript/issues/232)) ([115479f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/115479f))
* **deps:** update dependency ts-jest to v29.1.1 ([#233](https://github.com/anthropics/anthropic-sdk-typescript/issues/233)) ([bec6ab1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bec6ab1))
* **deps:** update jest ([#234](https://github.com/anthropics/anthropic-sdk-typescript/issues/234)) ([5506174](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5506174))
* update dependencies ([#231](https://github.com/anthropics/anthropic-sdk-typescript/issues/231)) ([4e34536](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4e34536))
* update prettier ([#230](https://github.com/anthropics/anthropic-sdk-typescript/issues/230)) ([173603e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/173603e))

### Documentation

* update examples to show claude-2.1 ([#227](https://github.com/anthropics/anthropic-sdk-typescript/issues/227)) ([4b00d84](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4b00d84))

### Build System

* specify `packageManager: yarn` ([#229](https://github.com/anthropics/anthropic-sdk-typescript/issues/229)) ([d31dae4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d31dae4))

## 0.10.2 (2023-11-28)

Full Changelog: [v0.10.1...v0.10.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.10.1...v0.10.2)

## 0.10.1 (2023-11-24)

Full Changelog: [v0.10.0...v0.10.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.10.0...v0.10.1)

### Chores

* **internal:** remove file import and conditionally run prepare ([#217](https://github.com/anthropics/anthropic-sdk-typescript/issues/217)) ([8ac5c7a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8ac5c7a))

## 0.10.0 (2023-11-21)

Full Changelog: [v0.9.1...v0.10.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.9.1...v0.10.0)

### Features

* allow installing package directly from github ([#215](https://github.com/anthropics/anthropic-sdk-typescript/issues/215)) ([3de3f1b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3de3f1b))

### Chores

* **ci:** fix publish-npm ([#213](https://github.com/anthropics/anthropic-sdk-typescript/issues/213)) ([4ab77b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4ab77b7))
* **internal:** don't call prepare in dist ([#216](https://github.com/anthropics/anthropic-sdk-typescript/issues/216)) ([b031904](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b031904))

## 0.9.1 (2023-11-14)

Full Changelog: [v0.9.0...v0.9.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.9.0...v0.9.1)

### Chores

* **ci:** update release-please config ([#206](https://github.com/anthropics/anthropic-sdk-typescript/issues/206)) ([270b0b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/270b0b7))
* **docs:** fix github links ([#208](https://github.com/anthropics/anthropic-sdk-typescript/issues/208)) ([b316603](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b316603))
* **internal:** update APIResource structure ([#211](https://github.com/anthropics/anthropic-sdk-typescript/issues/211)) ([0d6bbce](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0d6bbce))
* **internal:** update jest config ([#210](https://github.com/anthropics/anthropic-sdk-typescript/issues/210)) ([b0c64eb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b0c64eb))
* **internal:** update tsconfig ([#209](https://github.com/anthropics/anthropic-sdk-typescript/issues/209)) ([81b3e0b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/81b3e0b))

## 0.9.0 (2023-11-05)

Full Changelog: [v0.8.1...v0.9.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.8.1...v0.9.0)

### Features

* **client:** allow binary returns ([#203](https://github.com/anthropics/anthropic-sdk-typescript/issues/203)) ([5983d5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5983d5e))
* **github:** include a devcontainer setup ([#202](https://github.com/anthropics/anthropic-sdk-typescript/issues/202)) ([ea97913](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ea97913))

### Chores

* **internal:** update gitignore ([#198](https://github.com/anthropics/anthropic-sdk-typescript/issues/198)) ([3048738](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3048738))
* small cleanups ([#201](https://github.com/anthropics/anthropic-sdk-typescript/issues/201)) ([9f0a73d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9f0a73d))

### Documentation

* document customizing fetch ([#204](https://github.com/anthropics/anthropic-sdk-typescript/issues/204)) ([d2df724](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d2df724))
* fix github links ([#200](https://github.com/anthropics/anthropic-sdk-typescript/issues/200)) ([4038acd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4038acd))
* **readme:** mention version header ([#205](https://github.com/anthropics/anthropic-sdk-typescript/issues/205)) ([a8d8f07](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a8d8f07))

## 0.8.1 (2023-10-25)

Full Changelog: [v0.8.0...v0.8.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.8.0...v0.8.1)

### Bug Fixes

* typo in build script ([#197](https://github.com/anthropics/anthropic-sdk-typescript/issues/197)) ([212e990](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/212e990))

## 0.8.0 (2023-10-24)

Full Changelog: [v0.7.0...v0.8.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.7.0...v0.8.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#192](https://github.com/anthropics/anthropic-sdk-typescript/issues/192)) ([747afe2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/747afe2))

## 0.7.0 (2023-10-19)

Full Changelog: [v0.6.8...v0.7.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.8...v0.7.0)

### Features

* handle 204 No Content gracefully ([#190](https://github.com/anthropics/anthropic-sdk-typescript/issues/190)) ([c8a8bec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c8a8bec))

## 0.6.8 (2023-10-17)

Full Changelog: [v0.6.7...v0.6.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.7...v0.6.8)

### Bug Fixes

* import web-streams-polyfill without overriding globals ([#186](https://github.com/anthropics/anthropic-sdk-typescript/issues/186)) ([e774e17](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e774e17))

## 0.6.7 (2023-10-16)

Full Changelog: [v0.6.6...v0.6.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.6...v0.6.7)

### Bug Fixes

* improve status code in error messages ([#183](https://github.com/anthropics/anthropic-sdk-typescript/issues/183)) ([7d3bbd4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7d3bbd4))

### Chores

* add case insensitive get header function ([#178](https://github.com/anthropics/anthropic-sdk-typescript/issues/178)) ([13c398d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/13c398d))
* **internal:** add debug logs for stream responses ([#182](https://github.com/anthropics/anthropic-sdk-typescript/issues/182)) ([a1fa1b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a1fa1b7))
* update comment ([#179](https://github.com/anthropics/anthropic-sdk-typescript/issues/179)) ([27a425e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/27a425e))

### Documentation

* organisation -&gt; organization (UK to US English) ([#185](https://github.com/anthropics/anthropic-sdk-typescript/issues/185)) ([70257d4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/70257d4))

### Refactors

* **streaming:** change Stream constructor signature ([#174](https://github.com/anthropics/anthropic-sdk-typescript/issues/174)) ([1951824](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1951824))
* **test:** refactor authentication tests ([#176](https://github.com/anthropics/anthropic-sdk-typescript/issues/176)) ([f59daad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f59daad))

## 0.6.6 (2023-10-11)

Full Changelog: [v0.6.5...v0.6.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.5...v0.6.6)

### Chores

* update README ([#173](https://github.com/anthropics/anthropic-sdk-typescript/issues/173)) ([5f50c1b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5f50c1b))

## 0.6.5 (2023-10-11)

Full Changelog: [v0.6.4...v0.6.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.4...v0.6.5)

### Features

* **client:** handle retry-after with a date ([#162](https://github.com/anthropics/anthropic-sdk-typescript/issues/162)) ([31bd609](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/31bd609))
* **client:** retry on 408 Request Timeout ([#151](https://github.com/anthropics/anthropic-sdk-typescript/issues/151)) ([3523ffe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3523ffe))
* **client:** support importing node or web shims manually ([#157](https://github.com/anthropics/anthropic-sdk-typescript/issues/157)) ([c1237fe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c1237fe))
* **errors:** add status code to error message ([#155](https://github.com/anthropics/anthropic-sdk-typescript/issues/155)) ([76cf128](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/76cf128))
* **package:** export a root error type ([#160](https://github.com/anthropics/anthropic-sdk-typescript/issues/160)) ([51d8d60](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/51d8d60))

### Bug Fixes

* **client:** eliminate circular imports, which cause runtime errors in webpack dev bundles ([#170](https://github.com/anthropics/anthropic-sdk-typescript/issues/170)) ([4a86733](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4a86733))
* fix namespace exports regression ([#171](https://github.com/anthropics/anthropic-sdk-typescript/issues/171)) ([0689a91](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0689a91))
* prevent ReferenceError, update compatibility to ES2020 and Node 18+ ([#169](https://github.com/anthropics/anthropic-sdk-typescript/issues/169)) ([9753314](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9753314))

### Chores

* **internal:** bump lock file ([#159](https://github.com/anthropics/anthropic-sdk-typescript/issues/159)) ([e6030fa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e6030fa))
* **internal:** minor formatting improvement ([#168](https://github.com/anthropics/anthropic-sdk-typescript/issues/168)) ([6447608](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/6447608))
* **internal:** update lock file ([#161](https://github.com/anthropics/anthropic-sdk-typescript/issues/161)) ([370ce3c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/370ce3c))
* **internal:** update lock file ([#163](https://github.com/anthropics/anthropic-sdk-typescript/issues/163)) ([4a37181](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4a37181))
* **internal:** update lock file ([#164](https://github.com/anthropics/anthropic-sdk-typescript/issues/164)) ([939c155](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/939c155))

### Documentation

* **api.md:** add shared models ([#158](https://github.com/anthropics/anthropic-sdk-typescript/issues/158)) ([33e5518](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/33e5518))
* declare Bun 1.0 officially supported ([#154](https://github.com/anthropics/anthropic-sdk-typescript/issues/154)) ([429d8f4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/429d8f4))
* **readme:** remove incorrect wording in opening ([#156](https://github.com/anthropics/anthropic-sdk-typescript/issues/156)) ([01973fe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/01973fe))

## 0.6.4 (2023-09-08)

Full Changelog: [v0.6.3...v0.6.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.3...v0.6.4)

### Features

* **package:** add Bun export map ([#139](https://github.com/anthropics/anthropic-sdk-typescript/issues/139)) ([ba3310d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ba3310d))

### Bug Fixes

* **client:** fix TS errors that appear when users Go to Source in VSCode ([#142](https://github.com/anthropics/anthropic-sdk-typescript/issues/142)) ([f7bfbea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f7bfbea))
* **client:** handle case where the client is instantiated with a undefined baseURL ([#143](https://github.com/anthropics/anthropic-sdk-typescript/issues/143)) ([10e5203](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/10e5203))
* **client:** use explicit file extensions in _shims imports ([#141](https://github.com/anthropics/anthropic-sdk-typescript/issues/141)) ([10fd687](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/10fd687))
* fix module not found errors in Vercel edge ([#148](https://github.com/anthropics/anthropic-sdk-typescript/issues/148)) ([72e51a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/72e51a1))
* **readme:** update link to api.md to use the correct branch ([#145](https://github.com/anthropics/anthropic-sdk-typescript/issues/145)) ([5db78ed](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5db78ed))

### Chores

* **internal:** export helper from core ([#147](https://github.com/anthropics/anthropic-sdk-typescript/issues/147)) ([7e79de1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7e79de1))

### Documentation

* **readme:** add link to api.md ([#144](https://github.com/anthropics/anthropic-sdk-typescript/issues/144)) ([716c9f0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/716c9f0))

## 0.6.3 (2023-08-28)

Full Changelog: [v0.6.2...v0.6.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/v0.6.2...v0.6.3)

### Bug Fixes

* **types:** improve getNextPage() return type ([#137](https://github.com/anthropics/anthropic-sdk-typescript/issues/137)) ([713d603](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/713d603))

### Chores

* **ci:** setup workflows to create releases and release PRs ([#135](https://github.com/anthropics/anthropic-sdk-typescript/issues/135)) ([56229d9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/56229d9))

## [0.6.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.6.2) (2023-08-26)

### Bug Fixes

* **stream:** declare Stream.controller as public ([#132](https://github.com/anthropics/anthropic-sdk-typescript/issues/132)) ([ff33a89](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ff33a89))

### Refactors

* remove unnecessary line in constructor ([#131](https://github.com/anthropics/anthropic-sdk-typescript/issues/131)) ([dcdf5e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/dcdf5e5))

### Chores

* **internal:** add helper method ([#133](https://github.com/anthropics/anthropic-sdk-typescript/issues/133)) ([4c6950a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4c6950a))
* **internal:** export HeadersInit type shim ([#129](https://github.com/anthropics/anthropic-sdk-typescript/issues/129)) ([bcd51bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/bcd51bd))

## [0.6.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.6.1) (2023-08-23)

### Features

* allow a default timeout to be set for clients ([#113](https://github.com/anthropics/anthropic-sdk-typescript/issues/113)) ([1c5b2e2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1c5b2e2))
* **client:** improve compatibility with Bun ([#119](https://github.com/anthropics/anthropic-sdk-typescript/issues/119)) ([fe4f5d5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/fe4f5d5))
* **docs:** add documentation to the client constructor ([#118](https://github.com/anthropics/anthropic-sdk-typescript/issues/118)) ([79303f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/79303f9))
* **types:** export RequestOptions type ([#127](https://github.com/anthropics/anthropic-sdk-typescript/issues/127)) ([9769751](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9769751))
* **types:** remove footgun with streaming params ([#125](https://github.com/anthropics/anthropic-sdk-typescript/issues/125)) ([3ed67b6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3ed67b6))

### Bug Fixes

* **client:** fix TypeError when a request gets retried ([#117](https://github.com/anthropics/anthropic-sdk-typescript/issues/117)) ([0ade979](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0ade979))
* **core:** fix navigator check for strange environments ([#124](https://github.com/anthropics/anthropic-sdk-typescript/issues/124)) ([c783604](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c783604))
* **types:** add catch-all overload to streaming methods ([#123](https://github.com/anthropics/anthropic-sdk-typescript/issues/123)) ([7c229a2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7c229a2))

### Documentation

* **readme:** fix typo ([#121](https://github.com/anthropics/anthropic-sdk-typescript/issues/121)) ([c5dbc3f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c5dbc3f))

### Chores

* assign default reviewers to release PRs ([#115](https://github.com/anthropics/anthropic-sdk-typescript/issues/115)) ([1df3965](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/1df3965))
* **internal:** add missing eslint-plugin-prettier ([#122](https://github.com/anthropics/anthropic-sdk-typescript/issues/122)) ([66bede0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/66bede0))
* **internal:** fix error happening in CloudFlare pages ([#116](https://github.com/anthropics/anthropic-sdk-typescript/issues/116)) ([b0dc7b3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b0dc7b3))
* **internal:** minor reformatting of code ([#120](https://github.com/anthropics/anthropic-sdk-typescript/issues/120)) ([4bcaf9e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4bcaf9e))

## [0.6.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.6.0) (2023-08-12)

### Features

* **client:** add support for accessing the raw response object ([#105](https://github.com/anthropics/anthropic-sdk-typescript/issues/105)) ([c86b059](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c86b059))
* **client:** detect browser usage ([#101](https://github.com/anthropics/anthropic-sdk-typescript/issues/101)) ([f4cae3f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f4cae3f))
* **types:** improve streaming params types ([#102](https://github.com/anthropics/anthropic-sdk-typescript/issues/102)) ([cdf808c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/cdf808c))

### Documentation

* **readme:** minor updates ([#107](https://github.com/anthropics/anthropic-sdk-typescript/issues/107)) ([406fd97](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/406fd97))
* **readme:** remove beta status + document versioning policy ([#100](https://github.com/anthropics/anthropic-sdk-typescript/issues/100)) ([e9ef3d2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/e9ef3d2))

### Chores

* **docs:** remove trailing spaces ([#108](https://github.com/anthropics/anthropic-sdk-typescript/issues/108)) ([4ba2c6f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/4ba2c6f))
* **internal:** conditionally include bin during build output ([#109](https://github.com/anthropics/anthropic-sdk-typescript/issues/109)) ([58ac305](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/58ac305))
* **internal:** fix deno build ([#98](https://github.com/anthropics/anthropic-sdk-typescript/issues/98)) ([f011e04](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f011e04))
* **internal:** remove deno build ([#103](https://github.com/anthropics/anthropic-sdk-typescript/issues/103)) ([9af1527](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9af1527))

### Refactors

* **client:** remove Stream.toReadableStream() ([#110](https://github.com/anthropics/anthropic-sdk-typescript/issues/110)) ([c370412](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/c370412))

## [0.5.10](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.10) (2023-08-01)

### Refactors

* create build for deno.land ([#93](https://github.com/anthropics/anthropic-sdk-typescript/issues/93)) ([2ea741a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2ea741a))

### Documentation

* **readme:** add token counting reference ([#94](https://github.com/anthropics/anthropic-sdk-typescript/issues/94)) ([2c6a699](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c6a699))

### Chores

* **internal:** allow the build script to be run without yarn installed ([#91](https://github.com/anthropics/anthropic-sdk-typescript/issues/91)) ([9bd2b28](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/9bd2b28))
* **internal:** fix deno build ([#96](https://github.com/anthropics/anthropic-sdk-typescript/issues/96)) ([3fdab4e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/3fdab4e))

## [0.5.9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.9) (2023-07-29)

### Bug Fixes

* **client:** handle undefined process in more places ([#87](https://github.com/anthropics/anthropic-sdk-typescript/issues/87)) ([d950c25](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/d950c25))
* **examples:** avoid swallowing errors in example scripts ([#82](https://github.com/anthropics/anthropic-sdk-typescript/issues/82)) ([b27cfe9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/b27cfe9))
* fix undefined message in errors ([#86](https://github.com/anthropics/anthropic-sdk-typescript/issues/86)) ([5714a14](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5714a14))

### Chores

* **internal:** minor refactoring of client instantiation ([#88](https://github.com/anthropics/anthropic-sdk-typescript/issues/88)) ([2c53e1c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/2c53e1c))

### Refactors

* use destructuring arguments in client constructor and respect false values ([#89](https://github.com/anthropics/anthropic-sdk-typescript/issues/89)) ([8d4c686](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8d4c686))

## [0.5.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.8) (2023-07-22)

### Features

* **streaming:** make requests immediately throw an error if an aborted signal is passed in ([#79](https://github.com/anthropics/anthropic-sdk-typescript/issues/79)) ([5c86597](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5c86597))

## [0.5.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.7) (2023-07-19)

### Features

* add flexible enum to model param ([#73](https://github.com/anthropics/anthropic-sdk-typescript/issues/73)) ([a6bbcad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/a6bbcad))
* **client:** export ClientOptions interface ([#75](https://github.com/anthropics/anthropic-sdk-typescript/issues/75)) ([0315ce1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0315ce1))
* **deps:** remove unneeded qs dep ([#72](https://github.com/anthropics/anthropic-sdk-typescript/issues/72)) ([0aea5a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0aea5a6))

### Bug Fixes

* **client:** fix errors with file uploads in the browser ([#76](https://github.com/anthropics/anthropic-sdk-typescript/issues/76)) ([ac48fa7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/ac48fa7))
* fix error in environments without `TextEncoder` ([#70](https://github.com/anthropics/anthropic-sdk-typescript/issues/70)) ([5b78e05](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/5b78e05))
* fix export map order ([#74](https://github.com/anthropics/anthropic-sdk-typescript/issues/74)) ([51e70cb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/51e70cb))

## [0.5.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.6) (2023-07-15)

### Bug Fixes

* fix errors with "named" client export in CJS ([#67](https://github.com/anthropics/anthropic-sdk-typescript/issues/67)) ([08ef69c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/08ef69c))

## [0.5.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.5) (2023-07-13)

### Features

* **client:** add support for passing a `signal` request option ([#55](https://github.com/anthropics/anthropic-sdk-typescript/issues/55)) ([09604e9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/09604e9))

### Bug Fixes

* **streaming:** do not abort successfully completed streams ([#53](https://github.com/anthropics/anthropic-sdk-typescript/issues/53)) ([950dd49](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/950dd49))

### Documentation

* **examples:** bump model to claude-2 in example scripts ([#57](https://github.com/anthropics/anthropic-sdk-typescript/issues/57)) ([f85c05d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/f85c05d))
* **readme:** improvements to formatting code snippets ([#58](https://github.com/anthropics/anthropic-sdk-typescript/issues/58)) ([67bae64](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/67bae64))

### Chores

* **internal:** add helper function for b64 ([#62](https://github.com/anthropics/anthropic-sdk-typescript/issues/62)) ([04e303c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/04e303c))
* **internal:** let `toFile` helper accept promises to objects with name/type properties ([#63](https://github.com/anthropics/anthropic-sdk-typescript/issues/63)) ([93f9af2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/93f9af2))
* **internal:** remove unneeded type var usage ([#59](https://github.com/anthropics/anthropic-sdk-typescript/issues/59)) ([42fc4a9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/42fc4a9))

## [0.5.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/0.5.4) (2023-07-11)

### Features

* **api:** reference claude-2 in examples ([#50](https://github.com/anthropics/anthropic-sdk-typescript/issues/50)) ([7c53ded](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7c53ded))
* **client:** support passing a custom `fetch` function ([#46](https://github.com/anthropics/anthropic-sdk-typescript/issues/46)) ([7d54366](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/7d54366))

### Bug Fixes

* **client:** properly handle multi-byte characters in Content-Length ([#47](https://github.com/anthropics/anthropic-sdk-typescript/issues/47)) ([8dfff26](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/8dfff26))

### Refactors

* **streaming:** make response body streaming polyfill more spec-compliant ([#44](https://github.com/anthropics/anthropic-sdk-typescript/issues/44)) ([047d328](https://raw.githubusercontent.com/anthropics/anthropic-sdk-typescript/main/047d328))
