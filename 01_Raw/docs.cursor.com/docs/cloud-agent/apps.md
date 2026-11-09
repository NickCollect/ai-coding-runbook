---
source_url: https://cursor.com/docs/cloud-agent/apps
fetched_at: 2026-11-09T07:30:16.344937+00:00
fetch_method: mintlify_md
---

# Apps

[Cloud Agents](https://cursor.com/docs/cloud-agent.md) can build a working web app, like a dashboard, portal, or microsite. You describe what you want to build, and Cursor handles the hosting, database, auth, and secrets.

## Getting started

Be explicit that you want Cursor to build an app. You can start from scratch, which creates a new repository on [Cursor Origin](https://cursor.com/docs/origin.md), or ask Cursor to deploy an app from an existing GitHub repository. Remember to use a cloud agent; this feature is not supported locally.

Sample prompts:

- "Build an app that shows our weekly signups as a dashboard, with a chart and a table I can filter by plan."
- "Build an internal app where my team can submit bug reports and track their status."
- "Build a microsite for our product launch with a sign-up form that collects emails."
- "Deploy this repo as an app."

When Cursor has prepared the app, it shows you a tray where you can preview the app and publish it. When you publish, you pick the app's URL (which you can change later) and Cursor runs a series of deterministic and agentic security checks. If all checks pass, Cursor returns a live link. If not, it lists what it needs to fix before the app can deploy. Tell the agent to fix the issues, then publish again. Nothing goes live before you choose to publish.

## How it works

- **Hosting.** Cursor deploys each app in a dedicated account it creates for your team, or for you on an individual plan. Each hosting account is isolated from every other team's and user's.
- **Database.** If the app needs a database, Cursor provisions a Postgres database for it automatically.
- **Auth.** Private and team apps sit behind Cursor sign-in, so only the people you share with can open them. Users on individual plans can share apps publicly, which does not require Cursor auth.
- **Secrets.** When you want the app to use your own resources or connect to other systems, like a data warehouse, Cursor prompts you for the secrets it needs. The agent never sees the values. In most cases a team admin creates team secrets in the [Apps dashboard](https://cursor.com/dashboard/apps#secrets). If you have access to create personal secrets, you can add your own.

You can bring your own resources and integrations. Configure secrets and keys for them while building your app or in the [Apps dashboard](https://cursor.com/dashboard/apps#secrets).

## Sharing

| Visibility        | Who can open it                                                          |
| :---------------- | :----------------------------------------------------------------------- |
| People you invite | Only you or specific team members and groups that are signed into Cursor |
| Team              | You and your entire Cursor team, signed in to Cursor                     |
| Public            | Anyone with the link                                                     |

Public sharing is disabled by default for Teams and Enterprise. A team admin can turn it on in the [Apps dashboard](https://cursor.com/dashboard/apps#danger-zone).

## API keys for Grok Bot and scripts

Private and team apps sit behind Cursor sign-in, which automated tools can't get through. A Cursor API key lets Grok Bot, scripts, CI jobs, and more use an app the way another signed-in user would.

### How it works

- **Personal API keys** open the apps their owner can open.
- **Team API keys** open only the team apps they've been given access to.
- **Public apps** open for either key, as they would for a normal visitor.

A key that isn't allowed in is treated like a user with no access, so the caller gets the sign-in redirect.

### Using it with an HTTP header

Send the key in the `x-cursor-app-token` header on every request:

```bash
curl -H "x-cursor-app-token: $CURSOR_API_KEY" https://<your-app-url>
```

The key only works as a header. There's no query parameter and no cookie, so your tool has to set the header on each request.

Requests made with a key are marked as automated and identify the key, never a person. See all the API keys tied to apps in the [Apps dashboard](https://cursor.com/dashboard/apps/security/api-keys).

## Security and controls

The [Apps dashboard](https://cursor.com/dashboard/apps) lists the apps you created and the apps shared with you. Team admins can see every app and secret on the team, and can unpublish any app.

Four checks run before every publish. They're always on, even when the security review is off:

- **Block secrets written in app files.** Stops the publish if a file contains an API key or access token.
- **Block credential files.** Stops the publish if it includes private keys, service-account keys, or files with auth tokens.
- **Never publish .env files.** Leaves `.env` files out of what ships.
- **Never publish source maps.** Removes source maps so visitors can't read the original source code.

On top of these, an AI security review reads the app's files and blocks serious issues before the app goes live. Team admins can add their own instructions to the review prompt in the [Apps dashboard](https://cursor.com/dashboard/apps#security). Custom instructions can add rules, but they can't remove Cursor's built-in checks.

Team admins can also:

- Turn Apps on or off for the team.
- Allow or disallow public apps. Disallowing them moves existing public apps back to team visibility.
- Allow or disallow API keys opening apps.
- Approve publishes the review blocked, except for malicious code, hardcoded secrets, or exposed credentials.

Changes to these settings are recorded in the team's audit log.

## Availability

Apps is available on all paid plans with access to cloud agents.

We only provide technology and tools for you to use, do not provide any reps or warranties, and are not responsible for your apps, including your prompts and any outputs. Publication of an app does not constitute endorsement by us. A subdomain, associated account, published app(s) may be revoked, terminated, removed, or suspended if they violate these terms, the terms that govern your account, or the [Acceptable Use Policy](/acceptable-use-policy), or for business, financial, or legal reasons. You also agree that hosting is separate from, and is not part of, our services, and is provided "as is" and "as available."

## Related pages

- Learn more about [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md).
- Learn more about [Cloud agent security](https://cursor.com/docs/cloud-agent/security.md).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
