---
source_url: https://cursor.com/docs/agent/projects
fetched_at: 2026-11-16T07:30:43.765119+00:00
fetch_method: mintlify_md
---

# Projects

A Project takes on a larger body of work, such as a feature, a migration, or a full app. You direct it by chatting with its coordinator agent. The coordinator doesn't write code itself. It plans the work, delegates it to [agents](https://cursor.com/docs/agent/overview.md) that write the code, and brings the finished work back to you to check. Projects live in the left-hand nav of the [Agents Window](https://cursor.com/docs/agent/agents-window.md) and run on [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

Projects is available on every plan that includes Cloud Agents: Premium and higher, Teams, Enterprise, and legacy paid Cursor plans. Enterprise teams need Cursor 3.21.9 or later. Projects isn't available on Free, Plus, or the legacy Hobby plan, which don't include Cloud Agents. It also isn't available with Privacy Mode (Legacy), because Projects run on Cloud Agents, which store code in the cloud while they run.

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

To create and manage Projects from code, use the [Projects endpoints](https://cursor.com/docs/cloud-agent/api/endpoints.md#projects) of the Cloud Agents API.

Projects work best on work that outlives a single chat: a feature with several PRs, a migration, or a job you want handled while you're away.

## Add and remove chats

Drag an eligible top-level Cloud Agent chat from the sidebar onto a Project row to add it. You can also open the chat's sidebar menu and choose **Add to Project**. If the action is available for a local chat, Cursor converts it to Remote Control before adding it. The chat then appears under the Project row and in the **Agents** list above the Project's chat input.

To take a chat out, open its menu in the **Agents** list and choose **Remove from Project**.

## Cloud by default, local when needed

A Project runs on its own computer in the cloud, so closing your laptop doesn't stop it. Running in the cloud also lets a Project run more agents in parallel than your laptop could support.

When something needs testing on your machine, the coordinator starts a local agent to run it there.

## Shared context

You shouldn't have to onboard an agent every time you start a task. Each Project maintains a set of files that sync across every cloud and local machine its agents use. Agents add research and artifacts, along with what they learn about the codebase and how you prefer work to be done. If one agent figures out how to test a service, every future agent can use those instructions.

The shared context grows with the Project, making the coordinator more effective over time.

## Subscriptions

Tell the coordinator to watch a Slack channel, run on a schedule, or follow your pull requests. It then acts on the signals it detects without waiting for your prompt. For example, connect [Slack](https://cursor.com/docs/integrations/slack.md), point the coordinator at a bug-report channel, and it delegates a fix each time a bug comes in.

The coordinator creates a subscription when you ask it to. Once it has at least one, a **Listening** pill appears above the chat input. Click it to see every event the Project listens for, such as a message posted in a channel, PR activity in a repository, CI runs on a branch, or a schedule like every day at 8:00 AM. Remove a subscription from the same list when you no longer need it.

## Multiplayer Projects

Invite teammates into a Project to work on it together. Each person who joins gets their own chat in the Project, with their own coordinator and workers. Their chat runs and bills as them. Members share two parts of the Project:

- **The task board.** Everyone works from the same tasks in the Project's list and board.
- **Shared context.** The Project's [shared context](https://cursor.com/docs/agent/projects.md#shared-context), shown as **Context** in the app, is one Agent Store that every member's agents read and write.

Sharing a Project needs a team account and Cursor 3.26.13 or later.

### How coordinators message each other

When your coordinator needs something from a teammate's work, it messages their coordinator directly, so you don't have to relay it. Cursor delivers every message and holds it to these rules:

- **Messages are labeled as agent input.** The receiving agent is told which teammate's agent sent the message. It treats the text as untrusted input to weigh, not as a request from the person it works for, and asks before sharing that person's personal files or connector data.
- **Your chat isn't interrupted.** A teammate's message goes to a side chat forked from your chat, called **Chat with \{name}'s agent**. It answers from what your chat knows, its reply goes back to the sender's chat, and your chat gets a note about the exchange on its next turn.
- **Side chats only answer.** You can read, stop, or archive a side chat, but you can't message it. It never shares secrets, credentials, or tokens. It can read the task board but not change it, and it can't ask you questions, request access, connect source control, or manage routines.

### Context and your personal store

Agents in a Project use two stores:

| Store                       | Path                  | Who reads and writes it |
| --------------------------- | --------------------- | ----------------------- |
| Project store (**Context**) | `/cursor/stores/self` | Every member's agents   |
| Personal user store         | `/cursor/stores/user` | Your own agents         |

Each person's agents mount their own personal store at `/cursor/stores/user`, so a teammate's agents never see yours. It holds your preferences and skills, which follow you between Projects without reaching your teammates. When a teammate joins, your coordinator can offer to copy entries from your preferences that describe how to work in this Project into the Project's rules. It copies only what you approve.

### Who can join

Projects are shared within a Cursor team, and joining takes an invite. Someone on a personal account, or on another team, can't join.

### Open the invite menu

At the top of the Project, click **Invite**. After the first invite, click the row of faces in its place.

### Invite teammates

Under **Invite teammates to this project**, search for teammates by name or email and send the invite.

### Your teammate joins

Your teammate clicks **Accept Invite** on the Project's invite card and gets their own chat in the Project.

The owner and anyone who has joined can invite teammates. People can also join from the Project's link: **Copy link** in the same menu copies it, and only people in the Project can copy it. The owner can choose **Reset Share Link** to stop earlier copies from working.

A teammate needs access to the Project's repository to join. Joining isn't available with Privacy Mode (Legacy), on a Project that runs on a self-hosted machine, or on an archived Project.

To stop working in a shared Project, open its menu in the sidebar and choose **Leave Project**. You can rejoin later from an invite or the link. The owner can remove anyone else from the invite menu with **Remove**.

## Related pages

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md)
- [Subagents](https://cursor.com/docs/subagents.md)
- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Slack integration](https://cursor.com/docs/integrations/slack.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
