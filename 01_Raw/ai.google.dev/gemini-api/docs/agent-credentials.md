---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=bn
fetched_at: 2026-10-26T05:57:07.269630+00:00
title: "\u09ae\u09cd\u09af\u09be\u09a8\u09c7\u099c \u0995\u09b0\u09be \u098f\u099c\u09c7\u09a8\u09cd\u099f\u09a6\u09c7\u09b0 \u0995\u09cd\u09b0\u09c7\u09a1\u09c7\u09a8\u09b6\u09bf\u09df\u09be\u09b2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon এখন উপলভ্য। [এটি ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=bn)।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# ম্যানেজ করা এজেন্টদের ক্রেডেনশিয়াল

ক্রেডেনশিয়াল হল সার্ভার-ম্যানেজ করা সিক্রেট যা আপনার এজেন্টকে থার্ড-পার্টি
পরিষেবায় অ্যাক্সেস করতে দেয়, সিক্রেটটি কখনও এজেন্টের এনভায়রনমেন্টে প্রবেশ করে না। আপনি একবার
ক্রেডেনশিয়াল সেভ করেন, আইডি দিয়ে তা রেফার করেন এবং অনুরোধ করার সময় এগ্রেস প্রক্সি তা সমাধান করে ইনজেক্ট
করে।

গোপন ভ্যালু শুধুমাত্র লেখা যায়। সেগুলি স্টোর করা হয়ে গেলে, কোনও
এন্ডপয়েন্ট আর ফেরত পাঠায় না, তাই কোনও আপস করা এজেন্ট এটি ব্যবহার করছে এমন টোকেন আর পড়তে পারে না।

আপনি যে প্রধান জায়গায় ক্রেডেনশিয়াল ব্যবহার করেন সেটি হল
[`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn)-এ নেটওয়ার্কের অনুমোদিত তালিকা। প্রথমে সিক্রেট সেভ করুন:

### Python

```
from google import genai

client = genai.Client()

credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### জাভাস্ক্রিপ্ট

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});

console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

তারপর, এটি সেই ডোমেনের সাথে অ্যাটাচ করুন যেটি এটি প্রমাণীকরণ করে:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Triage the open issues in my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Triage the open issues in my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ],
        },
    },
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Triage the open issues in my-org/my-repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "api.github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "*"},
                    })),
                })),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Triage the open issues in my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

এজেন্ট এখন `api.github.com`-এ যাচাইকৃত অনুরোধ করে এবং টোকেন
কখনও স্যান্ডবক্সের মধ্যে থাকে না।

## ক্রেডেনশিয়ালের ধরন

প্রতিটি ক্রেডেনশিয়ালের একটি `type` থাকে যা নির্ধারণ করে যে এটি কোন কোন ফিল্ড গ্রহণ করে এবং কীভাবে
প্রক্সি এটি প্রয়োগ করে।

| ধরন | ব্যবহারিক ক্ষেত্র | আচরণ |
| --- | --- | --- |
| `bearer_token` | ব্যক্তিগত অ্যাক্সেস টোকেন, বট টোকেন, স্ট্যাটিক API কী | প্রক্সি টোকেনটি অনুরোধের হেডার হিসেবে ইনজেক্ট করে। কোনও রিফ্রেশ লজিক নেই। |
| `oauth2` | OAuth অ্যাপ ও ব্যবহারকারীর হয়ে কাজ করার ফ্লো | প্রক্সি অ্যাক্সেস টোকেনের জন্য রিফ্রেশ টোকেন এক্সচেঞ্জ করে এবং সেগুলি মেয়াদ শেষ হয়ে গেলে রিফ্রেশ করে। |
| `environment_variable` | প্রসেস এনভায়রনমেন্ট থেকে সিক্রেট রিড করে এমন ক্লায়েন্ট SDK | এজেন্টের এনভায়রনমেন্টে একটি প্লেসহোল্ডার যোগ করা হয়। আউটবাউন্ড অনুরোধে প্রক্সি আসল গোপনীয়তার পরিবর্তে ব্যবহার করা হয়। |

