---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=th
fetched_at: 2026-11-02T07:22:43.833988+00:00
title: "\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32\u0e15\u0e31\u0e27\u0e41\u0e17\u0e19\u0e01\u0e32\u0e23\u0e40\u0e02\u0e35\u0e22\u0e19\u0e42\u0e04\u0e49\u0e14\u0e41\u0e25\u0e30\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e19\u0e31\u0e01\u0e1e\u0e31\u0e12\u0e19\u0e32\u0e41\u0e2d\u0e1b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การตั้งค่าตัวแทนการเขียนโค้ดและแหล่งข้อมูลสำหรับนักพัฒนาแอป

Agent การเขียนโค้ดด้วย AI อาศัยข้อมูลฝึกฝนที่สิ้นสุด ณ วันที่ที่กำหนด ด้วยเหตุนี้ ตัวแทนจึงมักแนะนำโมเดลที่เลิกใช้งานแล้ว (`gemini-1.5`), SDK รุ่นเก่า (`google-generativeai`) หรือรูปแบบโค้ดที่ล้าสมัย

การเชื่อมต่อ Agent กับแหล่งข้อมูลอย่างเป็นทางการสำหรับนักพัฒนา Gemini จะช่วยให้ Agent เขียนโค้ดที่ถูกต้องโดยใช้โมเดลปัจจุบัน, `google-genai` SDK และ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)

คุณสามารถเชื่อมต่อเอเจนต์การเขียนโค้ดกับเอกสารประกอบ, กฎ และเครื่องมือ CLI ของ Gemini ได้ 5 วิธีดังนี้

## สรุปแหล่งข้อมูลของ Agent

