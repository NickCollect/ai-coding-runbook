---
type: summary
source: 01_Raw/github/anthropics/claude-quickstarts/customer-support-agent/README.md
source_url: https://github.com/anthropics/claude-quickstarts/blob/main/customer-support-agent/README.md
title: "Claude Quickstarts — customer-support-agent README"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway]
concepts_referenced: []
---

Advanced, fully customizable customer-support chat interface powered by Claude with Amazon Bedrock Knowledge Bases for retrieval.

**Key features.** AI-powered chat using Claude; Amazon Bedrock integration for contextual knowledge retrieval; real-time thinking/debug info display; knowledge-base source visualization; user mood detection with appropriate agent redirection; customizable UI with shadcn/ui components.

**Setup.** Clone the repo, `npm install`, configure env vars, `npm run dev`, open http://localhost:3000.

**Configuration.** Create `.env.local` with `ANTHROPIC_API_KEY`, `BAWS_ACCESS_KEY_ID`, `BAWS_SECRET_ACCESS_KEY`. The `B` prefix in front of AWS env vars is intentional and discussed in the deployment section.

**Getting keys.** Anthropic key from console.anthropic.com. AWS keys via IAM: create a user, attach `AmazonBedrockFullAccess` policy directly, create an access key for "Application running on an AWS compute service", capture the Access Key ID + Secret Access Key once at creation. Never share keys publicly.

**Bedrock RAG integration.** Requires an AWS account with Bedrock access. Create a Bedrock knowledge base in your region, index documents/sources, then update the `knowledgeBases` array in `ChatArea.tsx` with your KB IDs and names:

```ts
const knowledgeBases: KnowledgeBase[] = [
  { id: "your-knowledge-base-id", name: "Your KB Name" },
];
```

**Creating a knowledge base.** From AWS Console → Amazon Bedrock → Knowledge base → Create. Pick a source (S3 example uses an existing bucket; can also upload after creation). Walks through the setup with screenshots.

The README continues with deployment instructions, UI customization (sidebar variants), and architecture notes for the Next.js + shadcn/ui stack.
