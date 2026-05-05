# Changelog

## 0.97.0 (2026-04-23)

Full Changelog: [v0.96.0...v0.97.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.96.0...v0.97.0)

### Features

* **api:** CMA Memory public beta ([fc30ebe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fc30ebe))

### Bug Fixes

* **api:** fix errors in api spec ([f946de8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f946de8))
* **api:** restore missing features ([72212ab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72212ab))

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([1f9eed3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1f9eed3))

### Chores

* add missing import ([4b12f5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4b12f5e))
* **internal:** more robust bootstrap script ([7ed7370](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7ed7370))
* **tests:** bump steady to v0.22.1 ([a4b7184](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a4b7184))

## 0.96.0 (2026-04-16)

Full Changelog: [v0.95.0...v0.96.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.95.0...v0.96.0)

### Features

* **api:** add claude-opus-4-7, token budgets and user_profiles ([0aa2a0d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0aa2a0d))

### Chores

* **ci:** remove release-doctor workflow ([1d9add3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1d9add3))

## 0.95.0 (2026-04-14)

Full Changelog: [v0.94.1...v0.95.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.94.1...v0.95.0)

### Features

* **api:** mark Sonnet and Opus 4 as deprecated ([0c1e773](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0c1e773))
* **bedrock:** use auth header for mantle client ([#1644](https://github.com/anthropics/anthropic-sdk-python/issues/1644)) ([3b93090](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3b93090))

## 0.94.1 (2026-04-13)

Full Changelog: [v0.94.0...v0.94.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.94.0...v0.94.1)

### Bug Fixes

* **streaming:** add missing events ([c6a06d8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c6a06d8))

## 0.94.0 (2026-04-10)

Full Changelog: [v0.93.0...v0.94.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.93.0...v0.94.0)

### Features

* vertex eu region ([#1658](https://github.com/anthropics/anthropic-sdk-python/issues/1658)) ([b7e157d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b7e157d))

### Bug Fixes

* ensure file data are only sent as 1 parameter ([837b25b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/837b25b))

### Documentation

* improve examples ([48089fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/48089fd))
* update examples ([0f3c28b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0f3c28b))

## 0.93.0 (2026-04-09)

Full Changelog: [v0.92.0...v0.93.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.92.0...v0.93.0)

### Features

* **api:** Add beta advisor tool ([4297dca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4297dca))

## 0.92.0 (2026-04-08)

Full Changelog: [v0.91.0...v0.92.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.91.0...v0.92.0)

### Features

* **api:** add support for Claude Managed Agents ([5b879a7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5b879a7))

## 0.91.0 (2026-04-07)

Full Changelog: [v0.90.0...v0.91.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.90.0...v0.91.0)

### Features

* **client:** Create Bedrock Mantle client ([#1616](https://github.com/anthropics/anthropic-sdk-python/issues/1616)) ([fd195a2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fd195a2))

## 0.90.0 (2026-04-07)

Full Changelog: [v0.89.0...v0.90.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.89.0...v0.90.0)

### Features

* **api:** Add support for claude-mythos-preview ([fc7ddd8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fc7ddd8))

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([32d35e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/32d35e0))

## 0.89.0 (2026-04-03)

Full Changelog: [v0.88.0...v0.89.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.88.0...v0.89.0)

### Features

* **vertex:** add support for US multi-region endpoint ([4e732da](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4e732da))

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([e7f4a3c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e7f4a3c))

### Chores

* **client:** deprecate client-side compaction helpers ([e60affc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e60affc))

## 0.88.0 (2026-04-01)

Full Changelog: [v0.87.0...v0.88.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.87.0...v0.88.0)

### Features

* **api:** add structured stop_details to message responses ([fd82d6b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fd82d6b))
* bedrock api key auth ([#1623](https://github.com/anthropics/anthropic-sdk-python/issues/1623)) ([a95a3fc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a95a3fc))
* prepare aws package ([#1615](https://github.com/anthropics/anthropic-sdk-python/issues/1615)) ([6875fab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6875fab))

### Chores

* **tests:** bump steady to v0.20.2 ([1bc4e9f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1bc4e9f))

## 0.87.0 (2026-03-31)

Full Changelog: [v0.86.0...v0.87.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.86.0...v0.87.0)

### Features

* **client:** add error type field to APIStatusError ([#1587](https://github.com/anthropics/anthropic-sdk-python/issues/1587)) ([dd563c0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dd563c0))
* **internal:** implement indices array format for query and form serialization ([11a6244](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/11a6244))

### Bug Fixes

* honor __api_exclude__ in async transform path ([#1612](https://github.com/anthropics/anthropic-sdk-python/issues/1612)) ([8172232](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8172232)), closes [#1610](https://github.com/anthropics/anthropic-sdk-python/issues/1610)
* **memory:** return resolved path from async _validate_path ([7b0add3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7b0add3))
* **memory:** use restrictive file mode for memory files ([47ba5b8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/47ba5b8))
* sanitize endpoint path params ([98f60e4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/98f60e4))
* **transform schema:** support enums ([#1275](https://github.com/anthropics/anthropic-sdk-python/issues/1275)) ([5c088ab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5c088ab))

### Chores

* **ci:** run builds on CI even if only spec metadata changed ([194c050](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/194c050))
* **ci:** skip lint on metadata-only changes ([03e2ab9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/03e2ab9))
* **internal:** update gitignore ([94ede14](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/94ede14))
* **tests:** bump steady to v0.19.4 ([2d6d58f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2d6d58f))
* **tests:** bump steady to v0.19.5 ([8fb439a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8fb439a))
* **tests:** bump steady to v0.19.6 ([76da5fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/76da5fd))
* **tests:** bump steady to v0.19.7 ([bfa40e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bfa40e5))
* **tests:** bump steady to v0.20.1 ([4fd9446](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4fd9446))

## 0.86.0 (2026-03-18)

Full Changelog: [v0.85.0...v0.86.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.85.0...v0.86.0)

### Features

* add support for filesystem memory tools ([#1247](https://github.com/anthropics/anthropic-sdk-python/issues/1247)) ([235d218](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/235d218))
* **api:** manual updates ([86dbe4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/86dbe4a))
* **api:** manual updates ([45d9cc0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/45d9cc0))

### Bug Fixes

* AsyncAnthropic._make_status_error missing 529 and 413 cases ([#1244](https://github.com/anthropics/anthropic-sdk-python/issues/1244)) ([05220bc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/05220bc))
* **deps:** bump minimum typing-extensions version ([09ab112](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/09ab112))
* **pydantic:** do not pass `by_alias` unless set ([b17480e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b17480e))

### Chores

* **internal:** tweak CI branches ([3c0308c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3c0308c))

## 0.85.0 (2026-03-16)

Full Changelog: [v0.84.0...v0.85.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.84.0...v0.85.0)

### Features

* **api:** chore(config): clean up model enum list ([#31](https://github.com/anthropics/anthropic-sdk-python/issues/31)) ([cce1a5b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cce1a5b))
* **api:** GA thinking-display-setting ([207340c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/207340c))
* **tests:** update mock server ([7dc86a4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7dc86a4))

### Bug Fixes

* **client:** add missing 413 and 529 error handlers to async client ([#1554](https://github.com/anthropics/anthropic-sdk-python/issues/1554)) ([9c2986f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9c2986f))
* **tool runner:** propagate container_id for programmatic tool calling ([#1462](https://github.com/anthropics/anthropic-sdk-python/issues/1462)) ([3ae7ff6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3ae7ff6))
* **tools:** use filtered messages list in async compaction ([#1124](https://github.com/anthropics/anthropic-sdk-python/issues/1124)) ([710d666](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/710d666))

### Chores

* **ci:** bump uv version ([09656ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/09656ac))
* **internal:** codegen related update ([c9e9fc2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c9e9fc2))
* **internal:** codegen related update ([77f77d1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/77f77d1))
* **tests:** unskip tests that are now supported in steady ([827330b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/827330b))

## 0.84.0 (2026-02-25)

Full Changelog: [v0.83.0...v0.84.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.83.0...v0.84.0)

### Features

* **api:** change array_format to brackets ([925d2ad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/925d2ad))
* **api:** remove publishing section from cli target ([7bc7ceb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7bc7ceb))
* **helpers:** add conversion helpers for MCP tools, prompts, and resources ([#1383](https://github.com/anthropics/anthropic-sdk-python/issues/1383)) ([9489751](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9489751))

### Chores

* add missing raw jsonl results method ([1009d4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1009d4a))
* **internal:** add request options to SSE classes ([4f4bc8e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4f4bc8e))
* **internal:** make `test_proxy_environment_variables` more resilient ([f7056e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f7056e0))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([143efcc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/143efcc))
* **internal:** simplify http snapshots ([#1092](https://github.com/anthropics/anthropic-sdk-python/issues/1092)) ([4a4dc9f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4a4dc9f))
* **internal:** update jsonl tests ([a8e6a6e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a8e6a6e))

### Documentation

* rebrand to Claude SDK and streamline README ([6b54405](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6b54405))

## 0.83.0 (2026-02-19)

Full Changelog: [v0.82.0...v0.83.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.82.0...v0.83.0)

### Features

* **api:** Add top-level cache control (automatic caching) ([a940123](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a940123))

### Chores

* update mock server docs ([34ef48c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/34ef48c))

## 0.82.0 (2026-02-18)

Full Changelog: [v0.81.0...v0.82.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.81.0...v0.82.0)

### Features

* **api:** fix shared UserLocation and error code types ([da3b931](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/da3b931))

### Bug Fixes

* add backward-compat aliases for removed nested UserLocation classes ([#1409](https://github.com/anthropics/anthropic-sdk-python/issues/1409)) ([56db1e3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/56db1e3))

## 0.81.0 (2026-02-18)

Full Changelog: [v0.80.0...v0.81.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.80.0...v0.81.0)

### Features

* **api:** manual updates ([0a385c2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0a385c2))

## 0.80.0 (2026-02-17)

Full Changelog: [v0.79.0...v0.80.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.79.0...v0.80.0)

### Features

* **api:** Releasing claude-sonnet-4-6 ([d518d6e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d518d6e))

### Bug Fixes

* **api:** fix spec errors ([1413a76](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1413a76))
* remove speed from ga messages ([#1402](https://github.com/anthropics/anthropic-sdk-python/issues/1402)) ([f6ce67c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f6ce67c))

### Chores

* format all `api.md` files ([28a0eb5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/28a0eb5))
* **internal:** bump dependencies ([99f3014](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/99f3014))
* **internal:** fix lint error on Python 3.14 ([a90d71b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a90d71b))

### Refactors

* **vertex:** remove redundant isinstance check in `load_auth` ([#1387](https://github.com/anthropics/anthropic-sdk-python/issues/1387)) ([6b7a7dc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6b7a7dc))

## 0.79.0 (2026-02-07)

Full Changelog: [v0.78.0...v0.79.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.78.0...v0.79.0)

### Features

* **api:** enabling fast-mode in claude-opus-4-6 ([5953ba7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5953ba7))

### Bug Fixes

* pass speed parameter through in sync beta count_tokens ([1dd6119](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1dd6119))

## 0.78.0 (2026-02-05)

Full Changelog: [v0.77.1...v0.78.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.77.1...v0.78.0)

### Features

* **api:** Release Claude Opus 4.6, adaptive thinking, and other features ([3ef1529](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3ef1529))

## 0.77.1 (2026-02-03)

Full Changelog: [v0.77.0...v0.77.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.77.0...v0.77.1)

### Bug Fixes

* **structured outputs:** send structured output beta header when format is omitted ([#1158](https://github.com/anthropics/anthropic-sdk-python/issues/1158)) ([258494e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/258494e))

### Chores

* remove claude-code-review workflow ([#1338](https://github.com/anthropics/anthropic-sdk-python/issues/1338)) ([aec4512](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aec4512))

## 0.77.0 (2026-01-29)

Full Changelog: [v0.76.0...v0.77.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.76.0...v0.77.0)

### Features

* **api:** add support for Structured Outputs in the Messages API ([ad56677](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ad56677))
* **api:** migrate sending message format in output_config rather than output_format ([af405e4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/af405e4))
* **client:** add custom JSON encoder for extended type support ([7780e90](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7780e90))
* use output_config for structured outputs ([82d669d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/82d669d))

### Bug Fixes

* **client:** run formatter ([2e4ff86](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2e4ff86))
* remove class causing breaking change ([#1333](https://github.com/anthropics/anthropic-sdk-python/issues/1333)) ([81ee953](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/81ee953))
* **structured outputs:** avoid including beta header if `output_format` is missing ([#1121](https://github.com/anthropics/anthropic-sdk-python/issues/1121)) ([062077e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/062077e))

### Chores

* **ci:** upgrade `actions/github-script` ([34df616](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/34df616))
* **internal:** update `actions/checkout` version ([ea50de9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ea50de9))

## 0.76.0 (2026-01-13)

Full Changelog: [v0.75.0...v0.76.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.75.0...v0.76.0)

### Features

* allow raw JSON schema to be passed to messages.stream() ([955c61d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/955c61d))
* **client:** add support for binary request streaming ([5302f27](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5302f27))
* **tool runner:** add support for server-side tools ([#1086](https://github.com/anthropics/anthropic-sdk-python/issues/1086)) ([1521316](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1521316))

### Bug Fixes

* **client:** loosen auth header validation ([5a0b89b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5a0b89b))
* ensure streams are always closed ([388bd0c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/388bd0c))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([ede3242](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ede3242))
* use async_to_httpx_files in patch method ([718fa8e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/718fa8e))

### Chores

* add missing docstrings ([d306605](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d306605))
* bump required `uv` version ([90634f3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/90634f3))
* **ci:** Add Claude Code GitHub Workflow ([#1293](https://github.com/anthropics/anthropic-sdk-python/issues/1293)) ([83d1c4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/83d1c4a))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([21c6374](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/21c6374))
* **docs:** use environment variables for authentication in code snippets ([87aa378](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/87aa378))
* fix docstring ([51fca79](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/51fca79))
* **internal:** add `--fix` argument to lint script ([8914b7a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8914b7a))
* **internal:** add missing files argument to base client ([6285abc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6285abc))
* **internal:** avoid using unstable Python versions in tests ([4547171](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4547171))
* update lockfile ([d7ae1fc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d7ae1fc))
* update uv.lock ([746ac05](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/746ac05))

## 0.75.0 (2025-11-24)

Full Changelog: [v0.74.1...v0.75.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.74.1...v0.75.0)

### Features

* **api:** adds support for Claude Opus 4.5, Effort, Advance Tool Use Features, Autocompaction, and Computer Use v5 ([5c3e633](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5c3e633))

### Bug Fixes

* **internal:** small fixes ([36c82f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/36c82f7))

### Chores

* fix lint issues ([4f1fd54](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4f1fd54))

## 0.74.1 (2025-11-19)

Full Changelog: [v0.74.0...v0.74.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.74.0...v0.74.1)

### Bug Fixes

* **structured outputs:** use correct beta header ([e90d347](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e90d347))

### Chores

* **examples:** update model references ([e09461d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e09461d))

## 0.74.0 (2025-11-18)

Full Changelog: [v0.73.0...v0.74.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.73.0...v0.74.0)

### Features

* add Foundry SDK ([3ae9e45](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3ae9e45))

### Bug Fixes

* **examples/memory:** properly add assistant_content to messages ([#1049](https://github.com/anthropics/anthropic-sdk-python/issues/1049)) ([9c7141b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9c7141b))
* use posix paths in file collection for cross-platform compatibility ([d9c6f40](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d9c6f40)), closes [#1051](https://github.com/anthropics/anthropic-sdk-python/issues/1051)

### Chores

* **internal:** remove unnecessary wrapper around external snapshots ([19eceac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/19eceac))

### Documentation

* explain snapshot update process ([#1040](https://github.com/anthropics/anthropic-sdk-python/issues/1040)) ([b61fd87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b61fd87))

## 0.73.0 (2025-11-14)

Full Changelog: [v0.72.1...v0.73.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.72.1...v0.73.0)

### Features

* **api:** add support for structured outputs beta ([688da81](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/688da81))

## 0.72.1 (2025-11-11)

Full Changelog: [v0.72.0...v0.72.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.72.0...v0.72.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([109b771](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/109b771))
* compat with Python 3.14 ([bd2a137](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bd2a137))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([540f0f8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/540f0f8))

### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([72767ce](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72767ce))
* **internal:** grammar fix (it's -&gt; its) ([9efe993](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9efe993))
* **package:** drop Python 3.8 support ([e9af5d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e9af5d3))

## 0.72.0 (2025-10-28)

Full Changelog: [v0.71.1...v0.72.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.71.1...v0.72.0)

### Features

* **api:** add ability to clear thinking in context management ([27c8f17](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/27c8f17))

## 0.71.1 (2025-10-28)

Full Changelog: [v0.71.0...v0.71.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.71.0...v0.71.1)

### Bug Fixes

* **client:** resolve non-functional default socket options ([4606137](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4606137))

### Chores

* **api:** mark older sonnet models as deprecated ([7906595](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7906595))
* bump `httpx-aiohttp` version to 0.1.9 ([5d27492](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5d27492))

## 0.71.0 (2025-10-16)

Full Changelog: [v0.70.0...v0.71.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.70.0...v0.71.0)

### Features

* **api:** adding support for agent skills ([51a606f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/51a606f))

## 0.70.0 (2025-10-15)

Full Changelog: [v0.69.0...v0.70.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.69.0...v0.70.0)

### Features

* **api:** manual updates ([39e62ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/39e62ac))

### Chores

* **client:** add context-management-2025-06-27 beta header ([36dd334](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/36dd334))
* **client:** add model-context-window-exceeded-2025-08-26 beta header ([2cbdb0f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2cbdb0f))
* **internal:** detect missing future annotations with ruff ([b2a2b05](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b2a2b05))

## 0.69.0 (2025-09-29)

Full Changelog: [v0.68.2...v0.69.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.68.2...v0.69.0)

### Features

* **api:** adds support for Claude Sonnet 4.5 and context management features ([f93eb12](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f93eb12))

## 0.68.2 (2025-09-29)

Full Changelog: [v0.68.1...v0.68.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.68.1...v0.68.2)

### Bug Fixes

* do not set headers with default to omit ([95b14ab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/95b14ab))

## 0.68.1 (2025-09-26)

Full Changelog: [v0.68.0...v0.68.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.68.0...v0.68.1)

### Chores

* **deps:** move deprecated `dev-dependencies` in `pyproject.toml` to dev group ([df16b88](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/df16b88))
* do not install brew dependencies in ./scripts/bootstrap by default ([a457673](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a457673))
* rename tool runner helper header ([a9ed3f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a9ed3f9))
* **types:** change optional parameter type from NotGiven to Omit ([9f0a11f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9f0a11f))
* update more NotGiven usage sites ([72ab661](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72ab661))

## 0.68.0 (2025-09-17)

Full Changelog: [v0.67.0...v0.68.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.67.0...v0.68.0)

### Features

* add tool running helpers ([d9c9ce6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d9c9ce6))

### Chores

* **internal:** fix tests ([9858c79](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9858c79))
* **internal:** update pydantic dependency ([f59c2f1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f59c2f1))
* **tests:** simplify `get_platform` test ([7596748](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7596748))

## 0.67.0 (2025-09-10)

Full Changelog: [v0.66.0...v0.67.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.66.0...v0.67.0)

### Features

* **api:** adds support for web_fetch_20250910 tool ([f85b6a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f85b6a1))
* improve future compat with pydantic v3 ([39f28c5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/39f28c5))

### Bug Fixes

* more updates for future pydantic v3 compat ([7967d15](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7967d15))
* **types/beta:** add response content block type to params ([#1030](https://github.com/anthropics/anthropic-sdk-python/issues/1030)) ([9febe38](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9febe38))

### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([c5347b6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c5347b6))
* update SDK settings ([36e6870](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/36e6870))

## 0.66.0 (2025-09-03)

Full Changelog: [v0.65.0...v0.66.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.65.0...v0.66.0)

### Features

* **api:** adds support for Documents in tool results ([5309dad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5309dad))

## 0.65.0 (2025-09-02)

Full Changelog: [v0.64.0...v0.65.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.64.0...v0.65.0)

### Features

* **client:** adds support for code-execution-2025-08-26 tool ([fe92af0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fe92af0))
* **types:** replace List[str] with SequenceNotStr in params ([f542b54](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f542b54))

### Bug Fixes

* avoid newer type syntax ([c6d1cf5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c6d1cf5))
* **client:** remove unused import ([712c6d8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/712c6d8))

### Chores

* **client:** sync SequenceNotStr over to custom stream methods ([dd16483](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dd16483))
* **internal:** add Sequence related utils ([d523f29](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d523f29))
* **internal:** bump uv version ([aab5bc6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aab5bc6))
* **internal:** change ci workflow machines ([5383431](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5383431))
* **internal:** codegen related update ([eb8b19f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/eb8b19f))
* **internal:** improve breaking change detection ([6c8afa9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6c8afa9))
* **internal:** refactor pydantic v1 test setup ([cb5444b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cb5444b))
* **internal:** run tests in an isolated environment ([9adb089](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9adb089))
* **internal:** update pyright exclude list ([85961ef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/85961ef))
* update github action ([1e6a135](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1e6a135))

## 0.64.0 (2025-08-13)

Full Changelog: [v0.63.0...v0.64.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.63.0...v0.64.0)

### Features

* **api:** makes 1 hour TTL Cache Control generally available ([35201ba](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/35201ba))

### Chores

* deprecate older claude-3-5 sonnet models ([#1116](https://github.com/anthropics/anthropic-sdk-python/issues/1116)) ([3e8e10d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3e8e10d))

## 0.63.0 (2025-08-12)

Full Changelog: [v0.62.0...v0.63.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.62.0...v0.63.0)

### Features

* **betas:** add context-1m-2025-08-07 ([57a80e7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/57a80e7))

### Chores

* **internal:** detect breaking changes when removing endpoints ([5c62d7b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5c62d7b))
* **internal:** update comment in script ([9e9d69c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9e9d69c))
* **internal:** update test skipping reason ([b18a3d5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b18a3d5))
* update @stainless-api/prism-cli to v5.15.0 ([55cb0a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/55cb0a1))

## 0.62.0 (2025-08-08)

Full Changelog: [v0.61.0...v0.62.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.61.0...v0.62.0)

### Features

* **api:** search result content blocks ([1ae15cd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1ae15cd))

## 0.61.0 (2025-08-05)

Full Changelog: [v0.60.0...v0.61.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.60.0...v0.61.0)

### Features

* **api:** add claude-opus-4-1-20250805 ([baae0ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/baae0ee))
* **api:** adds support for text_editor_20250728 tool ([9ad8fe5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9ad8fe5))
* **client:** support file upload requests ([a9bd98a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a9bd98a))

### Chores

* **client:** add TextEditor_20250429 tool ([ec207c5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ec207c5))
* **internal:** codegen related update ([4498057](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4498057))
* **internal:** fix ruff target version ([3cfa202](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3cfa202))

## 0.60.0 (2025-07-28)

Full Changelog: [v0.59.0...v0.60.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.59.0...v0.60.0)

### Features

* update streaming error message to say 'required' not 'recommended' ([57120c8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/57120c8))
* update streaming error message to say 'required' not 'recommended' ([3b47368](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3b47368))

### Bug Fixes

* **vertex:** add missing beta methods ([#1004](https://github.com/anthropics/anthropic-sdk-python/issues/1004)) ([f8e9cb4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f8e9cb4))

### Chores

* **project:** add settings file for vscode ([1c4a9b1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1c4a9b1))

## 0.59.0 (2025-07-23)

Full Changelog: [v0.58.2...v0.59.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.58.2...v0.59.0)

### Features

* **api:** removed older deprecated models ([38998fd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/38998fd))

### Bug Fixes

* **parsing:** ignore empty metadata ([7099f32](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7099f32))
* **parsing:** parse extra field types ([dbea8a4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dbea8a4))

### Chores

* **internal:** version bump ([5defffa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5defffa))

## 0.58.2 (2025-07-18)

Full Changelog: [v0.58.1...v0.58.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.58.1...v0.58.2)

### Chores

* **internal:** version bump ([cd5d1ad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cd5d1ad))

## 0.58.1 (2025-07-18)

Full Changelog: [v0.58.0...v0.58.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.58.0...v0.58.1)

### Chores

* **internal:** version bump ([31c3b38](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/31c3b38))

## 0.58.0 (2025-07-18)

Full Changelog: [v0.57.1...v0.58.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.57.1...v0.58.0)

### Features

* clean up environment call outs ([4f64e9c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4f64e9c))

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([727268f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/727268f))
* **parsing:** correctly handle nested discriminated unions ([44dd47e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/44dd47e))

### Chores

* **internal:** bump pinned h11 dep ([9a947e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9a947e1))
* **internal:** codegen related update ([33f2b34](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/33f2b34))
* **internal:** version bump ([5f0f5ad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5f0f5ad))
* **package:** mark python 3.13 as supported ([703d557](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/703d557))
* **readme:** fix version rendering on pypi ([dd956a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dd956a6))

### Documentation

* model in examples ([89b6925](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/89b6925))
* model in examples ([1eccecb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1eccecb))

## 0.57.1 (2025-07-03)

Full Changelog: [v0.57.0...v0.57.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.57.0...v0.57.1)

### Chores

* **api:** update BetaCitationSearchResultLocation ([e0735b4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e0735b4))
* **internal:** version bump ([d368831](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d368831))

## 0.57.0 (2025-07-03)

Full Changelog: [v0.56.0...v0.57.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.56.0...v0.57.0)

### Features

* **api:** add support for Search Result Content Blocks ([4896178](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4896178))

### Bug Fixes

* improve timeout/network error message to be more helpful ([347fb57](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/347fb57))

### Chores

* **ci:** change upload type ([4dc4178](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4dc4178))
* **internal:** version bump ([363629c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/363629c))
* **stream:** improve get_final_text() error message ([#979](https://github.com/anthropics/anthropic-sdk-python/issues/979)) ([5ae0a33](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5ae0a33))

### Documentation

* fix vertex id ([f7392c7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f7392c7))
* fix vertex id ([92fe132](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/92fe132))
* update model in readme ([1a4df78](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1a4df78))
* update models and non-beta ([a54e65c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a54e65c))
* update more models ([9e3dd6a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9e3dd6a))

## 0.56.0 (2025-07-01)

Full Changelog: [v0.55.0...v0.56.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.55.0...v0.56.0)

### Features

* **bedrock:** automatically infer AWS Region ([#974](https://github.com/anthropics/anthropic-sdk-python/issues/974)) ([f648e09](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f648e09))
* **vertex:** support global region endpoint ([1fd1adf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1fd1adf))

### Bug Fixes

* **ci:** correct conditional ([18e625a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/18e625a))
* **ci:** release-doctor — report correct token name ([c91f50d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c91f50d))
* **tests:** avoid deprecation warnings ([71b432f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/71b432f))

### Chores

* **ci:** only run for pushes and fork pull requests ([447b793](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/447b793))
* **internal:** add breaking change detection ([e6d0eca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e6d0eca))
* **internal:** codegen related update ([f88517b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f88517b))
* **internal:** codegen related update ([a385cb9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a385cb9))
* **internal:** codegen related update ([9d4b537](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9d4b537))
* **internal:** codegen related update ([6a3a6fe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6a3a6fe))
* **internal:** codegen related update ([28704a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/28704a6))
* **tests:** run tests with min and max supported Python versions by default ([0ad8534](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0ad8534))
* **tests:** skip some failing tests on the latest python versions ([f63a2d2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f63a2d2))

## 0.55.0 (2025-06-23)

Full Changelog: [v0.54.0...v0.55.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.54.0...v0.55.0)

### Features

* **api:** api update ([4b2134e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4b2134e))
* **api:** api update ([2093bff](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2093bff))
* **api:** manual updates ([c80fda8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c80fda8))
* **client:** add support for aiohttp ([3b03295](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3b03295))

### Bug Fixes

* **client:** correctly parse binary response | stream ([d93817d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d93817d))
* **internal:** revert unintentional changes ([bb3beab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bb3beab))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([ee69d74](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ee69d74))
* **tests:** suppress warnings in tests when running on the latest Python versions ([#982](https://github.com/anthropics/anthropic-sdk-python/issues/982)) ([740da21](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/740da21))

### Chores

* **ci:** enable for pull requests ([08f2dd2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/08f2dd2))
* **internal:** update conftest.py ([1174a62](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1174a62))
* **internal:** version bump ([7241eaa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7241eaa))
* **readme:** update badges ([00661c2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00661c2))
* **tests:** add tests for httpx client instantiation & proxies ([b831d88](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b831d88))
* **tests:** run tests in parallel ([4b24a79](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4b24a79))

### Documentation

* **client:** fix httpx.Timeout documentation reference ([b0138b1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b0138b1))

## 0.54.0 (2025-06-10)

Full Changelog: [v0.53.0...v0.54.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.53.0...v0.54.0)

### Features

* **client:** add support for fine-grained-tool-streaming-2025-05-14 ([07ec081](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/07ec081))

### Bug Fixes

* **httpx:** resolve conflict between default transport and proxy settings ([#969](https://github.com/anthropics/anthropic-sdk-python/issues/969)) ([a6efded](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a6efded))
* **tests:** update test ([99c2433](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/99c2433))

### Chores

* **internal:** version bump ([45029f4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/45029f4))

### Documentation

* **contributing:** fix uv script for bootstrapping ([d2bde52](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d2bde52))

## 0.53.0 (2025-06-09)

Full Changelog: [v0.52.2...v0.53.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.52.2...v0.53.0)

### Features

* **client:** add follow_redirects request option ([e5238c0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e5238c0))
* **client:** add support for new text_editor_20250429 tool ([b3b3f5b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b3b3f5b))

### Bug Fixes

* **client:** deprecate BetaBase64PDFBlock in favor of BetaRequestDocumentBlock ([5ac58e9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5ac58e9))
* **internal:** fix typing remapping ([6c415da](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6c415da))

### Chores

* **internal:** codegen related update ([94812ec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/94812ec))
* **internal:** version bump ([41ce701](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/41ce701))
* **tests:** improve testing by extracting fixtures ([68c62cc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/68c62cc))

## 0.52.2 (2025-06-02)

Full Changelog: [v0.52.1...v0.52.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.52.1...v0.52.2)

### Bug Fixes

* **client:** fix issue with server_tool_use input tracking and improve tests ([3fe3fa2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3fe3fa2))
* **docs:** remove reference to rye shell ([2b3d677](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2b3d677))

### Chores

* **docs:** remove unnecessary param examples ([6b129f4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6b129f4))

### Refactors

* **pkg:** switch from rye to uv ([f553908](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f553908))

## 0.52.1 (2025-05-28)

Full Changelog: [v0.52.0...v0.52.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.52.0...v0.52.1)

### Bug Fixes

* **example:** logo.png was broken ([#1021](https://github.com/anthropics/anthropic-sdk-python/issues/1021)) ([1ee8314](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1ee8314))

### Chores

* **examples:** show how to pass an authorization token to an MCP server ([18be7f3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/18be7f3))
* **internal:** fix release workflows ([be9af1f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/be9af1f))

## 0.52.0 (2025-05-22)

Full Changelog: [v0.51.0...v0.52.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.51.0...v0.52.0)

### Features

* **api:** add claude 4 models, files API, code execution tool, MCP connector and more ([9c48bc6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9c48bc6))

### Bug Fixes

* **package:** support direct resource imports ([6d73bab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6d73bab))

### Chores

* **ci:** fix installation instructions ([ca374e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ca374e5))
* **ci:** upload sdks to package manager ([fde0c44](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fde0c44))
* **internal:** avoid errors for isinstance checks on proxies ([ef4be3f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ef4be3f))
* **internal:** codegen related update ([40359d9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/40359d9))

### Documentation

* add security warning for overriding parameters ([#1008](https://github.com/anthropics/anthropic-sdk-python/issues/1008)) ([9f52239](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9f52239))

## 0.51.0 (2025-05-07)

Full Changelog: [v0.50.0...v0.51.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.50.0...v0.51.0)

### Features

* **api:** adds web search capabilities to the Claude API ([bec0cf9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bec0cf9))

### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([c50f406](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c50f406))
* **sockets:** handle non-portable socket flags ([#935](https://github.com/anthropics/anthropic-sdk-python/issues/935)) ([205c8dd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/205c8dd))

### Chores

* broadly detect json family of content-type headers ([66bbb3a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/66bbb3a))
* **ci:** only use depot for staging repos ([c867a11](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c867a11))
* **ci:** run on more branches and use depot runners ([95f5f17](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/95f5f17))
* **internal:** add back missing custom modifications for Web Search ([f43ba69](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f43ba69))
* **internal:** minor formatting changes ([8afef08](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8afef08))
* use lazy imports for resources ([704be81](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/704be81))

## 0.50.0 (2025-04-22)

Full Changelog: [v0.49.0...v0.50.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.49.0...v0.50.0)

### Features

* **api:** extract ContentBlockDelta events into their own schemas ([#920](https://github.com/anthropics/anthropic-sdk-python/issues/920)) ([ae773d6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ae773d6))
* **api:** manual updates ([46ac1f8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/46ac1f8))
* **api:** manual updates ([48d9739](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/48d9739))
* **api:** manual updates ([66e8cc3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/66e8cc3))
* **api:** manual updates ([a74746e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a74746e))

### Bug Fixes

* **ci:** ensure pip is always available ([#907](https://github.com/anthropics/anthropic-sdk-python/issues/907)) ([3632687](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3632687))
* **ci:** remove publishing patch ([#908](https://github.com/anthropics/anthropic-sdk-python/issues/908)) ([cae0323](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cae0323))
* **client:** deduplicate stop reason type ([#913](https://github.com/anthropics/anthropic-sdk-python/issues/913)) ([3ab0194](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3ab0194))
* **client:** send all configured auth headers ([#929](https://github.com/anthropics/anthropic-sdk-python/issues/929)) ([9d2581e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9d2581e))
* **perf:** optimize some hot paths ([cff76cb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cff76cb))
* **perf:** skip traversing types for NotGiven values ([dadac7f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dadac7f))
* **project:** bump httpx minimum version to 0.25.0 ([b554138](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b554138)), closes [#902](https://github.com/anthropics/anthropic-sdk-python/issues/902)
* **types:** handle more discriminated union shapes ([#906](https://github.com/anthropics/anthropic-sdk-python/issues/906)) ([2fc179a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2fc179a))
* **vertex:** explicitly include requests extra ([2b1221b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2b1221b))

### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([#912](https://github.com/anthropics/anthropic-sdk-python/issues/912)) ([ddf7835](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ddf7835))
* **ci:** add timeout thresholds for CI jobs ([7226a5c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7226a5c))
* **client:** minor internal fixes ([99b9a38](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/99b9a38))
* **internal:** add back release workflow ([ce18972](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ce18972))
* **internal:** base client updates ([2e08c71](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2e08c71))
* **internal:** bump pyright version ([d9ea30e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d9ea30e))
* **internal:** bump rye to 0.44.0 ([#905](https://github.com/anthropics/anthropic-sdk-python/issues/905)) ([e1a1b14](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e1a1b14))
* **internal:** expand CI branch coverage ([#934](https://github.com/anthropics/anthropic-sdk-python/issues/934)) ([b23fdc9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b23fdc9))
* **internal:** fix list file params ([cfbaaf9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cfbaaf9))
* **internal:** import ordering changes ([#895](https://github.com/anthropics/anthropic-sdk-python/issues/895)) ([b8da2f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b8da2f7))
* **internal:** import reformatting ([5e6cd74](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e6cd74))
* **internal:** reduce CI branch coverage ([07e813f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/07e813f))
* **internal:** refactor retries to not use recursion ([4354e82](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4354e82))
* **internal:** remove CI condition ([#916](https://github.com/anthropics/anthropic-sdk-python/issues/916)) ([043b56b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/043b56b))
* **internal:** remove extra empty newlines ([#904](https://github.com/anthropics/anthropic-sdk-python/issues/904)) ([cfe8f6e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cfe8f6e))
* **internal:** remove trailing character ([#924](https://github.com/anthropics/anthropic-sdk-python/issues/924)) ([dc8e781](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dc8e781))
* **internal:** remove unused http client options forwarding ([#890](https://github.com/anthropics/anthropic-sdk-python/issues/890)) ([e0428bf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e0428bf))
* **internal:** slight transform perf improvement ([#931](https://github.com/anthropics/anthropic-sdk-python/issues/931)) ([3ed4e5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3ed4e5e))
* **internal:** update config ([#914](https://github.com/anthropics/anthropic-sdk-python/issues/914)) ([a697234](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a697234))
* **internal:** update models test ([b1e031d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b1e031d))
* **internal:** update pyright settings ([38bdc6c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/38bdc6c))
* **internal:** variable name and test updates ([#925](https://github.com/anthropics/anthropic-sdk-python/issues/925)) ([f5d0809](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f5d0809))
* **tests:** improve enum examples ([#932](https://github.com/anthropics/anthropic-sdk-python/issues/932)) ([808aaf3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/808aaf3))
* **vertex:** improve error message when missing extra ([15dc4cb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/15dc4cb))

### Documentation

* revise readme docs about nested params ([#900](https://github.com/anthropics/anthropic-sdk-python/issues/900)) ([0f80ab0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0f80ab0))
* swap examples used in readme ([#928](https://github.com/anthropics/anthropic-sdk-python/issues/928)) ([96ff1c7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/96ff1c7))

## 0.49.0 (2025-02-28)

Full Changelog: [v0.48.0...v0.49.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.48.0...v0.49.0)

### Features

* **api:** add support for disabling tool calls ([#888](https://github.com/anthropics/anthropic-sdk-python/issues/888)) ([bfde3d2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bfde3d2))

### Chores

* **docs:** update client docstring ([#887](https://github.com/anthropics/anthropic-sdk-python/issues/887)) ([4d3ec5e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4d3ec5e))

### Documentation

* update URLs from stainlessapi.com to stainless.com ([#885](https://github.com/anthropics/anthropic-sdk-python/issues/885)) ([312364b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/312364b))

## 0.48.0 (2025-02-27)

Full Changelog: [v0.47.2...v0.48.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.47.2...v0.48.0)

### Features

* **api:** add URL source blocks for images and PDFs ([#884](https://github.com/anthropics/anthropic-sdk-python/issues/884)) ([e6b3a70](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e6b3a70))

### Documentation

* add thinking examples ([f463248](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f463248))

## 0.47.2 (2025-02-25)

Full Changelog: [v0.47.1...v0.47.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.47.1...v0.47.2)

### Bug Fixes

* **beta:** add thinking to beta.messages.stream ([69e3db1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/69e3db1))

### Chores

* **internal:** properly set __pydantic_private__ ([#879](https://github.com/anthropics/anthropic-sdk-python/issues/879)) ([3537a3b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3537a3b))

## 0.47.1 (2025-02-24)

Full Changelog: [v0.47.0...v0.47.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.47.0...v0.47.1)

### Chores

* **internal:** update spec ([#871](https://github.com/anthropics/anthropic-sdk-python/issues/871)) ([916be18](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/916be18))
* update large max_tokens error message ([40c71df](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/40c71df))

## 0.47.0 (2025-02-24)

Full Changelog: [v0.46.0...v0.47.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.46.0...v0.47.0)

### Features

* **api:** add claude-3.7 + support for thinking ([c5387e6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c5387e6))
* **client:** add more status exceptions ([#854](https://github.com/anthropics/anthropic-sdk-python/issues/854)) ([00d9512](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00d9512))
* **client:** allow passing `NotGiven` for body ([#868](https://github.com/anthropics/anthropic-sdk-python/issues/868)) ([8ab445e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8ab445e))

### Bug Fixes

* **client:** mark some request bodies as optional ([8ab445e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8ab445e))

### Chores

* **internal:** fix devcontainers setup ([#870](https://github.com/anthropics/anthropic-sdk-python/issues/870)) ([1a21c6a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1a21c6a))

## 0.46.0 (2025-02-18)

Full Changelog: [v0.45.2...v0.46.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.45.2...v0.46.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#858](https://github.com/anthropics/anthropic-sdk-python/issues/858)) ([0e75983](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0e75983))
* **jsonl:** add .close() method ([#862](https://github.com/anthropics/anthropic-sdk-python/issues/862)) ([137335c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/137335c))
* **pagination:** avoid fetching when has_more: false ([#860](https://github.com/anthropics/anthropic-sdk-python/issues/860)) ([0cdb81d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0cdb81d))

### Bug Fixes

* asyncify on non-asyncio runtimes ([#864](https://github.com/anthropics/anthropic-sdk-python/issues/864)) ([f92b36d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f92b36d))
* **internal:** add back custom header naming support ([#861](https://github.com/anthropics/anthropic-sdk-python/issues/861)) ([cf851ae](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cf851ae))
* **jsonl:** lower chunk size ([#863](https://github.com/anthropics/anthropic-sdk-python/issues/863)) ([38fb720](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/38fb720))

### Chores

* **api:** update openapi spec url ([#852](https://github.com/anthropics/anthropic-sdk-python/issues/852)) ([461d821](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/461d821))
* **internal:** bummp ruff dependency ([#856](https://github.com/anthropics/anthropic-sdk-python/issues/856)) ([590c3fa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/590c3fa))
* **internal:** change default timeout to an int ([#855](https://github.com/anthropics/anthropic-sdk-python/issues/855)) ([3152e1a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3152e1a))
* **internal:** fix tests ([fc41ba2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fc41ba2))
* **internal:** fix type traversing dictionary params ([#859](https://github.com/anthropics/anthropic-sdk-python/issues/859)) ([c5b700d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c5b700d))
* **internal:** reorder model constants ([#847](https://github.com/anthropics/anthropic-sdk-python/issues/847)) ([aadd531](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aadd531))
* **internal:** update models used in tests ([aadd531](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aadd531))

## 0.45.2 (2025-01-27)

Full Changelog: [v0.45.1...v0.45.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.45.1...v0.45.2)

### Bug Fixes

* **streaming:** avoid invalid deser type error ([#845](https://github.com/anthropics/anthropic-sdk-python/issues/845)) ([72a2585](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72a2585))

## 0.45.1 (2025-01-27)

Full Changelog: [v0.45.0...v0.45.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.45.0...v0.45.1)

### Bug Fixes

* **streaming:** accumulate citations ([#844](https://github.com/anthropics/anthropic-sdk-python/issues/844)) ([e665f2f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e665f2f))

### Chores

* **docs:** updates ([#841](https://github.com/anthropics/anthropic-sdk-python/issues/841)) ([fb10a7d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fb10a7d))

## 0.45.0 (2025-01-23)

Full Changelog: [v0.44.0...v0.45.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.44.0...v0.45.0)

### Features

* **api:** add citations ([#839](https://github.com/anthropics/anthropic-sdk-python/issues/839)) ([2ec74b6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2ec74b6))
* **client:** support results endpoint ([#835](https://github.com/anthropics/anthropic-sdk-python/issues/835)) ([5dd88bf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5dd88bf))

### Chores

* **internal:** minor formatting changes ([#838](https://github.com/anthropics/anthropic-sdk-python/issues/838)) ([31eb826](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/31eb826))

## 0.44.0 (2025-01-21)

Full Changelog: [v0.43.1...v0.44.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.43.1...v0.44.0)

### Features

* **streaming:** add request_id getter ([#831](https://github.com/anthropics/anthropic-sdk-python/issues/831)) ([fb397e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fb397e0))

### Bug Fixes

* **tests:** make test_get_platform less flaky ([#830](https://github.com/anthropics/anthropic-sdk-python/issues/830)) ([f2c10ca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f2c10ca))

### Chores

* deprecate more models ([c647e25](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c647e25))
* **internal:** avoid pytest-asyncio deprecation warning ([#832](https://github.com/anthropics/anthropic-sdk-python/issues/832)) ([2b3ceff](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2b3ceff))
* **internal:** minor style changes ([#833](https://github.com/anthropics/anthropic-sdk-python/issues/833)) ([65cfb7b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/65cfb7b))

### Documentation

* **raw responses:** fix duplicate `the` ([#828](https://github.com/anthropics/anthropic-sdk-python/issues/828)) ([ff850f8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ff850f8))

## 0.43.1 (2025-01-17)

Full Changelog: [v0.43.0...v0.43.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.43.0...v0.43.1)

### Bug Fixes

* **docs:** correct results return type ([69ad511](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/69ad511))

### Chores

* **internal:** bump pyright dependency ([#822](https://github.com/anthropics/anthropic-sdk-python/issues/822)) ([f8ddb90](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f8ddb90))
* **internal:** fix lint ([483cc27](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/483cc27))
* **streaming:** add runtime type check for better error messages ([#826](https://github.com/anthropics/anthropic-sdk-python/issues/826)) ([cf69e09](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cf69e09))
* **types:** add more discriminator metadata ([#825](https://github.com/anthropics/anthropic-sdk-python/issues/825)) ([d0de8e5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d0de8e5))

## 0.43.0 (2025-01-14)

Full Changelog: [v0.42.0...v0.43.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.42.0...v0.43.0)

### Features

* **api:** add message batch delete endpoint ([#802](https://github.com/anthropics/anthropic-sdk-python/issues/802)) ([9cf1e99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9cf1e99))
* **beta:** add streaming helpers for beta messages ([#819](https://github.com/anthropics/anthropic-sdk-python/issues/819)) ([d913ba3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d913ba3))

### Bug Fixes

* **client:** only call .close() when needed ([#811](https://github.com/anthropics/anthropic-sdk-python/issues/811)) ([21e0eb3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/21e0eb3))
* correctly handle deserialising `cls` fields ([#817](https://github.com/anthropics/anthropic-sdk-python/issues/817)) ([60e56a5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/60e56a5))
* **types:** allow extra properties in input schemas ([d0961c2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d0961c2))

### Chores

* add missing isclass check ([#806](https://github.com/anthropics/anthropic-sdk-python/issues/806)) ([1fc034d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1fc034d))
* bump testing data uri ([#800](https://github.com/anthropics/anthropic-sdk-python/issues/800)) ([641ae8d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/641ae8d))
* **internal:** bump httpx dependency ([#809](https://github.com/anthropics/anthropic-sdk-python/issues/809)) ([7d678f1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7d678f1))
* **internal:** minor reformatting ([5a80668](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5a80668))
* **internal:** update deps ([#820](https://github.com/anthropics/anthropic-sdk-python/issues/820)) ([32c3e1a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/32c3e1a))
* **internal:** update examples ([#810](https://github.com/anthropics/anthropic-sdk-python/issues/810)) ([bb588ca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bb588ca))
* **vertex:** remove deprecated HTTP client options ([3f4eada](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3f4eada))
* **vertex:** remove deprecated HTTP client options ([c82f3e8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c82f3e8))

### Documentation

* fix typos ([#812](https://github.com/anthropics/anthropic-sdk-python/issues/812)) ([8f46cae](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8f46cae))
* fix typos ([#813](https://github.com/anthropics/anthropic-sdk-python/issues/813)) ([ac44348](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ac44348))
* **readme:** fix misplaced period ([#816](https://github.com/anthropics/anthropic-sdk-python/issues/816)) ([4358226](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4358226))

### Refactors

* **stream:** make `MessageStream` wrap `Stream` directly ([#805](https://github.com/anthropics/anthropic-sdk-python/issues/805)) ([5669399](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5669399))
* **vertex:** remove deprecated HTTP client options ([#808](https://github.com/anthropics/anthropic-sdk-python/issues/808)) ([3f4eada](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3f4eada))

## 0.42.0 (2024-12-17)

Full Changelog: [v0.41.0...v0.42.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.41.0...v0.42.0)

### Features

* **api:** general availability updates ([#795](https://github.com/anthropics/anthropic-sdk-python/issues/795)) ([0954c48](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0954c48))

### Bug Fixes

* **vertex:** remove `anthropic_version` deletion for token counting ([f613929](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f613929))

### Chores

* **internal:** fix some typos ([#799](https://github.com/anthropics/anthropic-sdk-python/issues/799)) ([45addb6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/45addb6))

## 0.41.0 (2024-12-17)

Full Changelog: [v0.40.0...v0.41.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.40.0...v0.41.0)

### Features

* **api:** general availability updates ([5db8538](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5db8538))
* **api:** general availability updates ([#795](https://github.com/anthropics/anthropic-sdk-python/issues/795)) ([c8d5e43](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c8d5e43))
* **vertex:** support token counting ([6c3eded](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6c3eded))

### Bug Fixes

* **internal:** correct support for TypeAliasType ([2f6ba9e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2f6ba9e))

### Chores

* **api:** update spec version ([#792](https://github.com/anthropics/anthropic-sdk-python/issues/792)) ([f54c1da](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f54c1da))
* **bedrock/vertex:** explicit error for unsupported messages endpoints ([c4cf816](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c4cf816))
* **internal:** add support for TypeAliasType ([#786](https://github.com/anthropics/anthropic-sdk-python/issues/786)) ([287ebd2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/287ebd2))
* **internal:** bump pydantic dependency ([#775](https://github.com/anthropics/anthropic-sdk-python/issues/775)) ([99b4d06](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/99b4d06))
* **internal:** bump pyright ([#769](https://github.com/anthropics/anthropic-sdk-python/issues/769)) ([81f7d70](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/81f7d70))
* **internal:** bump pyright ([#785](https://github.com/anthropics/anthropic-sdk-python/issues/785)) ([44ab333](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/44ab333))
* **internal:** remove some duplicated imports ([#788](https://github.com/anthropics/anthropic-sdk-python/issues/788)) ([576ae9b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/576ae9b))
* **internal:** update spec ([#793](https://github.com/anthropics/anthropic-sdk-python/issues/793)) ([7cffc99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7cffc99))
* **internal:** updated imports ([#789](https://github.com/anthropics/anthropic-sdk-python/issues/789)) ([d163c08](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d163c08))
* make the `Omit` type public ([#772](https://github.com/anthropics/anthropic-sdk-python/issues/772)) ([4ed0419](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4ed0419))
* remove deprecated HTTP client options ([#777](https://github.com/anthropics/anthropic-sdk-python/issues/777)) ([3933368](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3933368))

### Documentation

* **readme:** example snippet for client context manager ([#791](https://github.com/anthropics/anthropic-sdk-python/issues/791)) ([d0a5f0c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d0a5f0c))
* **readme:** fix http client proxies example ([#778](https://github.com/anthropics/anthropic-sdk-python/issues/778)) ([df1a549](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/df1a549))
* use latest sonnet in example snippets ([#781](https://github.com/anthropics/anthropic-sdk-python/issues/781)) ([1ad9e4f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1ad9e4f))

## 0.40.0 (2024-11-28)

Full Changelog: [v0.39.0...v0.40.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.39.0...v0.40.0)

### Features

* **client:** add ._request_id property to object responses ([#743](https://github.com/anthropics/anthropic-sdk-python/issues/743)) ([9fb64a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9fb64a6))

### Bug Fixes

* **asyncify:** avoid hanging process under certain conditions ([#756](https://github.com/anthropics/anthropic-sdk-python/issues/756)) ([c71bba2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c71bba2))
* **bedrock:** correct URL encoding for model params ([#759](https://github.com/anthropics/anthropic-sdk-python/issues/759)) ([be4e73a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/be4e73a))
* **client:** compat with new httpx 0.28.0 release ([#765](https://github.com/anthropics/anthropic-sdk-python/issues/765)) ([de51f60](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/de51f60))
* don't use dicts as iterables in transform ([#750](https://github.com/anthropics/anthropic-sdk-python/issues/750)) ([1f71464](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1f71464))
* **types:** remove anthropic-instant-1.2 model ([#744](https://github.com/anthropics/anthropic-sdk-python/issues/744)) ([23637de](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/23637de))

### Chores

* **api:** update spec version ([#751](https://github.com/anthropics/anthropic-sdk-python/issues/751)) ([4ec986c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4ec986c))
* **ci:** remove unneeded workflow ([#742](https://github.com/anthropics/anthropic-sdk-python/issues/742)) ([472b7d3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/472b7d3))
* **internal:** exclude mypy from running on tests ([#764](https://github.com/anthropics/anthropic-sdk-python/issues/764)) ([bce763a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bce763a))
* **internal:** fix compat model_dump method when warnings are passed ([#760](https://github.com/anthropics/anthropic-sdk-python/issues/760)) ([0e09236](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0e09236))
* **internal:** minor formatting changes ([493020e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/493020e))
* remove now unused `cached-property` dep ([#762](https://github.com/anthropics/anthropic-sdk-python/issues/762)) ([b9ffefe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b9ffefe))
* **tests:** adjust retry timeout values ([#736](https://github.com/anthropics/anthropic-sdk-python/issues/736)) ([27ed781](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/27ed781))
* **tests:** limit array example length ([#754](https://github.com/anthropics/anthropic-sdk-python/issues/754)) ([6cab2b9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6cab2b9))

### Documentation

* add info log level to readme ([#761](https://github.com/anthropics/anthropic-sdk-python/issues/761)) ([5966b85](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5966b85))
* move comments in example snippets ([#749](https://github.com/anthropics/anthropic-sdk-python/issues/749)) ([f887930](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f887930))

## 0.39.0 (2024-11-04)

Full Changelog: [v0.38.0...v0.39.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.38.0...v0.39.0)

### ⚠ BREAKING CHANGES

* **client:** remove legacy `client.count_tokens()` & `client.get_tokenizer()` methods ([#726](https://github.com/anthropics/anthropic-sdk-python/issues/726))
  * This functionality has been replaced by the `client.beta.messages.count_tokens()` API which supports newer models and all content functionality, such as images and PDFs.

### Features

* **api:** add new haiku model ([#731](https://github.com/anthropics/anthropic-sdk-python/issues/731)) ([77eaaf9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/77eaaf9))
* **project:** drop support for Python 3.7 ([#729](https://github.com/anthropics/anthropic-sdk-python/issues/729)) ([7f897e2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7f897e2))

### Bug Fixes

* don't use dicts as iterables in transform ([#724](https://github.com/anthropics/anthropic-sdk-python/issues/724)) ([62bb863](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/62bb863))
* support json safe serialization for basemodel subclasses ([#727](https://github.com/anthropics/anthropic-sdk-python/issues/727)) ([5be855e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5be855e))
* **types:** add missing token-counting-2024-11-01 ([#722](https://github.com/anthropics/anthropic-sdk-python/issues/722)) ([c549736](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c549736))

### Documentation

* **readme:** mention new token counting endpoint ([#728](https://github.com/anthropics/anthropic-sdk-python/issues/728)) ([72a4636](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72a4636))

### Refactors

* **client:** remove legacy `client.count_tokens()` method ([#726](https://github.com/anthropics/anthropic-sdk-python/issues/726)) ([14e4244](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/14e4244))

## 0.38.0 (2024-11-01)

Full Changelog: [v0.37.1...v0.38.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.37.1...v0.38.0)

### Features

* **api:** add message token counting & PDFs support ([#721](https://github.com/anthropics/anthropic-sdk-python/issues/721)) ([e4856dd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e4856dd))

### Bug Fixes

* **count_tokens:** correctly set beta header ([e5b4b54](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e5b4b54))
* **types:** add missing token-counting-2024-11-01 ([1897883](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1897883))

### Chores

* **internal:** bump mypy ([#720](https://github.com/anthropics/anthropic-sdk-python/issues/720)) ([fe8d19e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fe8d19e))
* **internal:** bump pytest to v8 & pydantic ([#716](https://github.com/anthropics/anthropic-sdk-python/issues/716)) ([00fe1f8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00fe1f8))
* **internal:** update spec version ([#712](https://github.com/anthropics/anthropic-sdk-python/issues/712)) ([f71b0f5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f71b0f5))
* **tests:** move lazy tokenizer test outside of pytest ([d8f2402](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d8f2402))

## 0.37.1 (2024-10-22)

Full Changelog: [v0.37.0...v0.37.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.37.0...v0.37.1)

### Bug Fixes

* **bedrock:** correct handling of messages beta ([#711](https://github.com/anthropics/anthropic-sdk-python/issues/711)) ([4cba32b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4cba32b))
* **vertex:** use correct beta url ([b76db5c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b76db5c))

## 0.37.0 (2024-10-22)

Full Changelog: [v0.36.2...v0.37.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.36.2...v0.37.0)

### Features

* **api:** add new model and `computer-use-2024-10-22` beta ([dd93d87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dd93d87))
* **bedrock:** add messages beta ([2566c93](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2566c93))
* **vertex:** add messages beta ([0d1f1a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0d1f1a6))

### Bug Fixes

* **client/async:** correctly retry in all cases ([#704](https://github.com/anthropics/anthropic-sdk-python/issues/704)) ([ee6febc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ee6febc))

### Chores

* **api:** add title ([#703](https://github.com/anthropics/anthropic-sdk-python/issues/703)) ([a046817](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a046817))
* **internal:** bump ruff dependency ([#700](https://github.com/anthropics/anthropic-sdk-python/issues/700)) ([d5bf9e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d5bf9e1))
* **internal:** remove unused black config ([#705](https://github.com/anthropics/anthropic-sdk-python/issues/705)) ([3259eb0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3259eb0))
* **internal:** update spec ([#706](https://github.com/anthropics/anthropic-sdk-python/issues/706)) ([6ab0ce9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6ab0ce9))

## 0.36.2 (2024-10-17)

Full Changelog: [v0.36.1...v0.36.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.36.1...v0.36.2)

### Bug Fixes

* **types:** remove misleading betas TypedDict property for the Batch API ([#697](https://github.com/anthropics/anthropic-sdk-python/issues/697)) ([e1b9e31](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e1b9e31))

### Chores

* **internal:** update test syntax ([#699](https://github.com/anthropics/anthropic-sdk-python/issues/699)) ([a836157](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a836157))

## 0.36.1 (2024-10-15)

Full Changelog: [v0.36.0...v0.36.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.36.0...v0.36.1)

### Bug Fixes

* allow header params to override default headers ([#690](https://github.com/anthropics/anthropic-sdk-python/issues/690)) ([56f195f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/56f195f))
* **beta:** merge betas param with the default value ([#695](https://github.com/anthropics/anthropic-sdk-python/issues/695)) ([f52eac9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f52eac9))

### Chores

* **internal:** update spec URL ([#694](https://github.com/anthropics/anthropic-sdk-python/issues/694)) ([1b437cc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1b437cc))

## 0.36.0 (2024-10-08)

Full Changelog: [v0.35.0...v0.36.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.35.0...v0.36.0)

### Features

* **api:** add message batches api ([cd1ffcb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cd1ffcb))

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#676](https://github.com/anthropics/anthropic-sdk-python/issues/676)) ([93d6eeb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/93d6eeb))

### Chores

* add repr to PageInfo class ([#678](https://github.com/anthropics/anthropic-sdk-python/issues/678)) ([53e87e8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/53e87e8))

### Refactors

* **types:** improve metadata type names ([#683](https://github.com/anthropics/anthropic-sdk-python/issues/683)) ([59f2088](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/59f2088))
* **types:** improve metadata types ([#682](https://github.com/anthropics/anthropic-sdk-python/issues/682)) ([e037d1c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e037d1c))
* **types:** improve tool type names ([#679](https://github.com/anthropics/anthropic-sdk-python/issues/679)) ([f6f3afe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f6f3afe))
* **types:** improve tool type names ([#680](https://github.com/anthropics/anthropic-sdk-python/issues/680)) ([fe2e417](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fe2e417))

## 0.35.0 (2024-10-04)

Full Changelog: [v0.34.2...v0.35.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.34.2...v0.35.0)

### Features

* **api:** support disabling parallel tool use ([#674](https://github.com/anthropics/anthropic-sdk-python/issues/674)) ([9079a99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9079a99))
* **bedrock:** add `profile` argument to client ([#648](https://github.com/anthropics/anthropic-sdk-python/issues/648)) ([6ea5fce](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6ea5fce))
* **client:** allow overriding retry count header ([#670](https://github.com/anthropics/anthropic-sdk-python/issues/670)) ([1fb081f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1fb081f))
* **client:** send retry count header ([#664](https://github.com/anthropics/anthropic-sdk-python/issues/664)) ([17c26d5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/17c26d5))

### Bug Fixes

* **client:** handle domains with underscores ([#663](https://github.com/anthropics/anthropic-sdk-python/issues/663)) ([84ad451](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/84ad451))
* **types:** correctly mark stream discriminator as optional ([#657](https://github.com/anthropics/anthropic-sdk-python/issues/657)) ([2386f98](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2386f98))

### Chores

* add docstrings to raw response properties ([#654](https://github.com/anthropics/anthropic-sdk-python/issues/654)) ([35e6cf7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/35e6cf7))
* **internal:** add support for parsing bool response content ([#675](https://github.com/anthropics/anthropic-sdk-python/issues/675)) ([0bbc0a3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0bbc0a3))
* **internal:** bump pyright / mypy version ([#662](https://github.com/anthropics/anthropic-sdk-python/issues/662)) ([c03a71f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c03a71f))
* **internal:** bump ruff ([#660](https://github.com/anthropics/anthropic-sdk-python/issues/660)) ([0a34018](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0a34018))
* **internal:** update pydantic v1 compat helpers ([#666](https://github.com/anthropics/anthropic-sdk-python/issues/666)) ([ee8e2bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ee8e2bd))
* **internal:** use `typing_extensions.overload` instead of `typing` ([#667](https://github.com/anthropics/anthropic-sdk-python/issues/667)) ([153361d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/153361d))
* pyproject.toml formatting changes ([#650](https://github.com/anthropics/anthropic-sdk-python/issues/650)) ([4c229dc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4c229dc))

### Documentation

* fix typo in fenced code block language ([#673](https://github.com/anthropics/anthropic-sdk-python/issues/673)) ([a03414e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a03414e))
* improve and reference contributing documentation ([#672](https://github.com/anthropics/anthropic-sdk-python/issues/672)) ([5bd9690](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5bd9690))
* **readme:** add section on determining installed version ([#655](https://github.com/anthropics/anthropic-sdk-python/issues/655)) ([5898f42](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5898f42))
* update CONTRIBUTING.md ([#659](https://github.com/anthropics/anthropic-sdk-python/issues/659)) ([2df25bf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2df25bf))

## 0.34.2 (2024-09-04)

Full Changelog: [v0.34.1...v0.34.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.34.1...v0.34.2)

### Chores

* **api:** deprecate claude-1 model ([eab07dc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/eab07dc))
* **ci:** also run pydantic v1 tests ([#644](https://github.com/anthropics/anthropic-sdk-python/issues/644)) ([c61fe89](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c61fe89))

## 0.34.1 (2024-08-19)

Full Changelog: [v0.34.0...v0.34.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.34.0...v0.34.1)

### Chores

* **ci:** add CODEOWNERS file ([#639](https://github.com/anthropics/anthropic-sdk-python/issues/639)) ([33001cc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/33001cc))
* **client:** fix parsing union responses when non-json is returned ([#643](https://github.com/anthropics/anthropic-sdk-python/issues/643)) ([45be91d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/45be91d))
* **docs/api:** update prompt caching helpers ([6a55aee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6a55aee))
* **internal:** use different 32bit detection method ([#640](https://github.com/anthropics/anthropic-sdk-python/issues/640)) ([d6b2b63](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d6b2b63))

## 0.34.0 (2024-08-14)

Full Changelog: [v0.33.1...v0.34.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.33.1...v0.34.0)

### Features

* **api:** add prompt caching beta ([3978411](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3978411))
* **client:** add streaming helpers for prompt caching ([98a0a7b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/98a0a7b))

### Chores

* **examples:** minor formatting changes ([#633](https://github.com/anthropics/anthropic-sdk-python/issues/633)) ([20487ea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/20487ea))

## 0.33.1 (2024-08-12)

Full Changelog: [v0.33.0...v0.33.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.33.0...v0.33.1)

### Chores

* **ci:** bump prism mock server version ([#630](https://github.com/anthropics/anthropic-sdk-python/issues/630)) ([29545ee](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/29545ee))
* **internal:** ensure package is importable in lint cmd ([#632](https://github.com/anthropics/anthropic-sdk-python/issues/632)) ([d685824](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d685824))

## 0.33.0 (2024-08-09)

Full Changelog: [v0.32.0...v0.33.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.32.0...v0.33.0)

### Features

* **client:** add `retries_taken` to raw response class ([43fb587](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/43fb587))

### Chores

* **internal:** bump pyright ([#622](https://github.com/anthropics/anthropic-sdk-python/issues/622)) ([9480109](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9480109))
* **internal:** bump ruff version ([#625](https://github.com/anthropics/anthropic-sdk-python/issues/625)) ([b1a4e7b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b1a4e7b))
* **internal:** test updates ([#624](https://github.com/anthropics/anthropic-sdk-python/issues/624)) ([2cea1f5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2cea1f5))
* **internal:** update pydantic compat helper function ([#627](https://github.com/anthropics/anthropic-sdk-python/issues/627)) ([dc18ee0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dc18ee0))
* **internal:** updates ([#629](https://github.com/anthropics/anthropic-sdk-python/issues/629)) ([d6357a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d6357a6))
* **internal:** use `TypeAlias` marker for type assignments ([#621](https://github.com/anthropics/anthropic-sdk-python/issues/621)) ([a4bff9c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a4bff9c))
* sync openapi version ([#617](https://github.com/anthropics/anthropic-sdk-python/issues/617)) ([9c0ad95](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9c0ad95))
* sync openapi version ([#620](https://github.com/anthropics/anthropic-sdk-python/issues/620)) ([0a3f3fa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0a3f3fa))
* sync openapi version ([#628](https://github.com/anthropics/anthropic-sdk-python/issues/628)) ([cfad41f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cfad41f))

## 0.32.0 (2024-07-29)

Full Changelog: [v0.31.2...v0.32.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.31.2...v0.32.0)

### Features

* add back compat alias for InputJsonDelta ([25a5b6c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/25a5b6c))

### Bug Fixes

* change signatures for the stream function ([c9eb11b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c9eb11b))
* **client:** correctly apply client level timeout for messages ([#615](https://github.com/anthropics/anthropic-sdk-python/issues/615)) ([5f8d88f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5f8d88f))

### Chores

* **docs:** document how to do per-request http client customization ([#603](https://github.com/anthropics/anthropic-sdk-python/issues/603)) ([5161f62](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5161f62))
* **internal:** add type construction helper ([#613](https://github.com/anthropics/anthropic-sdk-python/issues/613)) ([5e36940](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e36940))
* sync spec ([#605](https://github.com/anthropics/anthropic-sdk-python/issues/605)) ([6b7707f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6b7707f))
* **tests:** update prism version ([#607](https://github.com/anthropics/anthropic-sdk-python/issues/607)) ([1797dc6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1797dc6))

### Refactors

* extract model out to a named type and rename partialjson ([#612](https://github.com/anthropics/anthropic-sdk-python/issues/612)) ([c53efc7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c53efc7))

## 0.31.2 (2024-07-17)

Full Changelog: [v0.31.1...v0.31.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.31.1...v0.31.2)

### Bug Fixes

* **vertex:** also refresh auth if there is no token ([4a8d02d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4a8d02d))
* **vertex:** correct request options in retries ([460547b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/460547b))

### Chores

* **docs:** minor update to formatting of API link in README ([#594](https://github.com/anthropics/anthropic-sdk-python/issues/594)) ([113b6ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/113b6ac))
* **internal:** update formatting ([#597](https://github.com/anthropics/anthropic-sdk-python/issues/597)) ([565dfcd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/565dfcd))
* **tests:** faster bedrock retry tests ([4ff067f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4ff067f))

## 0.31.1 (2024-07-15)

Full Changelog: [v0.31.0...v0.31.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.31.0...v0.31.1)

### Bug Fixes

* **bedrock:** correct request options for retries ([#593](https://github.com/anthropics/anthropic-sdk-python/issues/593)) ([f68c81d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f68c81d))

### Chores

* **ci:** also run workflows for PRs targeting `next` ([#587](https://github.com/anthropics/anthropic-sdk-python/issues/587)) ([f7e49f2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f7e49f2))
* **internal:** minor changes to tests ([#591](https://github.com/anthropics/anthropic-sdk-python/issues/591)) ([fabd591](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fabd591))
* **internal:** minor formatting changes ([a71927b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a71927b))
* **internal:** minor import restructuring ([#588](https://github.com/anthropics/anthropic-sdk-python/issues/588)) ([1d9db4f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1d9db4f))
* **internal:** minor options / compat functions updates ([#592](https://github.com/anthropics/anthropic-sdk-python/issues/592)) ([d41a880](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d41a880))
* **internal:** update mypy ([#584](https://github.com/anthropics/anthropic-sdk-python/issues/584)) ([0a0edce](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0a0edce))

## 0.31.0 (2024-07-10)

Full Changelog: [v0.30.1...v0.31.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.30.1...v0.31.0)

### Features

* **client:** make request-id header more accessible ([#581](https://github.com/anthropics/anthropic-sdk-python/issues/581)) ([130d470](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/130d470))
* **vertex:** add copy and with_options ([#578](https://github.com/anthropics/anthropic-sdk-python/issues/578)) ([fcd425f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fcd425f))

### Bug Fixes

* **client:** always respect content-type multipart/form-data if provided ([#574](https://github.com/anthropics/anthropic-sdk-python/issues/574)) ([6051763](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6051763))
* **streaming/messages:** more robust event type construction ([#576](https://github.com/anthropics/anthropic-sdk-python/issues/576)) ([98e2075](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/98e2075))
* **types:** allow arbitrary types in image block param ([#582](https://github.com/anthropics/anthropic-sdk-python/issues/582)) ([ebd6590](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ebd6590))
* Updated doc typo ([17be06b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/17be06b))
* **vertex:** avoid credentials refresh on every request ([#575](https://github.com/anthropics/anthropic-sdk-python/issues/575)) ([37bd433](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/37bd433))

### Chores

* **ci:** update rye to v0.35.0 ([#577](https://github.com/anthropics/anthropic-sdk-python/issues/577)) ([e271d69](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e271d69))
* **internal:** add helper method for constructing `BaseModel`s ([#572](https://github.com/anthropics/anthropic-sdk-python/issues/572)) ([8e626ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8e626ac))
* **internal:** fix formatting ([a912917](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a912917))
* **internal:** minor request options handling changes ([#580](https://github.com/anthropics/anthropic-sdk-python/issues/580)) ([d1dcf42](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d1dcf42))

## 0.30.1 (2024-07-01)

Full Changelog: [v0.30.0...v0.30.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.30.0...v0.30.1)

### Bug Fixes

* **build:** include more files in sdist builds ([#559](https://github.com/anthropics/anthropic-sdk-python/issues/559)) ([9170d08](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9170d08))

### Chores

* **deps:** bump anyio to v4.4.0 ([#562](https://github.com/anthropics/anthropic-sdk-python/issues/562)) ([70fc936](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/70fc936))
* gitignore test server logs ([#567](https://github.com/anthropics/anthropic-sdk-python/issues/567)) ([f7b9283](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f7b9283))
* **internal:** add reflection helper function ([#565](https://github.com/anthropics/anthropic-sdk-python/issues/565)) ([9483573](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9483573))
* **internal:** add rich as a dev dependency ([#568](https://github.com/anthropics/anthropic-sdk-python/issues/568)) ([07903ac](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/07903ac))

## 0.30.0 (2024-06-26)

Full Changelog: [v0.29.2...v0.30.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.29.2...v0.30.0)

### Features

* **vertex:** add credentials argument ([#542](https://github.com/anthropics/anthropic-sdk-python/issues/542)) ([3bfb2ea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3bfb2ea))

## 0.29.2 (2024-06-26)

Full Changelog: [v0.29.1...v0.29.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.29.1...v0.29.2)

### Bug Fixes

* temporarily patch upstream version to fix broken release flow ([#555](https://github.com/anthropics/anthropic-sdk-python/issues/555)) ([5471710](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5471710))

## 0.29.1 (2024-06-25)

Full Changelog: [v0.29.0...v0.29.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.29.0...v0.29.1)

### Bug Fixes

* **api:** add string to tool result block ([#554](https://github.com/anthropics/anthropic-sdk-python/issues/554)) ([f283b4e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f283b4e))
* **docs:** fix link to advanced python httpx docs ([#550](https://github.com/anthropics/anthropic-sdk-python/issues/550)) ([474ff7c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/474ff7c))

## 0.29.0 (2024-06-20)

Full Changelog: [v0.28.1...v0.29.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.28.1...v0.29.0)

### Features

* **api:** add new claude-3-5-sonnet-20240620 model ([#545](https://github.com/anthropics/anthropic-sdk-python/issues/545)) ([5ea6b18](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5ea6b18))

### Bug Fixes

* **client/async:** avoid blocking io call for platform headers ([#544](https://github.com/anthropics/anthropic-sdk-python/issues/544)) ([3c2b75f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3c2b75f))

### Chores

* **internal:** add a `default_query` method ([#540](https://github.com/anthropics/anthropic-sdk-python/issues/540)) ([0253ebc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0253ebc))

## 0.28.1 (2024-06-14)

Full Changelog: [v0.28.0...v0.28.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.28.0...v0.28.1)

### Documentation

* **readme:** tool use is no longer in beta ([d2be3c0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d2be3c0))

## 0.28.0 (2024-05-30)

Full Changelog: [v0.27.0...v0.28.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.27.0...v0.28.0)

### ⚠ BREAKING CHANGES

* **streaming:** remove old event_handler API ([#532](https://github.com/anthropics/anthropic-sdk-python/issues/532))

### Refactors

* **streaming:** remove old event_handler API ([#532](https://github.com/anthropics/anthropic-sdk-python/issues/532)) ([d9acfd4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d9acfd4))

## 0.27.0 (2024-05-30)

Full Changelog: [v0.26.2...v0.27.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.26.2...v0.27.0)

### Features

* **api:** tool use is GA and available on 3P ([#530](https://github.com/anthropics/anthropic-sdk-python/issues/530)) ([ad7adbd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ad7adbd))
* **streaming/messages:** refactor to event iterator structure ([997af69](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/997af69))
* **streaming/tools:** refactor to event iterator structure ([bdcc283](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bdcc283))
* **streaming:** add tools support ([9f00950](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9f00950))

### Bug Fixes

* **beta:** streaming breakage due to breaking change in dependency ([afe3c87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/afe3c87))

### Chores

* add missing __all__ definitions ([#526](https://github.com/anthropics/anthropic-sdk-python/issues/526)) ([5021787](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5021787))
* **examples:** update tools ([56edecc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/56edecc))
* **formatting:** misc fixups ([fbad5a0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fbad5a0))
* **internal:** fix lint issues in tests ([d857640](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d857640))
* **internal:** update bootstrap script ([#527](https://github.com/anthropics/anthropic-sdk-python/issues/527)) ([93ae152](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/93ae152))
* **internal:** update some references to rye-up.com ([00e34e7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00e34e7))
* **tests:** ensure messages.create() and messages.stream() stay in sync ([52bd67b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/52bd67b))

### Documentation

* **helpers:** mention input json event ([02d482c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/02d482c))
* **helpers:** update for new event iterator ([26f9533](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/26f9533))

### Refactors

* **api:** add Raw prefix to API stream event type names ([#529](https://github.com/anthropics/anthropic-sdk-python/issues/529)) ([bb62980](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bb62980))

## 0.26.2 (2024-05-27)

Full Changelog: [v0.26.1...v0.26.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.26.1...v0.26.2)

### Bug Fixes

* **vertex:** don't error if project_id couldn't be loaded if it was already explicitly given ([#513](https://github.com/anthropics/anthropic-sdk-python/issues/513)) ([e7159d8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e7159d8))

### Chores

* **ci:** update rye install location ([#516](https://github.com/anthropics/anthropic-sdk-python/issues/516)) ([a6e347a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a6e347a))
* **ci:** update rye install location ([#518](https://github.com/anthropics/anthropic-sdk-python/issues/518)) ([5122420](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5122420))
* **internal:** bump pyright ([196e4b0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/196e4b0))
* **internal:** remove unused __events stream property ([472b831](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/472b831))
* **internal:** restructure streaming implementation to use composition ([b1a1c03](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b1a1c03))
* **messages:** add back-compat for isinstance() checks ([7794bcb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7794bcb))
* **tests:** fix lints ([#521](https://github.com/anthropics/anthropic-sdk-python/issues/521)) ([d96fc53](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d96fc53))

### Documentation

* **contributing:** update references to rye-up.com ([6486898](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6486898))

## 0.26.1 (2024-05-21)

Full Changelog: [v0.26.0...v0.26.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.26.0...v0.26.1)

### Chores

* **docs:** fix typo ([#511](https://github.com/anthropics/anthropic-sdk-python/issues/511)) ([d7401bd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d7401bd))
* **tools:** rely on pydantic's JSON parser instead of pydantic ([#510](https://github.com/anthropics/anthropic-sdk-python/issues/510)) ([8e7edca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8e7edca))

## 0.26.0 (2024-05-16)

Full Changelog: [v0.25.9...v0.26.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.9...v0.26.0)

### Features

* **api:** add `tool_choice` param, image block params inside `tool_result.content`, and streaming for `tool_use` blocks ([#502](https://github.com/anthropics/anthropic-sdk-python/issues/502)) ([e0bc274](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e0bc274))

### Chores

* **internal:** minor formatting changes ([#500](https://github.com/anthropics/anthropic-sdk-python/issues/500)) ([8b32558](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8b32558))

## 0.25.9 (2024-05-14)

Full Changelog: [v0.25.8...v0.25.9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.8...v0.25.9)

### Bug Fixes

* **types:** correct type for InputSchema ([#498](https://github.com/anthropics/anthropic-sdk-python/issues/498)) ([b86936c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b86936c))

### Chores

* **docs:** add SECURITY.md ([#493](https://github.com/anthropics/anthropic-sdk-python/issues/493)) ([d5cba46](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d5cba46))
* **internal:** add slightly better logging to scripts ([#497](https://github.com/anthropics/anthropic-sdk-python/issues/497)) ([acb0149](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/acb0149))
* **internal:** bump pydantic dependency ([#495](https://github.com/anthropics/anthropic-sdk-python/issues/495)) ([00cd840](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00cd840))
* **types:** add union discriminator metadata ([#491](https://github.com/anthropics/anthropic-sdk-python/issues/491)) ([95544a9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/95544a9))

## 0.25.8 (2024-05-07)

Full Changelog: [v0.25.7...v0.25.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.7...v0.25.8)

### Chores

* **client:** log response headers in debug mode ([#480](https://github.com/anthropics/anthropic-sdk-python/issues/480)) ([d1c4d14](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d1c4d14))
* **internal:** add link to openapi spec ([#484](https://github.com/anthropics/anthropic-sdk-python/issues/484)) ([876cd0d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/876cd0d))
* **internal:** add scripts/test, scripts/mock and add ci job ([#486](https://github.com/anthropics/anthropic-sdk-python/issues/486)) ([6111fe8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6111fe8))
* **internal:** bump prism version ([#487](https://github.com/anthropics/anthropic-sdk-python/issues/487)) ([98fb3e6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/98fb3e6))

### Documentation

* **readme:** fix misleading timeout example value ([#489](https://github.com/anthropics/anthropic-sdk-python/issues/489)) ([b465bce](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b465bce))

## 0.25.7 (2024-04-29)

Full Changelog: [v0.25.6...v0.25.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.6...v0.25.7)

### Bug Fixes

* **docs:** doc improvements ([#472](https://github.com/anthropics/anthropic-sdk-python/issues/472)) ([1b6d4e2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1b6d4e2))

### Chores

* **internal:** minor reformatting ([#478](https://github.com/anthropics/anthropic-sdk-python/issues/478)) ([de4b2e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/de4b2e0))
* **internal:** reformat imports ([#477](https://github.com/anthropics/anthropic-sdk-python/issues/477)) ([553e955](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/553e955))
* **internal:** restructure imports ([#470](https://github.com/anthropics/anthropic-sdk-python/issues/470)) ([49e0044](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/49e0044))
* **internal:** update test helper function ([#476](https://github.com/anthropics/anthropic-sdk-python/issues/476)) ([f46e454](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f46e454))
* **internal:** use actions/checkout@v4 for codeflow ([#474](https://github.com/anthropics/anthropic-sdk-python/issues/474)) ([8b18b52](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8b18b52))
* **tests:** rename test file ([#473](https://github.com/anthropics/anthropic-sdk-python/issues/473)) ([5b8261c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5b8261c))

## 0.25.6 (2024-04-18)

Full Changelog: [v0.25.5...v0.25.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.5...v0.25.6)

### Chores

* **internal:** bump pyright to 1.1.359 ([#466](https://github.com/anthropics/anthropic-sdk-python/issues/466)) ([8088160](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8088160))

## 0.25.5 (2024-04-17)

Full Changelog: [v0.25.4...v0.25.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.4...v0.25.5)

### Chores

* **internal:** ban usage of lru_cache ([#464](https://github.com/anthropics/anthropic-sdk-python/issues/464)) ([dc8ca22](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dc8ca22))

## 0.25.4 (2024-04-17)

Full Changelog: [v0.25.3...v0.25.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.3...v0.25.4)

### Bug Fixes

* **bedrock:** correct auth implementation ([#462](https://github.com/anthropics/anthropic-sdk-python/issues/462)) ([2f456f5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2f456f5))

## 0.25.3 (2024-04-17)

Full Changelog: [v0.25.2...v0.25.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.2...v0.25.3)

### Chores

* **bedrock:** cache boto sessions ([#455](https://github.com/anthropics/anthropic-sdk-python/issues/455)) ([d58adef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d58adef))

## 0.25.2 (2024-04-15)

Full Changelog: [v0.25.1...v0.25.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.1...v0.25.2)

### Chores

* **internal:** formatting ([#452](https://github.com/anthropics/anthropic-sdk-python/issues/452)) ([8ac016b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8ac016b))

## 0.25.1 (2024-04-11)

Full Changelog: [v0.25.0...v0.25.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.25.0...v0.25.1)

### Chores

* fix typo ([#449](https://github.com/anthropics/anthropic-sdk-python/issues/449)) ([420a6c5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/420a6c5))

## 0.25.0 (2024-04-09)

Full Changelog: [v0.24.0...v0.25.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.24.0...v0.25.0)

### Features

* **bedrock:** add `copy` / `with_options` to bedrock client ([8af7c41](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8af7c41))

### Chores

* unknown commit message ([8af7c41](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8af7c41))

## 0.24.0 (2024-04-09)

Full Changelog: [v0.23.1...v0.24.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.23.1...v0.24.0)

### Features

* **client:** add DefaultHttpxClient and DefaultAsyncHttpxClient ([#444](https://github.com/anthropics/anthropic-sdk-python/issues/444)) ([51d2427](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/51d2427))
* **models:** add to_dict & to_json helper methods ([#446](https://github.com/anthropics/anthropic-sdk-python/issues/446)) ([6709f58](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6709f58))

## 0.23.1 (2024-04-04)

Full Changelog: [v0.23.0...v0.23.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.23.0...v0.23.1)

### Documentation

* **readme:** mention tool use ([#441](https://github.com/anthropics/anthropic-sdk-python/issues/441)) ([e6cd916](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e6cd916))

## 0.23.0 (2024-04-04)

Full Changelog: [v0.22.1...v0.23.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.22.1...v0.23.0)

### Features

* **api:** tool use beta ([#438](https://github.com/anthropics/anthropic-sdk-python/issues/438)) ([5e35ffe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e35ffe))

## 0.22.1 (2024-04-04)

Full Changelog: [v0.22.0...v0.22.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.22.0...v0.22.1)

### Bug Fixes

* **types:** correctly mark type as a required property in requests ([#435](https://github.com/anthropics/anthropic-sdk-python/issues/435)) ([efc35ec](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/efc35ec))

### Chores

* **types:** consistent naming for text block types ([#437](https://github.com/anthropics/anthropic-sdk-python/issues/437)) ([e979fe1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e979fe1))

## 0.22.0 (2024-04-04)

Full Changelog: [v0.21.3...v0.22.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.21.3...v0.22.0)

### Features

* **client:** increase default HTTP max_connections to 1000 and max_keepalive_connections to 100 ([#428](https://github.com/anthropics/anthropic-sdk-python/issues/428)) ([9a43940](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9a43940))
* **package:** export default constants ([#423](https://github.com/anthropics/anthropic-sdk-python/issues/423)) ([0d694e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0d694e1))

### Bug Fixes

* **client:** correct logic for line decoding in streaming ([#433](https://github.com/anthropics/anthropic-sdk-python/issues/433)) ([6bf9379](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6bf9379))
* **project:** use absolute github links on PyPi ([#427](https://github.com/anthropics/anthropic-sdk-python/issues/427)) ([cbd8b1c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cbd8b1c))
* revert regression with 3.7 support ([#419](https://github.com/anthropics/anthropic-sdk-python/issues/419)) ([fa21f36](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fa21f36))
* **streaming:** correct accumulation of output tokens ([#426](https://github.com/anthropics/anthropic-sdk-python/issues/426)) ([b50ed05](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b50ed05))

### Chores

* **client:** validate that max_retries is not None ([#430](https://github.com/anthropics/anthropic-sdk-python/issues/430)) ([31b2a2f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/31b2a2f))
* **internal:** bump dependencies ([#421](https://github.com/anthropics/anthropic-sdk-python/issues/421)) ([30e8031](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/30e8031))
* **internal:** defer model build for import latency ([#431](https://github.com/anthropics/anthropic-sdk-python/issues/431)) ([51d4783](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/51d4783))
* **internal:** formatting change ([#415](https://github.com/anthropics/anthropic-sdk-python/issues/415)) ([1474f44](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1474f44))

### Documentation

* **contributing:** fix typo ([#414](https://github.com/anthropics/anthropic-sdk-python/issues/414)) ([aeaf995](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aeaf995))
* **readme:** change undocumented params wording ([#429](https://github.com/anthropics/anthropic-sdk-python/issues/429)) ([1336958](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1336958))

## 0.21.3 (2024-03-21)

Full Changelog: [v0.21.2...v0.21.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.21.2...v0.21.3)

### Bug Fixes

* **types:** correct typo claude-2.1' to claude-2.1 ([#400](https://github.com/anthropics/anthropic-sdk-python/issues/400)) ([7f82aa3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7f82aa3))
* **types:** correct typo claude-2.1' to claude-2.1 ([#413](https://github.com/anthropics/anthropic-sdk-python/issues/413)) ([bb1aebe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bb1aebe))

## 0.21.2 (2024-03-21)

Full Changelog: [v0.21.1...v0.21.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.21.1...v0.21.2)

### Documentation

* **readme:** consistent use of sentence case in headings ([#405](https://github.com/anthropics/anthropic-sdk-python/issues/405)) ([495ca87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/495ca87))
* **readme:** document how to make undocumented requests ([#407](https://github.com/anthropics/anthropic-sdk-python/issues/407)) ([b046d0d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b046d0d))

## 0.21.1 (2024-03-20)

Full Changelog: [v0.21.0...v0.21.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.21.0...v0.21.1)

### Chores

* **internal:** loosen input type for util function ([#402](https://github.com/anthropics/anthropic-sdk-python/issues/402)) ([9a6ca55](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9a6ca55))

## 0.21.0 (2024-03-19)

Full Changelog: [v0.20.0...v0.21.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.20.0...v0.21.0)

### Features

* **vertex:** api is no longer in private beta ([#399](https://github.com/anthropics/anthropic-sdk-python/issues/399)) ([4cb0e64](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4cb0e64))

### Performance Improvements

* cache TypeAdapters ([#396](https://github.com/anthropics/anthropic-sdk-python/issues/396)) ([a902c47](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a902c47))

### Chores

* **internal:** update generated pragma comment ([#398](https://github.com/anthropics/anthropic-sdk-python/issues/398)) ([330b61e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/330b61e))

### Documentation

* fix typo in CONTRIBUTING.md ([#397](https://github.com/anthropics/anthropic-sdk-python/issues/397)) ([d46629f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d46629f))
* **helpers:** fix example code ([#391](https://github.com/anthropics/anthropic-sdk-python/issues/391)) ([9fe0c8b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9fe0c8b))

## 0.20.0 (2024-03-13)

Full Changelog: [v0.19.2...v0.20.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.19.2...v0.20.0)

### Features

* **api:** add haiku model ([#390](https://github.com/anthropics/anthropic-sdk-python/issues/390)) ([43b57fc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/43b57fc))

### Documentation

* **readme:** mention vertex API ([#388](https://github.com/anthropics/anthropic-sdk-python/issues/388)) ([8bb6b98](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8bb6b98))

## 0.19.2 (2024-03-11)

Full Changelog: [v0.19.1...v0.19.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.19.1...v0.19.2)

### Bug Fixes

* **vertex:** use correct auth scopes ([#385](https://github.com/anthropics/anthropic-sdk-python/issues/385)) ([e4de056](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e4de056))

### Chores

* export NOT_GIVEN sentinel value ([#379](https://github.com/anthropics/anthropic-sdk-python/issues/379)) ([ba127bc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ba127bc))
* **internal:** improve deserialisation of discriminated unions ([#386](https://github.com/anthropics/anthropic-sdk-python/issues/386)) ([fbc7e0b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fbc7e0b))
* **internal:** support parsing Annotated types ([#377](https://github.com/anthropics/anthropic-sdk-python/issues/377)) ([f44efd5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f44efd5))

## 0.19.1 (2024-03-06)

Full Changelog: [v0.19.0...v0.19.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.19.0...v0.19.1)

### Chores

* **internal:** add core support for deserializing into number response ([#373](https://github.com/anthropics/anthropic-sdk-python/issues/373)) ([b62c422](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b62c422))

## 0.19.0 (2024-03-06)

Full Changelog: [v0.18.1...v0.19.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.18.1...v0.19.0)

### Features

* **api:** add enum to model param for message ([#371](https://github.com/anthropics/anthropic-sdk-python/issues/371)) ([f96765f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f96765f))

### Chores

* **client:** improve error message for invalid http_client argument ([#367](https://github.com/anthropics/anthropic-sdk-python/issues/367)) ([2f4df72](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2f4df72))

### Documentation

* **readme:** fix async streaming snippet ([#366](https://github.com/anthropics/anthropic-sdk-python/issues/366)) ([37c469d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/37c469d))

## 0.18.1 (2024-03-04)

Full Changelog: [v0.18.0...v0.18.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.18.0...v0.18.1)

### Chores

* **readme:** update bedrock example ([#364](https://github.com/anthropics/anthropic-sdk-python/issues/364)) ([81e4d10](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/81e4d10))

## 0.18.0 (2024-03-04)

Full Changelog: [v0.17.0...v0.18.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.17.0...v0.18.0)

### Features

* **bedrock:** add messages API ([#362](https://github.com/anthropics/anthropic-sdk-python/issues/362)) ([5409be9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5409be9))

### Chores

* remove old examples ([4895381](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4895381))

## 0.17.0 (2024-03-04)

Full Changelog: [v0.16.0...v0.17.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.16.0...v0.17.0)

### Features

* **messages:** add support for image inputs ([#359](https://github.com/anthropics/anthropic-sdk-python/issues/359)) ([579f013](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/579f013))

### Chores

* **client:** use anyio.sleep instead of asyncio.sleep ([#351](https://github.com/anthropics/anthropic-sdk-python/issues/351)) ([2778a22](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2778a22))
* **docs:** mention install from git repo ([#356](https://github.com/anthropics/anthropic-sdk-python/issues/356)) ([9d503ba](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9d503ba))
* **docs:** remove references to old bedrock package ([#344](https://github.com/anthropics/anthropic-sdk-python/issues/344)) ([3323883](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3323883))
* **internal:** bump pyright ([#350](https://github.com/anthropics/anthropic-sdk-python/issues/350)) ([ee0161c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ee0161c))
* **internal:** bump rye to v0.24.0 ([#348](https://github.com/anthropics/anthropic-sdk-python/issues/348)) ([be8597b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/be8597b))
* **internal:** improve bedrock streaming setup ([#354](https://github.com/anthropics/anthropic-sdk-python/issues/354)) ([2b55c68](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2b55c68))
* **internal:** refactor release environment script ([#347](https://github.com/anthropics/anthropic-sdk-python/issues/347)) ([a87443a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a87443a))
* **internal:** split up transforms into sync / async ([#357](https://github.com/anthropics/anthropic-sdk-python/issues/357)) ([f55ee71](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f55ee71))
* **internal:** support more input types ([#358](https://github.com/anthropics/anthropic-sdk-python/issues/358)) ([35b0347](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/35b0347))
* **internal:** update deps ([#349](https://github.com/anthropics/anthropic-sdk-python/issues/349)) ([ab82b2d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ab82b2d))

### Documentation

* **contributing:** improve wording ([#355](https://github.com/anthropics/anthropic-sdk-python/issues/355)) ([f9093a0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f9093a0))

### Refactors

* **api:** mark completions API as legacy ([#346](https://github.com/anthropics/anthropic-sdk-python/issues/346)) ([2bb25a1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2bb25a1))

## 0.16.0 (2024-02-13)

Full Changelog: [v0.15.1...v0.16.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.15.1...v0.16.0)

### Features

* **api:** messages is generally available ([#343](https://github.com/anthropics/anthropic-sdk-python/issues/343)) ([f682594](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f682594))
* **messages:** allow message response in params ([#339](https://github.com/anthropics/anthropic-sdk-python/issues/339)) ([86c63f0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/86c63f0))

### Documentation

* add CONTRIBUTING.md ([#340](https://github.com/anthropics/anthropic-sdk-python/issues/340)) ([78469ad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/78469ad))

## 0.15.1 (2024-02-07)

Full Changelog: [v0.15.0...v0.15.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.15.0...v0.15.1)

### Bug Fixes

* prevent crash when platform.architecture() is not allowed ([#334](https://github.com/anthropics/anthropic-sdk-python/issues/334)) ([fefb5c1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fefb5c1))
* **types:** loosen most List params types to Iterable ([#338](https://github.com/anthropics/anthropic-sdk-python/issues/338)) ([6e7761b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6e7761b))

### Chores

* **internal:** add lint command ([#337](https://github.com/anthropics/anthropic-sdk-python/issues/337)) ([2ebaf1d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2ebaf1d))
* **internal:** support serialising iterable types ([#336](https://github.com/anthropics/anthropic-sdk-python/issues/336)) ([ea3ed7b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ea3ed7b))

## 0.15.0 (2024-02-02)

Full Changelog: [v0.14.1...v0.15.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.14.1...v0.15.0)

### Features

* **api:** add new usage response fields ([#332](https://github.com/anthropics/anthropic-sdk-python/issues/332)) ([554098e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/554098e))

## 0.14.1 (2024-02-02)

Full Changelog: [v0.14.0...v0.14.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.14.0...v0.14.1)

### Chores

* **interal:** make link to api.md relative ([#330](https://github.com/anthropics/anthropic-sdk-python/issues/330)) ([e393317](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e393317))

## 0.14.0 (2024-01-31)

Full Changelog: [v0.13.0...v0.14.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.13.0...v0.14.0)

### Features

* **bedrock:** include bedrock SDK ([#328](https://github.com/anthropics/anthropic-sdk-python/issues/328)) ([a03f21f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a03f21f))

## 0.13.0 (2024-01-30)

Full Changelog: [v0.12.0...v0.13.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.12.0...v0.13.0)

### Features

* **client:** support parsing custom response types ([#325](https://github.com/anthropics/anthropic-sdk-python/issues/325)) ([416633f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/416633f))

### Chores

* **internal:** cast type in mocked test ([#326](https://github.com/anthropics/anthropic-sdk-python/issues/326)) ([fd22d8e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fd22d8e))
* **internal:** enable ruff type checking misuse lint rule ([#324](https://github.com/anthropics/anthropic-sdk-python/issues/324)) ([6587598](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6587598))
* **internal:** support multipart data with overlapping keys ([#322](https://github.com/anthropics/anthropic-sdk-python/issues/322)) ([9ecab60](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9ecab60))
* **internal:** support pre-release versioning ([#327](https://github.com/anthropics/anthropic-sdk-python/issues/327)) ([78b1bfe](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/78b1bfe))

## 0.12.0 (2024-01-25)

Full Changelog: [v0.11.0...v0.12.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.11.0...v0.12.0)

### Features

* **client:** enable follow redirects by default ([#320](https://github.com/anthropics/anthropic-sdk-python/issues/320)) ([9959c32](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9959c32))

## 0.11.0 (2024-01-23)

Full Changelog: [v0.10.0...v0.11.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.10.0...v0.11.0)

### Features

* **vertex:** add support for google vertex ([#319](https://github.com/anthropics/anthropic-sdk-python/issues/319)) ([5324415](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5324415))

### Chores

* **internal:** add internal helpers ([#316](https://github.com/anthropics/anthropic-sdk-python/issues/316)) ([8c75cdf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8c75cdf))
* **internal:** update resource client type ([#318](https://github.com/anthropics/anthropic-sdk-python/issues/318)) ([bdd8d84](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bdd8d84))

## 0.10.0 (2024-01-18)

Full Changelog: [v0.9.0...v0.10.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.9.0...v0.10.0)

### Features

* **client:** add support for streaming raw responses ([#307](https://github.com/anthropics/anthropic-sdk-python/issues/307)) ([f295982](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f295982))

### Bug Fixes

* **ci:** ignore stainless-app edits to release PR title ([#315](https://github.com/anthropics/anthropic-sdk-python/issues/315)) ([69e8b03](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/69e8b03))

### Chores

* add write_to_file binary helper method ([#309](https://github.com/anthropics/anthropic-sdk-python/issues/309)) ([8ac7988](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8ac7988))
* **client:** improve debug logging for failed requests ([#303](https://github.com/anthropics/anthropic-sdk-python/issues/303)) ([5e58c25](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e58c25))
* **internal:** fix typing util function ([#310](https://github.com/anthropics/anthropic-sdk-python/issues/310)) ([3671aa6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3671aa6))
* **internal:** remove redundant client test ([#311](https://github.com/anthropics/anthropic-sdk-python/issues/311)) ([d7140f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d7140f7))
* **internal:** share client instances between all tests ([#314](https://github.com/anthropics/anthropic-sdk-python/issues/314)) ([ccf731b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ccf731b))
* **internal:** speculative retry-after-ms support ([#312](https://github.com/anthropics/anthropic-sdk-python/issues/312)) ([4b27da9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4b27da9))
* **internal:** updates to proxy helper ([#308](https://github.com/anthropics/anthropic-sdk-python/issues/308)) ([a0b3cdb](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a0b3cdb))
* lazy load raw resource class properties ([#313](https://github.com/anthropics/anthropic-sdk-python/issues/313)) ([b13f824](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b13f824))

### Documentation

* **readme:** improve api reference ([#306](https://github.com/anthropics/anthropic-sdk-python/issues/306)) ([c3ab836](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c3ab836))

## 0.9.0 (2024-01-08)

Full Changelog: [v0.8.1...v0.9.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.8.1...v0.9.0)

### Features

* add `None` default value to nullable response properties ([#299](https://github.com/anthropics/anthropic-sdk-python/issues/299)) ([da423db](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/da423db))

### Bug Fixes

* **client:** correctly use custom http client auth ([#296](https://github.com/anthropics/anthropic-sdk-python/issues/296)) ([6289d6e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6289d6e))

### Chores

* add .keep files for examples and custom code directories ([#302](https://github.com/anthropics/anthropic-sdk-python/issues/302)) ([73a07ea](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/73a07ea))
* **internal:** loosen type var restrictions ([#301](https://github.com/anthropics/anthropic-sdk-python/issues/301)) ([5e5e1e7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e5e1e7))
* **internal:** replace isort with ruff ([#298](https://github.com/anthropics/anthropic-sdk-python/issues/298)) ([7c60904](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7c60904))
* use property declarations for resource members ([#300](https://github.com/anthropics/anthropic-sdk-python/issues/300)) ([8671297](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8671297))

## 0.8.1 (2023-12-22)

Full Changelog: [v0.8.0...v0.8.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.8.0...v0.8.1)

### Chores

* **internal:** add bin script ([#292](https://github.com/anthropics/anthropic-sdk-python/issues/292)) ([ba2953d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ba2953d))
* **internal:** fix typos ([#287](https://github.com/anthropics/anthropic-sdk-python/issues/287)) ([4ffbcdf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4ffbcdf))
* **internal:** use ruff instead of black for formatting ([#294](https://github.com/anthropics/anthropic-sdk-python/issues/294)) ([1753887](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1753887))
* **package:** bump minimum typing-extensions to 4.7 ([#290](https://github.com/anthropics/anthropic-sdk-python/issues/290)) ([9ec5c57](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9ec5c57))

### Documentation

* **messages:** improvements to helpers reference + typos ([#291](https://github.com/anthropics/anthropic-sdk-python/issues/291)) ([d18a895](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d18a895))
* **readme:** remove old migration guide ([#289](https://github.com/anthropics/anthropic-sdk-python/issues/289)) ([eec4574](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/eec4574))

## 0.8.0 (2023-12-19)

Full Changelog: [v0.7.8...v0.8.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.8...v0.8.0)

### Features

* **api:** add messages endpoint with streaming helpers ([#286](https://github.com/anthropics/anthropic-sdk-python/issues/286)) ([c464b87](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c464b87))

### Chores

* **ci:** run release workflow once per day ([#282](https://github.com/anthropics/anthropic-sdk-python/issues/282)) ([3a23912](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3a23912))
* **client:** only import tokenizers when needed ([#284](https://github.com/anthropics/anthropic-sdk-python/issues/284)) ([b9e38b2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b9e38b2))
* **streaming:** update constructor to use direct client names ([#285](https://github.com/anthropics/anthropic-sdk-python/issues/285)) ([0c55c84](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0c55c84))

## 0.7.8 (2023-12-12)

Full Changelog: [v0.7.7...v0.7.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.7...v0.7.8)

### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#275](https://github.com/anthropics/anthropic-sdk-python/issues/275)) ([5e51ebd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e51ebd))
* **client:** correct base_url setter implementation ([#265](https://github.com/anthropics/anthropic-sdk-python/issues/265)) ([29d0c8b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/29d0c8b))
* **client:** ensure retried requests are closed ([#261](https://github.com/anthropics/anthropic-sdk-python/issues/261)) ([5d9aa75](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5d9aa75))
* **errors:** properly assign APIError.body ([#274](https://github.com/anthropics/anthropic-sdk-python/issues/274)) ([342846f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/342846f))

### Chores

* **internal:** enable more lint rules ([#273](https://github.com/anthropics/anthropic-sdk-python/issues/273)) ([0ac62bc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0ac62bc))
* **internal:** reformat imports ([#270](https://github.com/anthropics/anthropic-sdk-python/issues/270)) ([dc55724](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dc55724))
* **internal:** reformat imports ([#272](https://github.com/anthropics/anthropic-sdk-python/issues/272)) ([0d82ce4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0d82ce4))
* **internal:** remove unused file ([#264](https://github.com/anthropics/anthropic-sdk-python/issues/264)) ([1bfc69b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1bfc69b))
* **internal:** replace string concatenation with f-strings ([#263](https://github.com/anthropics/anthropic-sdk-python/issues/263)) ([f545c35](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f545c35))
* **internal:** update formatting ([#271](https://github.com/anthropics/anthropic-sdk-python/issues/271)) ([802ab59](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/802ab59))
* **package:** lift anyio v4 restriction ([#266](https://github.com/anthropics/anthropic-sdk-python/issues/266)) ([a217e99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a217e99))

### Documentation

* update examples to show claude-2.1 ([#276](https://github.com/anthropics/anthropic-sdk-python/issues/276)) ([8f562f4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8f562f4))

### Refactors

* **client:** simplify cleanup ([#278](https://github.com/anthropics/anthropic-sdk-python/issues/278)) ([3611ae2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3611ae2))
* simplify internal error handling ([#279](https://github.com/anthropics/anthropic-sdk-python/issues/279)) ([993b51a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/993b51a))

## 0.7.7 (2023-11-29)

Full Changelog: [v0.7.6...v0.7.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.6...v0.7.7)

### Chores

* **internal:** add tests for proxy change ([#260](https://github.com/anthropics/anthropic-sdk-python/issues/260)) ([3b52136](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3b52136))
* **internal:** updates to proxy helper ([#258](https://github.com/anthropics/anthropic-sdk-python/issues/258)) ([94c4de8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/94c4de8))

## 0.7.6 (2023-11-28)

Full Changelog: [v0.7.5...v0.7.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.5...v0.7.6)

### Chores

* **deps:** bump mypy to v1.7.1 ([#256](https://github.com/anthropics/anthropic-sdk-python/issues/256)) ([02d4ed8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/02d4ed8))

## 0.7.5 (2023-11-24)

Full Changelog: [v0.7.4...v0.7.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.4...v0.7.5)

### Chores

* **internal:** revert recent options change ([#252](https://github.com/anthropics/anthropic-sdk-python/issues/252)) ([d60d5c3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d60d5c3))
* **internal:** send more detailed x-stainless headers ([#254](https://github.com/anthropics/anthropic-sdk-python/issues/254)) ([a268d4b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a268d4b))

## 0.7.4 (2023-11-23)

Full Changelog: [v0.7.3...v0.7.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.3...v0.7.4)

### Chores

* **internal:** options updates ([#248](https://github.com/anthropics/anthropic-sdk-python/issues/248)) ([5a3b236](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5a3b236))

## 0.7.3 (2023-11-21)

Full Changelog: [v0.7.2...v0.7.3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.2...v0.7.3)

### Bug Fixes

* **client:** attempt to parse unknown json content types ([#243](https://github.com/anthropics/anthropic-sdk-python/issues/243)) ([9fc275f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9fc275f))

### Chores

* **client:** improve copy method ([#246](https://github.com/anthropics/anthropic-sdk-python/issues/246)) ([c84563f](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c84563f))
* **package:** add license classifier metadata ([#247](https://github.com/anthropics/anthropic-sdk-python/issues/247)) ([500d0ca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/500d0ca))

## 0.7.2 (2023-11-17)

Full Changelog: [v0.7.1...v0.7.2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.1...v0.7.2)

### Chores

* **internal:** update type hint for helper function ([#241](https://github.com/anthropics/anthropic-sdk-python/issues/241)) ([3179104](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3179104))

## 0.7.1 (2023-11-16)

Full Changelog: [v0.7.0...v0.7.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.7.0...v0.7.1)

### Documentation

* **readme:** minor updates ([#238](https://github.com/anthropics/anthropic-sdk-python/issues/238)) ([c40c4e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c40c4e1))

## 0.7.0 (2023-11-15)

Full Changelog: [v0.6.0...v0.7.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.6.0...v0.7.0)

### Features

* **client:** support reading the base url from an env variable ([#237](https://github.com/anthropics/anthropic-sdk-python/issues/237)) ([dd91bfd](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dd91bfd))

### Bug Fixes

* **client:** correctly flush the stream response body ([#230](https://github.com/anthropics/anthropic-sdk-python/issues/230)) ([a60d543](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a60d543))
* **client:** retry if SSLWantReadError occurs in the async client ([#233](https://github.com/anthropics/anthropic-sdk-python/issues/233)) ([33b553a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/33b553a))
* **client:** serialise pydantic v1 default fields correctly in params ([#232](https://github.com/anthropics/anthropic-sdk-python/issues/232)) ([d5e70e8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d5e70e8))
* **models:** mark unknown fields as set in pydantic v1 ([#231](https://github.com/anthropics/anthropic-sdk-python/issues/231)) ([4ce7a1e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4ce7a1e))

### Chores

* **internal:** fix devcontainer interpeter path ([#235](https://github.com/anthropics/anthropic-sdk-python/issues/235)) ([7f92e25](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7f92e25))
* **internal:** fix typo in NotGiven docstring ([#234](https://github.com/anthropics/anthropic-sdk-python/issues/234)) ([ce5cccc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ce5cccc))

### Documentation

* fix code comment typo ([#236](https://github.com/anthropics/anthropic-sdk-python/issues/236)) ([7ef0464](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7ef0464))
* reword package description ([#228](https://github.com/anthropics/anthropic-sdk-python/issues/228)) ([c18e5ed](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c18e5ed))

## 0.6.0 (2023-11-08)

Full Changelog: [v0.5.1...v0.6.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.5.1...v0.6.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#205](https://github.com/anthropics/anthropic-sdk-python/issues/205)) ([c8a4119](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c8a4119))
* **client:** allow binary returns ([#217](https://github.com/anthropics/anthropic-sdk-python/issues/217)) ([159ddd6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/159ddd6))
* **client:** improve file upload types ([#204](https://github.com/anthropics/anthropic-sdk-python/issues/204)) ([d85d1e0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d85d1e0))
* **client:** support accessing raw response objects ([#211](https://github.com/anthropics/anthropic-sdk-python/issues/211)) ([ebe8e4a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ebe8e4a))
* **client:** support passing BaseModels to request params at runtime ([#218](https://github.com/anthropics/anthropic-sdk-python/issues/218)) ([9f04ea6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9f04ea6))
* **client:** support passing chunk size for binary responses ([#227](https://github.com/anthropics/anthropic-sdk-python/issues/227)) ([c88f01e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c88f01e))
* **client:** support passing httpx.Timeout to method timeout argument ([#222](https://github.com/anthropics/anthropic-sdk-python/issues/222)) ([ef58166](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ef58166))
* **github:** include a devcontainer setup ([#216](https://github.com/anthropics/anthropic-sdk-python/issues/216)) ([c9fee19](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c9fee19))
* **package:** add classifiers ([#214](https://github.com/anthropics/anthropic-sdk-python/issues/214)) ([380967e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/380967e))

### Bug Fixes

* **binaries:** don't synchronously block in astream_to_file ([#219](https://github.com/anthropics/anthropic-sdk-python/issues/219)) ([2a2a617](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2a2a617))
* prevent TypeError in Python 3.8 (ABC is not subscriptable) ([#221](https://github.com/anthropics/anthropic-sdk-python/issues/221)) ([893e885](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/893e885))

### Chores

* **docs:** fix github links ([#225](https://github.com/anthropics/anthropic-sdk-python/issues/225)) ([dfa9935](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dfa9935))
* **internal:** fix some typos ([#223](https://github.com/anthropics/anthropic-sdk-python/issues/223)) ([9038193](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9038193))
* **internal:** improve github devcontainer setup ([#226](https://github.com/anthropics/anthropic-sdk-python/issues/226)) ([3cd90ab](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3cd90ab))
* **internal:** minor restructuring of base client ([#213](https://github.com/anthropics/anthropic-sdk-python/issues/213)) ([60dc609](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/60dc609))
* **internal:** remove unused int/float conversion ([#220](https://github.com/anthropics/anthropic-sdk-python/issues/220)) ([a6bf20d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a6bf20d))
* **internal:** require explicit overrides ([#210](https://github.com/anthropics/anthropic-sdk-python/issues/210)) ([72f4339](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/72f4339))

### Documentation

* fix github links ([#215](https://github.com/anthropics/anthropic-sdk-python/issues/215)) ([8cbed15](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8cbed15))
* improve to dictionary example ([#207](https://github.com/anthropics/anthropic-sdk-python/issues/207)) ([5e32c20](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5e32c20))

## 0.5.1 (2023-10-20)

Full Changelog: [v0.5.0...v0.5.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.5.0...v0.5.1)

### Chores

* **internal:** bump mypy ([#203](https://github.com/anthropics/anthropic-sdk-python/issues/203)) ([aa9a67e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aa9a67e))
* **internal:** bump pyright ([#202](https://github.com/anthropics/anthropic-sdk-python/issues/202)) ([f96f5f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f96f5f7))
* **internal:** update gitignore ([#199](https://github.com/anthropics/anthropic-sdk-python/issues/199)) ([b92fa57](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/b92fa57))

## 0.5.0 (2023-10-18)

Full Changelog: [v0.4.1...v0.5.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.4.1...v0.5.0)

### Features

* **client:** support passing httpx.URL instances to base_url ([#197](https://github.com/anthropics/anthropic-sdk-python/issues/197)) ([fe61308](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/fe61308))

### Chores

* **internal:** improve publish script ([#196](https://github.com/anthropics/anthropic-sdk-python/issues/196)) ([7c92b90](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7c92b90))
* **internal:** migrate from Poetry to Rye ([#194](https://github.com/anthropics/anthropic-sdk-python/issues/194)) ([1dd605e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1dd605e))
* **internal:** update gitignore ([#198](https://github.com/anthropics/anthropic-sdk-python/issues/198)) ([4c210b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4c210b7))

## 0.4.1 (2023-10-16)

Full Changelog: [v0.4.0...v0.4.1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.4.0...v0.4.1)

### Bug Fixes

* **client:** accept io.IOBase instances in file params ([#190](https://github.com/anthropics/anthropic-sdk-python/issues/190)) ([5da5f0c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/5da5f0c))
* **streaming:** add additional overload for ambiguous stream param ([#185](https://github.com/anthropics/anthropic-sdk-python/issues/185)) ([794dc4d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/794dc4d))

### Chores

* **internal:** cleanup some redundant code ([#188](https://github.com/anthropics/anthropic-sdk-python/issues/188)) ([cb0bd8c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cb0bd8c))
* **internal:** enable lint rule ([#187](https://github.com/anthropics/anthropic-sdk-python/issues/187)) ([123b5c1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/123b5c1))

### Documentation

* organisation -&gt; organization (UK to US English) ([#192](https://github.com/anthropics/anthropic-sdk-python/issues/192)) ([901a330](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/901a330))

## 0.4.0 (2023-10-13)

Full Changelog: [v0.3.14...v0.4.0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.3.14...v0.4.0)

### Features

* **client:** add logging setup ([#177](https://github.com/anthropics/anthropic-sdk-python/issues/177)) ([a5f87ad](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a5f87ad))

### Bug Fixes

* **client:** correctly handle arguments with env vars ([#178](https://github.com/anthropics/anthropic-sdk-python/issues/178)) ([91a0e2a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/91a0e2a))

### Chores

* add case insensitive get header function ([#182](https://github.com/anthropics/anthropic-sdk-python/issues/182)) ([708fd02](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/708fd02))
* update comment ([#183](https://github.com/anthropics/anthropic-sdk-python/issues/183)) ([649d6f4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/649d6f4))
* update README ([#174](https://github.com/anthropics/anthropic-sdk-python/issues/174)) ([bb581b5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/bb581b5))

### Documentation

* minor readme reordering ([#180](https://github.com/anthropics/anthropic-sdk-python/issues/180)) ([92345e3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/92345e3))

### Refactors

* **test:** refactor authentication tests ([#175](https://github.com/anthropics/anthropic-sdk-python/issues/175)) ([c82da53](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/c82da53))

## 0.3.14 (2023-10-11)

Full Changelog: [v0.3.13...v0.3.14](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.3.13...v0.3.14)

### Features

* **client:** add forwards-compatible pydantic methods ([#171](https://github.com/anthropics/anthropic-sdk-python/issues/171)) ([4c5289e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/4c5289e))
* **client:** add support for passing in a httpx client ([#173](https://github.com/anthropics/anthropic-sdk-python/issues/173)) ([25046c4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/25046c4))
* **client:** handle retry-after header with a date format ([#168](https://github.com/anthropics/anthropic-sdk-python/issues/168)) ([afeabf1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/afeabf1))
* **client:** retry on 408 Request Timeout ([#155](https://github.com/anthropics/anthropic-sdk-python/issues/155)) ([46386f8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/46386f8))
* **package:** export a root error type ([#163](https://github.com/anthropics/anthropic-sdk-python/issues/163)) ([e7aa3e7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e7aa3e7))
* **types:** improve params type names ([#160](https://github.com/anthropics/anthropic-sdk-python/issues/160)) ([43544a6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/43544a6))

### Bug Fixes

* **client:** don't error by default for unexpected content types ([#161](https://github.com/anthropics/anthropic-sdk-python/issues/161)) ([76cfcf9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/76cfcf9))
* **client:** properly configure model set fields ([#154](https://github.com/anthropics/anthropic-sdk-python/issues/154)) ([da6ccb1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/da6ccb1))

### Chores

* **internal:** add helpers ([#156](https://github.com/anthropics/anthropic-sdk-python/issues/156)) ([00f5a19](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/00f5a19))
* **internal:** move error classes from _base_exceptions to _exceptions (⚠️ breaking) ([#162](https://github.com/anthropics/anthropic-sdk-python/issues/162)) ([329b307](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/329b307))
* **tests:** improve raw response test ([#166](https://github.com/anthropics/anthropic-sdk-python/issues/166)) ([8042473](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8042473))

### Documentation

* add some missing inline documentation ([#151](https://github.com/anthropics/anthropic-sdk-python/issues/151)) ([1f98257](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1f98257))
* update readme ([#172](https://github.com/anthropics/anthropic-sdk-python/issues/172)) ([351095b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/351095b))

## 0.3.13 (2023-09-11)

Full Changelog: [v0.3.12...v0.3.13](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.3.12...v0.3.13)

### Features

* **types:** de-duplicate nested streaming params types ([#141](https://github.com/anthropics/anthropic-sdk-python/issues/141)) ([f76f053](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f76f053))

### Bug Fixes

* **client:** properly handle optional file params ([#142](https://github.com/anthropics/anthropic-sdk-python/issues/142)) ([11196b7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/11196b7))

### Chores

* **internal:** add `pydantic.generics` import for compatibility ([#135](https://github.com/anthropics/anthropic-sdk-python/issues/135)) ([951446d](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/951446d))
* **internal:** minor restructuring ([#137](https://github.com/anthropics/anthropic-sdk-python/issues/137)) ([e601206](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e601206))
* **internal:** minor update ([#145](https://github.com/anthropics/anthropic-sdk-python/issues/145)) ([6a505ef](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6a505ef))
* **internal:** update base client ([#143](https://github.com/anthropics/anthropic-sdk-python/issues/143)) ([8e0dca4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8e0dca4))
* **internal:** update lock file ([#147](https://github.com/anthropics/anthropic-sdk-python/issues/147)) ([a72b5ca](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a72b5ca))
* **internal:** update pyright ([#149](https://github.com/anthropics/anthropic-sdk-python/issues/149)) ([9661f94](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9661f94))
* **internal:** updates ([#148](https://github.com/anthropics/anthropic-sdk-python/issues/148)) ([9f7fbbc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9f7fbbc))

### Documentation

* **readme:** add link to api.md ([#146](https://github.com/anthropics/anthropic-sdk-python/issues/146)) ([1fcb30a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1fcb30a))
* **readme:** reference pydantic helpers ([#138](https://github.com/anthropics/anthropic-sdk-python/issues/138)) ([ccaab99](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ccaab99))

## 0.3.12 (2023-08-29)

Full Changelog: [v0.3.11...v0.3.12](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/v0.3.11...v0.3.12)

### Chores

* **ci:** setup workflows to create releases and release PRs ([#130](https://github.com/anthropics/anthropic-sdk-python/issues/130)) ([8f1048b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/8f1048b))
* **internal:** use shared params references ([#133](https://github.com/anthropics/anthropic-sdk-python/issues/133)) ([feaf6aa](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/feaf6aa))

## [0.3.11](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.11) (2023-08-26)

### Documentation

* **readme:** make print statements in streaming examples flush ([#123](https://github.com/anthropics/anthropic-sdk-python/issues/123)) ([d24dfaf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d24dfaf))

### Chores

* **internal:** update anyio ([#125](https://github.com/anthropics/anthropic-sdk-python/issues/125)) ([34c7fa1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/34c7fa1))

## [0.3.10](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.10) (2023-08-16)

### Features

* add support for Pydantic v2 ([#121](https://github.com/anthropics/anthropic-sdk-python/issues/121)) ([cafa9be](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cafa9be))
* allow a default timeout to be set for clients ([#117](https://github.com/anthropics/anthropic-sdk-python/issues/117)) ([a115d2c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/a115d2c))

### Chores

* assign default reviewers to release PRs ([#119](https://github.com/anthropics/anthropic-sdk-python/issues/119)) ([029a9e1](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/029a9e1))
* **internal:** minor formatting change ([#120](https://github.com/anthropics/anthropic-sdk-python/issues/120)) ([7f2f54a](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7f2f54a))

## [0.3.9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.9) (2023-08-12)

### Features

* **docs:** remove extraneous space in examples ([#109](https://github.com/anthropics/anthropic-sdk-python/issues/109)) ([6d5c1f7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/6d5c1f7))

### Bug Fixes

* **docs:** correct async imports ([1ea1bf3](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1ea1bf3))

### Documentation

* **readme:** remove beta status + document versioning policy ([#102](https://github.com/anthropics/anthropic-sdk-python/issues/102)) ([2f0a0f9](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2f0a0f9))

### Chores

* **deps:** bump typing-extensions to 4.5 ([#112](https://github.com/anthropics/anthropic-sdk-python/issues/112)) ([f903269](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f903269))
* **docs:** remove trailing spaces ([#113](https://github.com/anthropics/anthropic-sdk-python/issues/113)) ([e876a6b](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/e876a6b))
* **internal:** bump pytest-asyncio ([#114](https://github.com/anthropics/anthropic-sdk-python/issues/114)) ([679ecd0](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/679ecd0))
* **internal:** update mypy to v1.4.1 ([#100](https://github.com/anthropics/anthropic-sdk-python/issues/100)) ([f615753](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/f615753))
* **internal:** update ruff to v0.0.282 ([#103](https://github.com/anthropics/anthropic-sdk-python/issues/103)) ([9db4b34](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/9db4b34))

## [0.3.8](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.8) (2023-08-01)

### Features

* **client:** add constants to client instances as well ([#95](https://github.com/anthropics/anthropic-sdk-python/issues/95)) ([d0fbe33](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d0fbe33))

### Chores

* **internal:** bump pyright ([#94](https://github.com/anthropics/anthropic-sdk-python/issues/94)) ([d2872dc](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d2872dc))
* **internal:** make demo example runnable and more portable ([#92](https://github.com/anthropics/anthropic-sdk-python/issues/92)) ([dea1aa2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/dea1aa2))

### Documentation

* **readme:** add token counting reference ([#96](https://github.com/anthropics/anthropic-sdk-python/issues/96)) ([79a339e](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/79a339e))

## [0.3.7](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.7) (2023-07-29)

### Features

* **client:** add client close handlers ([#89](https://github.com/anthropics/anthropic-sdk-python/issues/89)) ([2520a03](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/2520a03))

### Bug Fixes

* **client:** correctly handle environment variable access ([aa53754](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/aa53754))

### Documentation

* **readme:** use `client` everywhere for consistency ([0ff8924](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0ff8924))

### Chores

* **internal:** minor refactoring of client instantiation ([adf9158](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/adf9158))
* **internal:** minor reformatting of code ([#90](https://github.com/anthropics/anthropic-sdk-python/issues/90)) ([1175572](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/1175572))

## [0.3.6](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.6) (2023-07-22)

### Documentation

* **readme:** reference "client" in errors section and add missing import ([#79](https://github.com/anthropics/anthropic-sdk-python/issues/79)) ([ddc81cf](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/ddc81cf))

## [0.3.5](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.5) (2023-07-19)

### Features

* add flexible enum to model param ([#75](https://github.com/anthropics/anthropic-sdk-python/issues/75)) ([d16bb45](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d16bb45))

### Documentation

* **examples:** bump model to claude-2 in example scripts ([#67](https://github.com/anthropics/anthropic-sdk-python/issues/67)) ([cd68de2](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/cd68de2))

### Chores

* **internal:** add `codegen.log` to `.gitignore` ([#72](https://github.com/anthropics/anthropic-sdk-python/issues/72)) ([d9b7e30](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/d9b7e30))

## [0.3.4](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/0.3.4) (2023-07-11)

### Chores

* **package:** pin major versions of dependencies ([#59](https://github.com/anthropics/anthropic-sdk-python/issues/59)) ([3a75464](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/3a75464))

### Documentation

* **api:** reference claude-2 ([#61](https://github.com/anthropics/anthropic-sdk-python/issues/61)) ([91ece29](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/91ece29))
* **readme:** update examples to use claude-2 ([#65](https://github.com/anthropics/anthropic-sdk-python/issues/65)) ([7e4714c](https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/7e4714c))