| ทรัพยากร | สิ่งที่รายงานแสดง | ความพร้อมใช้งาน |
| --- | --- | --- |
| **[ทักษะของ Gemini Agent](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#available-skills)** | กฎทีละขั้นตอน, รูปแบบ SDK และสคริปต์ตัวช่วยสำหรับฟีเจอร์ที่เฉพาะเจาะจง (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) | ติดตั้งไว้ล่วงหน้าใน [AI Studio Build](https://ai.studio/build) โดยติดตั้งด้วย `skills.sh`, Context7 หรือ Managed Agents |
| **[เซิร์ฟเวอร์ MCP ของ Gemini Docs](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#mcp-setup)** | Live Search (`gemini_search_docs`) และการอ่านทั้งหน้า (`gemini_get_doc`) ในเอกสารประกอบทั้งหมด | รองรับใน Claude Code, Cursor, OpenAI Codex และ VS Code |
| **[ปลั๊กอิน Gemini API](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#gemini-api-plugin)** | แพ็กเกจรวมที่มีทักษะ Gemini อย่างเป็นทางการ, เซิร์ฟเวอร์ MCP ของเอกสาร และเครื่องมือคีย์ API | Antigravity |
| **[เอกสารที่เครื่องอ่านได้](https://ai.google.dev/gemini-api/docs/coding-agents?hl=th#machine-readable-docs)** | ล้างหน้า Markdown และดัชนี `llms.txt` | หน้าเอกสารประกอบทั้งหมดใน `ai.google.dev/gemini-api/docs` |
| **[Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=th)** | CLI แบบไม่เก็บสถานะ (`gemini-api`) เพื่อสร้าง GenMedia วิเคราะห์ไฟล์ และเรียกใช้ Agent ที่ได้รับการจัดการจาก Shell โดยไม่ต้องเขียนโค้ด SDK | ติดตั้งใน macOS, Linux หรือ Windows ด้วยสคริปต์การติดตั้ง, Go หรือไบนารีที่สร้างไว้ล่วงหน้า |

## ติดตั้งทักษะของตัวแทน Gemini

ทักษะของ Agent จะให้กฎขั้นตอน ชื่อโมเดลปัจจุบัน และรูปแบบโค้ด SDK แก่ Agent การเขียนโค้ด แทนที่จะเพิ่มคำสั่งยาวๆ ลงในพรอมต์ Agent จะโหลดทักษะแต่ละอย่างเมื่อจำเป็นเท่านั้น ซึ่งจะช่วยให้ Agent หลีกเลี่ยง SDK ที่เลิกใช้งานแล้วและใช้รูปแบบ Gemini ที่ทันสมัยได้

ทักษะจะทำงานร่วมกับเซิร์ฟเวอร์ MCP ของ Gemini เอกสาร หาก Agent ของคุณไม่ได้ติดตั้งเซิร์ฟเวอร์ MCP ไว้ ทักษะจะกลับไปใช้ [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=th) ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีการทำงานของทักษะได้ที่[คู่มือทักษะของ Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=th)

### ติดตั้งด้วย CLI (`skills.sh` หรือ Context7)

ติดตั้งทักษะโดยใช้ [skills.sh](https://skills.sh) (แนะนำ) หรือ
[Context7](https://context7.com):

```
# List all available skills in the repository
npx skills add google-gemini/gemini-skills --list

# Install a specific skill globally with skills.sh
npx skills add google-gemini/gemini-skills --skill <skill-name> --global

# Or install with Context7
npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
```

### ทักษะที่พร้อมใช้งาน

#### `gemini-api-dev`

ทักษะในการสร้างแอปพลิเคชันด้วย [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) และ SDK อย่างเป็นทางการของ Gemini API (`google-genai` สำหรับ Python และ `@google/genai` สำหรับ TypeScript) ทักษะนี้ครอบคลุมหัวข้อต่อไปนี้

- การสร้างข้อความ, แชทแบบหลายรอบ, การสตรีม, เอาต์พุตที่มีโครงสร้าง และการเรียกใช้ฟังก์ชัน
- การสร้างรูปภาพ การอ่านออกเสียงข้อความ (TTS) และอินพุตหลายรูปแบบ
- การจัดการสถานะการสนทนาฝั่งเซิร์ฟเวอร์, การดำเนินการในเบื้องหลัง, Deep Research และ Agent ที่มีการจัดการ
- ชื่อโมเดลปัจจุบันและการย้ายข้อมูลโค้ด `generateContent` หรือ `google-generativeai` เดิม

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### `gemini-live-api-dev`

ทักษะในการสร้างแอปพลิเคชันสตรีมมิงเสียงและวิดีโอแบบเรียลไทม์ด้วย [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=th) ทักษะนี้ครอบคลุมหัวข้อต่อไปนี้

- การจัดการเซสชัน WebSocket, โทเค็นไคลเอ็นต์แบบชั่วคราว และการกลับมาทำงานของเซสชัน
- การสตรีมเสียง วิดีโอ และข้อความพร้อมการตรวจจับกิจกรรมเสียงพูด (VAD) และการรองรับการขัดจังหวะ
- การให้เหตุผลในเบื้องหลัง (การคิดที่นานขึ้น) การเรียกใช้เครื่องมือแบบอะซิงโครนัสที่ไม่บล็อก การถอดเสียงเป็นคำ และการแปลเสียงพูดแบบเรียลไทม์

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### `gemini-omni-flash-api`

ทักษะในการสร้างและแก้ไขวิดีโอด้วย Gemini Omni Flash โดยใช้ Interactions API รวมสคริปต์ตัวช่วย (`upload_file.py`, `generate_video.py`, `prep_video.py`, `inspect_video.py`) และครอบคลุมสิ่งต่อไปนี้

- การสร้างวิดีโอจากข้อความและการเขียนพรอมต์
- การเปลี่ยนเฟรมแรกและเฟรมสุดท้ายและการสร้างวิดีโอตามข้อมูลอ้างอิง
- เวิร์กโฟลว์การประมวลผลล่วงหน้าของส่วนขยายวิดีโอและสื่อ

```
npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
```

### ติดตั้งทักษะใน Agent ที่มีการจัดการ

เมื่อเรียกใช้ Agent ที่มีการจัดการระยะไกลด้วย Interactions API คุณจะต่อเชื่อมที่เก็บ `google-gemini/gemini-skills` เข้ากับพื้นที่ทำงานของ Agent ได้ ดูรายละเอียดได้ที่[คู่มือทักษะ Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=th)

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build a script that generates a 5-second video of a neon cityscape.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/google-gemini/gemini-skills",
                "target": ".agents",
            }
        ],
    },
)
```

## เชื่อมต่อเซิร์ฟเวอร์ MCP ของ Gemini Docs

**เซิร์ฟเวอร์ MCP ของเอกสาร Gemini** สาธารณะ (`https://gemini-api-docs-mcp.dev`) ช่วยให้ Agent ของคุณเข้าถึงเว็บไซต์เอกสารทั้งหมดได้แบบเรียลไทม์ Agent ของคุณสามารถค้นหาและอ่านหน้าเอกสารประกอบเพื่อตรวจสอบสคีมาคำขอ ขีดจำกัดของโมเดล และฟีเจอร์ใหม่ๆ ได้ดังนี้

- `gemini_search_docs`: ค้นหาเอกสารประกอบของ Gemini API ตามหัวข้อหรือคำค้นหา
- `gemini_get_doc`: อ่านเนื้อหา Markdown ทั้งหมดของหน้าเอกสารที่เฉพาะเจาะจง

### การตั้งค่าอย่างรวดเร็ว

เรียกใช้คำสั่งนี้ในเทอร์มินัลหรือรูทของโปรเจ็กต์เพื่อกำหนดค่า Agent การเขียนโค้ดที่ตรวจพบโดยอัตโนมัติ

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

### การกำหนดค่าตามสภาพแวดล้อม

### Claude Code

เรียกใช้ในเทอร์มินัลของคุณ:

```
$ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
```

### เคอร์เซอร์

เพิ่มลงใน `~/.cursor/mcp.json` (ส่วนกลาง) หรือ `.cursor/mcp.json` (โปรเจ็กต์):

```
{
  "mcpServers": {
    "geminiDocs": {
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

### OpenAI Codex

เรียกใช้ในเทอร์มินัลของคุณ:

```
$ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
```

หรือเพิ่มลงใน `~/.codex/config.toml`:

```
[mcp_servers.geminiDocs]
url = "https://gemini-api-docs-mcp.dev"
```

### VS Code (Copilot)

เพิ่มไปยัง `.vscode/mcp.json` ในพื้นที่ทำงานของคุณ:

```
{
  "servers": {
    "geminiDocs": {
      "type": "http",
      "url": "https://gemini-api-docs-mcp.dev"
    }
  }
}
```

## ปลั๊กอิน Gemini API

หากใช้ **Antigravity** **ปลั๊กอิน Gemini API** เป็นวิธีที่เร็วที่สุดในการตั้งค่าพื้นที่ทำงาน โดยจะรวมเซิร์ฟเวอร์ MCP ของ Gemini เอกสาร, ทักษะ Gemini อย่างเป็นทางการทั้งหมด (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`) และเครื่องมือคีย์ API ไว้ในการดาวน์โหลดเดียว

- **ติดตั้งใน Antigravity (UI):** ไปที่**การตั้งค่า > การปรับแต่ง > สร้างด้วยปลั๊กอิน Google** แล้วดาวน์โหลด **Gemini API**
- **ติดตั้งด้วย CLI:**
  `bash
  agy plugin install https://github.com/google-gemini/gemini-skills`

## เอกสารประกอบที่เครื่องอ่านได้

หน้าเว็บมาตรฐานประกอบด้วยแท็ก HTML, แถบนำทาง และสคริปต์ที่ใช้พื้นที่หน้าต่างบริบท `ai.google.dev` มีปลายทางที่เครื่องอ่านได้เพื่อให้เอเจนต์และสคริปต์สามารถดึงข้อมูลมาร์กดาวน์ที่สะอาดได้โดยตรง ดังนี้

- **ดัชนี `llms.txt`**
  ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt?hl=th)):
  แสดงรายการหน้าเอกสารประกอบของ Gemini API ทั้งหมดพร้อมลิงก์ไปยังแต่ละหน้า
