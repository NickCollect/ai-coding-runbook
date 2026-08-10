---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=th
fetched_at: 2026-08-10T03:24:34.050138+00:00
title: "\u0e2b\u0e38\u0e48\u0e19\u0e22\u0e19\u0e15\u0e4c\u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e2a\u0e15\u0e23\u0e35\u0e21 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# หุ่นยนต์ที่มีการสตรีม

ปลายทางของโมเดล `gemini-robotics-er-2-streaming-preview` จะแสดงปลายทางการสตรีมมิงเฉพาะ
ที่ผสานรวมกับ [Live
API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th) ซึ่งช่วยให้แอปพลิเคชันและหุ่นยนต์โต้ตอบกันแบบสองทางได้แบบเรียลไทม์
จึงเหมาะสำหรับเอเจนต์ที่ต้องการวงจรความคิดเห็นที่รวดเร็วและการตอบสนองต่อสภาพแวดล้อมแบบโต้ตอบ

[ลองใช้ใน Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=th)
[โคลนแอปตัวอย่างจาก GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## กรณีการใช้งาน

- **การประสานงานของหุ่นยนต์หลายตัว**: หุ่นยนต์หลายตัวที่สื่อสารสถานะของงาน
  และมอบหมายงานย่อยผ่านเซสชันที่แชร์
- **การตรวจสอบอย่างต่อเนื่อง**: หุ่นยนต์ที่สังเกตฉากและทริกเกอร์การดำเนินการ
  เมื่อเกิดเหตุการณ์ที่เฉพาะเจาะจง เช่น คอนเทนเนอร์มีระดับการเติมถึงระดับหนึ่ง
- **คลังสินค้าและโลจิสติกส์**: เอเจนต์หยิบและแพ็กที่ยืนยันรายการ
  ด้วยสายตา ติดตามความคืบหน้าในการแพ็ก และกู้คืนจากข้อผิดพลาด

## ข้อกำหนดทางเทคนิค

ตารางต่อไปนี้สรุปข้อกำหนดทางเทคนิคของ Live API

| หมวดหมู่ | รายละเอียด |
| --- | --- |
| รูปแบบอินพุต | เสียง (เสียง PCM แบบดิบ 16 บิต, 16kHz, little-endian), รูปภาพ (JPEG <= 1FPS), ข้อความ |
| รูปแบบเอาต์พุต | ข้อความ |
| โปรโตคอล | การเชื่อมต่อ WebSocket แบบมีสถานะ (WSS) |

## สร้างการตั้งค่าแบบเอเจนต์

เอเจนต์ระบบหุ่นยนต์ทุกตัวที่สร้างขึ้นใน Live API จะทำตาม 3 ขั้นตอนต่อไปนี้

1. **ประกาศความสามารถของหุ่นยนต์เป็นเครื่องมือ** การดำเนินการแต่ละอย่างที่หุ่นยนต์ทำได้ เช่น การนำทาง การจับ การพูด จะกลายเป็นการประกาศฟังก์ชันที่มีชื่อ คำอธิบาย และสคีมาพารามิเตอร์ การดำเนินการทางกายภาพต้องใช้
   `"behavior": "BLOCKING"` เพื่อให้โมเดลรอให้หุ่นยนต์ดำเนินการเสร็จสิ้นก่อนที่จะ
   เลือกขั้นตอนถัดไป
2. **สตรีมอินพุตหลายรูปแบบลงในเซสชันแบบถาวร** เปิดเซสชัน `live.connect` และเปิดไว้ตลอดระยะเวลาของงาน ส่งเฟรมวิดีโอ เสียง หรือข้อความเมื่อเซ็นเซอร์ของหุ่นยนต์ส่งมา
3. **จัดการการเรียกเครื่องมือในลูปการรับ** ทุกครั้งที่โมเดลเลือกการดำเนินการ โมเดลจะส่งข้อความ `tool_call` ลูปการรับจะเรียกใช้ฟังก์ชันกับ SDK ของหุ่นยนต์และส่ง `tool_response` กลับ เซสชันจะเปิดอยู่ และโมเดลจะเลือกการดำเนินการถัดไปตามผลลัพธ์

ส่วนต่อไปนี้จะแสดงวิธีใช้ขั้นตอนเหล่านี้กับ 3 รูปแบบทั่วไป ได้แก่ ลูปเอเจนต์พื้นฐาน การตรวจสอบฉากเชิงรุกด้วยสัญญาณชีพจร และการกำหนดเส้นทางคำพูดผ่าน TTS เป็นเครื่องมือ

## ประสานงานหุ่นยนต์ผ่านการเรียกฟังก์ชัน

ตัวอย่างต่อไปนี้แสดงขั้นตอนทั้ง 3 ขั้นตอนที่เชื่อมโยงกันในสคริปต์ Python เดียว

ขั้นตอนที่ 1 - คำจำกัดความของเครื่องมือ - ประกาศความสามารถของหุ่นยนต์เป็นการประกาศฟังก์ชัน ฟังก์ชัน `navigate` ใช้ `"behavior": "BLOCKING"` เพื่อให้
โมเดลรอให้หุ่นยนต์ไปถึงจุดอ้างอิงก่อนที่จะเรียกเครื่องมืออื่น
เพิ่มการประกาศฟังก์ชันเพิ่มเติมในรายการเดียวกันเพื่อแสดงความสามารถเพิ่มเติมของหุ่นยนต์

ขั้นตอนที่ 2 - ตัวช่วยอินพุต - แสดงฟังก์ชัน 3 ฟังก์ชันที่สตรีมอินพุตรูปแบบต่างๆ ลงในเซสชัน ได้แก่ `send_text` สำหรับคำสั่ง, `send_image` สำหรับเฟรมกล้องที่มีพรอมต์ข้อความที่ไม่บังคับ และ `send_audio` สำหรับเสียง PCM แบบดิบจากไมโครโฟน

ขั้นตอนที่ 3 - ลูปการรับ - ทำงานพร้อมกันและจัดการข้อความ 2 ประเภท ได้แก่ ข้อความ `server_content` (เอาต์พุตข้อความของโมเดล) และข้อความ `tool_call` (โมเดลขอการดำเนินการของหุ่นยนต์) เมื่อมีการเรียกใช้เครื่องมือ ลูปจะเรียก `execute_tool` ซึ่งเป็น Stub ที่คุณแทนที่ด้วย SDK ของหุ่นยนต์จริง จากนั้นส่ง `tool_response` กลับเพื่อให้โมเดลเลือกการดำเนินการถัดไปได้

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

ลูปการรับจะยังคงทำงานอยู่หลังจากได้รับคำตอบจากเครื่องมือแต่ละรายการ โมเดลจะสร้างและแก้ไขแผนระยะยาวโดยที่คุณไม่ต้องเข้ารหัสลำดับการดำเนินการทั้งหมดล่วงหน้า

## การให้เหตุผลเชิงรุกด้านพื้นที่และเวลา

Live API จะสตรีมวิดีโอ แต่เฟรมวิดีโอเพียงอย่างเดียวจะไม่ทริกเกอร์การให้เหตุผลใหม่ เฟรมวิดีโอต้องมาพร้อมกับพรอมต์ข้อความหรือเสียงเพื่อทริกเกอร์การตอบสนองของโมเดล ดูรายละเอียดเพิ่มเติมได้ที่
[ความสามารถของ Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th)สำหรับ

หากต้องการเปิดใช้การให้เหตุผลเชิงรุก ให้ใช้**สัญญาณชีพจร**: ส่ง
เฟรมกล้องล่าสุดเป็นระยะๆ ตามด้วยพรอมต์ข้อความสั้นๆ ที่บังคับให้โมเดล
ตรวจสอบฉากและตัดสินใจอย่างชัดเจน อินพุตวิดีโอจะจำกัดอัตราไว้ที่ 1 เฟรมต่อวินาที

เพิ่มโครูทีนนี้ข้างลูปการรับจากส่วนก่อนหน้า โดยจะทำงานเป็นงาน `asyncio` แยกต่างหากในเซสชันเดียวกัน

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

คุณไม่จำเป็นต้องหยุดสัญญาณชีพจรชั่วคราวระหว่างการดำเนินการของหุ่นยนต์ เมื่อใช้เป็น
**ตัวตรวจจับความสำเร็จโดยนัย** การเปิดใช้งานสัญญาณชีพจรจะช่วยให้โมเดลสังเกตการดำเนินการที่กำลังดำเนินการอยู่ได้อย่างต่อเนื่อง (ติดตามว่าการจับยึดปลอดภัยหรือไม่ การเท
ตรงเป้าหมายหรือไม่ หรือวัตถุกำลังเข้าที่อย่างถูกต้องหรือไม่) และตอบสนองทันทีที่
ผลลัพธ์ชัดเจน

ข้อความสัญญาณชีพจรจะทำหน้าที่เป็นการโต้ตอบของผู้ใช้และขัดจังหวะการสร้างโมเดลที่กำลังดำเนินการอยู่
ดู
[คู่มือ Live API เกี่ยวกับการขัดจังหวะ](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=th#interruptions)
เพื่อทำความเข้าใจวิธีที่ Live API จัดการลักษณะการทำงานนี้

## เอาต์พุตเสียงผ่าน TTS ภายนอก

Gemini Robotics ER 2 จะแสดงผลข้อความ แอปพลิเคชันของคุณจะกำหนดเส้นทางคำตอบที่เสร็จสมบูรณ์
ไปยังผู้ให้บริการ TTS แยกต่างหาก (เช่น
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=th)) ผ่านการเรียกกลับที่แทรก
ซึ่งจะช่วยให้คุณควบคุมเวลาในการตอบสนองของคำพูด การเลือกเสียง และลักษณะการทำงานของการขัดจังหวะได้ และช่วยให้คุณสลับแบ็กเอนด์ TTS ได้โดยไม่ต้องเปลี่ยนตรรกะของเอเจนต์

นอกจากนี้ คุณยังประกาศ TTS เป็นเครื่องมือได้เพื่อให้โมเดลถือว่า "พูดอะไรบางอย่าง" เหมือนกับ "ขยับแขน" เพิ่มการประกาศฟังก์ชันต่อไปนี้ลงในรายการ `tools` จากส่วนแรก

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

การห่อหุ้ม TTS ในการประกาศฟังก์ชันจะช่วยให้โมเดลจัดการคำพูดผ่านเส้นทางการเรียกเครื่องมือเดียวกันกับการดำเนินการอื่นๆ ของหุ่นยนต์ แอปพลิเคชันของคุณจะดำเนินการตามการเรียกด้วยการเรียกกลับที่แทรก

## ตัวอย่างใน GitHub

ดูตัวอย่างการทำงานทั้งหมด รวมถึงการสาธิตการหยิบขนมของหุ่นยนต์ Spot และ Tinybot
pan-tilt hello world ได้ที่
[ตัวอย่าง Robotics Live API](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## ขั้นตอนถัดไป

- [การทำความเข้าใจวิดีโอ](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=th) - การค้นหาช่วงเวลาและการจัดประเภทความคืบหน้า
- [การประสานงานงาน](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=th) - งานระยะยาวโดยไม่มีการสตรีมมิง
- [ภาพรวมของ Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=th) - เอกสารประกอบทั้งหมดของ Live API

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-07-31 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-07-31 UTC"],[],[]]
