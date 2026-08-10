---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar
fetched_at: 2026-08-10T03:22:40.199888+00:00
title: "\u0628\u062f\u0621 \u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini Live API \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u062d\u0632\u0645\u0629 Google GenAI SDK \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# بدء استخدام Gemini Live API باستخدام حزمة Google GenAI SDK

تتيح واجهة برمجة التطبيقات Gemini Live API التفاعل الثنائي الاتجاه مع نماذج Gemini في الوقت الفعلي، وتتوافق مع إدخالات الصوت والفيديو والنص ومخرجات الصوت الأصلية. يوضّح هذا الدليل كيفية الدمج مع واجهة برمجة التطبيقات باستخدام حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي على الخادم.

[تجربة Live API في Google AI Studiomic](https://aistudio.google.com/live?hl=ar)
[استنساخ تطبيق المثال من GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)

## نظرة عامة

تستخدم واجهة برمجة التطبيقات Gemini Live WebSockets للتواصل في الوقت الفعلي. توفّر حزمة تطوير البرامج (SDK) `google-genai` واجهة غير متزامنة عالية المستوى لإدارة هذه الاتصالات.

المفاهيم الأساسية:

- **الجلسة**: اتصال دائم بالنموذج
- **الإعداد**: إعداد طرق الإدخال (صوت/نص) والصوت وتعليمات النظام
- **الإدخال في الوقت الفعلي**: إرسال إطارات الصوت والفيديو ككائنات ثنائية كبيرة الحجم

## الربط بواجهة برمجة التطبيقات Live API

بدء جلسة Live API باستخدام مفتاح واجهة برمجة تطبيقات:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## جارٍ إرسال الرسالة النصية

يمكن إرسال النص باستخدام `send_realtime_input` (Python) أو `sendRealtimeInput` (JavaScript).

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## إرسال الصوت

يجب إرسال الصوت كبيانات PCM أولية (صوت PCM أولي 16 بت، 16 كيلوهرتز، ترتيب البايتات الصغير).

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

للاطّلاع على مثال حول كيفية الحصول على الصوت من جهاز العميل (مثل المتصفح)،
يُرجى الرجوع إلى المثال الشامل على [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70).

## إرسال الفيديو

يتم إرسال إطارات الفيديو كصور فردية (مثل JPEG أو PNG) بعدد اللقطات في الثانية محدّد (إطار واحد في الثانية كحد أقصى).

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

للاطّلاع على مثال حول كيفية الحصول على الفيديو من جهاز العميل (مثل المتصفح)،
راجِع المثال الشامل على [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120).

## استلام الصوت

يتم تلقّي الردود الصوتية من النموذج على شكل أجزاء من البيانات.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

يمكنك الاطّلاع على مثال التطبيق على GitHub لمعرفة كيفية [تلقّي الصوت على الخادم](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) و[تشغيله في المتصفح](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174).

## جارٍ استلام الرسالة النصية

تتوفّر نصوص لكل من بيانات أدخلها المستخدم ومخرجات النموذج في محتوى الخادم.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## معالجة طلبات الأدوات

تتيح واجهة برمجة التطبيقات استخدام الأدوات (استدعاء الدوال). عندما يطلب النموذج إجراء مكالمة باستخدام أداة، عليك تنفيذ الدالة وإرسال الردّ.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## الخطوات التالية

- اطّلِع على دليل [الإمكانات](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar) الكامل لواجهة Live API لمعرفة الإمكانات والإعدادات الرئيسية، بما في ذلك ميزة "رصد النشاط الصوتي" وميزات الصوت الأصلية.
- اطّلِع على دليل [استخدام الأدوات](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar) لمعرفة كيفية دمج Live API مع الأدوات وميزة "استدعاء الدوال".
- اطّلِع على دليل [إدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-session?hl=ar) لمعرفة كيفية إدارة المحادثات الطويلة.
- اطّلِع على دليل [الرموز المميزة المؤقتة](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ar) لإجراء مصادقة آمنة في تطبيقات [العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live-api?hl=ar#implementation-approach).
- لمزيد من المعلومات عن واجهة برمجة تطبيقات WebSockets الأساسية، يُرجى الاطّلاع على [مرجع واجهة برمجة تطبيقات WebSockets](https://ai.google.dev/api/live?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-08 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-08 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
