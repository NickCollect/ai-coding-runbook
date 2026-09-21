---
source_url: https://cursor.com/docs/agent/projects
fetched_at: 2026-09-21T05:43:59.841121+00:00
fetch_method: mintlify_md
---

# Projects

A Project takes on a larger body of work, such as a feature, a migration, or a full app. You direct it by chatting with its coordinator agent. The coordinator doesn't write code itself. It plans the work, delegates it to [agents](https://cursor.com/docs/agent/overview.md) that write the code, and brings the finished work back to you to check. Projects live in the left-hand nav of the [Agents Window](https://cursor.com/docs/agent/agents-window.md) and run on [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

Projects is rolling out to all users. It isn't available on Enterprise plans. It also isn't available with Privacy Mode (Legacy), because Projects run on Cloud Agents, which store code in the cloud while they run.

## How a Project works

A Project maintains context over months of work, delegates tasks to many agents in parallel, and performs recurring work without being prompted.

- **The coordinator plans and delegates.** It creates and manages agents on your behalf, running as many in parallel as the work needs. Because it delegates rather than executes, it stays responsive to your direction.
- **Agents work inside the Project.** Open any agent the coordinator starts to follow its work or talk to it directly.

## Create a Project

### Open Projects in the left-hand nav

In the [Agents Window](https://cursor.com/docs/agent/agents-window.md), find the **Projects** section in the sidebar and click **New Project**.

### Name the Project

Choose an icon and enter a project name. If you leave the name empty, the Project is called **New Project**.

### Choose a workspace and model

Under **Workspace**, pick the repository the Project works in. Projects run in the cloud, so the list shows the repositories available to your cloud agents. If GitHub isn't connected yet, the menu offers **Connect GitHub**. Under **Model**, pick the model the coordinator uses.

### Click Create Project

The Project opens as a chat with its coordinator. Describe what you want built, and the coordinator takes it from there.

Projects work best on work that outlives a single chat: a feature with several PRs, a migration, or a job you want handled while you're away.

## Cloud by default, local when needed

A Project runs on its own computer in the cloud, so closing your laptop doesn't stop it. Running in the cloud also lets a Project run more agents in parallel than your laptop could support.

When something needs testing on your machine, the coordinator starts a local agent to run it there.

## Shared context

You shouldn't have to onboard an agent every time you start a task. Each Project maintains a set of files that sync across every cloud and local machine its agents use. Agents add research and artifacts, along with what they learn about the codebase and how you prefer work to be done. If one agent figures out how to test a service, every future agent can use those instructions.

The shared context grows with the Project, making the coordinator more effective over time.

## Subscriptions

Tell the coordinator to watch a Slack channel, run on a schedule, or follow your pull requests. It then acts on the signals it detects without waiting for your prompt. For example, connect [Slack](https://cursor.com/docs/integrations/slack.md), point the coordinator at a bug-report channel, and it delegates a fix each time a bug comes in.

The coordinator creates a subscription when you ask it to. Once it has at least one, a **Listening** pill appears above the chat input. Click it to see every event the Project listens for, such as a message posted in a channel, PR activity in a repository, CI runs on a branch, or a schedule like every day at 8:00 AM. Remove a subscription from the same list when you no longer need it.

## Related pages

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md)
- [Subagents](https://cursor.com/docs/subagents.md)
- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Slack integration](https://cursor.com/docs/integrations/slack.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