## নেটওয়ার্কের অনুমোদিত তালিকায় ক্রেডেনশিয়াল ব্যবহার করা

সাদাতালিকাভুক্ত নিয়মে `credential` যোগ করুন এবং প্রক্সি সেই ডোমেনে পাঠানো প্রতিটি
আউটবাউন্ড অনুরোধকে যাচাই করে। কোনও ব্যক্তিগত API, ব্যক্তিগত রিপোজিটরি বা ব্যক্তিগত বাকেটে
এজেন্টকে অ্যাক্সেস দেওয়ার জন্য এটি সাজেস্ট করা পদ্ধতি।

আপনি একই শ্বেততালিকা যাচাই করা ও যাচাই না করা নিয়ম একসাথে ব্যবহার করতে পারেন:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Sync the open Jira issues into the tracking sheet in my repo.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app",
            }
        ],
        "network": {
            "allowlist": [
                {"domain": "github.com", "credential": "github-production"},
                {"domain": "api.atlassian.com", "credential": "jira-oauth"},
                {"domain": "*.googleapis.com"},
            ]
        },
    },
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Sync the open Jira issues into the tracking sheet in my repo.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app",
            },
        ],
        network: {
            allowlist: [
                { domain: "github.com", credential: "github-production" },
                { domain: "api.atlassian.com", credential: "jira-oauth" },
                { domain: "*.googleapis.com" },
            ],
        },
    },
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Sync the open Jira issues into the tracking sheet in my repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Sources: []interactions.Source{
                    {
                        Type:   interactions.SourceTypeRepository.ToPointer(),
                        Source: genai.Ptr("https://github.com/your-org/backend"),
                        Target: genai.Ptr("/backend-app"),
                    },
                },
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "api.atlassian.com", Credential: genai.Ptr("jira-oauth")},
                        {Domain: "*.googleapis.com"},
                    })),
                })),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Sync the open Jira issues into the tracking sheet in my repo.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                { "domain": "github.com", "credential": "github-production" },
                { "domain": "api.atlassian.com", "credential": "jira-oauth" },
                { "domain": "*.googleapis.com" }
            ]
        }
    }
}'
```

প্রক্সি যেহেতু অনুরোধ অনুযায়ী ক্রেডেনশিয়াল সমাধান করে, তাই `oauth2` ক্রেডেনশিয়াল
এর অ্যাক্সেস টোকেন গোপনে রিফ্রেশ করা হয়। অ্যাক্সেস টোকেনের মেয়াদ শেষ হয়ে গেলেও
দীর্ঘক্ষণ ধরে চলা ইন্ট্যার‍্যাকশন বন্ধ হয় না।

### `credential` ও `transform`-কে একত্রিত করা

এছাড়াও, শ্বেততালিকাভুক্ত করার নিয়মে ইনলাইন
[`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn#private-sources) অবজেক্ট গ্রহণ করা হয় যা
সরাসরি নিয়মের উপর হেডার সেট করে। দুটি মেকানিজমই ওয়্যারে এগ্রেস
প্রক্সি প্রয়োগ করে, তাই দুটি ক্ষেত্রেই হেডার ভ্যালু কখনও
স্যান্ডবক্সের মধ্যে থাকে না। দুটি ফিল্ড একই নিয়মে থাকতে পারে।

| নিয়ম কনফিগারেশন | আচরণ |
| --- | --- |
| শুধুমাত্র `credential` | প্রক্সি ক্রেডেনশিয়াল সমাধান করে এবং ডোমেনে করা প্রতিটি অনুরোধে এর হেডার ইনজেক্ট করে। |
| শুধুমাত্র `transform` | স্ট্যাটিক হেডার ইনজেকশন। আপনি যে হেডার লিখবেন সেটি অপরিবর্তিত অবস্থায় পাঠানো হবে। |
| দুটিই | প্রথমে ক্রেডেনশিয়াল প্রয়োগ করা হয়, তারপর `transform` উপরে মার্জ করা হয়। দুটিই একই কী সেট করলে, এক্সপ্লিসিট `transform` হেডারটি জিতে যায়। |
| কোনওটিই নয় | ডোমেনটি অনুমোদিত এবং কোনও হেডার ইনজেক্ট করা হয়নি। |

