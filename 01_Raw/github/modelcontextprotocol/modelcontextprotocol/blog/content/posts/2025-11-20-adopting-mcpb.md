---
title: Adopting the MCP Bundle format (.mcpb) for portable local servers
date: "2025-11-21T00:00:00+00:00"
publishDate: "2025-11-21T00:00:00+00:00"
description: The MCP Bundle format (.mcpb) joins the MCP project, enabling one-click installation of local servers across any compatible client.
author:
  - David Soria Parra (MCP Lead Maintainer)
  - Joan Xie (MCPB Maintainer)
tags:
  - mcp
  - mcpb
  - bundles
---

The [MCP Bundle format](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/MCP Bundle format) (MCPB) is now part of the [Model Context Protocol project](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Model Context Protocol project). This distribution format simplifies how developers package and share local MCP servers, enabling users to install them across any compatible client, including the [Claude desktop app](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Claude desktop app), [Claude Code](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Claude Code), and [MCP for Windows](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/MCP for Windows).

## What are MCP Bundles?

MCP Bundles are ZIP archives containing a local MCP server and a `manifest.json` that describes the server and its capabilities. The format is similar to Chrome extensions (`.crx`) or VS Code extensions (`.vsix`), enabling end users to install local MCP servers with a single click.

A basic bundle structure looks like:

```text
bundle.mcpb (ZIP file)
├── manifest.json      # Required: Bundle metadata and configuration
├── server/            # Server implementation
│   └── index.js
├── node_modules/      # Bundled dependencies
└── icon.png           # Optional: Bundle icon
```

The format supports servers written in Node.js, Python, or compiled binaries, giving developers flexibility in how they build their integrations, while maintaining a consistent distribution mechanism for users.

## Why move MCPB to the MCP project?

Anthropic originally developed MCPB (previously called DXT) for Claude's desktop applications. However, we believe the local MCP server ecosystem benefits when portability extends beyond any single client. By moving the [bundle specification](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/bundle specification), [CLI tooling](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/CLI tooling), and [reference implementation](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/reference implementation) to the MCP project, we're enabling:

- **Cross-client compatibility:** A bundle created for one MCP-compatible application should work in any other that implements the specification. Developers can distribute their work once and reach users across the ecosystem.
- **Ecosystem-wide tooling:** The `mcpb` CLI and associated libraries are now open for the community to extend, improve, and build upon. Client developers can adopt standardized code for loading and verifying bundles.
- **User-friendly installation:** End users benefit from a consistent installation experience regardless of which AI application they prefer. Configuration variables, permissions, and updates can be handled uniformly.
- **Shared community:** MCPB contributors can now collaborate in the open with the rest of the [MCP community](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/MCP community).

## What this means for developers

This transition is mostly a logistical change, but also brings some benefits to implementers. For those that are building:

- **Servers:** You can use MCPB to package your local MCP servers for distribution across multiple clients. The `mcpb` CLI helps you create a `manifest.json` and package your server into a `.mcpb` file. Once packaged, users can install your server with a single click in any client that supports MCP Bundles.
- **Clients:** You can add support for MCP Bundles to your application using the open source toolchain. [The repository](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/The repository) includes the schemas and key functions used by Claude for macOS and Windows to implement bundle support, which you can adapt for your own client.

## Getting started

Check out the repo to get started: [modelcontextprotocol/mcpb](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/modelcontextprotocol/mcpb). We encourage [feedback](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/feedback) and contributions!

## Acknowledgements

Thanks to the MCP contributors and maintainers involved in making this happen, including:

- [David Soria Parra](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/David Soria Parra) (_MCP Lead Maintainer_)
- [Adam Jones](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Adam Jones) (_MCP Maintainer_)
- [Joan Xie](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Joan Xie) (_MCPB Maintainer_)
- [Felix Rieseberg](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Felix Rieseberg) (_MCPB Maintainer_)
- [Alex Sklar](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Alex Sklar) (_MCPB Maintainer_)
