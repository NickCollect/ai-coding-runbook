# Model Context Protocol servers

This repository is a collection of *reference implementations* for the [Model Context Protocol](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Model Context Protocol) (MCP), as well as references to community-built servers and additional resources.

> [!IMPORTANT]
> If you are looking for a list of MCP servers, you can browse published servers on [the MCP Registry](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/the MCP Registry). The repository served by this README is dedicated to housing just the small number of reference servers maintained by the MCP steering group.

> [!WARNING]
> The servers in this repository are intended as **reference implementations** to demonstrate MCP features and SDK usage. They are meant to serve as educational examples for developers building their own MCP servers, not as production-ready solutions. Developers should evaluate their own security requirements and implement appropriate safeguards based on their specific threat model and use case.

The servers in this repository showcase the versatility and extensibility of MCP, demonstrating how it can be used to give Large Language Models (LLMs) secure, controlled access to tools and data sources.
Typically, each MCP server is implemented with an MCP SDK:

- [C# MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/C# MCP SDK)
- [Go MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Go MCP SDK)
- [Java MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Java MCP SDK)
- [Kotlin MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Kotlin MCP SDK)
- [PHP MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PHP MCP SDK)
- [Python MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Python MCP SDK)
- [Ruby MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Ruby MCP SDK)
- [Rust MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Rust MCP SDK)
- [Swift MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Swift MCP SDK)
- [TypeScript MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/TypeScript MCP SDK)

## 🌟 Reference Servers

These servers aim to demonstrate MCP features and the official SDKs.

- **[Everything](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Everything)** - Reference / test server with prompts, resources, and tools.
- **[Fetch](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Fetch)** - Web content fetching and conversion for efficient LLM usage.
- **[Filesystem](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Filesystem)** - Secure file operations with configurable access controls.
- **[Git](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Git)** - Tools to read, search, and manipulate Git repositories.
- **[Memory](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Memory)** - Knowledge graph-based persistent memory system.
- **[Sequential Thinking](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Sequential Thinking)** - Dynamic and reflective problem-solving through thought sequences.
- **[Time](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Time)** - Time and timezone conversion capabilities.

### Archived

The following reference servers are now archived and can be found at [servers-archived](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/servers-archived).

- **[AWS KB Retrieval](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/AWS KB Retrieval)** - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime.
- **[Brave Search](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Brave Search)** - Web and local search using Brave's Search API.  Has been replaced by the [official server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/official server).
- **[EverArt](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/EverArt)** - AI image generation using various models.
- **[GitHub](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/GitHub)** - Repository management, file operations, and GitHub API integration.
- **[GitLab](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/GitLab)** - GitLab API, enabling project management.
- **[Google Drive](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Google Drive)** - File access and search capabilities for Google Drive.
- **[Google Maps](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Google Maps)** - Location services, directions, and place details.
- **[PostgreSQL](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PostgreSQL)** - Read-only database access with schema inspection.
- **[Puppeteer](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Puppeteer)** - Browser automation and web scraping.
- **[Redis](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Redis)** - Interact with Redis key-value stores.
- **[Sentry](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Sentry)** - Retrieving and analyzing issues from Sentry.io.
- **[Slack](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Slack)** - Channel management and messaging capabilities. Now maintained by [Zencoder](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Zencoder)
- **[SQLite](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/SQLite)** - Database interaction and business intelligence capabilities.

## 📚 Frameworks

These are high-level frameworks that make it easier to build MCP servers or clients.

### For servers

* **[Anubis MCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Anubis MCP)** (Elixir) - A high-performance and high-level Model Context Protocol (MCP) implementation in Elixir. Think like "Live View" for MCP.
* **[ModelFetch](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/ModelFetch)** (TypeScript) - Runtime-agnostic SDK to create and deploy MCP servers anywhere TypeScript/JavaScript runs
* **[EasyMCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/EasyMCP)** (TypeScript)
* **[FastAPI to MCP auto generator](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/FastAPI to MCP auto generator)** – A zero-configuration tool for automatically exposing FastAPI endpoints as MCP tools by **[Tadata](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Tadata)**
* **[FastMCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/FastMCP)** (TypeScript)
* **[Foobara MCP Connector](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Foobara MCP Connector)** - Easily expose Foobara commands written in Ruby as tools via MCP
* **[Foxy Contexts](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Foxy Contexts)** – A library to build MCP servers in Golang by **[strowk](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/strowk)**
* **[Higress MCP Server Hosting](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Higress MCP Server Hosting)** - A solution for hosting MCP Servers by extending the API Gateway (based on Envoy) with wasm plugins.
* **[MCP Declarative Java SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Declarative Java SDK)** Annotation-driven MCP servers development with Java, no Spring Framework Required, minimize dependencies as much as possible.
* **[MCP-Framework](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP-Framework)** Build MCP servers with elegance and speed in TypeScript. Comes with a CLI to create your project with `mcp create app`. Get started with your first server in under 5 minutes by **[Alex Andru](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Alex Andru)**
* **[MCP Plexus](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Plexus)**: A secure, **multi-tenant** and Multi-user MCP python server framework built to integrate easily with external services via OAuth 2.1, offering scalable and robust solutions for managing complex AI applications.
* **[mcp_sse (Elixir)](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp_sse (Elixir))** An SSE implementation in Elixir for rapidly creating MCP servers.
* **[mxcp](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mxcp)** (Python) - Open-source framework for building enterprise-grade MCP servers using just YAML, SQL, and Python, with built-in auth, monitoring, ETL and policy enforcement.
* **[Next.js MCP Server Template](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Next.js MCP Server Template)** (Typescript) - A starter Next.js project that uses the MCP Adapter to allow MCP clients to connect and access resources.
* **[PayMCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PayMCP)** (Python & TypeScript) - Lightweight payments layer for MCP servers: turn tools into paid endpoints with a two-line decorator. [PyPI](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PyPI) · [npm](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/npm) · [TS repo](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/TS repo)
* **[Perl SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Perl SDK)** - An SDK for building MCP servers and clients with the Perl programming language.
* **[Quarkus MCP Server SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Quarkus MCP Server SDK)** (Java)
- **[R mcptools](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/R mcptools)** - An R SDK for creating R-based MCP servers and retrieving functionality from third-party MCP servers as R functions.
* **[SAP ABAP MCP Server SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/SAP ABAP MCP Server SDK)** - Build SAP ABAP based MCP servers. ABAP 7.52 based with 7.02 downport; runs on R/3 & S/4HANA on-premises, currently not cloud-ready.
* **[Spring AI MCP Server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Spring AI MCP Server)** - Provides auto-configuration for setting up an MCP server in Spring Boot applications.
* **[Template MCP Server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Template MCP Server)** - A CLI tool to create a new Model Context Protocol server project with TypeScript support, dual transport options, and an extensible structure
* **[AgentR Universal MCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/AgentR Universal MCP SDK)** - A python SDK to build MCP Servers with inbuilt credential management by **[Agentr](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Agentr)**
* **[Vercel MCP Adapter](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Vercel MCP Adapter)** (TypeScript) - A simple package to start serving an MCP server on most major JS meta-frameworks including Next, Nuxt, Svelte, and more.
* **[PHP MCP Server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PHP MCP Server)** (PHP) - Core PHP implementation for the Model Context Protocol (MCP) server

### For clients

* **[codemirror-mcp](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/codemirror-mcp)** - CodeMirror extension that implements the Model Context Protocol (MCP) for resource mentions and prompt commands
* **[llm-analysis-assistant](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/llm-analysis-assistant)** <img height="12" width="12" src="https://raw.githubusercontent.com/xuzexin-hz/llm-analysis-assistant/refs/heads/main/src/llm_analysis_assistant/pages/html/imgs/favicon.ico" alt="Langfuse Logo" /> - A very streamlined mcp client that supports calling and monitoring stdio/sse/streamableHttp, and can also view request responses through the /logs page. It also supports monitoring and simulation of ollama/openai interface.
* **[MCP-Agent](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP-Agent)** - A simple, composable framework to build agents using Model Context Protocol by **[LastMile AI](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/LastMile AI)**
* **[Spring AI MCP Client](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Spring AI MCP Client)** - Provides auto-configuration for MCP client functionality in Spring Boot applications.
* **[MCP CLI Client](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP CLI Client)** - A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).
* **[OpenMCP Client](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/OpenMCP Client)** - An all-in-one vscode/trae/cursor plugin for MCP server debugging. [Document](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Document) & [OpenMCP SDK](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/OpenMCP SDK).
* **[PHP MCP Client](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PHP MCP Client)** - Core PHP implementation for the Model Context Protocol (MCP) Client
* **[Runbear](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Runbear)** - No-code MCP client for team chat platforms, such as Slack, Microsoft Teams, and Discord.

