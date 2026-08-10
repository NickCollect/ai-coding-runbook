---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=th
fetched_at: 2026-08-10T03:13:08.054744+00:00
title: "\u0e2e\u0e38\u0e01 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ฮุก

Hooks ช่วยให้คุณเรียกใช้สคริปต์ที่กำหนดเองหรือคำขอ HTTP ภายนอกได้ก่อนหรือหลังที่ Agent จะเรียกใช้โค้ดหรือแก้ไขไฟล์ภายใน Sandbox ระยะไกล ใช้ Hooks เพื่อขยายลูปของ Agent ด้วยการป้องกันอัตโนมัติและเวิร์กโฟลว์เบื้องหลัง เช่น

- **บังคับใช้การป้องกันด้านความปลอดภัยและการเข้าถึง** ก่อนที่จะมีการเรียกใช้คำสั่ง Shell ที่มีความเสี่ยงสูงหรือการอ่านไฟล์ที่จำกัด
- **เปลี่ยนรูปแบบไปป์ไลน์ข้อมูลโดยอัตโนมัติ** ทันทีหลังจากที่ Agent สร้างหรือแก้ไขไฟล์
- **สตรีมการวัดและส่งข้อมูลทางไกลสำหรับการตรวจสอบขององค์กร** ไปยังระบบการตรวจสอบภายนอกหลังจากที่เครื่องมือทำงานเสร็จ

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
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

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## เหตุการณ์ในวงจรที่รองรับ

Hooks รองรับ 2 เหตุการณ์ภายใน Sandbox ดังนี้

| เหตุการณ์ | เวลาที่ทริกเกอร์ | การทำงาน |
| --- | --- | --- |
| `pre_tool_execution` | ก่อนที่เครื่องมือจะทำงาน | สามารถอนุมัติ (`allow`) หรือบล็อก (`deny`) เครื่องมือก่อนที่จะมีการเรียกใช้ เมื่อถูกบล็อก โมเดลจะเห็นเหตุผลการปฏิเสธและปรับเปลี่ยน |
| `post_tool_execution` | หลังจากที่เครื่องมือทำงานเสร็จ | เรียกใช้ฟังก์ชันติดตามผล เช่น การจัดรูปแบบโค้ด การเรียกใช้การทดสอบหน่วย หรือการบันทึกการวัดและส่งข้อมูลทางไกล ไม่สามารถบล็อกหรือเลิกทำการดำเนินการที่เสร็จสมบูรณ์แล้ว |

### `pre_tool_execution`

ทริกเกอร์ก่อนที่เครื่องมือจะทำงาน สคริปต์จะอ่านรายละเอียดการเรียกใช้เครื่องมือจาก `stdin` และส่งออก JSON การตัดสินใจ (`allow` หรือ `deny`) ไปยัง `stdout`

