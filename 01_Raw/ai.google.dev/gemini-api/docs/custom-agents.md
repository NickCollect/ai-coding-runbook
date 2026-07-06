---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=th
fetched_at: 2026-07-06T05:18:01.253763+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้าง Agent ที่มีการจัดการ

Managed Agent ใน Gemini API ช่วยให้คุณขยาย Agent ของ Antigravity ด้วยวิธีการ ทักษะ และข้อมูลของคุณเอง คุณสามารถ [ปรับแต่ง Agent แบบอินไลน์](#customize-inline) ในระหว่างการโต้ตอบ หรือ [บันทึกการกำหนดค่า](#save-agent) เป็น Managed Agent ที่คุณเรียกใช้ด้วยรหัสได้

## ปรับแต่ง Agent ของ Antigravity

วิธีที่เร็วที่สุดในการสร้าง Agent ที่กำหนดเองคือการส่งการกำหนดค่าแบบอินไลน์ขณะสร้างการโต้ตอบใหม่โดยไม่ต้องลงทะเบียน คุณสามารถขยาย Agent ได้ 3 วิธีดังนี้

- **วิธีการของระบบ**: ส่งข้อความแบบอินไลน์ผ่าน `system_instruction` เพื่อกำหนดลักษณะการทำงาน
- **เครื่องมือ**: ลบล้างเครื่องมือเริ่มต้น (การรันโค้ด การค้นหา บริบท URL) ลงทะเบียนเซิร์ฟเวอร์ MCP ระยะไกล หรือกำหนดฟังก์ชันที่กำหนดเอง (การเรียกใช้ฟังก์ชัน)
- **ไฟล์และทักษะ**: เมานต์ไฟล์ เช่น `AGENTS.md` และ `SKILL.md` ลงในสภาพแวดล้อม

ตัวอย่างการส่งทั้ง 3 อย่างแบบอินไลน์

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",        
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",        
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

ทุกอย่างจะกำหนดไว้ในระหว่างการโต้ตอบ จึงไม่จำเป็นต้องลงทะเบียนสิ่งใดก่อน ระบบควบคุมการทำงานของ Agent ของ Antigravity จะมีรันไทม์ (การเรียกใช้โค้ด การจัดการไฟล์ การเข้าถึงเว็บ) และเลเยอร์การกำหนดค่าของคุณอยู่ด้านบน

### เครื่องมือและวิธีการของระบบ

คุณสามารถปรับแต่งลักษณะการทำงานและความสามารถของ Agent สำหรับการโต้ตอบที่เฉพาะเจาะจงได้โดยใช้พารามิเตอร์ `system_instruction` และ `tools`

- **วิธีการของระบบ**: ใช้พารามิเตอร์ `system_instruction` เพื่อส่งข้อความแบบอินไลน์ที่กำหนดลักษณะการทำงานของ Agent ซึ่งเหมาะสำหรับการปรับเปลี่ยนอย่างรวดเร็วที่คุณต้องการเปลี่ยนแปลงตามการเรียกใช้ `system_instruction` และ `AGENTS.md` เป็นแบบเพิ่มเติม ซึ่งทั้ง 2 อย่างจะมีผลเมื่อมีอยู่
- **เครื่องมือ**: โดยค่าเริ่มต้น Agent ของ Antigravity จะมีสิทธิ์เข้าถึง `code_execution`, `google_search` และ `url_context` คุณสามารถลบล้างรายการนี้ได้โดยส่งพารามิเตอร์ `tools` ในระหว่างการโต้ตอบ นอกจากนี้ คุณยังลงทะเบียน [เซิร์ฟเวอร์ MCP ระยะไกล](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#mcp-servers) หรือกำหนด [ฟังก์ชันที่กำหนดเอง (การเรียกใช้ฟังก์ชัน)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#function-calling) เพื่อเชื่อมต่อ Agent กับ API และฐานข้อมูลของคุณเองได้ด้วย ดูรายละเอียดทั้งหมดเกี่ยวกับเครื่องมือที่พร้อมใช้งานได้ที่ [Antigravity Agent: เครื่องมือที่รองรับ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#supported-tools)

### การปรับแต่งตามไฟล์

#### โครงสร้างไดเรกทอรีของ Agent

แม้ว่าคุณจะส่งการกำหนดค่าแบบอินไลน์ได้ แต่เราขอแนะนำให้จัดระเบียบไฟล์ของ Agent ในไดเรกทอรีที่มีโครงสร้าง ซึ่งจะช่วยให้จัดการ ควบคุมเวอร์ชัน และเมานต์ลงในสภาพแวดล้อมของ Agent ได้ง่ายขึ้น

ไดเรกทอรีโปรเจ็กต์ของ Agent โดยทั่วไปจะมีลักษณะดังนี้

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

รันไทม์ของ Antigravity จะสแกนหาไฟล์เหล่านี้ใน `.agents/` (และรูทของสภาพแวดล้อม)

#### AGENTS.md

Agent จะโหลด `.agents/AGENTS.md` (หรือ `/.agents/AGENTS.md`) จากสภาพแวดล้อมเป็นวิธีการของระบบโดยอัตโนมัติเมื่อเริ่มต้น ใช้ `AGENTS.md` สำหรับคำจำกัดความของบุคลิกภาพแบบยาว แนวทางโดยละเอียด และวิธีการที่คุณต้องการควบคุมเวอร์ชันควบคู่ไปกับโค้ด

เมานต์ `AGENTS.md` โดยใช้แหล่งข้อมูลแบบอินไลน์

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### ทักษะ: SKILL.md

ทักษะคือไฟล์ที่ขยายความสามารถของ Agent วางไฟล์ไว้ใน `.agents/skills/<skill-name>/SKILL.md` แล้ว Harness จะค้นพบและลงทะเบียนไฟล์เหล่านั้นโดยอัตโนมัติ

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

เมานต์ทักษะโดยใช้แหล่งข้อมูลแบบอินไลน์

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

ระบบจะค้นพบทักษะที่โหลดจาก `.agents/skills/` และ `/.agents/skills/` โดยอัตโนมัติ

## สร้าง Managed Agent

เมื่อทำซ้ำการกำหนดค่าแล้ว คุณจะสร้างการกำหนดค่าเป็น Managed Agent ได้ด้วย `agents.create` ซึ่งจะช่วยให้คุณเรียกใช้ Agent ด้วยรหัสได้โดยไม่ต้องทำซ้ำการกำหนดค่าทุกครั้ง

### จากแหล่งข้อมูล

ระบุ `base_agent`, `id`, `system_instruction` และ `base_environment` พร้อมแหล่งข้อมูล แพลตฟอร์มจะจัดเตรียมแซนด์บ็อกซ์ใหม่ที่มีไฟล์ของคุณทุกครั้งที่เรียกใช้ ดูประเภทแหล่งข้อมูลที่พร้อมใช้งาน (Git, GCS, อินไลน์) ได้ที่ [สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th)

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### จากสภาพแวดล้อมที่มีอยู่ (fork)

ทำซ้ำด้วย Agent ของ Antigravity ฐานจนกว่าสภาพแวดล้อมจะถูกต้อง (ติดตั้งแพ็กเกจแล้ว วางไฟล์เรียบร้อย) จากนั้น fork สภาพแวดล้อมนั้นเป็น Managed Agent

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### พร้อมกฎเครือข่าย

คุณสามารถล็อกการเข้าถึงขาออกหรือแทรกข้อมูลเข้าสู่ระบบเมื่อบันทึก Managed Agent ดูสคีมารายการที่อนุญาตทั้งหมด รูปแบบข้อมูลเข้าสู่ระบบ และสัญลักษณ์แทนได้ที่ [สภาพแวดล้อม: การกำหนดค่าเครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration)

ตัวอย่างต่อไปนี้จะสร้าง Agent `issue-resolver` ที่เข้าถึงได้เฉพาะ GitHub และ PyPI โดยมีการแทรกข้อมูลเข้าสู่ระบบสำหรับ GitHub

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-05-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## เรียกใช้ Agent

เรียกใช้ Managed Agent ด้วยรหัส Agent โดยสร้างการโต้ตอบใหม่ การเรียกใช้แต่ละครั้งจะ fork สภาพแวดล้อมฐาน ดังนั้นการเรียกใช้ทุกครั้งจะเริ่มต้นใหม่

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

ดูการสนทนาไปมาและการสตรีมได้ที่[คู่มือเริ่มใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th) รูปแบบ `previous_interaction_id` และ `environment` เดียวกันนี้ใช้ได้กับ Managed Agent

นอกจากนี้ Managed Agent ยังรองรับการรันเบื้องหลังและการยกเลิกด้วย ดูรายละเอียดและตัวอย่างโค้ดได้ที่ [Antigravity Agent: การรันเบื้องหลัง](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#background-execution)

## การลบล้างการกำหนดค่าเมื่อเรียกใช้

คุณสามารถลบล้าง `system_instruction` และ `tools` เริ่มต้นของ Agent ได้เมื่อสร้างการโต้ตอบ ซึ่งจะช่วยให้คุณแก้ไขลักษณะการทำงานหรือความสามารถของ Agent สำหรับการรันที่เฉพาะเจาะจงได้โดยไม่ต้องเปลี่ยนคำจำกัดความของ Agent ที่จัดเก็บไว้

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

## จัดการ Agent

คุณสามารถแสดงรายการ รับ และลบ Agent ได้

### แสดงรายการ Agent

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### รับ Agent

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### ลบ Agent

การลบจะนำการกำหนดค่าออก สภาพแวดล้อมและการโต้ตอบที่มีอยู่ซึ่งสร้างโดย Agent จะไม่ได้รับผลกระทบ

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## ข้อมูลอ้างอิงคำจำกัดความของ Agent

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `id` | สตริง | ใช่ | ตัวระบุที่ไม่ซ้ำกันของ Agent ใช้เพื่อเรียกใช้ Agent |
| `description` | สตริง | ไม่ | คำอธิบาย Agent ที่มนุษย์อ่านได้ |
| `base_agent` | สตริง | ใช่ | รหัส Agent ฐาน (เช่น `antigravity-preview-05-2026`) |
| `system_instruction` | สตริง | ไม่ | พรอมต์ของระบบที่กำหนดลักษณะการทำงานและบุคลิกภาพ |
| `tools` | อาร์เรย์ | ไม่ | เครื่องมือที่ Agent ใช้ได้ หากละไว้ ระบบจะใช้ `code_execution`, `google_search` และ `url_context` เป็นค่าเริ่มต้น เครื่องมือที่รองรับ ได้แก่ `code_execution`, `google_search`, `url_context`, `mcp_server` และคำจำกัดความ `function` ที่กำหนดเอง |
| `base_environment` | สตริงหรือออบเจ็กต์ | ไม่ | `"remote"`, `environment_id` หรือออบเจ็กต์การกำหนดค่าที่มี `sources` และ `network` ดูสภาพแวดล้อม |

## ขั้นตอนการทำซ้ำ

1. **สร้างต้นแบบ** ด้วย Agent ของ Antigravity ฐาน ส่งวิธีการของระบบและแหล่งข้อมูลสภาพแวดล้อมแบบอินไลน์ ทดสอบวิธีการ ทักษะ และการตั้งค่าสภาพแวดล้อมแบบอินเทอร์แอกทีฟ
2. **ทำให้ สภาพแวดล้อมเสถียร** ติดตั้งแพ็กเกจ เมานต์แหล่งข้อมูล ยืนยันว่าทุกอย่างทำงานได้
3. **คงอยู่** เป็น Managed Agent โดยสร้าง Agent ใหม่ ไม่ว่าจะจากแหล่งข้อมูลหรือโดยการ fork สภาพแวดล้อม
4. **อัปเดต** คำจำกัดความของ Agent เปลี่ยนวิธีการของระบบ สลับทักษะ หรือเพิ่มแหล่งข้อมูล การเรียกใช้ครั้งถัดไปจะใช้การกำหนดค่าใหม่

## ข้อจำกัด

- **สถานะเวอร์ชันทดลอง**: Managed Agent อยู่ในเวอร์ชันทดลอง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **Agent ฐาน**: ระบบรองรับเฉพาะ `antigravity-preview-05-2026` เป็น `base_agent`
- **ไม่มีการกำหนดเวอร์ชัน**: การกำหนดเวอร์ชันและการย้อนกลับของ Agent ยังไม่พร้อมใช้งาน
- **ไม่มีการซ้อน Agent ย่อย**: ระบบยังไม่รองรับการมอบสิทธิ์ Agent ย่อย
- คุณมี Managed Agent ได้สูงสุด 1,000 รายการ

## ขั้นตอนถัดไป

- [ภาพรวมของ Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของ Managed Agent
- [การเริ่มต้นอย่างรวดเร็ว](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): เริ่มสร้างด้วยการสนทนาไปมาและการสตรีม
- [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): สำรวจความสามารถ เครื่องมือ และราคาของ Agent เริ่มต้น
- [สภาพแวดล้อมของ Agent](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): กำหนดค่าแซนด์บ็อกซ์ แหล่งข้อมูล และเครือข่าย
- [Managed Agents API ในแพลตฟอร์ม Agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=th): สำหรับการสร้าง Agent ที่มีการกำกับดูแลองค์กรในตัว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-26 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-26 UTC"],[],[]]