আপনি যখন কোনও সিক্রেট একবার স্টোর করতে চান এবং আপনার প্রোজেক্টের প্রতিটি এনভায়রনমেন্ট, এজেন্ট ও ট্রিগার থেকে
সেটি রেফারেন্স করতে চান এবং যখন আপনি চান যে আপনার জন্য অ্যাক্সেস টোকেন রিফ্রেশ ও রোটেশন ম্যানেজ করা হোক, তখন কোনও ক্রেডেনশিয়াল ব্যবহার করা উপযুক্ত।
ইনলাইন `transform` ফিট করে
যখন ভ্যালু কোনও একটি কলের সাথে সম্পর্কিত হয়, যেমন, আপনি ইন্ট্যার‍্যাকশন তৈরি করার ঠিক আগে
নিজেই কোনও টোকেন জেনারেট করেছেন।

দুটি পদ্ধতিই একসাথে ব্যবহার করা হয়। ক্রেডেনশিয়ালে যাচাইকরণ হেডার
থাকে এবং `transform` একই
অনুরোধে আপস্ট্রিম পরিষেবা যা কিছু প্রত্যাশা করে তা যোগ করে:

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

ইনলাইন `transform` থেকে সরিয়ে কোনও ক্রেডেনশিয়ালে সিক্রেট সরাতে, এটিকে `POST /credentials`-এর সাথে স্টোর করুন, `transform`-এ থাকা অথরাইজেশন হেডারকে `"credential": "<id>"`-এর সাথে
বদল করুন এবং `transform` অবজেক্টের বাকি অংশ অপরিবর্তিত রাখুন।

## MCP সার্ভারের সাথে ক্রেডেনশিয়াল ব্যবহার করা

রিমোট MCP সার্ভার একই `credential` ফিল্ড নেয়। `mcp_server`
টুলে এটি সেট করুন এবং প্রক্সি সেই সার্ভারে পাঠানো প্রতিটি অনুরোধে অথরাইজেশন হেডার ইনজেক্ট করে:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a new issue in my-org/my-repo",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "github",
        "url": "https://api.githubcopilot.com/mcp",
        "credential": "github-production",
    }],
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Create a new issue in my-org/my-repo",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "github",
        url: "https://api.githubcopilot.com/mcp",
        credential: "github-production",
    }],
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Create a new issue in my-org/my-repo"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
                    Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                        {Domain: "api.githubcopilot.com", Credential: genai.Ptr("github-production")},
                    })),
                })),
            })),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("github"),
                    URL:  genai.Ptr("https://api.githubcopilot.com/mcp"),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Create a new issue in my-org/my-repo",
    "environment": "remote",
    "tools": [
        {
            "type": "mcp_server",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp",
            "credential": "github-production"
        }
    ]
}'
```

`credential` এবং `headers`, অনুমোদিত তালিকা হিসেবে একই অগ্রাধিকার সংক্রান্ত নিয়ম মেনে চলে।
প্রথমে ক্রেডেনশিয়াল প্রয়োগ করা হয় এবং `headers` উপরে মার্জ হয়ে যায়, তাই দুটিই একই কী সেট করলে, একটি স্পষ্ট
হেডার জিতে যায়:

```
{
    "type": "mcp_server",
    "name": "jira",
    "url": "https://jira.atlassian.com/mcp",
    "credential": "jira-oauth",
    "headers": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

ইনলাইন `headers` থেকে সরিয়ে কোনও ক্রেডেনশিয়ালে সিক্রেট সরাতে, এটিকে
`POST /credentials`-এর সাথে স্টোর করুন এবং `headers`-এর মধ্যে থাকা অথ এন্ট্রিকে `credential` দিয়ে পাল্টে দিন।
অন্যান্য হেডার যেখানে আছে সেখানেই রাখুন।

## এনভায়রনমেন্ট ভেরিয়েবল হিসেবে ক্রেডেনশিয়াল ব্যবহার করুন

কিছু ক্লায়েন্ট লাইব্রেরি রিকোয়েস্ট হেডার হিসেবে গ্রহণ করার পরিবর্তে
প্রসেস এনভায়রনমেন্ট থেকে সিক্রেট পড়ে। সকেট-মোড ও লং-পোলিং ক্লায়েন্ট হল
সাধারণ কেস।

`environment_variable` ক্রেডেনশিয়ালকে
`environment.env`-এর অধীনে ভেরিয়েবলের নামের সাথে বাইন্ড করুন:

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the sync script and check notifications.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": {"credential": "slack-bot-token"},
        },
    },
)
```

### জাভাস্ক্রিপ্ট

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the sync script and check notifications.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            SLACK_BOT_TOKEN: { credential: "slack-bot-token" },
        },
    },
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Run the sync script and check notifications."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Env: genai.Ptr(interactions.NewEnv(map[string]interactions.EnvVar{
                    "NODE_ENV":        {Value: genai.Ptr("production")},
                    "SLACK_BOT_TOKEN": {Credential: genai.Ptr("slack-bot-token")},
                })),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the sync script and check notifications.",
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": { "credential": "slack-bot-token" }
        }
    }
}'
```

