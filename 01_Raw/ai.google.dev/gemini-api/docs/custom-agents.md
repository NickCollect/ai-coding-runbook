---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=th
fetched_at: 2026-09-21T05:56:27.344257+00:00
title: "\u0e01\u0e32\u0e23\u0e2a\u0e23\u0e49\u0e32\u0e07 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การสร้าง Agent ที่มีการจัดการ

Agent ที่ได้รับการจัดการใน Gemini API ช่วยให้คุณขยาย Agent ของ Antigravity ด้วยคำสั่ง ทักษะ และข้อมูลของคุณเองได้ คุณสามารถ[ปรับแต่งเอเจนต์ในบรรทัด](#customize-inline)ในเวลาที่โต้ตอบ หรือ[บันทึกการกำหนดค่า](#save-agent)เป็นเอเจนต์ที่มีการจัดการซึ่งคุณเรียกใช้ด้วยรหัส

## ปรับแต่ง Agent ของ Antigravity

วิธีที่เร็วที่สุดในการสร้างเอเจนต์ที่กำหนดเองคือการส่งการกำหนดค่าแบบอินไลน์ขณะสร้างการโต้ตอบใหม่โดยไม่ต้องลงทะเบียน คุณขยาย Agent ได้หลายวิธีหลักๆ ดังนี้

- **[การเลือกโมเดล](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#model-selection)**: เลือกโมเดล Gemini พื้นฐานผ่าน `agent_config` (ค่าเริ่มต้นคือ **Gemini 3.8 Flash**)
- **คำสั่งของระบบ**: ส่งข้อความในบรรทัดผ่าน `system_instruction` เพื่อกำหนดลักษณะการทำงาน
- **เครื่องมือ**: ลบล้างเครื่องมือเริ่มต้น (การดำเนินการโค้ด การค้นหา บริบท URL) ลงทะเบียนเซิร์ฟเวอร์ MCP ระยะไกล หรือกำหนดฟังก์ชันที่กำหนดเอง (การเรียกใช้ฟังก์ชัน)
- **ไฟล์และทักษะ**: เมานต์ไฟล์ เช่น `AGENTS.md` และ `SKILL.md` ลงในสภาพแวดล้อม

ตัวอย่างการส่งทั้ง 3 รายการแบบอินไลน์

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a slide deck."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
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

ทุกอย่างจะกำหนดไว้ในเวลาที่เกิดการโต้ตอบ โดยคุณไม่จำเป็นต้องลงทะเบียนอะไรก่อน ระบบควบคุมการทำงานของ Agent ของ Antigravity มีรันไทม์ (การเรียกใช้โค้ด การจัดการไฟล์ การเข้าถึงเว็บ) และเลเยอร์การกำหนดค่าของคุณอยู่ด้านบน

### เครื่องมือและวิธีการของระบบ

คุณปรับแต่งลักษณะการทำงานและความสามารถของเอเจนต์สำหรับการโต้ตอบที่เฉพาะเจาะจงได้โดยใช้พารามิเตอร์ `system_instruction` และ `tools`

- **วิธีการของระบบ**: ใช้พารามิเตอร์ `system_instruction` เพื่อส่งข้อความในบรรทัดที่กำหนดลักษณะการทำงานของเอเจนต์ ซึ่งเหมาะสำหรับการปรับแต่งอย่างรวดเร็วที่คุณต้องการเปลี่ยนแปลงต่อการโทร `system_instruction` และ `AGENTS.md` จะเพิ่มขึ้น โดยทั้ง 2 อย่างจะมีผลเมื่อมีอยู่
- **เครื่องมือ**: โดยค่าเริ่มต้น Agent ของ Antigravity จะมีสิทธิ์เข้าถึง `code_execution`, `google_search` และ `url_context` คุณลบล้างรายการนี้ได้โดยส่งพารามิเตอร์ `tools` ในเวลาที่เกิดการโต้ตอบ นอกจากนี้ คุณยังลงทะเบียน[เซิร์ฟเวอร์ MCP ระยะไกล](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#mcp-servers)หรือกำหนด[ฟังก์ชันที่กำหนดเอง (การเรียกใช้ฟังก์ชัน)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#function-calling) เพื่อเชื่อมต่อเอเจนต์กับ API และฐานข้อมูลของคุณเองได้ด้วย โปรดดูรายละเอียดทั้งหมดเกี่ยวกับเครื่องมือที่มีที่หัวข้อ [Antigravity Agent: เครื่องมือที่รองรับ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#supported-tools)

### การปรับแต่งตามไฟล์

#### โครงสร้างไดเรกทอรีของ Agent

แม้ว่าคุณจะส่งการกำหนดค่าแบบอินไลน์ได้ แต่เราขอแนะนำให้จัดระเบียบไฟล์ของเอเจนต์ในไดเรกทอรีที่มีโครงสร้าง ซึ่งจะช่วยให้จัดการ ควบคุมเวอร์ชัน และติดตั้งในสภาพแวดล้อมของเอเจนต์ได้ง่ายขึ้น

ไดเรกทอรีโปรเจ็กต์เอเจนต์ทั่วไปมีลักษณะดังนี้

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

Agent จะโหลด `.agents/AGENTS.md` (หรือ `/.agents/AGENTS.md`) จากสภาพแวดล้อมโดยอัตโนมัติเป็นคำสั่งของระบบเมื่อเริ่มต้น ใช้ `AGENTS.md` สำหรับคำจำกัดความของกลุ่มเป้าหมายแบบยาว หลักเกณฑ์โดยละเอียด และวิธีการที่คุณต้องการควบคุมเวอร์ชันควบคู่ไปกับโค้ด

เมานต์ `AGENTS.md` โดยใช้แหล่งข้อมูลในบรรทัด

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a report."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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

ทักษะคือไฟล์ที่ขยายความสามารถของ Agent วางไว้ใต้ `.agents/skills/<skill-name>/SKILL.md` แล้ว Harness จะค้นหาและลงทะเบียนโดยอัตโนมัติ

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
    agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Create a presentation about our Q1 results."))
    .systemInstruction("You create presentations from data.")
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
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

เมื่อทำการกำหนดค่าซ้ำแล้ว คุณจะสร้างเป็นเอเจนต์ที่มีการจัดการด้วย `agents.create` ได้ ซึ่งช่วยให้คุณเรียกใช้ Agent ตามรหัสได้โดยไม่ต้องกำหนดค่าซ้ำทุกครั้ง

`id` ที่คุณระบุเมื่อสร้างเอเจนต์ที่มีการจัดการต้องไม่ซ้ำกันในโปรเจ็กต์ของคุณ และต้องไม่ขึ้นต้นด้วยคำนำหน้าที่สงวนไว้ (เช่น `google-`, `gemini-`) ดูรายการคำนำหน้าที่ถูกจำกัดทั้งหมดได้ที่[ข้อจำกัดของรหัสเอเจนต์](#agent-id-restrictions)

### จากแหล่งข้อมูล

ระบุ `base_agent`, `id`, `agent_config`, `system_instruction` และ `base_environment` พร้อมแหล่งที่มา แพลตฟอร์มจะจัดสรรแซนด์บ็อกซ์ใหม่พร้อมไฟล์ของคุณทุกครั้งที่เรียกใช้ ดูประเภทแหล่งข้อมูลที่ใช้ได้ (Git, GCS, อินไลน์) ใน[สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th)

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-09-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.8-flash",
    },
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
    base_agent: "antigravity-preview-09-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.8-flash",
    },
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.AgentConfig;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build(),
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/analysis-templates")
            .target("/workspace/templates")
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .agentConfig(AgentConfig.of(
        AntigravityAgentConfig.builder()
            .model("gemini-3.8-flash")
            .build()
    ))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created agent: " + agent.id().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-09-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.8-flash"
    },
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

วนซ้ำกับเอเจนต์ Antigravity ฐานจนกว่าสภาพแวดล้อมจะเหมาะสม (ติดตั้งแพ็กเกจแล้ว วางไฟล์แล้ว) จากนั้นแยกเป็นเอเจนต์ที่มีการจัดการ

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-09-2026",
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
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-09-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// Step 1: set up the environment interactively
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Step 2: fork that environment into a managed agent
Agent agentParams = Agent.builder()
    .id("my-data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You are a data analyst. Use the template at /workspace/template.py for all reports.")
    .baseEnvironment(BaseEnvironment.of(interaction.environmentId().orElse("")))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Forked agent successfully: " + agent.id().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### ใช้กฎเครือข่าย

คุณสามารถล็อกการเข้าถึงขาออกหรือแทรกข้อมูลเข้าสู่ระบบเมื่อบันทึกเอเจนต์ที่มีการจัดการ ดูสคีมารายการที่อนุญาต รูปแบบข้อมูลเข้าสู่ระบบ และสัญลักษณ์แทนทั้งหมดได้ที่[สภาพแวดล้อม: การกำหนดค่าเครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration)

อ้างอิง[ข้อมูลเข้าสู่ระบบ](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=th)ที่จัดเก็บไว้ตามรหัสในกฎรายการที่อนุญาต (`"credential": "github-production"`) และพร็อกซีขาออกจะแทรกข้อมูลลับในเวลาที่ส่งคำขอ จึงไม่มีการระบุข้อมูลลับในคำจำกัดความของเอเจนต์ ตัวอย่างนี้จะตั้งค่าส่วนหัวแบบอินไลน์ด้วย `transform` แทน พร็อกซีจะใช้ทั้ง 2 รูปแบบในลักษณะเดียวกัน นอกจากนี้ ข้อมูลเข้าสู่ระบบยังช่วยให้คุณนำข้อมูลลับไปใช้ซ้ำในเอเจนต์ต่างๆ และหมุนเวียนข้อมูลลับได้ในที่เดียว

ตัวอย่างต่อไปนี้สร้าง`issue-resolver`เอเจนต์ที่เข้าถึงได้เฉพาะ GitHub และ PyPI โดยมีการแทรกข้อมูลเข้าสู่ระบบสำหรับ GitHub

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-09-2026",
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
    base_agent: "antigravity-preview-09-2026",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/backend")
            .target("/workspace/repo")
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            ))
            .build()
    )))
    .build();

