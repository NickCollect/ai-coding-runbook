---
source_url: https://cursor.com/docs/bugbot
---

# Bugbot

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

On Teams and Individual Plans, Bugbot includes a free tier: every user gets a limited number of free PR reviews. You can start a 14-day free Bugbot Pro trial to keep using Bugbot.

[Bugbot leaving comments on a PR](/docs-static/images/bugbot/bugbot-report-cropped.mp4)

## How it works

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

- Runs **automatic reviews** on every PR update
- **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
- **Uses existing PR comments as context**: reads GitHub PR comments (top‑level and inline) to avoid duplicate suggestions and build on prior feedback
- **Fix in Cursor** links open issues directly in Cursor
- **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

## Setup

Connect your repositories through the Cursor dashboard to start using Bugbot.

- **GitHub** (including GitHub Enterprise Server): See the [GitHub integration page](https://cursor.com/docs/integrations/github.md)
- **GitLab** (including GitLab Self-Hosted): See the [GitLab integration page](https://cursor.com/docs/integrations/gitlab.md)

After connecting, return to the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) to enable Bugbot on specific repositories.

## Configuration

### Individual

### Repository settings

Enable or disable Bugbot per repository from your installations list. Bugbot runs only on PRs you author.

### Personal settings

- Run **only when mentioned** by commenting `cursor review` or `bugbot run`
- Run **only once** per PR, skipping subsequent commits

### Team

### Repository settings

Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

- Run **only once** per PR per installation, skipping subsequent commits

Bugbot runs for all contributors to enabled repositories, regardless of team membership.

### Personal settings

Team members can override settings for their own PRs:

- Run **only when mentioned** by commenting `cursor review` or `bugbot run`
- Run **only once** per PR, skipping subsequent commits
- **Enable reviews on draft PRs** to include draft pull requests in automatic reviews

## Analytics

![Bugbot dashboard](/docs-static/images/bugbot/bugbot-dashboard.png)

## Team rules

Team admins can create rules from the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) that apply to all repositories in the team. These rules are available to every enabled repository, making it easy to enforce organization-wide standards.

When Team Rules, repository rules, and project rule files all apply, Bugbot merges them. Order of application: Team Rules → repository rules (learned and manual) → project BUGBOT.md (including nested files) → User Rules.

## Repository rules

