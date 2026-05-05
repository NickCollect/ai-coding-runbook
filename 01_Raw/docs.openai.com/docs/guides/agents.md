# Agents SDK

<!-- source: https://platform.openai.com/docs/guides/agents -->

Agents are applications that plan, call tools, collaborate across specialists, and keep enough state to complete multi-step work.

**When to use what:**
- Use OpenAI client libraries when you want direct API clients for model requests
- Use the Agents SDK when your application owns orchestration, tool execution, approvals, and state
- Use Agent Builder only when you want the hosted workflow editor and ChatKit path

## Get the Agents SDK

- TypeScript: [openai/openai-agents-js](https://github.com/openai/openai-agents-js)
- Python: [openai/openai-agents-python](https://github.com/openai/openai-agents-python)

## Choosing your starting point

| Goal | Start here |
|---|---|
| Build a code-first agent app | Quickstart |
| Define one specialist cleanly | Agent definitions |
| Choose models, defaults, and transport | Models and providers |
| Understand the runtime loop and state | Running agents |
| Run work in a container-based environment | Sandbox agents |
| Design specialist ownership | Orchestration and handoffs |
| Add validation or human review | Guardrails and human review |
| Understand what a run returns | Results and state |
| Add tools, function tools, or MCP | Using tools |
| Inspect and improve runs | Integrations and observability |
| Build a voice-first workflow | Voice agents |

## SDK reading order

1. **Quickstart** — shortest path to a working SDK integration
2. **Agent definitions** + **Models and providers** — shape one specialist cleanly
3. **Running agents**, **Orchestration and handoffs**, **Guardrails and human review** — as the workflow grows
4. **Results and state**, **Integrations and observability** — when app logic depends on run object

## Agent Builder (hosted workflow path)

Use Agent Builder when you want OpenAI-hosted workflow creation, publishing, and ChatKit deployment. Agent Builder does NOT currently support voice workflows — use the SDK for voice.

## Sandbox agents

Sandbox agents are available in the Python Agents SDK. Use them when your agent needs a container-based environment with files, commands, packages, ports, snapshots, and memory.

## Key concepts

- **Orchestration**: One manager agent delegates to specialists, controls user-facing reply
- **Handoffs**: Transfer control between agents based on task context
- **Guardrails**: Input/output validations to block risky content
- **Human review (approvals)**: Pause before risky work continues
- **MCP integration**: Connect to external MCP servers for extended capabilities
