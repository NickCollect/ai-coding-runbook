---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/SECURITY.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md
title: "MCP security policy and trust model"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Defines the MCP project's vulnerability disclosure process **and** an explicit trust model documenting which behaviors are intentional design choices (and therefore NOT vulnerabilities). Important context for security researchers.

**Reporting**: use GitHub Security Advisory process for the repo; do NOT use public issues/discussions/PRs. Include description, repro steps, potential impact, optional suggested fixes.

**Trust model assumptions**:
1. **MCP clients trust MCP servers they connect to** — security depends on user/admin server selection.
2. **Local MCP servers are trusted like any other software you install** — evaluate trustworthiness before running, just like a library.
3. **MCP servers trust their execution environment** — by design they need access to local files, DBs, APIs.
4. **Users/admins are responsible for server selection** — clients should surface capabilities; the connect decision rests with the user.

**Behaviors explicitly NOT considered vulnerabilities** (and therefore not eligible for security reports):

- **Command execution for STDIO transport** — clients launch servers by executing commands; process spawning is core to STDIO. Server runs with client privileges. Reports about "arbitrary command execution via STDIO config" are not vulnerabilities.
- **Server capabilities and side effects** — file system access (read/write), git operations (including reset/force push), database queries/modifications, network/API calls, system commands. If a server's documented purpose is action Y, "server X can perform Y" is not a vulnerability. Permissioning is the operator's responsibility.
- **Resource access patterns** — exposing file contents, DB results, API responses to clients is the design intent. Scope is determined by server implementation/config.
- **LLM-driven tool invocation** — the LLM may invoke tools the user did not explicitly request, may chain multiple tools, may interpret intent unexpectedly. These are LLM/application-level concerns, not MCP vulnerabilities.

**Developer/operator responsibilities** spelled out for server developers (access controls, doc, input validation, least privilege), client developers (capability surfacing, consent UX, displaying invocations, sandboxing where feasible), operators/users (only trust trusted servers, review configs, understand capabilities, restrict access).

**What IS in scope for vulnerability reports**: protocol-level flaws in the MCP spec; auth/authz bypasses; SDK implementation bugs (buffer overflow, injection, etc.); sandbox escapes from explicitly-defined isolation; session hijacking; token theft/leakage; cross-tenant access in multi-tenant deployments. List is not exhaustive.

**Reporting evaluation guidance**: check this doc first; consider the trust model (does the issue assume access the model already grants?); focus on unexpected access; explain how the report violates intended security boundaries.

Links to the Security Best Practices in the spec for additional guidance.
