---
source_url: https://cursor.com/docs/integrations/tailscale
fetched_at: 2026-11-02T07:00:23.690013+00:00
fetch_method: mintlify_md
---

# Tailscale

The Tailscale integration lets [Rollouts](https://cursor.com/docs/rollouts.md) reach [MCP](https://cursor.com/docs/mcp.md) servers that are only reachable on your tailnet. Cursor joins your tailnet as a tagged, ephemeral device and connects to the servers your tailnet policy allows.

Remote MCP servers that use `https` can use a connection. A stdio server runs on the machine that starts it, so it has no tailnet address for Cursor to dial. [Grok Bot](https://cursor.com/docs/grok-bot/private-networks.md) reaches private networks through a separate setup.

Tailscale is in beta on Teams and Enterprise plans. [Contact sales](https://cursor.com/contact-sales?source=docs-tailscale)
to ask for it to be enabled for your team.

## Set up your tailnet

Edit the tailnet policy and create the OAuth client in the [Tailscale admin console](https://login.tailscale.com/admin).

### Pick a tag for Cursor

Cursor uses `tag:cursor` unless you choose another. Add that tag to
`tagOwners`.

### Create an OAuth client

Give it the `auth_keys` scope and let it assign the Cursor tag. Cursor
uses the client to mint a short-lived key each time it connects.

### Allow the tag to reach your MCP server

Add one rule from the Cursor tag to your MCP server's tag and port. Grant
the access Cursor needs. It doesn't need subnet routes, an exit node, or
`autogroup:internet`.

```json
{
  "tagOwners": {
    "tag:cursor": ["autogroup:admin"],
    "tag:mcp": ["autogroup:admin"]
  },
  "acls": [
    { "action": "accept", "src": ["tag:cursor"], "dst": ["tag:mcp:443"] }
  ]
}
```

The MCP server must serve `https` with a certificate for the hostname in its URL, because Cursor's TLS connection ends at your server. On a MagicDNS name, `tailscale serve --https=443` provides that certificate.

You can paste an auth key instead of an OAuth client. Make it reusable,
ephemeral, pre-approved, and tagged with the Cursor tag, because Cursor
starts a new device whenever it needs one. An OAuth client is the
recommended choice.

## Add the connection in Cursor

You need permission to manage your team's MCP servers.

### Open Tailscale

Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations?view=tailscale)
and select **Manage** next to Tailscale.

### Add a connection

Select **Add Connection**. Enter a **Display Name** and your **Tailnet
Name** (for example `acme.ts.net`). Set **Tag** to the tag from your
policy. It must start with `tag:`.

### Add the credential

Choose **OAuth Client** and enter the client ID and secret, or choose
**Auth Key** and paste a key. Secrets are write-only. To change a secret,
replace it.

### Save the connection

Select **Add Connection**.

A team can have two Tailscale connections.

## Choose the connection for an MCP server

Open the MCP server in Rollouts. Under **Transport** ("Choose a private link, or keep the public path"), choose your connection. **No connection** keeps the public path.

Deleting a connection makes every server that uses it fail closed until you
choose a transport again. Those servers don't fall back to the public
internet.

## How Cursor joins your tailnet

- **Ephemeral devices.** With an OAuth client, Cursor mints a single-use, pre-approved, ephemeral key that expires in 10 minutes. Cursor never stores the minted key. The device logs out after 15 minutes with no open connection.
- **Random device names.** Each device is named `cursor-external-tsnet-proxy-` plus a random suffix. Expect a new name each time, and more than one device online at once.
- **Your policy is the access control.** Cursor reaches only what the Cursor tag can reach. Each server is pinned to the host and port in its URL. A URL with no port uses `443`.
- **Write-only credentials.** Cursor encrypts the client secret or auth key before storing it and never shows it again.

## Troubleshooting

### Why does it ask me to choose a private link?

Cursor shows "This MCP server is on a private Tailscale network. Choose a
private link for it, then try again." The server's URL is a tailnet
address, and it has no Tailscale connection. Set **Transport** to a
connection.

### The server shows Failed to connect

Rollouts reports this on the server's status. Check these in order:

- The OAuth client needs the `auth_keys` scope and permission to assign
  the connection's tag. The tag must be listed in `tagOwners`.
- The policy must allow the Cursor tag to reach the server's host on the
  port in its URL, or `443` when the URL has no port.
- Posture rules that apply to the Cursor tag, such as
  `defaultSrcPosture` or a `srcPosture` on its rule, can block Cursor's
  devices. Cursor can't meet them, so exempt the tag.
- With Tailnet Lock, new devices must be signed before they can connect.
  Cursor creates a new device each time it connects.
- Only an `https` URL can use a Tailscale connection.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
