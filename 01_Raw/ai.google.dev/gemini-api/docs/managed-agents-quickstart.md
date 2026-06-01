---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th
fetched_at: 2026-06-01T05:59:40.051854+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน Agent ที่มีการจัดการอย่างรวดเร็ว

คู่มือนี้จะแนะนำขั้นตอนการสร้างและใช้ Managed Agent ใน Gemini API โดยใช้ [Antigravity Agent](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=th) คุณจะได้ทำการเรียก Agent ครั้งแรก สนทนาต่อแบบหลายรอบ สตรีมคำตอบ ดาวน์โหลดไฟล์จากแซนด์บ็อกซ์ และใช้ Antigravity Managed Agent

## เรียกใช้การโต้ตอบกับ Agent ครั้งแรก

การเรียกใช้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th) เพียงครั้งเดียวจะจัดเตรียมแซนด์บ็อกซ์ Linux เรียกใช้ลูปของ Agent และแสดงผลลัพธ์ คุณจะต้องกำหนดพารามิเตอร์ 3 รายการ ดังนี้

- ส่ง `agent` เป็น `"antigravity-preview-05-2026",` ซึ่งเป็นเวอร์ชันปัจจุบันของ Managed Agent ที่กำหนดไว้ล่วงหน้าและมีวัตถุประสงค์ทั่วไป
- กำหนด `environment="remote"` เพื่อจัดเตรียมสภาพแวดล้อมแซนด์บ็อกซ์ใหม่
- สร้างอินพุตเพื่อกำหนดสิ่งที่คุณต้องการให้ Agent ทำ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

การตอบกลับจะแสดงออบเจ็กต์ `Interaction` จัดเก็บ `interaction.id` และ `interaction.environment_id` เพื่อสนทนาต่อในแซนด์บ็อกซ์เดียวกัน ใช้ `interaction.output_text` เพื่อเข้าถึงการตอบกลับสุดท้ายของ Agent `interaction.steps` จะแสดงรายการแต่ละขั้นตอนที่ Agent ดำเนินการ (การให้เหตุผล การเรียกใช้เครื่องมือ การดำเนินการโค้ด)

## สนทนาต่อ (หลายรอบ)

API จะติดตามมิติข้อมูลสถานะ 2 รายการแยกกัน ดังนี้

- **บริบทการสนทนา:** ประวัติการแชท การติดตามการให้เหตุผล การใช้เครื่องมือ โดยใช้ `previous_interaction_id`
- [**สถานะสภาพแวดล้อม:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th) ไฟล์ แพ็กเกจที่ติดตั้ง และสถานะแซนด์บ็อกซ์ โดยใช้ `environment`

ส่งทั้ง 2 รายการในตำแหน่งที่เกี่ยวข้องเพื่อดำเนินการต่อ

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

ไฟล์จากรอบที่ 1 (`fibonacci.txt`) จะยังคงอยู่ในรอบที่ 2 นอกจากนี้ Agent ยังเก็บรักษาบริบทการสนทนาไว้ด้วย

คุณสามารถผสมและจับคู่รายการต่อไปนี้ได้อย่างอิสระ

- **ล้างการสนทนา แต่เก็บไฟล์ไว้:** ละเว้น `previous_interaction_id` และส่งเฉพาะรหัสสภาพแวดล้อมโดยใช้ `environment` เพื่อเริ่มการสนทนาใหม่ในพื้นที่ทำงานเดียวกัน
- **เก็บการสนทนาไว้ แต่ใช้พื้นที่ทำงานใหม่:** ส่ง `previous_interaction_id` และตั้งค่า `environment="remote"` เพื่อใช้แซนด์บ็อกซ์ใหม่

### การบีบอัดบริบทอัตโนมัติ

ในการสนทนาแบบหลายรอบที่ใช้เวลานาน ประวัติการให้เหตุผล การเรียกใช้เครื่องมือ และเนื้อหาไฟล์ขนาดใหญ่จะเพิ่มขึ้นอย่างรวดเร็วและใช้พื้นที่บริบทจำนวนมาก เพื่อป้องกันข้อผิดพลาดเกี่ยวกับขีดจำกัดโทเค็นและรักษาโฟกัสของ Agent (ป้องกัน "บริบทเสื่อม") Managed Agents API จึงมีขั้นตอนการบีบอัดบริบทในตัวเมื่อมีโทเค็นประมาณ 135,000 รายการ ซึ่งจะเกิดขึ้นโดยอัตโนมัติ

## สตรีมคำตอบ

สำหรับงานที่ใช้เวลานาน คุณสามารถสตรีมคำตอบเพื่อดูการทำงานของ Agent แบบเรียลไทม์ได้

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

การสตรีมจะแสดงผลการเปลี่ยนแปลงทีละขั้นตอน ซึ่งเป็นข้อความที่เพิ่มขึ้น โทเค็นการให้เหตุผล และการอัปเดตการเรียกใช้เครื่องมือ ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีสตรีมคำตอบใน[คู่มือการสตรีม](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=th)

## ดาวน์โหลดไฟล์จากสภาพแวดล้อม

เมื่อ Agent สร้างไฟล์ภายในแซนด์บ็อกซ์ ให้ดาวน์โหลดไฟล์โดยใช้ Files API ด้วยคำขอ HTTP โดยตรง (ยังไม่มีเมธอด SDK)

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## บันทึก Managed Agent

ในขั้นตอนก่อนหน้า เราใช้ Antigravity Agent เริ่มต้นและปรับแต่ง Agent แบบอินไลน์ เมื่อทำซ้ำการกำหนดค่า (คำแนะนำ สกิล และสภาพแวดล้อม) แล้ว คุณจะบันทึกการกำหนดค่าเป็น Managed Agent ได้ ซึ่งจะช่วยให้คุณเรียกใช้ Agent ตามรหัสได้โดยไม่ต้องกำหนดค่าซ้ำ

เมื่อบันทึก Agent คุณจะต้องกำหนด `base_environment` (จากแหล่งที่มาหรือโดยการแยกสภาพแวดล้อมที่มีอยู่ออกเป็นอีกสภาพแวดล้อมหนึ่ง) Agent จะใช้สภาพแวดล้อมนี้สำหรับการโต้ตอบใหม่ทุกครั้ง

**จากแหล่งที่มา:** กำหนดแหล่งที่มาแบบอินไลน์ หรือจากแหล่งที่มาอื่นๆ เช่น GitHub หรือ Cloud Storage

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## เรียกใช้ Managed Agent

เมื่อบันทึก Managed Agent แล้ว คุณจะเรียกใช้ Agent ตามรหัสได้ การเรียกใช้แต่ละครั้งจะแยกสภาพแวดล้อมพื้นฐานออกเป็นอีกสภาพแวดล้อมหนึ่ง ดังนั้นการเรียกใช้ทุกครั้งจึงเริ่มต้นด้วยสภาพแวดล้อมที่สะอาด

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## ขั้นตอนถัดไป

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): ความสามารถ เครื่องมือที่รองรับ อินพุตมัลติโมดัล การกำหนดราคา และข้อจำกัด
- [การสร้าง Managed Agent](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th): ขยาย Antigravity ด้วยคำแนะนำ สกิล และข้อมูลของคุณเอง
- [สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): แหล่งที่มา เครือข่าย วงจรชีวิต ขีดจำกัดของทรัพยากร
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=th): API พื้นฐานสำหรับโมเดลและ Agent

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-20 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-20 UTC"],[],[]]
