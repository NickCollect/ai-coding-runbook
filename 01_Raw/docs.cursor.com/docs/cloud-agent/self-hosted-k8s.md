---
source_url: https://cursor.com/docs/cloud-agent/self-hosted-k8s
fetched_at: 2026-05-11T04:55:36.647976+00:00
fetch_method: mintlify_md
---

# Self-Hosted Cloud: Deploying with Kubernetes

Deploy and manage [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md) workers using a Kubernetes operator. It handles scaling, rolling updates, and lifecycle management.

![Self-hosted Cloud Agents deployed with Kubernetes](/docs-static/images/cloud-agent/self-hosted-k8s.png)

## Prerequisites

- A Kubernetes cluster (v1.24+), either a cloud cluster (EKS, GKE, AKS) or a local one via [OrbStack](https://orbstack.dev) for testing
- `kubectl` configured to talk to your cluster
- `helm` v3 installed
- A Cursor Enterprise plan with Self-Hosted Cloud Agents enabled
- A [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md) for worker authentication

If using OrbStack locally, switch to its context first:

```bash
kubectl config use-context orbstack
```

Your cluster needs **outbound HTTPS** access to:

- `api2.cursor.sh`
- `api2direct.cursor.sh`
- `downloads.cursor.com`

No inbound ports or firewall rules are required.

***

## Step 1: Install the controller

```bash
helm upgrade --install worker-set-controller \
  oci://public.ecr.aws/j6w0t2f5/cursor/worker-set-controller-chart \
  --namespace cursord --create-namespace \
  --version 0.1.0-6c804a0 \
  --set imageTag=6c804a0 \
  --set env.enableAuthManagement=true
```

`spec.auth` only works when the controller starts with `--enable-auth-management=true`, which enables secret management from the controller. In Helm, set `env.enableAuthManagement=true`.

By default, the controller watches `WorkerDeployment` resources across all namespaces and the chart creates cluster-wide controller RBAC. To run the controller only in the release namespace, add `--set rbac.singleNamespace=true`:

```bash
helm upgrade --install worker-set-controller \
  oci://public.ecr.aws/j6w0t2f5/cursor/worker-set-controller-chart \
  --namespace cursord --create-namespace \
  --version 0.1.0-6c804a0 \
  --set imageTag=6c804a0 \
  --set env.enableAuthManagement=true \
  --set rbac.singleNamespace=true
```

In single-namespace mode, the chart renders a namespace-scoped `Role` and `RoleBinding` instead of the controller `ClusterRole` and `ClusterRoleBinding`, then starts the controller with `--watch-namespace=<release namespace>`. The `WorkerDeployment` CRD is still cluster-scoped. If the installer shouldn't manage cluster-scoped resources, install the CRD separately and set `crd.install=false`.

Verify the controller is running:

```bash
kubectl -n cursord rollout status deployment/worker-set-controller
```

***

## Step 2: Create the auth secret

Create a Kubernetes secret and bind it to the `WorkerDeployment` by label:

```bash
kubectl create secret generic my-workers-api-key \
  --from-literal=api-key='YOUR_SERVICE_ACCOUNT_API_KEY' \
  -n cursord
kubectl label secret my-workers-api-key -n cursord \
  workers.cursor.com/worker-deployment=my-workers
```

The label value must exactly match `metadata.name` on the `WorkerDeployment`. The controller refuses to read unbound secrets.

Kubernetes workers use this secret through controller-managed auth. The controller exchanges the key for a short-lived token and mounts it at:

```text
/var/run/cursor/token
```

The worker authenticates with `--auth-token-file /var/run/cursor/token`. When the token expires or the connection drops, the CLI reads this file again before reconnecting. This lets the controller rotate tokens without restarting the pod.

***

## Step 3: Create a worker pool

Your worker image must have:

- `agent` CLI installed
- `git` installed and available on `PATH`
- A cloned repository with a configured remote as the working directory

To install the CLI:

```bash
curl https://cursor.com/install -fsS | bash
```

Inside the `WorkerDeployment` pod, start the worker with `--pool`, `--idle-release-timeout`, and the controller-managed token file:

```bash
agent worker \
  --pool \
  --idle-release-timeout 600 \
  --auth-token-file /var/run/cursor/token \
  start
```

`--pool` registers each worker for pool assignment, where each Cloud Agent session claims one worker at a time. `--idle-release-timeout` (in seconds) keeps the worker alive briefly after the session ends for follow-up messages, then exits with code 0 so the pod gets replaced.

Workers deployed on Kubernetes support the same hooks model as [Self-Hosted
Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#hooks). They run project hooks from
`.cursor/hooks.json` and, on Enterprise, also support team hooks and
enterprise-managed hooks.

Example `WorkerDeployment` (adapt to your own setup):

The sample resource request below is a placeholder. `1` CPU and `2Gi` memory
are enough to boot the agent process, but you should size workers for the repo,
build, and test workload you expect them to run.

```yaml
apiVersion: workers.cursor.com/v1
kind: WorkerDeployment
metadata:
  name: my-workers
  namespace: cursord
spec:
  auth:
    apiKeySecretRef:
      name: my-workers-api-key
      key: api-key
    workerContainerName: worker
  readyReplicas: 5
  template:
    metadata:
      labels:
        app: my-worker
    spec:
      containers:
        - name: worker
          image: YOUR_IMAGE
          command: ["agent"]
          args:
            - "worker"
            - "--pool"
            - "--idle-release-timeout"
            - "600"
            - "--worker-dir"
            - "/path/to/your/repo"
            - "--auth-token-file"
            - "/var/run/cursor/token"
            - "--management-addr"
            - "0.0.0.0:8080"
            - "start"
          readinessProbe:
            httpGet:
              path: /readyz
              port: 8080
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8080
            periodSeconds: 10
          resources:
            requests:
              cpu: "1"
              memory: 2Gi
```

Apply the WorkerDeployment:

```bash
kubectl apply -f workers.yaml
```

***

## Step 4: Verify workers are running

Check the worker pool status:

```bash
kubectl get wd -n cursord
```

```bash
NAME         READY   DESIRED   TOTAL   AVAILABLE   REVISION           AGE
my-workers   3       3         3       True        a1b2c3d4e5f6g7h8   2m
```

Your workers should also appear in the **Self-Hosted** section of your [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents).

***

## Scaling

To change the number of workers, update `readyReplicas` in your `WorkerDeployment`:

```bash
kubectl patch wd my-workers -n cursord --type merge \
  -p '{"spec":{"readyReplicas": 20}}'
```

The controller scales in batches and **never terminates busy workers**. Pods actively processing agent work are preserved until they finish.

***

## Rolling updates

When you change the pod template (e.g. update the image, environment variables, or resource limits), the controller performs a safe rolling update:

1. Creates new-revision pods in batches
2. Waits for them to become ready
3. Drains old-revision pods that are idle
4. Preserves old-revision pods that are busy until they finish

Agent sessions are never interrupted by deployments.

***

## Worker labels

Use [Cursor worker labels](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#labels) to make workers selectable for specific teams, repos, or environments. These are separate from Kubernetes pod labels. They're passed as `--label` flags to the `agent` CLI and control which workers are eligible for a given session.

Inside the `WorkerDeployment` pod, pass labels with the worker args:

```bash
agent worker \
  --pool \
  --idle-release-timeout 600 \
  --auth-token-file /var/run/cursor/token \
  --label team=backend \
  --label env=production \
  start
```

Users select which worker pool to use from the Cloud Agents dropdown in Cursor.

## Health checks

The `--management-addr` flag in the WorkerDeployment exposes health check endpoints for Kubernetes readiness and liveness probes:

| Endpoint   | 200                | 503                               |
| ---------- | ------------------ | --------------------------------- |
| `/healthz` | Process is running | Never                             |
| `/readyz`  | Connected and idle | Starting up, or running a session |

The `/readyz` endpoint is the key integration point:

1. A worker starts and connects. `/readyz` returns 200.
2. A session claims the worker. `/readyz` flips to 503. Kubernetes removes it from the ready pool and spins up a replacement.
3. The session ends. The worker exits with code 0. The controller replaces the pod to maintain `readyReplicas`.

Busy workers are never terminated, even during scale-down or rolling updates.

***

## Related

- [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [Cloud Agents overview](https://cursor.com/docs/cloud-agent.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
