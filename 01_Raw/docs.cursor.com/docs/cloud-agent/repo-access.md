---
source_url: https://cursor.com/docs/cloud-agent/repo-access
fetched_at: 2026-11-23T08:28:23.029991+00:00
fetch_method: mintlify_md
---

# Access Other Repositories

Work often spans more than one repo. Cloud Agents and Projects can get access to the repos and environments they need while they work, so a change to your web app and the API it calls can happen in one piece of work, without you setting up a new environment first.

Every cloud agent starts with the repos in its environment: one repo, [several repos](https://cursor.com/docs/cloud-agent/setup.md#multi-repo-environments), or [repository dependencies](https://cursor.com/docs/cloud-agent/setup.md#repository-dependencies). Cloud Agents and [Projects](https://cursor.com/docs/agent/projects.md) can get access beyond that while they work.

## How it works

When a Cloud Agent or a Project needs another repo or environment, it asks for access first.

- **Repos** are allowed automatically when you can push to them.
- **Environments** are allowed automatically when you can use them and they have a name in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).
- **[Self-hosted](https://cursor.com/docs/cloud-agent/self-hosted.md) machines and pools** need your approval in the agent's chat, unless your team turns on **Automatically allow agents to use self-hosted machines** in [settings](https://cursor.com/docs/cloud-agent/settings.md#security-settings).

Access covers the whole Cloud Agent or Project, including agents it starts later, and lasts until you remove it. With access, it can start agents on that repo, in that environment with its secrets and network settings, or on that machine.

To see or remove access, open the **Run on** menu next to the chat input in the [Agents Window](https://cursor.com/docs/agent/agents-window.md).

**Example.** A Cloud Agent or Project in `acme/web` needs a new endpoint in `acme/api`. It gets access to `acme/api`, then starts an agent there to add the endpoint.

## Security

- **Access is consent.** Repos and environments are allowed automatically, so a Cloud Agent or Project can reach any repo you can push to. Give them tasks from sources you trust.
- **Repos run their own hooks.** An agent started on another repo runs that repo's [hooks](https://cursor.com/docs/hooks.md#cloud-agent-support), with the machine's git credentials and the environment's secrets.

## Related pages

- [Cloud Environment Setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Projects](https://cursor.com/docs/agent/projects.md)
- [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
