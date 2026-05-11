---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=th
fetched_at: 2026-05-11T05:09:44.804632+00:00
title: "Session management with Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# Session management with Live API

ใน Live API เซสชันหมายถึงการเชื่อมต่อแบบถาวร
ซึ่งมีการสตรีมอินพุตและเอาต์พุตอย่างต่อเนื่องผ่านการเชื่อมต่อเดียวกัน (อ่านเพิ่มเติมเกี่ยวกับ[วิธีการทำงาน](https://ai.google.dev/gemini-api/docs/live?hl=th))
การออกแบบเซสชันที่ไม่เหมือนใครนี้ช่วยให้เกิดเวลาในการตอบสนองที่ต่ำและรองรับฟีเจอร์ที่ไม่เหมือนใคร แต่
ก็อาจทำให้เกิดความท้าทายต่างๆ เช่น ขีดจำกัดเวลาของเซสชันและการสิ้นสุดก่อนเวลา
คู่มือนี้ครอบคลุมกลยุทธ์ในการแก้ปัญหาความท้าทายด้านการจัดการเซสชัน
ที่อาจเกิดขึ้นเมื่อใช้ Live API

## อายุของเซสชัน

หากไม่มีการบีบอัด เซสชันเสียงอย่างเดียวจะจำกัดไว้ที่ 15 นาที
และเซสชันเสียงและวิดีโอจะจำกัดไว้ที่ 2 นาที การเกินขีดจำกัดเหล่านี้จะทำให้เซสชันสิ้นสุดลง (และทำให้การเชื่อมต่อสิ้นสุดลงด้วย) แต่คุณสามารถใช้[การบีบอัดหน้าต่างบริบท](#context-window-compression)เพื่อขยายเซสชันได้โดยไม่จำกัดเวลา

อายุการใช้งานของการเชื่อมต่อก็ถูกจำกัดไว้ที่ประมาณ 10 นาทีเช่นกัน เมื่อการเชื่อมต่อสิ้นสุดลง เซสชันก็จะสิ้นสุดลงด้วย ในกรณีนี้ คุณสามารถ
กำหนดค่าเซสชันเดียวให้ทำงานอยู่ตลอดการเชื่อมต่อหลายครั้งได้โดยใช้
[การกลับมาใช้เซสชันต่อ](#session-resumption)
นอกจากนี้ คุณจะได้รับ[ข้อความ GoAway](#goaway-message) ก่อนที่การเชื่อมต่อจะสิ้นสุดลง ซึ่งจะช่วยให้คุณดำเนินการเพิ่มเติมได้

## การบีบอัดหน้าต่างบริบท

หากต้องการเปิดใช้เซสชันที่ยาวขึ้นและหลีกเลี่ยงการสิ้นสุดการเชื่อมต่ออย่างกะทันหัน คุณสามารถ
เปิดใช้การบีบอัดหน้าต่างบริบทได้โดยการตั้งค่าฟิลด์ [contextWindowCompression](https://ai.google.dev/api/live?hl=th#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
เป็นส่วนหนึ่งของการกำหนดค่าเซสชัน

ใน [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=th#contextwindowcompressionconfig) คุณสามารถกำหนดค่า
[กลไกหน้าต่างเลื่อน](https://ai.google.dev/api/live?hl=th#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
และ[จำนวนโทเค็น](https://ai.google.dev/api/live?hl=th#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
ที่ทริกเกอร์การบีบอัดได้

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## การกลับมาใช้เซสชันต่อ

หากต้องการป้องกันไม่ให้ระบบสิ้นสุดเซสชันเมื่อเซิร์ฟเวอร์รีเซ็ตการเชื่อมต่อ WebSocket เป็นระยะ
ให้กำหนดค่าฟิลด์ [sessionResumption](https://ai.google.dev/api/live?hl=th#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
ภายใน[การกำหนดค่าการตั้งค่า](https://ai.google.dev/api/live?hl=th#BidiGenerateContentSetup)

การส่งการกำหนดค่านี้จะทำให้เซิร์ฟเวอร์ส่งข้อความ [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=th#SessionResumptionUpdate)
ซึ่งใช้เพื่อกลับมาใช้เซสชันต่อได้โดยการส่งโทเค็นการกลับมาใช้ต่อล่าสุดเป็น [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=th#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)
ของการเชื่อมต่อครั้งถัดไป

โทเค็นการกลับมาทำงานต่อจะมีอายุ 2 ชั่วโมงหลังจากเซสชันสุดท้ายสิ้นสุดลง

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## การรับข้อความก่อนที่เซสชันจะตัดการเชื่อมต่อ

เซิร์ฟเวอร์จะส่งข้อความ [GoAway](https://ai.google.dev/api/live?hl=th#GoAway) ซึ่งส่งสัญญาณว่าการเชื่อมต่อปัจจุบันจะสิ้นสุดในเร็วๆ นี้ ข้อความนี้มี [timeLeft](https://ai.google.dev/api/live?hl=th#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left)
ซึ่งระบุเวลาที่เหลืออยู่และช่วยให้คุณดำเนินการเพิ่มเติมได้ก่อนที่ระบบจะสิ้นสุดการเชื่อมต่อเป็น ABORTED

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## รับข้อความเมื่อการสร้างเสร็จสมบูรณ์

เซิร์ฟเวอร์จะส่งข้อความ [generationComplete](https://ai.google.dev/api/live?hl=th#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
ซึ่งเป็นสัญญาณว่าโมเดลสร้างคำตอบเสร็จแล้ว

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## ขั้นตอนถัดไป

ดูวิธีอื่นๆ ในการทำงานกับ Live API ได้ในคู่มือ[ความสามารถ](https://ai.google.dev/gemini-api/docs/live?hl=th)ฉบับเต็ม
หน้า[การใช้เครื่องมือ](https://ai.google.dev/gemini-api/docs/live-tools?hl=th) หรือ
[ตำรา Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