**เพย์โหลดอินพุต (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**การตอบกลับเอาต์พุต (`stdout`):**

หากต้องการอนุมัติการเรียกใช้เครื่องมือ ให้ทำดังนี้

```
{
  "decision": "allow"
}
```

หากต้องการบล็อกการเรียกใช้เครื่องมือและส่งความคิดเห็นกลับไปยังโมเดล ให้ทำดังนี้

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

เมื่อ Hook ปฏิเสธคำสั่ง ระบบจะข้ามการเรียกใช้เครื่องมือทันที Agent จะเห็นผลลัพธ์ข้อผิดพลาดที่มีเหตุผลการปฏิเสธของคุณภายในเทิร์นปัจจุบัน จากนั้นโมเดลจะแก้ไขตัวเองได้โดยเลือกคำสั่งอื่นหรืออธิบายการบล็อกให้ผู้ใช้ทราบ

หากสคริปต์ส่งออก JSON, ข้อความธรรมดา หรือสิ่งอื่นที่ไม่รู้จักนอกเหนือจาก `{"decision": "deny"}` รันไทม์จะถือว่าการตอบกลับเป็นการอนุมัติ (`allow`)

### `post_tool_execution`

ทริกเกอร์หลังจากที่เครื่องมือทำงานเสร็จ สคริปต์จะอ่านรายละเอียดการดำเนินการและสถานะข้อผิดพลาดจาก `stdin`

**เพย์โหลดอินพุต (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

หากคำสั่ง Shell พิมพ์ข้อผิดพลาดไปยังข้อผิดพลาดมาตรฐาน (`stderr`) หรือการดำเนินการระบบไฟล์ล้มเหลว ระบบจะรวมฟิลด์ `"error"` ที่มีข้อความแสดงข้อผิดพลาดไว้ในเพย์โหลด เมื่อคำสั่งสำเร็จโดยไม่มีข้อผิดพลาด ระบบจะละเว้นฟิลด์ `"error"` ทั้งหมด

**การตอบกลับเอาต์พุต (`stdout`):**

```
{}
```

เนื่องจาก Hooks หลังการทำงานของเครื่องมือจะทำงานสำหรับฟังก์ชันเบื้องหลังอย่างเคร่งครัด เช่น การจัดรูปแบบโค้ดหรือการบันทึก รันไทม์จึงละเว้นค่าการตัดสินใจที่ส่งคืนใน `stdout`

## การค้นหาการกำหนดค่า

รันไทม์จะค้นหาคำจำกัดความของ Hooks จาก `.agents/hooks.json` หรือ `/.agents/hooks.json` ภายในสภาพแวดล้อม Sandbox โดยอัตโนมัติ คุณสามารถระบุ `hooks.json` ควบคู่ไปกับสคริปต์ที่กำหนดเองได้โดยใช้แหล่งที่มาของ [สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#mount_from_a_source) ที่รองรับ ดังนี้

- **การติดตั้งที่เก็บ**: ที่เก็บ Git ที่มี `.agents/hooks.json` ควบคู่ไปกับ `AGENTS.md`
- **Cloud Storage (`gcs`)**: บัคเก็ต GCS ที่มี `hooks.json` ซึ่งคัดลอกลงในสภาพแวดล้อม
- **แหล่งที่มาแบบอินไลน์**: สตริง JSON ดิบและเนื้อหาสคริปต์ที่ส่งใน `environment.sources` เมื่อเรียกใช้ `client.interactions.create`

### สคีมา `hooks.json`

ไฟล์ `hooks.json` จะจัดกลุ่มคำจำกัดความของเหตุการณ์ (`pre_tool_execution` หรือ `post_tool_execution`) ภายใต้ชื่อที่กำหนดเอง คุณสามารถเปิดหรือปิดใช้แต่ละกลุ่มแยกกันได้

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### ไวยากรณ์และกฎของ Matcher

แต่ละกลุ่มกฎใน `hooks.json` จะกำหนดเวลาและวิธีที่ตัวจัดการทริกเกอร์โดยใช้พร็อพเพอร์ตี้ `matcher` และ `hooks`

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `enabled` | `boolean` | ไม่บังคับ ตั้งค่าเป็น `false` เพื่อปิดใช้กลุ่ม (`true` โดยค่าเริ่มต้น) |
| `matcher` | `string` | รูปแบบนิพจน์ทั่วไปที่ตรงกับชื่อเครื่องมือเป้าหมายภายในคอนเทนเนอร์ |
| `hooks` | `array` | รายการคำจำกัดความของตัวจัดการ (`command` หรือ `http`) ที่เรียงลำดับ ตัวจัดการจะทำงานตามลำดับการประกาศ |

#### วิธีการทำงานของการประเมินนิพจน์ทั่วไป

เมื่อ Agent เรียกใช้เครื่องมือภายใน Sandbox รันไทม์จะประเมินชื่อคอนเทนเนอร์ของเครื่องมือกับรูปแบบ `matcher` โดยใช้นิพจน์ทั่วไป RE2 มาตรฐาน หากนิพจน์ทั่วไปตรงกับชื่อเครื่องมือ ตัวจัดการทั้งหมดในอาร์เรย์ `hooks` จะทำงานตามลำดับ หากกลุ่มกฎหลายกลุ่มตรงกับเครื่องมือเดียวกัน อาร์เรย์ตัวจัดการที่เกี่ยวข้องทั้งหมดจะทำงาน

คุณสามารถกำหนดเป้าหมายชื่อเครื่องมือคอนเทนเนอร์ในตัวได้ทุกชื่อ ได้แก่ การเรียกใช้โค้ด (`code_execution`) หรือการดำเนินการระบบไฟล์ (`read_file`, `write_file`, `list_files` และ `delete_file`)

#### นิพจน์ Matcher ที่พบบ่อย

- `"code_execution"`: การจับคู่สตริงที่แน่นอนสำหรับคำสั่ง Shell และการเรียกใช้สคริปต์
- `"write_file"`: การจับคู่ที่แน่นอนสำหรับการสร้างไฟล์ระบบไฟล์และการเขียนดิสก์
- `"read_file|write_file"`: การคั่นด้วยไปป์จะจับคู่ชื่อเครื่องมือที่เฉพาะเจาะจงหลายชื่อในกฎเดียว
- `".*_file"`: การจับคู่ไวลด์การ์ดของนิพจน์ทั่วไปกับเครื่องมือใดก็ตามที่ลงท้ายด้วย `_file` (เช่น `read_file`, `write_file` หรือ `delete_file`) นิพจน์ทั่วไป RE2 มาตรฐานต้องใช้ `.*` ส่วน Globs Shell อย่างง่าย เช่น `*_file` เป็นไวยากรณ์นิพจน์ทั่วไปที่ไม่ถูกต้องและจะจับคู่ไม่สำเร็จ
- `".*"` หรือ `"*"` หรือ `""`: รูปแบบการจับทั้งหมดที่สกัดกั้นการเรียกใช้เครื่องมือทุกรายการภายในคอนเทนเนอร์

## ประเภทตัวแฮนเดิล

### Hooks คำสั่ง

Hooks คำสั่งจะเรียกใช้คำสั่ง Shell หรือสคริปต์ภายใน Sandbox สคริปต์จะได้รับ JSON เหตุการณ์ใน `stdin` และส่งออก JSON การตัดสินใจใน `stdout`

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `type` | `string` | ต้องเป็น `"command"` |
| `command` | `string` | บรรทัดคำสั่งที่จะเรียกใช้ภายใน Sandbox (เช่น `python3 /.agents/hooks-scripts/gate.py`) |
| `timeout` | `integer` | การหมดเวลาเป็นวินาที ค่าเริ่มต้น: `30` |

### Hooks HTTP

Hooks HTTP จะส่ง JSON เหตุการณ์เป็นคำขอ POST ไปยัง URL HTTPS ภายนอกโดยตรงจากภายในเครือข่าย Sandbox เซิร์ฟเวอร์เป้าหมายจะส่งคืนการตัดสินใจในเนื้อหาการตอบกลับ HTTP โดยใช้รูปแบบ JSON เดียวกัน (`{"decision": "allow"}` หรือ `{"decision": "deny", "reason": "..."}`)

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `type` | `string` | ต้องเป็น `"http"` |
| `url` | `string` | ปลายทาง HTTPS ภายนอกที่จะ POST เพย์โหลดเหตุการณ์ |
| `headers` | `object` | คู่คีย์-ค่าที่ไม่บังคับสำหรับส่วนหัวที่กำหนดเองที่ไม่ละเอียดอ่อน (เช่น `{"X-Event-Source": "agent-sandbox"}`) สำหรับข้อมูลเข้าสู่ระบบการตรวจสอบสิทธิ์ ให้ใช้พร็อกซีเครือข่ายแทน |
| `timeout` | `integer` | การหมดเวลาเป็นวินาที ค่าเริ่มต้น: `30` |

#### พร็อกซีขาออกและการเปลี่ยนรูปแบบโทเค็น

เนื่องจาก Hooks HTTP จะทำงานโดยตรงจากเนมสเปซเครือข่าย Sandbox คำขอขาออกจึงผ่านพร็อกซีขาออกแบบโปร่งใส สถาปัตยกรรมนี้ให้ข้อได้เปรียบด้านความปลอดภัยที่สำคัญ 2 ประการ ดังนี้

- **การอนุญาตเครือข่าย:** ต้องได้รับอนุญาตปลายทางเป้าหมายอย่างชัดเจนใน `network.allowlist` ของสภาพแวดล้อม พร็อกซีจะบล็อกการรับส่งข้อมูลแบบวนซ้ำ (`127.0.0.1` หรือ `localhost`) ให้กำหนดเป้าหมายปลายทางภายนอกที่ได้รับอนุญาตเสมอ
- **การเปลี่ยนรูปแบบโทเค็น:** คุณไม่จำเป็นต้องจัดเก็บคีย์ API หรือโทเค็นผู้รับมอบสิทธิ์ที่เป็นความลับไว้ใน `.agents/hooks.json` หรือติดตั้งลงในคอนเทนเนอร์ แต่ให้กำหนดค่ากฎการเปลี่ยนรูปแบบโทเค็นในการกำหนดค่า[เครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration) (`network.allowlist.transform`) พร็อกซีขาออกจะสกัดกั้นการรับส่งข้อมูล Hooks HTTP ขาออกโดยอัตโนมัติและแทรกส่วนหัวการตรวจสอบสิทธิ์จริงลงในสายก่อนที่จะออกจาก Sandbox

## วิธีที่รันไทม์จัดการการตัดสินใจและความล้มเหลว

- **การรอแบบซิงโครนัส:** Agent จะหยุดชั่วคราวและรอให้ Hooks ทำงานเสร็จก่อนที่จะดำเนินการต่อ
- **การบล็อกการทำงานของเครื่องมือ:** หาก Hook ก่อนการทำงานของเครื่องมือส่งคืน `{"decision": "deny", "reason": "<your reason>"}` รันไทม์จะยกเลิกการเรียกใช้เครื่องมือทันที โมเดลจะเห็นเหตุผลการปฏิเสธในประวัติการสนทนาและปรับเปลี่ยนโดยเลือกตัวเลือกที่ปลอดภัยหรืออธิบายการบล็อกให้ผู้ใช้ทราบ
- **การจัดการการหยุดทำงานของสคริปต์ ข้อผิดพลาด HTTP และการหมดเวลา:** หากสคริปต์คำสั่งหยุดทำงาน (สถานะการออกที่ไม่เป็น 0) Hook HTTP ส่งคืนรหัสสถานะที่ไม่ใช่ 2xx (เช่น ข้อผิดพลาดเกี่ยวกับเซิร์ฟเวอร์ 4xx หรือ 5xx) หรือการดำเนินการหมดเวลาหรือส่งคืน JSON ที่ไม่รู้จัก รันไทม์จะถือว่าเป็นการอนุมัติ (`allow`) การทำงานของเครื่องมือจะดำเนินต่อไปตามปกติ สคริปต์ที่เสียหายหรือเซิร์ฟเวอร์การวัดและส่งข้อมูลทางไกลที่เข้าถึงไม่ได้จึงไม่ทำให้แอปพลิเคชันหยุดทำงาน

## กรณีการใช้งานทั่วไป

### การกู้คืนหลายเทิร์นเพื่อความเป็นส่วนตัวของข้อมูลและการปฏิบัติตามข้อกำหนด

เมื่อ Hook บล็อกการเข้าถึงทรัพยากรที่จำกัด เช่น ไดเรกทอรีที่มีข้อมูลส่วนบุคคลที่ระบุตัวบุคคลนั้นได้ (PII) หรือบันทึกทางการเงินที่เป็นความลับ คุณสามารถส่ง `previous_interaction_id` ในการเรียกใช้ครั้งถัดไปเพื่อดำเนินการต่อในสภาพแวดล้อมเดิม Agent จะอ่านคำอธิบายการปฏิเสธและกู้คืนโดยอัตโนมัติด้วยการค้นหาตารางสาธารณะที่ได้รับอนุมัติแทน

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "read_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### การวัดและส่งข้อมูลทางไกลและการบันทึกการตรวจสอบภายนอก

ส่งเหตุการณ์การตรวจสอบแบบเรียลไทม์จากภายใน Sandbox ไปยังเซิร์ฟเวอร์การตรวจสอบภายนอกทุกครั้งที่มีการอ่านหรือแก้ไขไฟล์

- **จับคู่เครื่องมือหลายรายการ:** เนื่องจาก Matcher ใช้นิพจน์ทั่วไปมาตรฐาน คุณจึงรวมเครื่องมือหลายรายการไว้ในกฎเดียวได้โดยใช้ไปป์ (`read_file|write_file`) หรือไวลด์การ์ด (`.*_file`)
- **เก็บข้อมูลลับไว้ในการกำหนดค่า:** กำหนดโทเค็นการตรวจสอบสิทธิ์ในการกำหนดค่า[เครือข่าย](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th#network-configuration)ของสภาพแวดล้อม (`network.allowlist.transform`) พร็อกซีขาออกจะแทรกโทเค็นผู้รับมอบสิทธิ์จริงลงในคำขอขาออกโดยอัตโนมัติ

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "read_file|write_file",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "read_file|write_file",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## ข้อจำกัด

- **ขอบเขตเครื่องมือ Sandbox:** Hooks จะสกัดกั้นเครื่องมือในตัวภายใน Sandbox ได้แก่ การเรียกใช้โค้ด (`code_execution`) และการดำเนินการระบบไฟล์ (`read_file`, `write_file`, `list_files` และ `delete_file`) โดยจะไม่ทริกเกอร์สำหรับการเรียกใช้ฟังก์ชันที่กำหนดเอง (`function`) หรือเครื่องมือ Model Context Protocol (`mcp_server`) ภายนอกที่จัดการนอกคอนเทนเนอร์
- **การอนุญาตเครือข่าย:** Hooks HTTP จะทำงานภายในเครือข่ายคอนเทนเนอร์ คุณต้องอนุญาต URL เป้าหมายอย่างชัดเจนใน `network.allowlist` ของสภาพแวดล้อม พร็อกซีจะบล็อกที่อยู่แบบวนซ้ำ (`localhost`, `127.0.0.1`)
- **การอนุมัติอัตโนมัติเมื่อเกิดข้อผิดพลาด:** หากสคริปต์ Hook หยุดทำงาน (สถานะการออกที่ไม่เป็น 0) หมดเวลา หรือล้มเหลว รันไทม์จะบันทึกความล้มเหลวและอนุญาตให้การเรียกใช้เครื่องมือดำเนินต่อไป ซึ่งจะช่วยให้สคริปต์ Linter ที่เสียหายหรือกระบวนการที่ค้างอยู่ไม่ทำให้แอปพลิเคชันหยุดทำงาน
- **การป้องกันการกำหนดค่า Sandbox:** เนื่องจาก Hooks ทำงานภายใน Sandbox คอนเทนเนอร์ Agent ที่มีเครื่องมือเขียนระบบไฟล์หรือสิทธิ์การเรียกใช้โค้ด Shell จึงสามารถแก้ไข `.agents/hooks.json` หรือสคริปต์ภายในพื้นที่ทำงานที่เขียนได้ ใช้ Hooks คอนเทนเนอร์เป็นคำแนะนำนโยบายอัตโนมัติและการป้องกันการทำงาน หากจำเป็นต้องมีการป้องกันการดัดแปลงอย่างเข้มงวดจากการเรียกใช้โมเดลที่ไม่น่าเชื่อถือ ให้ติดตั้งแหล่งที่มาของการกำหนดค่าจากที่เก็บแบบอ่านอย่างเดียว

## ขั้นตอนถัดไป

- ดูวิธีกำหนดค่า Sandbox และสภาพแวดล้อมระยะไกลแบบถาวร [remote sandboxes and environments](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th)
- สำรวจความสามารถและเครื่องมือในตัวของ [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th)
- ดูภาพรวมของ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) สำหรับเซสชันการสนทนาไปมาและการสตรีม

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-30 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-30 UTC"],[],[]]
