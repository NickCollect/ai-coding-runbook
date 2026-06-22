---
source_url: https://cursor.com/docs/cloud-agent/choose-runtime
fetched_at: 2026-06-22T06:23:24.927177+00:00
fetch_method: mintlify_md
---

# Choose where Cloud Agents run

Cursor-hosted Cloud Agents run each agent in an isolated cloud VM with managed lifecycle, saved environments, artifact capture, and dashboard controls for secrets and network access.

Self-hosted paths run tool calls on hardware you control through [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md) or [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md). The agent loop still runs in Cursor's cloud.

## Self-hosted or Cursor-hosted: which is right for you?

Cursor-hosted cloud agents are sufficient for over 80% of our customers. Leverage this decision tree to evaluate what works best for your organization.

## Quick comparison

| Option                          | Choose it when                                                                                                                                                                      | What you manage                                                                                                                                     |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cursor-managed Cloud Agents** | You want Cursor to manage VM provisioning, isolation, snapshots, startup, artifacts, capacity, and environment deployment after setup. This is the recommended path for most teams. | First-time environment configuration, secrets, repository access, and network policy. Cursor manages the host and environment lifecycle after that. |
| **My Machines**                 | You want a personal laptop, devbox, or remote VM to execute tool calls for a specific user and repo.                                                                                | The machine, worker process, local checkout, credentials, uptime, disk, network access, and keeping the machine in a clean working state.           |
| **Self-Hosted Pool**            | You need an org-managed worker fleet with service account auth, pool routing, labels, Kubernetes, autoscaling, or dedicated hardware.                                               | Hosts, images, VM resets, capacity, autoscaling, worker updates, monitoring, secrets, network access, and incident response.                        |

## Start with managed Cloud Agents

Managed Cloud Agents are usually the lowest-operations way to give agents secure access to code and internal systems.

Use the managed path when you can configure access through:

- [Cloud Agent environments](https://cursor.com/docs/cloud-agent/setup.md) with setup commands, Dockerfiles, snapshots, and secrets.
- [Network access controls](https://cursor.com/docs/cloud-agent/security-network.md#network-access) that restrict outbound domains by user, team, or environment.
- [Tailscale or a similar private-network client](https://cursor.com/docs/cloud-agent/setup.md#running-tailscale) inside the environment when agents need to reach services in your VPC or intranet.
- [Private connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) for private GitHub Enterprise Server, GitLab Enterprise, private source control APIs, and related webhook traffic.

This lets Cursor operate the agent infrastructure after setup while your team controls which repos, secrets, and network resources each environment can reach.

## When My Machines fits

My Machines works best for personal or small-scale workflows where a specific user already has a machine with the right checkout, tools, credentials, and private network access.

Use it for:

- A developer's devbox or remote workstation.
- A one-off repo that depends on local state you do not want to recreate in a cloud environment.
- A quick test before building a centrally managed worker pool.

My Machines is not an org-wide fleet system. Each worker belongs to the user who started it, targets the repo where it was started, and must stay online while sessions run. You also own cleanup: wiping state, refreshing the checkout, repairing dependencies, and keeping the machine ready for the next run.

## When Self-Hosted Pool fits

Self-Hosted Pool is for Enterprise teams that want centralized ownership of worker hardware or need to route work to specific fleets.

Use a pool when you need:

- Service account authentication instead of per-user worker login.
- Kubernetes, autoscaling, labels, and fleet monitoring.
- Dedicated hardware profiles, such as GPU workers or high-memory build machines.
- Company-managed hosts that execute all terminal commands, file edits, browser actions, and local MCP servers.

The tradeoff is operational ownership. Your team runs the fleet, keeps enough workers available, patches and flashes images, resets VMs between runs, manages capacity, rotates credentials, monitors health, and handles host failures. If your primary requirement is private network access, try managed Cloud Agents with network controls, Tailscale, or private connectivity first.

## Security model differences

All three options support Privacy Mode and controlled secrets. The main difference is where tool execution happens and who operates that execution environment.

| Question                                    | Managed Cloud Agents                                                                                                          | My Machines                            | Self-Hosted Pool              |
| :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------- | :---------------------------- |
| Where does the agent loop run?              | Cursor cloud                                                                                                                  | Cursor cloud                           | Cursor cloud                  |
| Where do tool calls run?                    | Cursor-managed isolated VM                                                                                                    | Your machine                           | Your worker                   |
| Who manages host and environment lifecycle? | Cursor, after first-time environment configuration                                                                            | You                                    | Your team                     |
| How do agents reach private resources?      | Environment networking, allowlists, Tailscale or similar clients, and private connectivity for supported source control paths | Your machine's existing network        | Your worker fleet's network   |
| Best operational fit                        | Most teams and repos                                                                                                          | Individual users and specific machines | Centralized enterprise fleets |

## Related

- [Cloud Agent setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md)
- [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md)
- [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [Private connectivity](https://cursor.com/docs/enterprise/private-connectivity.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