Agent agentParams = Agent.builder()
    .id("issue-resolver")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created issue-resolver agent successfully: " + agent.id().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-09-2026",
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

โทรหา Agent ที่มีการจัดการด้วยรหัส Agent โดยสร้างการโต้ตอบใหม่ การเรียกใช้แต่ละครั้งจะแยกสภาพแวดล้อมพื้นฐานออกเป็นหลายๆ ส่วน ดังนั้นการเรียกใช้ทุกครั้งจึงเริ่มต้นจากสภาพแวดล้อมที่สะอาด

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
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

สำหรับการสนทนาไปมาและการสตรีม โปรดดู[คู่มือเริ่มใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th) รูปแบบ `previous_interaction_id` และ `environment` เดียวกันนี้จะมีผลกับเอเจนต์ที่มีการจัดการ

นอกจากนี้ เอเจนต์ที่มีการจัดการยังรองรับการดำเนินการและการยกเลิกในเบื้องหลังด้วย ดูรายละเอียดและตัวอย่างโค้ดได้ที่[Antigravity Agent: การดำเนินการในเบื้องหลัง](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th#background-execution)

## การลบล้างการกำหนดค่าเมื่อเรียกใช้

คุณสามารถลบล้างการกำหนดค่าเครือข่าย `system_instruction`, `tools` และ `environment` เริ่มต้นของเอเจนต์เมื่อสร้างการโต้ตอบ ซึ่งจะช่วยให้คุณแก้ไขลักษณะการทำงาน ความสามารถ หรือข้อมูลเข้าสู่ระบบของเอเจนต์สำหรับการเรียกใช้ที่เฉพาะเจาะจงได้โดยไม่ต้องเปลี่ยนคำจำกัดความของเอเจนต์ที่จัดเก็บไว้

### ลบล้างคำสั่งและเครื่องมือของระบบ

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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table."))
    .systemInstruction("You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.")
    .tools(List.of(CodeExecution.builder().build())) // Override to only use code execution
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
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

### ลบล้างการกำหนดค่าเครือข่าย (รีเฟรชข้อมูลเข้าสู่ระบบ)

หากเอเจนต์ที่มีการจัดการมีข้อมูลเข้าสู่ระบบเครือข่ายฝังอยู่ใน `base_environment`,
คุณจะลบล้างข้อมูลดังกล่าวในเวลาที่เรียกใช้เพื่อรีเฟรชโทเค็นที่หมดอายุหรือหมุนเวียนคีย์ API ได้
ส่งออบเจ็กต์ `environment` ที่มีการกำหนดค่า `network` ใหม่ กฎเครือข่ายใหม่จะแทนที่กฎก่อนหน้าสำหรับการโต้ตอบนั้นโดยสมบูรณ์ แหล่งที่มา (ไฟล์ ที่เก็บ) ของ
สภาพแวดล้อมพื้นฐานจะยังคงอยู่

หาก `base_environment` อ้างอิง[ข้อมูลเข้าสู่ระบบ](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=th)ที่จัดเก็บไว้แทนโทเค็นแบบอินไลน์ คุณก็ไม่จำเป็นต้องลบล้างสิ่งใด หมุนเวียนข้อมูลเข้าสู่ระบบด้วย `PATCH` และทุก
เอเจนต์ที่อ้างอิงข้อมูลเข้าสู่ระบบนั้นจะรับข้อมูลลับใหม่ในการเรียกใช้ครั้งถัดไป

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Invoke the agent with a fresh token, overriding the base_environment credentials
Environment env = Environment.builder()
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_REFRESHED_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("issue-resolver"))
    .input(InteractionsInput.of("Fix issue #42 and open a PR."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import java.util.List;

Client client = new Client();

List<Agent> agents = client.agents.listDirect().agentListResponse().get().agents().orElse(List.of());
for (Agent a : agents) {
    System.out.println(a.id().orElse("") + ": " + a.description().orElse(""));
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;

Client client = new Client();

Agent agent = client.agents.get("data-analyst").agent().get();
System.out.println(agent);
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

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## ข้อมูลอ้างอิงคำจำกัดความของ Agent

| ช่อง | ประเภท | ต้องระบุ | คำอธิบาย |
| --- | --- | --- | --- |
| `id` | สตริง | ใช่ | ตัวระบุที่ไม่ซ้ำกันของ Agent ภายในโปรเจ็กต์ที่อยู่ในระบบคลาวด์ของ Google ใช้เพื่อเรียกใช้ Agent ต้องไม่ใช้คำนำหน้าที่สงวนไว้ ดู[ข้อจำกัดของรหัสตัวแทน](#agent-id-restrictions) |
| `description` | สตริง | ไม่ | คำอธิบาย Agent ที่มนุษย์อ่านได้ |
| `base_agent` | สตริง | ใช่ | รหัสตัวแทนฐาน (เช่น `antigravity-preview-09-2026`) |
| `agent_config` | ออบเจ็กต์ | ไม่ | การกำหนดค่าสำหรับเอเจนต์พื้นฐาน รวมถึงการเลือกรุ่น (`{"type": "antigravity", "model": "gemini-3.8-flash"}`) ค่าเริ่มต้นคือ `gemini-3.8-flash` หากละเว้น ไม่สามารถลบล้างได้ในเวลาที่โต้ตอบสำหรับตัวแทนที่มีชื่อ |
| `system_instruction` | สตริง | ไม่ | พรอมต์ของระบบที่กำหนดลักษณะการทำงานและตัวตน |
| `tools` | อาร์เรย์ | ไม่ | เครื่องมือที่ตัวแทนใช้ได้ หากละไว้ ค่าเริ่มต้นจะเป็น `code_execution`, `google_search` และ `url_context` เครื่องมือที่รองรับ ได้แก่ `code_execution`, `google_search`, `url_context`, `mcp_server` และคำจำกัดความ `function` ที่กำหนดเอง |
| `base_environment` | สตริงหรือออบเจ็กต์ | ไม่ | `"remote"`, `environment_id` หรือออบเจ็กต์การกำหนดค่าที่มี `sources` และ `network` ดูสภาพแวดล้อม |

### ข้อจำกัดเกี่ยวกับรหัสตัวแทน

เมื่อสร้างเอเจนต์ที่มีการจัดการ `id` ที่คุณระบุต้องเป็นไปตามกฎต่อไปนี้

- โดยต้องไม่ซ้ำกันในโปรเจ็กต์ Google Cloud
- ต้อง**ไม่**ขึ้นต้นด้วยคำนำหน้าที่สงวนไว้ต่อไปนี้ (ไม่คำนึงถึงตัวพิมพ์เล็กและตัวพิมพ์ใหญ่) ไม่เช่นนั้นการสร้างจะล้มเหลว
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## เวิร์กโฟลว์การทำซ้ำ

1. **สร้างต้นแบบ**ด้วย Agent พื้นฐานของ Antigravity ส่งคำสั่งของระบบและแหล่งที่มาของสภาพแวดล้อมแบบอินไลน์ ทดสอบวิธีการ ทักษะ และการตั้งค่าสภาพแวดล้อมแบบอินเทอร์แอกทีฟ
2. **รักษาความเสถียร**ของสภาพแวดล้อม ติดตั้งแพ็กเกจ เมานต์แหล่งที่มา และตรวจสอบว่าทุกอย่างทำงานได้
3. **คงอยู่**ในฐานะ Agent ที่มีการจัดการโดยการสร้าง Agent ใหม่จากแหล่งที่มาหรือโดยการแยกสาขาสภาพแวดล้อม
4. **อัปเดต**คำจำกัดความของเอเจนต์ เปลี่ยนคำสั่งของระบบ สลับทักษะ หรือเพิ่มแหล่งข้อมูล การเรียกใช้ครั้งถัดไปจะใช้การกำหนดค่าใหม่

## ข้อจำกัด

- **สถานะเวอร์ชันตัวอย่าง**: เอเจนต์ที่มีการจัดการอยู่ในเวอร์ชันตัวอย่าง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **เอเจนต์และโมเดลพื้นฐาน**: รองรับเฉพาะ `antigravity-preview-09-2026` เป็น `base_agent` ตัวเลือกโมเดลที่รองรับใน `agent_config` ได้แก่ `gemini-3.8-flash` (ค่าเริ่มต้น), `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash` และ `gemini-3.5-flash-lite` สำหรับเอเจนต์ที่มีชื่อ คุณจะลบล้างโมเดลในเวลาที่โต้ตอบไม่ได้
- **ไม่มีการกำหนดเวอร์ชัน**: การกำหนดเวอร์ชันและการย้อนกลับของเอเจนต์ยังไม่พร้อมใช้งาน
- **ไม่มีการซ้อน Agent ย่อย**: ระบบยังไม่รองรับการมอบสิทธิ์ Agent ย่อย
- คุณมีตัวแทนที่มีการจัดการได้สูงสุด 1,000 ราย

## ขั้นตอนถัดไป

- [ภาพรวมของ Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของ Agent ที่มีการจัดการ
- [เริ่มต้นใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): เริ่มสร้างด้วยการสนทนาไปมาและการสตรีม
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): ดูความสามารถ เครื่องมือ และราคาของเอเจนต์เริ่มต้น
- [สภาพแวดล้อมของเอเจนต์](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): กำหนดค่าแซนด์บ็อกซ์ แหล่งที่มา และเครือข่าย
- [Managed Agents API ใน Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=th): สำหรับการสร้าง Agent ที่ได้รับการจัดการซึ่งมีการกำกับดูแลขององค์กรในตัว

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-18 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-18 UTC"],[],[]]