`env` লিটারেল স্ট্রিং ও ক্রেডেনশিয়াল রেফারেন্স পাশাপাশি গ্রহণ করে। একটি আক্ষরিক
স্ট্রিং কন্টেনারে একটি সাধারণ প্লেনটেক্সট ভেরিয়েবল হিসেবে ইনজেক্ট করা হয়।

ক্রেডেনশিয়াল রেফারেন্স নেই। ভেরিয়েবলটি প্লেসহোল্ডার
`__GEMINI_CRED_<credential-id>__` পায় এবং প্রক্সি শুধুমাত্র
ক্রেডেনশিয়ালের `trusted_domains`-এ থাকা ডোমেনে পাঠানো আউটবাউন্ড অনুরোধের জন্য আসল সিক্রেট অদল-বদল করে। অন্য কোনও ডোমেনে করা অনুরোধ বাতিল করা হয়, তাই সিক্রেট কখনও
পরিধি ছেড়ে যায় না এবং এর পরিবর্তে প্লেসহোল্ডার পাঠানো হয় না।

প্রতিটি `environment_variable` ক্রেডেনশিয়ালের জন্য `trusted_domains` সেট করুন। এটি হল
কন্ট্রোল যা সেই স্কোপ নির্ধারণ করে যেখানে সিক্রেট ব্যবহার করা যেতে পারে।

## ক্রেডেনশিয়াল তৈরি করা

প্রতিটি ক্রিয়েট অনুরোধের জন্য `type` এবং সেই ধরনের জন্য প্রয়োজনীয় ফিল্ড পূরণ করতে হবে।

সরাসরি REST কল করার সময়, সব ফিল্ডের নামে snake\_case ব্যবহার করা হয়। camelCase
ফিল্ড পাঠালে `400` রিটার্ন করে।

### বিয়ারার টোকেন

বিয়ারার টোকেন ক্রেডেনশিয়ালের জন্য শুধু `token` প্রয়োজন:

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

উত্তরে শুধুমাত্র মেটাডেটা দেখানো হয়, কখনওই টোকেন নয়:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

সাধারণত, প্রক্সি `Authorization: Bearer <token>` পাঠায়। অন্য কিছু প্রত্যাশা করে এমন কোনও পরিষেবাকে টার্গেট করতে ওভাররাইড
`header_name` এবং `prefix` করুন:

### Python

