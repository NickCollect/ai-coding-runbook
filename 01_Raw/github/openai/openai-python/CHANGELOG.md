# Changelog

## 2.34.0 (2026-05-04)

Full Changelog: [v2.33.0...v2.34.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.33.0...v2.34.0)

### Features

* **api:** add external_key_id to projects, email/metadata params to users, update types ([2d232ee](https://raw.githubusercontent.com/openai/openai-python/main/2d232ee))
* **api:** add support for Admin API Keys per endpoint ([b8b176a](https://raw.githubusercontent.com/openai/openai-python/main/b8b176a))
* **api:** admin API updates ([4ae1138](https://raw.githubusercontent.com/openai/openai-python/main/4ae1138))
* **api:** manual updates ([c1870f1](https://raw.githubusercontent.com/openai/openai-python/main/c1870f1))
* **api:** manual updates ([f6bb9c7](https://raw.githubusercontent.com/openai/openai-python/main/f6bb9c7))
* support setting headers via env ([1e89d8b](https://raw.githubusercontent.com/openai/openai-python/main/1e89d8b))

### Bug Fixes

* allow explicit Azure auth headers ([a0626ba](https://raw.githubusercontent.com/openai/openai-python/main/a0626ba))
* **api:** correct prompt_cache_retention enum value from in-memory to in_memory ([d47d9f0](https://raw.githubusercontent.com/openai/openai-python/main/d47d9f0))
* **api:** preserve python api key attribute type ([62607f6](https://raw.githubusercontent.com/openai/openai-python/main/62607f6))
* **api:** resolve python auth type checks ([42a31a7](https://raw.githubusercontent.com/openai/openai-python/main/42a31a7))
* **api:** support admin api key auth ([f029eb9](https://raw.githubusercontent.com/openai/openai-python/main/f029eb9))
* avoid bearer fallback for admin auth ([22e01a8](https://raw.githubusercontent.com/openai/openai-python/main/22e01a8))
* preserve selected auth credentials ([0d27f9d](https://raw.githubusercontent.com/openai/openai-python/main/0d27f9d))
* require bearer auth for stream helpers ([d055539](https://raw.githubusercontent.com/openai/openai-python/main/d055539))
* **types:** correct created_at and completed_at to float in Response ([7da4b88](https://raw.githubusercontent.com/openai/openai-python/main/7da4b88))
* **types:** correct timestamp types to int in Response model ([e55631c](https://raw.githubusercontent.com/openai/openai-python/main/e55631c))
* use correct field name format for multipart file arrays ([9ee4825](https://raw.githubusercontent.com/openai/openai-python/main/9ee4825))

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([dca474e](https://raw.githubusercontent.com/openai/openai-python/main/dca474e))

### Chores

* **internal:** more robust bootstrap script ([9ec1600](https://raw.githubusercontent.com/openai/openai-python/main/9ec1600))
* **internal:** reformat pyproject.toml ([12ad57b](https://raw.githubusercontent.com/openai/openai-python/main/12ad57b))
* **tests:** bump steady to v0.22.1 ([486dfed](https://raw.githubusercontent.com/openai/openai-python/main/486dfed))

### Documentation

* **api:** add rate limit and vector store info to files create ([4f776df](https://raw.githubusercontent.com/openai/openai-python/main/4f776df))
* **api:** update files rate limit documentation ([b141a20](https://raw.githubusercontent.com/openai/openai-python/main/b141a20))

## 2.33.0 (2026-04-28)

Full Changelog: [v2.32.0...v2.33.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.32.0...v2.33.0)

### Features

* **api:** api update ([18f834a](https://raw.githubusercontent.com/openai/openai-python/main/18f834a))

### Bug Fixes

* **api:** correct prompt_cache_retention enum value from in-memory to in_memory ([#1822](https://github.com/openai/openai-python/issues/1822)) ([f9d2d13](https://raw.githubusercontent.com/openai/openai-python/main/f9d2d13))

### Chores

* **ci:** remove release-doctor workflow ([00b2091](https://raw.githubusercontent.com/openai/openai-python/main/00b2091))

## 2.32.0 (2026-04-15)

Full Changelog: [v2.31.0...v2.32.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.31.0...v2.32.0)

### Features

* **api:** Add detail to InputFileContent ([60de21d](https://raw.githubusercontent.com/openai/openai-python/main/60de21d))
* **api:** add OAuthErrorCode type ([0c8d2c3](https://raw.githubusercontent.com/openai/openai-python/main/0c8d2c3))
* **client:** add event handler implementation for websockets ([0280d05](https://raw.githubusercontent.com/openai/openai-python/main/0280d05))
* **client:** allow enqueuing to websockets even when not connected ([67aa20e](https://raw.githubusercontent.com/openai/openai-python/main/67aa20e))
* **client:** support reconnection in websockets ([eb72a95](https://raw.githubusercontent.com/openai/openai-python/main/eb72a95))

### Bug Fixes

* ensure file data are only sent as 1 parameter ([c0c2ecd](https://raw.githubusercontent.com/openai/openai-python/main/c0c2ecd))

### Documentation

* improve examples ([84712fa](https://raw.githubusercontent.com/openai/openai-python/main/84712fa))

## 2.31.0 (2026-04-08)

Full Changelog: [v2.30.0...v2.31.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.30.0...v2.31.0)

### Features

* **api:** add phase field to conversations message ([3e5834e](https://raw.githubusercontent.com/openai/openai-python/main/3e5834e))
* **api:** add web_search_call.results to ResponseIncludable type ([ffd8741](https://raw.githubusercontent.com/openai/openai-python/main/ffd8741))
* **client:** add support for short-lived tokens ([#1608](https://github.com/openai/openai-python/issues/1608)) ([22fe722](https://raw.githubusercontent.com/openai/openai-python/main/22fe722))
* **client:** support sending raw data over websockets ([f1bc52e](https://raw.githubusercontent.com/openai/openai-python/main/f1bc52e))
* **internal:** implement indices array format for query and form serialization ([49194cf](https://raw.githubusercontent.com/openai/openai-python/main/49194cf))

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([92e109c](https://raw.githubusercontent.com/openai/openai-python/main/92e109c))
* **types:** remove web_search_call.results from ResponseIncludable ([d3cc401](https://raw.githubusercontent.com/openai/openai-python/main/d3cc401))

### Chores

* **tests:** bump steady to v0.20.1 ([d60e2ee](https://raw.githubusercontent.com/openai/openai-python/main/d60e2ee))
* **tests:** bump steady to v0.20.2 ([6508d47](https://raw.githubusercontent.com/openai/openai-python/main/6508d47))

### Documentation

* **api:** update file parameter descriptions in vector_stores files and file_batches ([a9e7ebd](https://raw.githubusercontent.com/openai/openai-python/main/a9e7ebd))

## 2.30.0 (2026-03-25)

Full Changelog: [v2.29.0...v2.30.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.29.0...v2.30.0)

### Features

* **api:** add keys field to Click/DoubleClick/Drag/Move/Scroll computer actions ([ee1bbed](https://raw.githubusercontent.com/openai/openai-python/main/ee1bbed))

### Bug Fixes

* **api:** align SDK response types with expanded item schemas ([f3f258a](https://raw.githubusercontent.com/openai/openai-python/main/f3f258a))
* sanitize endpoint path params ([89f6698](https://raw.githubusercontent.com/openai/openai-python/main/89f6698))
* **types:** make type required in ResponseInputMessageItem ([cfdb167](https://raw.githubusercontent.com/openai/openai-python/main/cfdb167))

### Chores

* **ci:** skip lint on metadata-only changes ([faa93e1](https://raw.githubusercontent.com/openai/openai-python/main/faa93e1))
* **internal:** update gitignore ([c468477](https://raw.githubusercontent.com/openai/openai-python/main/c468477))
* **tests:** bump steady to v0.19.4 ([f350af8](https://raw.githubusercontent.com/openai/openai-python/main/f350af8))
* **tests:** bump steady to v0.19.5 ([5c03401](https://raw.githubusercontent.com/openai/openai-python/main/5c03401))
* **tests:** bump steady to v0.19.6 ([b6353b8](https://raw.githubusercontent.com/openai/openai-python/main/b6353b8))
* **tests:** bump steady to v0.19.7 ([1d654be](https://raw.githubusercontent.com/openai/openai-python/main/1d654be))

### Refactors

* **tests:** switch from prism to steady ([4a82035](https://raw.githubusercontent.com/openai/openai-python/main/4a82035))

## 2.29.0 (2026-03-17)

Full Changelog: [v2.28.0...v2.29.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.28.0...v2.29.0)

### Features

* **api:** 5.4 nano and mini model slugs ([3b45666](https://raw.githubusercontent.com/openai/openai-python/main/3b45666))
* **api:** add /v1/videos endpoint to batches create method ([c0e7a16](https://raw.githubusercontent.com/openai/openai-python/main/c0e7a16))
* **api:** add defer_loading field to ToolFunction ([3167595](https://raw.githubusercontent.com/openai/openai-python/main/3167595))
* **api:** add in and nin operators to ComparisonFilter type ([664f02b](https://raw.githubusercontent.com/openai/openai-python/main/664f02b))

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([a2fb2ca](https://raw.githubusercontent.com/openai/openai-python/main/a2fb2ca))
* **pydantic:** do not pass `by_alias` unless set ([8ebe8fb](https://raw.githubusercontent.com/openai/openai-python/main/8ebe8fb))

### Chores

* **internal:** tweak CI branches ([96ccc3c](https://raw.githubusercontent.com/openai/openai-python/main/96ccc3c))

## 2.28.0 (2026-03-13)

Full Changelog: [v2.27.0...v2.28.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.27.0...v2.28.0)

### Features

* **api:** custom voices ([50dc060](https://raw.githubusercontent.com/openai/openai-python/main/50dc060))

## 2.27.0 (2026-03-13)

Full Changelog: [v2.26.0...v2.27.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.26.0...v2.27.0)

### Features

* **api:** api update ([60ab24a](https://raw.githubusercontent.com/openai/openai-python/main/60ab24a))
* **api:** manual updates ([b244b09](https://raw.githubusercontent.com/openai/openai-python/main/b244b09))
* **api:** manual updates ([d806635](https://raw.githubusercontent.com/openai/openai-python/main/d806635))
* **api:** sora api improvements: character api, video extensions/edits, higher resolution exports. ([58b70d3](https://raw.githubusercontent.com/openai/openai-python/main/58b70d3))

### Bug Fixes

* **api:** repair merged videos resource ([742d8ee](https://raw.githubusercontent.com/openai/openai-python/main/742d8ee))

### Chores

* **internal:** codegen related update ([4e6498e](https://raw.githubusercontent.com/openai/openai-python/main/4e6498e))
* **internal:** codegen related update ([93af129](https://raw.githubusercontent.com/openai/openai-python/main/93af129))
* match http protocol with ws protocol instead of wss ([026f9de](https://raw.githubusercontent.com/openai/openai-python/main/026f9de))
* use proper capitalization for WebSockets ([a2f9b07](https://raw.githubusercontent.com/openai/openai-python/main/a2f9b07))

## 2.26.0 (2026-03-05)

Full Changelog: [v2.25.0...v2.26.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.25.0...v2.26.0)

### Features

* **api:** The GA ComputerTool now uses the CompuerTool class. The 'computer_use_preview' tool is moved to ComputerUsePreview ([78f5b3c](https://raw.githubusercontent.com/openai/openai-python/main/78f5b3c))

## 2.25.0 (2026-03-05)

Full Changelog: [v2.24.0...v2.25.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.24.0...v2.25.0)

### Features

* **api:** gpt-5.4, tool search tool, and new computer tool ([6b2043f](https://raw.githubusercontent.com/openai/openai-python/main/6b2043f))
* **api:** remove prompt_cache_key param from responses, phase field from message types ([44fb382](https://raw.githubusercontent.com/openai/openai-python/main/44fb382))

### Bug Fixes

* **api:** internal schema fixes ([0c0f970](https://raw.githubusercontent.com/openai/openai-python/main/0c0f970))
* **api:** manual updates ([9fc323f](https://raw.githubusercontent.com/openai/openai-python/main/9fc323f))
* **api:** readd phase ([1b27b5a](https://raw.githubusercontent.com/openai/openai-python/main/1b27b5a))

### Chores

* **internal:** codegen related update ([bdb837d](https://raw.githubusercontent.com/openai/openai-python/main/bdb837d))
* **internal:** codegen related update ([b1de941](https://raw.githubusercontent.com/openai/openai-python/main/b1de941))
* **internal:** reduce warnings ([7cdbd06](https://raw.githubusercontent.com/openai/openai-python/main/7cdbd06))

## 2.24.0 (2026-02-24)

Full Changelog: [v2.23.0...v2.24.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.23.0...v2.24.0)

### Features

* **api:** add phase ([391deb9](https://raw.githubusercontent.com/openai/openai-python/main/391deb9))

### Bug Fixes

* **api:** fix phase enum ([42ebf7c](https://raw.githubusercontent.com/openai/openai-python/main/42ebf7c))
* **api:** phase docs ([7ddc61c](https://raw.githubusercontent.com/openai/openai-python/main/7ddc61c))

### Chores

* **internal:** make `test_proxy_environment_variables` more resilient to env ([65af8fd](https://raw.githubusercontent.com/openai/openai-python/main/65af8fd))
* **internal:** refactor sse event parsing ([2344600](https://raw.githubusercontent.com/openai/openai-python/main/2344600))

## 2.23.0 (2026-02-24)

Full Changelog: [v2.22.0...v2.23.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.22.0...v2.23.0)

### Features

* **api:** add gpt-realtime-1.5 and gpt-audio-1.5 model options to realtime calls ([3300b61](https://raw.githubusercontent.com/openai/openai-python/main/3300b61))

### Chores

* **internal:** make `test_proxy_environment_variables` more resilient ([6b441e2](https://raw.githubusercontent.com/openai/openai-python/main/6b441e2))

## 2.22.0 (2026-02-23)

Full Changelog: [v2.21.0...v2.22.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.21.0...v2.22.0)

### Features

* **api:** websockets for responses api ([c01f6fb](https://raw.githubusercontent.com/openai/openai-python/main/c01f6fb))

### Chores

* **internal:** add request options to SSE classes ([cdb4315](https://raw.githubusercontent.com/openai/openai-python/main/cdb4315))
* update mock server docs ([91f4da8](https://raw.githubusercontent.com/openai/openai-python/main/91f4da8))

### Documentation

* **api:** add batch size limit to file_batches parameter descriptions ([16ae76a](https://raw.githubusercontent.com/openai/openai-python/main/16ae76a))
* **api:** enhance method descriptions across audio, chat, realtime, skills, uploads, videos ([21f9e5a](https://raw.githubusercontent.com/openai/openai-python/main/21f9e5a))
* **api:** update safety_identifier documentation in chat completions and responses ([d74bfff](https://raw.githubusercontent.com/openai/openai-python/main/d74bfff))

## 2.21.0 (2026-02-13)

Full Changelog: [v2.20.0...v2.21.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.20.0...v2.21.0)

### Features

* **api:** container network_policy and skills ([d19de2e](https://raw.githubusercontent.com/openai/openai-python/main/d19de2e))

### Bug Fixes

* **structured outputs:** resolve memory leak in parse methods ([#2860](https://github.com/openai/openai-python/issues/2860)) ([6dcbe21](https://raw.githubusercontent.com/openai/openai-python/main/6dcbe21))
* **webhooks:** preserve method visibility for compatibility checks ([44a8936](https://raw.githubusercontent.com/openai/openai-python/main/44a8936))

### Chores

* **internal:** fix lint error on Python 3.14 ([534f215](https://raw.githubusercontent.com/openai/openai-python/main/534f215))

### Documentation

* split `api.md` by standalone resources ([96e41b3](https://raw.githubusercontent.com/openai/openai-python/main/96e41b3))
* update comment ([63def23](https://raw.githubusercontent.com/openai/openai-python/main/63def23))

## 2.20.0 (2026-02-10)

Full Changelog: [v2.19.0...v2.20.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.19.0...v2.20.0)

### Features

* **api:** support for images in batch api ([28edb6e](https://raw.githubusercontent.com/openai/openai-python/main/28edb6e))

## 2.19.0 (2026-02-10)

Full Changelog: [v2.18.0...v2.19.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.18.0...v2.19.0)

### Features

* **api:** skills and hosted shell ([27fdf68](https://raw.githubusercontent.com/openai/openai-python/main/27fdf68))

### Chores

* **internal:** bump dependencies ([fae10fd](https://raw.githubusercontent.com/openai/openai-python/main/fae10fd))

## 2.18.0 (2026-02-09)

Full Changelog: [v2.17.0...v2.18.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.17.0...v2.18.0)

### Features

* **api:** add context_management to responses ([137e992](https://raw.githubusercontent.com/openai/openai-python/main/137e992))
* **api:** responses context_management ([c3bd017](https://raw.githubusercontent.com/openai/openai-python/main/c3bd017))

## 2.17.0 (2026-02-05)

Full Changelog: [v2.16.0...v2.17.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.16.0...v2.17.0)

### Features

* **api:** add shell_call_output status field ([1bbaf88](https://raw.githubusercontent.com/openai/openai-python/main/1bbaf88))
* **api:** image generation actions for responses; ResponseFunctionCallArgumentsDoneEvent.name ([7d96513](https://raw.githubusercontent.com/openai/openai-python/main/7d96513))
* **client:** add custom JSON encoder for extended type support ([9f43c8b](https://raw.githubusercontent.com/openai/openai-python/main/9f43c8b))

### Bug Fixes

* **client:** undo change to web search Find action ([8f14eb0](https://raw.githubusercontent.com/openai/openai-python/main/8f14eb0))
* **client:** update type for `find_in_page` action ([ec54dde](https://raw.githubusercontent.com/openai/openai-python/main/ec54dde))

## 2.16.0 (2026-01-27)

Full Changelog: [v2.15.0...v2.16.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.15.0...v2.16.0)

### Features

* **api:** api update ([b97f9f2](https://raw.githubusercontent.com/openai/openai-python/main/b97f9f2))
* **api:** api updates ([9debcc0](https://raw.githubusercontent.com/openai/openai-python/main/9debcc0))
* **client:** add support for binary request streaming ([49561d8](https://raw.githubusercontent.com/openai/openai-python/main/49561d8))

### Bug Fixes

* **api:** mark assistants as deprecated ([0419cbc](https://raw.githubusercontent.com/openai/openai-python/main/0419cbc))

### Chores

* **ci:** upgrade `actions/github-script` ([5139f13](https://raw.githubusercontent.com/openai/openai-python/main/5139f13))
* **internal:** update `actions/checkout` version ([f276714](https://raw.githubusercontent.com/openai/openai-python/main/f276714))

### Documentation

* **examples:** update Azure Realtime sample to use v1 API ([#2829](https://github.com/openai/openai-python/issues/2829)) ([3b31981](https://raw.githubusercontent.com/openai/openai-python/main/3b31981))

## 2.15.0 (2026-01-09)

Full Changelog: [v2.14.0...v2.15.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.14.0...v2.15.0)

### Features

* **api:** add new Response completed_at prop ([f077752](https://raw.githubusercontent.com/openai/openai-python/main/f077752))

### Chores

* **internal:** codegen related update ([e7daba6](https://raw.githubusercontent.com/openai/openai-python/main/e7daba6))

## 2.14.0 (2025-12-19)

Full Changelog: [v2.13.0...v2.14.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.13.0...v2.14.0)

### Features

* **api:** slugs for new audio models; make all `model` params accept strings ([e517792](https://raw.githubusercontent.com/openai/openai-python/main/e517792))

### Bug Fixes

* use async_to_httpx_files in patch method ([a6af9ee](https://raw.githubusercontent.com/openai/openai-python/main/a6af9ee))

### Chores

* **internal:** add `--fix` argument to lint script ([93107ef](https://raw.githubusercontent.com/openai/openai-python/main/93107ef))

## 2.13.0 (2025-12-16)

Full Changelog: [v2.12.0...v2.13.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.12.0...v2.13.0)

### Features

* **api:** gpt-image-1.5 ([1c88f03](https://raw.githubusercontent.com/openai/openai-python/main/1c88f03))

### Chores

* **ci:** add CI job to detect breaking changes with the Agents SDK ([#1436](https://github.com/openai/openai-python/issues/1436)) ([237c91e](https://raw.githubusercontent.com/openai/openai-python/main/237c91e))
* **internal:** add missing files argument to base client ([e6d6fd5](https://raw.githubusercontent.com/openai/openai-python/main/e6d6fd5))

## 2.12.0 (2025-12-15)

Full Changelog: [v2.11.0...v2.12.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.11.0...v2.12.0)

### Features

* **api:** api update ([a95c4d0](https://raw.githubusercontent.com/openai/openai-python/main/a95c4d0))
* **api:** fix grader input list, add dated slugs for sora-2 ([b2c389b](https://raw.githubusercontent.com/openai/openai-python/main/b2c389b))

## 2.11.0 (2025-12-11)

Full Changelog: [v2.10.0...v2.11.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.10.0...v2.11.0)

### Features

* **api:** gpt 5.2 ([dd9b8e8](https://raw.githubusercontent.com/openai/openai-python/main/dd9b8e8))

## 2.10.0 (2025-12-10)

Full Changelog: [v2.9.0...v2.10.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.9.0...v2.10.0)

### Features

* **api:** make model required for the responses/compact endpoint ([a12936b](https://raw.githubusercontent.com/openai/openai-python/main/a12936b))

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([8f0d230](https://raw.githubusercontent.com/openai/openai-python/main/8f0d230))

### Chores

* add missing docstrings ([f20a9a1](https://raw.githubusercontent.com/openai/openai-python/main/f20a9a1))
* **internal:** update docstring ([9a993f2](https://raw.githubusercontent.com/openai/openai-python/main/9a993f2))

## 2.9.0 (2025-12-04)

Full Changelog: [v2.8.1...v2.9.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.8.1...v2.9.0)

### Features

* **api:** gpt-5.1-codex-max and responses/compact ([22f646e](https://raw.githubusercontent.com/openai/openai-python/main/22f646e))

### Bug Fixes

* **client:** avoid mutating user-provided response config object ([#2700](https://github.com/openai/openai-python/issues/2700)) ([e040d22](https://raw.githubusercontent.com/openai/openai-python/main/e040d22))
* ensure streams are always closed ([0b1a27f](https://raw.githubusercontent.com/openai/openai-python/main/0b1a27f))
* **streaming:** correct indentation ([575bbac](https://raw.githubusercontent.com/openai/openai-python/main/575bbac))

### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([22cd586](https://raw.githubusercontent.com/openai/openai-python/main/22cd586))
* **docs:** use environment variables for authentication in code snippets ([c2a3cd5](https://raw.githubusercontent.com/openai/openai-python/main/c2a3cd5))
* **internal:** codegen related update ([307a066](https://raw.githubusercontent.com/openai/openai-python/main/307a066))
* update lockfile ([b4109c5](https://raw.githubusercontent.com/openai/openai-python/main/b4109c5))

## 2.8.1 (2025-11-17)

Full Changelog: [v2.8.0...v2.8.1](https://raw.githubusercontent.com/openai/openai-python/main/v2.8.0...v2.8.1)

### Bug Fixes

* **api:** align types of input items / output items for typescript ([64c9fb3](https://raw.githubusercontent.com/openai/openai-python/main/64c9fb3))

## 2.8.0 (2025-11-13)

Full Changelog: [v2.7.2...v2.8.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.7.2...v2.8.0)

### Features

* **api:** gpt 5.1 ([8d9f2ca](https://raw.githubusercontent.com/openai/openai-python/main/8d9f2ca))

### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([c7bd234](https://raw.githubusercontent.com/openai/openai-python/main/c7bd234))

## 2.7.2 (2025-11-10)

Full Changelog: [v2.7.1...v2.7.2](https://raw.githubusercontent.com/openai/openai-python/main/v2.7.1...v2.7.2)

### Bug Fixes

* compat with Python 3.14 ([15a7ec8](https://raw.githubusercontent.com/openai/openai-python/main/15a7ec8))

### Chores

* **package:** drop Python 3.8 support ([afc14f2](https://raw.githubusercontent.com/openai/openai-python/main/afc14f2))

## 2.7.1 (2025-11-04)

Full Changelog: [v2.7.0...v2.7.1](https://raw.githubusercontent.com/openai/openai-python/main/v2.7.0...v2.7.1)

### Bug Fixes

* **api:** fix nullability of logprobs ([373b7f6](https://raw.githubusercontent.com/openai/openai-python/main/373b7f6))

## 2.7.0 (2025-11-03)

Full Changelog: [v2.6.1...v2.7.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.6.1...v2.7.0)

### Features

* **api:** Realtime API token_limits, Hybrid searching ranking options ([5b43992](https://raw.githubusercontent.com/openai/openai-python/main/5b43992))
* **api:** remove InputAudio from ResponseInputContent ([bd70a33](https://raw.githubusercontent.com/openai/openai-python/main/bd70a33))

### Bug Fixes

* **client:** close streams without requiring full consumption ([d8bb7d6](https://raw.githubusercontent.com/openai/openai-python/main/d8bb7d6))
* **readme:** update realtime examples ([#2714](https://github.com/openai/openai-python/issues/2714)) ([d0370a8](https://raw.githubusercontent.com/openai/openai-python/main/d0370a8))
* **uploads:** avoid file handle leak ([4f1b691](https://raw.githubusercontent.com/openai/openai-python/main/4f1b691))

### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([933d23b](https://raw.githubusercontent.com/openai/openai-python/main/933d23b))
* **internal:** grammar fix (it's -&gt; its) ([f7e9e9e](https://raw.githubusercontent.com/openai/openai-python/main/f7e9e9e))

## 2.6.1 (2025-10-24)

Full Changelog: [v2.6.0...v2.6.1](https://raw.githubusercontent.com/openai/openai-python/main/v2.6.0...v2.6.1)

### Bug Fixes

* **api:** docs updates ([d01a0c9](https://raw.githubusercontent.com/openai/openai-python/main/d01a0c9))

### Chores

* **client:** clean up custom translations code ([cfb9e25](https://raw.githubusercontent.com/openai/openai-python/main/cfb9e25))

## 2.6.0 (2025-10-20)

Full Changelog: [v2.5.0...v2.6.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.5.0...v2.6.0)

### Features

* **api:** Add responses.input_tokens.count ([6dd09e2](https://raw.githubusercontent.com/openai/openai-python/main/6dd09e2))

### Bug Fixes

* **api:** internal openapi updates ([caabd7c](https://raw.githubusercontent.com/openai/openai-python/main/caabd7c))

## 2.5.0 (2025-10-17)

Full Changelog: [v2.4.0...v2.5.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.4.0...v2.5.0)

### Features

* **api:** api update ([8b280d5](https://raw.githubusercontent.com/openai/openai-python/main/8b280d5))

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([67f2f0a](https://raw.githubusercontent.com/openai/openai-python/main/67f2f0a))

## 2.4.0 (2025-10-16)

Full Changelog: [v2.3.0...v2.4.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.3.0...v2.4.0)

### Features

* **api:** Add support for gpt-4o-transcribe-diarize on audio/transcriptions endpoint ([bdbe9b8](https://raw.githubusercontent.com/openai/openai-python/main/bdbe9b8))

### Chores

* fix dangling comment ([da14e99](https://raw.githubusercontent.com/openai/openai-python/main/da14e99))
* **internal:** detect missing future annotations with ruff ([2672b8f](https://raw.githubusercontent.com/openai/openai-python/main/2672b8f))

## 2.3.0 (2025-10-10)

Full Changelog: [v2.2.0...v2.3.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.2.0...v2.3.0)

### Features

* **api:** comparison filter in/not in ([aa49f62](https://raw.githubusercontent.com/openai/openai-python/main/aa49f62))

### Chores

* **package:** bump jiter to &gt;=0.10.0 to support Python 3.14 ([#2618](https://github.com/openai/openai-python/issues/2618)) ([aa445ca](https://raw.githubusercontent.com/openai/openai-python/main/aa445ca))

## 2.2.0 (2025-10-06)

Full Changelog: [v2.1.0...v2.2.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.1.0...v2.2.0)

### Features

* **api:** dev day 2025 launches ([38ac009](https://raw.githubusercontent.com/openai/openai-python/main/38ac009))

### Bug Fixes

* **client:** add chatkit to beta resource ([de3e561](https://raw.githubusercontent.com/openai/openai-python/main/de3e561))

## 2.1.0 (2025-10-02)

Full Changelog: [v2.0.1...v2.1.0](https://raw.githubusercontent.com/openai/openai-python/main/v2.0.1...v2.1.0)

### Features

* **api:** add support for realtime calls ([7f7925b](https://raw.githubusercontent.com/openai/openai-python/main/7f7925b))

## 2.0.1 (2025-10-01)

Full Changelog: [v2.0.0...v2.0.1](https://raw.githubusercontent.com/openai/openai-python/main/v2.0.0...v2.0.1)

### Bug Fixes

* **api:** add status, approval_request_id to MCP tool call ([2a02255](https://raw.githubusercontent.com/openai/openai-python/main/2a02255))

## 2.0.0 (2025-09-30)

Full Changelog: [v1.109.1...v2.0.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.109.1...v2.0.0)

### ⚠ BREAKING CHANGES

* **api:** `ResponseFunctionToolCallOutputItem.output` and `ResponseCustomToolCallOutput.output` now return `string | Array<ResponseInputText | ResponseInputImage | ResponseInputFile>` instead of `string` only. This may break existing callsites that assume `output` is always a string.

### Features

* **api:** Support images and files for function call outputs in responses, BatchUsage ([4105376](https://raw.githubusercontent.com/openai/openai-python/main/4105376))

## 1.109.1 (2025-09-24)

Full Changelog: [v1.109.0...v1.109.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.109.0...v1.109.1)

### Bug Fixes

* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([5d95ecf](https://raw.githubusercontent.com/openai/openai-python/main/5d95ecf))

## 1.109.0 (2025-09-23)

Full Changelog: [v1.108.2...v1.109.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.108.2...v1.109.0)

### Features

* **api:** gpt-5-codex ([34502b5](https://raw.githubusercontent.com/openai/openai-python/main/34502b5))

## 1.108.2 (2025-09-22)

Full Changelog: [v1.108.1...v1.108.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.108.1...v1.108.2)

### Bug Fixes

* **api:** fix mcp tool name ([fd1c673](https://raw.githubusercontent.com/openai/openai-python/main/fd1c673))

### Chores

* **api:** openapi updates for conversations ([3224f6f](https://raw.githubusercontent.com/openai/openai-python/main/3224f6f))
* do not install brew dependencies in ./scripts/bootstrap by default ([6764b00](https://raw.githubusercontent.com/openai/openai-python/main/6764b00))
* improve example values ([20b58e1](https://raw.githubusercontent.com/openai/openai-python/main/20b58e1))

## 1.108.1 (2025-09-19)

Full Changelog: [v1.108.0...v1.108.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.108.0...v1.108.1)

### Features

* **api:** add reasoning_text ([18d8e12](https://raw.githubusercontent.com/openai/openai-python/main/18d8e12))

### Chores

* **types:** change optional parameter type from NotGiven to Omit ([acc190a](https://raw.githubusercontent.com/openai/openai-python/main/acc190a))

## 1.108.0 (2025-09-17)

Full Changelog: [v1.107.3...v1.108.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.107.3...v1.108.0)

### Features

* **api:** type updates for conversations, reasoning_effort and results for evals ([c2ee28c](https://raw.githubusercontent.com/openai/openai-python/main/c2ee28c))

### Chores

* **internal:** update pydantic dependency ([369d10a](https://raw.githubusercontent.com/openai/openai-python/main/369d10a))

## 1.107.3 (2025-09-15)

Full Changelog: [v1.107.2...v1.107.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.107.2...v1.107.3)

### Chores

* **api:** docs and spec refactoring ([9bab5da](https://raw.githubusercontent.com/openai/openai-python/main/9bab5da))
* **tests:** simplify `get_platform` test ([0b1f6a2](https://raw.githubusercontent.com/openai/openai-python/main/0b1f6a2))

## 1.107.2 (2025-09-12)

Full Changelog: [v1.107.1...v1.107.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.107.1...v1.107.2)

### Chores

* **api:** Minor docs and type updates for realtime ([ab6a10d](https://raw.githubusercontent.com/openai/openai-python/main/ab6a10d))
* **tests:** simplify `get_platform` test ([01f03e0](https://raw.githubusercontent.com/openai/openai-python/main/01f03e0))

## 1.107.1 (2025-09-10)

Full Changelog: [v1.107.0...v1.107.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.107.0...v1.107.1)

### Chores

* **api:** fix realtime GA types ([570fc5a](https://raw.githubusercontent.com/openai/openai-python/main/570fc5a))

## 1.107.0 (2025-09-08)

Full Changelog: [v1.106.1...v1.107.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.106.1...v1.107.0)

### Features

* **api:** ship the RealtimeGA API shape ([dc319d8](https://raw.githubusercontent.com/openai/openai-python/main/dc319d8))

### Chores

* **internal:** codegen related update ([b79b7ca](https://raw.githubusercontent.com/openai/openai-python/main/b79b7ca))

## 1.106.1 (2025-09-04)

Full Changelog: [v1.106.0...v1.106.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.106.0...v1.106.1)

### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([ca413a2](https://raw.githubusercontent.com/openai/openai-python/main/ca413a2))

## 1.106.0 (2025-09-04)

Full Changelog: [v1.105.0...v1.106.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.105.0...v1.106.0)

### Features

* **client:** support callable api_key ([#2588](https://github.com/openai/openai-python/issues/2588)) ([e1bad01](https://raw.githubusercontent.com/openai/openai-python/main/e1bad01))
* improve future compat with pydantic v3 ([6645d93](https://raw.githubusercontent.com/openai/openai-python/main/6645d93))

## 1.105.0 (2025-09-03)

Full Changelog: [v1.104.2...v1.105.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.104.2...v1.105.0)

### Features

* **api:** Add gpt-realtime models ([8502041](https://raw.githubusercontent.com/openai/openai-python/main/8502041))

## 1.104.2 (2025-09-02)

Full Changelog: [v1.104.1...v1.104.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.104.1...v1.104.2)

### Bug Fixes

* **types:** add aliases back for web search tool types ([2521cd8](https://raw.githubusercontent.com/openai/openai-python/main/2521cd8))

## 1.104.1 (2025-09-02)

Full Changelog: [v1.104.0...v1.104.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.104.0...v1.104.1)

### Chores

* **api:** manual updates for ResponseInputAudio ([0db5061](https://raw.githubusercontent.com/openai/openai-python/main/0db5061))

## 1.104.0 (2025-09-02)

Full Changelog: [v1.103.0...v1.104.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.103.0...v1.104.0)

### Features

* **types:** replace List[str] with SequenceNotStr in params ([bc00bda](https://raw.githubusercontent.com/openai/openai-python/main/bc00bda))

### Bug Fixes

* **types:** update more types to use SequenceNotStr ([cff135c](https://raw.githubusercontent.com/openai/openai-python/main/cff135c))
* **types:** update some types to SequenceNotStr ([03f8b88](https://raw.githubusercontent.com/openai/openai-python/main/03f8b88))

### Chores

* remove unused import ([ac7795b](https://raw.githubusercontent.com/openai/openai-python/main/ac7795b))

## 1.103.0 (2025-09-02)

Full Changelog: [v1.102.0...v1.103.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.102.0...v1.103.0)

### Features

* **api:** realtime API updates ([b7c2ddc](https://raw.githubusercontent.com/openai/openai-python/main/b7c2ddc))

### Bug Fixes

* **responses:** add missing params to stream() method ([bfc0673](https://raw.githubusercontent.com/openai/openai-python/main/bfc0673))

### Chores

* bump `inline-snapshot` version to 0.28.0 ([#2590](https://github.com/openai/openai-python/issues/2590)) ([a6b0872](https://raw.githubusercontent.com/openai/openai-python/main/a6b0872))
* **client:** format imports ([7ae3020](https://raw.githubusercontent.com/openai/openai-python/main/7ae3020))
* **internal:** add Sequence related utils ([d3d72b9](https://raw.githubusercontent.com/openai/openai-python/main/d3d72b9))
* **internal:** fix formatting ([3ab273f](https://raw.githubusercontent.com/openai/openai-python/main/3ab273f))
* **internal:** minor formatting change ([478a348](https://raw.githubusercontent.com/openai/openai-python/main/478a348))
* **internal:** update pyright exclude list ([66e440f](https://raw.githubusercontent.com/openai/openai-python/main/66e440f))

## 1.102.0 (2025-08-26)

Full Changelog: [v1.101.0...v1.102.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.101.0...v1.102.0)

### Features

* **api:** add web search filters ([1c199a8](https://raw.githubusercontent.com/openai/openai-python/main/1c199a8))

### Bug Fixes

* avoid newer type syntax ([bd0c668](https://raw.githubusercontent.com/openai/openai-python/main/bd0c668))

### Chores

* **internal:** change ci workflow machines ([3e129d5](https://raw.githubusercontent.com/openai/openai-python/main/3e129d5))
* **internal:** codegen related update ([b6dc170](https://raw.githubusercontent.com/openai/openai-python/main/b6dc170))

## 1.101.0 (2025-08-21)

Full Changelog: [v1.100.3...v1.101.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.100.3...v1.101.0)

### Features

* **api:** Add connectors support for MCP tool ([a47f962](https://raw.githubusercontent.com/openai/openai-python/main/a47f962))
* **api:** adding support for /v1/conversations to the API ([e30bcbc](https://raw.githubusercontent.com/openai/openai-python/main/e30bcbc))

### Chores

* update github action ([7333b28](https://raw.githubusercontent.com/openai/openai-python/main/7333b28))

## 1.100.3 (2025-08-20)

Full Changelog: [v1.100.2...v1.100.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.100.2...v1.100.3)

### Chores

* **internal/ci:** setup breaking change detection ([ca2f936](https://raw.githubusercontent.com/openai/openai-python/main/ca2f936))

## 1.100.2 (2025-08-19)

Full Changelog: [v1.100.1...v1.100.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.100.1...v1.100.2)

### Chores

* **api:** accurately represent shape for verbosity on Chat Completions ([c39d5fd](https://raw.githubusercontent.com/openai/openai-python/main/c39d5fd))

## 1.100.1 (2025-08-18)

Full Changelog: [v1.100.0...v1.100.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.100.0...v1.100.1)

### Bug Fixes

* **types:** revert response text config deletion ([ac4fb19](https://raw.githubusercontent.com/openai/openai-python/main/ac4fb19))

## 1.100.0 (2025-08-18)

Full Changelog: [v1.99.9...v1.100.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.9...v1.100.0)

### Features

* **api:** add new text parameters, expiration options ([e3dfa7c](https://raw.githubusercontent.com/openai/openai-python/main/e3dfa7c))

## 1.99.9 (2025-08-12)

Full Changelog: [v1.99.8...v1.99.9](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.8...v1.99.9)

### Bug Fixes

* **types:** actually fix ChatCompletionMessageToolCall type ([20cb0c8](https://raw.githubusercontent.com/openai/openai-python/main/20cb0c8))

## 1.99.8 (2025-08-11)

Full Changelog: [v1.99.7...v1.99.8](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.7...v1.99.8)

### Bug Fixes

* **internal/tests:** correct snapshot update comment ([2784a7a](https://raw.githubusercontent.com/openai/openai-python/main/2784a7a))
* **types:** revert ChatCompletionMessageToolCallUnion breaking change ([ba54e03](https://raw.githubusercontent.com/openai/openai-python/main/ba54e03))

### Chores

* **internal/tests:** add inline snapshot format command ([8107db8](https://raw.githubusercontent.com/openai/openai-python/main/8107db8))
* **internal:** fix formatting ([f03a03d](https://raw.githubusercontent.com/openai/openai-python/main/f03a03d))
* **tests:** add responses output_text test ([971347b](https://raw.githubusercontent.com/openai/openai-python/main/971347b))

### Refactors

* **tests:** share snapshot utils ([791c567](https://raw.githubusercontent.com/openai/openai-python/main/791c567))

## 1.99.7 (2025-08-11)

Full Changelog: [v1.99.6...v1.99.7](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.6...v1.99.7)

### Bug Fixes

* **types:** rename ChatCompletionMessageToolCallParam ([48085e2](https://raw.githubusercontent.com/openai/openai-python/main/48085e2))
* **types:** revert ChatCompletionMessageToolCallParam to a TypedDict ([c8e9cec](https://raw.githubusercontent.com/openai/openai-python/main/c8e9cec))

## 1.99.6 (2025-08-09)

Full Changelog: [v1.99.5...v1.99.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.5...v1.99.6)

### Bug Fixes

* **types:** re-export more tool call types ([8fe5741](https://raw.githubusercontent.com/openai/openai-python/main/8fe5741))

### Chores

* **internal:** update comment in script ([e407bb5](https://raw.githubusercontent.com/openai/openai-python/main/e407bb5))
* update @stainless-api/prism-cli to v5.15.0 ([a1883fc](https://raw.githubusercontent.com/openai/openai-python/main/a1883fc))

## 1.99.5 (2025-08-08)

Full Changelog: [v1.99.4...v1.99.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.4...v1.99.5)

### Bug Fixes

* **client:** fix verbosity parameter location in Responses ([2764ff4](https://raw.githubusercontent.com/openai/openai-python/main/2764ff4))

## 1.99.4 (2025-08-08)

Full Changelog: [v1.99.3...v1.99.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.3...v1.99.4)

### Bug Fixes

* **types:** rename chat completion tool ([8d3bf88](https://raw.githubusercontent.com/openai/openai-python/main/8d3bf88))
* **types:** revert ChatCompletionToolParam to a TypedDict ([3f4ae72](https://raw.githubusercontent.com/openai/openai-python/main/3f4ae72))

## 1.99.3 (2025-08-07)

Full Changelog: [v1.99.2...v1.99.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.2...v1.99.3)

### Bug Fixes

* **responses:** add output_text back ([585a4f1](https://raw.githubusercontent.com/openai/openai-python/main/585a4f1))

## 1.99.2 (2025-08-07)

Full Changelog: [v1.99.1...v1.99.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.1...v1.99.2)

### Features

* **api:** adds GPT-5 and new API features: platform.openai.com/docs/guides/gpt-5 ([ed370d8](https://raw.githubusercontent.com/openai/openai-python/main/ed370d8))

### Bug Fixes

* **types:** correct tool types ([0c57bd7](https://raw.githubusercontent.com/openai/openai-python/main/0c57bd7))

### Chores

* **tests:** bump inline-snapshot dependency ([e236fde](https://raw.githubusercontent.com/openai/openai-python/main/e236fde))

## 1.99.1 (2025-08-05)

Full Changelog: [v1.99.0...v1.99.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.99.0...v1.99.1)

### Bug Fixes

* **internal:** correct event imports ([2a6d143](https://raw.githubusercontent.com/openai/openai-python/main/2a6d143))

## 1.99.0 (2025-08-05)

Full Changelog: [v1.98.0...v1.99.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.98.0...v1.99.0)

### Features

* **api:** manual updates ([d4aa726](https://raw.githubusercontent.com/openai/openai-python/main/d4aa726))
* **client:** support file upload requests ([0772e6e](https://raw.githubusercontent.com/openai/openai-python/main/0772e6e))

### Bug Fixes

* add missing prompt_cache_key & prompt_cache_key params ([00b49ae](https://raw.githubusercontent.com/openai/openai-python/main/00b49ae))

### Chores

* **internal:** fix ruff target version ([aa6b252](https://raw.githubusercontent.com/openai/openai-python/main/aa6b252))

## 1.98.0 (2025-07-30)

Full Changelog: [v1.97.2...v1.98.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.97.2...v1.98.0)

### Features

* **api:** manual updates ([88a8036](https://raw.githubusercontent.com/openai/openai-python/main/88a8036))

## 1.97.2 (2025-07-30)

Full Changelog: [v1.97.1...v1.97.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.97.1...v1.97.2)

### Chores

* **client:** refactor streaming slightly to better future proof it ([71c0c74](https://raw.githubusercontent.com/openai/openai-python/main/71c0c74))
* **project:** add settings file for vscode ([29c22c9](https://raw.githubusercontent.com/openai/openai-python/main/29c22c9))

## 1.97.1 (2025-07-22)

Full Changelog: [v1.97.0...v1.97.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.97.0...v1.97.1)

### Bug Fixes

* **parsing:** ignore empty metadata ([58c359f](https://raw.githubusercontent.com/openai/openai-python/main/58c359f))
* **parsing:** parse extra field types ([d524b7e](https://raw.githubusercontent.com/openai/openai-python/main/d524b7e))

### Chores

* **api:** event shapes more accurate ([f3a9a92](https://raw.githubusercontent.com/openai/openai-python/main/f3a9a92))

## 1.97.0 (2025-07-16)

Full Changelog: [v1.96.1...v1.97.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.96.1...v1.97.0)

### Features

* **api:** manual updates ([ed8e899](https://raw.githubusercontent.com/openai/openai-python/main/ed8e899))

## 1.96.1 (2025-07-15)

Full Changelog: [v1.96.0...v1.96.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.96.0...v1.96.1)

### Chores

* **api:** update realtime specs ([b68b71b](https://raw.githubusercontent.com/openai/openai-python/main/b68b71b))

## 1.96.0 (2025-07-15)

Full Changelog: [v1.95.1...v1.96.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.95.1...v1.96.0)

### Features

* clean up environment call outs ([87c2e97](https://raw.githubusercontent.com/openai/openai-python/main/87c2e97))

### Chores

* **api:** update realtime specs, build config ([bf06d88](https://raw.githubusercontent.com/openai/openai-python/main/bf06d88))

## 1.95.1 (2025-07-11)

Full Changelog: [v1.95.0...v1.95.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.95.0...v1.95.1)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([182b763](https://raw.githubusercontent.com/openai/openai-python/main/182b763))

## 1.95.0 (2025-07-10)

Full Changelog: [v1.94.0...v1.95.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.94.0...v1.95.0)

### Features

* **api:** add file_url, fix event ID ([265e216](https://raw.githubusercontent.com/openai/openai-python/main/265e216))

### Chores

* **readme:** fix version rendering on pypi ([1eee5ca](https://raw.githubusercontent.com/openai/openai-python/main/1eee5ca))

## 1.94.0 (2025-07-10)

Full Changelog: [v1.93.3...v1.94.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.93.3...v1.94.0)

### Features

* **api:** return better error message on missing embedding ([#2369](https://github.com/openai/openai-python/issues/2369)) ([e53464a](https://raw.githubusercontent.com/openai/openai-python/main/e53464a))

## 1.93.3 (2025-07-09)

Full Changelog: [v1.93.2...v1.93.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.93.2...v1.93.3)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([fc8a677](https://raw.githubusercontent.com/openai/openai-python/main/fc8a677))

## 1.93.2 (2025-07-08)

Full Changelog: [v1.93.1...v1.93.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.93.1...v1.93.2)

### Chores

* **internal:** bump pinned h11 dep ([4fca6ae](https://raw.githubusercontent.com/openai/openai-python/main/4fca6ae))
* **package:** mark python 3.13 as supported ([2229047](https://raw.githubusercontent.com/openai/openai-python/main/2229047))

## 1.93.1 (2025-07-07)

Full Changelog: [v1.93.0...v1.93.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.93.0...v1.93.1)

### Bug Fixes

* **ci:** correct conditional ([de6a9ce](https://raw.githubusercontent.com/openai/openai-python/main/de6a9ce))
* **responses:** add missing arguments to parse ([05590ec](https://raw.githubusercontent.com/openai/openai-python/main/05590ec))
* **vector stores:** add missing arguments to files.create_and_poll ([3152134](https://raw.githubusercontent.com/openai/openai-python/main/3152134))
* **vector stores:** add missing arguments to files.upload_and_poll ([9d4f425](https://raw.githubusercontent.com/openai/openai-python/main/9d4f425))

### Chores

* **ci:** change upload type ([cd4aa88](https://raw.githubusercontent.com/openai/openai-python/main/cd4aa88))
* **ci:** only run for pushes and fork pull requests ([f89c7eb](https://raw.githubusercontent.com/openai/openai-python/main/f89c7eb))
* **internal:** codegen related update ([bddb8d2](https://raw.githubusercontent.com/openai/openai-python/main/bddb8d2))
* **tests:** ensure parse method is in sync with create ([4f58e18](https://raw.githubusercontent.com/openai/openai-python/main/4f58e18))
* **tests:** ensure vector store files create and poll method is in sync ([0fe75a2](https://raw.githubusercontent.com/openai/openai-python/main/0fe75a2))

## 1.93.0 (2025-06-27)

Full Changelog: [v1.92.3...v1.93.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.92.3...v1.93.0)

### Features

* **cli:** add support for fine_tuning.jobs ([#1224](https://github.com/openai/openai-python/issues/1224)) ([e362bfd](https://raw.githubusercontent.com/openai/openai-python/main/e362bfd))

## 1.92.3 (2025-06-27)

Full Changelog: [v1.92.2...v1.92.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.92.2...v1.92.3)

### Bug Fixes

* **client:** avoid encoding error with empty API keys ([5a3e64e](https://raw.githubusercontent.com/openai/openai-python/main/5a3e64e))

### Documentation

* **examples/realtime:** mention macOS requirements ([#2142](https://github.com/openai/openai-python/issues/2142)) ([27bf6b2](https://raw.githubusercontent.com/openai/openai-python/main/27bf6b2))

## 1.92.2 (2025-06-26)

Full Changelog: [v1.92.1...v1.92.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.92.1...v1.92.2)

### Chores

* **api:** remove unsupported property ([ec24408](https://raw.githubusercontent.com/openai/openai-python/main/ec24408))

## 1.92.1 (2025-06-26)

Full Changelog: [v1.92.0...v1.92.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.92.0...v1.92.1)

### Chores

* **client:** sync stream/parse methods over ([e2536cf](https://raw.githubusercontent.com/openai/openai-python/main/e2536cf))
* **docs:** update README to include links to docs on Webhooks ([ddbf9f1](https://raw.githubusercontent.com/openai/openai-python/main/ddbf9f1))

## 1.92.0 (2025-06-26)

Full Changelog: [v1.91.0...v1.92.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.91.0...v1.92.0)

### Features

* **api:** webhook and deep research support ([d3bb116](https://raw.githubusercontent.com/openai/openai-python/main/d3bb116))
* **client:** move stream and parse out of beta ([0e358ed](https://raw.githubusercontent.com/openai/openai-python/main/0e358ed))

### Bug Fixes

* **ci:** release-doctor — report correct token name ([ff8c556](https://raw.githubusercontent.com/openai/openai-python/main/ff8c556))

### Chores

* **internal:** add tests for breaking change detection ([710fe8f](https://raw.githubusercontent.com/openai/openai-python/main/710fe8f))
* **tests:** skip some failing tests on the latest python versions ([93ccc38](https://raw.githubusercontent.com/openai/openai-python/main/93ccc38))

## 1.91.0 (2025-06-23)

Full Changelog: [v1.90.0...v1.91.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.90.0...v1.91.0)

### Features

* **api:** update api shapes for usage and code interpreter ([060d566](https://raw.githubusercontent.com/openai/openai-python/main/060d566))

## 1.90.0 (2025-06-20)

Full Changelog: [v1.89.0...v1.90.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.89.0...v1.90.0)

### Features

* **api:** make model and inputs not required to create response ([11bd62e](https://raw.githubusercontent.com/openai/openai-python/main/11bd62e))

## 1.89.0 (2025-06-20)

Full Changelog: [v1.88.0...v1.89.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.88.0...v1.89.0)

### Features

* **client:** add support for aiohttp ([9218b07](https://raw.githubusercontent.com/openai/openai-python/main/9218b07))

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([35bcc4b](https://raw.githubusercontent.com/openai/openai-python/main/35bcc4b))

### Chores

* **readme:** update badges ([68044ee](https://raw.githubusercontent.com/openai/openai-python/main/68044ee))

## 1.88.0 (2025-06-17)

Full Changelog: [v1.87.0...v1.88.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.87.0...v1.88.0)

### Features

* **api:** manual updates ([5d18a84](https://raw.githubusercontent.com/openai/openai-python/main/5d18a84))

### Chores

* **ci:** enable for pull requests ([542b0ce](https://raw.githubusercontent.com/openai/openai-python/main/542b0ce))
* **internal:** minor formatting ([29d723d](https://raw.githubusercontent.com/openai/openai-python/main/29d723d))

## 1.87.0 (2025-06-16)

Full Changelog: [v1.86.0...v1.87.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.86.0...v1.87.0)

### Features

* **api:** add reusable prompt IDs ([36bfe6e](https://raw.githubusercontent.com/openai/openai-python/main/36bfe6e))

### Bug Fixes

* **client:** update service_tier on `client.beta.chat.completions` ([aa488d5](https://raw.githubusercontent.com/openai/openai-python/main/aa488d5))

### Chores

* **internal:** codegen related update ([b1a31e5](https://raw.githubusercontent.com/openai/openai-python/main/b1a31e5))
* **internal:** update conftest.py ([bba0213](https://raw.githubusercontent.com/openai/openai-python/main/bba0213))
* **tests:** add tests for httpx client instantiation & proxies ([bc93712](https://raw.githubusercontent.com/openai/openai-python/main/bc93712))

## 1.86.0 (2025-06-10)

Full Changelog: [v1.85.0...v1.86.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.85.0...v1.86.0)

### Features

* **api:** Add o3-pro model IDs ([d8dd80b](https://raw.githubusercontent.com/openai/openai-python/main/d8dd80b))

## 1.85.0 (2025-06-09)

Full Changelog: [v1.84.0...v1.85.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.84.0...v1.85.0)

### Features

* **api:** Add tools and structured outputs to evals ([002cc7b](https://raw.githubusercontent.com/openai/openai-python/main/002cc7b))

### Bug Fixes

* **responses:** support raw responses for `parse()` ([d459943](https://raw.githubusercontent.com/openai/openai-python/main/d459943))

## 1.84.0 (2025-06-03)

Full Changelog: [v1.83.0...v1.84.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.83.0...v1.84.0)

### Features

* **api:** add new realtime and audio models, realtime session options ([0acd0da](https://raw.githubusercontent.com/openai/openai-python/main/0acd0da))

### Chores

* **api:** update type names ([1924559](https://raw.githubusercontent.com/openai/openai-python/main/1924559))

## 1.83.0 (2025-06-02)

Full Changelog: [v1.82.1...v1.83.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.82.1...v1.83.0)

### Features

* **api:** Config update for pakrym-stream-param ([88bcf3a](https://raw.githubusercontent.com/openai/openai-python/main/88bcf3a))
* **client:** add follow_redirects request option ([26d715f](https://raw.githubusercontent.com/openai/openai-python/main/26d715f))

### Bug Fixes

* **api:** Fix evals and code interpreter interfaces ([2650159](https://raw.githubusercontent.com/openai/openai-python/main/2650159))
* **client:** return binary content from `get /containers/{container_id}/files/{file_id}/content` ([f7c80c4](https://raw.githubusercontent.com/openai/openai-python/main/f7c80c4))

### Chores

* **api:** mark some methods as deprecated ([3e2ca57](https://raw.githubusercontent.com/openai/openai-python/main/3e2ca57))
* deprecate Assistants API ([9d166d7](https://raw.githubusercontent.com/openai/openai-python/main/9d166d7))
* **docs:** remove reference to rye shell ([c7978e9](https://raw.githubusercontent.com/openai/openai-python/main/c7978e9))

## 1.82.1 (2025-05-29)

Full Changelog: [v1.82.0...v1.82.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.82.0...v1.82.1)

### Bug Fixes

* **responses:** don't include `parsed_arguments` when re-serialising ([6d04193](https://raw.githubusercontent.com/openai/openai-python/main/6d04193))

### Chores

* **internal:** fix release workflows ([361a909](https://raw.githubusercontent.com/openai/openai-python/main/361a909))

## 1.82.0 (2025-05-22)

Full Changelog: [v1.81.0...v1.82.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.81.0...v1.82.0)

### Features

* **api:** new streaming helpers for background responses ([2a65d4d](https://raw.githubusercontent.com/openai/openai-python/main/2a65d4d))

### Bug Fixes

* **azure:** mark images/edits as a deployment endpoint [#2371](https://github.com/openai/openai-python/issues/2371) ([5d1d5b4](https://raw.githubusercontent.com/openai/openai-python/main/5d1d5b4))

### Documentation

* **readme:** another async example fix ([9ec8289](https://raw.githubusercontent.com/openai/openai-python/main/9ec8289))
* **readme:** fix async example ([37d0b25](https://raw.githubusercontent.com/openai/openai-python/main/37d0b25))

## 1.81.0 (2025-05-21)

Full Changelog: [v1.80.0...v1.81.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.80.0...v1.81.0)

### Features

* **api:** add container endpoint ([054a210](https://raw.githubusercontent.com/openai/openai-python/main/054a210))

## 1.80.0 (2025-05-21)

Full Changelog: [v1.79.0...v1.80.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.79.0...v1.80.0)

### Features

* **api:** new API tools ([d36ae52](https://raw.githubusercontent.com/openai/openai-python/main/d36ae52))

### Chores

* **docs:** grammar improvements ([e746145](https://raw.githubusercontent.com/openai/openai-python/main/e746145))

## 1.79.0 (2025-05-16)

Full Changelog: [v1.78.1...v1.79.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.78.1...v1.79.0)

### Features

* **api:** further updates for evals API ([32c99a6](https://raw.githubusercontent.com/openai/openai-python/main/32c99a6))
* **api:** manual updates ([25245e5](https://raw.githubusercontent.com/openai/openai-python/main/25245e5))
* **api:** responses x eval api ([fd586cb](https://raw.githubusercontent.com/openai/openai-python/main/fd586cb))
* **api:** Updating Assistants and Evals API schemas ([98ba7d3](https://raw.githubusercontent.com/openai/openai-python/main/98ba7d3))

### Bug Fixes

* fix create audio transcription endpoint ([e9a89ab](https://raw.githubusercontent.com/openai/openai-python/main/e9a89ab))

### Chores

* **ci:** fix installation instructions ([f26c5fc](https://raw.githubusercontent.com/openai/openai-python/main/f26c5fc))
* **ci:** upload sdks to package manager ([861f105](https://raw.githubusercontent.com/openai/openai-python/main/861f105))

## 1.78.1 (2025-05-12)

Full Changelog: [v1.78.0...v1.78.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.78.0...v1.78.1)

### Bug Fixes

* **internal:** fix linting due to broken __test__ annotation ([5a7d7a0](https://raw.githubusercontent.com/openai/openai-python/main/5a7d7a0))
* **package:** support direct resource imports ([2293fc0](https://raw.githubusercontent.com/openai/openai-python/main/2293fc0))

## 1.78.0 (2025-05-08)

Full Changelog: [v1.77.0...v1.78.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.77.0...v1.78.0)

### Features

* **api:** Add reinforcement fine-tuning api support ([bebe361](https://raw.githubusercontent.com/openai/openai-python/main/bebe361))

### Bug Fixes

* ignore errors in isinstance() calls on LazyProxy subclasses ([#2343](https://github.com/openai/openai-python/issues/2343)) ([52cbbdf](https://raw.githubusercontent.com/openai/openai-python/main/52cbbdf)), closes [#2056](https://github.com/openai/openai-python/issues/2056)

### Chores

* **internal:** update proxy tests ([b8e848d](https://raw.githubusercontent.com/openai/openai-python/main/b8e848d))
* use lazy imports for module level client ([4d0f409](https://raw.githubusercontent.com/openai/openai-python/main/4d0f409))
* use lazy imports for resources ([834813c](https://raw.githubusercontent.com/openai/openai-python/main/834813c))

## 1.77.0 (2025-05-02)

Full Changelog: [v1.76.2...v1.77.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.76.2...v1.77.0)

### Features

* **api:** add image sizes, reasoning encryption ([473469a](https://raw.githubusercontent.com/openai/openai-python/main/473469a))

### Bug Fixes

* **parsing:** handle whitespace only strings ([#2007](https://github.com/openai/openai-python/issues/2007)) ([246bc5b](https://raw.githubusercontent.com/openai/openai-python/main/246bc5b))

### Chores

* only strip leading whitespace ([8467d66](https://raw.githubusercontent.com/openai/openai-python/main/8467d66))

## 1.76.2 (2025-04-29)

Full Changelog: [v1.76.1...v1.76.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.76.1...v1.76.2)

### Chores

* **api:** API spec cleanup ([0a4d3e2](https://raw.githubusercontent.com/openai/openai-python/main/0a4d3e2))

## 1.76.1 (2025-04-29)

Full Changelog: [v1.76.0...v1.76.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.76.0...v1.76.1)

### Chores

* broadly detect json family of content-type headers ([b4b1b08](https://raw.githubusercontent.com/openai/openai-python/main/b4b1b08))
* **ci:** only use depot for staging repos ([35312d8](https://raw.githubusercontent.com/openai/openai-python/main/35312d8))
* **ci:** run on more branches and use depot runners ([a6a45d4](https://raw.githubusercontent.com/openai/openai-python/main/a6a45d4))

## 1.76.0 (2025-04-23)

Full Changelog: [v1.75.0...v1.76.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.75.0...v1.76.0)

### Features

* **api:** adding new image model support ([74d7692](https://raw.githubusercontent.com/openai/openai-python/main/74d7692))

### Bug Fixes

* **pydantic v1:** more robust `ModelField.annotation` check ([#2163](https://github.com/openai/openai-python/issues/2163)) ([7351b12](https://raw.githubusercontent.com/openai/openai-python/main/7351b12))
* **pydantic v1:** more robust ModelField.annotation check ([eba7856](https://raw.githubusercontent.com/openai/openai-python/main/eba7856))

### Chores

* **ci:** add timeout thresholds for CI jobs ([0997211](https://raw.githubusercontent.com/openai/openai-python/main/0997211))
* **internal:** fix list file params ([da2113c](https://raw.githubusercontent.com/openai/openai-python/main/da2113c))
* **internal:** import reformatting ([b425fb9](https://raw.githubusercontent.com/openai/openai-python/main/b425fb9))
* **internal:** minor formatting changes ([aed1d76](https://raw.githubusercontent.com/openai/openai-python/main/aed1d76))
* **internal:** refactor retries to not use recursion ([8cb8cfa](https://raw.githubusercontent.com/openai/openai-python/main/8cb8cfa))
* **internal:** update models test ([870ad4e](https://raw.githubusercontent.com/openai/openai-python/main/870ad4e))
* update completion parse signature ([a44016c](https://raw.githubusercontent.com/openai/openai-python/main/a44016c))

## 1.75.0 (2025-04-16)

Full Changelog: [v1.74.1...v1.75.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.74.1...v1.75.0)

### Features

* **api:** add o3 and o4-mini model IDs ([4bacbd5](https://raw.githubusercontent.com/openai/openai-python/main/4bacbd5))

## 1.74.1 (2025-04-16)

Full Changelog: [v1.74.0...v1.74.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.74.0...v1.74.1)

### Chores

* **internal:** base client updates ([06303b5](https://raw.githubusercontent.com/openai/openai-python/main/06303b5))
* **internal:** bump pyright version ([9fd1c77](https://raw.githubusercontent.com/openai/openai-python/main/9fd1c77))

## 1.74.0 (2025-04-14)

Full Changelog: [v1.73.0...v1.74.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.73.0...v1.74.0)

### Features

* **api:** adding gpt-4.1 family of model IDs ([d4dae55](https://raw.githubusercontent.com/openai/openai-python/main/d4dae55))

### Bug Fixes

* **chat:** skip azure async filter events ([#2255](https://github.com/openai/openai-python/issues/2255)) ([fd3a38b](https://raw.githubusercontent.com/openai/openai-python/main/fd3a38b))

### Chores

* **client:** minor internal fixes ([6071ae5](https://raw.githubusercontent.com/openai/openai-python/main/6071ae5))
* **internal:** update pyright settings ([c8f8beb](https://raw.githubusercontent.com/openai/openai-python/main/c8f8beb))

## 1.73.0 (2025-04-12)

Full Changelog: [v1.72.0...v1.73.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.72.0...v1.73.0)

### Features

* **api:** manual updates ([a3253dd](https://raw.githubusercontent.com/openai/openai-python/main/a3253dd))

### Bug Fixes

* **perf:** optimize some hot paths ([f79d39f](https://raw.githubusercontent.com/openai/openai-python/main/f79d39f))
* **perf:** skip traversing types for NotGiven values ([28d220d](https://raw.githubusercontent.com/openai/openai-python/main/28d220d))

### Chores

* **internal:** expand CI branch coverage ([#2295](https://github.com/openai/openai-python/issues/2295)) ([0ae783b](https://raw.githubusercontent.com/openai/openai-python/main/0ae783b))
* **internal:** reduce CI branch coverage ([2fb7d42](https://raw.githubusercontent.com/openai/openai-python/main/2fb7d42))
* slight wording improvement in README ([#2291](https://github.com/openai/openai-python/issues/2291)) ([e020759](https://raw.githubusercontent.com/openai/openai-python/main/e020759))
* workaround build errors ([4e10c96](https://raw.githubusercontent.com/openai/openai-python/main/4e10c96))

## 1.72.0 (2025-04-08)

Full Changelog: [v1.71.0...v1.72.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.71.0...v1.72.0)

### Features

* **api:** Add evalapi to sdk ([#2287](https://github.com/openai/openai-python/issues/2287)) ([35262fc](https://raw.githubusercontent.com/openai/openai-python/main/35262fc))

### Chores

* **internal:** fix examples ([#2288](https://github.com/openai/openai-python/issues/2288)) ([39defd6](https://raw.githubusercontent.com/openai/openai-python/main/39defd6))
* **internal:** skip broken test ([#2289](https://github.com/openai/openai-python/issues/2289)) ([e2c9bce](https://raw.githubusercontent.com/openai/openai-python/main/e2c9bce))
* **internal:** slight transform perf improvement ([#2284](https://github.com/openai/openai-python/issues/2284)) ([746174f](https://raw.githubusercontent.com/openai/openai-python/main/746174f))
* **tests:** improve enum examples ([#2286](https://github.com/openai/openai-python/issues/2286)) ([c9dd81c](https://raw.githubusercontent.com/openai/openai-python/main/c9dd81c))

## 1.71.0 (2025-04-07)

Full Changelog: [v1.70.0...v1.71.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.70.0...v1.71.0)

### Features

* **api:** manual updates ([bf8b4b6](https://raw.githubusercontent.com/openai/openai-python/main/bf8b4b6))
* **api:** manual updates ([3e37aa3](https://raw.githubusercontent.com/openai/openai-python/main/3e37aa3))
* **api:** manual updates ([dba9b65](https://raw.githubusercontent.com/openai/openai-python/main/dba9b65))
* **api:** manual updates ([f0c463b](https://raw.githubusercontent.com/openai/openai-python/main/f0c463b))

### Chores

* **deps:** allow websockets v15 ([#2281](https://github.com/openai/openai-python/issues/2281)) ([19c619e](https://raw.githubusercontent.com/openai/openai-python/main/19c619e))
* **internal:** only run examples workflow in main repo ([#2282](https://github.com/openai/openai-python/issues/2282)) ([c3e0927](https://raw.githubusercontent.com/openai/openai-python/main/c3e0927))
* **internal:** remove trailing character ([#2277](https://github.com/openai/openai-python/issues/2277)) ([5a21a2d](https://raw.githubusercontent.com/openai/openai-python/main/5a21a2d))
* Remove deprecated/unused remote spec feature ([23f76eb](https://raw.githubusercontent.com/openai/openai-python/main/23f76eb))

## 1.70.0 (2025-03-31)

Full Changelog: [v1.69.0...v1.70.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.69.0...v1.70.0)

### Features

* **api:** add `get /responses/{response_id}/input_items` endpoint ([4c6a35d](https://raw.githubusercontent.com/openai/openai-python/main/4c6a35d))

## 1.69.0 (2025-03-27)

Full Changelog: [v1.68.2...v1.69.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.68.2...v1.69.0)

### Features

* **api:** add `get /chat/completions` endpoint ([e6b8a42](https://raw.githubusercontent.com/openai/openai-python/main/e6b8a42))

### Bug Fixes

* **audio:** correctly parse transcription stream events ([16a3a19](https://raw.githubusercontent.com/openai/openai-python/main/16a3a19))

### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([515e1cd](https://raw.githubusercontent.com/openai/openai-python/main/515e1cd))
* **api:** updates to supported Voice IDs ([#2261](https://github.com/openai/openai-python/issues/2261)) ([64956f9](https://raw.githubusercontent.com/openai/openai-python/main/64956f9))
* fix typos ([#2259](https://github.com/openai/openai-python/issues/2259)) ([6160de3](https://raw.githubusercontent.com/openai/openai-python/main/6160de3))

## 1.68.2 (2025-03-21)

Full Changelog: [v1.68.1...v1.68.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.68.1...v1.68.2)

### Refactors

* **package:** rename audio extra to voice_helpers ([2dd6cb8](https://raw.githubusercontent.com/openai/openai-python/main/2dd6cb8))

## 1.68.1 (2025-03-21)

Full Changelog: [v1.68.0...v1.68.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.68.0...v1.68.1)

### Bug Fixes

* **client:** remove duplicate types ([#2235](https://github.com/openai/openai-python/issues/2235)) ([063f7d0](https://raw.githubusercontent.com/openai/openai-python/main/063f7d0))
* **helpers/audio:** remove duplicative module ([f253d04](https://raw.githubusercontent.com/openai/openai-python/main/f253d04))
* **package:** make sounddevice and numpy optional dependencies ([8b04453](https://raw.githubusercontent.com/openai/openai-python/main/8b04453))

### Chores

* **ci:** run workflows on next too ([67f89d4](https://raw.githubusercontent.com/openai/openai-python/main/67f89d4))

## 1.68.0 (2025-03-20)

Full Changelog: [v1.67.0...v1.68.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.67.0...v1.68.0)

### Features

* add audio helpers ([423655c](https://raw.githubusercontent.com/openai/openai-python/main/423655c))
* **api:** new models for TTS, STT, + new audio features for Realtime ([#2232](https://github.com/openai/openai-python/issues/2232)) ([ab5192d](https://raw.githubusercontent.com/openai/openai-python/main/ab5192d))

## 1.67.0 (2025-03-19)

Full Changelog: [v1.66.5...v1.67.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.5...v1.67.0)

### Features

* **api:** o1-pro now available through the API ([#2228](https://github.com/openai/openai-python/issues/2228)) ([40a19d8](https://raw.githubusercontent.com/openai/openai-python/main/40a19d8))

## 1.66.5 (2025-03-18)

Full Changelog: [v1.66.4...v1.66.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.4...v1.66.5)

### Bug Fixes

* **types:** improve responses type names ([#2224](https://github.com/openai/openai-python/issues/2224)) ([5f7beb8](https://raw.githubusercontent.com/openai/openai-python/main/5f7beb8))

### Chores

* **internal:** add back releases workflow ([c71d4c9](https://raw.githubusercontent.com/openai/openai-python/main/c71d4c9))
* **internal:** codegen related update ([#2222](https://github.com/openai/openai-python/issues/2222)) ([f570d91](https://raw.githubusercontent.com/openai/openai-python/main/f570d91))

## 1.66.4 (2025-03-17)

Full Changelog: [v1.66.3...v1.66.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.3...v1.66.4)

### Bug Fixes

* **ci:** ensure pip is always available ([#2207](https://github.com/openai/openai-python/issues/2207)) ([3f08e56](https://raw.githubusercontent.com/openai/openai-python/main/3f08e56))
* **ci:** remove publishing patch ([#2208](https://github.com/openai/openai-python/issues/2208)) ([dd2dab7](https://raw.githubusercontent.com/openai/openai-python/main/dd2dab7))
* **types:** handle more discriminated union shapes ([#2206](https://github.com/openai/openai-python/issues/2206)) ([f85a9c6](https://raw.githubusercontent.com/openai/openai-python/main/f85a9c6))

### Chores

* **internal:** bump rye to 0.44.0 ([#2200](https://github.com/openai/openai-python/issues/2200)) ([2dd3139](https://raw.githubusercontent.com/openai/openai-python/main/2dd3139))
* **internal:** remove CI condition ([#2203](https://github.com/openai/openai-python/issues/2203)) ([9620fdc](https://raw.githubusercontent.com/openai/openai-python/main/9620fdc))
* **internal:** remove extra empty newlines ([#2195](https://github.com/openai/openai-python/issues/2195)) ([a1016a7](https://raw.githubusercontent.com/openai/openai-python/main/a1016a7))
* **internal:** update release workflows ([e2def44](https://raw.githubusercontent.com/openai/openai-python/main/e2def44))

## 1.66.3 (2025-03-12)

Full Changelog: [v1.66.2...v1.66.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.2...v1.66.3)

### Bug Fixes

* update module level client ([#2185](https://github.com/openai/openai-python/issues/2185)) ([456f324](https://raw.githubusercontent.com/openai/openai-python/main/456f324))

## 1.66.2 (2025-03-11)

Full Changelog: [v1.66.1...v1.66.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.1...v1.66.2)

### Bug Fixes

* **responses:** correct reasoning output type ([#2181](https://github.com/openai/openai-python/issues/2181)) ([8cb1129](https://raw.githubusercontent.com/openai/openai-python/main/8cb1129))

## 1.66.1 (2025-03-11)

Full Changelog: [v1.66.0...v1.66.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.66.0...v1.66.1)

### Bug Fixes

* **responses:** correct computer use enum value ([#2180](https://github.com/openai/openai-python/issues/2180)) ([48f4628](https://raw.githubusercontent.com/openai/openai-python/main/48f4628))

### Chores

* **internal:** temporary commit ([afabec1](https://raw.githubusercontent.com/openai/openai-python/main/afabec1))

## 1.66.0 (2025-03-11)

Full Changelog: [v1.65.5...v1.66.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.5...v1.66.0)

### Features

* **api:** add /v1/responses and built-in tools ([854df97](https://raw.githubusercontent.com/openai/openai-python/main/854df97))

### Chores

* export more types ([#2176](https://github.com/openai/openai-python/issues/2176)) ([a730f0e](https://raw.githubusercontent.com/openai/openai-python/main/a730f0e))

## 1.65.5 (2025-03-09)

Full Changelog: [v1.65.4...v1.65.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.4...v1.65.5)

### Chores

* move ChatModel type to shared ([#2167](https://github.com/openai/openai-python/issues/2167)) ([104f02a](https://raw.githubusercontent.com/openai/openai-python/main/104f02a))

## 1.65.4 (2025-03-05)

Full Changelog: [v1.65.3...v1.65.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.3...v1.65.4)

### Bug Fixes

* **api:** add missing file rank enum + more metadata ([#2164](https://github.com/openai/openai-python/issues/2164)) ([0387e48](https://raw.githubusercontent.com/openai/openai-python/main/0387e48))

## 1.65.3 (2025-03-04)

Full Changelog: [v1.65.2...v1.65.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.2...v1.65.3)

### Chores

* **internal:** remove unused http client options forwarding ([#2158](https://github.com/openai/openai-python/issues/2158)) ([76ec464](https://raw.githubusercontent.com/openai/openai-python/main/76ec464))
* **internal:** run example files in CI ([#2160](https://github.com/openai/openai-python/issues/2160)) ([9979345](https://raw.githubusercontent.com/openai/openai-python/main/9979345))

## 1.65.2 (2025-03-01)

Full Changelog: [v1.65.1...v1.65.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.1...v1.65.2)

### Bug Fixes

* **azure:** azure_deployment use with realtime + non-deployment-based APIs ([#2154](https://github.com/openai/openai-python/issues/2154)) ([5846b55](https://raw.githubusercontent.com/openai/openai-python/main/5846b55))

### Chores

* **docs:** update client docstring ([#2152](https://github.com/openai/openai-python/issues/2152)) ([0518c34](https://raw.githubusercontent.com/openai/openai-python/main/0518c34))

## 1.65.1 (2025-02-27)

Full Changelog: [v1.65.0...v1.65.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.65.0...v1.65.1)

### Documentation

* update URLs from stainlessapi.com to stainless.com ([#2150](https://github.com/openai/openai-python/issues/2150)) ([dee4298](https://raw.githubusercontent.com/openai/openai-python/main/dee4298))

## 1.65.0 (2025-02-27)

Full Changelog: [v1.64.0...v1.65.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.64.0...v1.65.0)

### Features

* **api:** add gpt-4.5-preview ([#2149](https://github.com/openai/openai-python/issues/2149)) ([4cee52e](https://raw.githubusercontent.com/openai/openai-python/main/4cee52e))

### Chores

* **internal:** properly set __pydantic_private__ ([#2144](https://github.com/openai/openai-python/issues/2144)) ([2b1bd16](https://raw.githubusercontent.com/openai/openai-python/main/2b1bd16))

## 1.64.0 (2025-02-22)

Full Changelog: [v1.63.2...v1.64.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.63.2...v1.64.0)

### Features

* **client:** allow passing `NotGiven` for body ([#2135](https://github.com/openai/openai-python/issues/2135)) ([4451f56](https://raw.githubusercontent.com/openai/openai-python/main/4451f56))

### Bug Fixes

* **client:** mark some request bodies as optional ([4451f56](https://raw.githubusercontent.com/openai/openai-python/main/4451f56))

### Chores

* **internal:** fix devcontainers setup ([#2137](https://github.com/openai/openai-python/issues/2137)) ([4d88402](https://raw.githubusercontent.com/openai/openai-python/main/4d88402))

## 1.63.2 (2025-02-17)

Full Changelog: [v1.63.1...v1.63.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.63.1...v1.63.2)

### Chores

* **internal:** revert temporary commit ([#2121](https://github.com/openai/openai-python/issues/2121)) ([72458ab](https://raw.githubusercontent.com/openai/openai-python/main/72458ab))

## 1.63.1 (2025-02-17)

Full Changelog: [v1.63.0...v1.63.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.63.0...v1.63.1)

### Chores

* **internal:** temporary commit ([#2121](https://github.com/openai/openai-python/issues/2121)) ([f7f8361](https://raw.githubusercontent.com/openai/openai-python/main/f7f8361))

## 1.63.0 (2025-02-13)

Full Changelog: [v1.62.0...v1.63.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.62.0...v1.63.0)

### Features

* **api:** add support for storing chat completions ([#2117](https://github.com/openai/openai-python/issues/2117)) ([2357a8f](https://raw.githubusercontent.com/openai/openai-python/main/2357a8f))

## 1.62.0 (2025-02-12)

Full Changelog: [v1.61.1...v1.62.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.61.1...v1.62.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#2094](https://github.com/openai/openai-python/issues/2094)) ([0288213](https://raw.githubusercontent.com/openai/openai-python/main/0288213))
* **embeddings:** use stdlib array type for improved performance ([#2060](https://github.com/openai/openai-python/issues/2060)) ([9a95db9](https://raw.githubusercontent.com/openai/openai-python/main/9a95db9))
* **pagination:** avoid fetching when has_more: false ([#2098](https://github.com/openai/openai-python/issues/2098)) ([1882483](https://raw.githubusercontent.com/openai/openai-python/main/1882483))

### Bug Fixes

* **api:** add missing reasoning effort + model enums ([#2096](https://github.com/openai/openai-python/issues/2096)) ([e0ca9f0](https://raw.githubusercontent.com/openai/openai-python/main/e0ca9f0))
* **parsing:** don't default to an empty array ([#2106](https://github.com/openai/openai-python/issues/2106)) ([8e748bb](https://raw.githubusercontent.com/openai/openai-python/main/8e748bb))

### Chores

* **internal:** fix type traversing dictionary params ([#2097](https://github.com/openai/openai-python/issues/2097)) ([4e5b368](https://raw.githubusercontent.com/openai/openai-python/main/4e5b368))
* **internal:** minor type handling changes ([#2099](https://github.com/openai/openai-python/issues/2099)) ([a2c6da0](https://raw.githubusercontent.com/openai/openai-python/main/a2c6da0))

## 1.61.1 (2025-02-05)

Full Changelog: [v1.61.0...v1.61.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.61.0...v1.61.1)

### Bug Fixes

* **api/types:** correct audio duration & role types ([#2091](https://github.com/openai/openai-python/issues/2091)) ([afcea48](https://raw.githubusercontent.com/openai/openai-python/main/afcea48))
* **cli/chat:** only send params when set ([#2077](https://github.com/openai/openai-python/issues/2077)) ([688b223](https://raw.githubusercontent.com/openai/openai-python/main/688b223))

### Chores

* **internal:** bummp ruff dependency ([#2080](https://github.com/openai/openai-python/issues/2080)) ([b7a80b1](https://raw.githubusercontent.com/openai/openai-python/main/b7a80b1))
* **internal:** change default timeout to an int ([#2079](https://github.com/openai/openai-python/issues/2079)) ([d3df1c6](https://raw.githubusercontent.com/openai/openai-python/main/d3df1c6))

## 1.61.0 (2025-01-31)

Full Changelog: [v1.60.2...v1.61.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.60.2...v1.61.0)

### Features

* **api:** add o3-mini ([#2067](https://github.com/openai/openai-python/issues/2067)) ([12b87a4](https://raw.githubusercontent.com/openai/openai-python/main/12b87a4))

### Bug Fixes

* **types:** correct metadata type + other fixes ([12b87a4](https://raw.githubusercontent.com/openai/openai-python/main/12b87a4))

### Chores

* **helpers:** section links ([ef8d3cc](https://raw.githubusercontent.com/openai/openai-python/main/ef8d3cc))
* **types:** fix Metadata types ([82d3156](https://raw.githubusercontent.com/openai/openai-python/main/82d3156))
* update api.md ([#2063](https://github.com/openai/openai-python/issues/2063)) ([21964f0](https://raw.githubusercontent.com/openai/openai-python/main/21964f0))

### Documentation

* **readme:** current section links ([#2055](https://github.com/openai/openai-python/issues/2055)) ([ef8d3cc](https://raw.githubusercontent.com/openai/openai-python/main/ef8d3cc))

## 1.60.2 (2025-01-27)

Full Changelog: [v1.60.1...v1.60.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.60.1...v1.60.2)

### Bug Fixes

* **parsing:** don't validate input tools in the asynchronous `.parse()` method ([6fcfe73](https://raw.githubusercontent.com/openai/openai-python/main/6fcfe73))

## 1.60.1 (2025-01-24)

Full Changelog: [v1.60.0...v1.60.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.60.0...v1.60.1)

### Chores

* **internal:** minor formatting changes ([#2050](https://github.com/openai/openai-python/issues/2050)) ([9c44192](https://raw.githubusercontent.com/openai/openai-python/main/9c44192))

### Documentation

* **examples/azure:** add async snippet ([#1787](https://github.com/openai/openai-python/issues/1787)) ([f60eda1](https://raw.githubusercontent.com/openai/openai-python/main/f60eda1))

## 1.60.0 (2025-01-22)

Full Changelog: [v1.59.9...v1.60.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.9...v1.60.0)

### Features

* **api:** update enum values, comments, and examples ([#2045](https://github.com/openai/openai-python/issues/2045)) ([e8205fd](https://raw.githubusercontent.com/openai/openai-python/main/e8205fd))

### Chores

* **internal:** minor style changes ([#2043](https://github.com/openai/openai-python/issues/2043)) ([89a9dd8](https://raw.githubusercontent.com/openai/openai-python/main/89a9dd8))

### Documentation

* **readme:** mention failed requests in request IDs ([5f7c30b](https://raw.githubusercontent.com/openai/openai-python/main/5f7c30b))

## 1.59.9 (2025-01-20)

Full Changelog: [v1.59.8...v1.59.9](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.8...v1.59.9)

### Bug Fixes

* **tests:** make test_get_platform less flaky ([#2040](https://github.com/openai/openai-python/issues/2040)) ([72ea05c](https://raw.githubusercontent.com/openai/openai-python/main/72ea05c))

### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#2041](https://github.com/openai/openai-python/issues/2041)) ([b901046](https://raw.githubusercontent.com/openai/openai-python/main/b901046))
* **internal:** update websockets dep ([#2036](https://github.com/openai/openai-python/issues/2036)) ([642cd11](https://raw.githubusercontent.com/openai/openai-python/main/642cd11))

### Documentation

* fix typo ([#2031](https://github.com/openai/openai-python/issues/2031)) ([02fcf15](https://raw.githubusercontent.com/openai/openai-python/main/02fcf15))
* **raw responses:** fix duplicate `the` ([#2039](https://github.com/openai/openai-python/issues/2039)) ([9b8eab9](https://raw.githubusercontent.com/openai/openai-python/main/9b8eab9))

## 1.59.8 (2025-01-17)

Full Changelog: [v1.59.7...v1.59.8](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.7...v1.59.8)

### Bug Fixes

* streaming ([c16f58e](https://raw.githubusercontent.com/openai/openai-python/main/c16f58e))
* **structured outputs:** avoid parsing empty empty content ([#2023](https://github.com/openai/openai-python/issues/2023)) ([6d3513c](https://raw.githubusercontent.com/openai/openai-python/main/6d3513c))
* **structured outputs:** correct schema coercion for inline ref expansion ([#2025](https://github.com/openai/openai-python/issues/2025)) ([2f4f0b3](https://raw.githubusercontent.com/openai/openai-python/main/2f4f0b3))
* **types:** correct type for vector store chunking strategy ([#2017](https://github.com/openai/openai-python/issues/2017)) ([e389279](https://raw.githubusercontent.com/openai/openai-python/main/e389279))

### Chores

* **examples:** update realtime model ([f26746c](https://raw.githubusercontent.com/openai/openai-python/main/f26746c)), closes [#2020](https://github.com/openai/openai-python/issues/2020)
* **internal:** bump pyright dependency ([#2021](https://github.com/openai/openai-python/issues/2021)) ([0a9a0f5](https://raw.githubusercontent.com/openai/openai-python/main/0a9a0f5))
* **internal:** streaming refactors ([#2012](https://github.com/openai/openai-python/issues/2012)) ([d76a748](https://raw.githubusercontent.com/openai/openai-python/main/d76a748))
* **internal:** update deps ([#2015](https://github.com/openai/openai-python/issues/2015)) ([514e0e4](https://raw.githubusercontent.com/openai/openai-python/main/514e0e4))

### Documentation

* **examples/azure:** example script with realtime API ([#1967](https://github.com/openai/openai-python/issues/1967)) ([84f2f9c](https://raw.githubusercontent.com/openai/openai-python/main/84f2f9c))

## 1.59.7 (2025-01-13)

Full Changelog: [v1.59.6...v1.59.7](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.6...v1.59.7)

### Chores

* export HttpxBinaryResponseContent class ([7191b71](https://raw.githubusercontent.com/openai/openai-python/main/7191b71))

## 1.59.6 (2025-01-09)

Full Changelog: [v1.59.5...v1.59.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.5...v1.59.6)

### Bug Fixes

* correctly handle deserialising `cls` fields ([#2002](https://github.com/openai/openai-python/issues/2002)) ([089c820](https://raw.githubusercontent.com/openai/openai-python/main/089c820))

### Chores

* **internal:** spec update ([#2000](https://github.com/openai/openai-python/issues/2000)) ([36548f8](https://raw.githubusercontent.com/openai/openai-python/main/36548f8))

## 1.59.5 (2025-01-08)

Full Changelog: [v1.59.4...v1.59.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.4...v1.59.5)

### Bug Fixes

* **client:** only call .close() when needed ([#1992](https://github.com/openai/openai-python/issues/1992)) ([bdfd699](https://raw.githubusercontent.com/openai/openai-python/main/bdfd699))

### Documentation

* fix typos ([#1995](https://github.com/openai/openai-python/issues/1995)) ([be694a0](https://raw.githubusercontent.com/openai/openai-python/main/be694a0))
* fix typos ([#1996](https://github.com/openai/openai-python/issues/1996)) ([714aed9](https://raw.githubusercontent.com/openai/openai-python/main/714aed9))
* more typo fixes ([#1998](https://github.com/openai/openai-python/issues/1998)) ([7bd92f0](https://raw.githubusercontent.com/openai/openai-python/main/7bd92f0))
* **readme:** moved period to inside parentheses ([#1980](https://github.com/openai/openai-python/issues/1980)) ([e7fae94](https://raw.githubusercontent.com/openai/openai-python/main/e7fae94))

## 1.59.4 (2025-01-07)

Full Changelog: [v1.59.3...v1.59.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.3...v1.59.4)

### Chores

* add missing isclass check ([#1988](https://github.com/openai/openai-python/issues/1988)) ([61d9072](https://raw.githubusercontent.com/openai/openai-python/main/61d9072))
* add missing isclass check for structured outputs ([bcbf013](https://raw.githubusercontent.com/openai/openai-python/main/bcbf013))
* **internal:** bump httpx dependency ([#1990](https://github.com/openai/openai-python/issues/1990)) ([288c2c3](https://raw.githubusercontent.com/openai/openai-python/main/288c2c3))

### Documentation

* **realtime:** fix event reference link ([9b6885d](https://raw.githubusercontent.com/openai/openai-python/main/9b6885d))

## 1.59.3 (2025-01-03)

Full Changelog: [v1.59.2...v1.59.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.2...v1.59.3)

### Chores

* **api:** bump spec version ([#1985](https://github.com/openai/openai-python/issues/1985)) ([c6f1b35](https://raw.githubusercontent.com/openai/openai-python/main/c6f1b35))

## 1.59.2 (2025-01-03)

Full Changelog: [v1.59.1...v1.59.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.1...v1.59.2)

### Chores

* **ci:** fix publish workflow ([0be1f5d](https://raw.githubusercontent.com/openai/openai-python/main/0be1f5d))
* **internal:** empty commit ([fe8dc2e](https://raw.githubusercontent.com/openai/openai-python/main/fe8dc2e))

## 1.59.1 (2025-01-02)

Full Changelog: [v1.59.0...v1.59.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.59.0...v1.59.1)

### Chores

* bump license year ([#1981](https://github.com/openai/openai-python/issues/1981)) ([f29011a](https://raw.githubusercontent.com/openai/openai-python/main/f29011a))

## 1.59.0 (2024-12-21)

Full Changelog: [v1.58.1...v1.59.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.58.1...v1.59.0)

### Features

* **azure:** support for the Realtime API ([#1963](https://github.com/openai/openai-python/issues/1963)) ([9fda141](https://raw.githubusercontent.com/openai/openai-python/main/9fda141))

### Chores

* **realtime:** update docstrings ([#1964](https://github.com/openai/openai-python/issues/1964)) ([3dee863](https://raw.githubusercontent.com/openai/openai-python/main/3dee863))

## 1.58.1 (2024-12-17)

Full Changelog: [v1.58.0...v1.58.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.58.0...v1.58.1)

### Documentation

* **readme:** fix example script link ([23ba877](https://raw.githubusercontent.com/openai/openai-python/main/23ba877))

## 1.58.0 (2024-12-17)

Full Changelog: [v1.57.4...v1.58.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.57.4...v1.58.0)

### Features

* add Realtime API support ([#1958](https://github.com/openai/openai-python/issues/1958)) ([97d73cf](https://raw.githubusercontent.com/openai/openai-python/main/97d73cf))
* **api:** new o1 and GPT-4o models + preference fine-tuning ([#1956](https://github.com/openai/openai-python/issues/1956)) ([ec22ffb](https://raw.githubusercontent.com/openai/openai-python/main/ec22ffb))

### Bug Fixes

* add reasoning_effort to all methods ([8829c32](https://raw.githubusercontent.com/openai/openai-python/main/8829c32))
* **assistants:** correctly send `include` query param ([9a4c69c](https://raw.githubusercontent.com/openai/openai-python/main/9a4c69c))
* **cli/migrate:** change grit binaries prefix ([#1951](https://github.com/openai/openai-python/issues/1951)) ([1c396c9](https://raw.githubusercontent.com/openai/openai-python/main/1c396c9))

### Chores

* **internal:** fix some typos ([#1955](https://github.com/openai/openai-python/issues/1955)) ([628dead](https://raw.githubusercontent.com/openai/openai-python/main/628dead))

### Documentation

* add examples + guidance on Realtime API support ([1cb00f8](https://raw.githubusercontent.com/openai/openai-python/main/1cb00f8))
* **readme:** example snippet for client context manager ([#1953](https://github.com/openai/openai-python/issues/1953)) ([ad80255](https://raw.githubusercontent.com/openai/openai-python/main/ad80255))

## 1.57.4 (2024-12-13)

Full Changelog: [v1.57.3...v1.57.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.57.3...v1.57.4)

### Chores

* **internal:** remove some duplicated imports ([#1946](https://github.com/openai/openai-python/issues/1946)) ([f94fddd](https://raw.githubusercontent.com/openai/openai-python/main/f94fddd))
* **internal:** updated imports ([#1948](https://github.com/openai/openai-python/issues/1948)) ([13971fc](https://raw.githubusercontent.com/openai/openai-python/main/13971fc))

## 1.57.3 (2024-12-12)

Full Changelog: [v1.57.2...v1.57.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.57.2...v1.57.3)

### Chores

* **internal:** add support for TypeAliasType ([#1942](https://github.com/openai/openai-python/issues/1942)) ([d3442ff](https://raw.githubusercontent.com/openai/openai-python/main/d3442ff))
* **internal:** bump pyright ([#1939](https://github.com/openai/openai-python/issues/1939)) ([190d1a8](https://raw.githubusercontent.com/openai/openai-python/main/190d1a8))

## 1.57.2 (2024-12-10)

Full Changelog: [v1.57.1...v1.57.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.57.1...v1.57.2)

### Bug Fixes

* **azure:** handle trailing slash in `azure_endpoint` ([#1935](https://github.com/openai/openai-python/issues/1935)) ([69b73c5](https://raw.githubusercontent.com/openai/openai-python/main/69b73c5))

### Documentation

* **readme:** fix http client proxies example ([#1932](https://github.com/openai/openai-python/issues/1932)) ([7a83e0f](https://raw.githubusercontent.com/openai/openai-python/main/7a83e0f))

## 1.57.1 (2024-12-09)

Full Changelog: [v1.57.0...v1.57.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.57.0...v1.57.1)

### Chores

* **internal:** bump pydantic dependency ([#1929](https://github.com/openai/openai-python/issues/1929)) ([5227c95](https://raw.githubusercontent.com/openai/openai-python/main/5227c95))

## 1.57.0 (2024-12-05)

Full Changelog: [v1.56.2...v1.57.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.56.2...v1.57.0)

### Features

* **api:** updates ([#1924](https://github.com/openai/openai-python/issues/1924)) ([82ba614](https://raw.githubusercontent.com/openai/openai-python/main/82ba614))

### Chores

* bump openapi url ([#1922](https://github.com/openai/openai-python/issues/1922)) ([a472a8f](https://raw.githubusercontent.com/openai/openai-python/main/a472a8f))

## 1.56.2 (2024-12-04)

Full Changelog: [v1.56.1...v1.56.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.56.1...v1.56.2)

### Chores

* make the `Omit` type public ([#1919](https://github.com/openai/openai-python/issues/1919)) ([4fb8a1c](https://raw.githubusercontent.com/openai/openai-python/main/4fb8a1c))

## 1.56.1 (2024-12-03)

Full Changelog: [v1.56.0...v1.56.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.56.0...v1.56.1)

### Bug Fixes

* **cli:** remove usage of httpx proxies ([0e9fc3d](https://raw.githubusercontent.com/openai/openai-python/main/0e9fc3d))

### Chores

* **internal:** bump pyright ([#1917](https://github.com/openai/openai-python/issues/1917)) ([0e87346](https://raw.githubusercontent.com/openai/openai-python/main/0e87346))

## 1.56.0 (2024-12-02)

Full Changelog: [v1.55.3...v1.56.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.55.3...v1.56.0)

### Features

* **client:** make ChatCompletionStreamState public ([#1898](https://github.com/openai/openai-python/issues/1898)) ([dc7f6cb](https://raw.githubusercontent.com/openai/openai-python/main/dc7f6cb))

## 1.55.3 (2024-11-28)

Full Changelog: [v1.55.2...v1.55.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.55.2...v1.55.3)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#1904](https://github.com/openai/openai-python/issues/1904)) ([72b6c63](https://raw.githubusercontent.com/openai/openai-python/main/72b6c63))

## 1.55.2 (2024-11-27)

Full Changelog: [v1.55.1...v1.55.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.55.1...v1.55.2)

### Chores

* **internal:** exclude mypy from running on tests ([#1899](https://github.com/openai/openai-python/issues/1899)) ([e2496f1](https://raw.githubusercontent.com/openai/openai-python/main/e2496f1))

### Documentation

* **assistants:** correct on_text_delta example ([#1896](https://github.com/openai/openai-python/issues/1896)) ([460b663](https://raw.githubusercontent.com/openai/openai-python/main/460b663))

## 1.55.1 (2024-11-25)

Full Changelog: [v1.55.0...v1.55.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.55.0...v1.55.1)

### Bug Fixes

* **pydantic-v1:** avoid runtime error for assistants streaming ([#1885](https://github.com/openai/openai-python/issues/1885)) ([197c94b](https://raw.githubusercontent.com/openai/openai-python/main/197c94b))

### Chores

* remove now unused `cached-property` dep ([#1867](https://github.com/openai/openai-python/issues/1867)) ([df5fac1](https://raw.githubusercontent.com/openai/openai-python/main/df5fac1))
* remove now unused `cached-property` dep ([#1891](https://github.com/openai/openai-python/issues/1891)) ([feebaae](https://raw.githubusercontent.com/openai/openai-python/main/feebaae))

### Documentation

* add info log level to readme ([#1887](https://github.com/openai/openai-python/issues/1887)) ([358255d](https://raw.githubusercontent.com/openai/openai-python/main/358255d))

## 1.55.0 (2024-11-20)

Full Changelog: [v1.54.5...v1.55.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.5...v1.55.0)

### Features

* **api:** add gpt-4o-2024-11-20 model ([#1877](https://github.com/openai/openai-python/issues/1877)) ([ff64c2a](https://raw.githubusercontent.com/openai/openai-python/main/ff64c2a))

## 1.54.5 (2024-11-19)

Full Changelog: [v1.54.4...v1.54.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.4...v1.54.5)

### Bug Fixes

* **asyncify:** avoid hanging process under certain conditions ([#1853](https://github.com/openai/openai-python/issues/1853)) ([3d23437](https://raw.githubusercontent.com/openai/openai-python/main/3d23437))

### Chores

* **internal:** minor test changes ([#1874](https://github.com/openai/openai-python/issues/1874)) ([189339d](https://raw.githubusercontent.com/openai/openai-python/main/189339d))
* **internal:** spec update ([#1873](https://github.com/openai/openai-python/issues/1873)) ([24c81f7](https://raw.githubusercontent.com/openai/openai-python/main/24c81f7))
* **tests:** limit array example length ([#1870](https://github.com/openai/openai-python/issues/1870)) ([1e550df](https://raw.githubusercontent.com/openai/openai-python/main/1e550df))

## 1.54.4 (2024-11-12)

Full Changelog: [v1.54.3...v1.54.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.3...v1.54.4)

### Bug Fixes

* don't use dicts as iterables in transform ([#1865](https://github.com/openai/openai-python/issues/1865)) ([76a51b1](https://raw.githubusercontent.com/openai/openai-python/main/76a51b1))

### Documentation

* bump models in example snippets to gpt-4o ([#1861](https://github.com/openai/openai-python/issues/1861)) ([adafe08](https://raw.githubusercontent.com/openai/openai-python/main/adafe08))
* move comments in example snippets ([#1860](https://github.com/openai/openai-python/issues/1860)) ([362cf74](https://raw.githubusercontent.com/openai/openai-python/main/362cf74))
* **readme:** add missing asyncio import ([#1858](https://github.com/openai/openai-python/issues/1858)) ([dec9d0c](https://raw.githubusercontent.com/openai/openai-python/main/dec9d0c))

## 1.54.3 (2024-11-06)

Full Changelog: [v1.54.2...v1.54.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.2...v1.54.3)

### Bug Fixes

* **logs:** redact sensitive headers ([#1850](https://github.com/openai/openai-python/issues/1850)) ([466608f](https://raw.githubusercontent.com/openai/openai-python/main/466608f))

## 1.54.2 (2024-11-06)

Full Changelog: [v1.54.1...v1.54.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.1...v1.54.2)

### Chores

* **tests:** adjust retry timeout values ([#1851](https://github.com/openai/openai-python/issues/1851)) ([cc8009c](https://raw.githubusercontent.com/openai/openai-python/main/cc8009c))

## 1.54.1 (2024-11-05)

Full Changelog: [v1.54.0...v1.54.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.54.0...v1.54.1)

### Bug Fixes

* add new prediction param to all methods ([6aa424d](https://raw.githubusercontent.com/openai/openai-python/main/6aa424d))

## 1.54.0 (2024-11-04)

Full Changelog: [v1.53.1...v1.54.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.53.1...v1.54.0)

### Features

* **api:** add support for predicted outputs ([#1847](https://github.com/openai/openai-python/issues/1847)) ([42a4103](https://raw.githubusercontent.com/openai/openai-python/main/42a4103))
* **project:** drop support for Python 3.7 ([#1845](https://github.com/openai/openai-python/issues/1845)) ([0ed5b1a](https://raw.githubusercontent.com/openai/openai-python/main/0ed5b1a))

## 1.53.1 (2024-11-04)

Full Changelog: [v1.53.0...v1.53.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.53.0...v1.53.1)

### Bug Fixes

* don't use dicts as iterables in transform ([#1842](https://github.com/openai/openai-python/issues/1842)) ([258f265](https://raw.githubusercontent.com/openai/openai-python/main/258f265))
* support json safe serialization for basemodel subclasses ([#1844](https://github.com/openai/openai-python/issues/1844)) ([2b80c90](https://raw.githubusercontent.com/openai/openai-python/main/2b80c90))

### Chores

* **internal:** bump mypy ([#1839](https://github.com/openai/openai-python/issues/1839)) ([d92f959](https://raw.githubusercontent.com/openai/openai-python/main/d92f959))

## 1.53.0 (2024-10-30)

Full Changelog: [v1.52.2...v1.53.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.52.2...v1.53.0)

### Features

* **api:** add new, expressive voices for Realtime and Audio in Chat Completions ([7cf0a49](https://raw.githubusercontent.com/openai/openai-python/main/7cf0a49))

### Chores

* **internal:** bump pytest to v8 & pydantic ([#1829](https://github.com/openai/openai-python/issues/1829)) ([0e67a8a](https://raw.githubusercontent.com/openai/openai-python/main/0e67a8a))

## 1.52.2 (2024-10-23)

Full Changelog: [v1.52.1...v1.52.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.52.1...v1.52.2)

### Chores

* **internal:** update spec version ([#1816](https://github.com/openai/openai-python/issues/1816)) ([c23282a](https://raw.githubusercontent.com/openai/openai-python/main/c23282a))

## 1.52.1 (2024-10-22)

Full Changelog: [v1.52.0...v1.52.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.52.0...v1.52.1)

### Bug Fixes

* **client/async:** correctly retry in all cases ([#1803](https://github.com/openai/openai-python/issues/1803)) ([9fe3f3f](https://raw.githubusercontent.com/openai/openai-python/main/9fe3f3f))

### Chores

* **internal:** bump ruff dependency ([#1801](https://github.com/openai/openai-python/issues/1801)) ([859c672](https://raw.githubusercontent.com/openai/openai-python/main/859c672))
* **internal:** remove unused black config ([#1807](https://github.com/openai/openai-python/issues/1807)) ([112dab0](https://raw.githubusercontent.com/openai/openai-python/main/112dab0))
* **internal:** update spec version ([#1810](https://github.com/openai/openai-python/issues/1810)) ([aa25b7b](https://raw.githubusercontent.com/openai/openai-python/main/aa25b7b))
* **internal:** update test syntax ([#1798](https://github.com/openai/openai-python/issues/1798)) ([d3098dd](https://raw.githubusercontent.com/openai/openai-python/main/d3098dd))
* **tests:** add more retry tests ([#1806](https://github.com/openai/openai-python/issues/1806)) ([5525a1b](https://raw.githubusercontent.com/openai/openai-python/main/5525a1b))

## 1.52.0 (2024-10-17)

Full Changelog: [v1.51.2...v1.52.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.51.2...v1.52.0)

### Features

* **api:** add gpt-4o-audio-preview model for chat completions ([#1796](https://github.com/openai/openai-python/issues/1796)) ([fbf1e0c](https://raw.githubusercontent.com/openai/openai-python/main/fbf1e0c))

## 1.51.2 (2024-10-08)

Full Changelog: [v1.51.1...v1.51.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.51.1...v1.51.2)

### Chores

* add repr to PageInfo class ([#1780](https://github.com/openai/openai-python/issues/1780)) ([63118ee](https://raw.githubusercontent.com/openai/openai-python/main/63118ee))

## 1.51.1 (2024-10-07)

Full Changelog: [v1.51.0...v1.51.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.51.0...v1.51.1)

### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#1779](https://github.com/openai/openai-python/issues/1779)) ([fb1dacf](https://raw.githubusercontent.com/openai/openai-python/main/fb1dacf))

### Chores

* **internal:** add support for parsing bool response content ([#1774](https://github.com/openai/openai-python/issues/1774)) ([aa2e25f](https://raw.githubusercontent.com/openai/openai-python/main/aa2e25f))

### Documentation

* fix typo in fenced code block language ([#1769](https://github.com/openai/openai-python/issues/1769)) ([57bbc15](https://raw.githubusercontent.com/openai/openai-python/main/57bbc15))
* improve and reference contributing documentation ([#1767](https://github.com/openai/openai-python/issues/1767)) ([a985a8b](https://raw.githubusercontent.com/openai/openai-python/main/a985a8b))

## 1.51.0 (2024-10-01)

Full Changelog: [v1.50.2...v1.51.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.50.2...v1.51.0)

### Features

* **api:** support storing chat completions, enabling evals and model distillation in the dashboard ([2840c6d](https://raw.githubusercontent.com/openai/openai-python/main/2840c6d))

### Chores

* **docs:** fix maxium typo ([#1762](https://github.com/openai/openai-python/issues/1762)) ([de94553](https://raw.githubusercontent.com/openai/openai-python/main/de94553))
* **internal:** remove ds store ([47a3968](https://raw.githubusercontent.com/openai/openai-python/main/47a3968))

### Documentation

* **helpers:** fix method name typo ([#1764](https://github.com/openai/openai-python/issues/1764)) ([e1bcfe8](https://raw.githubusercontent.com/openai/openai-python/main/e1bcfe8))

## 1.50.2 (2024-09-27)

Full Changelog: [v1.50.1...v1.50.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.50.1...v1.50.2)

### Bug Fixes

* **audio:** correct types for transcriptions / translations ([#1755](https://github.com/openai/openai-python/issues/1755)) ([76c1f3f](https://raw.githubusercontent.com/openai/openai-python/main/76c1f3f))

## 1.50.1 (2024-09-27)

Full Changelog: [v1.50.0...v1.50.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.50.0...v1.50.1)

### Documentation

* **helpers:** fix chat completion anchor ([#1753](https://github.com/openai/openai-python/issues/1753)) ([956d4e8](https://raw.githubusercontent.com/openai/openai-python/main/956d4e8))

## 1.50.0 (2024-09-26)

Full Changelog: [v1.49.0...v1.50.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.49.0...v1.50.0)

### Features

* **structured outputs:** add support for accessing raw responses ([#1748](https://github.com/openai/openai-python/issues/1748)) ([0189e28](https://raw.githubusercontent.com/openai/openai-python/main/0189e28))

### Chores

* **pydantic v1:** exclude specific properties when rich printing ([#1751](https://github.com/openai/openai-python/issues/1751)) ([af535ce](https://raw.githubusercontent.com/openai/openai-python/main/af535ce))

## 1.49.0 (2024-09-26)

Full Changelog: [v1.48.0...v1.49.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.48.0...v1.49.0)

### Features

* **api:** add omni-moderation model ([#1750](https://github.com/openai/openai-python/issues/1750)) ([05b50da](https://raw.githubusercontent.com/openai/openai-python/main/05b50da))

### Chores

* **internal:** update test snapshots ([#1749](https://github.com/openai/openai-python/issues/1749)) ([42f054e](https://raw.githubusercontent.com/openai/openai-python/main/42f054e))

## 1.48.0 (2024-09-25)

Full Changelog: [v1.47.1...v1.48.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.47.1...v1.48.0)

### Features

* **client:** allow overriding retry count header ([#1745](https://github.com/openai/openai-python/issues/1745)) ([9f07d4d](https://raw.githubusercontent.com/openai/openai-python/main/9f07d4d))

### Bug Fixes

* **audio:** correct response_format translations type ([#1743](https://github.com/openai/openai-python/issues/1743)) ([b912108](https://raw.githubusercontent.com/openai/openai-python/main/b912108))

### Chores

* **internal:** use `typing_extensions.overload` instead of `typing` ([#1740](https://github.com/openai/openai-python/issues/1740)) ([2522bd5](https://raw.githubusercontent.com/openai/openai-python/main/2522bd5))

## 1.47.1 (2024-09-23)

Full Changelog: [v1.47.0...v1.47.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.47.0...v1.47.1)

### Bug Fixes

* **pydantic v1:** avoid warnings error ([1e8e7d1](https://raw.githubusercontent.com/openai/openai-python/main/1e8e7d1))

## 1.47.0 (2024-09-20)

Full Changelog: [v1.46.1...v1.47.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.46.1...v1.47.0)

### Features

* **client:** send retry count header ([21b0c00](https://raw.githubusercontent.com/openai/openai-python/main/21b0c00))

### Chores

* **types:** improve type name for embedding models ([#1730](https://github.com/openai/openai-python/issues/1730)) ([4b4eb2b](https://raw.githubusercontent.com/openai/openai-python/main/4b4eb2b))

## 1.46.1 (2024-09-19)

Full Changelog: [v1.46.0...v1.46.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.46.0...v1.46.1)

### Bug Fixes

* **client:** handle domains with underscores ([#1726](https://github.com/openai/openai-python/issues/1726)) ([cd194df](https://raw.githubusercontent.com/openai/openai-python/main/cd194df))

### Chores

* **streaming:** silence pydantic model_dump warnings ([#1722](https://github.com/openai/openai-python/issues/1722)) ([30f84b9](https://raw.githubusercontent.com/openai/openai-python/main/30f84b9))

## 1.46.0 (2024-09-17)

Full Changelog: [v1.45.1...v1.46.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.45.1...v1.46.0)

### Features

* **client:** add ._request_id property to object responses ([#1707](https://github.com/openai/openai-python/issues/1707)) ([8b3da05](https://raw.githubusercontent.com/openai/openai-python/main/8b3da05))

### Documentation

* **readme:** add examples for chat with image content ([#1703](https://github.com/openai/openai-python/issues/1703)) ([192b8f2](https://raw.githubusercontent.com/openai/openai-python/main/192b8f2))

## 1.45.1 (2024-09-16)

Full Changelog: [v1.45.0...v1.45.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.45.0...v1.45.1)

### Chores

* **internal:** bump pyright / mypy version ([#1717](https://github.com/openai/openai-python/issues/1717)) ([351af85](https://raw.githubusercontent.com/openai/openai-python/main/351af85))
* **internal:** bump ruff ([#1714](https://github.com/openai/openai-python/issues/1714)) ([aceaf64](https://raw.githubusercontent.com/openai/openai-python/main/aceaf64))
* **internal:** update spec link ([#1716](https://github.com/openai/openai-python/issues/1716)) ([ca58c7f](https://raw.githubusercontent.com/openai/openai-python/main/ca58c7f))

### Documentation

* update CONTRIBUTING.md ([#1710](https://github.com/openai/openai-python/issues/1710)) ([4d45eb5](https://raw.githubusercontent.com/openai/openai-python/main/4d45eb5))

## 1.45.0 (2024-09-12)

Full Changelog: [v1.44.1...v1.45.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.44.1...v1.45.0)

### Features

* **api:** add o1 models ([#1708](https://github.com/openai/openai-python/issues/1708)) ([06bd42e](https://raw.githubusercontent.com/openai/openai-python/main/06bd42e))
* **errors:** include completion in LengthFinishReasonError ([#1701](https://github.com/openai/openai-python/issues/1701)) ([b0e3256](https://raw.githubusercontent.com/openai/openai-python/main/b0e3256))

### Bug Fixes

* **types:** correctly mark stream discriminator as optional ([#1706](https://github.com/openai/openai-python/issues/1706)) ([80f02f9](https://raw.githubusercontent.com/openai/openai-python/main/80f02f9))

## 1.44.1 (2024-09-09)

Full Changelog: [v1.44.0...v1.44.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.44.0...v1.44.1)

### Chores

* add docstrings to raw response properties ([#1696](https://github.com/openai/openai-python/issues/1696)) ([1d2a19b](https://raw.githubusercontent.com/openai/openai-python/main/1d2a19b))

### Documentation

* **readme:** add section on determining installed version ([#1697](https://github.com/openai/openai-python/issues/1697)) ([0255735](https://raw.githubusercontent.com/openai/openai-python/main/0255735))
* **readme:** improve custom `base_url` example ([#1694](https://github.com/openai/openai-python/issues/1694)) ([05eec8a](https://raw.githubusercontent.com/openai/openai-python/main/05eec8a))

## 1.44.0 (2024-09-06)

Full Changelog: [v1.43.1...v1.44.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.43.1...v1.44.0)

### Features

* **vector store:** improve chunking strategy type names ([#1690](https://github.com/openai/openai-python/issues/1690)) ([e82cd85](https://raw.githubusercontent.com/openai/openai-python/main/e82cd85))

## 1.43.1 (2024-09-05)

Full Changelog: [v1.43.0...v1.43.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.43.0...v1.43.1)

### Chores

* pyproject.toml formatting changes ([#1687](https://github.com/openai/openai-python/issues/1687)) ([3387ede](https://raw.githubusercontent.com/openai/openai-python/main/3387ede))

## 1.43.0 (2024-08-29)

Full Changelog: [v1.42.0...v1.43.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.42.0...v1.43.0)

### Features

* **api:** add file search result details to run steps ([#1681](https://github.com/openai/openai-python/issues/1681)) ([f5449c0](https://raw.githubusercontent.com/openai/openai-python/main/f5449c0))

## 1.42.0 (2024-08-20)

Full Changelog: [v1.41.1...v1.42.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.41.1...v1.42.0)

### Features

* **parsing:** add support for pydantic dataclasses ([#1655](https://github.com/openai/openai-python/issues/1655)) ([101bee9](https://raw.githubusercontent.com/openai/openai-python/main/101bee9))

### Chores

* **ci:** also run pydantic v1 tests ([#1666](https://github.com/openai/openai-python/issues/1666)) ([af2a1ca](https://raw.githubusercontent.com/openai/openai-python/main/af2a1ca))

## 1.41.1 (2024-08-19)

Full Changelog: [v1.41.0...v1.41.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.41.0...v1.41.1)

### Bug Fixes

* **json schema:** remove `None` defaults ([#1663](https://github.com/openai/openai-python/issues/1663)) ([30215c1](https://raw.githubusercontent.com/openai/openai-python/main/30215c1))

### Chores

* **client:** fix parsing union responses when non-json is returned ([#1665](https://github.com/openai/openai-python/issues/1665)) ([822c37d](https://raw.githubusercontent.com/openai/openai-python/main/822c37d))

## 1.41.0 (2024-08-16)

Full Changelog: [v1.40.8...v1.41.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.8...v1.41.0)

### Features

* **client:** add uploads.upload_file helper ([aae079d](https://raw.githubusercontent.com/openai/openai-python/main/aae079d))

## 1.40.8 (2024-08-15)

Full Changelog: [v1.40.7...v1.40.8](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.7...v1.40.8)

### Chores

* **types:** define FilePurpose enum ([#1653](https://github.com/openai/openai-python/issues/1653)) ([3c2eeae](https://raw.githubusercontent.com/openai/openai-python/main/3c2eeae))

## 1.40.7 (2024-08-15)

Full Changelog: [v1.40.6...v1.40.7](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.6...v1.40.7)

### Bug Fixes

* **cli/migrate:** change grit binaries download source ([#1649](https://github.com/openai/openai-python/issues/1649)) ([85e8935](https://raw.githubusercontent.com/openai/openai-python/main/85e8935))

### Chores

* **docs:** fix typo in example snippet ([4e83b57](https://raw.githubusercontent.com/openai/openai-python/main/4e83b57))
* **internal:** use different 32bit detection method ([#1652](https://github.com/openai/openai-python/issues/1652)) ([5831af6](https://raw.githubusercontent.com/openai/openai-python/main/5831af6))

## 1.40.6 (2024-08-12)

Full Changelog: [v1.40.5...v1.40.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.5...v1.40.6)

### Chores

* **examples:** minor formatting changes ([#1644](https://github.com/openai/openai-python/issues/1644)) ([e08acf1](https://raw.githubusercontent.com/openai/openai-python/main/e08acf1))
* **internal:** update some imports ([#1642](https://github.com/openai/openai-python/issues/1642)) ([fce1ea7](https://raw.githubusercontent.com/openai/openai-python/main/fce1ea7))
* sync openapi url ([#1646](https://github.com/openai/openai-python/issues/1646)) ([8ae3801](https://raw.githubusercontent.com/openai/openai-python/main/8ae3801))
* **tests:** fix pydantic v1 tests ([2623630](https://raw.githubusercontent.com/openai/openai-python/main/2623630))

## 1.40.5 (2024-08-12)

Full Changelog: [v1.40.4...v1.40.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.4...v1.40.5)

### Documentation

* **helpers:** make async client usage more clear ([34e1edf](https://raw.githubusercontent.com/openai/openai-python/main/34e1edf)), closes [#1639](https://github.com/openai/openai-python/issues/1639)

## 1.40.4 (2024-08-12)

Full Changelog: [v1.40.3...v1.40.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.3...v1.40.4)

### Bug Fixes

* **json schema:** unravel `$ref`s alongside additional keys ([c7a3d29](https://raw.githubusercontent.com/openai/openai-python/main/c7a3d29))
* **json schema:** unwrap `allOf`s with one entry ([53d964d](https://raw.githubusercontent.com/openai/openai-python/main/53d964d))

## 1.40.3 (2024-08-10)

Full Changelog: [v1.40.2...v1.40.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.2...v1.40.3)

### Chores

* **ci:** bump prism mock server version ([#1630](https://github.com/openai/openai-python/issues/1630)) ([214d8fd](https://raw.githubusercontent.com/openai/openai-python/main/214d8fd))
* **ci:** codeowners file ([#1627](https://github.com/openai/openai-python/issues/1627)) ([c059a20](https://raw.githubusercontent.com/openai/openai-python/main/c059a20))
* **internal:** ensure package is importable in lint cmd ([#1631](https://github.com/openai/openai-python/issues/1631)) ([779e6d0](https://raw.githubusercontent.com/openai/openai-python/main/779e6d0))

## 1.40.2 (2024-08-08)

Full Changelog: [v1.40.1...v1.40.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.1...v1.40.2)

### Bug Fixes

* **client:** raise helpful error message for response_format misuse ([18191da](https://raw.githubusercontent.com/openai/openai-python/main/18191da))
* **json schema:** support recursive BaseModels in Pydantic v1 ([#1623](https://github.com/openai/openai-python/issues/1623)) ([43e10c0](https://raw.githubusercontent.com/openai/openai-python/main/43e10c0))

### Chores

* **internal:** format some docstrings ([d34a081](https://raw.githubusercontent.com/openai/openai-python/main/d34a081))
* **internal:** updates ([#1624](https://github.com/openai/openai-python/issues/1624)) ([598e7a2](https://raw.githubusercontent.com/openai/openai-python/main/598e7a2))

## 1.40.1 (2024-08-07)

Full Changelog: [v1.40.0...v1.40.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.40.0...v1.40.1)

### Chores

* **internal:** update OpenAPI spec url ([#1608](https://github.com/openai/openai-python/issues/1608)) ([5392753](https://raw.githubusercontent.com/openai/openai-python/main/5392753))
* **internal:** update test snapshots ([a11d1cb](https://raw.githubusercontent.com/openai/openai-python/main/a11d1cb))

## 1.40.0 (2024-08-06)

Full Changelog: [v1.39.0...v1.40.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.39.0...v1.40.0)

### Features

* **api:** add structured outputs support ([e8dba7d](https://raw.githubusercontent.com/openai/openai-python/main/e8dba7d))

### Chores

* **internal:** bump ruff version ([#1604](https://github.com/openai/openai-python/issues/1604)) ([3e19a87](https://raw.githubusercontent.com/openai/openai-python/main/3e19a87))
* **internal:** update pydantic compat helper function ([#1607](https://github.com/openai/openai-python/issues/1607)) ([973c18b](https://raw.githubusercontent.com/openai/openai-python/main/973c18b))

## 1.39.0 (2024-08-05)

Full Changelog: [v1.38.0...v1.39.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.38.0...v1.39.0)

### Features

* **client:** add `retries_taken` to raw response class ([#1601](https://github.com/openai/openai-python/issues/1601)) ([777822b](https://raw.githubusercontent.com/openai/openai-python/main/777822b))

### Bug Fixes

* **assistants:** add parallel_tool_calls param to runs.stream ([113e82a](https://raw.githubusercontent.com/openai/openai-python/main/113e82a))

### Chores

* **internal:** bump pyright ([#1599](https://github.com/openai/openai-python/issues/1599)) ([27f0f10](https://raw.githubusercontent.com/openai/openai-python/main/27f0f10))
* **internal:** test updates ([#1602](https://github.com/openai/openai-python/issues/1602)) ([af22d80](https://raw.githubusercontent.com/openai/openai-python/main/af22d80))
* **internal:** use `TypeAlias` marker for type assignments ([#1597](https://github.com/openai/openai-python/issues/1597)) ([5907ea0](https://raw.githubusercontent.com/openai/openai-python/main/5907ea0))

## 1.38.0 (2024-08-02)

Full Changelog: [v1.37.2...v1.38.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.37.2...v1.38.0)

### Features

* extract out `ImageModel`, `AudioModel`, `SpeechModel` ([#1586](https://github.com/openai/openai-python/issues/1586)) ([b800316](https://raw.githubusercontent.com/openai/openai-python/main/b800316))
* make enums not nominal ([#1588](https://github.com/openai/openai-python/issues/1588)) ([ab4519b](https://raw.githubusercontent.com/openai/openai-python/main/ab4519b))

## 1.37.2 (2024-08-01)

Full Changelog: [v1.37.1...v1.37.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.37.1...v1.37.2)

### Chores

* **internal:** add type construction helper ([#1584](https://github.com/openai/openai-python/issues/1584)) ([cbb186a](https://raw.githubusercontent.com/openai/openai-python/main/cbb186a))
* **runs/create_and_poll:** add parallel_tool_calls request param ([04b3e6c](https://raw.githubusercontent.com/openai/openai-python/main/04b3e6c))

## 1.37.1 (2024-07-25)

Full Changelog: [v1.37.0...v1.37.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.37.0...v1.37.1)

### Chores

* **tests:** update prism version ([#1572](https://github.com/openai/openai-python/issues/1572)) ([af82593](https://raw.githubusercontent.com/openai/openai-python/main/af82593))

## 1.37.0 (2024-07-22)

Full Changelog: [v1.36.1...v1.37.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.36.1...v1.37.0)

### Features

* **api:** add uploads endpoints ([#1568](https://github.com/openai/openai-python/issues/1568)) ([d877b6d](https://raw.githubusercontent.com/openai/openai-python/main/d877b6d))

### Bug Fixes

* **cli/audio:** handle non-json response format ([#1557](https://github.com/openai/openai-python/issues/1557)) ([bb7431f](https://raw.githubusercontent.com/openai/openai-python/main/bb7431f))

### Documentation

* **readme:** fix example snippet imports ([#1569](https://github.com/openai/openai-python/issues/1569)) ([0c90af6](https://raw.githubusercontent.com/openai/openai-python/main/0c90af6))

## 1.36.1 (2024-07-20)

Full Changelog: [v1.36.0...v1.36.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.36.0...v1.36.1)

### Bug Fixes

* **types:** add gpt-4o-mini to more assistants methods ([39a8a37](https://raw.githubusercontent.com/openai/openai-python/main/39a8a37))

## 1.36.0 (2024-07-19)

Full Changelog: [v1.35.15...v1.36.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.15...v1.36.0)

### Features

* **api:** add new gpt-4o-mini models ([#1561](https://github.com/openai/openai-python/issues/1561)) ([5672ad4](https://raw.githubusercontent.com/openai/openai-python/main/5672ad4))

## 1.35.15 (2024-07-18)

Full Changelog: [v1.35.14...v1.35.15](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.14...v1.35.15)

### Chores

* **docs:** document how to do per-request http client customization ([#1560](https://github.com/openai/openai-python/issues/1560)) ([24c0768](https://raw.githubusercontent.com/openai/openai-python/main/24c0768))
* **internal:** update formatting ([#1553](https://github.com/openai/openai-python/issues/1553)) ([e1389bc](https://raw.githubusercontent.com/openai/openai-python/main/e1389bc))

## 1.35.14 (2024-07-15)

Full Changelog: [v1.35.13...v1.35.14](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.13...v1.35.14)

### Chores

* **docs:** minor update to formatting of API link in README ([#1550](https://github.com/openai/openai-python/issues/1550)) ([a6e59c6](https://raw.githubusercontent.com/openai/openai-python/main/a6e59c6))
* **internal:** minor formatting changes ([ee1c62e](https://raw.githubusercontent.com/openai/openai-python/main/ee1c62e))
* **internal:** minor options / compat functions updates ([#1549](https://github.com/openai/openai-python/issues/1549)) ([a0701b5](https://raw.githubusercontent.com/openai/openai-python/main/a0701b5))

## 1.35.13 (2024-07-10)

Full Changelog: [v1.35.12...v1.35.13](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.12...v1.35.13)

### Bug Fixes

* **threads/runs/create_and_run_stream:** correct tool_resources param ([8effd08](https://raw.githubusercontent.com/openai/openai-python/main/8effd08))

### Chores

* **internal:** add helper function ([#1538](https://github.com/openai/openai-python/issues/1538)) ([81655a0](https://raw.githubusercontent.com/openai/openai-python/main/81655a0))

## 1.35.12 (2024-07-09)

Full Changelog: [v1.35.11...v1.35.12](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.11...v1.35.12)

### Bug Fixes

* **azure:** refresh auth token during retries ([#1533](https://github.com/openai/openai-python/issues/1533)) ([287926e](https://raw.githubusercontent.com/openai/openai-python/main/287926e))
* **tests:** fresh_env() now resets new environment values ([64da888](https://raw.githubusercontent.com/openai/openai-python/main/64da888))

## 1.35.11 (2024-07-09)

Full Changelog: [v1.35.10...v1.35.11](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.10...v1.35.11)

### Chores

* **internal:** minor request options handling changes ([#1534](https://github.com/openai/openai-python/issues/1534)) ([8b0e493](https://raw.githubusercontent.com/openai/openai-python/main/8b0e493))

## 1.35.10 (2024-07-03)

Full Changelog: [v1.35.9...v1.35.10](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.9...v1.35.10)

### Chores

* **ci:** update rye to v0.35.0 ([#1523](https://github.com/openai/openai-python/issues/1523)) ([dd118c4](https://raw.githubusercontent.com/openai/openai-python/main/dd118c4))

## 1.35.9 (2024-07-02)

Full Changelog: [v1.35.8...v1.35.9](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.8...v1.35.9)

### Bug Fixes

* **client:** always respect content-type multipart/form-data if provided ([#1519](https://github.com/openai/openai-python/issues/1519)) ([6da55e1](https://raw.githubusercontent.com/openai/openai-python/main/6da55e1))

### Chores

* minor change to tests ([#1521](https://github.com/openai/openai-python/issues/1521)) ([a679c0b](https://raw.githubusercontent.com/openai/openai-python/main/a679c0b))

## 1.35.8 (2024-07-02)

Full Changelog: [v1.35.7...v1.35.8](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.7...v1.35.8)

### Chores

* gitignore test server logs ([#1509](https://github.com/openai/openai-python/issues/1509)) ([936d840](https://raw.githubusercontent.com/openai/openai-python/main/936d840))
* **internal:** add helper method for constructing `BaseModel`s ([#1517](https://github.com/openai/openai-python/issues/1517)) ([e5ddbf5](https://raw.githubusercontent.com/openai/openai-python/main/e5ddbf5))
* **internal:** add reflection helper function ([#1508](https://github.com/openai/openai-python/issues/1508)) ([6044e1b](https://raw.githubusercontent.com/openai/openai-python/main/6044e1b))
* **internal:** add rich as a dev dependency ([#1514](https://github.com/openai/openai-python/issues/1514)) ([8a2b4e4](https://raw.githubusercontent.com/openai/openai-python/main/8a2b4e4))

## 1.35.7 (2024-06-27)

Full Changelog: [v1.35.6...v1.35.7](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.6...v1.35.7)

### Bug Fixes

* **build:** include more files in sdist builds ([#1504](https://github.com/openai/openai-python/issues/1504)) ([730c1b5](https://raw.githubusercontent.com/openai/openai-python/main/730c1b5))

## 1.35.6 (2024-06-27)

Full Changelog: [v1.35.5...v1.35.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.5...v1.35.6)

### Documentation

* **readme:** improve some wording ([#1392](https://github.com/openai/openai-python/issues/1392)) ([a58a052](https://raw.githubusercontent.com/openai/openai-python/main/a58a052))

## 1.35.5 (2024-06-26)

Full Changelog: [v1.35.4...v1.35.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.4...v1.35.5)

### Bug Fixes

* **cli/migrate:** avoid reliance on Python 3.12 argument ([be7a06b](https://raw.githubusercontent.com/openai/openai-python/main/be7a06b))

## 1.35.4 (2024-06-26)

Full Changelog: [v1.35.3...v1.35.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.3...v1.35.4)

### Bug Fixes

* **docs:** fix link to advanced python httpx docs ([#1499](https://github.com/openai/openai-python/issues/1499)) ([cf45cd5](https://raw.githubusercontent.com/openai/openai-python/main/cf45cd5))
* temporarily patch upstream version to fix broken release flow ([#1500](https://github.com/openai/openai-python/issues/1500)) ([4f10470](https://raw.githubusercontent.com/openai/openai-python/main/4f10470))

### Chores

* **doc:** clarify service tier default value ([#1496](https://github.com/openai/openai-python/issues/1496)) ([ba39667](https://raw.githubusercontent.com/openai/openai-python/main/ba39667))

## 1.35.3 (2024-06-20)

Full Changelog: [v1.35.2...v1.35.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.2...v1.35.3)

### Bug Fixes

* **tests:** add explicit type annotation ([9345f10](https://raw.githubusercontent.com/openai/openai-python/main/9345f10))

## 1.35.2 (2024-06-20)

Full Changelog: [v1.35.1...v1.35.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.1...v1.35.2)

### Bug Fixes

* **api:** add missing parallel_tool_calls arguments ([4041e4f](https://raw.githubusercontent.com/openai/openai-python/main/4041e4f))

## 1.35.1 (2024-06-19)

Full Changelog: [v1.35.0...v1.35.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.35.0...v1.35.1)

### Bug Fixes

* **client/async:** avoid blocking io call for platform headers ([#1488](https://github.com/openai/openai-python/issues/1488)) ([ae64c05](https://raw.githubusercontent.com/openai/openai-python/main/ae64c05))

## 1.35.0 (2024-06-18)

Full Changelog: [v1.34.0...v1.35.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.34.0...v1.35.0)

### Features

* **api:** add service tier argument for chat completions ([#1486](https://github.com/openai/openai-python/issues/1486)) ([b4b4e66](https://raw.githubusercontent.com/openai/openai-python/main/b4b4e66))

## 1.34.0 (2024-06-12)

Full Changelog: [v1.33.0...v1.34.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.33.0...v1.34.0)

### Features

* **api:** updates ([#1481](https://github.com/openai/openai-python/issues/1481)) ([b83db36](https://raw.githubusercontent.com/openai/openai-python/main/b83db36))

## 1.33.0 (2024-06-07)

Full Changelog: [v1.32.1...v1.33.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.32.1...v1.33.0)

### Features

* **api:** adding chunking_strategy to polling helpers ([#1478](https://github.com/openai/openai-python/issues/1478)) ([83be2a1](https://raw.githubusercontent.com/openai/openai-python/main/83be2a1))

## 1.32.1 (2024-06-07)

Full Changelog: [v1.32.0...v1.32.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.32.0...v1.32.1)

### Bug Fixes

* remove erroneous thread create argument ([#1476](https://github.com/openai/openai-python/issues/1476)) ([43175c4](https://raw.githubusercontent.com/openai/openai-python/main/43175c4))

## 1.32.0 (2024-06-06)

Full Changelog: [v1.31.2...v1.32.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.31.2...v1.32.0)

### Features

* **api:** updates ([#1474](https://github.com/openai/openai-python/issues/1474)) ([87ddff0](https://raw.githubusercontent.com/openai/openai-python/main/87ddff0))

## 1.31.2 (2024-06-06)

Full Changelog: [v1.31.1...v1.31.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.31.1...v1.31.2)

### Chores

* **internal:** minor refactor of tests ([#1471](https://github.com/openai/openai-python/issues/1471)) ([b7f2298](https://raw.githubusercontent.com/openai/openai-python/main/b7f2298))

## 1.31.1 (2024-06-05)

Full Changelog: [v1.31.0...v1.31.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.31.0...v1.31.1)

### Chores

* **internal:** minor change to tests ([#1466](https://github.com/openai/openai-python/issues/1466)) ([cb33e71](https://raw.githubusercontent.com/openai/openai-python/main/cb33e71))

## 1.31.0 (2024-06-03)

Full Changelog: [v1.30.5...v1.31.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.5...v1.31.0)

### Features

* **api:** updates ([#1461](https://github.com/openai/openai-python/issues/1461)) ([0d7cc5e](https://raw.githubusercontent.com/openai/openai-python/main/0d7cc5e))

### Chores

* fix lint ([1886dd4](https://raw.githubusercontent.com/openai/openai-python/main/1886dd4))

## 1.30.5 (2024-05-29)

Full Changelog: [v1.30.4...v1.30.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.4...v1.30.5)

### Chores

* **internal:** fix lint issue ([35a1e80](https://raw.githubusercontent.com/openai/openai-python/main/35a1e80))

## 1.30.4 (2024-05-28)

Full Changelog: [v1.30.3...v1.30.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.3...v1.30.4)

### Chores

* add missing __all__ definitions ([7fba60f](https://raw.githubusercontent.com/openai/openai-python/main/7fba60f))
* **internal:** fix lint issue ([f423cd0](https://raw.githubusercontent.com/openai/openai-python/main/f423cd0))

## 1.30.3 (2024-05-24)

Full Changelog: [v1.30.2...v1.30.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.2...v1.30.3)

### Chores

* **ci:** update rye install location ([#1440](https://github.com/openai/openai-python/issues/1440)) ([8a0e5bf](https://raw.githubusercontent.com/openai/openai-python/main/8a0e5bf))
* **internal:** bump pyright ([#1442](https://github.com/openai/openai-python/issues/1442)) ([64a151e](https://raw.githubusercontent.com/openai/openai-python/main/64a151e))
* **internal:** fix lint issue ([#1444](https://github.com/openai/openai-python/issues/1444)) ([b0eb458](https://raw.githubusercontent.com/openai/openai-python/main/b0eb458))

### Documentation

* **contributing:** update references to rye-up.com ([dcc34a2](https://raw.githubusercontent.com/openai/openai-python/main/dcc34a2))

## 1.30.2 (2024-05-23)

Full Changelog: [v1.30.1...v1.30.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.1...v1.30.2)

### Chores

* **ci:** update rye install location ([#1436](https://github.com/openai/openai-python/issues/1436)) ([f7cc4e7](https://raw.githubusercontent.com/openai/openai-python/main/f7cc4e7))

## 1.30.1 (2024-05-14)

Full Changelog: [v1.30.0...v1.30.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.30.0...v1.30.1)

### Chores

* **internal:** add slightly better logging to scripts ([#1422](https://github.com/openai/openai-python/issues/1422)) ([43dffab](https://raw.githubusercontent.com/openai/openai-python/main/43dffab))

## 1.30.0 (2024-05-14)

Full Changelog: [v1.29.0...v1.30.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.29.0...v1.30.0)

### Features

* **api:** add incomplete state ([#1420](https://github.com/openai/openai-python/issues/1420)) ([6484984](https://raw.githubusercontent.com/openai/openai-python/main/6484984))

## 1.29.0 (2024-05-13)

Full Changelog: [v1.28.2...v1.29.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.28.2...v1.29.0)

### Features

* **api:** add gpt-4o model ([#1417](https://github.com/openai/openai-python/issues/1417)) ([4f09f8c](https://raw.githubusercontent.com/openai/openai-python/main/4f09f8c))

## 1.28.2 (2024-05-13)

Full Changelog: [v1.28.1...v1.28.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.28.1...v1.28.2)

### Bug Fixes

* **client:** accidental blocking sleep in async code ([#1415](https://github.com/openai/openai-python/issues/1415)) ([0ac6ecb](https://raw.githubusercontent.com/openai/openai-python/main/0ac6ecb))

### Chores

* **internal:** bump pydantic dependency ([#1413](https://github.com/openai/openai-python/issues/1413)) ([ed73d1d](https://raw.githubusercontent.com/openai/openai-python/main/ed73d1d))

## 1.28.1 (2024-05-11)

Full Changelog: [v1.28.0...v1.28.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.28.0...v1.28.1)

### Chores

* **docs:** add SECURITY.md ([#1408](https://github.com/openai/openai-python/issues/1408)) ([119970a](https://raw.githubusercontent.com/openai/openai-python/main/119970a))

## 1.28.0 (2024-05-09)

Full Changelog: [v1.27.0...v1.28.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.27.0...v1.28.0)

### Features

* **api:** add message image content ([#1405](https://github.com/openai/openai-python/issues/1405)) ([a115de6](https://raw.githubusercontent.com/openai/openai-python/main/a115de6))

## 1.27.0 (2024-05-08)

Full Changelog: [v1.26.0...v1.27.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.26.0...v1.27.0)

### Features

* **api:** adding file purposes ([#1401](https://github.com/openai/openai-python/issues/1401)) ([2e9d0bd](https://raw.githubusercontent.com/openai/openai-python/main/2e9d0bd))

## 1.26.0 (2024-05-06)

Full Changelog: [v1.25.2...v1.26.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.25.2...v1.26.0)

### Features

* **api:** add usage metadata when streaming ([#1395](https://github.com/openai/openai-python/issues/1395)) ([3cb064b](https://raw.githubusercontent.com/openai/openai-python/main/3cb064b))

## 1.25.2 (2024-05-05)

Full Changelog: [v1.25.1...v1.25.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.25.1...v1.25.2)

### Documentation

* **readme:** fix misleading timeout example value ([#1393](https://github.com/openai/openai-python/issues/1393)) ([3eba8e7](https://raw.githubusercontent.com/openai/openai-python/main/3eba8e7))

## 1.25.1 (2024-05-02)

Full Changelog: [v1.25.0...v1.25.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.25.0...v1.25.1)

### Chores

* **internal:** bump prism version ([#1390](https://github.com/openai/openai-python/issues/1390)) ([a5830fc](https://raw.githubusercontent.com/openai/openai-python/main/a5830fc))

## 1.25.0 (2024-05-01)

Full Changelog: [v1.24.1...v1.25.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.24.1...v1.25.0)

### Features

* **api:** delete messages ([#1388](https://github.com/openai/openai-python/issues/1388)) ([d0597cd](https://raw.githubusercontent.com/openai/openai-python/main/d0597cd))

## 1.24.1 (2024-04-30)

Full Changelog: [v1.24.0...v1.24.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.24.0...v1.24.1)

### Chores

* **internal:** add link to openapi spec ([#1385](https://github.com/openai/openai-python/issues/1385)) ([b315d04](https://raw.githubusercontent.com/openai/openai-python/main/b315d04))

## 1.24.0 (2024-04-29)

Full Changelog: [v1.23.6...v1.24.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.6...v1.24.0)

### Features

* **api:** add required tool_choice ([#1382](https://github.com/openai/openai-python/issues/1382)) ([c558f65](https://raw.githubusercontent.com/openai/openai-python/main/c558f65))

### Chores

* **client:** log response headers in debug mode ([#1383](https://github.com/openai/openai-python/issues/1383)) ([f31a426](https://raw.githubusercontent.com/openai/openai-python/main/f31a426))
* **internal:** minor reformatting ([#1377](https://github.com/openai/openai-python/issues/1377)) ([7003dbb](https://raw.githubusercontent.com/openai/openai-python/main/7003dbb))
* **internal:** reformat imports ([#1375](https://github.com/openai/openai-python/issues/1375)) ([2ad0c3b](https://raw.githubusercontent.com/openai/openai-python/main/2ad0c3b))

## 1.23.6 (2024-04-25)

Full Changelog: [v1.23.5...v1.23.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.5...v1.23.6)

### Chores

* **internal:** update test helper function ([#1371](https://github.com/openai/openai-python/issues/1371)) ([6607c4a](https://raw.githubusercontent.com/openai/openai-python/main/6607c4a))

## 1.23.5 (2024-04-24)

Full Changelog: [v1.23.4...v1.23.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.4...v1.23.5)

### Chores

* **internal:** use actions/checkout@v4 for codeflow ([#1368](https://github.com/openai/openai-python/issues/1368)) ([d1edf8b](https://raw.githubusercontent.com/openai/openai-python/main/d1edf8b))

## 1.23.4 (2024-04-24)

Full Changelog: [v1.23.3...v1.23.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.3...v1.23.4)

### Bug Fixes

* **api:** change timestamps to unix integers ([#1367](https://github.com/openai/openai-python/issues/1367)) ([fbc0e15](https://raw.githubusercontent.com/openai/openai-python/main/fbc0e15))
* **docs:** doc improvements ([#1364](https://github.com/openai/openai-python/issues/1364)) ([8c3a005](https://raw.githubusercontent.com/openai/openai-python/main/8c3a005))

### Chores

* **tests:** rename test file ([#1366](https://github.com/openai/openai-python/issues/1366)) ([4204e63](https://raw.githubusercontent.com/openai/openai-python/main/4204e63))

## 1.23.3 (2024-04-23)

Full Changelog: [v1.23.2...v1.23.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.2...v1.23.3)

### Chores

* **internal:** restructure imports ([#1359](https://github.com/openai/openai-python/issues/1359)) ([4e5eb37](https://raw.githubusercontent.com/openai/openai-python/main/4e5eb37))

## 1.23.2 (2024-04-19)

Full Changelog: [v1.23.1...v1.23.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.1...v1.23.2)

### Bug Fixes

* **api:** correct types for message attachment tools ([#1348](https://github.com/openai/openai-python/issues/1348)) ([78a6261](https://raw.githubusercontent.com/openai/openai-python/main/78a6261))

## 1.23.1 (2024-04-18)

Full Changelog: [v1.23.0...v1.23.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.23.0...v1.23.1)

### Bug Fixes

* **api:** correct types for attachments ([#1342](https://github.com/openai/openai-python/issues/1342)) ([542d30c](https://raw.githubusercontent.com/openai/openai-python/main/542d30c))

## 1.23.0 (2024-04-18)

Full Changelog: [v1.22.0...v1.23.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.22.0...v1.23.0)

### Features

* **api:** add request id property to response classes ([#1341](https://github.com/openai/openai-python/issues/1341)) ([444d680](https://raw.githubusercontent.com/openai/openai-python/main/444d680))

### Documentation

* **helpers:** fix example snippets ([#1339](https://github.com/openai/openai-python/issues/1339)) ([8929088](https://raw.githubusercontent.com/openai/openai-python/main/8929088))

## 1.22.0 (2024-04-18)

Full Changelog: [v1.21.2...v1.22.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.21.2...v1.22.0)

### Features

* **api:** batch list endpoint ([#1338](https://github.com/openai/openai-python/issues/1338)) ([a776f38](https://raw.githubusercontent.com/openai/openai-python/main/a776f38))

### Chores

* **internal:** ban usage of lru_cache ([#1331](https://github.com/openai/openai-python/issues/1331)) ([8f9223b](https://raw.githubusercontent.com/openai/openai-python/main/8f9223b))
* **internal:** bump pyright to 1.1.359 ([#1337](https://github.com/openai/openai-python/issues/1337)) ([feec0dd](https://raw.githubusercontent.com/openai/openai-python/main/feec0dd))

## 1.21.2 (2024-04-17)

Full Changelog: [v1.21.1...v1.21.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.21.1...v1.21.2)

### Chores

* **internal:** add lru_cache helper function ([#1329](https://github.com/openai/openai-python/issues/1329)) ([cbeebfc](https://raw.githubusercontent.com/openai/openai-python/main/cbeebfc))

## 1.21.1 (2024-04-17)

Full Changelog: [v1.21.0...v1.21.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.21.0...v1.21.1)

### Chores

* **api:** docs and response_format response property ([#1327](https://github.com/openai/openai-python/issues/1327)) ([7a6d142](https://raw.githubusercontent.com/openai/openai-python/main/7a6d142))

## 1.21.0 (2024-04-17)

Full Changelog: [v1.20.0...v1.21.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.20.0...v1.21.0)

### Features

* **api:** add vector stores ([#1325](https://github.com/openai/openai-python/issues/1325)) ([038a3c5](https://raw.githubusercontent.com/openai/openai-python/main/038a3c5))

## 1.20.0 (2024-04-16)

Full Changelog: [v1.19.0...v1.20.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.19.0...v1.20.0)

### Features

* **client:** add header OpenAI-Project ([#1320](https://github.com/openai/openai-python/issues/1320)) ([0c489f1](https://raw.githubusercontent.com/openai/openai-python/main/0c489f1))
* extract chat models to a named enum ([#1322](https://github.com/openai/openai-python/issues/1322)) ([1ccd9b6](https://raw.githubusercontent.com/openai/openai-python/main/1ccd9b6))

## 1.19.0 (2024-04-15)

Full Changelog: [v1.18.0...v1.19.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.18.0...v1.19.0)

### Features

* **errors:** add request_id property ([#1317](https://github.com/openai/openai-python/issues/1317)) ([f9eb77d](https://raw.githubusercontent.com/openai/openai-python/main/f9eb77d))

## 1.18.0 (2024-04-15)

Full Changelog: [v1.17.1...v1.18.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.17.1...v1.18.0)

### Features

* **api:** add batch API ([#1316](https://github.com/openai/openai-python/issues/1316)) ([3e6f19e](https://raw.githubusercontent.com/openai/openai-python/main/3e6f19e))
* **api:** updates ([#1314](https://github.com/openai/openai-python/issues/1314)) ([8281dc9](https://raw.githubusercontent.com/openai/openai-python/main/8281dc9))

## 1.17.1 (2024-04-12)

Full Changelog: [v1.17.0...v1.17.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.17.0...v1.17.1)

### Chores

* fix typo ([#1304](https://github.com/openai/openai-python/issues/1304)) ([1129082](https://raw.githubusercontent.com/openai/openai-python/main/1129082))
* **internal:** formatting ([#1311](https://github.com/openai/openai-python/issues/1311)) ([8fd411b](https://raw.githubusercontent.com/openai/openai-python/main/8fd411b))

## 1.17.0 (2024-04-10)

Full Changelog: [v1.16.2...v1.17.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.16.2...v1.17.0)

### Features

* **api:** add additional messages when creating thread run ([#1298](https://github.com/openai/openai-python/issues/1298)) ([70eb081](https://raw.githubusercontent.com/openai/openai-python/main/70eb081))
* **client:** add DefaultHttpxClient and DefaultAsyncHttpxClient ([#1302](https://github.com/openai/openai-python/issues/1302)) ([69cdfc3](https://raw.githubusercontent.com/openai/openai-python/main/69cdfc3))
* **models:** add to_dict & to_json helper methods ([#1305](https://github.com/openai/openai-python/issues/1305)) ([40a881d](https://raw.githubusercontent.com/openai/openai-python/main/40a881d))

## 1.16.2 (2024-04-04)

Full Changelog: [v1.16.1...v1.16.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.16.1...v1.16.2)

### Bug Fixes

* **client:** correct logic for line decoding in streaming ([#1293](https://github.com/openai/openai-python/issues/1293)) ([687caef](https://raw.githubusercontent.com/openai/openai-python/main/687caef))

## 1.16.1 (2024-04-02)

Full Changelog: [v1.16.0...v1.16.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.16.0...v1.16.1)

### Chores

* **internal:** defer model build for import latency ([#1291](https://github.com/openai/openai-python/issues/1291)) ([bc6866e](https://raw.githubusercontent.com/openai/openai-python/main/bc6866e))

## 1.16.0 (2024-04-01)

Full Changelog: [v1.15.0...v1.16.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.15.0...v1.16.0)

### Features

* **api:** add support for filtering messages by run_id ([#1288](https://github.com/openai/openai-python/issues/1288)) ([58d6b77](https://raw.githubusercontent.com/openai/openai-python/main/58d6b77))
* **api:** run polling helpers ([#1289](https://github.com/openai/openai-python/issues/1289)) ([6b427f3](https://raw.githubusercontent.com/openai/openai-python/main/6b427f3))

### Chores

* **client:** validate that max_retries is not None ([#1286](https://github.com/openai/openai-python/issues/1286)) ([aa5920a](https://raw.githubusercontent.com/openai/openai-python/main/aa5920a))

### Refactors

* rename createAndStream to stream ([6b427f3](https://raw.githubusercontent.com/openai/openai-python/main/6b427f3))

## 1.15.0 (2024-03-31)

Full Changelog: [v1.14.3...v1.15.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.14.3...v1.15.0)

### Features

* **api:** adding temperature parameter ([#1282](https://github.com/openai/openai-python/issues/1282)) ([0e68fd3](https://raw.githubusercontent.com/openai/openai-python/main/0e68fd3))
* **client:** increase default HTTP max_connections to 1000 and max_keepalive_connections to 100 ([#1281](https://github.com/openai/openai-python/issues/1281)) ([340d139](https://raw.githubusercontent.com/openai/openai-python/main/340d139))
* **package:** export default constants ([#1275](https://github.com/openai/openai-python/issues/1275)) ([fdc126e](https://raw.githubusercontent.com/openai/openai-python/main/fdc126e))

### Bug Fixes

* **project:** use absolute github links on PyPi ([#1280](https://github.com/openai/openai-python/issues/1280)) ([94cd528](https://raw.githubusercontent.com/openai/openai-python/main/94cd528))

### Chores

* **internal:** bump dependencies ([#1273](https://github.com/openai/openai-python/issues/1273)) ([18dcd65](https://raw.githubusercontent.com/openai/openai-python/main/18dcd65))

### Documentation

* **readme:** change undocumented params wording ([#1284](https://github.com/openai/openai-python/issues/1284)) ([7498ef1](https://raw.githubusercontent.com/openai/openai-python/main/7498ef1))

## 1.14.3 (2024-03-25)

Full Changelog: [v1.14.2...v1.14.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.14.2...v1.14.3)

### Bug Fixes

* revert regression with 3.7 support ([#1269](https://github.com/openai/openai-python/issues/1269)) ([37aed56](https://raw.githubusercontent.com/openai/openai-python/main/37aed56))

### Chores

* **internal:** construct error properties instead of using the raw response ([#1257](https://github.com/openai/openai-python/issues/1257)) ([11dce5c](https://raw.githubusercontent.com/openai/openai-python/main/11dce5c))
* **internal:** formatting change ([#1258](https://github.com/openai/openai-python/issues/1258)) ([b907dd7](https://raw.githubusercontent.com/openai/openai-python/main/b907dd7))
* **internal:** loosen input type for util function ([#1250](https://github.com/openai/openai-python/issues/1250)) ([fc8b4c3](https://raw.githubusercontent.com/openai/openai-python/main/fc8b4c3))

### Documentation

* **contributing:** fix typo ([#1264](https://github.com/openai/openai-python/issues/1264)) ([835cb9b](https://raw.githubusercontent.com/openai/openai-python/main/835cb9b))
* **readme:** consistent use of sentence case in headings ([#1255](https://github.com/openai/openai-python/issues/1255)) ([519f371](https://raw.githubusercontent.com/openai/openai-python/main/519f371))
* **readme:** document how to make undocumented requests ([#1256](https://github.com/openai/openai-python/issues/1256)) ([5887858](https://raw.githubusercontent.com/openai/openai-python/main/5887858))

## 1.14.2 (2024-03-19)

Full Changelog: [v1.14.1...v1.14.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.14.1...v1.14.2)

### Performance Improvements

* cache TypeAdapters ([#1114](https://github.com/openai/openai-python/issues/1114)) ([41b6fee](https://raw.githubusercontent.com/openai/openai-python/main/41b6fee))
* cache TypeAdapters ([#1243](https://github.com/openai/openai-python/issues/1243)) ([2005076](https://raw.githubusercontent.com/openai/openai-python/main/2005076))

### Chores

* **internal:** update generated pragma comment ([#1247](https://github.com/openai/openai-python/issues/1247)) ([3eeb9b3](https://raw.githubusercontent.com/openai/openai-python/main/3eeb9b3))

### Documentation

* assistant improvements ([#1249](https://github.com/openai/openai-python/issues/1249)) ([e7a3176](https://raw.githubusercontent.com/openai/openai-python/main/e7a3176))
* fix typo in CONTRIBUTING.md ([#1245](https://github.com/openai/openai-python/issues/1245)) ([adef57a](https://raw.githubusercontent.com/openai/openai-python/main/adef57a))

## 1.14.1 (2024-03-15)

Full Changelog: [v1.14.0...v1.14.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.14.0...v1.14.1)

### Documentation

* **readme:** assistant streaming ([#1238](https://github.com/openai/openai-python/issues/1238)) ([0fc30a2](https://raw.githubusercontent.com/openai/openai-python/main/0fc30a2))

## 1.14.0 (2024-03-13)

Full Changelog: [v1.13.4...v1.14.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.13.4...v1.14.0)

### Features

* **assistants:** add support for streaming ([#1233](https://github.com/openai/openai-python/issues/1233)) ([17635dc](https://raw.githubusercontent.com/openai/openai-python/main/17635dc))

## 1.13.4 (2024-03-13)

Full Changelog: [v1.13.3...v1.13.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.13.3...v1.13.4)

### Bug Fixes

* **streaming:** improve error messages ([#1218](https://github.com/openai/openai-python/issues/1218)) ([4f5ff29](https://raw.githubusercontent.com/openai/openai-python/main/4f5ff29))

### Chores

* **api:** update docs ([#1212](https://github.com/openai/openai-python/issues/1212)) ([71236e0](https://raw.githubusercontent.com/openai/openai-python/main/71236e0))
* **client:** improve error message for invalid http_client argument ([#1216](https://github.com/openai/openai-python/issues/1216)) ([d0c928a](https://raw.githubusercontent.com/openai/openai-python/main/d0c928a))
* **docs:** mention install from git repo ([#1203](https://github.com/openai/openai-python/issues/1203)) ([3ab6f44](https://raw.githubusercontent.com/openai/openai-python/main/3ab6f44))
* export NOT_GIVEN sentinel value ([#1223](https://github.com/openai/openai-python/issues/1223)) ([8a4f76f](https://raw.githubusercontent.com/openai/openai-python/main/8a4f76f))
* **internal:** add core support for deserializing into number response ([#1219](https://github.com/openai/openai-python/issues/1219)) ([004bc92](https://raw.githubusercontent.com/openai/openai-python/main/004bc92))
* **internal:** bump pyright ([#1221](https://github.com/openai/openai-python/issues/1221)) ([3c2e815](https://raw.githubusercontent.com/openai/openai-python/main/3c2e815))
* **internal:** improve deserialisation of discriminated unions ([#1227](https://github.com/openai/openai-python/issues/1227)) ([4767259](https://raw.githubusercontent.com/openai/openai-python/main/4767259))
* **internal:** minor core client restructuring ([#1199](https://github.com/openai/openai-python/issues/1199)) ([4314cdc](https://raw.githubusercontent.com/openai/openai-python/main/4314cdc))
* **internal:** split up transforms into sync / async ([#1210](https://github.com/openai/openai-python/issues/1210)) ([7853a83](https://raw.githubusercontent.com/openai/openai-python/main/7853a83))
* **internal:** support more input types ([#1211](https://github.com/openai/openai-python/issues/1211)) ([d0e4baa](https://raw.githubusercontent.com/openai/openai-python/main/d0e4baa))
* **internal:** support parsing Annotated types ([#1222](https://github.com/openai/openai-python/issues/1222)) ([8598f81](https://raw.githubusercontent.com/openai/openai-python/main/8598f81))
* **types:** include discriminators in unions ([#1228](https://github.com/openai/openai-python/issues/1228)) ([3ba0dcc](https://raw.githubusercontent.com/openai/openai-python/main/3ba0dcc))

### Documentation

* **contributing:** improve wording ([#1201](https://github.com/openai/openai-python/issues/1201)) ([95a1e0e](https://raw.githubusercontent.com/openai/openai-python/main/95a1e0e))

## 1.13.3 (2024-02-28)

Full Changelog: [v1.13.2...v1.13.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.13.2...v1.13.3)

### Features

* **api:** add wav and pcm to response_format ([#1189](https://github.com/openai/openai-python/issues/1189)) ([dbd20fc](https://raw.githubusercontent.com/openai/openai-python/main/dbd20fc))

### Chores

* **client:** use anyio.sleep instead of asyncio.sleep ([#1198](https://github.com/openai/openai-python/issues/1198)) ([b6d025b](https://raw.githubusercontent.com/openai/openai-python/main/b6d025b))
* **internal:** bump pyright ([#1193](https://github.com/openai/openai-python/issues/1193)) ([9202e04](https://raw.githubusercontent.com/openai/openai-python/main/9202e04))
* **types:** extract run status to a named type ([#1178](https://github.com/openai/openai-python/issues/1178)) ([249ecbd](https://raw.githubusercontent.com/openai/openai-python/main/249ecbd))

### Documentation

* add note in azure_deployment docstring ([#1188](https://github.com/openai/openai-python/issues/1188)) ([96fa995](https://raw.githubusercontent.com/openai/openai-python/main/96fa995))
* **examples:** add pyaudio streaming example ([#1194](https://github.com/openai/openai-python/issues/1194)) ([3683c5e](https://raw.githubusercontent.com/openai/openai-python/main/3683c5e))

## 1.13.2 (2024-02-20)

Full Changelog: [v1.13.1...v1.13.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.13.1...v1.13.2)

### Bug Fixes

* **ci:** revert "move github release logic to github app" ([#1170](https://github.com/openai/openai-python/issues/1170)) ([f1adc2e](https://raw.githubusercontent.com/openai/openai-python/main/f1adc2e))

## 1.13.1 (2024-02-20)

Full Changelog: [v1.13.0...v1.13.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.13.0...v1.13.1)

### Chores

* **internal:** bump rye to v0.24.0 ([#1168](https://github.com/openai/openai-python/issues/1168)) ([84c4256](https://raw.githubusercontent.com/openai/openai-python/main/84c4256))

## 1.13.0 (2024-02-19)

Full Changelog: [v1.12.0...v1.13.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.12.0...v1.13.0)

### Features

* **api:** updates ([#1146](https://github.com/openai/openai-python/issues/1146)) ([79b7675](https://raw.githubusercontent.com/openai/openai-python/main/79b7675))

### Bug Fixes

* **api:** remove non-GA instance_id param ([#1164](https://github.com/openai/openai-python/issues/1164)) ([1abe139](https://raw.githubusercontent.com/openai/openai-python/main/1abe139))

### Chores

* **ci:** move github release logic to github app ([#1155](https://github.com/openai/openai-python/issues/1155)) ([67cfac2](https://raw.githubusercontent.com/openai/openai-python/main/67cfac2))
* **client:** use correct accept headers for binary data ([#1161](https://github.com/openai/openai-python/issues/1161)) ([e536437](https://raw.githubusercontent.com/openai/openai-python/main/e536437))
* **internal:** refactor release environment script ([#1158](https://github.com/openai/openai-python/issues/1158)) ([7fe8ec3](https://raw.githubusercontent.com/openai/openai-python/main/7fe8ec3))

## 1.12.0 (2024-02-08)

Full Changelog: [v1.11.1...v1.12.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.11.1...v1.12.0)

### Features

* **api:** add `timestamp_granularities`, add `gpt-3.5-turbo-0125` model ([#1125](https://github.com/openai/openai-python/issues/1125)) ([1ecf8f6](https://raw.githubusercontent.com/openai/openai-python/main/1ecf8f6))
* **cli/images:** add support for `--model` arg ([#1132](https://github.com/openai/openai-python/issues/1132)) ([0d53866](https://raw.githubusercontent.com/openai/openai-python/main/0d53866))

### Bug Fixes

* remove double brackets from timestamp_granularities param ([#1140](https://github.com/openai/openai-python/issues/1140)) ([3db0222](https://raw.githubusercontent.com/openai/openai-python/main/3db0222))
* **types:** loosen most List params types to Iterable ([#1129](https://github.com/openai/openai-python/issues/1129)) ([bdb31a3](https://raw.githubusercontent.com/openai/openai-python/main/bdb31a3))

### Chores

* **internal:** add lint command ([#1128](https://github.com/openai/openai-python/issues/1128)) ([4c021c0](https://raw.githubusercontent.com/openai/openai-python/main/4c021c0))
* **internal:** support serialising iterable types ([#1127](https://github.com/openai/openai-python/issues/1127)) ([98d4e59](https://raw.githubusercontent.com/openai/openai-python/main/98d4e59))

### Documentation

* add CONTRIBUTING.md ([#1138](https://github.com/openai/openai-python/issues/1138)) ([79c8f0e](https://raw.githubusercontent.com/openai/openai-python/main/79c8f0e))

## 1.11.1 (2024-02-04)

Full Changelog: [v1.11.0...v1.11.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.11.0...v1.11.1)

### Bug Fixes

* prevent crash when platform.architecture() is not allowed ([#1120](https://github.com/openai/openai-python/issues/1120)) ([9490554](https://raw.githubusercontent.com/openai/openai-python/main/9490554))

## 1.11.0 (2024-02-03)

Full Changelog: [v1.10.0...v1.11.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.10.0...v1.11.0)

### Features

* **client:** support parsing custom response types ([#1111](https://github.com/openai/openai-python/issues/1111)) ([da00fc3](https://raw.githubusercontent.com/openai/openai-python/main/da00fc3))

### Chores

* **interal:** make link to api.md relative ([#1117](https://github.com/openai/openai-python/issues/1117)) ([4a10879](https://raw.githubusercontent.com/openai/openai-python/main/4a10879))
* **internal:** cast type in mocked test ([#1112](https://github.com/openai/openai-python/issues/1112)) ([99b21e1](https://raw.githubusercontent.com/openai/openai-python/main/99b21e1))
* **internal:** enable ruff type checking misuse lint rule ([#1106](https://github.com/openai/openai-python/issues/1106)) ([fa63e60](https://raw.githubusercontent.com/openai/openai-python/main/fa63e60))
* **internal:** support multipart data with overlapping keys ([#1104](https://github.com/openai/openai-python/issues/1104)) ([455bc9f](https://raw.githubusercontent.com/openai/openai-python/main/455bc9f))
* **internal:** support pre-release versioning ([#1113](https://github.com/openai/openai-python/issues/1113)) ([dea5b08](https://raw.githubusercontent.com/openai/openai-python/main/dea5b08))

## 1.10.0 (2024-01-25)

Full Changelog: [v1.9.0...v1.10.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.9.0...v1.10.0)

### Features

* **api:** add text embeddings dimensions param ([#1103](https://github.com/openai/openai-python/issues/1103)) ([94abfa0](https://raw.githubusercontent.com/openai/openai-python/main/94abfa0))
* **azure:** proactively add audio/speech to deployment endpoints ([#1099](https://github.com/openai/openai-python/issues/1099)) ([fdf8742](https://raw.githubusercontent.com/openai/openai-python/main/fdf8742))
* **client:** enable follow redirects by default ([#1100](https://github.com/openai/openai-python/issues/1100)) ([d325b7c](https://raw.githubusercontent.com/openai/openai-python/main/d325b7c))

### Chores

* **internal:** add internal helpers ([#1092](https://github.com/openai/openai-python/issues/1092)) ([629bde5](https://raw.githubusercontent.com/openai/openai-python/main/629bde5))

### Refactors

* remove unnecessary builtin import ([#1094](https://github.com/openai/openai-python/issues/1094)) ([504b7d4](https://raw.githubusercontent.com/openai/openai-python/main/504b7d4))

## 1.9.0 (2024-01-21)

Full Changelog: [v1.8.0...v1.9.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.8.0...v1.9.0)

### Features

* **api:** add usage to runs and run steps ([#1090](https://github.com/openai/openai-python/issues/1090)) ([6c116df](https://raw.githubusercontent.com/openai/openai-python/main/6c116df))

### Chores

* **internal:** fix typing util function ([#1083](https://github.com/openai/openai-python/issues/1083)) ([3e60db6](https://raw.githubusercontent.com/openai/openai-python/main/3e60db6))
* **internal:** remove redundant client test ([#1085](https://github.com/openai/openai-python/issues/1085)) ([947974f](https://raw.githubusercontent.com/openai/openai-python/main/947974f))
* **internal:** share client instances between all tests ([#1088](https://github.com/openai/openai-python/issues/1088)) ([05cd753](https://raw.githubusercontent.com/openai/openai-python/main/05cd753))
* **internal:** speculative retry-after-ms support ([#1086](https://github.com/openai/openai-python/issues/1086)) ([36a7576](https://raw.githubusercontent.com/openai/openai-python/main/36a7576))
* lazy load raw resource class properties ([#1087](https://github.com/openai/openai-python/issues/1087)) ([d307127](https://raw.githubusercontent.com/openai/openai-python/main/d307127))

## 1.8.0 (2024-01-16)

Full Changelog: [v1.7.2...v1.8.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.7.2...v1.8.0)

### Features

* **client:** add support for streaming raw responses ([#1072](https://github.com/openai/openai-python/issues/1072)) ([0e93c3b](https://raw.githubusercontent.com/openai/openai-python/main/0e93c3b))

### Bug Fixes

* **client:** ensure path params are non-empty ([#1075](https://github.com/openai/openai-python/issues/1075)) ([9a25149](https://raw.githubusercontent.com/openai/openai-python/main/9a25149))
* **proxy:** prevent recursion errors when debugging pycharm ([#1076](https://github.com/openai/openai-python/issues/1076)) ([3d78798](https://raw.githubusercontent.com/openai/openai-python/main/3d78798))

### Chores

* add write_to_file binary helper method ([#1077](https://github.com/openai/openai-python/issues/1077)) ([c622c6a](https://raw.githubusercontent.com/openai/openai-python/main/c622c6a))

## 1.7.2 (2024-01-12)

Full Changelog: [v1.7.1...v1.7.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.7.1...v1.7.2)

### Documentation

* **readme:** improve api reference ([#1065](https://github.com/openai/openai-python/issues/1065)) ([745b9e0](https://raw.githubusercontent.com/openai/openai-python/main/745b9e0))

### Refactors

* **api:** remove deprecated endpoints ([#1067](https://github.com/openai/openai-python/issues/1067)) ([199ddcd](https://raw.githubusercontent.com/openai/openai-python/main/199ddcd))

## 1.7.1 (2024-01-10)

Full Changelog: [v1.7.0...v1.7.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.7.0...v1.7.1)

### Chores

* **client:** improve debug logging for failed requests ([#1060](https://github.com/openai/openai-python/issues/1060)) ([cf9a651](https://raw.githubusercontent.com/openai/openai-python/main/cf9a651))

## 1.7.0 (2024-01-08)

Full Changelog: [v1.6.1...v1.7.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.6.1...v1.7.0)

### Features

* add `None` default value to nullable response properties ([#1043](https://github.com/openai/openai-python/issues/1043)) ([d94b4d3](https://raw.githubusercontent.com/openai/openai-python/main/d94b4d3))

### Bug Fixes

* **client:** correctly use custom http client auth ([#1028](https://github.com/openai/openai-python/issues/1028)) ([3d7d93e](https://raw.githubusercontent.com/openai/openai-python/main/3d7d93e))

### Chores

* add .keep files for examples and custom code directories ([#1057](https://github.com/openai/openai-python/issues/1057)) ([7524097](https://raw.githubusercontent.com/openai/openai-python/main/7524097))
* **internal:** bump license ([#1037](https://github.com/openai/openai-python/issues/1037)) ([d828527](https://raw.githubusercontent.com/openai/openai-python/main/d828527))
* **internal:** loosen type var restrictions ([#1049](https://github.com/openai/openai-python/issues/1049)) ([e00876b](https://raw.githubusercontent.com/openai/openai-python/main/e00876b))
* **internal:** replace isort with ruff ([#1042](https://github.com/openai/openai-python/issues/1042)) ([f1fbc9c](https://raw.githubusercontent.com/openai/openai-python/main/f1fbc9c))
* **internal:** update formatting ([#1041](https://github.com/openai/openai-python/issues/1041)) ([2e9ecee](https://raw.githubusercontent.com/openai/openai-python/main/2e9ecee))
* **src:** fix typos ([#988](https://github.com/openai/openai-python/issues/988)) ([6a8b806](https://raw.githubusercontent.com/openai/openai-python/main/6a8b806))
* use property declarations for resource members ([#1047](https://github.com/openai/openai-python/issues/1047)) ([131f6bc](https://raw.githubusercontent.com/openai/openai-python/main/131f6bc))

### Documentation

* fix docstring typos ([#1022](https://github.com/openai/openai-python/issues/1022)) ([ad3fd2c](https://raw.githubusercontent.com/openai/openai-python/main/ad3fd2c))
* improve audio example to show how to stream to a file ([#1017](https://github.com/openai/openai-python/issues/1017)) ([d45ed7f](https://raw.githubusercontent.com/openai/openai-python/main/d45ed7f))

## 1.6.1 (2023-12-22)

Full Changelog: [v1.6.0...v1.6.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.6.0...v1.6.1)

### Chores

* **internal:** add bin script ([#1001](https://github.com/openai/openai-python/issues/1001)) ([99ffbda](https://raw.githubusercontent.com/openai/openai-python/main/99ffbda))
* **internal:** use ruff instead of black for formatting ([#1008](https://github.com/openai/openai-python/issues/1008)) ([ceaf9a0](https://raw.githubusercontent.com/openai/openai-python/main/ceaf9a0))

## 1.6.0 (2023-12-19)

Full Changelog: [v1.5.0...v1.6.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.5.0...v1.6.0)

### Features

* **api:** add additional instructions for runs ([#995](https://github.com/openai/openai-python/issues/995)) ([7bf9b75](https://raw.githubusercontent.com/openai/openai-python/main/7bf9b75))

### Chores

* **cli:** fix typo in completions ([#985](https://github.com/openai/openai-python/issues/985)) ([d1e9e8f](https://raw.githubusercontent.com/openai/openai-python/main/d1e9e8f))
* **cli:** fix typo in completions ([#986](https://github.com/openai/openai-python/issues/986)) ([626bc34](https://raw.githubusercontent.com/openai/openai-python/main/626bc34))
* **internal:** fix binary response tests ([#983](https://github.com/openai/openai-python/issues/983)) ([cfb7e30](https://raw.githubusercontent.com/openai/openai-python/main/cfb7e30))
* **internal:** fix typos ([#993](https://github.com/openai/openai-python/issues/993)) ([3b338a4](https://raw.githubusercontent.com/openai/openai-python/main/3b338a4))
* **internal:** minor utils restructuring ([#992](https://github.com/openai/openai-python/issues/992)) ([5ba576a](https://raw.githubusercontent.com/openai/openai-python/main/5ba576a))
* **package:** bump minimum typing-extensions to 4.7 ([#994](https://github.com/openai/openai-python/issues/994)) ([0c2da84](https://raw.githubusercontent.com/openai/openai-python/main/0c2da84))
* **streaming:** update constructor to use direct client names ([#991](https://github.com/openai/openai-python/issues/991)) ([6c3427d](https://raw.githubusercontent.com/openai/openai-python/main/6c3427d))

### Documentation

* upgrade models in examples to latest version ([#989](https://github.com/openai/openai-python/issues/989)) ([cedd574](https://raw.githubusercontent.com/openai/openai-python/main/cedd574))

## 1.5.0 (2023-12-17)

Full Changelog: [v1.4.0...v1.5.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.4.0...v1.5.0)

### Features

* **api:** add token logprobs to chat completions ([#980](https://github.com/openai/openai-python/issues/980)) ([f50e962](https://raw.githubusercontent.com/openai/openai-python/main/f50e962))

### Chores

* **ci:** run release workflow once per day ([#978](https://github.com/openai/openai-python/issues/978)) ([215476a](https://raw.githubusercontent.com/openai/openai-python/main/215476a))

## 1.4.0 (2023-12-15)

Full Changelog: [v1.3.9...v1.4.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.9...v1.4.0)

### Features

* **api:** add optional `name` argument + improve docs ([#972](https://github.com/openai/openai-python/issues/972)) ([7972010](https://raw.githubusercontent.com/openai/openai-python/main/7972010))

## 1.3.9 (2023-12-12)

Full Changelog: [v1.3.8...v1.3.9](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.8...v1.3.9)

### Documentation

* improve README timeout comment ([#964](https://github.com/openai/openai-python/issues/964)) ([3c3ed5e](https://raw.githubusercontent.com/openai/openai-python/main/3c3ed5e))
* small Improvement in the async chat response code ([#959](https://github.com/openai/openai-python/issues/959)) ([fb9d0a3](https://raw.githubusercontent.com/openai/openai-python/main/fb9d0a3))
* small streaming readme improvements ([#962](https://github.com/openai/openai-python/issues/962)) ([f3be2e5](https://raw.githubusercontent.com/openai/openai-python/main/f3be2e5))

### Refactors

* **client:** simplify cleanup ([#966](https://github.com/openai/openai-python/issues/966)) ([5c138f4](https://raw.githubusercontent.com/openai/openai-python/main/5c138f4))
* simplify internal error handling ([#968](https://github.com/openai/openai-python/issues/968)) ([d187f6b](https://raw.githubusercontent.com/openai/openai-python/main/d187f6b))

## 1.3.8 (2023-12-08)

Full Changelog: [v1.3.7...v1.3.8](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.7...v1.3.8)

### Bug Fixes

* avoid leaking memory when Client.with_options is used ([#956](https://github.com/openai/openai-python/issues/956)) ([e37ecca](https://raw.githubusercontent.com/openai/openai-python/main/e37ecca))
* **errors:** properly assign APIError.body ([#949](https://github.com/openai/openai-python/issues/949)) ([c70e194](https://raw.githubusercontent.com/openai/openai-python/main/c70e194))
* **pagination:** use correct type hint for .object ([#943](https://github.com/openai/openai-python/issues/943)) ([23fe7ee](https://raw.githubusercontent.com/openai/openai-python/main/23fe7ee))

### Chores

* **internal:** enable more lint rules ([#945](https://github.com/openai/openai-python/issues/945)) ([2c8add6](https://raw.githubusercontent.com/openai/openai-python/main/2c8add6))
* **internal:** reformat imports ([#939](https://github.com/openai/openai-python/issues/939)) ([ec65124](https://raw.githubusercontent.com/openai/openai-python/main/ec65124))
* **internal:** reformat imports ([#944](https://github.com/openai/openai-python/issues/944)) ([5290639](https://raw.githubusercontent.com/openai/openai-python/main/5290639))
* **internal:** update formatting ([#941](https://github.com/openai/openai-python/issues/941)) ([8e5a156](https://raw.githubusercontent.com/openai/openai-python/main/8e5a156))
* **package:** lift anyio v4 restriction ([#927](https://github.com/openai/openai-python/issues/927)) ([be0438a](https://raw.githubusercontent.com/openai/openai-python/main/be0438a))

### Documentation

* fix typo in example ([#950](https://github.com/openai/openai-python/issues/950)) ([54f0ce0](https://raw.githubusercontent.com/openai/openai-python/main/54f0ce0))

## 1.3.7 (2023-12-01)

Full Changelog: [v1.3.6...v1.3.7](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.6...v1.3.7)

### Bug Fixes

* **client:** correct base_url setter implementation ([#919](https://github.com/openai/openai-python/issues/919)) ([135d9cf](https://raw.githubusercontent.com/openai/openai-python/main/135d9cf))
* **client:** don't cause crashes when inspecting the module ([#897](https://github.com/openai/openai-python/issues/897)) ([db029a5](https://raw.githubusercontent.com/openai/openai-python/main/db029a5))
* **client:** ensure retried requests are closed ([#902](https://github.com/openai/openai-python/issues/902)) ([e025e6b](https://raw.githubusercontent.com/openai/openai-python/main/e025e6b))

### Chores

* **internal:** add tests for proxy change ([#899](https://github.com/openai/openai-python/issues/899)) ([71a13d0](https://raw.githubusercontent.com/openai/openai-python/main/71a13d0))
* **internal:** remove unused type var ([#915](https://github.com/openai/openai-python/issues/915)) ([4233bcd](https://raw.githubusercontent.com/openai/openai-python/main/4233bcd))
* **internal:** replace string concatenation with f-strings ([#908](https://github.com/openai/openai-python/issues/908)) ([663a8f6](https://raw.githubusercontent.com/openai/openai-python/main/663a8f6))
* **internal:** replace string concatenation with f-strings ([#909](https://github.com/openai/openai-python/issues/909)) ([caab767](https://raw.githubusercontent.com/openai/openai-python/main/caab767))

### Documentation

* fix typo in readme ([#904](https://github.com/openai/openai-python/issues/904)) ([472cd44](https://raw.githubusercontent.com/openai/openai-python/main/472cd44))
* **readme:** update example snippets ([#907](https://github.com/openai/openai-python/issues/907)) ([bbb648e](https://raw.githubusercontent.com/openai/openai-python/main/bbb648e))

## 1.3.6 (2023-11-28)

Full Changelog: [v1.3.5...v1.3.6](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.5...v1.3.6)

### Bug Fixes

* **client:** add support for streaming binary responses ([#866](https://github.com/openai/openai-python/issues/866)) ([2470d25](https://raw.githubusercontent.com/openai/openai-python/main/2470d25))

### Chores

* **deps:** bump mypy to v1.7.1 ([#891](https://github.com/openai/openai-python/issues/891)) ([11fcb2a](https://raw.githubusercontent.com/openai/openai-python/main/11fcb2a))
* **internal:** send more detailed x-stainless headers ([#877](https://github.com/openai/openai-python/issues/877)) ([69e0549](https://raw.githubusercontent.com/openai/openai-python/main/69e0549))
* revert binary streaming change ([#875](https://github.com/openai/openai-python/issues/875)) ([0a06d6a](https://raw.githubusercontent.com/openai/openai-python/main/0a06d6a))

### Documentation

* **readme:** minor updates ([#894](https://github.com/openai/openai-python/issues/894)) ([5458457](https://raw.githubusercontent.com/openai/openai-python/main/5458457))
* **readme:** update examples ([#893](https://github.com/openai/openai-python/issues/893)) ([124da87](https://raw.githubusercontent.com/openai/openai-python/main/124da87))
* update readme code snippet ([#890](https://github.com/openai/openai-python/issues/890)) ([c522f21](https://raw.githubusercontent.com/openai/openai-python/main/c522f21))

## 1.3.5 (2023-11-21)

Full Changelog: [v1.3.4...v1.3.5](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.4...v1.3.5)

### Bug Fixes

* **azure:** ensure custom options can be passed to copy ([#858](https://github.com/openai/openai-python/issues/858)) ([05ca0d6](https://raw.githubusercontent.com/openai/openai-python/main/05ca0d6))

### Chores

* **package:** add license classifier ([#826](https://github.com/openai/openai-python/issues/826)) ([bec004d](https://raw.githubusercontent.com/openai/openai-python/main/bec004d))
* **package:** add license classifier metadata ([#860](https://github.com/openai/openai-python/issues/860)) ([80dffb1](https://raw.githubusercontent.com/openai/openai-python/main/80dffb1))

## 1.3.4 (2023-11-21)

Full Changelog: [v1.3.3...v1.3.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.3...v1.3.4)

### Bug Fixes

* **client:** attempt to parse unknown json content types ([#854](https://github.com/openai/openai-python/issues/854)) ([ba50466](https://raw.githubusercontent.com/openai/openai-python/main/ba50466))

### Chores

* **examples:** fix static types in assistants example ([#852](https://github.com/openai/openai-python/issues/852)) ([5b47b2c](https://raw.githubusercontent.com/openai/openai-python/main/5b47b2c))

## 1.3.3 (2023-11-17)

Full Changelog: [v1.3.2...v1.3.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.2...v1.3.3)

### Chores

* **internal:** update type hint for helper function ([#846](https://github.com/openai/openai-python/issues/846)) ([9a5966c](https://raw.githubusercontent.com/openai/openai-python/main/9a5966c))

## 1.3.2 (2023-11-16)

Full Changelog: [v1.3.1...v1.3.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.1...v1.3.2)

### Documentation

* **readme:** minor updates ([#841](https://github.com/openai/openai-python/issues/841)) ([7273ad1](https://raw.githubusercontent.com/openai/openai-python/main/7273ad1))

## 1.3.1 (2023-11-16)

Full Changelog: [v1.3.0...v1.3.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.3.0...v1.3.1)

### Chores

* **internal:** add publish script ([#838](https://github.com/openai/openai-python/issues/838)) ([3ea41bc](https://raw.githubusercontent.com/openai/openai-python/main/3ea41bc))

## 1.3.0 (2023-11-15)

Full Changelog: [v1.2.4...v1.3.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.2.4...v1.3.0)

### Features

* **api:** add gpt-3.5-turbo-1106 ([#813](https://github.com/openai/openai-python/issues/813)) ([9bb3c4e](https://raw.githubusercontent.com/openai/openai-python/main/9bb3c4e))
* **client:** support reading the base url from an env variable ([#829](https://github.com/openai/openai-python/issues/829)) ([ca5fdc6](https://raw.githubusercontent.com/openai/openai-python/main/ca5fdc6))

### Bug Fixes

* **breaking!:** correct broken type names in moderation categories  ([#811](https://github.com/openai/openai-python/issues/811)) ([0bc211f](https://raw.githubusercontent.com/openai/openai-python/main/0bc211f))

### Chores

* fix typo in docs and add request header for function calls ([#807](https://github.com/openai/openai-python/issues/807)) ([cbef703](https://raw.githubusercontent.com/openai/openai-python/main/cbef703))
* **internal:** fix devcontainer interpeter path ([#810](https://github.com/openai/openai-python/issues/810)) ([0acc07d](https://raw.githubusercontent.com/openai/openai-python/main/0acc07d))

### Documentation

* add azure env vars ([#814](https://github.com/openai/openai-python/issues/814)) ([bd8e32a](https://raw.githubusercontent.com/openai/openai-python/main/bd8e32a))
* fix code comment typo ([#790](https://github.com/openai/openai-python/issues/790)) ([8407a27](https://raw.githubusercontent.com/openai/openai-python/main/8407a27))
* **readme:** fix broken azure_ad notebook link ([#781](https://github.com/openai/openai-python/issues/781)) ([3b92cdf](https://raw.githubusercontent.com/openai/openai-python/main/3b92cdf))

## 1.2.4 (2023-11-13)

Full Changelog: [v1.2.3...v1.2.4](https://raw.githubusercontent.com/openai/openai-python/main/v1.2.3...v1.2.4)

### Bug Fixes

* **client:** retry if SSLWantReadError occurs in the async client ([#804](https://github.com/openai/openai-python/issues/804)) ([be82288](https://raw.githubusercontent.com/openai/openai-python/main/be82288))

## 1.2.3 (2023-11-10)

Full Changelog: [v1.2.2...v1.2.3](https://raw.githubusercontent.com/openai/openai-python/main/v1.2.2...v1.2.3)

### Bug Fixes

* **cli/audio:** file format detection failing for whisper ([#733](https://github.com/openai/openai-python/issues/733)) ([01079d6](https://raw.githubusercontent.com/openai/openai-python/main/01079d6))
* **client:** correctly flush the stream response body ([#771](https://github.com/openai/openai-python/issues/771)) ([0d52731](https://raw.githubusercontent.com/openai/openai-python/main/0d52731))
* **client:** serialise pydantic v1 default fields correctly in params ([#776](https://github.com/openai/openai-python/issues/776)) ([d4c49ad](https://raw.githubusercontent.com/openai/openai-python/main/d4c49ad))
* **models:** mark unknown fields as set in pydantic v1 ([#772](https://github.com/openai/openai-python/issues/772)) ([ae032a1](https://raw.githubusercontent.com/openai/openai-python/main/ae032a1))
* prevent IndexError in fine-tunes CLI ([#768](https://github.com/openai/openai-python/issues/768)) ([42f1633](https://raw.githubusercontent.com/openai/openai-python/main/42f1633))

### Documentation

* reword package description ([#764](https://github.com/openai/openai-python/issues/764)) ([9ff10df](https://raw.githubusercontent.com/openai/openai-python/main/9ff10df))

## 1.2.2 (2023-11-09)

Full Changelog: [v1.2.1...v1.2.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.2.1...v1.2.2)

### Bug Fixes

* **client:** correctly assign error properties ([#759](https://github.com/openai/openai-python/issues/759)) ([ef264d2](https://raw.githubusercontent.com/openai/openai-python/main/ef264d2))

### Documentation

* **readme:** link to migration guide ([#761](https://github.com/openai/openai-python/issues/761)) ([ddde839](https://raw.githubusercontent.com/openai/openai-python/main/ddde839))

## 1.2.1 (2023-11-09)

Full Changelog: [v1.2.0...v1.2.1](https://raw.githubusercontent.com/openai/openai-python/main/v1.2.0...v1.2.1)

### Documentation

* **readme:** fix nested params example ([#756](https://github.com/openai/openai-python/issues/756)) ([ffbe5ec](https://raw.githubusercontent.com/openai/openai-python/main/ffbe5ec))

### Refactors

* **client:** deprecate files.retrieve_content in favour of files.content ([#753](https://github.com/openai/openai-python/issues/753)) ([eea5bc1](https://raw.githubusercontent.com/openai/openai-python/main/eea5bc1))

## 1.2.0 (2023-11-08)

Full Changelog: [v1.1.2...v1.2.0](https://raw.githubusercontent.com/openai/openai-python/main/v1.1.2...v1.2.0)

### Features

* **api:** unify function types ([#741](https://github.com/openai/openai-python/issues/741)) ([ed16c4d](https://raw.githubusercontent.com/openai/openai-python/main/ed16c4d))
* **client:** support passing chunk size for binary responses ([#747](https://github.com/openai/openai-python/issues/747)) ([c0c89b7](https://raw.githubusercontent.com/openai/openai-python/main/c0c89b7))

### Bug Fixes

* **api:** update embedding response object type ([#739](https://github.com/openai/openai-python/issues/739)) ([29182c4](https://raw.githubusercontent.com/openai/openai-python/main/29182c4))
* **client:** show a helpful error message if the v0 API is used ([#743](https://github.com/openai/openai-python/issues/743)) ([920567c](https://raw.githubusercontent.com/openai/openai-python/main/920567c))

### Chores

* **internal:** improve github devcontainer setup ([#737](https://github.com/openai/openai-python/issues/737)) ([0ac1abb](https://raw.githubusercontent.com/openai/openai-python/main/0ac1abb))

### Refactors

* **api:** rename FunctionObject to FunctionDefinition ([#746](https://github.com/openai/openai-python/issues/746)) ([1afd138](https://raw.githubusercontent.com/openai/openai-python/main/1afd138))

## 1.1.2 (2023-11-08)

Full Changelog: [v1.1.1...v1.1.2](https://raw.githubusercontent.com/openai/openai-python/main/v1.1.1...v1.1.2)

### Bug Fixes

* **api:** accidentally required params, add new models & other fixes ([#729](https://github.com/openai/openai-python/issues/729)) ([03c3e03](https://raw.githubusercontent.com/openai/openai-python/main/03c3e03))
* asssitant_deleted -&gt; assistant_deleted ([#711](https://github.com/openai/openai-python/issues/711)) ([287b51e](https://raw.githubusercontent.com/openai/openai-python/main/287b51e))

### Chores

* **docs:** fix github links ([#719](https://github.com/openai/openai-python/issues/719)) ([0cda8ca](https://raw.githubusercontent.com/openai/openai-python/main/0cda8ca))
* **internal:** fix some typos ([#718](https://github.com/openai/openai-python/issues/718)) ([894ad87](https://raw.githubusercontent.com/openai/openai-python/main/894ad87))
