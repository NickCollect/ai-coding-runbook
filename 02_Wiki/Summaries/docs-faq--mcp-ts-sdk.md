---
type: summary
source: 01_Raw/github/modelcontextprotocol/typescript-sdk/docs/faq.md
source_url: https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/faq.md
title: "TS SDK FAQ"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

FAQ document with sections: General, Clients, Servers, v1 (legacy).

**Notable entry**: "Why do I see `TS2589: Type instantiation is excessively deep and possibly infinite` after upgrading the SDK?" — happens when upgrading to versions supporting Zod v4 (e.g., older `@modelcontextprotocol/sdk` → newer `@modelcontextprotocol/{client,server}`) AND your project ends up with multiple `zod` versions in the dependency tree. TypeScript hits recursion limits trying to instantiate cross-version types. **Fix**: run `npm ls zod` / `pnpm why zod` / `yarn why zod` to find duplicate `zod` versions; deduplicate via npm `overrides` / pnpm `overrides` / yarn resolutions. See issue #1180.

Other entries cover client troubleshooting, server troubleshooting, and v1 legacy migration questions.