```
credential = client.credentials.create(
    id="my-api-key",
    type="bearer_token",
    token="key_xxxxxxxxxxxx",
    header_name="x-goog-api-key",
    prefix="",
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:         "my-api-key",
            Token:      "key_xxxxxxxxxxxx",
            HeaderName: genai.Ptr("x-goog-api-key"),
            Prefix:     genai.Ptr(""),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "my-api-key",
    "type": "bearer_token",
    "token": "key_xxxxxxxxxxxx",
    "header_name": "x-goog-api-key",
    "prefix": ""
}'
```

এই কনফিগারেশন `x-goog-api-key: key_xxxxxxxxxxxx` হেডার তৈরি করে।

`header_name` ও `prefix` কীভাবে একসাথে কাজ করে তা নিচের সারণীতে দেখানো হয়েছে:

| কনফিগারেশন | ইনজেক্ট করা হেডার |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

OAuth2 ক্রেডেনশিয়ালের জন্য `client_id`, `client_secret`, `refresh_token`,
এবং `token_url` প্রয়োজন। `scopes` ফিল্ডটি ঐচ্ছিক:

### Python

```
credential = client.credentials.create(
    id="jira-oauth",
    type="oauth2",
    client_id="my-client-id",
    client_secret="my-client-secret",
    token_url="https://auth.atlassian.com/oauth/token",
    refresh_token="rt_xxxxxxxxxxxxxxxxxxxx",
    scopes=["read:jira-work", "write:jira-work"],
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.create({
    id: "jira-oauth",
    type: "oauth2",
    client_id: "my-client-id",
    client_secret: "my-client-secret",
    token_url: "https://auth.atlassian.com/oauth/token",
    refresh_token: "rt_xxxxxxxxxxxxxxxxxxxx",
    scopes: ["read:jira-work", "write:jira-work"],
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.OAuth2Config{
            ID:           "jira-oauth",
            ClientID:     "my-client-id",
            ClientSecret: "my-client-secret",
            TokenURL:     "https://auth.atlassian.com/oauth/token",
            RefreshToken: "rt_xxxxxxxxxxxxxxxxxxxx",
            Scopes:       []string{"read:jira-work", "write:jira-work"},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created OAuth2 credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "jira-oauth",
    "type": "oauth2",
    "client_id": "my-client-id",
    "client_secret": "my-client-secret",
    "token_url": "https://auth.atlassian.com/oauth/token",
    "refresh_token": "rt_xxxxxxxxxxxxxxxxxxxx",
    "scopes": ["read:jira-work", "write:jira-work"]
}'
```

OAuth2 ক্রেডেনশিয়াল তৈরি করলে, কনফিগারেশন কাজ করছে কিনা তা কনফার্ম করতে
`token_url`-এর বিরুদ্ধে লাইভ টোকেন এক্সচেঞ্জ করা হয়। প্রোভাইডার যদি
`access_token` সহ একটি সফল টোকেন উত্তর রিটার্ন করে, তাহলেই শুধুমাত্র ক্রেডেনশিয়াল সেভ করা হয়।
JSON ও form-urlencoded, দু'টি ফর্ম্যাটের উত্তরই গ্রহণ করা হয়।

এর অর্থ হল, তৈরি করার সময় আপনার একটি বৈধ, মেয়াদ না ফুরানো রিফ্রেশ টোকেন প্রয়োজন। প্রোভাইডার যদি
এক্সচেঞ্জ প্রত্যাখ্যান করে, তাহলে আপনাকে এই সমস্যা দেখানো হবে:

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

সেভ করা হয়ে গেলে, প্রক্সি অ্যাক্সেস টোকেনের মেয়াদ শেষ হয়ে গেলে সেগুলি রিফ্রেশ করে। রিফ্রেশ করার সময় প্রদানকারী
রিফ্রেশ টোকেন রোটেট করলে এবং নতুন টোকেন দিলে, নতুন টোকেনটি
সেভ করা টোকেনের জায়গায় অটোমেটিক সেভ হয়ে যায়।

### এনভায়রনমেন্ট ভেরিয়েবল

`environment_variable` ক্রেডেনশিয়ালের জন্য `value` ও `injection_location` প্রয়োজন:

### Python

