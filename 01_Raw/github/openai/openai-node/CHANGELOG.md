# Changelog

## 6.36.0 (2026-05-01)

Full Changelog: [v6.35.0...v6.36.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.35.0...v6.36.0)

### Features

* **api:** add group_type/user metadata fields, update types across admin resources ([cc52f97](https://raw.githubusercontent.com/openai/openai-node/main/cc52f97))
* **api:** add support for Admin API Keys per endpoint ([770d187](https://raw.githubusercontent.com/openai/openai-node/main/770d187))
* **api:** admin API updates ([ee2bd2d](https://raw.githubusercontent.com/openai/openai-node/main/ee2bd2d))
* **api:** manual updates ([6af2b6d](https://raw.githubusercontent.com/openai/openai-node/main/6af2b6d))
* **api:** manual updates ([f2dceda](https://raw.githubusercontent.com/openai/openai-node/main/f2dceda))

### Bug Fixes

* **api:** support admin api key auth ([e3862a3](https://raw.githubusercontent.com/openai/openai-node/main/e3862a3))
* **api:** tighten auth header selection ([f1203bd](https://raw.githubusercontent.com/openai/openai-node/main/f1203bd))

### Chores

* **format:** run eslint and prettier separately ([104543a](https://raw.githubusercontent.com/openai/openai-node/main/104543a))
* **internal:** codegen related update ([05d86da](https://raw.githubusercontent.com/openai/openai-node/main/05d86da))
* **internal:** codegen related update ([f184586](https://raw.githubusercontent.com/openai/openai-node/main/f184586))

## 6.35.0 (2026-04-28)

Full Changelog: [v6.34.0...v6.35.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.34.0...v6.35.0)

### Features

* **api:** Add detail to InputFileContent ([910ec5d](https://raw.githubusercontent.com/openai/openai-node/main/910ec5d))
* **api:** add OAuthErrorCode type ([f84bd1f](https://raw.githubusercontent.com/openai/openai-node/main/f84bd1f))
* **api:** add prompt_cache_retention parameter to responses compact ([c486d1f](https://raw.githubusercontent.com/openai/openai-node/main/c486d1f))
* **api:** add web_search_call.results to ResponseIncludable ([72449a1](https://raw.githubusercontent.com/openai/openai-node/main/72449a1))
* **api:** manual updates ([b742f1f](https://raw.githubusercontent.com/openai/openai-node/main/b742f1f))
* **client:** add support for binary messages ([c498cc3](https://raw.githubusercontent.com/openai/openai-node/main/c498cc3))
* **client:** add support for path parameters in websockets clients ([e0aba70](https://raw.githubusercontent.com/openai/openai-node/main/e0aba70))
* **client:** add support for queuing messages when waiting for a connection ([fd8868c](https://raw.githubusercontent.com/openai/openai-node/main/fd8868c))
* **client:** add support for WebSockets in the browser when using simple auth ([27bda6a](https://raw.githubusercontent.com/openai/openai-node/main/27bda6a))
* **client:** support automatic reconnection for websockets ([189410b](https://raw.githubusercontent.com/openai/openai-node/main/189410b))
* **typescript:** expose underlying WebSocket type ([7e96939](https://raw.githubusercontent.com/openai/openai-node/main/7e96939))

### Bug Fixes

* **client:** allow single messages greater than the size of the websockets queue ([ad19ab2](https://raw.githubusercontent.com/openai/openai-node/main/ad19ab2))
* **internal:** gitignore generated `oidc` dir ([cf860f6](https://raw.githubusercontent.com/openai/openai-node/main/cf860f6))
* **types:** correct prompt_cache_retention enum value in chat/completions and responses ([5a81e1a](https://raw.githubusercontent.com/openai/openai-node/main/5a81e1a))
* **types:** preserve emitted ts-ignore comments ([1cde375](https://raw.githubusercontent.com/openai/openai-node/main/1cde375))

### Chores

* **ci:** remove release-doctor workflow ([e5ab4d1](https://raw.githubusercontent.com/openai/openai-node/main/e5ab4d1))
* **format:** apply prettier output ([80fa23d](https://raw.githubusercontent.com/openai/openai-node/main/80fa23d))
* **format:** ignore release-updated jsr config ([f606e8b](https://raw.githubusercontent.com/openai/openai-node/main/f606e8b))
* **formatter:** run prettier and eslint separately ([68a988e](https://raw.githubusercontent.com/openai/openai-node/main/68a988e))
* **internal:** codegen related update ([7673137](https://raw.githubusercontent.com/openai/openai-node/main/7673137))
* **internal:** fix package.json duplicate keys ([5f075a8](https://raw.githubusercontent.com/openai/openai-node/main/5f075a8))
* **internal:** more robust bootstrap script ([252e70a](https://raw.githubusercontent.com/openai/openai-node/main/252e70a))
* **internal:** version bump ([34c84ee](https://raw.githubusercontent.com/openai/openai-node/main/34c84ee))
* **tests:** bump steady to v0.22.1 ([316bdba](https://raw.githubusercontent.com/openai/openai-node/main/316bdba))

### Documentation

* improve examples ([6400d19](https://raw.githubusercontent.com/openai/openai-node/main/6400d19))

## 6.34.0 (2026-04-08)

Full Changelog: [v6.33.0...v6.34.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.33.0...v6.34.0)

### Features

* **api:** add phase field to Message in conversations ([eb7cbc1](https://raw.githubusercontent.com/openai/openai-node/main/eb7cbc1))
* **client:** add support for short-lived tokens ([#839](https://github.com/openai/openai-node/issues/839)) ([a72ebcf](https://raw.githubusercontent.com/openai/openai-node/main/a72ebcf))

### Bug Fixes

* **api:** remove web_search_call.results from ResponseIncludable in responses ([1f6968e](https://raw.githubusercontent.com/openai/openai-node/main/1f6968e))

### Chores

* **internal:** codegen related update ([1081460](https://raw.githubusercontent.com/openai/openai-node/main/1081460))
* **internal:** update multipart form array serialization ([3faee8d](https://raw.githubusercontent.com/openai/openai-node/main/3faee8d))
* **tests:** bump steady to v0.20.1 ([b73cc6b](https://raw.githubusercontent.com/openai/openai-node/main/b73cc6b))

### Documentation

* **api:** add multi-file ingestion recommendations to vector-stores files/file-batches ([1bc32a3](https://raw.githubusercontent.com/openai/openai-node/main/1bc32a3))

## 6.33.0 (2026-03-25)

Full Changelog: [v6.32.0...v6.33.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.32.0...v6.33.0)

### Features

* **api:** add keys field to computer action types ([27a850e](https://raw.githubusercontent.com/openai/openai-node/main/27a850e))
* **client:** add async iterator and stream() to WebSocket classes ([e1c16ee](https://raw.githubusercontent.com/openai/openai-node/main/e1c16ee))

### Bug Fixes

* **api:** align SDK response types with expanded item schemas ([491cd52](https://raw.githubusercontent.com/openai/openai-node/main/491cd52))
* **types:** make type required in ResponseInputMessageItem ([2012293](https://raw.githubusercontent.com/openai/openai-node/main/2012293))

### Chores

* **ci:** skip lint on metadata-only changes ([74a917f](https://raw.githubusercontent.com/openai/openai-node/main/74a917f))
* **internal:** refactor imports ([cfe9c60](https://raw.githubusercontent.com/openai/openai-node/main/cfe9c60))
* **internal:** update gitignore ([71bd114](https://raw.githubusercontent.com/openai/openai-node/main/71bd114))
* **tests:** bump steady to v0.19.4 ([f2e9dea](https://raw.githubusercontent.com/openai/openai-node/main/f2e9dea))
* **tests:** bump steady to v0.19.5 ([37c6cf4](https://raw.githubusercontent.com/openai/openai-node/main/37c6cf4))
* **tests:** bump steady to v0.19.6 ([496b3af](https://raw.githubusercontent.com/openai/openai-node/main/496b3af))
* **tests:** bump steady to v0.19.7 ([8491eb6](https://raw.githubusercontent.com/openai/openai-node/main/8491eb6))

### Refactors

* **tests:** switch from prism to steady ([47c0581](https://raw.githubusercontent.com/openai/openai-node/main/47c0581))

## 6.32.0 (2026-03-17)

Full Changelog: [v6.31.0...v6.32.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.31.0...v6.32.0)

### Features

* **api:** 5.4 nano and mini model slugs ([068df6d](https://raw.githubusercontent.com/openai/openai-node/main/068df6d))

## 6.31.0 (2026-03-16)

Full Changelog: [v6.30.1...v6.31.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.30.1...v6.31.0)

### Features

* **api:** add in/nin filter types to ComparisonFilter ([b2eda27](https://raw.githubusercontent.com/openai/openai-node/main/b2eda27))

## 6.30.1 (2026-03-16)

Full Changelog: [v6.30.0...v6.30.1](https://raw.githubusercontent.com/openai/openai-node/main/v6.30.0...v6.30.1)

### Chores

* **internal:** tweak CI branches ([25f5d74](https://raw.githubusercontent.com/openai/openai-node/main/25f5d74))

## 6.30.0 (2026-03-16)

Full Changelog: [v6.29.0...v6.30.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.29.0...v6.30.0)

### Features

* **api:** add /v1/videos endpoint option to batches ([271d879](https://raw.githubusercontent.com/openai/openai-node/main/271d879))
* **api:** add defer_loading field to NamespaceTool ([7cc8f0a](https://raw.githubusercontent.com/openai/openai-node/main/7cc8f0a))

### Bug Fixes

* **api:** oidc publishing for npm ([fa50066](https://raw.githubusercontent.com/openai/openai-node/main/fa50066))

## 6.29.0 (2026-03-13)

Full Changelog: [v6.28.0...v6.29.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.28.0...v6.29.0)

### Features

* **api:** custom voices ([a11307a](https://raw.githubusercontent.com/openai/openai-node/main/a11307a))

## 6.28.0 (2026-03-13)

Full Changelog: [v6.27.0...v6.28.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.27.0...v6.28.0)

### Features

* **api:** manual updates ([d543959](https://raw.githubusercontent.com/openai/openai-node/main/d543959))
* **api:** manual updates ([4f87840](https://raw.githubusercontent.com/openai/openai-node/main/4f87840))
* **api:** sora api improvements: character api, video extensions/edits, higher resolution exports. ([262dac2](https://raw.githubusercontent.com/openai/openai-node/main/262dac2))

### Bug Fixes

* **types:** remove detail field from ResponseInputFile and ResponseInputFileContent ([8d6c0cd](https://raw.githubusercontent.com/openai/openai-node/main/8d6c0cd))

### Chores

* **internal:** update dependencies to address dependabot vulnerabilities ([f5810ee](https://raw.githubusercontent.com/openai/openai-node/main/f5810ee))
* match http protocol with ws protocol instead of wss ([6f4e936](https://raw.githubusercontent.com/openai/openai-node/main/6f4e936))
* **mcp-server:** improve instructions ([aad9ca1](https://raw.githubusercontent.com/openai/openai-node/main/aad9ca1))
* use proper capitalization for WebSockets ([cb4cf62](https://raw.githubusercontent.com/openai/openai-node/main/cb4cf62))

## 6.27.0 (2026-03-05)

Full Changelog: [v6.26.0...v6.27.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.26.0...v6.27.0)

### Features

* **api:** The GA ComputerTool now uses the CompuerTool class. The 'computer_use_preview' tool is moved to ComputerUsePreview ([0206188](https://raw.githubusercontent.com/openai/openai-node/main/0206188))

### Chores

* **internal:** improve import alias names ([9cc2478](https://raw.githubusercontent.com/openai/openai-node/main/9cc2478))

## 6.26.0 (2026-03-05)

Full Changelog: [v6.25.0...v6.26.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.25.0...v6.26.0)

### Features

* **api:** gpt-5.4, tool search tool, and new computer tool ([1d1e5a9](https://raw.githubusercontent.com/openai/openai-node/main/1d1e5a9))

### Bug Fixes

* **api:** internal schema fixes ([6b401ad](https://raw.githubusercontent.com/openai/openai-node/main/6b401ad))
* **api:** manual updates ([2b54919](https://raw.githubusercontent.com/openai/openai-node/main/2b54919))
* **api:** readd phase ([4a0cf29](https://raw.githubusercontent.com/openai/openai-node/main/4a0cf29))
* **api:** remove phase from message types, prompt_cache_key param in responses ([088fca6](https://raw.githubusercontent.com/openai/openai-node/main/088fca6))

### Chores

* **internal:** codegen related update ([6a0aa9e](https://raw.githubusercontent.com/openai/openai-node/main/6a0aa9e))
* **internal:** codegen related update ([b2a4299](https://raw.githubusercontent.com/openai/openai-node/main/b2a4299))
* **internal:** move stringifyQuery implementation to internal function ([f9f4660](https://raw.githubusercontent.com/openai/openai-node/main/f9f4660))
* **internal:** reduce warnings ([7e19492](https://raw.githubusercontent.com/openai/openai-node/main/7e19492))

## 6.25.0 (2026-02-24)

Full Changelog: [v6.24.0...v6.25.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.24.0...v6.25.0)

### Features

* **api:** add phase ([e32b853](https://raw.githubusercontent.com/openai/openai-node/main/e32b853))

### Bug Fixes

* **api:** fix phase enum ([2ffe1be](https://raw.githubusercontent.com/openai/openai-node/main/2ffe1be))
* **api:** phase docs ([7fdfa38](https://raw.githubusercontent.com/openai/openai-node/main/7fdfa38))

### Chores

* **internal:** refactor sse event parsing ([0ea2380](https://raw.githubusercontent.com/openai/openai-node/main/0ea2380))

## 6.24.0 (2026-02-24)

Full Changelog: [v6.23.0...v6.24.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.23.0...v6.24.0)

### Features

* **api:** add gpt-realtime-1.5 and gpt-audio-1.5 models to realtime ([75875bf](https://raw.githubusercontent.com/openai/openai-node/main/75875bf))

## 6.23.0 (2026-02-23)

Full Changelog: [v6.22.0...v6.23.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.22.0...v6.23.0)

### Features

* **api:** websockets for responses api ([c6b96b8](https://raw.githubusercontent.com/openai/openai-node/main/c6b96b8))

### Bug Fixes

* **docs/contributing:** correct pnpm link command ([8a198a5](https://raw.githubusercontent.com/openai/openai-node/main/8a198a5))
* **internal:** skip tests that depend on mock server ([3d88cb0](https://raw.githubusercontent.com/openai/openai-node/main/3d88cb0))

### Chores

* **internal/client:** fix form-urlencoded requests ([646cedd](https://raw.githubusercontent.com/openai/openai-node/main/646cedd))
* update mock server docs ([29f78f3](https://raw.githubusercontent.com/openai/openai-node/main/29f78f3))

### Documentation

* **api:** document 2000 file limit in file-batches create parameters ([ff7bde0](https://raw.githubusercontent.com/openai/openai-node/main/ff7bde0))
* **api:** enhance method descriptions across audio/chat/skills/videos/responses ([f5e02a1](https://raw.githubusercontent.com/openai/openai-node/main/f5e02a1))
* **api:** update safety_identifier description in chat/responses ([a55e0ef](https://raw.githubusercontent.com/openai/openai-node/main/a55e0ef))

## 6.22.0 (2026-02-14)

Full Changelog: [v6.21.0...v6.22.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.21.0...v6.22.0)

### Features

* **api:** container network_policy and skills ([65c1482](https://raw.githubusercontent.com/openai/openai-node/main/65c1482))

### Bug Fixes

* **docs:** restore helper methods in API reference ([3a4c189](https://raw.githubusercontent.com/openai/openai-node/main/3a4c189))
* **webhooks:** restore webhook type exports ([49bbf46](https://raw.githubusercontent.com/openai/openai-node/main/49bbf46))

### Chores

* **internal:** avoid type checking errors with ts-reset ([4b0d1f2](https://raw.githubusercontent.com/openai/openai-node/main/4b0d1f2))

### Documentation

* split `api.md` by standalone resources ([48e07d6](https://raw.githubusercontent.com/openai/openai-node/main/48e07d6))
* update comment ([e3a1ea0](https://raw.githubusercontent.com/openai/openai-node/main/e3a1ea0))

## 6.21.0 (2026-02-10)

Full Changelog: [v6.20.0...v6.21.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.20.0...v6.21.0)

### Features

* **api:** support for images in batch api ([017ba1c](https://raw.githubusercontent.com/openai/openai-node/main/017ba1c))

## 6.20.0 (2026-02-10)

Full Changelog: [v6.19.0...v6.20.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.19.0...v6.20.0)

### Features

* **api:** skills and hosted shell ([e4bdd62](https://raw.githubusercontent.com/openai/openai-node/main/e4bdd62))

## 6.19.0 (2026-02-09)

Full Changelog: [v6.18.0...v6.19.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.18.0...v6.19.0)

### Features

* **api:** responses context_management ([40e7671](https://raw.githubusercontent.com/openai/openai-node/main/40e7671))

## 6.18.0 (2026-02-05)

Full Changelog: [v6.17.0...v6.18.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.17.0...v6.18.0)

### Features

* **api:** image generation actions for responses; ResponseFunctionCallArgumentsDoneEvent.name ([d373c32](https://raw.githubusercontent.com/openai/openai-node/main/d373c32))

### Bug Fixes

* **client:** avoid memory leak with abort signals ([b449f36](https://raw.githubusercontent.com/openai/openai-node/main/b449f36))
* **client:** avoid removing abort listener too early ([1c045f7](https://raw.githubusercontent.com/openai/openai-node/main/1c045f7))
* **client:** undo change to web search Find action ([8259b45](https://raw.githubusercontent.com/openai/openai-node/main/8259b45))
* **client:** update type for `find_in_page` action ([9aa8d98](https://raw.githubusercontent.com/openai/openai-node/main/9aa8d98))

### Chores

* **client:** do not parse responses with empty content-length ([4a118fa](https://raw.githubusercontent.com/openai/openai-node/main/4a118fa))
* **client:** restructure abort controller binding ([a4d7151](https://raw.githubusercontent.com/openai/openai-node/main/a4d7151))
* **internal:** fix pagination internals not accepting option promises ([6677905](https://raw.githubusercontent.com/openai/openai-node/main/6677905))

## 6.17.0 (2026-01-28)

Full Changelog: [v6.16.0...v6.17.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.16.0...v6.17.0)

### Features

* **api:** add shell_call_output status field ([edf9590](https://raw.githubusercontent.com/openai/openai-node/main/edf9590))
* **api:** api update ([6a2eb80](https://raw.githubusercontent.com/openai/openai-node/main/6a2eb80))
* **api:** api updates ([19ca100](https://raw.githubusercontent.com/openai/openai-node/main/19ca100))

### Bug Fixes

* **api:** mark assistants as deprecated ([3ae2a14](https://raw.githubusercontent.com/openai/openai-node/main/3ae2a14))

### Chores

* **ci:** upgrade `actions/github-script` ([4ea73d3](https://raw.githubusercontent.com/openai/openai-node/main/4ea73d3))
* **internal:** update `actions/checkout` version ([f163b77](https://raw.githubusercontent.com/openai/openai-node/main/f163b77))
* **internal:** upgrade babel, qs, js-yaml ([2e2f3c6](https://raw.githubusercontent.com/openai/openai-node/main/2e2f3c6))

## 6.16.0 (2026-01-09)

Full Changelog: [v6.15.0...v6.16.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.15.0...v6.16.0)

### Features

* **api:** add new Response completed_at prop ([ca40534](https://raw.githubusercontent.com/openai/openai-node/main/ca40534))
* **ci:** add breaking change detection workflow ([a6f3dea](https://raw.githubusercontent.com/openai/openai-node/main/a6f3dea))

### Chores

* break long lines in snippets into multiline ([80dee2f](https://raw.githubusercontent.com/openai/openai-node/main/80dee2f))
* **internal:** codegen related update ([b2fac3e](https://raw.githubusercontent.com/openai/openai-node/main/b2fac3e))

## 6.15.0 (2025-12-19)

Full Changelog: [v6.14.0...v6.15.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.14.0...v6.15.0)

### Bug Fixes

* rebuild ([5627b41](https://raw.githubusercontent.com/openai/openai-node/main/5627b41))

## 6.14.0 (2025-12-16)

Full Changelog: [v6.13.0...v6.14.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.13.0...v6.14.0)

### Features

* **api:** gpt-image-1.5 ([6c1ac1d](https://raw.githubusercontent.com/openai/openai-node/main/6c1ac1d))

## 6.13.0 (2025-12-15)

Full Changelog: [v6.12.0...v6.13.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.12.0...v6.13.0)

### Features

* **api:** api update ([bc759dc](https://raw.githubusercontent.com/openai/openai-node/main/bc759dc))
* **api:** fix grader input list, add dated slugs for sora-2 ([6b2a38f](https://raw.githubusercontent.com/openai/openai-node/main/6b2a38f))

## 6.12.0 (2025-12-11)

Full Changelog: [v6.11.0...v6.12.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.11.0...v6.12.0)

### Features

* **api:** gpt 5.2 ([7000ddb](https://raw.githubusercontent.com/openai/openai-node/main/7000ddb))

## 6.11.0 (2025-12-10)

Full Changelog: [v6.10.0...v6.11.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.10.0...v6.11.0)

### Features

* **api:** make model required for the responses/compact endpoint ([0b52b12](https://raw.githubusercontent.com/openai/openai-node/main/0b52b12))

### Bug Fixes

* **mcp:** correct code tool API endpoint ([e3f2a33](https://raw.githubusercontent.com/openai/openai-node/main/e3f2a33))
* **mcp:** return correct lines on typescript errors ([f485c3c](https://raw.githubusercontent.com/openai/openai-node/main/f485c3c))

### Chores

* **internal:** codegen related update ([5af1c38](https://raw.githubusercontent.com/openai/openai-node/main/5af1c38))
* **internal:** codegen related update ([e43a8d9](https://raw.githubusercontent.com/openai/openai-node/main/e43a8d9))

## 6.10.0 (2025-12-04)

Full Changelog: [v6.9.1...v6.10.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.9.1...v6.10.0)

### Features

* **api:** gpt-5.1-codex-max and responses/compact ([935f79e](https://raw.githubusercontent.com/openai/openai-node/main/935f79e))

### Chores

* **client:** fix logger property type ([fdc671f](https://raw.githubusercontent.com/openai/openai-node/main/fdc671f))
* **internal:** upgrade eslint ([9de0f90](https://raw.githubusercontent.com/openai/openai-node/main/9de0f90))

## 6.9.1 (2025-11-17)

Full Changelog: [v6.9.0...v6.9.1](https://raw.githubusercontent.com/openai/openai-node/main/v6.9.0...v6.9.1)

### Bug Fixes

* **api:** align types of input items / output items for typescript ([99adaa7](https://raw.githubusercontent.com/openai/openai-node/main/99adaa7))

## 6.9.0 (2025-11-13)

Full Changelog: [v6.8.1...v6.9.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.8.1...v6.9.0)

### Features

* **api:** gpt 5.1 ([58e78a8](https://raw.githubusercontent.com/openai/openai-node/main/58e78a8))

### Chores

* add typescript-estree dependency for jsr readme script ([3759514](https://raw.githubusercontent.com/openai/openai-node/main/3759514))

## 6.8.1 (2025-11-05)

Full Changelog: [v6.8.0...v6.8.1](https://raw.githubusercontent.com/openai/openai-node/main/v6.8.0...v6.8.1)

### Bug Fixes

* **api:** fix nullability of logprobs ([40a403c](https://raw.githubusercontent.com/openai/openai-node/main/40a403c))

## 6.8.0 (2025-11-03)

Full Changelog: [v6.7.0...v6.8.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.7.0...v6.8.0)

### Features

* **api:** Realtime API token_limits, Hybrid searching ranking options ([6a5b48c](https://raw.githubusercontent.com/openai/openai-node/main/6a5b48c))
* **api:** remove InputAudio from ResponseInputContent ([9909fef](https://raw.githubusercontent.com/openai/openai-node/main/9909fef))

### Chores

* **internal:** codegen related update ([3ad52aa](https://raw.githubusercontent.com/openai/openai-node/main/3ad52aa))

## 6.7.0 (2025-10-24)

Full Changelog: [v6.6.0...v6.7.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.6.0...v6.7.0)

### Features

* add support for zod@4 schemas ([#1666](https://github.com/openai/openai-node/issues/1666)) ([10ef7ff](https://raw.githubusercontent.com/openai/openai-node/main/10ef7ff))

### Bug Fixes

* **api:** docs updates ([2591c21](https://raw.githubusercontent.com/openai/openai-node/main/2591c21))

## 6.6.0 (2025-10-20)

Full Changelog: [v6.5.0...v6.6.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.5.0...v6.6.0)

### Features

* **api:** Add responses.input_tokens.count ([520c8a9](https://raw.githubusercontent.com/openai/openai-node/main/520c8a9))

### Bug Fixes

* **api:** internal openapi updates ([d4aaef9](https://raw.githubusercontent.com/openai/openai-node/main/d4aaef9))

## 6.5.0 (2025-10-17)

Full Changelog: [v6.4.0...v6.5.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.4.0...v6.5.0)

### Features

* **api:** api update ([4d21af3](https://raw.githubusercontent.com/openai/openai-node/main/4d21af3))

## 6.4.0 (2025-10-16)

Full Changelog: [v6.3.0...v6.4.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.3.0...v6.4.0)

### Features

* **api:** Add support for gpt-4o-transcribe-diarize on audio/transcriptions endpoint ([2d27392](https://raw.githubusercontent.com/openai/openai-node/main/2d27392))

## 6.3.0 (2025-10-10)

Full Changelog: [v6.2.0...v6.3.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.2.0...v6.3.0)

### Features

* **api:** comparison filter in/not in ([1a733c6](https://raw.githubusercontent.com/openai/openai-node/main/1a733c6))

### Chores

* **internal:** use npm pack for build uploads ([a532410](https://raw.githubusercontent.com/openai/openai-node/main/a532410))

## 6.2.0 (2025-10-06)

Full Changelog: [v6.1.0...v6.2.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.1.0...v6.2.0)

### Features

* **api:** dev day 2025 launches ([f2816db](https://raw.githubusercontent.com/openai/openai-node/main/f2816db))

### Chores

* **internal:** codegen related update ([b6f64b7](https://raw.githubusercontent.com/openai/openai-node/main/b6f64b7))
* **jsdoc:** fix [@link](https://raw.githubusercontent.com/openai/openai-node/main/@link) annotations to refer only to parts of the package‘s public interface ([73e465d](https://raw.githubusercontent.com/openai/openai-node/main/73e465d))

## 6.1.0 (2025-10-02)

Full Changelog: [v6.0.1...v6.1.0](https://raw.githubusercontent.com/openai/openai-node/main/v6.0.1...v6.1.0)

### Features

* **api:** add support for realtime calls ([5de9585](https://raw.githubusercontent.com/openai/openai-node/main/5de9585))

## 6.0.1 (2025-10-01)

Full Changelog: [v6.0.0...v6.0.1](https://raw.githubusercontent.com/openai/openai-node/main/v6.0.0...v6.0.1)

### Bug Fixes

* **api:** add status, approval_request_id to MCP tool call ([498c6a5](https://raw.githubusercontent.com/openai/openai-node/main/498c6a5))

## 6.0.0 (2025-09-30)

Full Changelog: [v5.23.2...v6.0.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.23.2...v6.0.0)

### ⚠ BREAKING CHANGES

* **api:** `ResponseFunctionToolCallOutputItem.output` and `ResponseCustomToolCallOutput.output` now return `string | Array<ResponseInputText | ResponseInputImage | ResponseInputFile>` instead of `string` only. This may break existing callsites that assume `output` is always a string.

### Features

* **api:** Support images and files for function call outputs in responses, BatchUsage ([abe56f8](https://raw.githubusercontent.com/openai/openai-node/main/abe56f8))

### Chores

* compat with zod v4 ([#1658](https://github.com/openai/openai-node/issues/1658)) ([94569a0](https://raw.githubusercontent.com/openai/openai-node/main/94569a0))

## 5.23.2 (2025-09-29)

Full Changelog: [v5.23.1...v5.23.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.23.1...v5.23.2)

### Chores

* **env-tests:** upgrade jest-fixed-jsdom 0.0.9 -&gt; 0.0.10 ([6d6d0b0](https://raw.githubusercontent.com/openai/openai-node/main/6d6d0b0))
* **internal:** codegen related update ([1b684af](https://raw.githubusercontent.com/openai/openai-node/main/1b684af))
* **internal:** ignore .eslintcache ([da9e146](https://raw.githubusercontent.com/openai/openai-node/main/da9e146))

## 5.23.1 (2025-09-26)

Full Changelog: [v5.23.0...v5.23.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.23.0...v5.23.1)

### Bug Fixes

* **realtime:** remove beta header from GA classes ([a5e9e70](https://raw.githubusercontent.com/openai/openai-node/main/a5e9e70))

### Performance Improvements

* faster formatting ([d56f309](https://raw.githubusercontent.com/openai/openai-node/main/d56f309))

### Chores

* **internal:** fix incremental formatting in some cases ([166d28f](https://raw.githubusercontent.com/openai/openai-node/main/166d28f))
* **internal:** remove deprecated `compilerOptions.baseUrl` from tsconfig.json ([dfab408](https://raw.githubusercontent.com/openai/openai-node/main/dfab408))

## 5.23.0 (2025-09-23)

Full Changelog: [v5.22.1...v5.23.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.22.1...v5.23.0)

### Features

* **api:** gpt-5-codex ([2e4ece6](https://raw.githubusercontent.com/openai/openai-node/main/2e4ece6))

## 5.22.1 (2025-09-22)

Full Changelog: [v5.22.0...v5.22.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.22.0...v5.22.1)

### Bug Fixes

* **api:** fix mcp tool name ([fa9f305](https://raw.githubusercontent.com/openai/openai-node/main/fa9f305))

### Chores

* **api:** openapi updates for conversations ([975c075](https://raw.githubusercontent.com/openai/openai-node/main/975c075))
* do not install brew dependencies in ./scripts/bootstrap by default ([6f5e45f](https://raw.githubusercontent.com/openai/openai-node/main/6f5e45f))
* improve example values ([b336a64](https://raw.githubusercontent.com/openai/openai-node/main/b336a64))

## 5.22.0 (2025-09-19)

Full Changelog: [v5.21.0...v5.22.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.21.0...v5.22.0)

### Features

* **api:** add reasoning_text ([7ff6186](https://raw.githubusercontent.com/openai/openai-node/main/7ff6186))

### Chores

* **api:** manual fixes for streaming ([3a2ae4c](https://raw.githubusercontent.com/openai/openai-node/main/3a2ae4c))

## 5.21.0 (2025-09-17)

Full Changelog: [v5.20.3...v5.21.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.20.3...v5.21.0)

### Features

* **api:** type updates for conversations, reasoning_effort and results for evals ([f243f54](https://raw.githubusercontent.com/openai/openai-node/main/f243f54))

## 5.20.3 (2025-09-15)

Full Changelog: [v5.20.2...v5.20.3](https://raw.githubusercontent.com/openai/openai-node/main/v5.20.2...v5.20.3)

### Chores

* **api:** docs and spec refactoring ([05b4498](https://raw.githubusercontent.com/openai/openai-node/main/05b4498))

## 5.20.2 (2025-09-12)

Full Changelog: [v5.20.1...v5.20.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.20.1...v5.20.2)

### Bug Fixes

* coerce nullable values to undefined ([836d1b4](https://raw.githubusercontent.com/openai/openai-node/main/836d1b4))

### Chores

* **api:** Minor docs and type updates for realtime ([ccb00dc](https://raw.githubusercontent.com/openai/openai-node/main/ccb00dc))

## 5.20.1 (2025-09-10)

Full Changelog: [v5.20.0...v5.20.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.20.0...v5.20.1)

### Chores

* **api:** fix realtime GA types ([1c0d314](https://raw.githubusercontent.com/openai/openai-node/main/1c0d314))

## 5.20.0 (2025-09-08)

Full Changelog: [v5.19.1...v5.20.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.19.1...v5.20.0)

### Features

* **api:** ship the RealtimeGA API shape ([4286ddd](https://raw.githubusercontent.com/openai/openai-node/main/4286ddd))

### Chores

* ci build action ([c8ce143](https://raw.githubusercontent.com/openai/openai-node/main/c8ce143))

## 5.19.1 (2025-09-03)

Full Changelog: [v5.19.0...v5.19.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.19.0...v5.19.1)

### Bug Fixes

* **azure:** correctly send API key ([#1635](https://github.com/openai/openai-node/issues/1635)) ([08f6178](https://raw.githubusercontent.com/openai/openai-node/main/08f6178))

## 5.19.0 (2025-09-03)

Full Changelog: [v5.18.1...v5.19.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.18.1...v5.19.0)

### Features

* **api:** Add gpt-realtime models ([256d932](https://raw.githubusercontent.com/openai/openai-node/main/256d932))

## 5.18.1 (2025-09-02)

Full Changelog: [v5.18.0...v5.18.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.18.0...v5.18.1)

### Chores

* **api:** manual updates for ResponseInputAudio ([570501b](https://raw.githubusercontent.com/openai/openai-node/main/570501b))

## 5.18.0 (2025-09-02)

Full Changelog: [v5.17.0...v5.18.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.17.0...v5.18.0)

### Features

* **client:** support api key provider functions ([#1587](https://github.com/openai/openai-node/issues/1587)) ([c3a92c7](https://raw.githubusercontent.com/openai/openai-node/main/c3a92c7))

### Bug Fixes

* update non beta realtime websockets helpers ([265a42f](https://raw.githubusercontent.com/openai/openai-node/main/265a42f))

## 5.17.0 (2025-09-02)

Full Changelog: [v5.16.0...v5.17.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.16.0...v5.17.0)

### Features

* **api:** realtime API updates ([e817255](https://raw.githubusercontent.com/openai/openai-node/main/e817255))

### Chores

* **internal:** update global Error reference ([e566ff3](https://raw.githubusercontent.com/openai/openai-node/main/e566ff3))

## 5.16.0 (2025-08-26)

Full Changelog: [v5.15.0...v5.16.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.15.0...v5.16.0)

### Features

* **api:** add web search filters ([975b141](https://raw.githubusercontent.com/openai/openai-node/main/975b141))

### Chores

* **client:** qualify global Blob ([7998d3f](https://raw.githubusercontent.com/openai/openai-node/main/7998d3f))
* update CI script ([accb0c1](https://raw.githubusercontent.com/openai/openai-node/main/accb0c1))

## 5.15.0 (2025-08-21)

Full Changelog: [v5.14.0...v5.15.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.14.0...v5.15.0)

### Features

* **api:** Add connectors support for MCP tool ([048bee3](https://raw.githubusercontent.com/openai/openai-node/main/048bee3))
* **api:** adding support for /v1/conversations to the API ([1380d17](https://raw.githubusercontent.com/openai/openai-node/main/1380d17))

### Chores

* add package to package.json ([6748b2b](https://raw.githubusercontent.com/openai/openai-node/main/6748b2b))

## 5.14.0 (2025-08-20)

Full Changelog: [v5.13.1...v5.14.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.13.1...v5.14.0)

### Features

* **mcp:** add code execution tool ([3f8264c](https://raw.githubusercontent.com/openai/openai-node/main/3f8264c))

### Chores

* **internal/ci:** setup breaking change detection ([87e8004](https://raw.githubusercontent.com/openai/openai-node/main/87e8004))

## 5.13.1 (2025-08-19)

Full Changelog: [v5.13.0...v5.13.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.13.0...v5.13.1)

### Chores

* **api:** accurately represent shape for verbosity on Chat Completions ([5ddac3c](https://raw.githubusercontent.com/openai/openai-node/main/5ddac3c))

## 5.13.0 (2025-08-18)

Full Changelog: [v5.12.3...v5.13.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.12.3...v5.13.0)

### Features

* **api:** add new text parameters, expiration options ([499179c](https://raw.githubusercontent.com/openai/openai-node/main/499179c))

### Chores

* **deps:** update dependency @types/node to v20.17.58 ([7812d0d](https://raw.githubusercontent.com/openai/openai-node/main/7812d0d))
* **internal:** formatting change ([56b2073](https://raw.githubusercontent.com/openai/openai-node/main/56b2073))

## 5.12.3 (2025-08-12)

Full Changelog: [v5.12.2...v5.12.3](https://raw.githubusercontent.com/openai/openai-node/main/v5.12.2...v5.12.3)

### Chores

* **internal:** update comment in script ([2488faf](https://raw.githubusercontent.com/openai/openai-node/main/2488faf))
* update @stainless-api/prism-cli to v5.15.0 ([db44a7d](https://raw.githubusercontent.com/openai/openai-node/main/db44a7d))

## 5.12.2 (2025-08-08)

Full Changelog: [v5.12.1...v5.12.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.12.1...v5.12.2)

### Bug Fixes

* **client:** fix verbosity parameter location in Responses ([eaa246f](https://raw.githubusercontent.com/openai/openai-node/main/eaa246f))

## 5.12.1 (2025-08-07)

Full Changelog: [v5.12.0...v5.12.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.12.0...v5.12.1)

### Features

* **api:** adds GPT-5 and new API features: platform.openai.com/docs/guides/gpt-5 ([59acd85](https://raw.githubusercontent.com/openai/openai-node/main/59acd85))

### Chores

* **internal:** move publish config ([b3d02f6](https://raw.githubusercontent.com/openai/openai-node/main/b3d02f6))

## 5.12.0 (2025-08-05)

Full Changelog: [v5.11.0...v5.12.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.11.0...v5.12.0)

### Features

* **api:** manual updates ([f0d3056](https://raw.githubusercontent.com/openai/openai-node/main/f0d3056))

## 5.11.0 (2025-07-30)

Full Changelog: [v5.10.3...v5.11.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.10.3...v5.11.0)

### Features

* **api:** manual updates ([442dc25](https://raw.githubusercontent.com/openai/openai-node/main/442dc25))

## 5.10.3 (2025-07-30)

Full Changelog: [v5.10.2...v5.10.3](https://raw.githubusercontent.com/openai/openai-node/main/v5.10.2...v5.10.3)

### Bug Fixes

* **zod:** avoid adding redundant not to optional schemas [#1593](https://github.com/openai/openai-node/issues/1593) ([162b697](https://raw.githubusercontent.com/openai/openai-node/main/162b697))

### Chores

* **client:** refactor streaming slightly to better future proof it ([292427f](https://raw.githubusercontent.com/openai/openai-node/main/292427f))
* **internal:** remove redundant imports config ([28dd66d](https://raw.githubusercontent.com/openai/openai-node/main/28dd66d))
* **internal:** version bump ([56e0760](https://raw.githubusercontent.com/openai/openai-node/main/56e0760))

## 5.10.2 (2025-07-22)

Full Changelog: [v5.10.1...v5.10.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.10.1...v5.10.2)

### Chores

* **api:** event shapes more accurate ([78f4e1d](https://raw.githubusercontent.com/openai/openai-node/main/78f4e1d))
* **internal:** version bump ([ea885ca](https://raw.githubusercontent.com/openai/openai-node/main/ea885ca))

### Documentation

* fix typos in helpers and realtime ([#1592](https://github.com/openai/openai-node/issues/1592)) ([17733b7](https://raw.githubusercontent.com/openai/openai-node/main/17733b7))

## 5.10.1 (2025-07-16)

Full Changelog: [v5.10.0...v5.10.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.10.0...v5.10.1)

### Chores

* **internal:** version bump ([896b418](https://raw.githubusercontent.com/openai/openai-node/main/896b418))
* **ts:** reorder package.json imports ([2f8d2f7](https://raw.githubusercontent.com/openai/openai-node/main/2f8d2f7))

## 5.10.0 (2025-07-16)

Full Changelog: [v5.9.2...v5.10.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.9.2...v5.10.0)

### Features

* **api:** manual updates ([35338b4](https://raw.githubusercontent.com/openai/openai-node/main/35338b4))

### Chores

* **internal:** version bump ([3d9de4b](https://raw.githubusercontent.com/openai/openai-node/main/3d9de4b))

## 5.9.2 (2025-07-15)

Full Changelog: [v5.9.1...v5.9.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.9.1...v5.9.2)

### Chores

* **api:** update realtime specs ([4a20a3d](https://raw.githubusercontent.com/openai/openai-node/main/4a20a3d))
* **internal:** version bump ([103e8de](https://raw.githubusercontent.com/openai/openai-node/main/103e8de))

## 5.9.1 (2025-07-15)

Full Changelog: [v5.9.0...v5.9.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.9.0...v5.9.1)

### Chores

* **api:** update realtime specs, build config ([bb4649f](https://raw.githubusercontent.com/openai/openai-node/main/bb4649f))

## 5.9.0 (2025-07-10)

Full Changelog: [v5.8.4...v5.9.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.8.4...v5.9.0)

### Features

* **api:** add file_url, fix event ID ([5f5d39e](https://raw.githubusercontent.com/openai/openai-node/main/5f5d39e))

## 5.8.4 (2025-07-10)

Full Changelog: [v5.8.3...v5.8.4](https://raw.githubusercontent.com/openai/openai-node/main/v5.8.3...v5.8.4)

### Chores

* **internal:** bump undici version in tests ([6f38b80](https://raw.githubusercontent.com/openai/openai-node/main/6f38b80))
* make some internal functions async ([841940d](https://raw.githubusercontent.com/openai/openai-node/main/841940d))

## 5.8.3 (2025-07-08)

Full Changelog: [v5.8.2...v5.8.3](https://raw.githubusercontent.com/openai/openai-node/main/v5.8.2...v5.8.3)

### Bug Fixes

* avoid console usage ([aec57c5](https://raw.githubusercontent.com/openai/openai-node/main/aec57c5))

### Chores

* add docs to RequestOptions type ([3735172](https://raw.githubusercontent.com/openai/openai-node/main/3735172))
* **ci:** only run for pushes and fork pull requests ([e200bc4](https://raw.githubusercontent.com/openai/openai-node/main/e200bc4))
* **client:** improve path param validation ([b5a043b](https://raw.githubusercontent.com/openai/openai-node/main/b5a043b))
* **internal/tests:** pin bun types version ([fcffa88](https://raw.githubusercontent.com/openai/openai-node/main/fcffa88))

## 5.8.2 (2025-06-27)

Full Changelog: [v5.8.1...v5.8.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.8.1...v5.8.2)

### Bug Fixes

* **client:** get fetchOptions type more reliably ([b3c959d](https://raw.githubusercontent.com/openai/openai-node/main/b3c959d))

## 5.8.1 (2025-06-26)

Full Changelog: [v5.8.0...v5.8.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.8.0...v5.8.1)

### Bug Fixes

* **client:** ensure addOutputText is called on responses.retrieve ([d55bb64](https://raw.githubusercontent.com/openai/openai-node/main/d55bb64))

### Chores

* **api:** remove unsupported property ([1966954](https://raw.githubusercontent.com/openai/openai-node/main/1966954))
* **docs:** update README to include links to docs on Webhooks ([586d5da](https://raw.githubusercontent.com/openai/openai-node/main/586d5da))
* **webhooks:** make private methods really private ([0ee396a](https://raw.githubusercontent.com/openai/openai-node/main/0ee396a))

## 5.8.0 (2025-06-26)

Full Changelog: [v5.7.0...v5.8.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.7.0...v5.8.0)

### Features

* **api:** webhook and deep research support ([f2b4f66](https://raw.githubusercontent.com/openai/openai-node/main/f2b4f66))

### Bug Fixes

* **ci:** release-doctor — report correct token name ([aed2587](https://raw.githubusercontent.com/openai/openai-node/main/aed2587))

### Refactors

* **types:** replace Record with mapped types ([7865910](https://raw.githubusercontent.com/openai/openai-node/main/7865910))

## 5.7.0 (2025-06-23)

Full Changelog: [v5.6.0...v5.7.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.6.0...v5.7.0)

### Features

* **api:** update api shapes for usage and code interpreter ([f2100e8](https://raw.githubusercontent.com/openai/openai-node/main/f2100e8))

## 5.6.0 (2025-06-20)

Full Changelog: [v5.5.1...v5.6.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.5.1...v5.6.0)

### Features

* **api:** make model and inputs not required to create response ([52211c0](https://raw.githubusercontent.com/openai/openai-node/main/52211c0))

### Bug Fixes

* **client:** explicitly copy fetch in withOptions ([0efacae](https://raw.githubusercontent.com/openai/openai-node/main/0efacae))

### Chores

* **readme:** update badges ([6898954](https://raw.githubusercontent.com/openai/openai-node/main/6898954))
* **readme:** use better example snippet for undocumented params ([668611f](https://raw.githubusercontent.com/openai/openai-node/main/668611f))

## 5.5.1 (2025-06-17)

Full Changelog: [v5.5.0...v5.5.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.5.0...v5.5.1)

### Chores

* **ci:** enable for pull requests ([e1cf00c](https://raw.githubusercontent.com/openai/openai-node/main/e1cf00c))

## 5.5.0 (2025-06-16)

Full Changelog: [v5.4.0...v5.5.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.4.0...v5.5.0)

### Features

* **api:** manual updates ([ab6b57c](https://raw.githubusercontent.com/openai/openai-node/main/ab6b57c))

## 5.4.0 (2025-06-16)

Full Changelog: [v5.3.0...v5.4.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.3.0...v5.4.0)

### Features

* **api:** add reusable prompt IDs ([c720bb3](https://raw.githubusercontent.com/openai/openai-node/main/c720bb3))
* **client:** add support for endpoint-specific base URLs ([05f558b](https://raw.githubusercontent.com/openai/openai-node/main/05f558b))

### Bug Fixes

* publish script — handle NPM errors correctly ([a803cce](https://raw.githubusercontent.com/openai/openai-node/main/a803cce))

### Chores

* **client:** refactor imports ([9eb4470](https://raw.githubusercontent.com/openai/openai-node/main/9eb4470))
* **internal:** add pure annotations, make base APIResource abstract ([418eb02](https://raw.githubusercontent.com/openai/openai-node/main/418eb02))

## 5.3.0 (2025-06-10)

Full Changelog: [v5.2.0...v5.3.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.2.0...v5.3.0)

### Features

* **api:** Add o3-pro model IDs ([9988f8e](https://raw.githubusercontent.com/openai/openai-node/main/9988f8e))

## 5.2.0 (2025-06-09)

Full Changelog: [v5.1.1...v5.2.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.1.1...v5.2.0)

### Features

* **api:** Add tools and structured outputs to evals ([64844f1](https://raw.githubusercontent.com/openai/openai-node/main/64844f1))

### Bug Fixes

* **changelog:** remove duplicated entries ([18484cc](https://raw.githubusercontent.com/openai/openai-node/main/18484cc))

### Chores

* avoid type error in certain environments ([44ac3d9](https://raw.githubusercontent.com/openai/openai-node/main/44ac3d9))

### Documentation

* **changelog:** reference MIGRATION.md ([b3d488f](https://raw.githubusercontent.com/openai/openai-node/main/b3d488f)), closes [#1539](https://github.com/openai/openai-node/issues/1539)

## 5.1.1 (2025-06-05)

Full Changelog: [v5.1.0...v5.1.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.1.0...v5.1.1)

### Bug Fixes

* **assistants:** handle thread.run.incomplete while streaming ([8f5e7f3](https://raw.githubusercontent.com/openai/openai-node/main/8f5e7f3))

### Chores

* **docs:** use top-level-await in example snippets ([065d3b0](https://raw.githubusercontent.com/openai/openai-node/main/065d3b0))
* **internal:** fix readablestream types in node 20 ([771ae81](https://raw.githubusercontent.com/openai/openai-node/main/771ae81))

## 5.1.0 (2025-06-03)

Full Changelog: [v5.0.2...v5.1.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.0.2...v5.1.0)

### Features

* **api:** add new realtime and audio models, realtime session options ([1219f09](https://raw.githubusercontent.com/openai/openai-node/main/1219f09))

### Chores

* adjust eslint.config.mjs ignore pattern ([9b5c898](https://raw.githubusercontent.com/openai/openai-node/main/9b5c898))
* **api:** update type names ([7c296d6](https://raw.githubusercontent.com/openai/openai-node/main/7c296d6))

## 5.0.2 (2025-06-02)

Full Changelog: [v5.0.1...v5.0.2](https://raw.githubusercontent.com/openai/openai-node/main/v5.0.1...v5.0.2)

### Bug Fixes

* **api:** Fix evals and code interpreter interfaces ([992a9d8](https://raw.githubusercontent.com/openai/openai-node/main/992a9d8))

### Chores

* **deps:** bump eslint-plugin-prettier ([1428a8b](https://raw.githubusercontent.com/openai/openai-node/main/1428a8b))
* **internal:** codegen related update ([a65428f](https://raw.githubusercontent.com/openai/openai-node/main/a65428f))

## 5.0.1 (2025-05-29)

Full Changelog: [v5.0.0...v5.0.1](https://raw.githubusercontent.com/openai/openai-node/main/v5.0.0...v5.0.1)

### Chores

* sync changes ([90b100d](https://raw.githubusercontent.com/openai/openai-node/main/90b100d))
* **types:** add missing type annotation ([de37b55](https://raw.githubusercontent.com/openai/openai-node/main/de37b55))

## 5.0.0 (2025-05-29)

This release migrates from node-fetch to builtin fetch, for full release notes see [MIGRATION.md](https://raw.githubusercontent.com/openai/openai-node/main/MIGRATION.md).

Full Changelog: [v5.0.0-alpha.0...v5.0.0](https://raw.githubusercontent.com/openai/openai-node/main/v5.0.0-alpha.0...v5.0.0)

### Features

* add audio helpers ([ec5067d](https://raw.githubusercontent.com/openai/openai-node/main/ec5067d))
* add migration guide ([cfd2088](https://raw.githubusercontent.com/openai/openai-node/main/cfd2088))
* add SKIP_BREW env var to ./scripts/bootstrap ([7ea4a24](https://raw.githubusercontent.com/openai/openai-node/main/7ea4a24))
* **api:** add /v1/responses and built-in tools ([91af47c](https://raw.githubusercontent.com/openai/openai-node/main/91af47c))
* **api:** add `get /chat/completions` endpoint ([9697139](https://raw.githubusercontent.com/openai/openai-node/main/9697139))
* **api:** add `get /responses/{response_id}/input_items` endpoint ([f2c5aba](https://raw.githubusercontent.com/openai/openai-node/main/f2c5aba))
* **api:** add container endpoint ([3ffca5c](https://raw.githubusercontent.com/openai/openai-node/main/3ffca5c))
* **api:** Add evalapi to sdk ([70092d7](https://raw.githubusercontent.com/openai/openai-node/main/70092d7))
* **api:** add gpt-4.5-preview ([1d4478d](https://raw.githubusercontent.com/openai/openai-node/main/1d4478d))
* **api:** add image sizes, reasoning encryption ([0c25021](https://raw.githubusercontent.com/openai/openai-node/main/0c25021))
* **api:** add o3 and o4-mini model IDs ([19cda5d](https://raw.githubusercontent.com/openai/openai-node/main/19cda5d))
* **api:** Add reinforcement fine-tuning api support ([e6bbaf5](https://raw.githubusercontent.com/openai/openai-node/main/e6bbaf5))
* **api:** add support for storing chat completions ([59da177](https://raw.githubusercontent.com/openai/openai-node/main/59da177))
* **api:** adding gpt-4.1 family of model IDs ([8a2a745](https://raw.githubusercontent.com/openai/openai-node/main/8a2a745))
* **api:** adding new image model support ([a0010fd](https://raw.githubusercontent.com/openai/openai-node/main/a0010fd))
* **api:** Config update for pakrym-stream-param ([469ad7b](https://raw.githubusercontent.com/openai/openai-node/main/469ad7b))
* **api:** further updates for evals API ([3f6f248](https://raw.githubusercontent.com/openai/openai-node/main/3f6f248))
* **api:** manual updates ([debe529](https://raw.githubusercontent.com/openai/openai-node/main/debe529))
* **api:** manual updates ([e83286b](https://raw.githubusercontent.com/openai/openai-node/main/e83286b))
* **api:** manual updates ([959eace](https://raw.githubusercontent.com/openai/openai-node/main/959eace))
* **api:** manual updates ([179a607](https://raw.githubusercontent.com/openai/openai-node/main/179a607))
* **api:** manual updates ([0cb0c86](https://raw.githubusercontent.com/openai/openai-node/main/0cb0c86))
* **api:** manual updates ([678ae6b](https://raw.githubusercontent.com/openai/openai-node/main/678ae6b))
* **api:** manual updates ([4560dc6](https://raw.githubusercontent.com/openai/openai-node/main/4560dc6))
* **api:** manual updates ([554c3b1](https://raw.githubusercontent.com/openai/openai-node/main/554c3b1))
* **api:** manual updates ([b893d81](https://raw.githubusercontent.com/openai/openai-node/main/b893d81))
* **api:** manual updates ([c1c2819](https://raw.githubusercontent.com/openai/openai-node/main/c1c2819))
* **api:** manual updates ([efce6d3](https://raw.githubusercontent.com/openai/openai-node/main/efce6d3))
* **api:** manual updates ([32afb00](https://raw.githubusercontent.com/openai/openai-node/main/32afb00))
* **api:** new API tools ([fb4014f](https://raw.githubusercontent.com/openai/openai-node/main/fb4014f))
* **api:** new models for TTS, STT, + new audio features for Realtime ([#1407](https://github.com/openai/openai-node/issues/1407)) ([d11b13c](https://raw.githubusercontent.com/openai/openai-node/main/d11b13c))
* **api:** new streaming helpers for background responses ([1ddd6ff](https://raw.githubusercontent.com/openai/openai-node/main/1ddd6ff))
* **api:** o1-pro now available through the API ([#1398](https://github.com/openai/openai-node/issues/1398)) ([aefd267](https://raw.githubusercontent.com/openai/openai-node/main/aefd267))
* **api:** responses x eval api ([ea1d56c](https://raw.githubusercontent.com/openai/openai-node/main/ea1d56c))
* **api:** Updating Assistants and Evals API schemas ([8cc63d3](https://raw.githubusercontent.com/openai/openai-node/main/8cc63d3))
* **client:** accept RFC6838 JSON content types ([67da9ce](https://raw.githubusercontent.com/openai/openai-node/main/67da9ce))
* **client:** add Realtime API support ([7737d25](https://raw.githubusercontent.com/openai/openai-node/main/7737d25))
* **client:** add withOptions helper ([7e9ea85](https://raw.githubusercontent.com/openai/openai-node/main/7e9ea85))
* **client:** improve logging ([ead0ba4](https://raw.githubusercontent.com/openai/openai-node/main/ead0ba4))
* **client:** promote beta completions methods to GA ([4c622f9](https://raw.githubusercontent.com/openai/openai-node/main/4c622f9))

### Bug Fixes

* **api:** add missing file rank enum + more metadata ([b943a0a](https://raw.githubusercontent.com/openai/openai-node/main/b943a0a))
* **api:** correct some Responses types ([#1391](https://github.com/openai/openai-node/issues/1391)) ([e983d0c](https://raw.githubusercontent.com/openai/openai-node/main/e983d0c))
* **api:** improve type resolution when importing as a package ([#1444](https://github.com/openai/openai-node/issues/1444)) ([4af79dd](https://raw.githubusercontent.com/openai/openai-node/main/4af79dd))
* **assistants:** handle `thread.run.incomplete` event ([a2714bb](https://raw.githubusercontent.com/openai/openai-node/main/a2714bb))
* **audio:** correctly handle transcription streaming ([9c7d352](https://raw.githubusercontent.com/openai/openai-node/main/9c7d352))
* avoid type error in certain environments ([#1413](https://github.com/openai/openai-node/issues/1413)) ([f395e95](https://raw.githubusercontent.com/openai/openai-node/main/f395e95))
* **azure/audio:** use model param for deployments ([0eda70a](https://raw.githubusercontent.com/openai/openai-node/main/0eda70a))
* **azure:** add /images/edits to deployments endpoints ([#1509](https://github.com/openai/openai-node/issues/1509)) ([4b18059](https://raw.githubusercontent.com/openai/openai-node/main/4b18059))
* **azure:** add /images/edits to deployments endpoints ([#1509](https://github.com/openai/openai-node/issues/1509)) ([84fc31a](https://raw.githubusercontent.com/openai/openai-node/main/84fc31a))
* **azure:** use correct internal method ([a9c7821](https://raw.githubusercontent.com/openai/openai-node/main/a9c7821))
* **client:** always overwrite when merging headers ([c160550](https://raw.githubusercontent.com/openai/openai-node/main/c160550))
* **client:** fix export map for index exports ([#1328](https://github.com/openai/openai-node/issues/1328)) ([26d5868](https://raw.githubusercontent.com/openai/openai-node/main/26d5868))
* **client:** fix export map for index exports, accept BunFile ([9416c96](https://raw.githubusercontent.com/openai/openai-node/main/9416c96))
* **client:** fix TypeError with undefined File ([0e980d0](https://raw.githubusercontent.com/openai/openai-node/main/0e980d0))
* **client:** remove duplicate types ([bee2ce5](https://raw.githubusercontent.com/openai/openai-node/main/bee2ce5))
* **client:** remove duplicate types ([#1410](https://github.com/openai/openai-node/issues/1410)) ([23fd3ff](https://raw.githubusercontent.com/openai/openai-node/main/23fd3ff))
* **client:** return binary content from `get /containers/{container_id}/files/{file_id}/content` ([8502966](https://raw.githubusercontent.com/openai/openai-node/main/8502966))
* **client:** return binary content from `get /containers/{container_id}/files/{file_id}/content` ([899869b](https://raw.githubusercontent.com/openai/openai-node/main/899869b))
* **client:** return binary content from `get /containers/{container_id}/files/{file_id}/content` ([83129d7](https://raw.githubusercontent.com/openai/openai-node/main/83129d7))
* **client:** send `X-Stainless-Timeout` in seconds ([5a272a7](https://raw.githubusercontent.com/openai/openai-node/main/5a272a7))
* **client:** send `X-Stainless-Timeout` in seconds ([#1442](https://github.com/openai/openai-node/issues/1442)) ([5e5e460](https://raw.githubusercontent.com/openai/openai-node/main/5e5e460))
* **client:** send all configured auth headers ([ee01414](https://raw.githubusercontent.com/openai/openai-node/main/ee01414))
* compat with more runtimes ([f743730](https://raw.githubusercontent.com/openai/openai-node/main/f743730))
* correct imports ([21f2107](https://raw.githubusercontent.com/openai/openai-node/main/21f2107))
* correctly decode multi-byte characters over multiple chunks ([f3d7083](https://raw.githubusercontent.com/openai/openai-node/main/f3d7083))
* **docs:** correct docstring on responses.stream ([1847673](https://raw.githubusercontent.com/openai/openai-node/main/1847673))
* **ecosystem-tests/bun:** bump dependencies ([1e52734](https://raw.githubusercontent.com/openai/openai-node/main/1e52734))
* **ecosystem-tests/cloudflare-worker:** ignore lib errors for now ([157248a](https://raw.githubusercontent.com/openai/openai-node/main/157248a))
* **ecosystem-tests:** correct ecosystem tests setup ([6fa0675](https://raw.githubusercontent.com/openai/openai-node/main/6fa0675))
* **embeddings:** correctly decode base64 data ([#1448](https://github.com/openai/openai-node/issues/1448)) ([d6b99c8](https://raw.githubusercontent.com/openai/openai-node/main/d6b99c8))
* **exports:** add missing type exports ([a816029](https://raw.githubusercontent.com/openai/openai-node/main/a816029))
* **exports:** add missing type exports ([#1417](https://github.com/openai/openai-node/issues/1417)) ([06c03d7](https://raw.githubusercontent.com/openai/openai-node/main/06c03d7))
* **exports:** ensure resource imports don't require /index ([d028ad7](https://raw.githubusercontent.com/openai/openai-node/main/d028ad7))
* **helpers/zod:** error on optional + not nullable fields ([6e424b5](https://raw.githubusercontent.com/openai/openai-node/main/6e424b5))
* **internal:** add mts file + crypto shim types ([a06deb8](https://raw.githubusercontent.com/openai/openai-node/main/a06deb8))
* **internal:** clean up undefined File test ([da43aa9](https://raw.githubusercontent.com/openai/openai-node/main/da43aa9))
* **internal:** fix file uploads in node 18 jest ([abfff03](https://raw.githubusercontent.com/openai/openai-node/main/abfff03))
* **internal:** work around https://github.com/vercel/next.js/issues/76881 ([#1427](https://github.com/openai/openai-node/issues/1427)) ([84edc62](https://raw.githubusercontent.com/openai/openai-node/main/84edc62))
* **jsr:** correct zod config ([04e30c0](https://raw.githubusercontent.com/openai/openai-node/main/04e30c0))
* **jsr:** export realtime helpers ([0ea64eb](https://raw.githubusercontent.com/openai/openai-node/main/0ea64eb))
* **jsr:** export zod helpers ([77e1180](https://raw.githubusercontent.com/openai/openai-node/main/77e1180))
* **mcp:** remove unused tools.ts ([#1445](https://github.com/openai/openai-node/issues/1445)) ([4ba9947](https://raw.githubusercontent.com/openai/openai-node/main/4ba9947))
* optimize sse chunk reading off-by-one error ([#1339](https://github.com/openai/openai-node/issues/1339)) ([b0b4189](https://raw.githubusercontent.com/openai/openai-node/main/b0b4189))
* **package:** add chat/completions.ts back in ([#1333](https://github.com/openai/openai-node/issues/1333)) ([1f38cc1](https://raw.githubusercontent.com/openai/openai-node/main/1f38cc1))
* **parsing:** remove tool_calls default empty array ([#1341](https://github.com/openai/openai-node/issues/1341)) ([6d056bf](https://raw.githubusercontent.com/openai/openai-node/main/6d056bf))
* **realtime:** call .toString() on WebSocket url ([#1324](https://github.com/openai/openai-node/issues/1324)) ([6e9444c](https://raw.githubusercontent.com/openai/openai-node/main/6e9444c))
* **responses:** correct computer use enum value ([66fb815](https://raw.githubusercontent.com/openai/openai-node/main/66fb815))
* **responses:** correct reasoning output type ([9cb9576](https://raw.githubusercontent.com/openai/openai-node/main/9cb9576))
* **responses:** correctly add output_text ([8ae07cc](https://raw.githubusercontent.com/openai/openai-node/main/8ae07cc))
* **responses:** support streaming retrieve calls ([657807c](https://raw.githubusercontent.com/openai/openai-node/main/657807c))
* **tests/embeddings:** avoid cross-realm issue ([aceaac0](https://raw.githubusercontent.com/openai/openai-node/main/aceaac0))
* **tests:** don't rely on OPENAI_API_KEY env variable ([087580a](https://raw.githubusercontent.com/openai/openai-node/main/087580a))
* **tests:** manually reset node:buffer File ([1d18ed4](https://raw.githubusercontent.com/openai/openai-node/main/1d18ed4))
* **tests:** port tests to new setup ([9eb9854](https://raw.githubusercontent.com/openai/openai-node/main/9eb9854))
* **tests:** stop using node:stream ([317a04d](https://raw.githubusercontent.com/openai/openai-node/main/317a04d))
* **threads:** remove unused duplicative types ([0b77c7c](https://raw.githubusercontent.com/openai/openai-node/main/0b77c7c))
* **types:** export AssistantStream ([#1472](https://github.com/openai/openai-node/issues/1472)) ([bc492ba](https://raw.githubusercontent.com/openai/openai-node/main/bc492ba))
* **types:** export ParseableToolsParams ([#1486](https://github.com/openai/openai-node/issues/1486)) ([3e7c92c](https://raw.githubusercontent.com/openai/openai-node/main/3e7c92c))
* **types:** ignore missing `id` in responses pagination ([d2be74a](https://raw.githubusercontent.com/openai/openai-node/main/d2be74a))
* **types:** improve responses type names ([#1392](https://github.com/openai/openai-node/issues/1392)) ([4548326](https://raw.githubusercontent.com/openai/openai-node/main/4548326))
* **zod:** warn on optional field usage ([#1469](https://github.com/openai/openai-node/issues/1469)) ([aea2d12](https://raw.githubusercontent.com/openai/openai-node/main/aea2d12))

### Performance Improvements

* **embedding:** default embedding creation to base64 ([#1312](https://github.com/openai/openai-node/issues/1312)) ([be00d29](https://raw.githubusercontent.com/openai/openai-node/main/be00d29)), closes [#1310](https://github.com/openai/openai-node/issues/1310)

### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([1b0a94d](https://raw.githubusercontent.com/openai/openai-node/main/1b0a94d))
* add missing type alias exports ([5d75cb9](https://raw.githubusercontent.com/openai/openai-node/main/5d75cb9))
* **api:** updates to supported Voice IDs ([28130c7](https://raw.githubusercontent.com/openai/openai-node/main/28130c7))
* **ci:** add timeout thresholds for CI jobs ([5775451](https://raw.githubusercontent.com/openai/openai-node/main/5775451))
* **ci:** bump node version for release workflows ([bbf5d45](https://raw.githubusercontent.com/openai/openai-node/main/bbf5d45))
* **ci:** only use depot for staging repos ([c59c3b5](https://raw.githubusercontent.com/openai/openai-node/main/c59c3b5))
* **ci:** run on more branches and use depot runners ([e17a4f8](https://raw.githubusercontent.com/openai/openai-node/main/e17a4f8))
* **client:** drop support for EOL node versions ([a326944](https://raw.githubusercontent.com/openai/openai-node/main/a326944))
* **client:** expose headers on some streaming errors ([#1423](https://github.com/openai/openai-node/issues/1423)) ([6c93a23](https://raw.githubusercontent.com/openai/openai-node/main/6c93a23))
* **client:** minor internal fixes ([5032c28](https://raw.githubusercontent.com/openai/openai-node/main/5032c28))
* **client:** more accurate streaming errors ([0c21914](https://raw.githubusercontent.com/openai/openai-node/main/0c21914))
* **client:** move misc public files to new `core/` directory, deprecate old paths ([38c9d54](https://raw.githubusercontent.com/openai/openai-node/main/38c9d54))
* **client:** only accept standard types for file uploads ([53e35c8](https://raw.githubusercontent.com/openai/openai-node/main/53e35c8))
* deprecate Assistants API ([0be23b9](https://raw.githubusercontent.com/openai/openai-node/main/0be23b9))
* **docs:** add missing deprecation warnings ([995075b](https://raw.githubusercontent.com/openai/openai-node/main/995075b))
* **docs:** grammar improvements ([7761cfb](https://raw.githubusercontent.com/openai/openai-node/main/7761cfb))
* **docs:** improve docs for withResponse/asResponse ([9f4c30b](https://raw.githubusercontent.com/openai/openai-node/main/9f4c30b))
* **docs:** improve migration doc ([732d870](https://raw.githubusercontent.com/openai/openai-node/main/732d870))
* **docs:** update zod tool call example, fix azure tests ([f18ced8](https://raw.githubusercontent.com/openai/openai-node/main/f18ced8))
* **exports:** cleaner resource index imports ([#1396](https://github.com/openai/openai-node/issues/1396)) ([023d106](https://raw.githubusercontent.com/openai/openai-node/main/023d106))
* **exports:** stop using path fallbacks ([09af7ff](https://raw.githubusercontent.com/openai/openai-node/main/09af7ff))
* **exports:** stop using path fallbacks ([#1397](https://github.com/openai/openai-node/issues/1397)) ([7c3d212](https://raw.githubusercontent.com/openai/openai-node/main/7c3d212))
* fix example types ([20f179d](https://raw.githubusercontent.com/openai/openai-node/main/20f179d))
* improve publish-npm script --latest tag logic ([6207a2a](https://raw.githubusercontent.com/openai/openai-node/main/6207a2a))
* **internal:** add aliases for Record and Array ([#1443](https://github.com/openai/openai-node/issues/1443)) ([1cb66b6](https://raw.githubusercontent.com/openai/openai-node/main/1cb66b6))
* **internal:** add back release workflow ([ca6266e](https://raw.githubusercontent.com/openai/openai-node/main/ca6266e))
* **internal:** add Bun.File ecosystem test ([cb4194f](https://raw.githubusercontent.com/openai/openai-node/main/cb4194f))
* **internal:** add missing return type annotation ([#1334](https://github.com/openai/openai-node/issues/1334)) ([13aab10](https://raw.githubusercontent.com/openai/openai-node/main/13aab10))
* **internal:** add proxy ecosystem tests ([619711a](https://raw.githubusercontent.com/openai/openai-node/main/619711a))
* **internal:** bump migration cli version ([a899c97](https://raw.githubusercontent.com/openai/openai-node/main/a899c97))
* **internal:** codegen related update ([c735a3c](https://raw.githubusercontent.com/openai/openai-node/main/c735a3c))
* **internal:** fix devcontainers setup ([#1343](https://github.com/openai/openai-node/issues/1343)) ([9485f5d](https://raw.githubusercontent.com/openai/openai-node/main/9485f5d))
* **internal:** fix eslint ignores ([ad5a9b6](https://raw.githubusercontent.com/openai/openai-node/main/ad5a9b6))
* **internal:** fix examples ([#1457](https://github.com/openai/openai-node/issues/1457)) ([a100f0a](https://raw.githubusercontent.com/openai/openai-node/main/a100f0a))
* **internal:** fix format script ([3e1ea40](https://raw.githubusercontent.com/openai/openai-node/main/3e1ea40))
* **internal:** fix formatting ([6469d53](https://raw.githubusercontent.com/openai/openai-node/main/6469d53))
* **internal:** fix lint ([45a372c](https://raw.githubusercontent.com/openai/openai-node/main/45a372c))
* **internal:** fix release workflows ([353349d](https://raw.githubusercontent.com/openai/openai-node/main/353349d))
* **internal:** fix tests failing on node v18 ([c54270a](https://raw.githubusercontent.com/openai/openai-node/main/c54270a))
* **internal:** fix tests not always being type checked ([0266b41](https://raw.githubusercontent.com/openai/openai-node/main/0266b41))
* **internal:** improve node 18 shims ([ee3f483](https://raw.githubusercontent.com/openai/openai-node/main/ee3f483))
* **internal:** minor client file refactoring ([d1aa00a](https://raw.githubusercontent.com/openai/openai-node/main/d1aa00a))
* **internal:** only run examples workflow in main repo ([#1450](https://github.com/openai/openai-node/issues/1450)) ([93569f3](https://raw.githubusercontent.com/openai/openai-node/main/93569f3))
* **internal:** reduce CI branch coverage ([77fc77f](https://raw.githubusercontent.com/openai/openai-node/main/77fc77f))
* **internal:** refactor utils ([e7fbfbc](https://raw.githubusercontent.com/openai/openai-node/main/e7fbfbc))
* **internal:** remove CI condition ([#1381](https://github.com/openai/openai-node/issues/1381)) ([e905c95](https://raw.githubusercontent.com/openai/openai-node/main/e905c95))
* **internal:** remove unnecessary todo ([b55321e](https://raw.githubusercontent.com/openai/openai-node/main/b55321e))
* **internal:** run CI on update-specs branch ([9c45ef3](https://raw.githubusercontent.com/openai/openai-node/main/9c45ef3))
* **internal:** run example files in CI ([#1357](https://github.com/openai/openai-node/issues/1357)) ([1044c48](https://raw.githubusercontent.com/openai/openai-node/main/1044c48))
* **internal:** share typescript helpers ([2470933](https://raw.githubusercontent.com/openai/openai-node/main/2470933))
* **internal:** skip broken test ([#1458](https://github.com/openai/openai-node/issues/1458)) ([58f4559](https://raw.githubusercontent.com/openai/openai-node/main/58f4559))
* **internal:** update @types/bun ([d94b41a](https://raw.githubusercontent.com/openai/openai-node/main/d94b41a))
* **internal:** update release workflows ([2cbf49a](https://raw.githubusercontent.com/openai/openai-node/main/2cbf49a))
* **internal:** upload builds and expand CI branch coverage ([#1460](https://github.com/openai/openai-node/issues/1460)) ([2d45287](https://raw.githubusercontent.com/openai/openai-node/main/2d45287))
* **migration:** add beta handling ([3508099](https://raw.githubusercontent.com/openai/openai-node/main/3508099))
* move ChatModel type to shared ([236dbf4](https://raw.githubusercontent.com/openai/openai-node/main/236dbf4))
* **package:** remove engines ([500a82f](https://raw.githubusercontent.com/openai/openai-node/main/500a82f))
* **perf:** faster base64 decoding ([11b9534](https://raw.githubusercontent.com/openai/openai-node/main/11b9534))
* **tests:** improve enum examples ([#1454](https://github.com/openai/openai-node/issues/1454)) ([15a86c9](https://raw.githubusercontent.com/openai/openai-node/main/15a86c9))
* **tests:** stop using node-fetch, don't directly upload FormDataFile ([ebd464f](https://raw.githubusercontent.com/openai/openai-node/main/ebd464f))
* **tests:** switch proxy tests to fetchOptions ([da6ed5f](https://raw.githubusercontent.com/openai/openai-node/main/da6ed5f))
* **types:** improved go to definition on fetchOptions ([f1712cd](https://raw.githubusercontent.com/openai/openai-node/main/f1712cd))
* update next to 14.2.25 for CVE-2025-29927 ([1ed4288](https://raw.githubusercontent.com/openai/openai-node/main/1ed4288))
* workaround build errors ([e4a7f67](https://raw.githubusercontent.com/openai/openai-node/main/e4a7f67))
* workaround build errors ([d6b396b](https://raw.githubusercontent.com/openai/openai-node/main/d6b396b))

### Documentation

* add examples to tsdocs ([e8d2092](https://raw.githubusercontent.com/openai/openai-node/main/e8d2092))
* fix "procesing" -&gt; "processing" in realtime examples ([#1406](https://github.com/openai/openai-node/issues/1406)) ([dfbdc65](https://raw.githubusercontent.com/openai/openai-node/main/dfbdc65))
* **migration:** mention zod helpers error ([43b870d](https://raw.githubusercontent.com/openai/openai-node/main/43b870d))
* **readme:** fix typo ([c44ed98](https://raw.githubusercontent.com/openai/openai-node/main/c44ed98))
* **readme:** fix typo ([0989ddc](https://raw.githubusercontent.com/openai/openai-node/main/0989ddc))
* update URLs from stainlessapi.com to stainless.com ([#1352](https://github.com/openai/openai-node/issues/1352)) ([634a209](https://raw.githubusercontent.com/openai/openai-node/main/634a209))

### Refactors

* **client:** remove deprecated runFunctions method ([e29a009](https://raw.githubusercontent.com/openai/openai-node/main/e29a009))
* **functions:** rename function helper methods to include tools ([fdd6f66](https://raw.githubusercontent.com/openai/openai-node/main/fdd6f66))

## 4.104.0 (2025-05-29)

Full Changelog: [v4.103.0...v4.104.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.103.0...v4.104.0)

### Features

* **api:** Config update for pakrym-stream-param ([469ad7b](https://raw.githubusercontent.com/openai/openai-node/main/469ad7b))

### Bug Fixes

* **azure:** add /images/edits to deployments endpoints ([#1509](https://github.com/openai/openai-node/issues/1509)) ([84fc31a](https://raw.githubusercontent.com/openai/openai-node/main/84fc31a))
* **client:** return binary content from `get /containers/{container_id}/files/{file_id}/content` ([83129d7](https://raw.githubusercontent.com/openai/openai-node/main/83129d7))

### Chores

* deprecate Assistants API ([5b34fcd](https://raw.githubusercontent.com/openai/openai-node/main/5b34fcd))
* improve publish-npm script --latest tag logic ([6207a2a](https://raw.githubusercontent.com/openai/openai-node/main/6207a2a))
* **internal:** fix release workflows ([353349d](https://raw.githubusercontent.com/openai/openai-node/main/353349d))

## 4.103.0 (2025-05-22)

Full Changelog: [v4.102.0...v4.103.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.102.0...v4.103.0)

### Features

* **api:** new streaming helpers for background responses ([1ddd6ff](https://raw.githubusercontent.com/openai/openai-node/main/1ddd6ff))

## 4.102.0 (2025-05-21)

Full Changelog: [v4.101.0...v4.102.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.101.0...v4.102.0)

### Features

* **api:** add container endpoint ([e973476](https://raw.githubusercontent.com/openai/openai-node/main/e973476))

## 4.101.0 (2025-05-21)

Full Changelog: [v4.100.0...v4.101.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.100.0...v4.101.0)

### Features

* **api:** new API tools ([fb4014f](https://raw.githubusercontent.com/openai/openai-node/main/fb4014f))

### Chores

* **docs:** grammar improvements ([7761cfb](https://raw.githubusercontent.com/openai/openai-node/main/7761cfb))
* **internal:** version bump ([b40e830](https://raw.githubusercontent.com/openai/openai-node/main/b40e830))

## 4.100.0 (2025-05-16)

Full Changelog: [v4.99.0...v4.100.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.99.0...v4.100.0)

### Features

* **api:** further updates for evals API ([3f6f248](https://raw.githubusercontent.com/openai/openai-node/main/3f6f248))

### Chores

* **internal:** version bump ([5123fe0](https://raw.githubusercontent.com/openai/openai-node/main/5123fe0))

## 4.99.0 (2025-05-16)

Full Changelog: [v4.98.0...v4.99.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.98.0...v4.99.0)

### Features

* **api:** manual updates ([75eb804](https://raw.githubusercontent.com/openai/openai-node/main/75eb804))
* **api:** responses x eval api ([5029f1a](https://raw.githubusercontent.com/openai/openai-node/main/5029f1a))
* **api:** Updating Assistants and Evals API schemas ([27fd517](https://raw.githubusercontent.com/openai/openai-node/main/27fd517))

## 4.98.0 (2025-05-08)

Full Changelog: [v4.97.0...v4.98.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.97.0...v4.98.0)

### Features

* **api:** Add reinforcement fine-tuning api support ([4aa7a79](https://raw.githubusercontent.com/openai/openai-node/main/4aa7a79))

### Chores

* **ci:** bump node version for release workflows ([2961f63](https://raw.githubusercontent.com/openai/openai-node/main/2961f63))
* **internal:** fix formatting ([91a44fe](https://raw.githubusercontent.com/openai/openai-node/main/91a44fe))

### Documentation

* add examples to tsdocs ([7d841b7](https://raw.githubusercontent.com/openai/openai-node/main/7d841b7))

## 4.97.0 (2025-05-02)

Full Changelog: [v4.96.2...v4.97.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.96.2...v4.97.0)

### Features

* **api:** add image sizes, reasoning encryption ([9c2113a](https://raw.githubusercontent.com/openai/openai-node/main/9c2113a))

### Chores

* **docs:** add missing deprecation warnings ([253392c](https://raw.githubusercontent.com/openai/openai-node/main/253392c))

### Documentation

* fix "procesing" -&gt; "processing" in realtime examples ([#1406](https://github.com/openai/openai-node/issues/1406)) ([8717b9f](https://raw.githubusercontent.com/openai/openai-node/main/8717b9f))
* **readme:** fix typo ([cab3478](https://raw.githubusercontent.com/openai/openai-node/main/cab3478))

## 4.96.2 (2025-04-29)

Full Changelog: [v4.96.1...v4.96.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.96.1...v4.96.2)

### Bug Fixes

* **types:** export ParseableToolsParams ([#1486](https://github.com/openai/openai-node/issues/1486)) ([3e7c92c](https://raw.githubusercontent.com/openai/openai-node/main/3e7c92c))

### Chores

* **ci:** only use depot for staging repos ([214da39](https://raw.githubusercontent.com/openai/openai-node/main/214da39))
* **ci:** run on more branches and use depot runners ([ead76fc](https://raw.githubusercontent.com/openai/openai-node/main/ead76fc))

## 4.96.1 (2025-04-29)

Full Changelog: [v4.96.0...v4.96.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.96.0...v4.96.1)

### Bug Fixes

* **types:** export ParseableToolsParams ([#1486](https://github.com/openai/openai-node/issues/1486)) ([eb055b2](https://raw.githubusercontent.com/openai/openai-node/main/eb055b2))

### Chores

* **ci:** only use depot for staging repos ([e80af47](https://raw.githubusercontent.com/openai/openai-node/main/e80af47))
* **ci:** run on more branches and use depot runners ([b04a801](https://raw.githubusercontent.com/openai/openai-node/main/b04a801))

## 4.96.0 (2025-04-23)

Full Changelog: [v4.95.1...v4.96.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.95.1...v4.96.0)

### Features

* **api:** adding new image model support ([a00d331](https://raw.githubusercontent.com/openai/openai-node/main/a00d331))

### Bug Fixes

* **types:** export AssistantStream ([#1472](https://github.com/openai/openai-node/issues/1472)) ([626c844](https://raw.githubusercontent.com/openai/openai-node/main/626c844))

### Chores

* **ci:** add timeout thresholds for CI jobs ([e465063](https://raw.githubusercontent.com/openai/openai-node/main/e465063))

## 4.95.1 (2025-04-18)

Full Changelog: [v4.95.0...v4.95.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.95.0...v4.95.1)

### Bug Fixes

* **zod:** warn on optional field usage ([#1469](https://github.com/openai/openai-node/issues/1469)) ([aea2d12](https://raw.githubusercontent.com/openai/openai-node/main/aea2d12))

## 4.95.0 (2025-04-16)

Full Changelog: [v4.94.0...v4.95.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.94.0...v4.95.0)

### Features

* **api:** add o3 and o4-mini model IDs ([4845cd9](https://raw.githubusercontent.com/openai/openai-node/main/4845cd9))

## 4.94.0 (2025-04-14)

Full Changelog: [v4.93.0...v4.94.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.93.0...v4.94.0)

### Features

* **api:** adding gpt-4.1 family of model IDs ([bddcbcf](https://raw.githubusercontent.com/openai/openai-node/main/bddcbcf))
* **api:** manual updates ([7532f48](https://raw.githubusercontent.com/openai/openai-node/main/7532f48))

### Chores

* **client:** minor internal fixes ([d342f17](https://raw.githubusercontent.com/openai/openai-node/main/d342f17))
* **internal:** reduce CI branch coverage ([a49b94a](https://raw.githubusercontent.com/openai/openai-node/main/a49b94a))
* **internal:** upload builds and expand CI branch coverage ([#1460](https://github.com/openai/openai-node/issues/1460)) ([7e23bb4](https://raw.githubusercontent.com/openai/openai-node/main/7e23bb4))
* workaround build errors ([913eba8](https://raw.githubusercontent.com/openai/openai-node/main/913eba8))

## 4.93.0 (2025-04-08)

Full Changelog: [v4.92.1...v4.93.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.92.1...v4.93.0)

### Features

* **api:** Add evalapi to sdk ([#1456](https://github.com/openai/openai-node/issues/1456)) ([ee917e3](https://raw.githubusercontent.com/openai/openai-node/main/ee917e3))

### Chores

* **internal:** fix examples ([#1457](https://github.com/openai/openai-node/issues/1457)) ([a3dd0dd](https://raw.githubusercontent.com/openai/openai-node/main/a3dd0dd))
* **internal:** skip broken test ([#1458](https://github.com/openai/openai-node/issues/1458)) ([4d2f815](https://raw.githubusercontent.com/openai/openai-node/main/4d2f815))
* **tests:** improve enum examples ([#1454](https://github.com/openai/openai-node/issues/1454)) ([ecabce2](https://raw.githubusercontent.com/openai/openai-node/main/ecabce2))

## 4.92.1 (2025-04-07)

Full Changelog: [v4.92.0...v4.92.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.92.0...v4.92.1)

### Chores

* **internal:** only run examples workflow in main repo ([#1450](https://github.com/openai/openai-node/issues/1450)) ([5e49a7a](https://raw.githubusercontent.com/openai/openai-node/main/5e49a7a))

## 4.92.0 (2025-04-07)

Full Changelog: [v4.91.1...v4.92.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.91.1...v4.92.0)

### Features

* **api:** manual updates ([891754d](https://raw.githubusercontent.com/openai/openai-node/main/891754d))
* **api:** manual updates ([01e5546](https://raw.githubusercontent.com/openai/openai-node/main/01e5546))
* **api:** manual updates ([f38dbf3](https://raw.githubusercontent.com/openai/openai-node/main/f38dbf3))
* **api:** manual updates ([1f12253](https://raw.githubusercontent.com/openai/openai-node/main/1f12253))

### Bug Fixes

* **api:** improve type resolution when importing as a package ([#1444](https://github.com/openai/openai-node/issues/1444)) ([4aa46d6](https://raw.githubusercontent.com/openai/openai-node/main/4aa46d6))
* **client:** send `X-Stainless-Timeout` in seconds ([#1442](https://github.com/openai/openai-node/issues/1442)) ([aa4206c](https://raw.githubusercontent.com/openai/openai-node/main/aa4206c))
* **embeddings:** correctly decode base64 data ([#1448](https://github.com/openai/openai-node/issues/1448)) ([58128f7](https://raw.githubusercontent.com/openai/openai-node/main/58128f7))
* **mcp:** remove unused tools.ts ([#1445](https://github.com/openai/openai-node/issues/1445)) ([520a8fa](https://raw.githubusercontent.com/openai/openai-node/main/520a8fa))

### Chores

* **internal:** add aliases for Record and Array ([#1443](https://github.com/openai/openai-node/issues/1443)) ([b65391b](https://raw.githubusercontent.com/openai/openai-node/main/b65391b))

## 4.91.1 (2025-04-01)

Full Changelog: [v4.91.0...v4.91.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.91.0...v4.91.1)

### Bug Fixes

* **docs:** correct docstring on responses.stream ([1c8cd6a](https://raw.githubusercontent.com/openai/openai-node/main/1c8cd6a))

### Chores

* Remove deprecated/unused remote spec feature ([ce3dfa8](https://raw.githubusercontent.com/openai/openai-node/main/ce3dfa8))

## 4.91.0 (2025-03-31)

Full Changelog: [v4.90.0...v4.91.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.90.0...v4.91.0)

### Features

* **api:** add `get /responses/{response_id}/input_items` endpoint ([ef0e0ac](https://raw.githubusercontent.com/openai/openai-node/main/ef0e0ac))

### Performance Improvements

* **embedding:** default embedding creation to base64 ([#1312](https://github.com/openai/openai-node/issues/1312)) ([e54530e](https://raw.githubusercontent.com/openai/openai-node/main/e54530e)), closes [#1310](https://github.com/openai/openai-node/issues/1310)

## 4.90.0 (2025-03-27)

Full Changelog: [v4.89.1...v4.90.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.89.1...v4.90.0)

### Features

* **api:** add `get /chat/completions` endpoint ([2d6710a](https://raw.githubusercontent.com/openai/openai-node/main/2d6710a))

### Bug Fixes

* **audio:** correctly handle transcription streaming ([2a9b603](https://raw.githubusercontent.com/openai/openai-node/main/2a9b603))
* **internal:** work around https://github.com/vercel/next.js/issues/76881 ([#1427](https://github.com/openai/openai-node/issues/1427)) ([b467e94](https://raw.githubusercontent.com/openai/openai-node/main/b467e94))

### Chores

* add hash of OpenAPI spec/config inputs to .stats.yml ([45db35e](https://raw.githubusercontent.com/openai/openai-node/main/45db35e))
* **api:** updates to supported Voice IDs ([#1424](https://github.com/openai/openai-node/issues/1424)) ([404f4db](https://raw.githubusercontent.com/openai/openai-node/main/404f4db))
* **client:** expose headers on some streaming errors ([#1423](https://github.com/openai/openai-node/issues/1423)) ([b0783cc](https://raw.githubusercontent.com/openai/openai-node/main/b0783cc))

## 4.89.1 (2025-03-26)

Full Changelog: [v4.89.0...v4.89.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.89.0...v4.89.1)

### Bug Fixes

* avoid type error in certain environments ([#1413](https://github.com/openai/openai-node/issues/1413)) ([d3f6f8f](https://raw.githubusercontent.com/openai/openai-node/main/d3f6f8f))
* **client:** remove duplicate types ([#1410](https://github.com/openai/openai-node/issues/1410)) ([338878b](https://raw.githubusercontent.com/openai/openai-node/main/338878b))
* **exports:** add missing type exports ([#1417](https://github.com/openai/openai-node/issues/1417)) ([2d15ada](https://raw.githubusercontent.com/openai/openai-node/main/2d15ada))

### Chores

* **internal:** version bump ([#1408](https://github.com/openai/openai-node/issues/1408)) ([9c0949a](https://raw.githubusercontent.com/openai/openai-node/main/9c0949a))

## 4.89.0 (2025-03-20)

Full Changelog: [v4.88.0...v4.89.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.88.0...v4.89.0)

### Features

* add audio helpers ([ea1b6b4](https://raw.githubusercontent.com/openai/openai-node/main/ea1b6b4))
* **api:** new models for TTS, STT, + new audio features for Realtime ([#1407](https://github.com/openai/openai-node/issues/1407)) ([142933a](https://raw.githubusercontent.com/openai/openai-node/main/142933a))

### Chores

* **internal:** version bump ([#1400](https://github.com/openai/openai-node/issues/1400)) ([6838ab4](https://raw.githubusercontent.com/openai/openai-node/main/6838ab4))

## 4.88.0 (2025-03-19)

Full Changelog: [v4.87.4...v4.88.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.87.4...v4.88.0)

### Features

* **api:** o1-pro now available through the API ([#1398](https://github.com/openai/openai-node/issues/1398)) ([616a7e9](https://raw.githubusercontent.com/openai/openai-node/main/616a7e9))

### Chores

* **exports:** cleaner resource index imports ([#1396](https://github.com/openai/openai-node/issues/1396)) ([26b0856](https://raw.githubusercontent.com/openai/openai-node/main/26b0856))
* **exports:** stop using path fallbacks ([#1397](https://github.com/openai/openai-node/issues/1397)) ([d1479c2](https://raw.githubusercontent.com/openai/openai-node/main/d1479c2))
* **internal:** version bump ([#1393](https://github.com/openai/openai-node/issues/1393)) ([7f16c3a](https://raw.githubusercontent.com/openai/openai-node/main/7f16c3a))

## 4.87.4 (2025-03-18)

Full Changelog: [v4.87.3...v4.87.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.87.3...v4.87.4)

### Bug Fixes

* **api:** correct some Responses types ([#1391](https://github.com/openai/openai-node/issues/1391)) ([af45876](https://raw.githubusercontent.com/openai/openai-node/main/af45876))
* **types:** ignore missing `id` in responses pagination ([1b9d20e](https://raw.githubusercontent.com/openai/openai-node/main/1b9d20e))
* **types:** improve responses type names ([#1392](https://github.com/openai/openai-node/issues/1392)) ([164f476](https://raw.githubusercontent.com/openai/openai-node/main/164f476))

### Chores

* add missing type alias exports ([#1390](https://github.com/openai/openai-node/issues/1390)) ([16c5e22](https://raw.githubusercontent.com/openai/openai-node/main/16c5e22))
* **internal:** add back release workflow ([dddf29b](https://raw.githubusercontent.com/openai/openai-node/main/dddf29b))
* **internal:** remove CI condition ([#1381](https://github.com/openai/openai-node/issues/1381)) ([ef17981](https://raw.githubusercontent.com/openai/openai-node/main/ef17981))
* **internal:** run CI on update-specs branch ([9fc2130](https://raw.githubusercontent.com/openai/openai-node/main/9fc2130))
* **internal:** update release workflows ([90b77d0](https://raw.githubusercontent.com/openai/openai-node/main/90b77d0))

## 4.87.3 (2025-03-11)

Full Changelog: [v4.87.2...v4.87.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.87.2...v4.87.3)

### Bug Fixes

* **responses:** correct reasoning output type ([2abef57](https://raw.githubusercontent.com/openai/openai-node/main/2abef57))

## 4.87.2 (2025-03-11)

Full Changelog: [v4.87.1...v4.87.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.87.1...v4.87.2)

### Bug Fixes

* **responses:** correctly add output_text ([4ceb5cc](https://raw.githubusercontent.com/openai/openai-node/main/4ceb5cc))

## 4.87.1 (2025-03-11)

Full Changelog: [v4.87.0...v4.87.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.87.0...v4.87.1)

### Bug Fixes

* correct imports ([5cdf17c](https://raw.githubusercontent.com/openai/openai-node/main/5cdf17c))

## 4.87.0 (2025-03-11)

Full Changelog: [v4.86.2...v4.87.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.86.2...v4.87.0)

### Features

* **api:** add /v1/responses and built-in tools ([119b584](https://raw.githubusercontent.com/openai/openai-node/main/119b584))

## 4.86.2 (2025-03-05)

Full Changelog: [v4.86.1...v4.86.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.86.1...v4.86.2)

### Chores

* **internal:** run example files in CI ([#1357](https://github.com/openai/openai-node/issues/1357)) ([88d0050](https://raw.githubusercontent.com/openai/openai-node/main/88d0050))

## 4.86.1 (2025-02-27)

Full Changelog: [v4.86.0...v4.86.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.86.0...v4.86.1)

### Documentation

* update URLs from stainlessapi.com to stainless.com ([#1352](https://github.com/openai/openai-node/issues/1352)) ([8294e9e](https://raw.githubusercontent.com/openai/openai-node/main/8294e9e))

## 4.86.0 (2025-02-27)

Full Changelog: [v4.85.4...v4.86.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.85.4...v4.86.0)

### Features

* **api:** add gpt-4.5-preview ([#1349](https://github.com/openai/openai-node/issues/1349)) ([2a1d36b](https://raw.githubusercontent.com/openai/openai-node/main/2a1d36b))

## 4.85.4 (2025-02-22)

Full Changelog: [v4.85.3...v4.85.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.85.3...v4.85.4)

### Chores

* **internal:** fix devcontainers setup ([#1343](https://github.com/openai/openai-node/issues/1343)) ([cb1ec90](https://raw.githubusercontent.com/openai/openai-node/main/cb1ec90))

## 4.85.3 (2025-02-20)

Full Changelog: [v4.85.2...v4.85.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.85.2...v4.85.3)

### Bug Fixes

* **parsing:** remove tool_calls default empty array ([#1341](https://github.com/openai/openai-node/issues/1341)) ([2672160](https://raw.githubusercontent.com/openai/openai-node/main/2672160))

## 4.85.2 (2025-02-18)

Full Changelog: [v4.85.1...v4.85.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.85.1...v4.85.2)

### Bug Fixes

* optimize sse chunk reading off-by-one error ([#1339](https://github.com/openai/openai-node/issues/1339)) ([c82795b](https://raw.githubusercontent.com/openai/openai-node/main/c82795b))

## 4.85.1 (2025-02-14)

Full Changelog: [v4.85.0...v4.85.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.85.0...v4.85.1)

### Bug Fixes

* **client:** fix export map for index exports ([#1328](https://github.com/openai/openai-node/issues/1328)) ([647ba7a](https://raw.githubusercontent.com/openai/openai-node/main/647ba7a))
* **package:** add chat/completions.ts back in ([#1333](https://github.com/openai/openai-node/issues/1333)) ([e4b5546](https://raw.githubusercontent.com/openai/openai-node/main/e4b5546))

### Chores

* **internal:** add missing return type annotation ([#1334](https://github.com/openai/openai-node/issues/1334)) ([53e0856](https://raw.githubusercontent.com/openai/openai-node/main/53e0856))

## 4.85.0 (2025-02-13)

Full Changelog: [v4.84.1...v4.85.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.84.1...v4.85.0)

### Features

* **api:** add support for storing chat completions ([#1327](https://github.com/openai/openai-node/issues/1327)) ([8d77f8e](https://raw.githubusercontent.com/openai/openai-node/main/8d77f8e))

### Bug Fixes

* **realtime:** call .toString() on WebSocket url ([#1324](https://github.com/openai/openai-node/issues/1324)) ([09bc50d](https://raw.githubusercontent.com/openai/openai-node/main/09bc50d))

## 4.84.1 (2025-02-13)

Full Changelog: [v4.84.0...v4.84.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.84.0...v4.84.1)

### Bug Fixes

* **realtime:** correct websocket type var constraint ([#1321](https://github.com/openai/openai-node/issues/1321)) ([afb17ea](https://raw.githubusercontent.com/openai/openai-node/main/afb17ea))

## 4.84.0 (2025-02-12)

Full Changelog: [v4.83.0...v4.84.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.83.0...v4.84.0)

### Features

* **pagination:** avoid fetching when has_more: false ([#1305](https://github.com/openai/openai-node/issues/1305)) ([b6944c6](https://raw.githubusercontent.com/openai/openai-node/main/b6944c6))

### Bug Fixes

* **api:** add missing reasoning effort + model enums ([#1302](https://github.com/openai/openai-node/issues/1302)) ([14c55c3](https://raw.githubusercontent.com/openai/openai-node/main/14c55c3))
* **assistants:** handle `thread.run.incomplete` event ([7032cc4](https://raw.githubusercontent.com/openai/openai-node/main/7032cc4))
* correctly decode multi-byte characters over multiple chunks ([#1316](https://github.com/openai/openai-node/issues/1316)) ([dd776c4](https://raw.githubusercontent.com/openai/openai-node/main/dd776c4))

### Chores

* **internal:** remove segfault-handler dependency ([3521ca3](https://raw.githubusercontent.com/openai/openai-node/main/3521ca3))

### Documentation

* **readme:** cleanup into multiple files ([da94424](https://raw.githubusercontent.com/openai/openai-node/main/da94424))

## 4.83.0 (2025-02-05)

Full Changelog: [v4.82.0...v4.83.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.82.0...v4.83.0)

### Features

* **client:** send `X-Stainless-Timeout` header ([#1299](https://github.com/openai/openai-node/issues/1299)) ([ddfc686](https://raw.githubusercontent.com/openai/openai-node/main/ddfc686))

### Bug Fixes

* **api/types:** correct audio duration & role types ([#1300](https://github.com/openai/openai-node/issues/1300)) ([a955ac2](https://raw.githubusercontent.com/openai/openai-node/main/a955ac2))
* **azure/audio:** use model param for deployments ([#1297](https://github.com/openai/openai-node/issues/1297)) ([85de382](https://raw.githubusercontent.com/openai/openai-node/main/85de382))

## 4.82.0 (2025-01-31)

Full Changelog: [v4.81.0...v4.82.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.81.0...v4.82.0)

### Features

* **api:** add o3-mini ([#1295](https://github.com/openai/openai-node/issues/1295)) ([378e2f7](https://raw.githubusercontent.com/openai/openai-node/main/378e2f7))

### Bug Fixes

* **examples/realtime:** remove duplicate `session.update` call ([#1293](https://github.com/openai/openai-node/issues/1293)) ([ad800b4](https://raw.githubusercontent.com/openai/openai-node/main/ad800b4))
* **types:** correct metadata type + other fixes ([378e2f7](https://raw.githubusercontent.com/openai/openai-node/main/378e2f7))

## 4.81.0 (2025-01-29)

Full Changelog: [v4.80.1...v4.81.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.80.1...v4.81.0)

### Features

* **azure:** Realtime API support ([#1287](https://github.com/openai/openai-node/issues/1287)) ([fe090c0](https://raw.githubusercontent.com/openai/openai-node/main/fe090c0))

## 4.80.1 (2025-01-24)

Full Changelog: [v4.80.0...v4.80.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.80.0...v4.80.1)

### Bug Fixes

* **azure:** include retry count header ([3e0ba40](https://raw.githubusercontent.com/openai/openai-node/main/3e0ba40))

### Documentation

* fix typo, "zodFunctionTool" -&gt; "zodFunction" ([#1128](https://github.com/openai/openai-node/issues/1128)) ([b7ab6bb](https://raw.githubusercontent.com/openai/openai-node/main/b7ab6bb))
* **helpers:** fix type annotation ([fc019df](https://raw.githubusercontent.com/openai/openai-node/main/fc019df))
* **readme:** fix realtime errors docs link ([#1286](https://github.com/openai/openai-node/issues/1286)) ([d1d50c8](https://raw.githubusercontent.com/openai/openai-node/main/d1d50c8))

## 4.80.0 (2025-01-22)

Full Changelog: [v4.79.4...v4.80.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.79.4...v4.80.0)

### Features

* **api:** update enum values, comments, and examples ([#1280](https://github.com/openai/openai-node/issues/1280)) ([d38f2c2](https://raw.githubusercontent.com/openai/openai-node/main/d38f2c2))

## 4.79.4 (2025-01-21)

Full Changelog: [v4.79.3...v4.79.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.79.3...v4.79.4)

### Bug Fixes

* **jsr:** correct zod config ([e45fa5f](https://raw.githubusercontent.com/openai/openai-node/main/e45fa5f))

### Chores

* **internal:** minor restructuring ([#1278](https://github.com/openai/openai-node/issues/1278)) ([58ea92a](https://raw.githubusercontent.com/openai/openai-node/main/58ea92a))

### Documentation

* update deprecation messages ([#1275](https://github.com/openai/openai-node/issues/1275)) ([1c6599e](https://raw.githubusercontent.com/openai/openai-node/main/1c6599e))

## 4.79.3 (2025-01-21)

Full Changelog: [v4.79.2...v4.79.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.79.2...v4.79.3)

### Bug Fixes

* **jsr:** export zod helpers ([9dc55b6](https://raw.githubusercontent.com/openai/openai-node/main/9dc55b6))

## 4.79.2 (2025-01-21)

Full Changelog: [v4.79.1...v4.79.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.79.1...v4.79.2)

### Chores

* **internal:** add test ([#1270](https://github.com/openai/openai-node/issues/1270)) ([b7c2d3d](https://raw.githubusercontent.com/openai/openai-node/main/b7c2d3d))

### Documentation

* **readme:** fix Realtime API example link ([#1272](https://github.com/openai/openai-node/issues/1272)) ([d0653c7](https://raw.githubusercontent.com/openai/openai-node/main/d0653c7))

## 4.79.1 (2025-01-17)

Full Changelog: [v4.79.0...v4.79.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.79.0...v4.79.1)

### Bug Fixes

* **realtime:** correct import syntax ([#1267](https://github.com/openai/openai-node/issues/1267)) ([74702a7](https://raw.githubusercontent.com/openai/openai-node/main/74702a7))

## 4.79.0 (2025-01-17)

Full Changelog: [v4.78.1...v4.79.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.78.1...v4.79.0)

### Features

* **client:** add Realtime API support ([#1266](https://github.com/openai/openai-node/issues/1266)) ([7160ebe](https://raw.githubusercontent.com/openai/openai-node/main/7160ebe))

### Bug Fixes

* **logs/azure:** redact sensitive header when DEBUG is set ([#1218](https://github.com/openai/openai-node/issues/1218)) ([6a72fd7](https://raw.githubusercontent.com/openai/openai-node/main/6a72fd7))

### Chores

* fix streaming ([379c743](https://raw.githubusercontent.com/openai/openai-node/main/379c743))
* **internal:** streaming refactors ([#1261](https://github.com/openai/openai-node/issues/1261)) ([dd4af93](https://raw.githubusercontent.com/openai/openai-node/main/dd4af93))
* **types:** add `| undefined` to client options properties ([#1264](https://github.com/openai/openai-node/issues/1264)) ([5e56979](https://raw.githubusercontent.com/openai/openai-node/main/5e56979))
* **types:** rename vector store chunking strategy ([#1263](https://github.com/openai/openai-node/issues/1263)) ([d31acee](https://raw.githubusercontent.com/openai/openai-node/main/d31acee))

## 4.78.1 (2025-01-10)

Full Changelog: [v4.78.0...v4.78.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.78.0...v4.78.1)

### Bug Fixes

* send correct Accept header for certain endpoints ([#1257](https://github.com/openai/openai-node/issues/1257)) ([8756693](https://raw.githubusercontent.com/openai/openai-node/main/8756693))

## 4.78.0 (2025-01-09)

Full Changelog: [v4.77.4...v4.78.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.77.4...v4.78.0)

### Features

* **client:** add realtime types ([#1254](https://github.com/openai/openai-node/issues/1254)) ([7130995](https://raw.githubusercontent.com/openai/openai-node/main/7130995))

## 4.77.4 (2025-01-08)

Full Changelog: [v4.77.3...v4.77.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.77.3...v4.77.4)

### Documentation

* **readme:** fix misplaced period ([#1252](https://github.com/openai/openai-node/issues/1252)) ([c2fe465](https://raw.githubusercontent.com/openai/openai-node/main/c2fe465))

## 4.77.3 (2025-01-03)

Full Changelog: [v4.77.2...v4.77.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.77.2...v4.77.3)

### Chores

* **api:** bump spec version ([#1248](https://github.com/openai/openai-node/issues/1248)) ([37b3df9](https://raw.githubusercontent.com/openai/openai-node/main/37b3df9))

## 4.77.2 (2025-01-02)

Full Changelog: [v4.77.1...v4.77.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.77.1...v4.77.2)

### Chores

* bump license year ([#1246](https://github.com/openai/openai-node/issues/1246)) ([13197c1](https://raw.githubusercontent.com/openai/openai-node/main/13197c1))

## 4.77.1 (2024-12-21)

Full Changelog: [v4.77.0...v4.77.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.77.0...v4.77.1)

### Bug Fixes

* **client:** normalize method ([#1235](https://github.com/openai/openai-node/issues/1235)) ([4a213da](https://raw.githubusercontent.com/openai/openai-node/main/4a213da))

### Chores

* **internal:** spec update ([#1231](https://github.com/openai/openai-node/issues/1231)) ([a97ea73](https://raw.githubusercontent.com/openai/openai-node/main/a97ea73))

### Documentation

* minor formatting changes ([#1236](https://github.com/openai/openai-node/issues/1236)) ([6387968](https://raw.githubusercontent.com/openai/openai-node/main/6387968))
* **readme:** add alpha callout ([f2eff37](https://raw.githubusercontent.com/openai/openai-node/main/f2eff37))

## 4.77.0 (2024-12-17)

Full Changelog: [v4.76.3...v4.77.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.76.3...v4.77.0)

### Features

* **api:** new o1 and GPT-4o models + preference fine-tuning ([#1229](https://github.com/openai/openai-node/issues/1229)) ([2e872d4](https://raw.githubusercontent.com/openai/openai-node/main/2e872d4))

### Chores

* **internal:** fix some typos ([#1227](https://github.com/openai/openai-node/issues/1227)) ([d51fcfe](https://raw.githubusercontent.com/openai/openai-node/main/d51fcfe))
* **internal:** spec update ([#1230](https://github.com/openai/openai-node/issues/1230)) ([ed2b61d](https://raw.githubusercontent.com/openai/openai-node/main/ed2b61d))

## 4.76.3 (2024-12-13)

Full Changelog: [v4.76.2...v4.76.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.76.2...v4.76.3)

### Chores

* **internal:** better ecosystem test debugging ([86fc0a8](https://raw.githubusercontent.com/openai/openai-node/main/86fc0a8))

### Documentation

* **README:** fix helpers section links ([#1224](https://github.com/openai/openai-node/issues/1224)) ([efbe30a](https://raw.githubusercontent.com/openai/openai-node/main/efbe30a))

## 4.76.2 (2024-12-12)

Full Changelog: [v4.76.1...v4.76.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.76.1...v4.76.2)

### Chores

* **internal:** update isAbsoluteURL ([#1223](https://github.com/openai/openai-node/issues/1223)) ([e908ed7](https://raw.githubusercontent.com/openai/openai-node/main/e908ed7))
* **types:** nicer error class types + jsdocs ([#1219](https://github.com/openai/openai-node/issues/1219)) ([576d24c](https://raw.githubusercontent.com/openai/openai-node/main/576d24c))

## 4.76.1 (2024-12-10)

Full Changelog: [v4.76.0...v4.76.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.76.0...v4.76.1)

### Chores

* **internal:** bump cross-spawn to v7.0.6 ([#1217](https://github.com/openai/openai-node/issues/1217)) ([c07ad29](https://raw.githubusercontent.com/openai/openai-node/main/c07ad29))
* **internal:** remove unnecessary getRequestClient function ([#1215](https://github.com/openai/openai-node/issues/1215)) ([bef3925](https://raw.githubusercontent.com/openai/openai-node/main/bef3925))

## 4.76.0 (2024-12-05)

Full Changelog: [v4.75.0...v4.76.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.75.0...v4.76.0)

### Features

* **api:** updates ([#1212](https://github.com/openai/openai-node/issues/1212)) ([e0fedf2](https://raw.githubusercontent.com/openai/openai-node/main/e0fedf2))

### Chores

* bump openapi url ([#1210](https://github.com/openai/openai-node/issues/1210)) ([3fa95a4](https://raw.githubusercontent.com/openai/openai-node/main/3fa95a4))

## 4.75.0 (2024-12-03)

Full Changelog: [v4.74.0...v4.75.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.74.0...v4.75.0)

### Features

* improve docs for jsr README.md ([#1208](https://github.com/openai/openai-node/issues/1208)) ([338527e](https://raw.githubusercontent.com/openai/openai-node/main/338527e))

## 4.74.0 (2024-12-02)

Full Changelog: [v4.73.1...v4.74.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.73.1...v4.74.0)

### Features

* **internal:** make git install file structure match npm ([#1204](https://github.com/openai/openai-node/issues/1204)) ([e7c4c6d](https://raw.githubusercontent.com/openai/openai-node/main/e7c4c6d))

## 4.73.1 (2024-11-25)

Full Changelog: [v4.73.0...v4.73.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.73.0...v4.73.1)

### Documentation

* **readme:** mention `.withResponse()` for streaming request ID ([#1202](https://github.com/openai/openai-node/issues/1202)) ([b6800d4](https://raw.githubusercontent.com/openai/openai-node/main/b6800d4))

## 4.73.0 (2024-11-20)

Full Changelog: [v4.72.0...v4.73.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.72.0...v4.73.0)

### Features

* **api:** add gpt-4o-2024-11-20 model ([#1201](https://github.com/openai/openai-node/issues/1201)) ([0feeafd](https://raw.githubusercontent.com/openai/openai-node/main/0feeafd))
* bump model in all example snippets to gpt-4o ([6961c37](https://raw.githubusercontent.com/openai/openai-node/main/6961c37))

### Bug Fixes

* **docs:** add missing await to pagination example ([#1190](https://github.com/openai/openai-node/issues/1190)) ([524b9e8](https://raw.githubusercontent.com/openai/openai-node/main/524b9e8))

### Chores

* **client:** drop unused devDependency ([#1191](https://github.com/openai/openai-node/issues/1191)) ([8ee6c03](https://raw.githubusercontent.com/openai/openai-node/main/8ee6c03))
* **internal:** spec update ([#1195](https://github.com/openai/openai-node/issues/1195)) ([12f9334](https://raw.githubusercontent.com/openai/openai-node/main/12f9334))
* **internal:** use reexports not destructuring ([#1181](https://github.com/openai/openai-node/issues/1181)) ([f555dd6](https://raw.githubusercontent.com/openai/openai-node/main/f555dd6))

### Documentation

* bump models in example snippets to gpt-4o ([#1184](https://github.com/openai/openai-node/issues/1184)) ([4ec4027](https://raw.githubusercontent.com/openai/openai-node/main/4ec4027))
* change readme title ([#1198](https://github.com/openai/openai-node/issues/1198)) ([e34981c](https://raw.githubusercontent.com/openai/openai-node/main/e34981c))
* improve jsr documentation ([#1197](https://github.com/openai/openai-node/issues/1197)) ([ebdb4f7](https://raw.githubusercontent.com/openai/openai-node/main/ebdb4f7))
* **readme:** fix incorrect fileBatches.uploadAndPoll params ([#1200](https://github.com/openai/openai-node/issues/1200)) ([3968ef1](https://raw.githubusercontent.com/openai/openai-node/main/3968ef1))

## 4.72.0 (2024-11-12)

Full Changelog: [v4.71.1...v4.72.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.71.1...v4.72.0)

### Features

* add back deno runtime testing without type checks ([1626cf5](https://raw.githubusercontent.com/openai/openai-node/main/1626cf5))

### Chores

* **ecosystem-tests:** bump wrangler version ([#1178](https://github.com/openai/openai-node/issues/1178)) ([4dfb0c6](https://raw.githubusercontent.com/openai/openai-node/main/4dfb0c6))

## 4.71.1 (2024-11-06)

Full Changelog: [v4.71.0...v4.71.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.71.0...v4.71.1)

### Bug Fixes

* change release please configuration for jsr.json ([#1174](https://github.com/openai/openai-node/issues/1174)) ([c39efba](https://raw.githubusercontent.com/openai/openai-node/main/c39efba))

## 4.71.0 (2024-11-04)

Full Changelog: [v4.70.3...v4.71.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.70.3...v4.71.0)

### Features

* **api:** add support for predicted outputs ([#1172](https://github.com/openai/openai-node/issues/1172)) ([08a7bb4](https://raw.githubusercontent.com/openai/openai-node/main/08a7bb4))

## 4.70.3 (2024-11-04)

Full Changelog: [v4.70.2...v4.70.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.70.2...v4.70.3)

### Bug Fixes

* change streaming helper imports to be relative ([e73b7cf](https://raw.githubusercontent.com/openai/openai-node/main/e73b7cf))

## 4.70.2 (2024-11-01)

Full Changelog: [v4.70.1...v4.70.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.70.1...v4.70.2)

### Bug Fixes

* add permissions to github workflow ([ee75e00](https://raw.githubusercontent.com/openai/openai-node/main/ee75e00))
* skip deno ecosystem test ([5b181b0](https://raw.githubusercontent.com/openai/openai-node/main/5b181b0))

## 4.70.1 (2024-11-01)

Full Changelog: [v4.70.0...v4.70.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.70.0...v4.70.1)

### Bug Fixes

* don't require deno to run build-deno ([#1167](https://github.com/openai/openai-node/issues/1167)) ([9d857bc](https://raw.githubusercontent.com/openai/openai-node/main/9d857bc))

## 4.70.0 (2024-11-01)

Full Changelog: [v4.69.0...v4.70.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.69.0...v4.70.0)

### Features

* publish to jsr ([#1165](https://github.com/openai/openai-node/issues/1165)) ([5aa93a7](https://raw.githubusercontent.com/openai/openai-node/main/5aa93a7))

### Chores

* **internal:** fix isolated modules exports ([9cd1958](https://raw.githubusercontent.com/openai/openai-node/main/9cd1958))

### Refactors

* use type imports for type-only imports ([#1159](https://github.com/openai/openai-node/issues/1159)) ([07bbaf6](https://raw.githubusercontent.com/openai/openai-node/main/07bbaf6))

## 4.69.0 (2024-10-30)

Full Changelog: [v4.68.4...v4.69.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.68.4...v4.69.0)

### Features

* **api:** add new, expressive voices for Realtime and Audio in Chat Completions ([#1157](https://github.com/openai/openai-node/issues/1157)) ([12e501c](https://raw.githubusercontent.com/openai/openai-node/main/12e501c))

### Bug Fixes

* **internal:** support pnpm git installs ([#1156](https://github.com/openai/openai-node/issues/1156)) ([b744c5b](https://raw.githubusercontent.com/openai/openai-node/main/b744c5b))

### Documentation

* **readme:** minor typo fixes ([#1154](https://github.com/openai/openai-node/issues/1154)) ([c6c9f9a](https://raw.githubusercontent.com/openai/openai-node/main/c6c9f9a))

## 4.68.4 (2024-10-23)

Full Changelog: [v4.68.3...v4.68.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.68.3...v4.68.4)

### Chores

* **internal:** update spec version ([#1146](https://github.com/openai/openai-node/issues/1146)) ([0165a8d](https://raw.githubusercontent.com/openai/openai-node/main/0165a8d))

## 4.68.3 (2024-10-23)

Full Changelog: [v4.68.2...v4.68.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.68.2...v4.68.3)

### Chores

* **internal:** bumps eslint and related dependencies ([#1143](https://github.com/openai/openai-node/issues/1143)) ([2643f42](https://raw.githubusercontent.com/openai/openai-node/main/2643f42))

## 4.68.2 (2024-10-22)

Full Changelog: [v4.68.1...v4.68.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.68.1...v4.68.2)

### Chores

* **internal:** update spec version ([#1141](https://github.com/openai/openai-node/issues/1141)) ([2ccb3e3](https://raw.githubusercontent.com/openai/openai-node/main/2ccb3e3))

## 4.68.1 (2024-10-18)

Full Changelog: [v4.68.0...v4.68.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.68.0...v4.68.1)

### Bug Fixes

* **client:** respect x-stainless-retry-count default headers ([#1138](https://github.com/openai/openai-node/issues/1138)) ([266717b](https://raw.githubusercontent.com/openai/openai-node/main/266717b))

## 4.68.0 (2024-10-17)

Full Changelog: [v4.67.3...v4.68.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.67.3...v4.68.0)

### Features

* **api:** add gpt-4o-audio-preview model for chat completions ([#1135](https://github.com/openai/openai-node/issues/1135)) ([17a623f](https://raw.githubusercontent.com/openai/openai-node/main/17a623f))

## 4.67.3 (2024-10-08)

Full Changelog: [v4.67.2...v4.67.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.67.2...v4.67.3)

### Chores

* **internal:** pass props through internal parser ([#1125](https://github.com/openai/openai-node/issues/1125)) ([5ef8aa8](https://raw.githubusercontent.com/openai/openai-node/main/5ef8aa8))

## 4.67.2 (2024-10-07)

Full Changelog: [v4.67.1...v4.67.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.67.1...v4.67.2)

### Chores

* **internal:** move LineDecoder to a separate file ([#1120](https://github.com/openai/openai-node/issues/1120)) ([0a4be65](https://raw.githubusercontent.com/openai/openai-node/main/0a4be65))

## 4.67.1 (2024-10-02)

Full Changelog: [v4.67.0...v4.67.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.67.0...v4.67.1)

### Documentation

* improve and reference contributing documentation ([#1115](https://github.com/openai/openai-node/issues/1115)) ([7fa30b3](https://raw.githubusercontent.com/openai/openai-node/main/7fa30b3))

## 4.67.0 (2024-10-01)

Full Changelog: [v4.66.1...v4.67.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.66.1...v4.67.0)

### Features

* **api:** support storing chat completions, enabling evals and model distillation in the dashboard ([#1112](https://github.com/openai/openai-node/issues/1112)) ([6424924](https://raw.githubusercontent.com/openai/openai-node/main/6424924))

## 4.66.1 (2024-09-30)

Full Changelog: [v4.66.0...v4.66.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.66.0...v4.66.1)

### Bug Fixes

* **audio:** add fallback overload types ([0c00a13](https://raw.githubusercontent.com/openai/openai-node/main/0c00a13))
* **audio:** use export type ([1519100](https://raw.githubusercontent.com/openai/openai-node/main/1519100))

## 4.66.0 (2024-09-27)

Full Changelog: [v4.65.0...v4.66.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.65.0...v4.66.0)

### Features

* **client:** add request_id to `.withResponse()` ([#1095](https://github.com/openai/openai-node/issues/1095)) ([2d0f565](https://raw.githubusercontent.com/openai/openai-node/main/2d0f565))

### Bug Fixes

* **audio:** correct types for transcriptions / translations ([#1104](https://github.com/openai/openai-node/issues/1104)) ([96e86c2](https://raw.githubusercontent.com/openai/openai-node/main/96e86c2))
* **client:** correct types for transcriptions / translations ([#1105](https://github.com/openai/openai-node/issues/1105)) ([fa16ebb](https://raw.githubusercontent.com/openai/openai-node/main/fa16ebb))

## 4.65.0 (2024-09-26)

Full Changelog: [v4.64.0...v4.65.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.64.0...v4.65.0)

### Features

* **api:** add omni-moderation model ([#1100](https://github.com/openai/openai-node/issues/1100)) ([66c0f21](https://raw.githubusercontent.com/openai/openai-node/main/66c0f21))

## 4.64.0 (2024-09-25)

Full Changelog: [v4.63.0...v4.64.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.63.0...v4.64.0)

### Features

* **client:** allow overriding retry count header ([#1098](https://github.com/openai/openai-node/issues/1098)) ([a466ff7](https://raw.githubusercontent.com/openai/openai-node/main/a466ff7))

### Bug Fixes

* **audio:** correct response_format translations type ([#1097](https://github.com/openai/openai-node/issues/1097)) ([9a5f461](https://raw.githubusercontent.com/openai/openai-node/main/9a5f461))

### Chores

* **internal:** fix ecosystem tests error output ([#1096](https://github.com/openai/openai-node/issues/1096)) ([ecdb4e9](https://raw.githubusercontent.com/openai/openai-node/main/ecdb4e9))
* **internal:** fix slow ecosystem test ([#1093](https://github.com/openai/openai-node/issues/1093)) ([80ed9ec](https://raw.githubusercontent.com/openai/openai-node/main/80ed9ec))

## 4.63.0 (2024-09-20)

Full Changelog: [v4.62.1...v4.63.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.62.1...v4.63.0)

### Features

* **client:** send retry count header ([#1087](https://github.com/openai/openai-node/issues/1087)) ([7bcebc0](https://raw.githubusercontent.com/openai/openai-node/main/7bcebc0))

### Chores

* **types:** improve type name for embedding models ([#1089](https://github.com/openai/openai-node/issues/1089)) ([d6966d9](https://raw.githubusercontent.com/openai/openai-node/main/d6966d9))

## 4.62.1 (2024-09-18)

Full Changelog: [v4.62.0...v4.62.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.62.0...v4.62.1)

### Bug Fixes

* **types:** remove leftover polyfill usage ([#1084](https://github.com/openai/openai-node/issues/1084)) ([b7c9538](https://raw.githubusercontent.com/openai/openai-node/main/b7c9538))

## 4.62.0 (2024-09-17)

Full Changelog: [v4.61.1...v4.62.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.61.1...v4.62.0)

### Features

* **client:** add ._request_id property to object responses ([#1078](https://github.com/openai/openai-node/issues/1078)) ([d5c2131](https://raw.githubusercontent.com/openai/openai-node/main/d5c2131))

### Chores

* **internal:** add ecosystem test for qs reproduction ([0199dd8](https://raw.githubusercontent.com/openai/openai-node/main/0199dd8))
* **internal:** add query string encoder ([#1079](https://github.com/openai/openai-node/issues/1079)) ([f870682](https://raw.githubusercontent.com/openai/openai-node/main/f870682))
* **internal:** fix some types ([#1082](https://github.com/openai/openai-node/issues/1082)) ([1ec41a7](https://raw.githubusercontent.com/openai/openai-node/main/1ec41a7))
* **tests:** add query string tests to ecosystem tests ([36be724](https://raw.githubusercontent.com/openai/openai-node/main/36be724))

## 4.61.1 (2024-09-16)

Full Changelog: [v4.61.0...v4.61.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.61.0...v4.61.1)

### Bug Fixes

* **runTools:** correct request options type ([#1073](https://github.com/openai/openai-node/issues/1073)) ([399f971](https://raw.githubusercontent.com/openai/openai-node/main/399f971))

### Chores

* **internal:** update spec link ([#1076](https://github.com/openai/openai-node/issues/1076)) ([20f1bcc](https://raw.githubusercontent.com/openai/openai-node/main/20f1bcc))

## 4.61.0 (2024-09-13)

Full Changelog: [v4.60.1...v4.61.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.60.1...v4.61.0)

### Bug Fixes

* **client:** partial parsing update to handle strings ([46e8eb6](https://raw.githubusercontent.com/openai/openai-node/main/46e8eb6))
* **examples:** handle usage chunk in tool call streaming ([#1068](https://github.com/openai/openai-node/issues/1068)) ([e4188c4](https://raw.githubusercontent.com/openai/openai-node/main/e4188c4))

### Chores

* **examples:** add a small delay to tool-calls example streaming ([a3fc659](https://raw.githubusercontent.com/openai/openai-node/main/a3fc659))

### Documentation

* update CONTRIBUTING.md ([#1071](https://github.com/openai/openai-node/issues/1071)) ([5de81c9](https://raw.githubusercontent.com/openai/openai-node/main/5de81c9))

## 4.60.1 (2024-09-13)

Full Changelog: [v4.60.0...v4.60.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.60.0...v4.60.1)

### Bug Fixes

* **zod:** correctly add $ref definitions for transformed schemas ([#1065](https://github.com/openai/openai-node/issues/1065)) ([9b93b24](https://raw.githubusercontent.com/openai/openai-node/main/9b93b24))

## 4.60.0 (2024-09-12)

Full Changelog: [v4.59.0...v4.60.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.59.0...v4.60.0)

### Features

* **api:** add o1 models ([#1061](https://github.com/openai/openai-node/issues/1061)) ([224cc04](https://raw.githubusercontent.com/openai/openai-node/main/224cc04))

## 4.59.0 (2024-09-11)

Full Changelog: [v4.58.2...v4.59.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.58.2...v4.59.0)

### Features

* **structured outputs:** support accessing raw responses ([#1058](https://github.com/openai/openai-node/issues/1058)) ([af17697](https://raw.githubusercontent.com/openai/openai-node/main/af17697))

### Documentation

* **azure:** example for custom base URL ([#1055](https://github.com/openai/openai-node/issues/1055)) ([20defc8](https://raw.githubusercontent.com/openai/openai-node/main/20defc8))
* **azure:** remove locale from docs link ([#1054](https://github.com/openai/openai-node/issues/1054)) ([f9b7eac](https://raw.githubusercontent.com/openai/openai-node/main/f9b7eac))

## 4.58.2 (2024-09-09)

Full Changelog: [v4.58.1...v4.58.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.58.1...v4.58.2)

### Bug Fixes

* **errors:** pass message through to APIConnectionError ([#1050](https://github.com/openai/openai-node/issues/1050)) ([5a34316](https://raw.githubusercontent.com/openai/openai-node/main/5a34316))

### Chores

* better object fallback behaviour for casting errors ([#1053](https://github.com/openai/openai-node/issues/1053)) ([b7d4619](https://raw.githubusercontent.com/openai/openai-node/main/b7d4619))

## 4.58.1 (2024-09-06)

Full Changelog: [v4.58.0...v4.58.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.58.0...v4.58.1)

### Chores

* **docs:** update browser support information ([#1045](https://github.com/openai/openai-node/issues/1045)) ([d326cc5](https://raw.githubusercontent.com/openai/openai-node/main/d326cc5))

## 4.58.0 (2024-09-05)

Full Changelog: [v4.57.3...v4.58.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.57.3...v4.58.0)

### Features

* **vector store:** improve chunking strategy type names ([#1041](https://github.com/openai/openai-node/issues/1041)) ([471cec3](https://raw.githubusercontent.com/openai/openai-node/main/471cec3))

### Bug Fixes

* **uploads:** avoid making redundant memory copies ([#1043](https://github.com/openai/openai-node/issues/1043)) ([271297b](https://raw.githubusercontent.com/openai/openai-node/main/271297b))

## 4.57.3 (2024-09-04)

Full Changelog: [v4.57.2...v4.57.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.57.2...v4.57.3)

### Bug Fixes

* **helpers/zod:** avoid import issue in certain environments ([#1039](https://github.com/openai/openai-node/issues/1039)) ([e238daa](https://raw.githubusercontent.com/openai/openai-node/main/e238daa))

### Chores

* **internal:** minor bump qs version ([#1037](https://github.com/openai/openai-node/issues/1037)) ([8ec218e](https://raw.githubusercontent.com/openai/openai-node/main/8ec218e))

## 4.57.2 (2024-09-04)

Full Changelog: [v4.57.1...v4.57.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.57.1...v4.57.2)

### Chores

* **internal:** dependency updates ([#1035](https://github.com/openai/openai-node/issues/1035)) ([e815fb6](https://raw.githubusercontent.com/openai/openai-node/main/e815fb6))

## 4.57.1 (2024-09-03)

Full Changelog: [v4.57.0...v4.57.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.57.0...v4.57.1)

### Bug Fixes

* **assistants:** correctly accumulate tool calls when streaming ([#1031](https://github.com/openai/openai-node/issues/1031)) ([d935ad3](https://raw.githubusercontent.com/openai/openai-node/main/d935ad3))
* **client:** correct File construction from node-fetch Responses ([#1029](https://github.com/openai/openai-node/issues/1029)) ([22ebdc2](https://raw.githubusercontent.com/openai/openai-node/main/22ebdc2))
* runTools without stream should not emit user message events ([#1005](https://github.com/openai/openai-node/issues/1005)) ([22ded4d](https://raw.githubusercontent.com/openai/openai-node/main/22ded4d))

### Chores

* **internal/tests:** workaround bug in recent types/node release ([3c7bdfd](https://raw.githubusercontent.com/openai/openai-node/main/3c7bdfd))

## 4.57.0 (2024-08-29)

Full Changelog: [v4.56.2...v4.57.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.56.2...v4.57.0)

### Features

* **api:** add file search result details to run steps ([#1023](https://github.com/openai/openai-node/issues/1023)) ([d9acd0a](https://raw.githubusercontent.com/openai/openai-node/main/d9acd0a))

### Bug Fixes

* install examples deps as part of bootstrap script ([#1022](https://github.com/openai/openai-node/issues/1022)) ([eae8e36](https://raw.githubusercontent.com/openai/openai-node/main/eae8e36))

## 4.56.2 (2024-08-29)

Full Changelog: [v4.56.1...v4.56.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.56.1...v4.56.2)

### Chores

* run tsc as part of lint script ([#1020](https://github.com/openai/openai-node/issues/1020)) ([4942347](https://raw.githubusercontent.com/openai/openai-node/main/4942347))

## 4.56.1 (2024-08-27)

Full Changelog: [v4.56.0...v4.56.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.56.0...v4.56.1)

### Chores

* **ci:** check for build errors ([#1013](https://github.com/openai/openai-node/issues/1013)) ([7ff2127](https://raw.githubusercontent.com/openai/openai-node/main/7ff2127))

## 4.56.0 (2024-08-16)

Full Changelog: [v4.55.9...v4.56.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.9...v4.56.0)

### Features

* **api:** add chatgpt-4o-latest model ([edc4398](https://raw.githubusercontent.com/openai/openai-node/main/edc4398))

## 4.55.9 (2024-08-16)

Full Changelog: [v4.55.8...v4.55.9](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.8...v4.55.9)

### Bug Fixes

* **azure/tts:** avoid stripping model param ([#999](https://github.com/openai/openai-node/issues/999)) ([c3a7ccd](https://raw.githubusercontent.com/openai/openai-node/main/c3a7ccd))

## 4.55.8 (2024-08-15)

Full Changelog: [v4.55.7...v4.55.8](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.7...v4.55.8)

### Chores

* **types:** define FilePurpose enum ([#997](https://github.com/openai/openai-node/issues/997)) ([19b941b](https://raw.githubusercontent.com/openai/openai-node/main/19b941b))

## 4.55.7 (2024-08-13)

Full Changelog: [v4.55.6...v4.55.7](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.6...v4.55.7)

### Bug Fixes

* **json-schema:** correct handling of nested recursive schemas ([#992](https://github.com/openai/openai-node/issues/992)) ([ac309ab](https://raw.githubusercontent.com/openai/openai-node/main/ac309ab))

## 4.55.6 (2024-08-13)

Full Changelog: [v4.55.5...v4.55.6](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.5...v4.55.6)

### Bug Fixes

* **zod-to-json-schema:** correct licensing ([#986](https://github.com/openai/openai-node/issues/986)) ([bd2051e](https://raw.githubusercontent.com/openai/openai-node/main/bd2051e))

## 4.55.5 (2024-08-12)

Full Changelog: [v4.55.4...v4.55.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.4...v4.55.5)

### Chores

* **examples:** minor formatting changes ([#987](https://github.com/openai/openai-node/issues/987)) ([8e6b615](https://raw.githubusercontent.com/openai/openai-node/main/8e6b615))
* sync openapi url ([#989](https://github.com/openai/openai-node/issues/989)) ([02ff1c5](https://raw.githubusercontent.com/openai/openai-node/main/02ff1c5))

## 4.55.4 (2024-08-09)

Full Changelog: [v4.55.3...v4.55.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.3...v4.55.4)

### Bug Fixes

* **helpers/zod:** nested union schema extraction ([#979](https://github.com/openai/openai-node/issues/979)) ([31b05aa](https://raw.githubusercontent.com/openai/openai-node/main/31b05aa))

### Chores

* **ci:** bump prism mock server version ([#982](https://github.com/openai/openai-node/issues/982)) ([7442643](https://raw.githubusercontent.com/openai/openai-node/main/7442643))
* **ci:** codeowners file ([#980](https://github.com/openai/openai-node/issues/980)) ([17a42b2](https://raw.githubusercontent.com/openai/openai-node/main/17a42b2))

## 4.55.3 (2024-08-08)

Full Changelog: [v4.55.2...v4.55.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.2...v4.55.3)

### Chores

* **internal:** updates ([#975](https://github.com/openai/openai-node/issues/975)) ([313a190](https://raw.githubusercontent.com/openai/openai-node/main/313a190))

## 4.55.2 (2024-08-08)

Full Changelog: [v4.55.1...v4.55.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.1...v4.55.2)

### Bug Fixes

* **helpers/zod:** add `extract-to-root` ref strategy ([ef3c73c](https://raw.githubusercontent.com/openai/openai-node/main/ef3c73c))
* **helpers/zod:** add `nullableStrategy` option ([ad89892](https://raw.githubusercontent.com/openai/openai-node/main/ad89892))
* **helpers/zod:** correct logic for adding root schema to definitions ([e4a247a](https://raw.githubusercontent.com/openai/openai-node/main/e4a247a))

### Chores

* **internal:** add README for vendored zod-to-json-schema ([d8a80a9](https://raw.githubusercontent.com/openai/openai-node/main/d8a80a9))
* **tests:** add more API request tests ([04c1590](https://raw.githubusercontent.com/openai/openai-node/main/04c1590))

## 4.55.1 (2024-08-07)

Full Changelog: [v4.55.0...v4.55.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.55.0...v4.55.1)

### Bug Fixes

* **helpers/zod:** correct schema generation for recursive schemas ([cb54d93](https://raw.githubusercontent.com/openai/openai-node/main/cb54d93))

### Chores

* **api:** remove old `AssistantResponseFormat` type ([#967](https://github.com/openai/openai-node/issues/967)) ([9fd94bf](https://raw.githubusercontent.com/openai/openai-node/main/9fd94bf))
* **internal:** update test snapshots ([bceea60](https://raw.githubusercontent.com/openai/openai-node/main/bceea60))
* **vendor/zodJsonSchema:** add option to duplicate top-level ref ([84b8a38](https://raw.githubusercontent.com/openai/openai-node/main/84b8a38))

### Documentation

* **examples:** add UI generation example script ([c75c017](https://raw.githubusercontent.com/openai/openai-node/main/c75c017))

## 4.55.0 (2024-08-06)

Full Changelog: [v4.54.0...v4.55.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.54.0...v4.55.0)

### Features

* **api:** add structured outputs support ([573787c](https://raw.githubusercontent.com/openai/openai-node/main/573787c))

## 4.54.0 (2024-08-02)

Full Changelog: [v4.53.2...v4.54.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.53.2...v4.54.0)

### Features

* extract out `ImageModel`, `AudioModel`, `SpeechModel` ([#964](https://github.com/openai/openai-node/issues/964)) ([1edf957](https://raw.githubusercontent.com/openai/openai-node/main/1edf957))
* make enums not nominal ([#965](https://github.com/openai/openai-node/issues/965)) ([0dd0cd1](https://raw.githubusercontent.com/openai/openai-node/main/0dd0cd1))

### Chores

* **ci:** correctly tag pre-release npm packages ([#963](https://github.com/openai/openai-node/issues/963)) ([f1a4a68](https://raw.githubusercontent.com/openai/openai-node/main/f1a4a68))
* **internal:** add constant for default timeout ([#960](https://github.com/openai/openai-node/issues/960)) ([55c01f4](https://raw.githubusercontent.com/openai/openai-node/main/55c01f4))
* **internal:** cleanup event stream helpers ([#950](https://github.com/openai/openai-node/issues/950)) ([8f49956](https://raw.githubusercontent.com/openai/openai-node/main/8f49956))

### Documentation

* **README:** link Lifecycle in Polling Helpers section ([#962](https://github.com/openai/openai-node/issues/962)) ([c610c81](https://raw.githubusercontent.com/openai/openai-node/main/c610c81))

## 4.53.2 (2024-07-26)

Full Changelog: [v4.53.1...v4.53.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.53.1...v4.53.2)

### Chores

* **docs:** fix incorrect client var names ([#955](https://github.com/openai/openai-node/issues/955)) ([cc91be8](https://raw.githubusercontent.com/openai/openai-node/main/cc91be8))

## 4.53.1 (2024-07-25)

Full Changelog: [v4.53.0...v4.53.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.53.0...v4.53.1)

### Bug Fixes

* **compat:** remove ReadableStream polyfill redundant since node v16 ([#954](https://github.com/openai/openai-node/issues/954)) ([78b2a83](https://raw.githubusercontent.com/openai/openai-node/main/78b2a83))

### Chores

* **tests:** update prism version ([#948](https://github.com/openai/openai-node/issues/948)) ([9202c91](https://raw.githubusercontent.com/openai/openai-node/main/9202c91))

## 4.53.0 (2024-07-22)

Full Changelog: [v4.52.7...v4.53.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.7...v4.53.0)

### Features

* **api:** add new gpt-4o-mini models ([#942](https://github.com/openai/openai-node/issues/942)) ([7ac10dd](https://raw.githubusercontent.com/openai/openai-node/main/7ac10dd))
* **api:** add uploads endpoints ([#946](https://github.com/openai/openai-node/issues/946)) ([8709ceb](https://raw.githubusercontent.com/openai/openai-node/main/8709ceb))

### Chores

* **docs:** mention support of web browser runtimes ([#938](https://github.com/openai/openai-node/issues/938)) ([123d19d](https://raw.githubusercontent.com/openai/openai-node/main/123d19d))
* **docs:** use client instead of package name in Node examples ([#941](https://github.com/openai/openai-node/issues/941)) ([8b5db1f](https://raw.githubusercontent.com/openai/openai-node/main/8b5db1f))

## 4.52.7 (2024-07-11)

Full Changelog: [v4.52.6...v4.52.7](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.6...v4.52.7)

### Documentation

* **examples:** update example values ([#933](https://github.com/openai/openai-node/issues/933)) ([92512ab](https://raw.githubusercontent.com/openai/openai-node/main/92512ab))

## 4.52.6 (2024-07-11)

Full Changelog: [v4.52.5...v4.52.6](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.5...v4.52.6)

### Chores

* **ci:** also run workflows for PRs targeting `next` ([#931](https://github.com/openai/openai-node/issues/931)) ([e3f979a](https://raw.githubusercontent.com/openai/openai-node/main/e3f979a))

## 4.52.5 (2024-07-10)

Full Changelog: [v4.52.4...v4.52.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.4...v4.52.5)

### Bug Fixes

* **vectorStores:** correctly handle missing `files` in `uploadAndPoll()` ([#926](https://github.com/openai/openai-node/issues/926)) ([945fca6](https://raw.githubusercontent.com/openai/openai-node/main/945fca6))

## 4.52.4 (2024-07-08)

Full Changelog: [v4.52.3...v4.52.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.3...v4.52.4)

### Refactors

* **examples:** removedduplicated 'messageDelta' streaming event. ([#909](https://github.com/openai/openai-node/issues/909)) ([7b0b3d2](https://raw.githubusercontent.com/openai/openai-node/main/7b0b3d2))

## 4.52.3 (2024-07-02)

Full Changelog: [v4.52.2...v4.52.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.2...v4.52.3)

### Chores

* minor change to tests ([#916](https://github.com/openai/openai-node/issues/916)) ([b8a33e3](https://raw.githubusercontent.com/openai/openai-node/main/b8a33e3))

## 4.52.2 (2024-06-28)

Full Changelog: [v4.52.1...v4.52.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.1...v4.52.2)

### Chores

* gitignore test server logs ([#914](https://github.com/openai/openai-node/issues/914)) ([6316720](https://raw.githubusercontent.com/openai/openai-node/main/6316720))

## 4.52.1 (2024-06-25)

Full Changelog: [v4.52.0...v4.52.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.52.0...v4.52.1)

### Chores

* **doc:** clarify service tier default value ([#908](https://github.com/openai/openai-node/issues/908)) ([e4c8100](https://raw.githubusercontent.com/openai/openai-node/main/e4c8100))
* **internal:** minor reformatting ([#911](https://github.com/openai/openai-node/issues/911)) ([78c9377](https://raw.githubusercontent.com/openai/openai-node/main/78c9377))
* **internal:** re-order some imports ([#904](https://github.com/openai/openai-node/issues/904)) ([dbd5c40](https://raw.githubusercontent.com/openai/openai-node/main/dbd5c40))

## 4.52.0 (2024-06-18)

Full Changelog: [v4.51.0...v4.52.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.51.0...v4.52.0)

### Features

* **api:** add service tier argument for chat completions ([#900](https://github.com/openai/openai-node/issues/900)) ([91e6651](https://raw.githubusercontent.com/openai/openai-node/main/91e6651))

## 4.51.0 (2024-06-12)

Full Changelog: [v4.50.0...v4.51.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.50.0...v4.51.0)

### Features

* **api:** updates ([#894](https://github.com/openai/openai-node/issues/894)) ([b58f5a1](https://raw.githubusercontent.com/openai/openai-node/main/b58f5a1))

## 4.50.0 (2024-06-10)

Full Changelog: [v4.49.1...v4.50.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.49.1...v4.50.0)

### Features

* support `application/octet-stream` request bodies ([#892](https://github.com/openai/openai-node/issues/892)) ([51661c8](https://raw.githubusercontent.com/openai/openai-node/main/51661c8))

## 4.49.1 (2024-06-07)

Full Changelog: [v4.49.0...v4.49.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.49.0...v4.49.1)

### Bug Fixes

* remove erroneous thread create argument ([#889](https://github.com/openai/openai-node/issues/889)) ([a9f898e](https://raw.githubusercontent.com/openai/openai-node/main/a9f898e))

## 4.49.0 (2024-06-06)

Full Changelog: [v4.48.3...v4.49.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.48.3...v4.49.0)

### Features

* **api:** updates ([#887](https://github.com/openai/openai-node/issues/887)) ([359eeb3](https://raw.githubusercontent.com/openai/openai-node/main/359eeb3))

## 4.48.3 (2024-06-06)

Full Changelog: [v4.48.2...v4.48.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.48.2...v4.48.3)

### Chores

* **internal:** minor refactor of tests ([#884](https://github.com/openai/openai-node/issues/884)) ([0b71f2b](https://raw.githubusercontent.com/openai/openai-node/main/0b71f2b))

## 4.48.2 (2024-06-05)

Full Changelog: [v4.48.1...v4.48.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.48.1...v4.48.2)

### Chores

* **internal:** minor change to tests ([#881](https://github.com/openai/openai-node/issues/881)) ([5e2d608](https://raw.githubusercontent.com/openai/openai-node/main/5e2d608))

## 4.48.1 (2024-06-04)

Full Changelog: [v4.48.0...v4.48.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.48.0...v4.48.1)

### Bug Fixes

* resolve typescript issue ([1129707](https://raw.githubusercontent.com/openai/openai-node/main/1129707))

## 4.48.0 (2024-06-03)

Full Changelog: [v4.47.3...v4.48.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.47.3...v4.48.0)

### Features

* **api:** updates ([#874](https://github.com/openai/openai-node/issues/874)) ([295c248](https://raw.githubusercontent.com/openai/openai-node/main/295c248))

## 4.47.3 (2024-05-31)

Full Changelog: [v4.47.2...v4.47.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.47.2...v4.47.3)

### Bug Fixes

* allow git imports for pnpm ([#873](https://github.com/openai/openai-node/issues/873)) ([9da9809](https://raw.githubusercontent.com/openai/openai-node/main/9da9809))

### Documentation

* **azure:** update example and readme to use Entra ID ([#857](https://github.com/openai/openai-node/issues/857)) ([722eff1](https://raw.githubusercontent.com/openai/openai-node/main/722eff1))

## 4.47.2 (2024-05-28)

Full Changelog: [v4.47.1...v4.47.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.47.1...v4.47.2)

### Documentation

* **readme:** add bundle size badge ([#869](https://github.com/openai/openai-node/issues/869)) ([e252132](https://raw.githubusercontent.com/openai/openai-node/main/e252132))

## 4.47.1 (2024-05-14)

Full Changelog: [v4.47.0...v4.47.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.47.0...v4.47.1)

### Chores

* **internal:** add slightly better logging to scripts ([#848](https://github.com/openai/openai-node/issues/848)) ([139e690](https://raw.githubusercontent.com/openai/openai-node/main/139e690))

## 4.47.0 (2024-05-14)

Full Changelog: [v4.46.1...v4.47.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.46.1...v4.47.0)

### Features

* **api:** add incomplete state ([#846](https://github.com/openai/openai-node/issues/846)) ([5f663a1](https://raw.githubusercontent.com/openai/openai-node/main/5f663a1))

## 4.46.1 (2024-05-13)

Full Changelog: [v4.46.0...v4.46.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.46.0...v4.46.1)

### Refactors

* change import paths to be relative ([#843](https://github.com/openai/openai-node/issues/843)) ([7913574](https://raw.githubusercontent.com/openai/openai-node/main/7913574))

## 4.46.0 (2024-05-13)

Full Changelog: [v4.45.0...v4.46.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.45.0...v4.46.0)

### Features

* **api:** add gpt-4o model ([#841](https://github.com/openai/openai-node/issues/841)) ([c818ed1](https://raw.githubusercontent.com/openai/openai-node/main/c818ed1))

## 4.45.0 (2024-05-11)

Full Changelog: [v4.44.0...v4.45.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.44.0...v4.45.0)

### Features

* **azure:** batch api ([#839](https://github.com/openai/openai-node/issues/839)) ([e279f8c](https://raw.githubusercontent.com/openai/openai-node/main/e279f8c))

### Chores

* **dependency:** bumped Next.js version ([#836](https://github.com/openai/openai-node/issues/836)) ([babb140](https://raw.githubusercontent.com/openai/openai-node/main/babb140))
* **docs:** add SECURITY.md ([#838](https://github.com/openai/openai-node/issues/838)) ([6e556d9](https://raw.githubusercontent.com/openai/openai-node/main/6e556d9))

## 4.44.0 (2024-05-09)

Full Changelog: [v4.43.0...v4.44.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.43.0...v4.44.0)

### Features

* **api:** add message image content ([#834](https://github.com/openai/openai-node/issues/834)) ([7757b3e](https://raw.githubusercontent.com/openai/openai-node/main/7757b3e))

## 4.43.0 (2024-05-08)

Full Changelog: [v4.42.0...v4.43.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.42.0...v4.43.0)

### Features

* **api:** adding file purposes ([#831](https://github.com/openai/openai-node/issues/831)) ([a62b877](https://raw.githubusercontent.com/openai/openai-node/main/a62b877))

## 4.42.0 (2024-05-06)

Full Changelog: [v4.41.1...v4.42.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.41.1...v4.42.0)

### Features

* **api:** add usage metadata when streaming ([#829](https://github.com/openai/openai-node/issues/829)) ([6707f11](https://raw.githubusercontent.com/openai/openai-node/main/6707f11))

### Bug Fixes

* **example:** fix fine tuning example ([#827](https://github.com/openai/openai-node/issues/827)) ([6480a50](https://raw.githubusercontent.com/openai/openai-node/main/6480a50))

## 4.41.1 (2024-05-06)

Full Changelog: [v4.41.0...v4.41.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.41.0...v4.41.1)

### Bug Fixes

* **azure:** update build script ([#825](https://github.com/openai/openai-node/issues/825)) ([8afc6e7](https://raw.githubusercontent.com/openai/openai-node/main/8afc6e7))

## 4.41.0 (2024-05-05)

Full Changelog: [v4.40.2...v4.41.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.40.2...v4.41.0)

### Features

* **client:** add Azure client ([#822](https://github.com/openai/openai-node/issues/822)) ([92f9049](https://raw.githubusercontent.com/openai/openai-node/main/92f9049))

## 4.40.2 (2024-05-03)

Full Changelog: [v4.40.1...v4.40.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.40.1...v4.40.2)

### Bug Fixes

* **package:** revert recent client file change ([#819](https://github.com/openai/openai-node/issues/819)) ([fa722c9](https://raw.githubusercontent.com/openai/openai-node/main/fa722c9))
* **vectorStores:** correct uploadAndPoll method ([#817](https://github.com/openai/openai-node/issues/817)) ([d63f22c](https://raw.githubusercontent.com/openai/openai-node/main/d63f22c))

## 4.40.1 (2024-05-02)

Full Changelog: [v4.40.0...v4.40.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.40.0...v4.40.1)

### Chores

* **internal:** bump prism version ([#813](https://github.com/openai/openai-node/issues/813)) ([81a6c28](https://raw.githubusercontent.com/openai/openai-node/main/81a6c28))
* **internal:** move client class to separate file ([#815](https://github.com/openai/openai-node/issues/815)) ([d0b915a](https://raw.githubusercontent.com/openai/openai-node/main/d0b915a))

## 4.40.0 (2024-05-01)

Full Changelog: [v4.39.1...v4.40.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.39.1...v4.40.0)

### Features

* **api:** delete messages ([#811](https://github.com/openai/openai-node/issues/811)) ([9e37dbd](https://raw.githubusercontent.com/openai/openai-node/main/9e37dbd))

## 4.39.1 (2024-04-30)

Full Changelog: [v4.39.0...v4.39.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.39.0...v4.39.1)

### Chores

* **internal:** add link to openapi spec ([#810](https://github.com/openai/openai-node/issues/810)) ([61b5b83](https://raw.githubusercontent.com/openai/openai-node/main/61b5b83))
* **internal:** fix release please for deno ([#808](https://github.com/openai/openai-node/issues/808)) ([ecc2eae](https://raw.githubusercontent.com/openai/openai-node/main/ecc2eae))
* **internal:** refactor scripts ([#806](https://github.com/openai/openai-node/issues/806)) ([9283519](https://raw.githubusercontent.com/openai/openai-node/main/9283519))

## 4.39.0 (2024-04-29)

Full Changelog: [v4.38.5...v4.39.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.5...v4.39.0)

### Features

* **api:** add required tool_choice ([#803](https://github.com/openai/openai-node/issues/803)) ([99693e6](https://raw.githubusercontent.com/openai/openai-node/main/99693e6))

### Chores

* **internal:** add scripts/test and scripts/mock ([#801](https://github.com/openai/openai-node/issues/801)) ([6656105](https://raw.githubusercontent.com/openai/openai-node/main/6656105))

## 4.38.5 (2024-04-24)

Full Changelog: [v4.38.4...v4.38.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.4...v4.38.5)

### Chores

* **internal:** use actions/checkout@v4 for codeflow ([#799](https://github.com/openai/openai-node/issues/799)) ([5ab7780](https://raw.githubusercontent.com/openai/openai-node/main/5ab7780))

## 4.38.4 (2024-04-24)

Full Changelog: [v4.38.3...v4.38.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.3...v4.38.4)

### Bug Fixes

* **api:** change timestamps to unix integers ([#798](https://github.com/openai/openai-node/issues/798)) ([7271a6c](https://raw.githubusercontent.com/openai/openai-node/main/7271a6c))
* **docs:** doc improvements ([#796](https://github.com/openai/openai-node/issues/796)) ([49fcc86](https://raw.githubusercontent.com/openai/openai-node/main/49fcc86))

## 4.38.3 (2024-04-22)

Full Changelog: [v4.38.2...v4.38.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.2...v4.38.3)

### Chores

* **internal:** use @swc/jest for running tests ([#793](https://github.com/openai/openai-node/issues/793)) ([8947f19](https://raw.githubusercontent.com/openai/openai-node/main/8947f19))

## 4.38.2 (2024-04-19)

Full Changelog: [v4.38.1...v4.38.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.1...v4.38.2)

### Bug Fixes

* **api:** correct types for message attachment tools ([#787](https://github.com/openai/openai-node/issues/787)) ([8626884](https://raw.githubusercontent.com/openai/openai-node/main/8626884))

## 4.38.1 (2024-04-18)

Full Changelog: [v4.38.0...v4.38.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.38.0...v4.38.1)

### Bug Fixes

* **api:** correct types for attachments ([#783](https://github.com/openai/openai-node/issues/783)) ([6893631](https://raw.githubusercontent.com/openai/openai-node/main/6893631))

## 4.38.0 (2024-04-18)

Full Changelog: [v4.37.1...v4.38.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.37.1...v4.38.0)

### Features

* **api:** batch list endpoint ([#781](https://github.com/openai/openai-node/issues/781)) ([d226759](https://raw.githubusercontent.com/openai/openai-node/main/d226759))

## 4.37.1 (2024-04-17)

Full Changelog: [v4.37.0...v4.37.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.37.0...v4.37.1)

### Chores

* **api:** docs and response_format response property ([#778](https://github.com/openai/openai-node/issues/778)) ([78f5c35](https://raw.githubusercontent.com/openai/openai-node/main/78f5c35))

## 4.37.0 (2024-04-17)

Full Changelog: [v4.36.0...v4.37.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.36.0...v4.37.0)

### Features

* **api:** add vector stores ([#776](https://github.com/openai/openai-node/issues/776)) ([8bb929b](https://raw.githubusercontent.com/openai/openai-node/main/8bb929b))

## 4.36.0 (2024-04-16)

Full Changelog: [v4.35.0...v4.36.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.35.0...v4.36.0)

### Features

* **client:** add header OpenAI-Project ([#772](https://github.com/openai/openai-node/issues/772)) ([bb4df37](https://raw.githubusercontent.com/openai/openai-node/main/bb4df37))
* extract chat models to a named enum ([#775](https://github.com/openai/openai-node/issues/775)) ([141d2ed](https://raw.githubusercontent.com/openai/openai-node/main/141d2ed))

### Build System

* configure UTF-8 locale in devcontainer ([#774](https://github.com/openai/openai-node/issues/774)) ([bebf4f0](https://raw.githubusercontent.com/openai/openai-node/main/bebf4f0))

## 4.35.0 (2024-04-15)

Full Changelog: [v4.34.0...v4.35.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.34.0...v4.35.0)

### Features

* **errors:** add request_id property ([#769](https://github.com/openai/openai-node/issues/769)) ([43aa6a1](https://raw.githubusercontent.com/openai/openai-node/main/43aa6a1))

## 4.34.0 (2024-04-15)

Full Changelog: [v4.33.1...v4.34.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.33.1...v4.34.0)

### Features

* **api:** add batch API ([#768](https://github.com/openai/openai-node/issues/768)) ([7fe34f2](https://raw.githubusercontent.com/openai/openai-node/main/7fe34f2))
* **api:** updates ([#766](https://github.com/openai/openai-node/issues/766)) ([52bcc47](https://raw.githubusercontent.com/openai/openai-node/main/52bcc47))

## 4.33.1 (2024-04-12)

Full Changelog: [v4.33.0...v4.33.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.33.0...v4.33.1)

### Chores

* **internal:** formatting ([#763](https://github.com/openai/openai-node/issues/763)) ([b6acf54](https://raw.githubusercontent.com/openai/openai-node/main/b6acf54))
* **internal:** improve ecosystem tests ([#761](https://github.com/openai/openai-node/issues/761)) ([fcf748d](https://raw.githubusercontent.com/openai/openai-node/main/fcf748d))

## 4.33.0 (2024-04-05)

Full Changelog: [v4.32.2...v4.33.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.32.2...v4.33.0)

### Features

* **api:** add additional messages when creating thread run ([#759](https://github.com/openai/openai-node/issues/759)) ([f1fdb41](https://raw.githubusercontent.com/openai/openai-node/main/f1fdb41))

## 4.32.2 (2024-04-04)

Full Changelog: [v4.32.1...v4.32.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.32.1...v4.32.2)

### Bug Fixes

* **streaming:** handle special line characters and fix multi-byte character decoding ([#757](https://github.com/openai/openai-node/issues/757)) ([8dcdda2](https://raw.githubusercontent.com/openai/openai-node/main/8dcdda2))
* **tests:** update wrangler to v3.19.0 (CVE-2023-7080) ([#755](https://github.com/openai/openai-node/issues/755)) ([47ca41d](https://raw.githubusercontent.com/openai/openai-node/main/47ca41d))

### Chores

* **tests:** bump ecosystem tests dependencies ([#753](https://github.com/openai/openai-node/issues/753)) ([3f86ea2](https://raw.githubusercontent.com/openai/openai-node/main/3f86ea2))

## 4.32.1 (2024-04-02)

Full Changelog: [v4.32.0...v4.32.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.32.0...v4.32.1)

### Chores

* **deps:** bump yarn to v1.22.22 ([#751](https://github.com/openai/openai-node/issues/751)) ([5b41d10](https://raw.githubusercontent.com/openai/openai-node/main/5b41d10))

## 4.32.0 (2024-04-01)

Full Changelog: [v4.31.0...v4.32.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.31.0...v4.32.0)

### Features

* **api:** add support for filtering messages by run_id ([#747](https://github.com/openai/openai-node/issues/747)) ([9a397ac](https://raw.githubusercontent.com/openai/openai-node/main/9a397ac))
* **api:** run polling helpers ([#749](https://github.com/openai/openai-node/issues/749)) ([02920ae](https://raw.githubusercontent.com/openai/openai-node/main/02920ae))

### Chores

* **deps:** remove unused dependency digest-fetch ([#748](https://github.com/openai/openai-node/issues/748)) ([5376837](https://raw.githubusercontent.com/openai/openai-node/main/5376837))

### Documentation

* **readme:** change undocumented params wording ([#744](https://github.com/openai/openai-node/issues/744)) ([8796691](https://raw.githubusercontent.com/openai/openai-node/main/8796691))

### Refactors

* rename createAndStream to stream ([02920ae](https://raw.githubusercontent.com/openai/openai-node/main/02920ae))

## 4.31.0 (2024-03-30)

Full Changelog: [v4.30.0...v4.31.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.30.0...v4.31.0)

### Features

* **api:** adding temperature parameter ([#742](https://github.com/openai/openai-node/issues/742)) ([b173b05](https://raw.githubusercontent.com/openai/openai-node/main/b173b05))

### Bug Fixes

* **streaming:** trigger all event handlers with fromReadableStream ([#741](https://github.com/openai/openai-node/issues/741)) ([7b1e593](https://raw.githubusercontent.com/openai/openai-node/main/7b1e593))

## 4.30.0 (2024-03-28)

Full Changelog: [v4.29.2...v4.30.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.29.2...v4.30.0)

### Features

* assistant fromReadableStream ([#738](https://github.com/openai/openai-node/issues/738)) ([8f4ba18](https://raw.githubusercontent.com/openai/openai-node/main/8f4ba18))

### Bug Fixes

* **client:** correctly send deno version header ([#736](https://github.com/openai/openai-node/issues/736)) ([b7ea175](https://raw.githubusercontent.com/openai/openai-node/main/b7ea175))
* **example:** correcting example ([#739](https://github.com/openai/openai-node/issues/739)) ([a819551](https://raw.githubusercontent.com/openai/openai-node/main/a819551))
* handle process.env being undefined in debug func ([#733](https://github.com/openai/openai-node/issues/733)) ([2baa149](https://raw.githubusercontent.com/openai/openai-node/main/2baa149))
* **internal:** make toFile use input file's options ([#727](https://github.com/openai/openai-node/issues/727)) ([15880d7](https://raw.githubusercontent.com/openai/openai-node/main/15880d7))

### Chores

* **internal:** add type ([#737](https://github.com/openai/openai-node/issues/737)) ([18c1989](https://raw.githubusercontent.com/openai/openai-node/main/18c1989))

### Documentation

* **readme:** consistent use of sentence case in headings ([#729](https://github.com/openai/openai-node/issues/729)) ([7e515fd](https://raw.githubusercontent.com/openai/openai-node/main/7e515fd))
* **readme:** document how to make undocumented requests ([#730](https://github.com/openai/openai-node/issues/730)) ([a06d861](https://raw.githubusercontent.com/openai/openai-node/main/a06d861))

## 4.29.2 (2024-03-19)

Full Changelog: [v4.29.1...v4.29.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.29.1...v4.29.2)

### Chores

* **internal:** update generated pragma comment ([#724](https://github.com/openai/openai-node/issues/724)) ([139e205](https://raw.githubusercontent.com/openai/openai-node/main/139e205))

### Documentation

* assistant improvements ([#725](https://github.com/openai/openai-node/issues/725)) ([6a2c41b](https://raw.githubusercontent.com/openai/openai-node/main/6a2c41b))
* fix typo in CONTRIBUTING.md ([#722](https://github.com/openai/openai-node/issues/722)) ([05ff8f7](https://raw.githubusercontent.com/openai/openai-node/main/05ff8f7))

## 4.29.1 (2024-03-15)

Full Changelog: [v4.29.0...v4.29.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.29.0...v4.29.1)

### Documentation

* **readme:** assistant streaming ([#719](https://github.com/openai/openai-node/issues/719)) ([bc9a1ca](https://raw.githubusercontent.com/openai/openai-node/main/bc9a1ca))

## 4.29.0 (2024-03-13)

Full Changelog: [v4.28.5...v4.29.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.5...v4.29.0)

### Features

* **assistants:** add support for streaming ([#714](https://github.com/openai/openai-node/issues/714)) ([7d27d28](https://raw.githubusercontent.com/openai/openai-node/main/7d27d28))

## 4.28.5 (2024-03-13)

Full Changelog: [v4.28.4...v4.28.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.4...v4.28.5)

### Bug Fixes

* **ChatCompletionStream:** abort on async iterator break and handle errors ([#699](https://github.com/openai/openai-node/issues/699)) ([ac417a2](https://raw.githubusercontent.com/openai/openai-node/main/ac417a2))
* **streaming:** correctly handle trailing new lines in byte chunks ([#708](https://github.com/openai/openai-node/issues/708)) ([4753be2](https://raw.githubusercontent.com/openai/openai-node/main/4753be2))

### Chores

* **api:** update docs ([#703](https://github.com/openai/openai-node/issues/703)) ([e1db98b](https://raw.githubusercontent.com/openai/openai-node/main/e1db98b))
* **docs:** mention install from git repo ([#700](https://github.com/openai/openai-node/issues/700)) ([c081bdb](https://raw.githubusercontent.com/openai/openai-node/main/c081bdb))
* fix error handler in readme ([#704](https://github.com/openai/openai-node/issues/704)) ([4ff790a](https://raw.githubusercontent.com/openai/openai-node/main/4ff790a))
* **internal:** add explicit type annotation to decoder ([#712](https://github.com/openai/openai-node/issues/712)) ([d728e99](https://raw.githubusercontent.com/openai/openai-node/main/d728e99))
* **types:** fix accidental exposure of Buffer type to cloudflare ([#709](https://github.com/openai/openai-node/issues/709)) ([0323ecb](https://raw.githubusercontent.com/openai/openai-node/main/0323ecb))

### Documentation

* **contributing:** improve wording ([#696](https://github.com/openai/openai-node/issues/696)) ([940d569](https://raw.githubusercontent.com/openai/openai-node/main/940d569))
* **readme:** fix https proxy example ([#705](https://github.com/openai/openai-node/issues/705)) ([d144789](https://raw.githubusercontent.com/openai/openai-node/main/d144789))
* **readme:** fix typo in custom fetch implementation ([#698](https://github.com/openai/openai-node/issues/698)) ([64041fd](https://raw.githubusercontent.com/openai/openai-node/main/64041fd))
* remove extraneous --save and yarn install instructions ([#710](https://github.com/openai/openai-node/issues/710)) ([8ec216d](https://raw.githubusercontent.com/openai/openai-node/main/8ec216d))
* use [@deprecated](https://raw.githubusercontent.com/openai/openai-node/main/@deprecated) decorator for deprecated params ([#711](https://github.com/openai/openai-node/issues/711)) ([4688ef4](https://raw.githubusercontent.com/openai/openai-node/main/4688ef4))

## 4.28.4 (2024-02-28)

Full Changelog: [v4.28.3...v4.28.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.3...v4.28.4)

### Features

* **api:** add wav and pcm to response_format ([#691](https://github.com/openai/openai-node/issues/691)) ([b1c6171](https://raw.githubusercontent.com/openai/openai-node/main/b1c6171))

### Chores

* **ci:** update actions/setup-node action to v4 ([#685](https://github.com/openai/openai-node/issues/685)) ([f2704d5](https://raw.githubusercontent.com/openai/openai-node/main/f2704d5))
* **internal:** fix ecosystem tests ([#693](https://github.com/openai/openai-node/issues/693)) ([616624d](https://raw.githubusercontent.com/openai/openai-node/main/616624d))
* **types:** extract run status to a named type ([#686](https://github.com/openai/openai-node/issues/686)) ([b3b3b8e](https://raw.githubusercontent.com/openai/openai-node/main/b3b3b8e))
* update @types/react to 18.2.58, @types/react-dom to 18.2.19 ([#688](https://github.com/openai/openai-node/issues/688)) ([2a0d0b1](https://raw.githubusercontent.com/openai/openai-node/main/2a0d0b1))
* update dependency @types/node to v20.11.20 ([#690](https://github.com/openai/openai-node/issues/690)) ([4ca005b](https://raw.githubusercontent.com/openai/openai-node/main/4ca005b))
* update dependency @types/ws to v8.5.10 ([#683](https://github.com/openai/openai-node/issues/683)) ([a617268](https://raw.githubusercontent.com/openai/openai-node/main/a617268))
* update dependency next to v13.5.6 ([#689](https://github.com/openai/openai-node/issues/689)) ([abb3b66](https://raw.githubusercontent.com/openai/openai-node/main/abb3b66))

## 4.28.3 (2024-02-20)

Full Changelog: [v4.28.2...v4.28.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.2...v4.28.3)

### Bug Fixes

* **ci:** revert "move github release logic to github app" ([#680](https://github.com/openai/openai-node/issues/680)) ([8b4009a](https://raw.githubusercontent.com/openai/openai-node/main/8b4009a))

## 4.28.2 (2024-02-19)

Full Changelog: [v4.28.1...v4.28.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.1...v4.28.2)

### Bug Fixes

* **api:** remove non-GA instance_id param ([#677](https://github.com/openai/openai-node/issues/677)) ([4d0d4da](https://raw.githubusercontent.com/openai/openai-node/main/4d0d4da))

## 4.28.1 (2024-02-19)

Full Changelog: [v4.28.0...v4.28.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.28.0...v4.28.1)

### Chores

* **ci:** move github release logic to github app ([#671](https://github.com/openai/openai-node/issues/671)) ([ecca6bc](https://raw.githubusercontent.com/openai/openai-node/main/ecca6bc))
* **internal:** refactor release environment script ([#674](https://github.com/openai/openai-node/issues/674)) ([27d3770](https://raw.githubusercontent.com/openai/openai-node/main/27d3770))

## 4.28.0 (2024-02-13)

Full Changelog: [v4.27.1...v4.28.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.27.1...v4.28.0)

### Features

* **api:** updates ([#669](https://github.com/openai/openai-node/issues/669)) ([e1900f9](https://raw.githubusercontent.com/openai/openai-node/main/e1900f9))

## 4.27.1 (2024-02-12)

Full Changelog: [v4.27.0...v4.27.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.27.0...v4.27.1)

## 4.27.0 (2024-02-08)

Full Changelog: [v4.26.1...v4.27.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.26.1...v4.27.0)

### Features

* **api:** add `timestamp_granularities`, add `gpt-3.5-turbo-0125` model ([#661](https://github.com/openai/openai-node/issues/661)) ([5016806](https://raw.githubusercontent.com/openai/openai-node/main/5016806))

### Chores

* **internal:** fix retry mechanism for ecosystem-test ([#663](https://github.com/openai/openai-node/issues/663)) ([0eb7ed5](https://raw.githubusercontent.com/openai/openai-node/main/0eb7ed5))
* respect `application/vnd.api+json` content-type header ([#664](https://github.com/openai/openai-node/issues/664)) ([f4fad54](https://raw.githubusercontent.com/openai/openai-node/main/f4fad54))

## 4.26.1 (2024-02-05)

Full Changelog: [v4.26.0...v4.26.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.26.0...v4.26.1)

### Chores

* **internal:** enable building when git installed ([#657](https://github.com/openai/openai-node/issues/657)) ([8c80a7d](https://raw.githubusercontent.com/openai/openai-node/main/8c80a7d))
* **internal:** re-order pagination import ([#656](https://github.com/openai/openai-node/issues/656)) ([21ae54e](https://raw.githubusercontent.com/openai/openai-node/main/21ae54e))
* **internal:** support pre-release versioning ([#653](https://github.com/openai/openai-node/issues/653)) ([0c3859f](https://raw.githubusercontent.com/openai/openai-node/main/0c3859f))
* **test:** add delay between ecosystem tests retry ([#651](https://github.com/openai/openai-node/issues/651)) ([6a4cc5c](https://raw.githubusercontent.com/openai/openai-node/main/6a4cc5c))

### Documentation

* add a CONTRIBUTING.md ([#659](https://github.com/openai/openai-node/issues/659)) ([8ea58b0](https://raw.githubusercontent.com/openai/openai-node/main/8ea58b0))

## 4.26.0 (2024-01-25)

Full Changelog: [v4.25.0...v4.26.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.25.0...v4.26.0)

### Features

* **api:** add text embeddings dimensions param ([#650](https://github.com/openai/openai-node/issues/650)) ([1b5a977](https://raw.githubusercontent.com/openai/openai-node/main/1b5a977))

### Chores

* **internal:** add internal helpers & improve build scripts ([#643](https://github.com/openai/openai-node/issues/643)) ([9392f50](https://raw.githubusercontent.com/openai/openai-node/main/9392f50))
* **internal:** adjust ecosystem-tests logging in CI ([#646](https://github.com/openai/openai-node/issues/646)) ([156084b](https://raw.githubusercontent.com/openai/openai-node/main/156084b))
* **internal:** don't re-export streaming type ([#648](https://github.com/openai/openai-node/issues/648)) ([4c4be94](https://raw.githubusercontent.com/openai/openai-node/main/4c4be94))
* **internal:** fix binary files ([#645](https://github.com/openai/openai-node/issues/645)) ([e1fbc39](https://raw.githubusercontent.com/openai/openai-node/main/e1fbc39))
* **internal:** minor streaming updates ([#647](https://github.com/openai/openai-node/issues/647)) ([2f073e4](https://raw.githubusercontent.com/openai/openai-node/main/2f073e4))
* **internal:** pin deno version ([#649](https://github.com/openai/openai-node/issues/649)) ([7e4b903](https://raw.githubusercontent.com/openai/openai-node/main/7e4b903))

## 4.25.0 (2024-01-21)

Full Changelog: [v4.24.7...v4.25.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.7...v4.25.0)

### Features

* **api:** add usage to runs and run steps ([#640](https://github.com/openai/openai-node/issues/640)) ([3caa416](https://raw.githubusercontent.com/openai/openai-node/main/3caa416))

### Bug Fixes

* allow body type in RequestOptions to be null ([#637](https://github.com/openai/openai-node/issues/637)) ([c4f8a36](https://raw.githubusercontent.com/openai/openai-node/main/c4f8a36))
* handle system_fingerprint in streaming helpers ([#636](https://github.com/openai/openai-node/issues/636)) ([f273530](https://raw.githubusercontent.com/openai/openai-node/main/f273530))
* **types:** accept undefined for optional client options ([#635](https://github.com/openai/openai-node/issues/635)) ([e48cd57](https://raw.githubusercontent.com/openai/openai-node/main/e48cd57))

### Chores

* **internal:** debug logging for retries; speculative retry-after-ms support ([#633](https://github.com/openai/openai-node/issues/633)) ([fd64971](https://raw.githubusercontent.com/openai/openai-node/main/fd64971))
* **internal:** update comment ([#631](https://github.com/openai/openai-node/issues/631)) ([e109d40](https://raw.githubusercontent.com/openai/openai-node/main/e109d40))

## 4.24.7 (2024-01-13)

Full Changelog: [v4.24.6...v4.24.7](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.6...v4.24.7)

### Chores

* **ecosystem-tests:** fix flaky vercel-edge, cloudflare-worker, and deno tests ([#626](https://github.com/openai/openai-node/issues/626)) ([ae412a5](https://raw.githubusercontent.com/openai/openai-node/main/ae412a5))
* **ecosystem-tests:** fix typo in deno test ([#628](https://github.com/openai/openai-node/issues/628)) ([048ec94](https://raw.githubusercontent.com/openai/openai-node/main/048ec94))

## 4.24.6 (2024-01-12)

Full Changelog: [v4.24.5...v4.24.6](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.5...v4.24.6)

### Chores

* **ecosystem-tests:** fix flaky tests and remove fine tuning calls ([#623](https://github.com/openai/openai-node/issues/623)) ([258d79f](https://raw.githubusercontent.com/openai/openai-node/main/258d79f))
* **ecosystem-tests:** fix flaky tests and remove fine tuning calls ([#625](https://github.com/openai/openai-node/issues/625)) ([58e5fd8](https://raw.githubusercontent.com/openai/openai-node/main/58e5fd8))

## 4.24.5 (2024-01-12)

Full Changelog: [v4.24.4...v4.24.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.4...v4.24.5)

### Refactors

* **api:** remove deprecated endpoints ([#621](https://github.com/openai/openai-node/issues/621)) ([2054d71](https://raw.githubusercontent.com/openai/openai-node/main/2054d71))

## 4.24.4 (2024-01-11)

Full Changelog: [v4.24.3...v4.24.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.3...v4.24.4)

### Chores

* **internal:** narrow type into stringifyQuery ([#619](https://github.com/openai/openai-node/issues/619)) ([88fb9cd](https://raw.githubusercontent.com/openai/openai-node/main/88fb9cd))

## 4.24.3 (2024-01-10)

Full Changelog: [v4.24.2...v4.24.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.2...v4.24.3)

### Bug Fixes

* use default base url if BASE_URL env var is blank ([#615](https://github.com/openai/openai-node/issues/615)) ([a27ad3d](https://raw.githubusercontent.com/openai/openai-node/main/a27ad3d))

## 4.24.2 (2024-01-08)

Full Changelog: [v4.24.1...v4.24.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.1...v4.24.2)

### Bug Fixes

* **headers:** always send lowercase headers and strip undefined (BREAKING in rare cases) ([#608](https://github.com/openai/openai-node/issues/608)) ([4ea159f](https://raw.githubusercontent.com/openai/openai-node/main/4ea159f))

### Chores

* add .keep files for examples and custom code directories ([#612](https://github.com/openai/openai-node/issues/612)) ([5e0f733](https://raw.githubusercontent.com/openai/openai-node/main/5e0f733))
* **internal:** bump license ([#605](https://github.com/openai/openai-node/issues/605)) ([045ee74](https://raw.githubusercontent.com/openai/openai-node/main/045ee74))
* **internal:** improve type signatures ([#609](https://github.com/openai/openai-node/issues/609)) ([e1ccc82](https://raw.githubusercontent.com/openai/openai-node/main/e1ccc82))

### Documentation

* fix docstring typos ([#600](https://github.com/openai/openai-node/issues/600)) ([1934fa1](https://raw.githubusercontent.com/openai/openai-node/main/1934fa1))
* improve audio example to show how to stream to a file ([#598](https://github.com/openai/openai-node/issues/598)) ([e950ad9](https://raw.githubusercontent.com/openai/openai-node/main/e950ad9))

## 4.24.1 (2023-12-22)

Full Changelog: [v4.24.0...v4.24.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.24.0...v4.24.1)

### Bug Fixes

* **pagination:** correct type annotation object field ([#590](https://github.com/openai/openai-node/issues/590)) ([4066eda](https://raw.githubusercontent.com/openai/openai-node/main/4066eda))

### Documentation

* **messages:** improvements to helpers reference + typos ([#595](https://github.com/openai/openai-node/issues/595)) ([96a59b9](https://raw.githubusercontent.com/openai/openai-node/main/96a59b9))
* reformat README.md ([#592](https://github.com/openai/openai-node/issues/592)) ([8ffc7f8](https://raw.githubusercontent.com/openai/openai-node/main/8ffc7f8))

### Refactors

* write jest config in typescript ([#588](https://github.com/openai/openai-node/issues/588)) ([eb6ceeb](https://raw.githubusercontent.com/openai/openai-node/main/eb6ceeb))

## 4.24.0 (2023-12-19)

Full Changelog: [v4.23.0...v4.24.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.23.0...v4.24.0)

### Features

* **api:** add additional instructions for runs ([#586](https://github.com/openai/openai-node/issues/586)) ([401d93e](https://raw.githubusercontent.com/openai/openai-node/main/401d93e))

### Chores

* **deps:** update dependency start-server-and-test to v2.0.3 ([#580](https://github.com/openai/openai-node/issues/580)) ([8e1aca1](https://raw.githubusercontent.com/openai/openai-node/main/8e1aca1))
* **deps:** update dependency ts-jest to v29.1.1 ([#578](https://github.com/openai/openai-node/issues/578)) ([a6edb7b](https://raw.githubusercontent.com/openai/openai-node/main/a6edb7b))
* **deps:** update jest ([#582](https://github.com/openai/openai-node/issues/582)) ([e49e471](https://raw.githubusercontent.com/openai/openai-node/main/e49e471))
* **internal:** bump deps ([#583](https://github.com/openai/openai-node/issues/583)) ([2e07b4c](https://raw.githubusercontent.com/openai/openai-node/main/2e07b4c))
* **internal:** update deps ([#581](https://github.com/openai/openai-node/issues/581)) ([7b690dc](https://raw.githubusercontent.com/openai/openai-node/main/7b690dc))

### Documentation

* upgrade models in examples to latest version ([#585](https://github.com/openai/openai-node/issues/585)) ([60101a4](https://raw.githubusercontent.com/openai/openai-node/main/60101a4))

## 4.23.0 (2023-12-17)

Full Changelog: [v4.22.1...v4.23.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.22.1...v4.23.0)

### Features

* **api:** add token logprobs to chat completions ([#576](https://github.com/openai/openai-node/issues/576)) ([8d4292e](https://raw.githubusercontent.com/openai/openai-node/main/8d4292e))

### Chores

* **ci:** run release workflow once per day ([#574](https://github.com/openai/openai-node/issues/574)) ([529f09f](https://raw.githubusercontent.com/openai/openai-node/main/529f09f))

## 4.22.1 (2023-12-15)

Full Changelog: [v4.22.0...v4.22.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.22.0...v4.22.1)

### Chores

* update dependencies ([#572](https://github.com/openai/openai-node/issues/572)) ([a51e620](https://raw.githubusercontent.com/openai/openai-node/main/a51e620))

### Documentation

* replace runFunctions with runTools in readme ([#570](https://github.com/openai/openai-node/issues/570)) ([c3b9ad5](https://raw.githubusercontent.com/openai/openai-node/main/c3b9ad5))

## 4.22.0 (2023-12-15)

Full Changelog: [v4.21.0...v4.22.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.21.0...v4.22.0)

### Features

* **api:** add optional `name` argument + improve docs ([#569](https://github.com/openai/openai-node/issues/569)) ([3b68ace](https://raw.githubusercontent.com/openai/openai-node/main/3b68ace))

### Chores

* update prettier ([#567](https://github.com/openai/openai-node/issues/567)) ([83dec2a](https://raw.githubusercontent.com/openai/openai-node/main/83dec2a))

## 4.21.0 (2023-12-11)

Full Changelog: [v4.20.1...v4.21.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.20.1...v4.21.0)

### Features

* **client:** support reading the base url from an env variable ([#547](https://github.com/openai/openai-node/issues/547)) ([06fb68d](https://raw.githubusercontent.com/openai/openai-node/main/06fb68d))

### Bug Fixes

* correct some runTools behavior and deprecate runFunctions ([#562](https://github.com/openai/openai-node/issues/562)) ([f5cdd0f](https://raw.githubusercontent.com/openai/openai-node/main/f5cdd0f))
* prevent 400 when using runTools/runFunctions with Azure OpenAI API ([#544](https://github.com/openai/openai-node/issues/544)) ([735d9b8](https://raw.githubusercontent.com/openai/openai-node/main/735d9b8))

### Documentation

* **readme:** update example snippets ([#546](https://github.com/openai/openai-node/issues/546)) ([566d290](https://raw.githubusercontent.com/openai/openai-node/main/566d290))

### Build System

* specify `packageManager: yarn` ([#561](https://github.com/openai/openai-node/issues/561)) ([935b898](https://raw.githubusercontent.com/openai/openai-node/main/935b898))

## 4.20.1 (2023-11-24)

Full Changelog: [v4.20.0...v4.20.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.20.0...v4.20.1)

### Chores

* **internal:** remove file import and conditionally run prepare ([#533](https://github.com/openai/openai-node/issues/533)) ([48cb729](https://raw.githubusercontent.com/openai/openai-node/main/48cb729))

### Documentation

* **readme:** fix typo and add examples link ([#529](https://github.com/openai/openai-node/issues/529)) ([cf959b1](https://raw.githubusercontent.com/openai/openai-node/main/cf959b1))

## 4.20.0 (2023-11-22)

Full Changelog: [v4.19.1...v4.20.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.19.1...v4.20.0)

### Features

* allow installing package directly from github ([#522](https://github.com/openai/openai-node/issues/522)) ([51926d7](https://raw.githubusercontent.com/openai/openai-node/main/51926d7))

### Chores

* **internal:** don't call prepare in dist ([#525](https://github.com/openai/openai-node/issues/525)) ([d09411e](https://raw.githubusercontent.com/openai/openai-node/main/d09411e))

## 4.19.1 (2023-11-20)

Full Changelog: [v4.19.0...v4.19.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.19.0...v4.19.1)

## 4.19.0 (2023-11-15)

Full Changelog: [v4.18.0...v4.19.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.18.0...v4.19.0)

### Features

* **api:** updates ([#501](https://github.com/openai/openai-node/issues/501)) ([944d58e](https://raw.githubusercontent.com/openai/openai-node/main/944d58e))

## 4.18.0 (2023-11-14)

Full Changelog: [v4.17.5...v4.18.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.5...v4.18.0)

### Features

* **api:** add gpt-3.5-turbo-1106 ([#496](https://github.com/openai/openai-node/issues/496)) ([45f7672](https://raw.githubusercontent.com/openai/openai-node/main/45f7672))

## 4.17.5 (2023-11-13)

Full Changelog: [v4.17.4...v4.17.5](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.4...v4.17.5)

### Chores

* fix typo in docs and add request header for function calls ([#494](https://github.com/openai/openai-node/issues/494)) ([22ce244](https://raw.githubusercontent.com/openai/openai-node/main/22ce244))

## 4.17.4 (2023-11-10)

Full Changelog: [v4.17.3...v4.17.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.3...v4.17.4)

### Chores

* **internal:** update jest config ([#482](https://github.com/openai/openai-node/issues/482)) ([3013e8c](https://raw.githubusercontent.com/openai/openai-node/main/3013e8c))

## 4.17.3 (2023-11-09)

Full Changelog: [v4.17.2...v4.17.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.2...v4.17.3)

## 4.17.2 (2023-11-09)

Full Changelog: [v4.17.1...v4.17.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.1...v4.17.2)

### Chores

* **internal:** bump deno version number ([#478](https://github.com/openai/openai-node/issues/478)) ([69913f3](https://raw.githubusercontent.com/openai/openai-node/main/69913f3))

## 4.17.1 (2023-11-09)

Full Changelog: [v4.17.0...v4.17.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.17.0...v4.17.1)

### Refactors

* **client:** deprecate files.retrieveContent in favour of files.content ([#474](https://github.com/openai/openai-node/issues/474)) ([7c7bfc2](https://raw.githubusercontent.com/openai/openai-node/main/7c7bfc2))

## 4.17.0 (2023-11-08)

Full Changelog: [v4.16.2...v4.17.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.16.2...v4.17.0)

### Features

* **api:** unify function types ([#467](https://github.com/openai/openai-node/issues/467)) ([d51cd94](https://raw.githubusercontent.com/openai/openai-node/main/d51cd94))

### Refactors

* **api:** rename FunctionObject to FunctionDefinition ([#470](https://github.com/openai/openai-node/issues/470)) ([f3990c7](https://raw.githubusercontent.com/openai/openai-node/main/f3990c7))

## 4.16.2 (2023-11-08)

Full Changelog: [v4.16.1...v4.16.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.16.1...v4.16.2)

### Bug Fixes

* **api:** accidentally required params, add new models & other fixes ([#463](https://github.com/openai/openai-node/issues/463)) ([1cb403e](https://raw.githubusercontent.com/openai/openai-node/main/1cb403e))
* **api:** update embedding response object type ([#466](https://github.com/openai/openai-node/issues/466)) ([53b7e25](https://raw.githubusercontent.com/openai/openai-node/main/53b7e25))
* asssitant_deleted -&gt; assistant_deleted ([#452](https://github.com/openai/openai-node/issues/452)) ([ef89bd7](https://raw.githubusercontent.com/openai/openai-node/main/ef89bd7))
* **types:** ensure all code paths return a value ([#458](https://github.com/openai/openai-node/issues/458)) ([19402c3](https://raw.githubusercontent.com/openai/openai-node/main/19402c3))

### Chores

* **docs:** fix github links ([#457](https://github.com/openai/openai-node/issues/457)) ([6b9b94e](https://raw.githubusercontent.com/openai/openai-node/main/6b9b94e))
* **internal:** fix typo in comment ([#456](https://github.com/openai/openai-node/issues/456)) ([fe24342](https://raw.githubusercontent.com/openai/openai-node/main/fe24342))

### Documentation

* update deno deploy link to include v ([#441](https://github.com/openai/openai-node/issues/441)) ([47b13aa](https://raw.githubusercontent.com/openai/openai-node/main/47b13aa))

## 4.16.1 (2023-11-06)

Full Changelog: [v4.16.0...v4.16.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.16.0...v4.16.1)

### Bug Fixes

* **api:** retreival -&gt; retrieval ([#437](https://github.com/openai/openai-node/issues/437)) ([b4bd3ee](https://raw.githubusercontent.com/openai/openai-node/main/b4bd3ee))

### Documentation

* **api:** improve docstrings ([#435](https://github.com/openai/openai-node/issues/435)) ([ee8b24c](https://raw.githubusercontent.com/openai/openai-node/main/ee8b24c))

## 4.16.0 (2023-11-06)

Full Changelog: [v4.15.4...v4.16.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.15.4...v4.16.0)

### Features

* **api:** releases from DevDay; assistants, multimodality, tools, dall-e-3, tts, and more ([#433](https://github.com/openai/openai-node/issues/433)) ([fb92f5e](https://raw.githubusercontent.com/openai/openai-node/main/fb92f5e))

### Bug Fixes

* improve deno readme ([#429](https://github.com/openai/openai-node/issues/429)) ([871ceac](https://raw.githubusercontent.com/openai/openai-node/main/871ceac))

### Documentation

* deno version ([#432](https://github.com/openai/openai-node/issues/432)) ([74bf336](https://raw.githubusercontent.com/openai/openai-node/main/74bf336))
* update deno link in more places ([#431](https://github.com/openai/openai-node/issues/431)) ([5da63d4](https://raw.githubusercontent.com/openai/openai-node/main/5da63d4))

## 4.15.4 (2023-11-05)

Full Changelog: [v4.15.3...v4.15.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.15.3...v4.15.4)

### Documentation

* **readme:** remove redundant whitespace ([#427](https://github.com/openai/openai-node/issues/427)) ([aa3a178](https://raw.githubusercontent.com/openai/openai-node/main/aa3a178))

## 4.15.3 (2023-11-04)

Full Changelog: [v4.15.2...v4.15.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.15.2...v4.15.3)

### Bug Fixes

* improve deno releases ([#425](https://github.com/openai/openai-node/issues/425)) ([19469f2](https://raw.githubusercontent.com/openai/openai-node/main/19469f2))

## 4.15.2 (2023-11-04)

Full Changelog: [v4.15.1...v4.15.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.15.1...v4.15.2)

### Documentation

* fix deno.land import ([#423](https://github.com/openai/openai-node/issues/423)) ([e5415a2](https://raw.githubusercontent.com/openai/openai-node/main/e5415a2))

## 4.15.1 (2023-11-04)

Full Changelog: [v4.15.0...v4.15.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.15.0...v4.15.1)

### Documentation

* document customizing fetch ([#420](https://github.com/openai/openai-node/issues/420)) ([1ca982f](https://raw.githubusercontent.com/openai/openai-node/main/1ca982f))

## 4.15.0 (2023-11-03)

Full Changelog: [v4.14.2...v4.15.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.14.2...v4.15.0)

### Features

* **beta:** add streaming and function calling helpers ([#409](https://github.com/openai/openai-node/issues/409)) ([510c1f3](https://raw.githubusercontent.com/openai/openai-node/main/510c1f3))
* **client:** allow binary returns ([#416](https://github.com/openai/openai-node/issues/416)) ([02f7ad7](https://raw.githubusercontent.com/openai/openai-node/main/02f7ad7))
* **github:** include a devcontainer setup ([#413](https://github.com/openai/openai-node/issues/413)) ([fb2996f](https://raw.githubusercontent.com/openai/openai-node/main/fb2996f))
* streaming improvements ([#411](https://github.com/openai/openai-node/issues/411)) ([37b622c](https://raw.githubusercontent.com/openai/openai-node/main/37b622c))

## 4.14.2 (2023-10-30)

Full Changelog: [v4.14.1...v4.14.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.14.1...v4.14.2)

### Chores

* **docs:** update deno link ([#407](https://github.com/openai/openai-node/issues/407)) ([0328882](https://raw.githubusercontent.com/openai/openai-node/main/0328882))

## 4.14.1 (2023-10-27)

Full Changelog: [v4.14.0...v4.14.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.14.0...v4.14.1)

### Bug Fixes

* deploy deno in a github workflow instead of postpublish step ([#405](https://github.com/openai/openai-node/issues/405)) ([3a6dba0](https://raw.githubusercontent.com/openai/openai-node/main/3a6dba0))
* typo in build script ([#403](https://github.com/openai/openai-node/issues/403)) ([76c5c96](https://raw.githubusercontent.com/openai/openai-node/main/76c5c96))

### Chores

* **internal:** update gitignore ([#406](https://github.com/openai/openai-node/issues/406)) ([986b0bb](https://raw.githubusercontent.com/openai/openai-node/main/986b0bb))

## 4.14.0 (2023-10-25)

Full Changelog: [v4.13.0...v4.14.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.13.0...v4.14.0)

### Features

* **client:** adjust retry behavior to be exponential backoff ([#400](https://github.com/openai/openai-node/issues/400)) ([2bc14ce](https://raw.githubusercontent.com/openai/openai-node/main/2bc14ce))

### Chores

* **docs:** update deno version ([#399](https://github.com/openai/openai-node/issues/399)) ([cdee077](https://raw.githubusercontent.com/openai/openai-node/main/cdee077))

## 4.13.0 (2023-10-22)

Full Changelog: [v4.12.4...v4.13.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.12.4...v4.13.0)

### Features

* **api:** add embeddings encoding_format ([#390](https://github.com/openai/openai-node/issues/390)) ([cf70dea](https://raw.githubusercontent.com/openai/openai-node/main/cf70dea))
* handle 204 No Content gracefully ([#391](https://github.com/openai/openai-node/issues/391)) ([2dd005c](https://raw.githubusercontent.com/openai/openai-node/main/2dd005c))

## 4.12.4 (2023-10-17)

Full Changelog: [v4.12.3...v4.12.4](https://raw.githubusercontent.com/openai/openai-node/main/v4.12.3...v4.12.4)

### Bug Fixes

* import web-streams-polyfill without overriding globals ([#385](https://github.com/openai/openai-node/issues/385)) ([be8e18b](https://raw.githubusercontent.com/openai/openai-node/main/be8e18b))

## 4.12.3 (2023-10-16)

Full Changelog: [v4.12.2...v4.12.3](https://raw.githubusercontent.com/openai/openai-node/main/v4.12.2...v4.12.3)

### Documentation

* organisation -&gt; organization (UK to US English) ([#382](https://github.com/openai/openai-node/issues/382)) ([516f0ad](https://raw.githubusercontent.com/openai/openai-node/main/516f0ad))

## 4.12.2 (2023-10-16)

Full Changelog: [v4.12.1...v4.12.2](https://raw.githubusercontent.com/openai/openai-node/main/v4.12.1...v4.12.2)

### Bug Fixes

* **client:** correctly handle errors during streaming ([#377](https://github.com/openai/openai-node/issues/377)) ([09233b1](https://raw.githubusercontent.com/openai/openai-node/main/09233b1))
* **client:** correctly handle errors during streaming ([#379](https://github.com/openai/openai-node/issues/379)) ([9ced580](https://raw.githubusercontent.com/openai/openai-node/main/9ced580))
* improve status code in error messages ([#381](https://github.com/openai/openai-node/issues/381)) ([68dfb17](https://raw.githubusercontent.com/openai/openai-node/main/68dfb17))

### Chores

* add case insensitive get header function ([#373](https://github.com/openai/openai-node/issues/373)) ([b088998](https://raw.githubusercontent.com/openai/openai-node/main/b088998))
* **internal:** add debug logs for stream responses ([#380](https://github.com/openai/openai-node/issues/380)) ([689db0b](https://raw.githubusercontent.com/openai/openai-node/main/689db0b))
* show deprecation notice on re-export ([#368](https://github.com/openai/openai-node/issues/368)) ([b176703](https://raw.githubusercontent.com/openai/openai-node/main/b176703))
* update comment ([#376](https://github.com/openai/openai-node/issues/376)) ([a06c685](https://raw.githubusercontent.com/openai/openai-node/main/a06c685))
* update comment ([#378](https://github.com/openai/openai-node/issues/378)) ([b04031d](https://raw.githubusercontent.com/openai/openai-node/main/b04031d))

### Refactors

* **streaming:** change Stream constructor signature ([#370](https://github.com/openai/openai-node/issues/370)) ([71984ed](https://raw.githubusercontent.com/openai/openai-node/main/71984ed))
* **test:** refactor authentication tests ([#371](https://github.com/openai/openai-node/issues/371)) ([e0d459f](https://raw.githubusercontent.com/openai/openai-node/main/e0d459f))

## 4.12.1 (2023-10-11)

Full Changelog: [v4.12.0...v4.12.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.12.0...v4.12.1)

### Bug Fixes

* fix namespace exports regression ([#366](https://github.com/openai/openai-node/issues/366)) ([b2b1d85](https://raw.githubusercontent.com/openai/openai-node/main/b2b1d85))

## 4.12.0 (2023-10-11)

Full Changelog: [v4.11.1...v4.12.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.11.1...v4.12.0)

### Features

* **api:** remove `content_filter` stop_reason and update documentation ([#352](https://github.com/openai/openai-node/issues/352)) ([a4b401e](https://raw.githubusercontent.com/openai/openai-node/main/a4b401e))
* re-export chat completion types at the top level, and work around webpack limitations ([#365](https://github.com/openai/openai-node/issues/365)) ([bb815d0](https://raw.githubusercontent.com/openai/openai-node/main/bb815d0))

### Bug Fixes

* prevent ReferenceError, update compatibility to ES2020 and Node 18+ ([#356](https://github.com/openai/openai-node/issues/356)) ([fc71a4b](https://raw.githubusercontent.com/openai/openai-node/main/fc71a4b))

### Chores

* **internal:** minor formatting improvement ([#354](https://github.com/openai/openai-node/issues/354)) ([3799863](https://raw.githubusercontent.com/openai/openai-node/main/3799863))

## 4.11.1 (2023-10-03)

Full Changelog: [v4.11.0...v4.11.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.11.0...v4.11.1)

## 4.11.0 (2023-09-29)

Full Changelog: [v4.10.0...v4.11.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.10.0...v4.11.0)

### Features

* **client:** handle retry-after with a date ([#340](https://github.com/openai/openai-node/issues/340)) ([b6dd384](https://raw.githubusercontent.com/openai/openai-node/main/b6dd384))
* **package:** export a root error type ([#338](https://github.com/openai/openai-node/issues/338)) ([462bcda](https://raw.githubusercontent.com/openai/openai-node/main/462bcda))

### Bug Fixes

* **api:** add content_filter to chat completion finish reason ([#344](https://github.com/openai/openai-node/issues/344)) ([f10c757](https://raw.githubusercontent.com/openai/openai-node/main/f10c757))

### Chores

* **internal:** bump lock file ([#334](https://github.com/openai/openai-node/issues/334)) ([fd2337b](https://raw.githubusercontent.com/openai/openai-node/main/fd2337b))
* **internal:** update lock file ([#339](https://github.com/openai/openai-node/issues/339)) ([1bf84b6](https://raw.githubusercontent.com/openai/openai-node/main/1bf84b6))
* **internal:** update lock file ([#342](https://github.com/openai/openai-node/issues/342)) ([0001f06](https://raw.githubusercontent.com/openai/openai-node/main/0001f06))
* **internal:** update lock file ([#343](https://github.com/openai/openai-node/issues/343)) ([a02ac8e](https://raw.githubusercontent.com/openai/openai-node/main/a02ac8e))

## 4.10.0 (2023-09-21)

Full Changelog: [v4.9.1...v4.10.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.9.1...v4.10.0)

### Features

* **api:** add 'gpt-3.5-turbo-instruct', fine-tune error objects, update documentation ([#329](https://github.com/openai/openai-node/issues/329)) ([e5f3852](https://raw.githubusercontent.com/openai/openai-node/main/e5f3852))

## 4.10.0 (2023-09-21)

Full Changelog: [v4.9.1...v4.10.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.9.1...v4.10.0)

### Features

* **api:** add 'gpt-3.5-turbo-instruct', fine-tune error objects, update documentation ([#329](https://github.com/openai/openai-node/issues/329)) ([e5f3852](https://raw.githubusercontent.com/openai/openai-node/main/e5f3852))

## 4.9.1 (2023-09-21)

Full Changelog: [v4.9.0...v4.9.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.9.0...v4.9.1)

### Documentation

* **README:** fix variable names in some examples ([#327](https://github.com/openai/openai-node/issues/327)) ([5e05b31](https://raw.githubusercontent.com/openai/openai-node/main/5e05b31))

## 4.9.0 (2023-09-20)

Full Changelog: [v4.8.0...v4.9.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.8.0...v4.9.0)

### Features

* **client:** support importing node or web shims manually ([#325](https://github.com/openai/openai-node/issues/325)) ([628f293](https://raw.githubusercontent.com/openai/openai-node/main/628f293))

## 4.8.0 (2023-09-15)

Full Changelog: [v4.7.1...v4.8.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.7.1...v4.8.0)

### Features

* **errors:** add status code to error message ([#315](https://github.com/openai/openai-node/issues/315)) ([9341219](https://raw.githubusercontent.com/openai/openai-node/main/9341219))

## 4.7.1 (2023-09-15)

Full Changelog: [v4.7.0...v4.7.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.7.0...v4.7.1)

### Documentation

* declare Bun 1.0 officially supported ([#314](https://github.com/openai/openai-node/issues/314)) ([a16e268](https://raw.githubusercontent.com/openai/openai-node/main/a16e268))

## 4.7.0 (2023-09-14)

Full Changelog: [v4.6.0...v4.7.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.6.0...v4.7.0)

### Features

* **client:** retry on 408 Request Timeout ([#310](https://github.com/openai/openai-node/issues/310)) ([1f98eac](https://raw.githubusercontent.com/openai/openai-node/main/1f98eac))
* make docs urls in comments absolute ([#306](https://github.com/openai/openai-node/issues/306)) ([9db3819](https://raw.githubusercontent.com/openai/openai-node/main/9db3819))

## 4.6.0 (2023-09-08)

Full Changelog: [v4.5.0...v4.6.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.5.0...v4.6.0)

### Features

* **types:** extract ChatCompletionRole enum to its own type ([#298](https://github.com/openai/openai-node/issues/298)) ([5893e37](https://raw.githubusercontent.com/openai/openai-node/main/5893e37))

### Bug Fixes

* fix module not found errors in Vercel edge ([#300](https://github.com/openai/openai-node/issues/300)) ([47c79fe](https://raw.githubusercontent.com/openai/openai-node/main/47c79fe))

## 4.5.0 (2023-09-06)

Full Changelog: [v4.4.0...v4.5.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.4.0...v4.5.0)

### Features

* **client:** add files.waitForProcessing() method ([#292](https://github.com/openai/openai-node/issues/292)) ([ef59010](https://raw.githubusercontent.com/openai/openai-node/main/ef59010))
* fixes tests where an array has to have unique enum values ([#290](https://github.com/openai/openai-node/issues/290)) ([a10b895](https://raw.githubusercontent.com/openai/openai-node/main/a10b895))
* make docs more readable by eliminating unnecessary escape sequences ([#287](https://github.com/openai/openai-node/issues/287)) ([a068043](https://raw.githubusercontent.com/openai/openai-node/main/a068043))

### Bug Fixes

* **client:** fix TS errors that appear when users Go to Source in VSCode ([#281](https://github.com/openai/openai-node/issues/281)) ([8dc59bc](https://raw.githubusercontent.com/openai/openai-node/main/8dc59bc)), closes [#249](https://github.com/openai/openai-node/issues/249)
* **client:** handle case where the client is instantiated with a undefined baseURL ([#285](https://github.com/openai/openai-node/issues/285)) ([5095cf3](https://raw.githubusercontent.com/openai/openai-node/main/5095cf3))
* **client:** use explicit file extensions in _shims imports ([#276](https://github.com/openai/openai-node/issues/276)) ([16fe929](https://raw.githubusercontent.com/openai/openai-node/main/16fe929))

### Documentation

* **api:** update docstrings ([#286](https://github.com/openai/openai-node/issues/286)) ([664e953](https://raw.githubusercontent.com/openai/openai-node/main/664e953))
* **readme:** add link to api.md ([#291](https://github.com/openai/openai-node/issues/291)) ([0d1cce2](https://raw.githubusercontent.com/openai/openai-node/main/0d1cce2))

## 4.4.0 (2023-09-01)

Full Changelog: [v4.3.1...v4.4.0](https://raw.githubusercontent.com/openai/openai-node/main/v4.3.1...v4.4.0)

### Features

* **package:** add Bun export map ([#269](https://github.com/openai/openai-node/issues/269)) ([16f239c](https://raw.githubusercontent.com/openai/openai-node/main/16f239c))
* re-export chat completion types at the top level ([#268](https://github.com/openai/openai-node/issues/268)) ([1a71a39](https://raw.githubusercontent.com/openai/openai-node/main/1a71a39))
* **tests:** unskip multipart form data tests ([#275](https://github.com/openai/openai-node/issues/275)) ([47d3e18](https://raw.githubusercontent.com/openai/openai-node/main/47d3e18))
* **types:** fix ambiguous auto-import for chat completions params ([#266](https://github.com/openai/openai-node/issues/266)) ([19c99fb](https://raw.githubusercontent.com/openai/openai-node/main/19c99fb))

### Bug Fixes

* revert import change which triggered circular import bug in webpack ([#274](https://github.com/openai/openai-node/issues/274)) ([6534e36](https://raw.githubusercontent.com/openai/openai-node/main/6534e36))

## 4.3.1 (2023-08-29)

Full Changelog: [v4.3.0...v4.3.1](https://raw.githubusercontent.com/openai/openai-node/main/v4.3.0...v4.3.1)

### Bug Fixes

* **types:** improve getNextPage() return type ([#262](https://github.com/openai/openai-node/issues/262)) ([245a984](https://raw.githubusercontent.com/openai/openai-node/main/245a984))

### Chores

* **ci:** setup workflows to create releases and release PRs ([#259](https://github.com/openai/openai-node/issues/259)) ([290908c](https://raw.githubusercontent.com/openai/openai-node/main/290908c))

## [4.3.0](https://raw.githubusercontent.com/openai/openai-node/main/4.3.0) (2023-08-27)

### Features

* **client:** add auto-pagination to fine tuning list endpoints ([#254](https://github.com/openai/openai-node/issues/254)) ([5f89c5e](https://raw.githubusercontent.com/openai/openai-node/main/5f89c5e))
* **cli:** rewrite in JS for better compatibility ([#244](https://github.com/openai/openai-node/issues/244)) ([d8d7c05](https://raw.githubusercontent.com/openai/openai-node/main/d8d7c05))

### Bug Fixes

* **stream:** declare Stream.controller as public ([#252](https://github.com/openai/openai-node/issues/252)) ([81e5de7](https://raw.githubusercontent.com/openai/openai-node/main/81e5de7))

### Documentation

* **readme:** mention Azure support ([#253](https://github.com/openai/openai-node/issues/253)) ([294727a](https://raw.githubusercontent.com/openai/openai-node/main/294727a))

### Chores

* **internal:** add helper method ([#255](https://github.com/openai/openai-node/issues/255)) ([6d8cff0](https://raw.githubusercontent.com/openai/openai-node/main/6d8cff0))

## [4.2.0](https://raw.githubusercontent.com/openai/openai-node/main/4.2.0) (2023-08-23)

### Features

* **types:** export RequestOptions type ([#240](https://github.com/openai/openai-node/issues/240)) ([ecf3bce](https://raw.githubusercontent.com/openai/openai-node/main/ecf3bce))

### Chores

* **internal:** export HeadersInit type shim ([#241](https://github.com/openai/openai-node/issues/241)) ([cf9f672](https://raw.githubusercontent.com/openai/openai-node/main/cf9f672))