- **URL มาร์กดาวน์โดยตรง (`.md.txt`)**: เพิ่ม `.md.txt` ต่อท้าย URL เอกสารประกอบใน `ai.google.dev` (เช่น [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt?hl=th)) เพื่อรับแหล่งข้อมูลมาร์กดาวน์ที่สะอาดสำหรับพรอมต์ที่บันทึกไว้ กฎ `AGENTS.md` หรือสคริปต์อัตโนมัติ

## กฎโปรเจ็กต์ที่แนะนำ (`AGENTS.md`)

ไฟล์กฎของโปรเจ็กต์ (`AGENTS.md`, `.cursorrules` หรือ `CLAUDE.md`) จะกำหนดกฎพื้นฐานที่โหลดเมื่อเริ่มต้นเซสชันของ Agent ทุกเซสชัน เพิ่มหลักเกณฑ์เหล่านี้ลงในรูทของโปรเจ็กต์เพื่อให้เอเจนต์การเขียนโค้ดใช้โมเดลและ SDK ปัจจุบันโดยค่าเริ่มต้น

```
# Gemini API Guidelines

- Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
- Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
- Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
- Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
```

## ยืนยันและแก้ปัญหา

### ตรวจสอบการตั้งค่า

หากต้องการทดสอบการตั้งค่า ให้ถาม Agent การเขียนโค้ดดังนี้

