---
source_url: https://cursor.com/docs/cloud-agent/setup
---

# Setup

Cloud agents run on an isolated Ubuntu machine. We recommend configuring this environment so the agent has access to the same tools a human developer would use.

Go to [cursor.com/onboard](https://cursor.com/onboard) to configure your environment.

## Environment Options

There are two main ways to configure the environment for your cloud agent:

1. Let Cursor's agent set up its own environment at [cursor.com/onboard](https://cursor.com/onboard). After the agent is done, you will have the option to create a snapshot of its virtual machine that can be reused for future agents.
2. Manually configure the environment with a Dockerfile. If you choose this option, you can specify the Dockerfile in a `.cursor/environment.json` file.

Both options generate an environment, and also allow you to specify an update command that will be run before the agent starts to ensure that its dependencies are up to date (e.g. `npm install`, `pip install`, etc.).

### Environment resolution order

Cursor resolves environment configuration in this order, using the first match:

1. `.cursor/environment.json` in the repository
2. Personal environment configuration
3. Team environment configuration

This gives you predictable defaults at the team level while still letting individual users override with a personal environment when a repo-level `.cursor/environment.json` is not present. User overrides are also useful to allow testing out a new environment configuration before rolling it out to the entire team.

### Agent-driven setup (recommended)

You will be asked to connect your GitHub or GitLab account and select the repository you want to work on.

Then, you provide Cursor with the environment variables and secrets it will need to install dependencies and run the code.

Finally, after Cursor has installed the dependencies and verified the code is working, you can save a snapshot of its virtual machine to be reused for future agents.

### Manual setup with Dockerfile (advanced)

For advanced cases, configure the environment with a Dockerfile:

- Create a Dockerfile to install system-level dependencies, use specific compiler versions, install debuggers, or switch the base OS image
- Do not `COPY` the full project; Cursor manages the workspace and checks out the correct commit
- Edit `.cursor/environment.json` directly to configure runtime settings

Here's an example `.cursor/environment.json` referencing a `.cursor/Dockerfile` (relative path) and a `custom_script.sh` install script:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

If your repo needs Docker or Tailscale, see [Running Docker](https://cursor.com/docs/cloud-agent/setup.md#running-docker) and [Running Tailscale](https://cursor.com/docs/cloud-agent/setup.md#running-tailscale) below.

You configure the environment with a Dockerfile; you do not get direct access to the remote machine.

### Computer Use Support for Dockerfile Repos

Computer use is supported for repos with Dockerfiles based on Debian/Ubuntu-based Linux distributions. If you require support for a different Linux distribution, please contact support.

### Resource limits

Each cloud agent runs on a default VM profile with limited memory and CPU. If you are on an Enterprise plan and your repo needs more resources, contact support and we can increase limits for your workspace.

Self-serve custom resource configuration is coming soon.

## Update command

When a new machine boots, Cursor starts from the base environment, then runs the `update` command (called `install` in `environment.json`).

For most repos, the `update` script is `npm install`, `bazel build`, or a similar dependency setup command.

### Update script idempotency

The `update` script must be idempotent. It can run more than once, and it may run on partially cached state.

### How caching works

After `update` completes, if it took more than a few seconds to run, Cursor will take an internal checkpoint snapshot and will attempt to start future cloud agents from this checkpoint.

This is why `update` commands like `pnpm install` usually lead to fast startup - if dependencies changed, the command only needs to do incremental work.

Caching is best effort; you may see slower startup times on infrequently used repositories.

### How to decide what to put in your `update` script

There is a tradeoff between caching work in `update` and doing setup on demand during a run.

Placing infrequently run or expensive commands (such as starting services or building docker images) in `update` can slow down startup time.

A practical pattern is to run basic cached dependency updates (such as `pnpm install`) in your `update` script, then [adding instructions in AGENTS.md](https://cursor.com/docs/cloud-agent/setup.md#add-cloud-specific-instructions-to-agentsmd) so the agent can figure out which commands it needs to run for each specific task.

## Startup commands

After `install`, the machine starts and runs the `start` command, then any configured `terminals`. Use this to start processes that should stay alive while the agent runs.

You can skip `start` in many repos. If your environment depends on Docker, add `sudo service docker start` in `start`.

`terminals` are for app code processes. These terminals run in a `tmux` session shared by you and the agent.

## Add cloud-specific instructions to `AGENTS.md`

Cloud agents read `AGENTS.md` files. We recommend adding a dedicated section for Cloud-only setup and testing instructions, with a title such as `Cursor Cloud specific instructions`.

If this section gets large, we recommend including references to other files that can contain detailed instructions for specific tasks.

See our [AGENTS.md docs](https://cursor.com/docs/rules.md#agentsmd) for more information.

## Environment variables and secrets

Cloud agents need environment variables and secrets such as API keys and database credentials.

### Recommended: use the Secrets tab in Cursor settings

The easiest way to manage secrets is through [cursor.com](https://cursor.com/dashboard/cloud-agents).

Add secrets as key-value pairs. Secrets are:

- Encrypted at rest with KMS
- Exposed to cloud agents as environment variables
- Shared across cloud agents for your workspace or team

As an additional level of security, you have the option to specify secrets as redacted. Redacted secrets are scanned in commits the agent makes to prevent the agent from accidentally committing secrets to the repository. They are also redacted in the tool call results so they are not exposed to the agent, or stored in the chat transcript.

### Sign-in credentials and 2FA

If your app requires login, add the same credentials you use locally as secrets, such as a username, email, and password.

If your login flow uses TOTP-based 2FA, add the TOTP secret, sometimes called the shared or root secret, as a secret too. The agent can generate the current 6-digit code with `oathtool --totp -b "$TOTP_SECRET"`.

### Monorepos with multiple `.env` files

If your monorepo has multiple `.env.local` files:

- Add values from all `.env.local` files to the same Secrets tab
- Use unique variable names when keys overlap, such as `NEXTJS_*` and `CONVEX_*`
- Reference those variables from each app as needed

If you include `.env.local` files while taking a snapshot, they can be saved and available to cloud agents. The Secrets tab remains the recommended approach for security and management.

### Using AWS IAM Roles

Cursor supports assuming customer-provided IAM roles for deeper integration with AWS. This allows you to grant specific AWS permissions to cloud agents without sharing long-lived credentials.

1. **Create the IAM role**: In your AWS account, create the IAM role that you'd like the cloud agent to assume, and note its ARN (e.g. `arn:aws:iam::123456789012:role/acmeRole`).

2. **Configure the IAM role secret**: Navigate to [Cursor Dashboard → Cloud Agents](https://cursor.com/dashboard?tab=cloud-agents), and add a user or team secret named `CURSOR_AWS_ASSUME_IAM_ROLE_ARN` set to the ARN of the IAM role you created.

3. **Generate an external ID**: Navigate to [Cursor Dashboard → Settings](https://cursor.com/dashboard?tab=settings) and find the External ID settings. If you don't see an external ID displayed, enter a placeholder value in the "AWS IAM Role ARN" field, click "Validate & Save", and reload the page. This will generate an external ID for your team (e.g. `cursor-xxx-yyy-zzz`).

4. **Configure IAM role trust policy**: In your AWS account, update the IAM role's trust policy to trust Cursor's role assumer. The trust policy should look like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCursorAssume",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::289469326074:role/roleAssumer"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "cursor-xxx-yyy-zzz"
        }
      }
    }
  ]
}
```

Replace `cursor-xxx-yyy-zzz` with the external ID generated for your team.

**Environment variables:**

When configured, Cursor sets these environment variables so AWS tooling uses the `cursor-cloud-agent` profile:

- `AWS_CONFIG_FILE` points to a Cursor-managed AWS config file
- `AWS_PROFILE` is set to `cursor-cloud-agent`
- `AWS_SDK_LOAD_CONFIG` is set to `1`

The AWS CLI and AWS SDKs that use the default credential chain pick up this profile automatically during setup commands and while the agent is running. You don't need to export `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN` yourself.

Cursor assumes the role with STS credentials that expire after 1 hour.
When the agent wakes, Cursor refreshes credentials that are missing, invalid, or within 15 minutes of expiration.

## Configuration in code with environment.json

If you prefer to keep your environment configuration defined in code, you can commit a `.cursor/environment.json` to your repository.

Cloud agents will use the configuration at the commit they start from, so to test a new configuration, you can commit and push the change to a new branch, and start a cloud agent from that branch.

Sample `environment.json` using a snapshot-based config (the snapshot ID is accessible from the environments page of the dashboard):

```json
{
  "snapshot": "snapshot-20260212-00000000-0000-0000-0000-000000000000",
  "install": "npm install"
}
```

Here is a sample `.cursor/environment.json` referencing a `.cursor/Dockerfile` (relative path) and a `custom_script.sh` install script:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

### Important path behavior

The `dockerfile` and `context` paths in `build` are relative to `.cursor`.
The `install` command runs from your project root.

The full schema is [defined here](https://www.cursor.com/schemas/environment.schema.json).

## Running Docker

Cloud agents support Docker workflows. We use this internally for full-stack repos that run many services.

For simple setups, installing Docker is often enough. Commands like `docker run hello-world` usually work once Docker is installed and the daemon is running.

Docker has edge cases in Cloud Agents because it runs inside another container layer. Simple workflows usually work. More complex setups should start from the `fuse-overlayfs` and `iptables-legacy` configuration below.

For more complex Docker setups, use `fuse-overlayfs`, `iptables-legacy`, and make sure your cloud agent user can run Docker.

### Recommended Dockerfile for complex Docker setups

```docker
########################################################
# DOCKER INSTALLATION
########################################################

# Install Docker
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl --retry 3 --retry-delay 5 -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y \
    docker-ce=5:28.5.2-1~ubuntu.24.04~noble \
    docker-ce-cli=5:28.5.2-1~ubuntu.24.04~noble \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y fuse-overlayfs && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /etc/docker && \
    printf '%s\n' '{' \
    '  "storage-driver": "fuse-overlayfs"' \
    '}' > /etc/docker/daemon.json
RUN apt-get update && apt-get install -y iptables && rm -rf /var/lib/apt/lists/*
RUN update-alternatives --set iptables /usr/sbin/iptables-legacy && \
    update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy

########################################################
# CONFIG UBUNTU USER
########################################################

# ensure no password authentication
RUN echo 'PasswordAuthentication no\nChallengeResponseAuthentication no\nUsePAM no' > /etc/ssh/sshd_config.d/disable_password_auth.conf

# Create non-root user (only if it doesn't exist)
RUN id -u ubuntu &>/dev/null || useradd -m -s /bin/bash ubuntu
# Create docker group if it doesn't exist and add ubuntu user to it
RUN groupadd -f docker && usermod -aG docker ubuntu
RUN usermod -aG sudo ubuntu
# Configure passwordless sudo for ubuntu user
RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu
# Set a password for ubuntu user
RUN echo "ubuntu:ubuntu" | chpasswd
```

After Docker is installed, add `sudo service docker start` to your `start` command so the daemon is available before the agent begins work.

## Running Tailscale

Tailscale does not work in its default networking mode in Cloud agent VMs. Use userspace networking mode instead.

Start `tailscaled` with:

```bash
tailscaled --tun=userspace-networking \
  --outbound-http-proxy-listen=localhost:1054 \
  --socks5-server=localhost:1055
```

Then export these proxy variables in the shell where you want traffic to flow through Tailscale:

```bash
export ALL_PROXY=socks5h://localhost:1055/
export HTTP_PROXY=http://localhost:1054/
export HTTPS_PROXY=http://localhost:1054/
```

After that, run your usual `tailscale up ...` flow.

If you want a working reference, some customers have used [`tailscale-orb`](https://circleci.com/developer/orbs/orb/orbiously/tailscale#commands-connect) successfully because its Docker mode follows this pattern.

Userspace networking does not let the VM appear as a tailnet exit node.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