```
credential = client.credentials.create(
    id="slack-bot-token",
    type="environment_variable",
    value="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains=["*.slack.com", "slack.com"],
    injection_location="header",
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.EnvironmentVariableConfig{
            ID:                "slack-bot-token",
            Value:             "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
            TrustedDomains:    []string{"*.slack.com", "slack.com"},
            InjectionLocation: credentials.NewEnvironmentVariableConfigInjectionLocation(credentials.InjectionLocationEnumHeader),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created environment variable credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "slack-bot-token",
    "type": "environment_variable",
    "value": "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    "trusted_domains": ["*.slack.com", "slack.com"],
    "injection_location": "header"
}'
```

`injection_location` ফিল্ডটি প্রক্সি সার্ভারকে জানায় যে আউটবাউন্ড অনুরোধে কোথায়
গোপন তথ্যটি পরিবর্তন করতে হবে। এটি `header`, `query` বা `body` গ্রহণ করে, একটি
স্ট্রিং হিসেবে অথবা কোনও পরিষেবার একাধিক প্রয়োজন হলে একটি অ্যারে হিসেবে:

```
"injection_location": ["header", "query"]
```

আপনি যেসব লোকেশন তালিকাভুক্ত করেন, শুধুমাত্র সেখানেই বিকল্প প্রোডাক্ট ব্যবহার করা হয়। কোনও অনুরোধে প্লেসহোল্ডারটি
অন্য কোথাও থাকলে, সেটি পাঠানোর পরিবর্তে বাতিল করা হয়।

