---
title: Introducing the MCP Registry
date: "2025-09-08T00:00:00Z"
description: "Launching the MCP Registry in preview: an open catalog and API for discovering publicly available MCP servers."
author:
  - David Soria Parra (Lead Maintainer)
  - Adam Jones (Registry Maintainer)
  - Tadas Antanavicius (Registry Maintainer)
  - Toby Padilla (Registry Maintainer)
  - Theodora Chu (MCP PM at Anthropic)
tags:
  - announcement
  - community
---

Today, we're launching the Model Context Protocol (MCP) Registry—an open catalog and API for publicly available MCP servers to improve discoverability and implementation. By standardizing how servers are distributed and discovered, we’re expanding their reach while making it easier for clients to get connected.

The MCP Registry is now available in preview. To get started:

- **Add your server** by following our guide on [Adding Servers to the MCP Registry](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Adding Servers to the MCP Registry) (for server maintainers)
- **Access server data** by following our guide on [Accessing MCP Registry Data](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Accessing MCP Registry Data) (for client maintainers)

# Single source of truth for MCP servers

In March 2025, we shared that we wanted to build a central registry for the MCP ecosystem. Today we are announcing that we’ve launched [https://registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io) as the official MCP Registry. As part of the MCP project, the MCP Registry, as well as a parent [OpenAPI specification](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/OpenAPI specification), are open source—allowing everyone to build a compatible sub-registry.

Our goal is to standardize how servers are distributed and discovered, providing a primary source of truth that sub-registries can build upon. In turn, this will expand server reach and help clients find servers more easily across the MCP ecosystem.

## Public and private sub-registries

In building a central registry, it was important to us not to take away from existing registries that the community and companies have built. The MCP Registry serves as a primary source of truth for publicly available MCP servers, and organizations can choose to [create sub-registries](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/create sub-registries) based on custom criteria. For example:

**Public subregistries** like opinionated “MCP marketplaces” associated with each MCP client are free to augment and enhance data they ingest from the upstream MCP Registry. Every MCP end-user persona will have different needs, and it is up to the MCP client marketplaces to properly serve their end-users in opinionated ways.

**Private subregistries** will exist within enterprises that have strict privacy and security requirements, but the MCP Registry gives these enterprises a single upstream data source they can build upon. At a minimum, we aim to share API schemas with these private implementations so that associated SDKs and tooling can be shared across the ecosystem.

In both cases, the MCP Registry is the starting point – it’s the centralized location where MCP server maintainers publish and maintain their self-reported information for these downstream consumers to massage and deliver to their end-users.

## Community-driven mechanism for moderation

The MCP Registry is an official MCP project maintained by the registry working group and permissively licensed. Community members can submit issues to flag servers that violate the MCP [moderation guidelines](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/moderation guidelines)—such as those containing spam, malicious code, or impersonating legitimate services. Registry maintainers can then denylist these entries and retroactively remove them from public access.

# Getting started

To get started:

- **Add your server** by following our guide on [Adding Servers to the MCP Registry](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Adding Servers to the MCP Registry) (for server maintainers)
- **Access server data** by following our guide on [Accessing MCP Registry Data](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Accessing MCP Registry Data) (for client maintainers)

This preview of the MCP Registry is meant to help us improve the user experience before general availability and does not provide data durability guarantees or other warranties. We advise MCP adopters to watch development closely as breaking changes may occur before the registry is made generally available.

As we continue to develop the registry, we encourage feedback and contributions on the [modelcontextprotocol/registry GitHub repository](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/modelcontextprotocol/registry GitHub repository): Discussion, Issues, and Pull Requests are all welcome.

# Thanks to the MCP community

The MCP Registry has been a collaborative effort from the beginning and we are incredibly grateful for the enthusiasm and support from the broader developer community.

In February 2025, it began as a grassroots project when MCP creators [David Soria Parra](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/David Soria Parra) and [Justin Spahr-Summers](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Justin Spahr-Summers) asked the [PulseMCP](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/PulseMCP) and [Goose](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Goose) teams to help build a centralized community registry. Registry Maintainer [Tadas Antanavicius](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Tadas Antanavicius) from [PulseMCP](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/PulseMCP) spearheaded the initial effort in collaboration with [Alex Hancock](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Alex Hancock) from [Block](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Block). They were soon joined by Registry Maintainer [Toby Padilla](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Toby Padilla), Head of MCP at [GitHub](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/GitHub), and more recently, [Adam Jones](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Adam Jones) from [Anthropic](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Anthropic) joined as Registry Maintainer to drive the project towards the launch today. The [initial announcement](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/initial announcement) of the MCP Registry's development lists 16 contributing individuals from at least 9 different companies.

Many others made crucial contributions to bring this project to life: [Radoslav Dimitrov](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Radoslav Dimitrov) from [Stacklok](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Stacklok), [Avinash Sridhar](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Avinash Sridhar) from [GitHub](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/GitHub), [Connor Peet](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Connor Peet) from [VS Code](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/VS Code), [Joel Verhagen](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Joel Verhagen) from [NuGet](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/NuGet), [Preeti Dewani](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Preeti Dewani) from [Last9](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Last9), [Avish Porwal](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Avish Porwal) from [Microsoft](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Microsoft), [Jonathan Hefner](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Jonathan Hefner), and many Anthropic and GitHub employees that provided code reviews and development support. We are also grateful to everyone on the [Registry's contributors log](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/Registry's contributors log) and those who participated in [discussions and issues](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/blog/content/posts/discussions and issues).

We deeply appreciate everyone investing in this foundational open source infrastructure. Together, we're helping developers and organizations worldwide to build more reliable, context-aware AI applications. On behalf of the MCP community, thank you.
