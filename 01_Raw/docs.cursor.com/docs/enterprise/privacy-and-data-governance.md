---
source_url: https://cursor.com/docs/enterprise/privacy-and-data-governance
fetched_at: 2026-06-15T06:17:45.357407+00:00
fetch_method: mintlify_md
---

# Privacy and Data Governance

Understanding how data flows through Cursor is critical for security reviews and compliance assessments. This documentation explains what data goes where, what guarantees you have, and where that data lives geographically.

## Three data flows

There are three ways data leaves your local environment when using Cursor:

### 1. The indexing process

When you open a project in Cursor, we create embeddings that represent your code. These embeddings power semantic search across your codebase.

**What gets sent:**

- Your code, temporarily, to create embeddings
- Nothing is stored; embeddings are generated and the original code is discarded

**What gets stored:**

- One-way mathematical embeddings (vectors) that represent code semantics
- Obfuscated file paths
- Line numbers

**How it works:**
When you ask a question or use Cmd K, we create an embedding from your request and search for similar embeddings in the vector database. The search returns obfuscated file paths and line numbers. We then look up the actual code on your local machine using those coordinates.

The vector database never sees your raw code. It only stores mathematical representations that can't be reverse-engineered back to source code.

### 2. LLM requests

When you use AI features, we send prompts and code context to language model providers like OpenAI, Anthropic, and Google. If you are using Cursor's custom models (e.g. Composer), your data may also be processed by our inference providers. See our list of [sub-processors](https://trust.cursor.com/subprocessors).

**With Privacy Mode enabled** your code is never used for training by Cursor or other AI model providers.

Privacy Mode is on by default for Enterprise teams. See [Privacy Overview](https://cursor.com/privacy-overview) for details.

### 3. Cloud Agents

Cloud Agents are the only feature that requires Cursor to store code. Unlike the indexing process or LLM requests, Cloud Agents need access to your repository over time to make changes.

**Architecture:**

- Agents run in isolated virtual machines
- Each agent has a dedicated environment
- Isolated from other agents and users

**What gets stored:**

- Encrypted copies of repositories that Cloud Agents work on
- Stored temporarily while the agent runs
- Deleted after the agent completes

Cloud Agents are optional. If your security policy prohibits code storage, don't enable Cloud Agents. You can still use all other Cursor features.

See [Cloud Agents](https://cursor.com/docs/cloud-agent.md) for details.

## Models with data retention

Most models run under Cursor's ZDR agreements, so providers don't store inputs or outputs or train on your data ([read more](https://cursor.com/data-use) about our data use policies). A few models require data retention with the provider and fall outside these agreements. For Enterprise customers, Teams with Privacy Mode enabled, and individual customers with Privacy Mode enabled, Cursor requires admin approval before use.

[Claude Fable 5](https://cursor.com/docs/models/claude-fable-5.md) works this way. Anthropic stores its inputs and outputs to run automatic and human harm-prevention reviews. This data is not used for training or product improvement. For Enterprise customers and customers with Privacy Mode enabled, requests to Fable 5 fail until the model's data retention policy is approved from the [dashboard](https://cursor.com/dashboard/restricted_models/claude-fable-5). Opting in applies to the whole team. Enterprise admins can still limit which user groups can select the model with [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

When a Fable 5 request trips one of its security guardrails, Cursor routes that request to Claude Opus automatically so your work continues.

## Privacy Mode enforcement

Privacy Mode can be enabled at the team level to ensure all team members benefit from ZDR guarantees.

**Team-level enforcement:**

1. Go to your [team dashboard](https://cursor.com/dashboard)
2. Navigate to Settings
3. Enable Privacy Mode for the team
4. Optionally enforce it so members can't disable it

**MDM enforcement:**
For additional assurance, use the Allowed Team IDs policy. This prevents users from logging into personal accounts (which might not have Privacy Mode enabled) on corporate devices.

See [Identity and Access Management](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-team-ids) for policy details and [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for MDM configuration.

## Compliance and contracts

Our [DPA](https://cursor.com/terms/dpa) includes comprehensive data protection commitments that follow industry standards, including data minimization, access control, and secure processing.

All [sub-processors](https://trust.cursor.com/subprocessors) are covered by appropriate data processing agreements.

## Data encryption

Cursor encrypts data for all infrastructure, including:

- TLS 1.2+ in transit
- AES-256 at rest

For enhanced security control, enterprise customers can use Customer Managed Encryption Keys (CMEK) for encrypting data stored in Cursor's infrastructure.

With CMEK enabled:

- Embeddings are encrypted using your customer encryption key
- Cloud Agent data is encrypted using your customer encryption key
- You control key rotation and access
- Provides additional layer of security beyond standard encryption

[Contact sales](https://cursor.com/contact-sales?source=docs-cmek) to enable CMEK for your organization.

### Enterprise privacy and data controls

Contact our team to learn about CMEK, Privacy Mode enforcement, and more.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