## 📚 Resources

Additional resources on MCP.

- **[A2A-MCP Java Bridge](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/A2A-MCP Java Bridge)** - A2AJava brings powerful A2A-MCP integration directly into your Java applications. It enables developers to annotate standard Java methods and instantly expose them as MCP Server, A2A-discoverable actions — with no boilerplate or service registration overhead.
- **[AiMCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/AiMCP)** - A collection of MCP clients&servers to find the right mcp tools by **[Hekmon](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Hekmon)**
- **[Awesome Crypto MCP Servers by badkk](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Awesome Crypto MCP Servers by badkk)** - A curated list of MCP servers by **[Luke Fan](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Luke Fan)**
- **[Awesome MCP Servers by appcypher](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Awesome MCP Servers by appcypher)** - A curated list of MCP servers by **[Stephen Akinyemi](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Stephen Akinyemi)**
- **[Awesome MCP Servers by punkpeye](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Awesome MCP Servers by punkpeye)** (**[website](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/website)**) - A curated list of MCP servers by **[Frank Fiegel](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Frank Fiegel)**
- **[Awesome MCP Servers by wong2](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Awesome MCP Servers by wong2)** (**[website](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/website)**) - A curated list of MCP servers by **[wong2](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/wong2)**
- **[Awesome Remote MCP Servers by JAW9C](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Awesome Remote MCP Servers by JAW9C)** - A curated list of **remote** MCP servers, including their authentication support by **[JAW9C](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/JAW9C)**
- **[Discord Server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Discord Server)** – A community discord server dedicated to MCP by **[Frank Fiegel](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Frank Fiegel)**
- **[Install This MCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Install This MCP)** - Reduce Installation Friction with beautiful installation guides
- <img height="12" width="12" src="https://raw.githubusercontent.com/klavis-ai/klavis/main/static/klavis-ai.png" alt="Klavis Logo" /> **[Klavis AI](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Klavis AI)** - Open Source MCP Infra. Hosted MCP servers and MCP clients on Slack and Discord.
- **[MCP Badges](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Badges)** – Quickly highlight your MCP project with clear, eye-catching badges, by **[Ironben](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Ironben)**
- <img height="12" width="12" src="https://mcpproxy.app/favicon.svg" alt="MCPProxy Logo" /> **[MCPProxy](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPProxy)** - Open-source local app that enables access to multiple MCP servers and thousands of tools with intelligent discovery via MCP protocol, runs servers in isolated environments, and features automatic quarantine protection against malicious tools.
- **[MCPRepository.com](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPRepository.com)** - A repository that indexes and organizes all MCP servers for easy discovery.
- **[mcp-cli](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp-cli)** - A CLI inspector for the Model Context Protocol by **[wong2](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/wong2)**
- **[mcp-dockmaster](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp-dockmaster)** - An Open-Sourced UI to install and manage MCP servers for Windows, Linux and macOS.
- **[mcp-get](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp-get)** - Command line tool for installing and managing MCP servers by **[Michael Latman](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Michael Latman)**
- **[mcp-guardian](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp-guardian)** - GUI application + tools for proxying / managing control of MCP servers by **[EQTY Lab](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/EQTY Lab)**
- **[MCP Linker](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Linker)** - A cross-platform Tauri GUI tool for one-click setup and management of MCP servers, supporting Claude Desktop, Cursor, Windsurf, VS Code, Cline, and Neovim.
- **[mcp-manager](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp-manager)** - Simple Web UI to install and manage MCP servers for Claude Desktop by **[Zue](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Zue)**
- **[MCP Marketplace Web Plugin](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Marketplace Web Plugin)** MCP Marketplace is a small Web UX plugin to integrate with AI applications, Support various MCP Server API Endpoint (e.g pulsemcp.com/deepnlp.org and more). Allowing user to browse, paginate and select various MCP servers by different categories. [Pypi](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Pypi) | [Maintainer](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Maintainer) | [Website](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Website)
- **[mcp.natoma.ai](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp.natoma.ai)** – A Hosted MCP Platform to discover, install, manage and deploy MCP servers by **[Natoma Labs](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Natoma Labs)**
- **[mcp.run](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcp.run)** - A hosted registry and control plane to install & run secure + portable MCP Servers.
- **[MCPHub](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPHub)** - Website to list high quality MCP servers and reviews by real users. Also provide online chatbot for popular LLM models with MCP server support.
- **[MCP Router](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Router)** – Free Windows and macOS app that simplifies MCP management while providing seamless app authentication and powerful log visualization by **[MCP Router](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Router)**
- **[MCP Servers Hub](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Servers Hub)** (**[website](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/website)**) - A curated list of MCP servers by **[apappascs](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/apappascs)**
- **[MCPServers.com](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPServers.com)** - A growing directory of high-quality MCP servers with clear setup guides for a variety of MCP clients. Built by the team behind the **[Highlight MCP client](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Highlight MCP client)**
- **[MCP Servers Rating and User Reviews](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Servers Rating and User Reviews)** - Website to rate MCP servers, write authentic user reviews, and [search engine for agent & mcp](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/search engine for agent & mcp)
- **[MCP Sky](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Sky)** - Bluesky feed for MCP related news and discussion by **[@brianell.in](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/@brianell.in)**
- **[MCP X Community](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP X Community)** – A X community for MCP by **[Xiaoyi](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Xiaoyi)**
- **[MCPHub](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPHub)** – An Open Source macOS & Windows GUI Desktop app for discovering, installing and managing MCP servers by **[Jeamee](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Jeamee)**
- **[mcpm](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcpm)** ([website](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/website)) - MCP Manager (MCPM) is a Homebrew-like service for managing Model Context Protocol (MCP) servers across clients by **[Pathintegral](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Pathintegral)**
- **[MCPVerse](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPVerse)** - A portal for creating & hosting authenticated MCP servers and connecting to them securely.
- **[MCP Servers Search](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Servers Search)** - An MCP server that provides tools for querying and discovering available MCP servers from this list.
- **[Search MCP Server](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Search MCP Server)** - Recommends the most relevant MCP servers based on the client's query by searching this README file.
- **[MCPWatch](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCPWatch)** - A comprehensive security scanner for Model Context Protocol (MCP) servers that detects vulnerabilities and security issues in your MCP server implementations.
- <img height="12" width="12" src="https://mkinf.io/favicon-lilac.png" alt="mkinf Logo" /> **[mkinf](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mkinf)** - An Open Source registry of hosted MCP Servers to accelerate AI agent workflows.
- **[Open-Sourced MCP Servers Directory](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Open-Sourced MCP Servers Directory)** - A curated list of MCP servers by **[mcpso](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/mcpso)**
- <img height="12" width="12" src="https://opentools.com/favicon.ico" alt="OpenTools Logo" /> **[OpenTools](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/OpenTools)** - An open registry for finding, installing, and building with MCP servers by **[opentoolsteam](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/opentoolsteam)**
- **[Programmatic MCP Prototype](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Programmatic MCP Prototype)** - Experimental agent prototype demonstrating programmatic MCP tool composition, progressive tool discovery, state persistence, and skill building through TypeScript code execution by **[Adam Jones](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Adam Jones)**
- **[PulseMCP](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/PulseMCP)** ([API](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/API)) - Community hub & weekly newsletter for discovering MCP servers, clients, articles, and news by **[Tadas Antanavicius](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Tadas Antanavicius)**, **[Mike Coughlin](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Mike Coughlin)**, and **[Ravina Patel](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Ravina Patel)**
- **[r/mcp](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/r/mcp)** – A Reddit community dedicated to MCP by **[Frank Fiegel](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Frank Fiegel)**
- **[MCP.ing](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP.ing)** - A list of MCP services for discovering MCP servers in the community and providing a convenient search function for MCP services by **[iiiusky](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/iiiusky)**
- **[MCP Hunt](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/MCP Hunt)** - Realtime platform for discovering trending MCP servers with momentum tracking, upvoting, and community discussions - like Product Hunt meets Reddit for MCP
- **[Smithery](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Smithery)** - A registry of MCP servers to find the right tools for your LLM agents by **[Henry Mao](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Henry Mao)**
- **[Toolbase](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Toolbase)** - Desktop application that manages tools and MCP servers with just a few clicks - no coding required by **[gching](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/gching)**
- **[ToolHive](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/ToolHive)** - A lightweight utility designed to simplify the deployment and management of MCP servers, ensuring ease of use, consistency, and security through containerization by **[StacklokLabs](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/StacklokLabs)**
- **[NetMind](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/NetMind)** - Access powerful AI services via simple APIs or MCP servers to supercharge your productivity.
- **[Webrix MCP Gateway](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Webrix MCP Gateway)** - Enterprise MCP gateway with SSO, RBAC, audit trails, and token vaults for secure, centralized AI agent access control. Deploy via Helm charts on-premise or in your cloud. [webrix.ai](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/webrix.ai)

