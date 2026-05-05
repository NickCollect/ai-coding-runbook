---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers
title: "Remote MCP servers"
summarized_at: 2026-05-05
entities_referenced: [MCP-server]
concepts_referenced: []
---

Short reference page describing third-party companies' deployed remote [[MCP-server]]s that developers can connect to via the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.

**Disclaimer.** Anthropic does not own, operate, or endorse the listed remote MCP servers. Users should only connect to remote MCP servers they trust and should review each server's security practices and terms before connecting.

**Connection flow:**
1. Review the documentation for the specific server you want to use.
2. Ensure you have the necessary authentication credentials.
3. Follow the server-specific connection instructions provided by each company.

For details on how to wire a remote MCP server into a request (the `mcp_servers` array, `mcp_toolset` configuration, OAuth tokens), the page redirects to the MCP connector docs.

**Server directory.** The page renders a `<MCPServersTable platform="mcpConnector" />` MDX component that dynamically displays the curated list of partner-deployed MCP servers known to work with the Anthropic MCP connector. The raw markdown does not enumerate the servers themselves (the table is populated at render time on the docs site).

**Where to find more.** A note links to [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) for "hundreds more MCP servers" beyond the curated remote-MCP-connector list.

This is one of the shortest pages in the docs; its function is essentially a directory entry pointing readers from the agents-and-tools section into (a) the MCP connector setup docs and (b) the MCP ecosystem repo. There are no code examples, no API parameters, and no specific server names enumerated in the markdown content.
