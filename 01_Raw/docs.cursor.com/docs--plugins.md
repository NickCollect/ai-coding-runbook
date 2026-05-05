---
source_url: https://cursor.com/docs/plugins
---

# Plugins

Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles. Browse official plugins in the [Cursor Marketplace](/marketplace). For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory). You can also [build your own](https://cursor.com/docs/plugins.md#creating-plugins) to share with other developers.

## What plugins contain

A plugin can bundle any combination of these components:

| Component       | Description                                                |
| :-------------- | :--------------------------------------------------------- |
| **Rules**       | Persistent AI guidance and coding standards (`.mdc` files) |
| **Skills**      | Specialized agent capabilities for complex tasks           |
| **Agents**      | Custom agent configurations and prompts                    |
| **Commands**    | Agent-executable command files                             |
| **MCP Servers** | Model Context Protocol integrations                        |
| **Hooks**       | Automation scripts triggered by events                     |

## The marketplace

The [Cursor Marketplace](/marketplace) is where you discover and install official plugins. Plugins are distributed as Git repositories and submitted through the Cursor team. Every plugin is [manually reviewed](https://cursor.com/help/security-and-privacy/marketplace-security.md) before it's listed. Browse official plugins at [cursor.com/marketplace](https://cursor.com/marketplace) or search by keyword in the marketplace panel. For community plugins and MCP servers, browse [cursor.directory](https://cursor.directory).

## Team marketplaces

Team marketplaces are available on Teams and Enterprise plans.

- Teams plan: up to 1 team marketplace
- Enterprise plan: unlimited team marketplaces

[Contact sales](https://cursor.com/contact-sales?source=docs-plugins) for unlimited team marketplaces and Enterprise admin controls.

The **Team Marketplaces** section appears below **Plugins** in dashboard settings.

On Enterprise plans, only admins can add team marketplaces from **Dashboard ->
Settings -> Plugins**.

### Required vs optional plugins

When you assign a plugin to a distribution group, you can set it as required or optional:

- **Required**: After you click **Save**, the plugin is installed automatically for everyone in that distribution group.
- **Optional**: The plugin is available to everyone in that distribution group, and each developer can choose whether to install it.

### How do distribution groups work with SCIM?

Distribution groups can be controlled with [SCIM](https://cursor.com/docs/account/teams/scim.md)-synced directory groups. If your organization uses SCIM, manage group membership in your identity provider, and Cursor will sync those group updates.

## Add a team marketplace

Use this flow to import a GitHub repository as a team marketplace:

1. Go to **Dashboard -> Settings -> Plugins**.
2. In **Team Marketplaces**, click **Import**.
3. Paste the GitHub repository URL and continue.
4. Review the parsed plugins. Optionally set Team Access groups, then continue.
5. Set the marketplace name and description, then save.

Example repository to try:

- [fieldsphere/cursor-team-marketplace-template](https://github.com/fieldsphere/cursor-team-marketplace-template)

## Where developers find team marketplaces

Developers can find team marketplaces in the marketplace panel in Cursor.

- Open the marketplace panel in Cursor.
- Look for plugins from your team marketplace.
- Install optional plugins directly from that panel.
- Required plugins are installed automatically when admins save the required setting for your distribution group.

## Installing plugins

Install plugins from the marketplace. Plugins can be scoped to a project or installed at the user level.

### MCP Apps deeplinks

Share MCP server configurations using install links:

```text
cursor://anysphere.cursor-deeplink/mcp/install?name=$NAME&config=$BASE64_ENCODED_CONFIG
```

See [MCP install links](https://cursor.com/docs/mcp/install-links.md) for details on generating these links.

## Managing installed plugins

### MCP servers

Toggle MCP servers on or off from Cursor Settings:

1. Open Settings (Cmd+Shift+J)
2. Go to **Features** > **Model Context Protocol**
3. Click the toggle next to any server

Disabled servers won't load or appear in chat.

### Rules and skills

Manage rules and skills from the Rules section of Cursor Settings. Toggle individual rules between **Always**, **Agent Decides**, and **Manual** modes. Skills appear in the **Agent Decides** section and can be invoked manually with `/skill-name` in chat.

## Using the Extension API

Extensions can register plugin directories programmatically, which is useful for distributing plugins bundled inside VS Code extensions or automating plugin setup.

### Extension API reference

Register plugin paths with `vscode.cursor.plugins.registerPath()`

## Creating plugins

A plugin is a directory with a `.cursor-plugin/plugin.json` manifest and your components (rules, skills, agents, commands, hooks, or MCP servers). Start from the [plugin template repository](https://github.com/cursor/plugin-template) or create one from scratch:

```text
my-plugin/
├── .cursor-plugin/
│   └── plugin.json
├── rules/
│   └── coding-standards.mdc
├── skills/
│   └── code-reviewer/
│       └── SKILL.md
└── mcp.json
```

The manifest only requires a `name` field. Components are discovered automatically from their default directories, or you can specify custom paths in the manifest.

```json
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

### Test plugins locally

Before you publish, load your plugin from `~/.cursor/plugins/local`:

1. Create a folder for your plugin:
   `~/.cursor/plugins/local/my-plugin`
2. Copy your plugin files into that folder. Make sure `.cursor-plugin/plugin.json` is at the plugin root.
3. Restart Cursor, or run **Developer: Reload Window**.
4. Verify your plugin components load in Cursor, such as rules, skills, or MCP servers.

For faster iteration, symlink your plugin repository:

```bash
ln -s /path/to/my-plugin ~/.cursor/plugins/local/my-plugin
```

When your plugin is ready, submit it for review at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish). For multi-plugin repositories, add a marketplace manifest at `.cursor-plugin/marketplace.json`.

See the [Plugins reference](https://cursor.com/docs/reference/plugins.md) for the full manifest schema, component formats, and submission checklist.

### Team and Enterprise marketplaces

Upgrade for private team marketplaces and organization-wide plugin distribution.

## FAQ

### Are marketplace plugins reviewed for security?

Yes. Every plugin is manually reviewed before it's listed. All plugins must be open source, and we review each update before publishing. See [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security.md) for details on vetting, update reviews, and how to report issues.

### How do I create a plugin?

Create a directory with a `.cursor-plugin/plugin.json` manifest file, add your rules, skills, agents, commands, or other components, and submit it to the Cursor team. See the [Plugins reference](https://cursor.com/docs/reference/plugins.md) for the full guide.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
