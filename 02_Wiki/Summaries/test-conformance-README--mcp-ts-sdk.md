---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/test/conformance/README.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/test/conformance/README.md
title: "TS SDK conformance tests README"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Conformance test implementations for the TypeScript MCP SDK.

**Client conformance tests** — test the SDK's client implementation against a conformance test server:
- `pnpm run test:conformance:client:all` — run all client tests
- `pnpm run test:conformance:client -- --suite auth` — specific suite
- `pnpm run test:conformance:client -- --scenario auth/basic-cimd` — single scenario

**Server conformance tests** — test the SDK's server implementation by running a conformance server. Used together with the cross-SDK conformance harness mandated by SEP-1730 (SDKs Tiering System) — Tier 1 SDKs must pass 100% of conformance tests.
