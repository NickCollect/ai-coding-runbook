---
type: summary
source: 01_Raw/github/modelcontextprotocol/modelcontextprotocol/seps/1024-mcp-client-security-requirements-for-local-server-.md
source_url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/1024-mcp-client-security-requirements-for-local-server-.md
title: "SEP-1024: MCP Client Security Requirements for Local Server Installation"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

**Status: Final | Type: Standards Track | Created: 2025-07-22 | Author: Den Delimarsky**

Addresses critical client-side security gaps in MCP clients that support **one-click** installation of local MCP servers. Without this SEP, clients can silently execute arbitrary commands embedded in MCP server configurations distributed via links or social engineering — creating data exfiltration, system compromise, and privilege escalation vectors.

**Mandatory client requirement**: MCP clients supporting one-click local server configuration **MUST**:

1. Display a clear consent dialog showing:
   - The exact command that will be executed (without truncation)
   - All arguments and parameters
   - A clear warning that the operation may be dangerous
2. Require explicit user approval (button click, checkbox, etc.)
3. Provide a cancel option
4. Not proceed without consent

VS Code and Cursor already implement consent dialogs along these lines.

**Backward compatibility**: addresses client behavior, not the wire protocol — existing MCP servers and protocol unchanged; clients update local-install flows to comply; users see consent dialogs on new flows; existing installed servers continue working normally.

**Security**: addresses arbitrary code execution, social engineering, supply-chain attacks, privilege escalation. Residual risks (user override, sophisticated obfuscation, implementation gaps) mitigated via clear warning language, recommended additional layers (sandboxing, signatures), ongoing security research.

Adopted in the November 2025 spec release.