### Project rules

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```bash
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

### Learned rules

In the [Bugbot dashboard](https://cursor.com/dashboard/bugbot/repository-rules), enable learning for your organizations and repositories.

Rules are generated automatically from your team's activity on GitHub for that repository or by manually backfilling from the history of the repository.

You can also teach Bugbot new rules inline by commenting `@cursor remember [fact]` on any PR. Bugbot saves the fact as a learned rule and applies it to future reviews.

Cursor will automatically enable or disable rules as it learns more about your team's activity over time.

| Field            | Description                                                                                                    |
| :--------------- | :------------------------------------------------------------------------------------------------------------- |
| **Name**         | Short title for the rule.                                                                                      |
| **Rule content** | The instructions Bugbot should follow (i.e. style gates, paths, or review expectations).                       |
| **Scoped paths** | Optional glob patterns such as `src/components/**`. Leave empty to apply the rule across the whole repository. |

### Manual rules

In the [Bugbot dashboard](https://cursor.com/dashboard/bugbot/repository-rules), you can create manual rules for individual repositories.

| Field            | Description                                                                                                    |
| :--------------- | :------------------------------------------------------------------------------------------------------------- |
| **Name**         | Short title for the rule.                                                                                      |
| **Rule content** | The instructions Bugbot should follow (i.e. style gates, paths, or review expectations).                       |
| **Scoped paths** | Optional glob patterns such as `src/components/**`. Leave empty to apply the rule across the whole repository. |

### Rule analytics

**Analytics** on a Bugbot rule show how it performs on real PRs:

| Metric              | Meaning                                                    |
| :------------------ | :--------------------------------------------------------- |
| **Issues found**    | Number of findings Bugbot reported that involve this rule. |
| **PRs reviewed**    | Number of pull requests where those findings appeared.     |
| **Accepted issues** | Number of findings your team accepted.                     |
| **Acceptance rate** | Percentage of findings that were accepted.                 |

### Examples

### Security: Flag any use of eval() or exec()

```text
If any changed file contains the string pattern /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug with title "Dangerous dynamic execution" and body:
  "Usage of eval/exec was found. Replace with safe alternatives or justify with a detailed comment and tests."
- Assign the Bug to the PR author.
- Apply label "security".
```

### OSS licenses: Prevent importing disallowed licenses

```text
If the PR modifies dependency files (package.json, pnpm-lock.yaml, yarn.lock, requirements.txt, go.mod, Cargo.toml), then:
- Run the built-in License Scan.
- If any new or upgraded dependency has license in {GPL-2.0, GPL-3.0, AGPL-3.0}, then:
  - Add a blocking Bug titled "Disallowed license detected"
  - Include the offending package names, versions, and licenses in the Bug body
  - Apply labels "compliance" and "security"
```

### Language standards: Flag React componentWillMount usage

```text
For files matching **/*.{js,jsx,ts,tsx} in React projects:
If a changed file contains /componentWillMount\s*\(/, then:
- Add a blocking Bug titled "Deprecated React lifecycle method"
- Body: "Replace componentWillMount with constructor or useEffect. See React docs."
- Suggest an autofix snippet that migrates side effects to useEffect.
```

### Standards: Require tests for backend changes

```text
If the PR modifies files in {server/**, api/**, backend/**} and there are no changes in {**/*.test.*, **/__tests__/**, tests/**}, then:
- Add a blocking Bug titled "Missing tests for backend changes"
- Body: "This PR modifies backend code but includes no accompanying tests. Please add or update tests."
- Apply label "quality"
```

### Style: Disallow TODO comments

```text
If any changed file contains /(?:^|\s)(TODO|FIXME)(?:\s*:|\s+)/, then:
- Add a non-blocking Bug titled "TODO/FIXME comment found"
- Body: "Replace TODO/FIXME with a tracked issue reference, e.g., `TODO(#1234): ...`, or remove it."
- If the TODO already references an issue pattern /#\d+|[A-Z]+-\d+/, mark the Bug as resolved automatically.
```

## Autofix

Bugbot Autofix automatically spawns a [Cloud Agent](https://cursor.com/docs/cloud-agent.md#overview) to fix bugs found during PR reviews.

### How it works

When Bugbot finds bugs during a PR review, it can automatically:

1. Spawn a Cloud Agent to analyze and fix the reported issues
2. Push fixes to the existing branch or a new branch (depending on your settings)
3. Post a comment on the original PR with the results

![Bugbot Autofix comment on a PR](/docs-static/images/bugbot/bugbot-autofix-comment.png)

### Configuration

Configure autofix behavior from the [Bugbot dashboard](https://cursor.com/dashboard/bugbot).

### Individual

Individual users can configure their autofix preference in their personal Bugbot settings:

- **Use Installation Default** — Follow your organization's settings
- **Off** — autofix is disabled; use manual "Fix in Cursor" or "Fix in Web" links
- **Create New Branch** (Recommended) — Push fixes to a new branch
- **Commit to Existing Branch** — Push fixes to your branch (max 3 attempts per PR to prevent loops)

User settings override team defaults for your own PRs.

### Team

Team admins can set a default autofix mode for all team members in a GitHub organization:

- **Off** — autofix is disabled by default
- **Create New Branch** (Recommended) — Push fixes to a new branch for team members
- **Commit to Existing Branch** — Push fixes directly to the PR branch (max 3 attempts per PR to prevent loops)

Individual team members can override these defaults in their personal settings.

Autofix uses your **Default agent model** from [Settings → Models](https://cursor.com/dashboard/settings). If you haven't set a personal model preference, autofix falls back to your team's default model (if you're on a team) or the system default.

### Requirements

Autofix requires:

- [Usage-based pricing](https://cursor.com/docs/models-and-pricing.md) enabled
- Storage enabled (not in Legacy Privacy Mode)

### Billing

Autofix uses Cloud Agent credits and is billed at your plan rates. Cloud Agent billing follows your existing [pricing plan](https://cursor.com/docs/models-and-pricing.md).

## MCP support

Bugbot is integrated with your [MCP servers](https://cursor.com/docs/mcp.md) so your AI tools can interact with Bugbot directly. Use the MCP server to provide additional tools to guide Bugbot's review process.

To get started:

1. Follow the [MCP documentation](https://cursor.com/docs/mcp.md) for MCP server setup instructions.
2. Add the tools to Bugbot in the [Bugbot dashboard](https://cursor.com/dashboard/bugbot).

MCP support is available on Team and Enterprise plans only.

## Admin Configuration API

Team admins can use the Bugbot Admin API to manage repositories and control which users can use Bugbot. Use it to automate repository management, enable Bugbot across multiple repositories, or integrate user provisioning with internal tools.

### Authentication

All endpoints require a team Admin API Key passed as a Bearer token:

```bash
Authorization: Bearer $API_KEY
```

To create an API key:

1. Visit the [Settings tab in the Cursor dashboard](https://cursor.com/dashboard/settings)
2. Under **Advanced**, click **New Admin API Key**
3. Save the API key

All endpoints are rate-limited to 60 requests per minute per team.

### Enabling or disabling repositories

Use the `/bugbot/repo/update` endpoint to toggle Bugbot on or off for a repository:

```bash
curl -X POST https://api.cursor.com/bugbot/repo/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repoUrl": "https://github.com/your-org/your-repo",
    "enabled": true
  }'
```

**Parameters:**

- `repoUrl` (string, required): The full URL of the repository
- `enabled` (boolean, required): `true` to enable Bugbot, `false` to disable it

The dashboard UI may take a moment to reflect changes made through the API due to caching. The API response shows the current state in the database.

### Listing repositories

Use the `/bugbot/repos` endpoint to list all repositories with their Bugbot settings for your team:

```bash
curl https://api.cursor.com/bugbot/repos \
  -H "Authorization: Bearer $API_KEY"
```

The response includes each repository's enabled status, manual-only setting, and timestamps.

### Managing user access

Use the `/bugbot/user/update` endpoint to control which GitHub or GitLab users can use your team's Bugbot licenses. Enterprises use this to integrate Bugbot provisioning with internal access-request tools.

#### Prerequisites

Before calling this endpoint, enable an allowlist or blocklist mode in your [team Bugbot settings](https://cursor.com/dashboard/bugbot):

- **Allowlist mode ("Only...")**: Only users on the list can use Bugbot
- **Blocklist mode ("Everyone but...")**: All users can use Bugbot except those on the list

If neither mode is enabled, the API returns an error.

#### Adding or removing a user

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "octocat",
    "allow": true
  }'
```

**Parameters:**

- `username` (string, required): The GitHub or GitLab username (case-insensitive)
- `allow` (boolean, required): Whether to grant or revoke access

How `allow` behaves depends on the active mode:

| Mode      | `allow: true`                                | `allow: false`                             |
| --------- | -------------------------------------------- | ------------------------------------------ |
| Allowlist | Adds user to list (can use Bugbot)           | Removes user from list (cannot use Bugbot) |
| Blocklist | Removes user from blocklist (can use Bugbot) | Adds user to blocklist (cannot use Bugbot) |

**Response:**

```json
{
  "outcome": "success",
  "message": "Updated team-level allowlist for @octocat",
  "updatedTeamSettings": true,
  "updatedInstallations": 0
}
```

The allowlist is stored at the team level and applies across all GitHub and GitLab installations owned by that team. Usernames are normalized to lowercase.

#### Example: provisioning users through an internal tool

Connect this API to an internal access-request portal. When an employee requests Bugbot access, the portal calls the API to add them. When they leave or lose access, it calls the API to remove them.

**Grant access:**

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-github-name", "allow": true}'
```

**Revoke access:**

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-github-name", "allow": false}'
```

## Pricing

Bugbot offers two tiers: **Free** and **Pro**.

### Free tier

On Teams and Individual Cursor plans, every user gets a limited number of free PR reviews each month. For teams, each team member gets their own free reviews. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a paid Bugbot plan for reviews on all PRs.

### Pro tier

### Individuals

### Flat rate

$40 per month for Bugbot reviews on up to 200 PRs per month across all repositories.

### Getting started

Subscribe through your account settings.

### Teams

### Per-user billing

Teams pay $40 per user per month for reviews.

We count a user as someone who authored PRs reviewed by Bugbot in a month.

All licenses are relinquished at the start of each billing cycle, and will be assigned out on a first-come, first-served basis. If a user doesn't author any PRs reviewed by Bugbot in a month, the seat can be used by another user.

### Seat limits

Team admins can set maximum Bugbot seats per month to control costs.

### Getting started

Subscribe through your team dashboard to enable billing.

### Abuse guardrails

In order to prevent abuse, we have a pooled cap of 200 pull requests per month for every Bugbot license. If you need more than 200 pull requests per month, reach out through the [help center](https://cursor.com/help/ai-features/bugbot.md) and we'll increase it.

For example, if your team has 100 users, your organization will initially be able to review 20,000 pull requests per month. If you reach that limit naturally, please reach out to us and we'll be happy to increase the limit.

## Troubleshooting

If Bugbot isn't working:

1. **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2. **Check permissions** to verify Bugbot has repository access
3. **Verify installation** to confirm the GitHub app is installed and enabled

Include the request ID from verbose mode when reporting issues.

## FAQ

### Does Bugbot read GitHub PR comments?

Yes. Bugbot reads both top‑level and inline GitHub pull request comments and includes them as context during reviews. This helps avoid duplicate suggestions and allows Bugbot to build on prior feedback from reviewers.

### Is Bugbot privacy-mode compliant?

Yes, Bugbot follows the same privacy compliance as Cursor and processes data identically to other Cursor requests.

### What happens when I hit the free tier limit?

When you reach your monthly free tier limit, Bugbot reviews pause until your next billing cycle. You can start a 14‑day free Bugbot Pro trial to keep using Bugbot.

### How do I give Bugbot access to my GitLab or GitHub Enterprise Server instance?

See the setup and networking guides on the respective integration pages:

- [GitHub Enterprise Server](https://cursor.com/docs/integrations/github.md#setup)
- [GitLab Self-Hosted](https://cursor.com/docs/integrations/gitlab.md#setup)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
