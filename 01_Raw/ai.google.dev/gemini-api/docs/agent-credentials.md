---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=th
fetched_at: 2026-10-12T06:55:20.138660+00:00
title: "\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e40\u0e02\u0e49\u0e32\u0e2a\u0e39\u0e48\u0e23\u0e30\u0e1a\u0e1a\u0e43\u0e19\u0e40\u0e2d\u0e40\u0e08\u0e19\u0e15\u0e4c\u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ข้อมูลเข้าสู่ระบบในเอเจนต์ที่มีการจัดการ

ข้อมูลเข้าสู่ระบบคือข้อมูลลับที่เซิร์ฟเวอร์จัดการซึ่งช่วยให้ Agent เข้าถึงบริการของบุคคลที่สามได้โดยไม่ต้องป้อนข้อมูลลับลงในสภาพแวดล้อมของ Agent คุณจัดเก็บ
ข้อมูลเข้าสู่ระบบเพียงครั้งเดียว อ้างอิงตามรหัส และพร็อกซีขาออกจะแก้ไขและแทรก
ข้อมูลดังกล่าวเมื่อมีการส่งคำขอ

ค่าของข้อมูลลับเป็นแบบเขียนอย่างเดียว เมื่อจัดเก็บแล้ว ระบบจะไม่แสดงโทเค็นดังกล่าวใน
ปลายทางใดๆ ดังนั้นเอเจนต์ที่ถูกบุกรุกจึงไม่สามารถอ่านโทเค็นที่กำลังใช้อยู่ได้