ভেরিয়েবল নামের সাথে ক্রেডেনশিয়াল বাইন্ড করতে, [এনভায়রনমেন্ট ভেরিয়েবল হিসেবে ক্রেডেনশিয়াল ব্যবহার করুন](#environment-variables) দেখুন।

### জেনারেট করা আইডি

`id` ফিল্ডটি ঐচ্ছিক। এটি বাদ দিন এবং পরিষেবা একটি UUID তৈরি করে:

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

ইন্টার‍্যাকশন জুড়ে ব্যবহার করার জন্য স্থিতিশীল, পাঠযোগ্য রেফারেন্স চাইলে আপনার নিজস্ব আইডি দিন। যেহেতু রিসোর্স পাথে আইডি দেখা যায়, তাই হাইফেন বা আন্ডারস্কোর সহ ছোট হাতের
বর্ণসাংখ্যিক অক্ষর ব্যবহার করুন।

## ক্রেডেনশিয়ালের তালিকা তৈরি করা

আপনার প্রোজেক্টের ক্রেডেনশিয়ালের তালিকা তৈরি করুন। উত্তর ব্যাচের সাইজ নিয়ন্ত্রণ করতে
পেজিনেশন প্যারামিটার ব্যবহার করুন।

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### জাভাস্ক্রিপ্ট

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.List(ctx, operations.ListCredentialsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, cred := range res.CredentialListResponse.Credentials {
        fmt.Printf("Credential ID: %s, Type: %v\n", cred.ID, cred.GetType())
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials?page_size=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

উত্তরে শুধুমাত্র মেটাডেটা রয়েছে:

```
{
  "credentials": [
    {
      "id": "github-production",
      "type": "bearer_token",
      "status": "active",
      "create_time": "2026-07-15T10:00:00.000000000Z",
      "update_time": "2026-07-15T10:00:00.000000000Z"
    },
    {
      "id": "jira-oauth",
      "type": "oauth2",
      "status": "active",
      "create_time": "2026-07-15T10:05:00.000000000Z",
      "update_time": "2026-07-15T10:05:00.000000000Z"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

পরের পৃষ্ঠা পেতে `next_page_token` কে `page_token` হিসেবে পাস করুন। আর কোনও ফলাফল না থাকলে
এই ফিল্ডটি বাদ দেওয়া হয়।

| প্যারামিটার | ধরন | বিবরণ |
| --- | --- | --- |
| `page_size` | পূর্ণসংখ্যা | প্রতি পৃষ্ঠায় সর্বাধিক সংখ্যক ক্রেডেনশিয়াল। |
| `page_token` | স্ট্রিং | আগের উত্তরের `next_page_token` থেকে টোকেন। |

## ক্রেডেনশিয়াল পাওয়া

কোনও নির্দিষ্ট ক্রেডেনশিয়ালের আইডি দিয়ে সেটির মেটাডেটা রিট্রিভ করুন।

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Get(ctx, operations.GetCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

উত্তরটি নিচে উল্লেখ করা উত্তরের মতো:

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

বিদ্যমান নেই এমন ক্রেডেনশিয়ালের অনুরোধ করলে `404` রিটার্ন করে:

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## ক্রেডেনশিয়াল রোটেট করা

কোনও অনুমতিপ্রাপ্ত তালিকা সংক্রান্ত নিয়ম, টুল সংজ্ঞা বা
এনভায়রনমেন্ট ভেরিয়েবেল স্পর্শ না করেই কোনও সিক্রেট পাল্টে দিন যা এটিকে রেফার করে। পরবর্তী
প্রক্সি রেজোলিউশনে রোটেশন কার্যকর হয়।

অনুরোধে `type` সহ আপনি যেসব ফিল্ড পরিবর্তন করতে চান সেগুলি উল্লেখ করতে হবে। আপনি বাদ দিয়েছেন
এমন ফিল্ডের বর্তমান ভ্যালু বজায় থাকে।

বিয়ারার টোকেন রোটেট করা:

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "github-production",
        Body: credentials.NewCredentialUpdate(credentials.HTTPBearerUpdateConfig{
            Token: genai.Ptr("ghp_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "bearer_token",
    "token": "ghp_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

OAuth2 রিফ্রেশ টোকেন রোটেট করা:

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### জাভাস্ক্রিপ্ট

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### খুলুন

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "jira-oauth",
        Body: credentials.NewCredentialUpdate(credentials.OAuth2UpdateConfig{
            RefreshToken: genai.Ptr("rt_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/jira-oauth" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "oauth2",
    "refresh_token": "rt_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

উত্তরে নতুন `update_time` বিষয়গুলি উঠে এসেছে:

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

কোনও ক্রেডেনশিয়াল তৈরি করার সময় তার `type` নির্দিষ্ট করা হয়। এটি পরিবর্তন করতে, ক্রেডেনশিয়াল মুছে দিন
এবং নতুন একটি তৈরি করুন।

## ক্রেডেনশিয়াল মুছে দেওয়া

ক্রেডেনশিয়াল ও সেটির স্টোর করা গোপন তথ্য আর প্রয়োজন না হলে সেটি মুছে দিন।

### Python

```
client.credentials.delete(id="github-production")
```

### জাভাস্ক্রিপ্ট

```
await client.credentials.delete("github-production");
```

### খুলুন

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Credentials.Delete(ctx, operations.DeleteCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

সফলভাবে মুছে দিলে একটি খালি অবজেক্ট রিটার্ন করে:

```
{}
```

এখনও আইডি উল্লেখ করছে এমন কোনও হোয়াইটলিস্ট নিয়ম, টুল বা এনভায়রনমেন্ট ভেরিয়েবেল
সমাধান করতে পারবে না, তাই প্রথমে সেগুলি আপডেট করুন।

## ফিল্ড রেফারেন্স

প্রতিটি ক্রেডেনশিয়ালের সাধারণ ফিল্ড:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `id` | স্ট্রিং | না | অনন্য শনাক্তকারী। উল্লেখ না করা হলে UUID হিসেবে জেনারেট করা হয়। |
| `type` | স্ট্রিং | হ্যাঁ | `bearer_token`, `oauth2`, `environment_variable`-এর মধ্যে একটি। |
| `status` | স্ট্রিং | শুধু পড়া যায় | ক্রেডেনশিয়ালের বর্তমান স্ট্যাটাস। |
| `create_time` | স্ট্রিং | শুধু পড়া যায় | RFC 3339 তৈরির টাইমস্ট্যাম্প। |
| `update_time` | স্ট্রিং | শুধু পড়া যায় | শেষ আপডেটের RFC 3339 টাইমস্ট্যাম্প। |

`bearer_token`-এর জন্য ফিল্ড:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `token` | স্ট্রিং | হ্যাঁ | শুধুমাত্র লেখার সুবিধা। টোকেনের ভ্যালু। |
| `header_name` | স্ট্রিং | না | ইনজেক্ট করার জন্য হেডার। ডিফল্ট হিসেবে `Authorization` সেট করা থাকে। |
| `prefix` | স্ট্রিং | না | ভ্যালু প্রিফিক্স। ডিফল্ট হিসেবে `Bearer` সেট করা থাকে। কোনওটির জন্য `""` হিসেবে সেট করুন। |

`oauth2`-এর জন্য ফিল্ড:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `client_id` | স্ট্রিং | হ্যাঁ | OAuth2 ক্লায়েন্ট আইডি। |
| `client_secret` | স্ট্রিং | হ্যাঁ | শুধুমাত্র লেখার সুবিধা। OAuth2 ক্লায়েন্ট সিক্রেট। |
| `refresh_token` | স্ট্রিং | হ্যাঁ | শুধুমাত্র লেখার সুবিধা। অ্যাক্সেস টোকেন পাওয়ার জন্য রিফ্রেশ টোকেন ব্যবহার করা হয়। |
| `token_url` | স্ট্রিং | হ্যাঁ | প্রোভাইডার টোকেন এন্ডপয়েন্ট। |
| `scopes` | এরে | না | অনুরোধ করার জন্য OAuth স্কোপ। |

`environment_variable`-এর জন্য ফিল্ড:

| ফিল্ড | ধরন | প্রয়োজনীয় | বিবরণ |
| --- | --- | --- | --- |
| `value` | স্ট্রিং | হ্যাঁ | শুধুমাত্র লেখার সুবিধা। গোপন ভ্যালু। |
| `injection_location` | স্ট্রিং বা অ্যারে | হ্যাঁ | গোপন তথ্য কোথায় বসাতে হবে। `header`, `query`, `body`-এর মধ্যে একটি বা একাধিক। |
| `trusted_domains` | এরে | না | সাবস্টিটিউশনের জন্য অনুমোদিত ডোমেন প্যাটার্ন। |

## সমস্যা

সমস্যা হলে, `message` ও `code` সহ JSON অবজেক্ট ফেরত দেওয়া হয়:

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| HTTP স্ট্যাটাস | `code` | কারণ |
| --- | --- | --- |
| 400 | `invalid_request` | প্রয়োজনীয় ফিল্ড নেই, অজানা ফিল্ড, কাজ করে না এমন `type` অথবা OAuth2 যাচাইকরণ করা যায়নি। |
| 404 | `not_found` | ওই আইডি সহ কোনও ক্রেডেনশিয়াল নেই। |
| 409 | `aborted` | এই আইডি-সহ একটি ক্রেডেনশিয়াল আগে থেকেই আছে। |

অপরিচিত ফিল্ড উপেক্ষা না করে বাতিল করা হয় এবং সমস্যার নামে ফিল্ডের নাম উল্লেখ করা হয়:

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## এর পরে কী করতে হবে

- [এনভায়রনমেন্ট](https://ai.google.dev/gemini-api/docs/agent-environment?hl=bn): এজেন্ট কীভাবে কোড রান করে এবং ফাইল সেভ করে তা জানুন।
- [এজেন্ট ওভারভিউ](https://ai.google.dev/gemini-api/docs/agents?hl=bn): ম্যানেজ করা এজেন্টদের মূল ধারণা সম্পর্কে জানুন।
- [কাস্টম এজেন্ট তৈরি করা](https://ai.google.dev/gemini-api/docs/custom-agents?hl=bn): `AGENTS.md` ও `SKILL.md` ব্যবহার করে আপনার নিজস্ব এজেন্ট নির্ধারণ করুন।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-07 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-07 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
