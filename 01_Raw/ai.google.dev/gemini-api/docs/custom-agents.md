---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=th
fetched_at: 2026-06-15T06:19:43.787500+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้าง Agent ที่มีการจัดการ

Agent ที่มีการจัดการใน Gemini API ช่วยให้คุณขยาย Agent Antigravity ด้วยคำสั่ง ทักษะ และข้อมูลของคุณเองได้ คุณสามารถ[ปรับแต่งเอเจนต์ในบรรทัด](#customize-inline)ในเวลาที่โต้ตอบ หรือ[บันทึกการกำหนดค่า](#save-agent)เป็นเอเจนต์ที่มีการจัดการซึ่งคุณเรียกใช้ด้วยรหัส

## ปรับแต่งเอเจนต์แรงโน้มถ่วง

วิธีที่เร็วที่สุดในการสร้างเอเจนต์ที่กำหนดเองคือการส่งการกำหนดค่าแบบอินไลน์ขณะสร้างการโต้ตอบใหม่โดยไม่ต้องลงทะเบียน คุณขยาย Agent ได้ 3 วิธีดังนี้

- **คำสั่งของระบบ**: ส่งข้อความในบรรทัดผ่าน `system_instruction` เพื่อกำหนดลักษณะการทำงาน
- **เครื่องมือ**: ลบล้างเครื่องมือเริ่มต้น (การดำเนินการโค้ด การค้นหา บริบท URL)
- **ไฟล์และทักษะ**: เมานต์ไฟล์ เช่น `AGENTS.md` และ `SKILL.md` ลงในสภาพแวดล้อม

ตัวอย่างการส่งทั้ง 3 รายการแบบอินไลน์

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
-H "Api-Revision: 2026-05-20" \
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

ทุกอย่างจะกำหนดไว้ในเวลาที่เกิดการโต้ตอบ โดยคุณไม่จำเป็นต้องลงทะเบียนอะไรก่อน ฮาร์เนสของเอเจนต์ Antigravity จะให้รันไทม์ (การรันโค้ด การจัดการไฟล์ การเข้าถึงเว็บ) และเลเยอร์การกำหนดค่าของคุณอยู่ด้านบน

### เครื่องมือและวิธีการของระบบ

คุณปรับแต่งลักษณะการทำงานและความสามารถของเอเจนต์สำหรับการโต้ตอบที่เฉพาะเจาะจงได้โดยใช้พารามิเตอร์ `system_instruction` และ `tools`

- **คำสั่งของระบบ**: ใช้พารามิเตอร์ `system_instruction` เพื่อส่งข้อความในบรรทัดที่กำหนดลักษณะการทำงานของเอเจนต์ ซึ่งเหมาะสำหรับการปรับแต่งอย่างรวดเร็วที่คุณต้องการเปลี่ยนแปลงต่อการโทร `system_instruction` และ `AGENTS.md` จะเพิ่มขึ้น โดยทั้ง 2 อย่างจะมีผลเมื่อมีอยู่
- **เครื่องมือ**: โดยค่าเริ่มต้น เอเจนต์ Antigravity จะมีสิทธิ์เข้าถึง `code_execution`, `google_search` และ `url_context` คุณลบล้างรายการนี้ได้โดยส่งพารามิเตอร์ `tools` ในเวลาที่เกิดการโต้ตอบ ดูรายละเอียดทั้งหมดเกี่ยวกับเครื่องมือที่มีและวิธีใช้ได้ที่[Antigravity Agent: เครื่องมือที่รองรับ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#supported-tools)

### การปรับแต่งตามไฟล์

#### โครงสร้างไดเรกทอรีของ Agent

แม้ว่าคุณจะส่งการกำหนดค่าแบบอินไลน์ได้ แต่เราขอแนะนำให้จัดระเบียบไฟล์ของเอเจนต์ในไดเรกทอรีที่มีโครงสร้าง ซึ่งจะช่วยให้จัดการ ควบคุมเวอร์ชัน และติดตั้งในสภาพแวดล้อมของเอเจนต์ได้ง่ายขึ้น

ไดเรกทอรีโปรเจ็กต์ของเอเจนต์ทั่วไปมีลักษณะดังนี้

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

รันไทม์ Antigravity จะสแกน `.agents/` (และรูทของสภาพแวดล้อม) เพื่อหาไฟล์เหล่านี้

#### AGENTS.md

เอเจนต์จะโหลด `.agents/AGENTS.md` (หรือ `/.agents/AGENTS.md`) จากสภาพแวดล้อมโดยอัตโนมัติเป็นคำสั่งของระบบเมื่อเริ่มต้น ใช้ `AGENTS.md` สำหรับคำจำกัดความของกลุ่มเป้าหมายแบบยาว หลักเกณฑ์โดยละเอียด และวิธีการที่คุณต้องการควบคุมเวอร์ชันควบคู่ไปกับโค้ด

เมานต์ `AGENTS.md` โดยใช้แหล่งข้อมูลในบรรทัด

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
  -H "Api-Revision: 2026-05-20" \
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

ทักษะคือไฟล์ที่ขยายความสามารถของเอเจนต์ วางไว้ใต้ `.agents/skills/<skill-name>/SKILL.md` แล้ว Harness จะค้นหาและลงทะเบียนโดยอัตโนมัติ

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

ติดตั้งทักษะโดยใช้แหล่งข้อมูลในบรรทัด

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
  -H "Api-Revision: 2026-05-20" \
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

## สร้าง Agent ที่มีการจัดการ

เมื่อปรับปรุงการกำหนดค่าแล้ว คุณจะสร้างเป็นเอเจนต์ที่มีการจัดการด้วย `agents.create` ได้ ซึ่งช่วยให้คุณเรียกใช้ Agent ตามรหัสได้โดยไม่ต้องกำหนดค่าซ้ำทุกครั้ง

### จากแหล่งที่มา

ระบุ `base_agent`, `id`, `system_instruction` และ `base_environment` พร้อมแหล่งที่มา แพลตฟอร์มจะจัดสรรแซนด์บ็อกซ์ใหม่พร้อมไฟล์ของคุณทุกครั้งที่เรียกใช้ ดูประเภทแหล่งข้อมูลที่ใช้ได้ (Git, GCS, อินไลน์) ใน[สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th)

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
-H "Api-Revision: 2026-05-20" \
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

### จากสภาพแวดล้อมที่มีอยู่ (Fork)

วนซ้ำกับเอเจนต์ Antigravity พื้นฐานจนกว่าสภาพแวดล้อมจะพร้อม (ติดตั้งแพ็กเกจแล้ว วางไฟล์แล้ว) จากนั้นแยกเป็นเอเจนต์ที่มีการจัดการ

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### ด้วยกฎเครือข่าย

คุณสามารถล็อกการเข้าถึงขาออกหรือแทรกข้อมูลเข้าสู่ระบบเมื่อบันทึกเอเจนต์ที่มีการจัดการ ดูสคีมารายการที่อนุญาต รูปแบบข้อมูลเข้าสู่ระบบ และสัญลักษณ์แทนทั้งหมดได้ที่[สภาพแวดล้อม: การกำหนดค่าเครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration)

ตัวอย่างต่อไปนี้สร้างเอเจนต์ `issue-resolver` ที่เข้าถึงได้เฉพาะ GitHub และ PyPI โดยมีการแทรกข้อมูลเข้าสู่ระบบสำหรับ GitHub

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
  -H "Api-Revision: 2026-05-20" \
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

เรียกใช้ Agent ที่มีการจัดการด้วยรหัส Agent โดยสร้างการโต้ตอบใหม่ การเรียกใช้แต่ละครั้งจะแยกสภาพแวดล้อมพื้นฐานออกเป็น 2 ส่วน ดังนั้นการเรียกใช้ทุกครั้งจึงเริ่มต้นจากสภาพแวดล้อมที่สะอาด

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

สำหรับการสนทนาแบบหลายรอบและการสตรีม โปรดดู[การเริ่มต้นอย่างรวดเร็ว](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th) รูปแบบ `previous_interaction_id` และ `environment` เดียวกันนี้จะมีผลกับตัวแทนที่มีการจัดการ

## การลบล้างการกำหนดค่าเมื่อเรียกใช้

คุณลบล้าง `system_instruction` และ `tools` เริ่มต้นของตัวแทนได้เมื่อสร้างการโต้ตอบ ซึ่งจะช่วยให้คุณแก้ไขลักษณะการทำงานหรือความสามารถของเอเจนต์สำหรับการเรียกใช้ที่เฉพาะเจาะจงได้โดยไม่ต้องเปลี่ยนคำจำกัดความของเอเจนต์ที่จัดเก็บไว้

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

## จัดการ Agent

คุณแสดงรายการ รับ และลบเอเจนต์ได้

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

### รับตัวแทน

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

การลบจะนำการกำหนดค่าออก สภาพแวดล้อมและการโต้ตอบที่มีอยู่ซึ่งสร้างโดยเอเจนต์จะไม่ได้รับผลกระทบ

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
| `id` | สตริง | ใช่ | ตัวระบุเอเจนต์ที่ไม่ซ้ำกัน ใช้เพื่อเรียกใช้ Agent |
| `description` | สตริง | ไม่ | คำอธิบายที่มนุษย์อ่านได้ของ Agent |
| `base_agent` | สตริง | ใช่ | รหัสตัวแทนฐาน (เช่น `antigravity-preview-05-2026`) |
| `system_instruction` | สตริง | ไม่ | พรอมต์ของระบบที่กำหนดลักษณะการทำงานและตัวตน |
| `tools` | สตริงหรือออบเจ็กต์ | ไม่ | เครื่องมือที่ตัวแทนใช้ได้ หากละเว้นไว้ ตัวแทนจะมีสิทธิ์เข้าถึง `code_execution`, `google_search` และ `url_context` |
| `base_environment` | สตริงหรือออบเจ็กต์ | ไม่ | `"remote"`, `environment_id` หรือออบเจ็กต์การกำหนดค่าที่มี `sources` และ `network` ดูสภาพแวดล้อม |

## เวิร์กโฟลว์การทำซ้ำ

1. **สร้างต้นแบบ**ด้วย Agent Antigravity พื้นฐาน ส่งคำสั่งของระบบและแหล่งที่มาของสภาพแวดล้อมแบบอินไลน์ ทดสอบวิธีการ ทักษะ และการตั้งค่าสภาพแวดล้อมแบบอินเทอร์แอกทีฟ
2. **รักษาความเสถียร**ของสภาพแวดล้อม ติดตั้งแพ็กเกจ เมานต์แหล่งที่มา และตรวจสอบว่าทุกอย่างทำงานได้
3. **คงอยู่**ในฐานะเอเจนต์ที่มีการจัดการโดยการสร้างเอเจนต์ใหม่จากแหล่งที่มาหรือโดยการแยกสาขาสภาพแวดล้อม
4. **อัปเดต**คำจำกัดความของเอเจนต์ เปลี่ยนคำสั่งของระบบ สลับทักษะ หรือเพิ่มแหล่งข้อมูล การเรียกใช้ครั้งถัดไปจะใช้การกำหนดค่าใหม่

## ข้อจำกัด

- **สถานะเวอร์ชันตัวอย่าง**: เอเจนต์ที่มีการจัดการอยู่ในเวอร์ชันตัวอย่าง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **เอเจนต์พื้นฐาน**: รองรับเฉพาะ `antigravity-preview-05-2026` เป็น `base_agent`
- **ไม่มีการกำหนดเวอร์ชัน**: การกำหนดเวอร์ชันและการย้อนกลับของ Agent ยังไม่พร้อมใช้งาน
- **ไม่มีการซ้อน Agent ย่อย**: ระบบยังไม่รองรับการมอบสิทธิ์ Agent ย่อย
- คุณมีตัวแทนที่มีการจัดการได้สูงสุด 1,000 ราย

## ขั้นตอนถัดไป

- [ภาพรวมของ Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของ Agent ที่มีการจัดการ
- [เริ่มต้นใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): เริ่มสร้างด้วยการสนทนาแบบหลายรอบและการสตรีม
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): สำรวจความสามารถ เครื่องมือ และราคาของเอเจนต์เริ่มต้น
- [สภาพแวดล้อมของเอเจนต์](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): กำหนดค่าแซนด์บ็อกซ์ แหล่งที่มา และเครือข่าย

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-01 UTC"],[],[]]