ที่ที่คุณใช้ข้อมูลเข้าสู่ระบบเป็นหลักคือรายการที่อนุญาตของเครือข่ายใน
[`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th) จัดเก็บข้อมูลลับ
ก่อน

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

### JavaScript

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

### Go

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

จากนั้นแนบไปกับโดเมนที่ตรวจสอบสิทธิ์

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

### JavaScript

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

### Go

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

ตอนนี้ Agent จะส่งคำขอที่ผ่านการตรวจสอบสิทธิ์ไปยัง `api.github.com` และโทเค็น
จะไม่เคยอยู่ในแซนด์บ็อกซ์

## ประเภทข้อมูลเข้าสู่ระบบ

ข้อมูลเข้าสู่ระบบทุกรายการมี `type` ที่กำหนดว่าข้อมูลเข้าสู่ระบบนั้นยอมรับฟิลด์ใดและพร็อกซีจะใช้ข้อมูลเข้าสู่ระบบนั้นอย่างไร

| ประเภท | กรณีการใช้งาน | พฤติกรรม |
| --- | --- | --- |
| `bearer_token` | โทเค็นเพื่อการเข้าถึงส่วนบุคคล โทเค็นบอท คีย์ API แบบคงที่ | พร็อกซีจะแทรกโทเค็นเป็นส่วนหัวของคำขอ ไม่มีตรรกะการรีเฟรช |
| `oauth2` | แอป OAuth และโฟลว์ที่ผู้ใช้มอบสิทธิ์ | พร็อกซีจะแลกเปลี่ยนโทเค็นการรีเฟรชเป็นโทเค็นเพื่อการเข้าถึงและรีเฟรชโทเค็นเหล่านั้นเมื่อหมดอายุ |
| `environment_variable` | SDK ไคลเอ็นต์ที่อ่านข้อมูลลับจากสภาพแวดล้อมของกระบวนการ | สภาพแวดล้อมของเอเจนต์จะได้รับตัวยึดตำแหน่ง พร็อกซีจะแทนที่ข้อมูลลับจริงในคำขอขาออก |

## ใช้ข้อมูลเข้าสู่ระบบในรายการที่อนุญาตของเครือข่าย

เพิ่ม `credential` ลงในกฎรายการที่อนุญาตและพร็อกซีจะตรวจสอบสิทธิ์ทุกคำขอขาออกไปยังโดเมนนั้น นี่คือวิธีที่แนะนำในการให้สิทธิ์เข้าถึง API ส่วนตัว ที่เก็บข้อมูลส่วนตัว หรือที่เก็บข้อมูลส่วนตัวแก่ Agent

คุณสามารถรวมกฎที่ตรวจสอบสิทธิ์แล้วและยังไม่ได้ตรวจสอบสิทธิ์ไว้ในรายการที่อนุญาตเดียวกันได้โดยทำดังนี้

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

### JavaScript

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

### Go

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

เนื่องจากพร็อกซีจะแก้ไขข้อมูลเข้าสู่ระบบต่อคำขอ `oauth2` ข้อมูลเข้าสู่ระบบ
จึงรีเฟรชโทเค็นการเข้าถึงอย่างโปร่งใส การโต้ตอบที่ใช้เวลานานจะไม่หยุดทำงานเมื่อโทเค็นเพื่อการเข้าถึงหมดอายุ

### การรวม `credential` และ `transform`

กฎรายการที่อนุญาตยังยอมรับออบเจ็กต์
[`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#private-sources)แบบอินไลน์ที่
ตั้งค่าส่วนหัวในกฎโดยตรงด้วย ทั้ง 2 กลไกนี้ใช้โดยพร็อกซีขาออก
บนสาย ดังนั้นในทั้ง 2 กรณี ค่าส่วนหัวจึงไม่เคยมีอยู่ภายใน
แซนด์บ็อกซ์ ทั้ง 2 ช่องจะปรากฏในกฎเดียวกันได้

| การกำหนดค่ากฎ | พฤติกรรม |
| --- | --- |
| `credential` เท่านั้น | พร็อกซีจะแก้ไขข้อมูลเข้าสู่ระบบและแทรกส่วนหัวในทุกคำขอไปยังโดเมน |
| `transform` เท่านั้น | การแทรกส่วนหัวแบบคงที่ ระบบจะส่งส่วนหัวที่คุณเขียนตามที่เขียน |
| ทั้งคู่ | ระบบจะใช้ข้อมูลเข้าสู่ระบบก่อน แล้วจึง`transform`ผสานด้านบน ส่วนหัว `transform` ที่ชัดเจนจะชนะหากทั้ง 2 รายการตั้งค่าคีย์เดียวกัน |
| เฉยๆ | ระบบอนุญาตโดเมนและไม่ได้แทรกส่วนหัว |

คุณควรใช้ข้อมูลเข้าสู่ระบบเมื่อต้องการจัดเก็บข้อมูลลับเพียงครั้งเดียวและอ้างอิง
จากทุกสภาพแวดล้อม เอเจนต์ และทริกเกอร์ในโปรเจ็กต์ รวมถึงเมื่อต้องการให้ระบบจัดการการรีเฟรชและการหมุนเวียนโทเค็นเพื่อการเข้าถึงให้คุณ
`transform` ในบรรทัดจะพอดี
เมื่อค่าเป็นของการเรียกครั้งเดียว เช่น โทเค็นที่คุณสร้าง
ด้วยตนเองก่อนสร้างการโต้ตอบ

การใช้ทั้ง 2 อย่างร่วมกันเป็นเรื่องปกติ ข้อมูลเข้าสู่ระบบมีส่วนหัวการตรวจสอบสิทธิ์
และ `transform` จะเพิ่มข้อมูลอื่นๆ ที่บริการต้นทางคาดหวังในคำขอเดียวกัน

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

หากต้องการย้ายข้อมูลลับออกจาก `transform` แบบอินไลน์และไปยังข้อมูลเข้าสู่ระบบ ให้จัดเก็บข้อมูลลับด้วย `POST /credentials` แทนที่ส่วนหัวการตรวจสอบสิทธิ์ใน `transform` ด้วย `"credential": "<id>"` และปล่อยให้ส่วนที่เหลือของออบเจ็กต์ `transform` เหมือนเดิม

## ใช้ข้อมูลเข้าสู่ระบบกับเซิร์ฟเวอร์ MCP

เซิร์ฟเวอร์ MCP ระยะไกลใช้ฟิลด์ `credential` เดียวกัน ตั้งค่าใน`mcp_server`
เครื่องมือและพร็อกซีจะแทรกส่วนหัวการตรวจสอบสิทธิ์ลงในคำขอทุกรายการที่ส่งไปยังเซิร์ฟเวอร์นั้น

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

### JavaScript

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

### Go

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

`credential` และ `headers` จะใช้กฎลำดับความสำคัญเดียวกันกับรายการที่อนุญาต
ระบบจะใช้ข้อมูลเข้าสู่ระบบก่อนและ `headers` จะผสานรวมอยู่ด้านบน ดังนั้นส่วนหัวที่ชัดเจน
จะชนะหากทั้ง 2 รายการตั้งค่าคีย์เดียวกัน

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

หากต้องการย้ายข้อมูลลับออกจาก `headers` แบบอินไลน์และไปยังข้อมูลเข้าสู่ระบบ ให้จัดเก็บข้อมูลลับด้วย
`POST /credentials` แล้วแทนที่รายการการตรวจสอบสิทธิ์ใน `headers` ด้วย `credential`
คงส่วนหัวอื่นๆ ไว้ที่เดิม

## ใช้ข้อมูลเข้าสู่ระบบเป็นตัวแปรสภาพแวดล้อม

ไลบรารีของไคลเอ็นต์บางรายการจะอ่านข้อมูลลับจากสภาพแวดล้อมของกระบวนการแทนที่จะ
ยอมรับเป็นส่วนหัวของคำขอ ไคลเอ็นต์ในโหมด Socket และ Long Polling เป็นกรณีที่พบบ่อย

เชื่อมโยง`environment_variable`ข้อมูลเข้าสู่ระบบกับชื่อตัวแปรภายใต้
`environment.env`:

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

### JavaScript

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

### Go

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

`env`ยอมรับสตริงลิเทอรัลและการอ้างอิงข้อมูลเข้าสู่ระบบควบคู่กัน ระบบจะแทรกสตริงตามตัวอักษร
ลงในคอนเทนเนอร์เป็นตัวแปรข้อความธรรมดาปกติ

แต่การอ้างอิงข้อมูลเข้าสู่ระบบไม่ใช่ ตัวแปรจะได้รับตัวยึดตำแหน่ง
`__GEMINI_CRED_<credential-id>__` และพร็อกซีจะสลับข้อมูลลับจริงเฉพาะ
สำหรับคำขอขาออกที่ไปยังโดเมนใน `trusted_domains` ของข้อมูลเข้าสู่ระบบ
คำขอไปยังโดเมนอื่นๆ จะถูกปฏิเสธ ดังนั้นระบบจะไม่ส่งข้อมูลลับออกนอก
ขอบเขต และจะไม่ส่งตัวยึดตำแหน่งแทน

ตั้งค่า `trusted_domains` ในข้อมูลเข้าสู่ระบบ `environment_variable` ทุกรายการ ซึ่งเป็น
การควบคุมที่กำหนดขอบเขตที่ใช้ข้อมูลลับได้

## สร้างข้อมูลเข้าสู่ระบบ

คำขอสร้างทุกรายการต้องมี `type` รวมถึงฟิลด์อื่นๆ ที่ประเภทนั้นๆ กำหนด

เมื่อเรียกใช้ REST โดยตรง ชื่อฟิลด์ทั้งหมดจะใช้รูปแบบ snake\_case การส่งฟิลด์ camelCase
จะแสดงผล `400`

### โทเค็นสำหรับผู้ถือ

ข้อมูลเข้าสู่ระบบโทเค็นผู้ถือใช้สิทธิ์ต้องมีเพียง`token`

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### Go

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

การตอบกลับจะแสดงเฉพาะข้อมูลเมตา ไม่ใช่โทเค็น

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

โดยค่าเริ่มต้นพร็อกซีจะส่ง `Authorization: Bearer <token>` แทนที่
`header_name` และ `prefix` เพื่อกำหนดเป้าหมายบริการที่คาดหวังสิ่งอื่น

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

### JavaScript

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### Go

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

การกำหนดค่านี้จะสร้างส่วนหัว `x-goog-api-key: key_xxxxxxxxxxxx`

ตารางต่อไปนี้แสดงวิธีรวม `header_name` และ `prefix`

| การกำหนดค่า | ส่วนหัวที่แทรก |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

ข้อมูลเข้าสู่ระบบ OAuth2 ต้องมี `client_id`, `client_secret`, `refresh_token`
และ `token_url` ฟิลด์ `scopes` เป็นฟิลด์ที่ไม่บังคับ

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

### JavaScript

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

### Go

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

การสร้างข้อมูลเข้าสู่ระบบ OAuth2 จะดำเนินการแลกเปลี่ยนโทเค็นแบบเรียลไทม์กับ
`token_url` เพื่อยืนยันว่าการกำหนดค่าใช้งานได้ ระบบจะจัดเก็บข้อมูลเข้าสู่ระบบก็ต่อเมื่อผู้ให้บริการส่งคืนการตอบกลับโทเค็นที่สำเร็จซึ่งมี `access_token` ระบบยอมรับทั้งการตอบกลับแบบ JSON และ form-urlencoded

ซึ่งหมายความว่าคุณต้องมีโทเค็นการรีเฟรชที่ยังไม่หมดอายุและใช้งานได้ในขณะสร้าง หาก
ผู้ให้บริการปฏิเสธการแลกเปลี่ยน ระบบจะแสดงข้อผิดพลาดต่อไปนี้ให้คุณ

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

เมื่อจัดเก็บแล้ว พร็อกซีจะรีเฟรชโทเค็นเพื่อการเข้าถึงเมื่อโทเค็นหมดอายุ หากผู้ให้บริการ
หมุนเวียนโทเค็นการรีเฟรชและส่งคืนโทเค็นใหม่ระหว่างการรีเฟรช โทเค็นใหม่
จะแทนที่โทเค็นที่จัดเก็บไว้โดยอัตโนมัติ

### ตัวแปรสภาพแวดล้อม

`environment_variable` การรับรองต้องมี`value`และ`injection_location`

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

### JavaScript

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### Go

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

ฟิลด์ `injection_location` จะบอกพร็อกซีว่าควรแทนที่ข้อมูลลับในคำขอขาออกที่ใด
โดยจะยอมรับ `header`, `query` หรือ `body` ไม่ว่าจะเป็นสตริงเดียวหรืออาร์เรย์เมื่อบริการต้องการมากกว่า 1 รายการ

```
"injection_location": ["header", "query"]
```

การแทนที่จะเกิดขึ้นเฉพาะในสถานที่ตั้งที่คุณระบุ คำขอที่มีตัวยึดตำแหน่งในที่อื่นจะถูกปฏิเสธแทนที่จะส่งต่อ

หากต้องการเชื่อมโยงข้อมูลเข้าสู่ระบบกับชื่อตัวแปร โปรดดูหัวข้อ
[ใช้ข้อมูลเข้าสู่ระบบเป็นตัวแปรสภาพแวดล้อม](#environment-variables)

### รหัสที่สร้างขึ้น

ช่อง `id` เป็นข้อมูลที่ไม่บังคับ ละเว้นไว้ แล้วบริการจะสร้าง UUID ให้

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

ระบุรหัสของคุณเองเมื่อต้องการการอ้างอิงที่คงที่และอ่านได้เพื่อใช้ในการโต้ตอบ
เนื่องจากรหัสจะปรากฏในเส้นทางทรัพยากร จึงควรใช้ตัวอักษรและตัวเลขคละกันที่เป็นตัวพิมพ์เล็กโดยมีขีดกลางหรือขีดล่าง

## แสดงรายการข้อมูลเข้าสู่ระบบ

แสดงรายการข้อมูลเข้าสู่ระบบที่เป็นของโปรเจ็กต์ ใช้พารามิเตอร์การแบ่งหน้าเพื่อ
ควบคุมขนาดกลุ่มการตอบกลับ

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### JavaScript

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### Go

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

การตอบกลับมีเฉพาะข้อมูลเมตา

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

ส่ง `next_page_token` กลับเป็น `page_token` เพื่อดึงข้อมูลหน้าถัดไป ระบบจะละเว้นฟิลด์
เมื่อไม่มีผลลัพธ์เพิ่มเติม

| พารามิเตอร์ | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `page_size` | จำนวนเต็ม | จำนวนข้อมูลเข้าสู่ระบบสูงสุดต่อหน้าเว็บ |
| `page_token` | สตริง | โทเค็นจาก `next_page_token` ของคำตอบก่อนหน้า |

## รับการรับรอง

ดึงข้อมูลเมตาสำหรับข้อมูลเข้าสู่ระบบที่เฉพาะเจาะจงตามรหัส

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### JavaScript

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### Go

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

การตอบกลับจะมีลักษณะคล้ายกับตัวอย่างต่อไปนี้

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

การขอข้อมูลเข้าสู่ระบบที่ไม่มีอยู่จะแสดงผล `404`

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## หมุนเวียนข้อมูลเข้าสู่ระบบ

แทนที่ข้อมูลลับโดยไม่ต้องแตะต้องกฎรายการที่อนุญาต คำจำกัดความของเครื่องมือ หรือตัวแปรสภาพแวดล้อมที่อ้างอิงถึงข้อมูลลับนั้น
การหมุนเวียนจะมีผลในการ
แก้ไขพร็อกซีครั้งถัดไป

คำขอต้องมี `type` รวมถึงฟิลด์ที่คุณต้องการเปลี่ยนแปลง ฟิลด์ที่คุณ
ละไว้จะยังคงมีค่าปัจจุบัน

หมุนเวียนโทเค็นสำหรับผู้ถือ

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

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

หมุนเวียนโทเค็นการรีเฟรช OAuth2 โดยทำดังนี้

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### JavaScript

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

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

คำตอบจะแสดง `update_time` ใหม่ดังนี้

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

`type` ของข้อมูลเข้าสู่ระบบจะคงที่เมื่อสร้าง หากต้องการเปลี่ยน ให้ลบข้อมูลเข้าสู่ระบบ
แล้วสร้างใหม่

## ลบข้อมูลเข้าสู่ระบบ

ลบข้อมูลเข้าสู่ระบบและข้อมูลลับที่จัดเก็บไว้เมื่อไม่จำเป็นต้องใช้แล้ว

### Python

```
client.credentials.delete(id="github-production")
```

### JavaScript

```
await client.credentials.delete("github-production");
```

### Go

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

การลบที่สำเร็จจะแสดงออบเจ็กต์ว่าง

```
{}
```

กฎรายการที่อนุญาต เครื่องมือ หรือตัวแปรสภาพแวดล้อมที่ยังอ้างอิงรหัสจะ
ไม่สามารถแก้ไขได้ ดังนั้นให้อัปเดตสิ่งเหล่านั้นก่อน

## ข้อมูลอ้างอิงฟิลด์

ฟิลด์ที่ใช้ร่วมกันในข้อมูลเข้าสู่ระบบทุกรายการ

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `id` | สตริง | ไม่ | ตัวระบุที่ไม่ซ้ำกัน สร้างเป็น UUID เมื่อละเว้น |
| `type` | สตริง | ใช่ | `bearer_token`, `oauth2`, `environment_variable` |
| `status` | สตริง | อ่านอย่างเดียว | สถานะปัจจุบันของข้อมูลเข้าสู่ระบบ |
| `create_time` | สตริง | อ่านอย่างเดียว | การประทับเวลาการสร้าง RFC 3339 |
| `update_time` | สตริง | อ่านอย่างเดียว | การประทับเวลา RFC 3339 ของการอัปเดตล่าสุด |

ฟิลด์สำหรับ `bearer_token`

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `token` | สตริง | ใช่ | เขียนอย่างเดียว ค่าโทเค็น |
| `header_name` | สตริง | ไม่ | ส่วนหัวที่จะแทรก ค่าเริ่มต้นคือ `Authorization` |
| `prefix` | สตริง | ไม่ | คำนำหน้าค่า ค่าเริ่มต้นคือ `Bearer` หากไม่ต้องการ ให้ตั้งค่าเป็น `""` |

ฟิลด์สำหรับ `oauth2`

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `client_id` | สตริง | ใช่ | รหัสไคลเอ็นต์ OAuth2 |
| `client_secret` | สตริง | ใช่ | เขียนอย่างเดียว รหัสลับไคลเอ็นต์ OAuth2 |
| `refresh_token` | สตริง | ใช่ | เขียนอย่างเดียว โทเค็นการรีเฟรชที่ใช้เพื่อรับโทเค็นเพื่อการเข้าถึง |
| `token_url` | สตริง | ใช่ | ปลายทางของโทเค็นผู้ให้บริการ |
| `scopes` | อาร์เรย์ | ไม่ | ขอบเขต OAuth ที่จะขอ |

ฟิลด์สำหรับ `environment_variable`

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `value` | สตริง | ใช่ | เขียนอย่างเดียว ค่าข้อมูลลับ |
| `injection_location` | สตริงหรืออาร์เรย์ | ใช่ | ตำแหน่งที่จะแทนที่ข้อมูลลับ `header`, `query`, `body` อย่างน้อย 1 รายการ |
| `trusted_domains` | อาร์เรย์ | ไม่ | รูปแบบโดเมนที่ได้รับอนุญาตให้ใช้แทน |

## ข้อผิดพลาด

ข้อผิดพลาดจะแสดงออบเจ็กต์ JSON ที่มี `message` และ `code` ดังนี้

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| สถานะ HTTP | `code` | สาเหตุ |
| --- | --- | --- |
| 400 | `invalid_request` | ไม่มีช่องที่ต้องกรอก ไม่รู้จักช่อง ไม่รองรับ `type` หรือการตรวจสอบ OAuth2 ไม่สําเร็จ |
| 404 | `not_found` | ไม่มีข้อมูลเข้าสู่ระบบที่มีรหัสดังกล่าว |
| 409 | `aborted` | มีข้อมูลเข้าสู่ระบบที่มีรหัสดังกล่าวอยู่แล้ว |

ระบบจะปฏิเสธฟิลด์ที่ไม่รู้จักแทนที่จะเพิกเฉย และชื่อข้อผิดพลาดจะระบุชื่อฟิลด์

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## ขั้นตอนถัดไป

- [สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): ดูวิธีที่เอเจนต์เรียกใช้โค้ดและคงไฟล์ไว้
- [ภาพรวมของ Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของ Agent ที่มีการจัดการ
- [การสร้าง Agent ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th): กำหนด Agent ของคุณเองโดยใช้ `AGENTS.md` และ `SKILL.md`

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-07 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-07 UTC"],[],[]]
