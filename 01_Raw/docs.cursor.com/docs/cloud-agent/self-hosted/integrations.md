---
source_url: https://cursor.com/docs/cloud-agent/self-hosted/integrations
fetched_at: 2026-09-07T05:31:27.606477+00:00
fetch_method: mintlify_md
---

# Integrations

Run [Team Pool](https://cursor.com/docs/cloud-agent/self-hosted/pool.md) workers on an infrastructure partner's platform, or start from a reference template you clone and adapt. Every option runs the same worker: the [Cursor CLI](https://cursor.com/docs/cli/overview.md) opens an outbound HTTPS connection to Cursor, and Cursor sends agent tool calls over that connection.

Partner guides and templates are reference architectures. You own the worker image, infrastructure, secrets, scaling policy, and production validation.

## Partner guides

Each partner maintains its own guide for running Self-Hosted Machines workers on its platform:

- **AWS Lambda.** [Cursor Self-Hosted Machines on Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-cursor-self-hosted-machines.html)
- **Cloudflare.** [Cursor Cloud Agents on Cloudflare Sandbox](https://developers.cloudflare.com/sandbox/tutorials/cursor-cloud-agents/)
- **Namespace.** [Cursor integration](https://namespace.so/docs/integrations/cursor)
- **Modal.** [Cursor on Modal](https://modal.com/docs/cursor)
- **Daytona.** [Cursor Self-Hosted Machines on Daytona](https://www.daytona.io/docs/en/guides/cursor/cursor-self-hosted-machines)
- **E2B.** [Cursor agents on E2B](https://docs.e2b.dev/agents/cursor)
- **Vercel.** [Cursor with Vercel Sandbox](https://vercel.com/kb/guide/cursor-vercel-sandbox)
- **Coder.** [Agent Relay for Cursor](https://coder.com/docs/@main/ai-coder/agent-relay)

## Reference templates

Clone one of these repositories to start from a working worker deployment. Each one runs a [worker controller](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#worker-controller) that claims pending pool requests and starts one worker per claim:

- **AWS Lambda MicroVMs.** [anysphere/aws-lambda-workers](https://github.com/anysphere/aws-lambda-workers): a `--spawn` hook launches one Firecracker-isolated Lambda MicroVM per claimed request.
- **Cloudflare Containers.** [anysphere/cloudflare-workers](https://github.com/anysphere/cloudflare-workers): a Cloudflare Worker acts as the controller and starts one Cloudflare Container per claimed request.
- **Kubernetes.** [anysphere/k8s-workers](https://github.com/anysphere/k8s-workers): a Helm sample that runs `agent worker controller --spawn` in your cluster and creates one Pod per claimed request, or keeps warm idle Pods with `--warm-idle`, without a CRD. This is the Kubernetes path for new deployments.

The Cursor Kubernetes operator and `WorkerDeployment` Helm chart are
deprecated. Clusters that already run the operator can keep using it; the
[operator reference](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md) stays
available for them. Don't start new deployments on it.

## What every integration needs

The platform changes, but the worker requirements stay the same:

- A **Cursor Enterprise plan**, with Self-Hosted Machines enabled by a team admin in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents).
- A [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) in `CURSOR_API_KEY`. See [Authenticate workers](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#authenticate-workers).
- Outbound HTTPS to `api2.cursor.sh`, `api2direct.cursor.sh`, and `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`. See [Networking](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#networking).
- A [pool name](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#pool-names) or [labels](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#labels) so Cursor routes the right requests to workers on that platform.

For a single personal machine instead of a platform-managed fleet, use [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md).

## Next steps

- [Team Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md): start a pool worker by hand before you automate it on a platform.
- [Worker controller](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#worker-controller): the `--spawn` hook model every template builds on.
- [Kubernetes operator (deprecated)](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md): reference for clusters that already run the `WorkerDeployment` operator.
- [API reference](https://cursor.com/docs/cloud-agent/api/endpoints.md#workers-and-pools): endpoints for workers, pools, the pending-request queue, and worker tokens.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
