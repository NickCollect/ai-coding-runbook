---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar
fetched_at: 2026-06-01T06:06:33.175523+00:00
title: "\u0625\u062f\u0627\u0631\u0629 \u0627\u0644\u062c\u0644\u0633\u0627\u062a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إدارة الجلسات باستخدام Live API

في Live API، تشير الجلسة إلى اتصال مستمر يتم فيه بث الإدخال والإخراج بشكل مستمر عبر الاتصال نفسه (مزيد من المعلومات حول [طريقة عمله](https://ai.google.dev/gemini-api/docs/live?hl=ar)).
يتيح تصميم الجلسة الفريد هذا وقت استجابة منخفضًا ويدعم ميزات فريدة، ولكن يمكن أن يطرح أيضًا تحديات، مثل حدود وقت الجلسة والإنهاء المبكر.
يغطي هذا الدليل استراتيجيات للتغلّب على تحديات إدارة الجلسات التي يمكن أن تنشأ عند استخدام Live API.

## مدة الجلسة

بدون ضغط، تقتصر الجلسات الصوتية فقط على 15 دقيقة، وتقتصر الجلسات الصوتية والمرئية على دقيقتَين. سيؤدي تجاوز هذه الحدود
إلى إنهاء الجلسة (وبالتالي، الاتصال)، ولكن يمكنك استخدام
[ضغط قدرة استيعاب](#context-window-compression) لتمديد الجلسات إلى
مدة غير محدودة.

تقتصر مدة الاتصال أيضًا على 10 دقائق تقريبًا. عند انتهاء الاتصال، تنتهي الجلسة أيضًا. في هذه الحالة، يمكنك
ضبط جلسة واحدة لتظل نشطة على عدة اتصالات باستخدام
[استئناف الجلسة](#session-resumption).
ستتلقّى أيضًا رسالة [GoAway](#goaway-message) قبل انتهاء
الاتصال، ما يتيح لك اتّخاذ إجراءات إضافية.

## ضغط قدرة استيعاب السياق

لإتاحة جلسات أطول وتجنُّب إنهاء الاتصال المفاجئ، يمكنك تفعيل ضغط قدرة الاستيعاب من خلال ضبط الحقل [contextWindowCompression](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) كجزء من إعداد الجلسة.

في [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=ar#contextwindowcompressionconfig)، يمكنك ضبط آلية
[النافذة المنزلقة](https://ai.google.dev/api/live?hl=ar#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
و[عدد الرموز المميّزة](https://ai.google.dev/api/live?hl=ar#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
التي تؤدي إلى الضغط.

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

## استئناف الجلسة

لمنع إنهاء الجلسة عندما يعيد الخادم ضبط اتصال WebSocket
، اضبط الحقل [sessionResumption](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
ضمن [إعداد الإعداد](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentSetup).

يؤدي تمرير هذا الإعداد إلى إرسال الخادم رسائل [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=ar#SessionResumptionUpdate)، التي يمكن استخدامها لاستئناف الجلسة من خلال تمرير آخر رمز مميّز للاستئناف كـ [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=ar#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) للاتصال اللاحق.

تكون الرموز المميّزة للاستئناف صالحة لمدة ساعتَين بعد إنهاء الجلسات الأخيرة.

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

## تلقّي رسالة قبل قطع اتصال الجلسة

يرسل الخادم رسالة [GoAway](https://ai.google.dev/api/live?hl=ar#GoAway) تشير إلى أنّ الاتصال الحالي
سيتم إنهاؤه قريبًا. تتضمّن هذه الرسالة الحقل [timeLeft](https://ai.google.dev/api/live?hl=ar#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left)،
الذي يشير إلى الوقت المتبقي ويسمح لك باتّخاذ إجراءات إضافية قبل
إنهاء الاتصال كـ ABORTED.

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

## تلقّي رسالة عند اكتمال الإنشاء

يرسل الخادم رسالة [generationComplete](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
تشير إلى أنّ النموذج انتهى من إنشاء الردّ.

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

## الخطوات التالية

يمكنك استكشاف المزيد من الطرق لاستخدام Live API في دليل
[الإمكانات](https://ai.google.dev/gemini-api/docs/live?hl=ar) الكامل أو
صفحة [استخدام الأدوات](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar) أو
[دليل Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