## 🚀 Getting Started

### Using MCP Servers in this Repository
TypeScript-based servers in this repository can be used directly with `npx`.

For example, this will start the [Memory](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Memory) server:
```sh
npx -y @modelcontextprotocol/server-memory
```

Python-based servers in this repository can be used directly with [`uvx`](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/`uvx`) or [`pip`](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/`pip`). `uvx` is recommended for ease of use and setup.

For example, this will start the [Git](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/Git) server:
```sh
# With uvx
uvx mcp-server-git

# With pip
pip install mcp-server-git
python -m mcp_server_git
```

Follow [these](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/these) instructions to install `uv` / `uvx` and [these](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/these) to install `pip`.

### Using an MCP Client
However, running a server on its own isn't very useful, and should instead be configured into an MCP client. For example, here's the Claude Desktop configuration to use the above server:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

On Windows, wrap `npx` with `cmd /c`:

```json
{
  "mcpServers": {
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

Additional examples of using the Claude Desktop as an MCP client might look like:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "path/to/git/repo"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

On Windows, apply the same wrapper to each `npx`-based entry above by changing `"command"` to `"cmd"` and prepending `"/c", "npx"` to the existing `args`. Leave `uvx` entries unchanged.

## 🛠️ Creating Your Own Server

Interested in creating your own MCP server? Visit the official documentation at [modelcontextprotocol.io](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/modelcontextprotocol.io) for comprehensive guides, best practices, and technical details on implementing MCP servers.

## 🤝 Contributing

See [CONTRIBUTING.md](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/CONTRIBUTING.md) for information about contributing to this repository.

## 🔒 Security

See [SECURITY.md](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/SECURITY.md) for reporting security vulnerabilities.

## 📜 License

This project is licensed under the Apache License, Version 2.0 for new contributions, with existing code under MIT - see the [LICENSE](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/LICENSE) file for details.

## 💬 Community

- [GitHub Discussions](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/GitHub Discussions)

## ⭐ Support

If you find MCP servers useful, please consider starring the repository and contributing new servers or improvements!

---

Managed by Anthropic, but built together with the community. The Model Context Protocol is open source and we encourage everyone to contribute their own servers and improvements!
