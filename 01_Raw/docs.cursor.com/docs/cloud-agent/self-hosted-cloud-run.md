---
source_url: https://cursor.com/docs/cloud-agent/self-hosted-cloud-run
fetched_at: 2026-05-11T04:55:36.768477+00:00
fetch_method: mintlify_md
---

# Self-Hosted Cloud: Deploying with Cloud Run Worker Pools

Deploy and manage [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md) workers on Google Cloud using [Cloud Run Worker Pools](https://cloud.google.com/run/docs/deploying-worker-pools). A second Worker Pool runs a custom autoscaler that polls the Cursor [fleet management API](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#fleet-management-api) and scales the worker pool up or down based on utilization.

This guide covers a minimal reference setup. Adapt the image contents, secrets, and autoscaling logic to match your own infrastructure.

## Architecture

Two Cloud Run Worker Pools work together:

- **Cursor worker pool.** Each instance runs a container that starts the `agent` CLI as a pool worker and holds an outbound HTTPS connection to Cursor. Sessions are routed to idle instances.
- **Autoscaler pool.** A single-instance Worker Pool that polls `https://api.cursor.com/v0/private-workers/summary` on an interval and calls the Cloud Run Admin API to resize the worker pool based on utilization.

## Prerequisites

- A Google Cloud project with billing enabled
- `gcloud` CLI installed and authenticated (`gcloud auth login`, `gcloud config set project <PROJECT_ID>`)
- The following APIs enabled in your project: Cloud Run (`run.googleapis.com`), Artifact Registry (`artifactregistry.googleapis.com`), Cloud Build (`cloudbuild.googleapis.com`), and Secret Manager (`secretmanager.googleapis.com`)
- A Cursor team plan with Self-Hosted Cloud Agents enabled
- A Cursor team-level API key — see [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#authenticate-workers) for authentication setup
- A Git token (e.g. a GitHub personal access token or fine-grained token) with read/write access to the repositories your agents will operate on

Your worker pool needs **outbound HTTPS** access to:

- `api2.cursor.sh`
- `api2direct.cursor.sh`
- `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` (for [artifact](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#artifacts) uploads)
- Your git host (for example `github.com`) and any package registries your builds need

No inbound ports or firewall rules are required.

***

## Step 1: Prepare your environment

Set the environment variables used throughout this guide:

```bash
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION="us-central1"
export REPO_NAME="cursor-workers"
export IMAGE_NAME="cursor-agent-worker"
export SCALER_IMAGE_NAME="cursor-agent-scaler"
export CURSOR_AGENTS_POOL="cursor-agents-pool"
```

***

## Step 2: Build the worker container

Create a directory for the worker image and add the two files below.

### `Dockerfile`

```dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# - curl/ca-certificates: to download the Cursor CLI
# - git: required by the worker to identify and operate on the repo
# - build-essential/python3/nodejs: common tools the agent might need
RUN apt-get update && \
    apt-get install -y \
      curl \
      git \
      ca-certificates \
      build-essential \
      python3 \
      nodejs \
      npm \
    && rm -rf /var/lib/apt/lists/*

# Install the Cursor Agent CLI
RUN curl -fsSL https://cursor.com/install | bash

# Ensure the 'agent' binary is available in PATH
ENV PATH="/root/.cursor/bin:/root/.local/bin:/usr/local/bin:$PATH"

WORKDIR /workspace

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Cloud Run injects the PORT env var (default 8080). The management/health
# server binds to it so Cloud Run's TCP health checks pass.
ENV PORT=8080

ENTRYPOINT ["/entrypoint.sh"]
```

### `entrypoint.sh`

```bash
#!/bin/bash
set -e

# Disable git terminal prompts so the container crashes cleanly if auth fails
# instead of hanging.
export GIT_TERMINAL_PROMPT=0

if [ -z "$CURSOR_API_KEY" ]; then
  echo "FATAL: CURSOR_API_KEY environment variable is missing."
  exit 1
fi

if [ -z "$REPO_URL" ]; then
  echo "FATAL: REPO_URL environment variable is missing."
  echo "Example: https://github.com/your-org/your-repo.git"
  exit 1
fi

# Configure Git authentication for private repos.
if [ -n "$GIT_TOKEN" ]; then
  echo "Configuring git credentials using provided GIT_TOKEN..."
  git config --global credential.helper "!f() { echo username=oauth2; echo password=$GIT_TOKEN; }; f"
fi

REPO_DIR="/workspace/repo"
if [ ! -d "$REPO_DIR/.git" ]; then
  echo "Cloning repository: $REPO_URL..."
  git clone "$REPO_URL" "$REPO_DIR"
fi

# Cursor workers require the CWD to be the git repo.
cd "$REPO_DIR"

AGENT_BIN=$(command -v agent || find /root -name agent -type f | head -n 1)
if [ -z "$AGENT_BIN" ]; then
  echo "FATAL: Could not find the Cursor 'agent' binary."
  exit 1
fi

echo "Starting Cursor Cloud Agent Worker..."

# - `exec` replaces the shell so the agent handles container termination signals.
# - `--management-addr` binds to Cloud Run's PORT for TCP health checks.
# - `"$@"` forwards extra flags (for example `--pool-name`) passed at deploy time.
exec "$AGENT_BIN" worker start \
  --api-key "$CURSOR_API_KEY" \
  --management-addr ":${PORT}" \
  --pool \
  --idle-release-timeout 600 \
  "$@"
```

`--pool` registers the worker for pool assignment, where each Cloud Agent
session claims one worker at a time. `--idle-release-timeout` (in seconds)
keeps the worker alive briefly after the session ends for follow-up
messages, then exits with code 0 so Cloud Run replaces the instance.

Cloud Run workers support the same [hooks model](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#hooks) as other Self-Hosted Pool workers. They run project hooks from `.cursor/hooks.json`, and on Enterprise also support team hooks and enterprise-managed hooks.

***

## Step 3: Create an Artifact Registry repository

Create a Docker repository to host both images:

```bash
gcloud artifacts repositories create $REPO_NAME \
  --repository-format=docker \
  --location=$LOCATION \
  --description="Docker repository for Cursor self-hosted agents"
```

***

## Step 4: Build and push the worker image

From the directory containing the `Dockerfile` and `entrypoint.sh`:

```bash
gcloud builds submit \
  -t $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest .
```

If you'd rather not build and push the image ahead of time, you can use Cloud Run's source deploy in Step 6 instead.

***

## Step 5: Create secrets

Store the Cursor API key and Git token in Secret Manager so they're never baked into images.

### `CURSOR_API_KEY`

```bash
gcloud secrets create CURSOR_API_KEY --replication-policy="automatic"

echo -n "YOUR_CURSOR_API_KEY" | \
  gcloud secrets versions add CURSOR_API_KEY --data-file=-
```

### `GIT_TOKEN`

```bash
gcloud secrets create GIT_TOKEN --replication-policy="automatic"

echo -n "YOUR_GIT_TOKEN" | \
  gcloud secrets versions add GIT_TOKEN --data-file=-
```

Grant your Git token the permissions the worker needs. For most agent workflows, that means **read and write** access to contents and the ability to open and merge pull requests on the repositories the workers operate on.

***

## Step 6: Deploy the Cursor worker as a Worker Pool

```bash
gcloud run worker-pools deploy $CURSOR_AGENTS_POOL \
  --image $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:latest \
  --region $LOCATION \
  --set-env-vars="REPO_URL=https://github.com/your-org/your-repo.git" \
  --set-secrets="CURSOR_API_KEY=CURSOR_API_KEY:latest,GIT_TOKEN=GIT_TOKEN:latest"
```

Replace `REPO_URL` with the git URL of the repository this pool should serve.

Once the pool rolls out, its workers should appear in the **Self-Hosted** section of the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents).

Each worker serves one repository. To support multiple repositories, deploy
an additional Cloud Run Worker Pool per repo and use [pool
names](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#pool-names) or
[labels](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#labels) to route agent sessions
to the right pool.

***

## Step 7: Deploy the autoscaler

The worker pool is deployed with a static instance count. To scale based on utilization, deploy a small Node.js app as a second Worker Pool that polls the Cursor fleet management API and calls the Cloud Run Admin API to resize the worker pool.

Create a directory for the autoscaler and add the three files below.

### `package.json`

```json
{
  "name": "cursor-worker-autoscaler",
  "version": "1.0.0",
  "description": "Autoscaler for Cursor Cloud Run Worker Pools",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "@google-cloud/run": "latest"
  }
}
```

### `index.js`

```javascript
const { WorkerPoolsClient } = require('@google-cloud/run').v2;

const CURSOR_API_KEY = process.env.CURSOR_API_KEY;
const PROJECT_ID = process.env.GOOGLE_CLOUD_PROJECT;
const LOCATION = process.env.CLOUD_RUN_LOCATION;
const TARGET_POOL_NAME = process.env.WORKER_SERVICE_NAME;

const TARGET_UTILIZATION = parseFloat(process.env.TARGET_UTILIZATION || '0.5');
const MIN_INSTANCES = parseInt(process.env.MIN_INSTANCES || '1', 10);
const MAX_INSTANCES = parseInt(process.env.MAX_INSTANCES || '50', 10);
const POLLING_INTERVAL_MS = parseInt(process.env.POLLING_INTERVAL_MS || '30000', 10);

if (!PROJECT_ID || !LOCATION || !TARGET_POOL_NAME) {
  console.error('FATAL: Missing required environment variables.');
  process.exit(1);
}

const workerPoolClient = new WorkerPoolsClient();

async function scaleCursorWorkers() {
  try {
    const response = await fetch('https://api.cursor.com/v0/private-workers/summary', {
      method: 'GET',
      headers: {
        'Authorization': 'Basic ' + Buffer.from(`${CURSOR_API_KEY}:`).toString('base64'),
      },
    });

    if (!response.ok) {
      throw new Error(`Cursor API responded with status: ${response.status}`);
    }

    const summary = await response.json();
    const team = summary.teamSummary;
    const user = summary.userSummary;

    let inUse = 0;
    let totalConnected = 0;

    if (team && team.totalConnected > 0) {
      inUse = team.inUse;
      totalConnected = team.totalConnected;
    } else if (user && user.totalConnected > 0) {
      inUse = user.inUse;
      totalConnected = user.totalConnected;
    } else {
      console.log('Current state: 0 workers connected. Waiting for next cycle...');
      return;
    }

    console.log(`Current state: ${inUse} workers in use out of ${totalConnected} total connected.`);

    let desiredInstances = Math.ceil(inUse / TARGET_UTILIZATION);
    desiredInstances = Math.max(MIN_INSTANCES, Math.min(desiredInstances, MAX_INSTANCES));

    if (desiredInstances !== totalConnected) {
      console.log(`Utilization threshold breached. Scaling Worker Pool from ${totalConnected} to ${desiredInstances} instances...`);
      await updateCloudRunWorkerPool(desiredInstances);
    } else {
      console.log('Utilization is stable. No scaling action required.');
    }
  } catch (error) {
    console.error('Error in scaling execution:', error);
  }
}

async function updateCloudRunWorkerPool(instanceCount) {
  const workerPoolPath = workerPoolClient.workerPoolPath(PROJECT_ID, LOCATION, TARGET_POOL_NAME);

  const request = {
    workerPool: {
      name: workerPoolPath,
      scaling: {
        manualInstanceCount: instanceCount,
      },
    },
    updateMask: {
      paths: ['scaling.manual_instance_count'],
    },
  };

  const [operation] = await workerPoolClient.updateWorkerPool(request);
  console.log('Waiting for Cloud Run scaling operation to apply...');
  await operation.promise();
  console.log(`Successfully patched Cloud Run Worker Pool. Pool scaled to ${instanceCount} workers.`);
}

console.log(`Starting background autoscaler loop (Interval: ${POLLING_INTERVAL_MS}ms)`);
scaleCursorWorkers();
setInterval(scaleCursorWorkers, POLLING_INTERVAL_MS);
```

### `Dockerfile`

```dockerfile
FROM node:20-alpine

WORKDIR /usr/src/app

COPY package.json ./
RUN npm install --omit=dev

COPY index.js ./

CMD ["npm", "start"]
```

### Build and deploy the autoscaler

Optionally build and push the image first:

```bash
gcloud builds submit \
  -t $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$SCALER_IMAGE_NAME:latest .
```

Or skip the build step and let Cloud Run build from source on deploy:

```bash
gcloud run worker-pools deploy cursor-autoscaler-pool --project $PROJECT_ID \
  --region $LOCATION \
  --source . \
  --instances 1 \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=$PROJECT_ID,CLOUD_RUN_LOCATION=$LOCATION,WORKER_SERVICE_NAME=$CURSOR_AGENTS_POOL,MIN_INSTANCES=1,MAX_INSTANCES=10,TARGET_UTILIZATION=0.5,POLLING_INTERVAL_MS=30000" \
  --set-secrets="CURSOR_API_KEY=CURSOR_API_KEY:latest"
```

The autoscaler's service account needs permission to update the worker pool. Grant it the **Cloud Run Admin** role (or a more scoped custom role) on the project, or directly on the `$CURSOR_AGENTS_POOL` resource.

### Autoscaler configuration

| Variable               | Default | Description                                                                  |
| ---------------------- | ------- | ---------------------------------------------------------------------------- |
| `GOOGLE_CLOUD_PROJECT` | —       | Project ID that hosts the worker pool.                                       |
| `CLOUD_RUN_LOCATION`   | —       | Region of the worker pool, for example `us-central1`.                        |
| `WORKER_SERVICE_NAME`  | —       | Name of the Cursor worker pool to scale.                                     |
| `CURSOR_API_KEY`       | —       | Team-level Cursor API key used to query the fleet management API.            |
| `TARGET_UTILIZATION`   | `0.5`   | Desired fraction of workers in use. Lower values scale up more aggressively. |
| `MIN_INSTANCES`        | `1`     | Floor on the worker pool size.                                               |
| `MAX_INSTANCES`        | `50`    | Ceiling on the worker pool size.                                             |
| `POLLING_INTERVAL_MS`  | `30000` | How often to poll the Cursor API and reconcile.                              |

***

## Testing

Once the worker pool is running:

1. Go to [cursor.com/agents](https://cursor.com/agents).
2. Select **Self-hosted** from the worker selector.
3. Your Cloud Run workers should appear in the list of available workers.
4. Start a task, and the agent will execute its tool calls inside your Cloud Run containers.

You can also verify workers are connected from the command line using the [fleet management API](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#fleet-management-api):

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

***

## Related

- [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted-k8s.md)
- [Cloud Agents overview](https://cursor.com/docs/cloud-agent.md)
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