```
Look up the request schema for the Gemini Interactions API in the documentation.
```

Agent ที่กำหนดค่าไว้จะใช้ `gemini_search_docs` ในเซิร์ฟเวอร์ MCP `geminiDocs` และเขียนโค้ดโดยใช้ `client.interactions.create` กับ SDK `google-genai` หรือ `@google/genai`

### คำสั่งสถานะ

| สภาพแวดล้อม | การยืนยัน MCP | การยืนยันความสามารถ |
| --- | --- | --- |
| **Claude Code** | เรียกใช้ `/mcp` | เรียกใช้ `/skills` |
| **เคอร์เซอร์** | เปิด**การตั้งค่า > ฟีเจอร์ > MCP** | เปิด**การตั้งค่า > กฎ** |
| **OpenAI Codex** | เรียกใช้ `codex mcp list` | ตรวจสอบ `.codex/skills/` หรือ `~/.codex/skills/` |
| **Antigravity** | เปิด**การปรับแต่ง > การเชื่อมต่อ** | เปิด**การปรับแต่ง > กฎ** หรือเรียกใช้ `/skills list` |
| **VS Code (Copilot)** | เปิด**ส่วนขยาย > MCP** หรือแผงเอาต์พุต | คลิก**เลือกเครื่องมือ**ในแชท Copilot |

### การแก้ปัญหา

- **ไม่พบทักษะหรือเซิร์ฟเวอร์ MCP:** รีสตาร์ทเครื่องมือแก้ไข (Cursor หรือ VS Code) หรือเซสชันเทอร์มินัล (Claude Code หรือ Codex) เอเจนต์ส่วนใหญ่จะโหลดเซิร์ฟเวอร์ MCP และทักษะเมื่อเริ่มต้นเท่านั้น
- **ความขัดแย้งของ Skill ส่วนกลาง:** หาก Agent ละเว้น Skill ที่ติดตั้งส่วนกลาง ให้ติดตั้ง Skill ในรูทโปรเจ็กต์โดยไม่มี `--global`:
  `bash
  npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
- **กฎที่ละเว้น:** ตรวจสอบว่าไฟล์ `AGENTS.md`, `.cursorrules` หรือ `CLAUDE.md` อยู่ในไดเรกทอรีรากของโปรเจ็กต์

## ขั้นตอนถัดไป

- [Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=th)
- [คู่มือทักษะ Gemini API](https://aistudio.google.com/learn/gemini-api-skills?hl=th)
- [ทักษะ Gemini API ใน GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th)
- [โมเดลที่พร้อมให้บริการ](https://ai.google.dev/gemini-api/docs/models?hl=th)
- [ไลบรารีและ SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-28 UTC"],[],[]]
