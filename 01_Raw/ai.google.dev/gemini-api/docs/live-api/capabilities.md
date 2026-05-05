---
source_url: https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar
fetched_at: 2026-05-05T20:04:39.404281+00:00
title: "Live API capabilities guide \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Live API capabilities guide

هذا دليل شامل يتناول الإمكانات والإعدادات المتاحة من خلال Live API.
يمكنك الاطّلاع على صفحة [البدء باستخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar) للحصول على نظرة عامة ورمز نموذجي لحالات الاستخدام الشائعة.

## قبل البدء

- **التعرّف على المفاهيم الأساسية:** إذا لم يسبق لك ذلك،
  ننصحك بقراءة صفحة [البدء باستخدام Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)  أولاً.
  سنتعرّف في هذا الدليل على المبادئ الأساسية لواجهة برمجة التطبيقات Live API وطريقة عملها و[مختلف طرق التنفيذ](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach).
- **تجربة Live API في AI Studio:** قد يكون من المفيد تجربة Live API في [Google AI Studio](https://aistudio.google.com/app/live?hl=ar) قبل البدء في إنشاء التطبيقات. لاستخدام Live API في Google AI Studio، انقر على **البث المباشر (Stream)**.

## مقارنة النماذج

يلخّص الجدول التالي الاختلافات الرئيسية بين
نموذج [Gemini 3.1 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ar) ونموذج [Gemini 2.5 Flash Live Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=ar):

| الميزة | معاينة Gemini 3.1 Flash Live | النسخة الحصرية من Gemini 2.5 Flash |
| --- | --- | --- |
| **[التفكير](#native-audio-output-thinking)** | تستخدم `thinkingLevel` للتحكّم في عمق التفكير من خلال إعدادات مثل `minimal` و`low` و`medium` و`high`. القيمة التلقائية هي `minimal` لتحسين وقت الاستجابة إلى أدنى حدّ. اطّلِع على [مستويات التفكير والميزانيات](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#levels-budgets). | يتم استخدام `thinkingBudget` لضبط عدد الرموز المميزة للتفكير. تكون ميزة "التفكير الديناميكي" مفعَّلة تلقائيًا. اضبط `thinkingBudget` على `0` لإيقافها. اطّلِع على [مستويات التفكير والميزانيات](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#levels-budgets). |
| **[تلقّي الردّ](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentservercontent)** | يمكن أن يحتوي حدث خادم واحد على أجزاء متعدّدة من المحتوى في الوقت نفسه (على سبيل المثال، `inlineData` والنص). احرص على أن يعالج الرمز البرمجي جميع الأجزاء في كل حدث لتجنُّب فقدان المحتوى. | يحتوي كل حدث على الخادم على جزء واحد فقط من المحتوى. يتم تسليم الأجزاء في أحداث منفصلة. |
| **[محتوى العميل](#incremental-updates)** | لا تتوفّر `send_client_content` إلا لإنشاء سجلّ سياق أولي (يتطلّب ضبط `initial_history_in_client_content` في إعدادات الجلسة). لإرسال تحديثات نصية أثناء المحادثة، استخدِم `send_realtime_input` بدلاً من ذلك. | يتوفّر `send_client_content` طوال المحادثة لإرسال تحديثات المحتوى التدريجية وتحديد السياق. |
| **[تفعيل التغطية](https://ai.google.dev/api/live?hl=ar#turncoverage)** | القيمة التلقائية هي `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO`. يتضمّن دور النموذج النشاط الصوتي الذي تم رصده وجميع لقطات الفيديو. | القيمة التلقائية هي `TURN_INCLUDES_ONLY_ACTIVITY`. يتضمّن ردّ النموذج النشاط الذي تم رصده فقط. |
| **[التعرّف المخصّص على النشاط الصوتي](#disable-automatic-vad)** (`activity_start`/`activity_end`) | متاح أوقِف ميزة "رصد النشاط الصوتي" التلقائية وأرسِل الرسالتَين `activityStart` و`activityEnd` يدويًا للتحكّم في حدود الدور. | متاح أوقِف ميزة "رصد النشاط الصوتي" التلقائية وأرسِل الرسالتَين `activityStart` و`activityEnd` يدويًا للتحكّم في حدود الدور. |
| **[إعدادات VAD التلقائية](#configure-automatic-vad)** | متاح اضبط المَعلمات، مثل `start_of_speech_sensitivity` و`end_of_speech_sensitivity` و`prefix_padding_ms` و`silence_duration_ms`. | متاح اضبط المَعلمات، مثل `start_of_speech_sensitivity` و`end_of_speech_sensitivity` و`prefix_padding_ms` و`silence_duration_ms`. |
| **[استدعاء الدوال غير المتزامن](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar#async-function-calling)** (`behavior: NON_BLOCKING`) | غير متاح لا يمكن استدعاء الدوال إلا بشكل تسلسلي. لن يبدأ النموذج في الردّ إلى أن ترسل ردّ الأداة. | متاح اضبط قيمة `behavior` على `NON_BLOCKING` في تعريف الدالة للسماح للنموذج بمواصلة التفاعل أثناء تشغيل الدالة. يمكنك التحكّم في طريقة تعامل النموذج مع الردود باستخدام المَعلمة `scheduling` (`INTERRUPT` أو `WHEN_IDLE` أو `SILENT`). |
| **[التحكّم الاستباقي بالصوت](#proactive-audio)** | غير متاح | متاح عند تفعيل هذه الميزة، يمكن للنموذج أن يقرّر بشكل استباقي عدم الردّ إذا كان المحتوى المُدخَل غير ذي صلة. اضبط قيمة `proactive_audio` على `true` في إعدادات `proactivity` (يتطلّب ذلك `v1alpha`). |
| **[الحوار العاطفي](#affective-dialog)** | غير متاح | متاح يعدّل النموذج أسلوب الردّ ليتناسب مع أسلوب التعبير والنبرة في الإدخال. اضبط قيمة `enable_affective_dialog` على `true` في إعدادات الجلسة (يتطلّب ذلك `v1alpha`). |

للانتقال من Gemini 2.5 Flash Live إلى Gemini 3.1 Flash Live، يُرجى الاطّلاع على [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ar#migrating).

## إنشاء اتصال

يوضّح المثال التالي كيفية إنشاء عملية ربط باستخدام مفتاح واجهة برمجة التطبيقات:

### Python

```
import asyncio
from google import genai

client = genai.Client()

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

const ai = new GoogleGenAI({});
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

## طُرق التفاعل

تقدّم الأقسام التالية أمثلة وسياقًا داعمًا لمختلف أساليب الإدخال والإخراج المتاحة في Live API.

### إرسال الصوت

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

### تنسيقات الصوت

تكون البيانات الصوتية في Live API دائمًا بتنسيق PCM الأولي ذي الترتيب البايتي الصغير، وبدقة 16 بت. يستخدم مصدر إخراج الصوت دائمًا معدّل بيانات يبلغ 24 كيلوهرتز. يكون معدّل البيانات في الملف الصوتي 16 كيلو هرتز بشكل تلقائي، ولكن ستعيد Live API أخذ عينات إذا لزم الأمر، ما يتيح إرسال أي معدّل بيانات في الملف الصوتي. لتحديد معدّل أخذ العينات من الصوت المُدخَل، اضبط نوع MIME لكل [Blob](https://ai.google.dev/api/caching?hl=ar#Blob) يحتوي على صوت على قيمة مثل `audio/pcm;rate=16000`.

### استلام الصوت

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

### جارٍ إرسال الرسالة النصية

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

### إرسال الفيديو

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

#### تعديلات المحتوى التدريجية

استخدِم التحديثات التزايدية لإرسال النص المُدخَل أو إنشاء سياق الجلسة أو استعادة سياق الجلسة. بالنسبة إلى السياقات القصيرة، يمكنك إرسال تفاعلات اتّجاهات مفصّلة لتمثيل التسلسل الدقيق للأحداث:

### Python

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)
```

### JavaScript

```
let inputTurns = [
  { "role": "user", "parts": [{ "text": "What is the capital of France?" }] },
  { "role": "model", "parts": [{ "text": "Paris" }] },
]

session.sendClientContent({ turns: inputTurns, turnComplete: false })

inputTurns = [{ "role": "user", "parts": [{ "text": "What is the capital of Germany?" }] }]

session.sendClientContent({ turns: inputTurns, turnComplete: true })
```

بالنسبة إلى السياقات الأطول، ننصحك بتقديم ملخّص لرسالة واحدة لإتاحة مساحة أكبر في قدرة الاستيعاب للتفاعلات اللاحقة. راجِع [استئناف الجلسة](https://ai.google.dev/gemini-api/docs/live-session?hl=ar#session-resumption) للتعرّف على طريقة أخرى لتحميل سياق الجلسة.

### النصوص المُحوَّلة من مقاطع صوتية

بالإضافة إلى ردّ النموذج، يمكنك أيضًا تلقّي نصوص لكل من مصدر إخراج الصوت والمدخل الصوتي.

لتفعيل تحويل الصوت الذي يخرجه النموذج إلى نص، أرسِل
`output_audio_transcription` في إعدادات الضبط. يتم استنتاج لغة التسجيل الذي تريد تحويله إلى نص من ردّ النموذج.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "output_audio_transcription": {}
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        message = "Hello? Gemini are you there?"

        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for response in session.receive():
            if response.server_content.model_turn:
                print("Model turn:", response.server_content.model_turn)
            if response.server_content.output_transcription:
                print("Transcript:", response.server_content.output_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  outputAudioTranscription: {}
};

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
    config: config,
  });

  const inputTurns = 'Hello how are you?';
  session.sendClientContent({ turns: inputTurns });

  const turns = await handleTurn();

  for (const turn of turns) {
    if (turn.serverContent && turn.serverContent.outputTranscription) {
      console.debug('Received output transcription: %s\n', turn.serverContent.outputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

لتفعيل تحويل الصوت إلى نص، أرسِل
`input_audio_transcription` في إعدادات الضبط.

### Python

```
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_data = Path("16000.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_data, mime_type='audio/pcm;rate=16000')
        )

        async for msg in session.receive():
            if msg.server_content.input_transcription:
                print('Transcript:', msg.server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";
import pkg from 'wavefile';
const { WaveFile } = pkg;

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

const config = {
  responseModalities: [Modality.AUDIO],
  inputAudioTranscription: {}
};

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("16000.wav");

  // Ensure audio conforms to API requirements (16-bit PCM, 16kHz, mono)
  const wav = new WaveFile();
  wav.fromBuffer(fileBuffer);
  wav.toSampleRate(16000);
  wav.toBitDepth("16");
  const base64Audio = wav.toBase64();

  // If already in correct format, you can use this:
  // const fileBuffer = fs.readFileSync("sample.pcm");
  // const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }
  );

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
    else if (turn.serverContent && turn.serverContent.inputTranscription) {
      console.debug('Received input transcription: %s\n', turn.serverContent.inputTranscription.text);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

### تغيير الصوت واللغة

تتيح نماذج [مصدر إخراج الصوت الأصلي](#native-audio-output) استخدام أي من الأصوات المتاحة لنماذج [تحويل النص إلى كلام (TTS)](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar#voices). يمكنك الاستماع إلى جميع الأصوات في [AI Studio](https://aistudio.google.com/app/live?hl=ar).

لتحديد صوت، اضبط اسم الصوت ضمن الكائن `speechConfig` كجزء من إعدادات الجلسة:

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "speech_config": {
        "voice_config": {"prebuilt_voice_config": {"voice_name": "Kore"}}
    },
}
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } }
};
```

تتيح Live API [لغات متعددة](#supported-languages).
تختار نماذج [مصدر إخراج الصوت الأصلي](#native-audio-output) اللغة المناسبة تلقائيًا، ولا تتيح ضبط رمز اللغة بشكل صريح.

## إمكانات الصوت المضمَّنة

تتضمّن أحدث نماذجنا ميزة [مصدر إخراج الصوت الأصلي](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=ar)، التي توفّر كلامًا طبيعيًا وواقعيًا وأداءً محسّنًا بلغات متعددة.

### جارٍ التفكير

تستخدم نماذج Gemini 3.1 `thinkingLevel` للتحكّم في عمق التفكير، مع إعدادات مثل `minimal` و`low` و`medium` و`high`. القيمة التلقائية هي `minimal` لتحسين وقت الاستجابة إلى أدنى حدّ. تستخدم نماذج Gemini 2.5
`thinkingBudget` لتحديد عدد الرموز المميزة الخاصة بالتفكير بدلاً من ذلك. لمزيد من التفاصيل حول المستويات والميزانيات، يُرجى الاطّلاع على [مستويات التفكير والميزانيات](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#levels-budgets).

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
    )
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Send audio input and receive audio
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
  },
};

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: ...,
  });

  // Send audio input and receive audio

  session.close();
}

main();
```

بالإضافة إلى ذلك، يمكنك تفعيل ملخّصات الأفكار من خلال ضبط `includeThoughts` على
`true` في الإعدادات. يمكنك الاطّلاع على [ملخّصات الأفكار](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#summaries)
لمزيد من المعلومات:

### Python

```
model = "gemini-3.1-flash-live-preview"

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"]
    thinking_config=types.ThinkingConfig(
        thinking_level="low",
        include_thoughts=True
    )
)
```

### JavaScript

```
const model = 'gemini-3.1-flash-live-preview';
const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low',
    includeThoughts: true,
  },
};
```

### حوار تفاعلي تعاطفي

تتيح هذه الميزة لـ Gemini مواءمة أسلوب ردوده مع التعبير المدخَل ونبرته.

لاستخدام الحوار التفاعلي التعاطفي، اضبط إصدار واجهة برمجة التطبيقات على `v1alpha` واضبط
`enable_affective_dialog` على `true` في رسالة الإعداد:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  enableAffectiveDialog: true
};
```

### التحكّم التلقائي بالصوت

عند تفعيل هذه الميزة، يمكن لـ Gemini أن يقرّر بشكل استباقي عدم الردّ إذا كان المحتوى غير ذي صلة.

لاستخدامها، اضبط إصدار واجهة برمجة التطبيقات على `v1alpha` واضبط الحقل `proactivity`
في رسالة الإعداد واضبط `proactive_audio` على `true`:

### Python

```
client = genai.Client(http_options={"api_version": "v1alpha"})

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={'proactive_audio': True}
)
```

### JavaScript

```
const ai = new GoogleGenAI({ httpOptions: {"apiVersion": "v1alpha"} });

const config = {
  responseModalities: [Modality.AUDIO],
  proactivity: { proactiveAudio: true }
}
```

## التعرّف على النشاط الصوتي (VAD)

تتيح ميزة "رصد النشاط الصوتي" (VAD) للنموذج التعرّف على وقت تحدث شخص ما. وهذا أمر ضروري لإنشاء محادثات طبيعية، لأنّه يتيح للمستخدم مقاطعة النموذج في أي وقت.

عندما ترصد ميزة VAD انقطاعًا، يتم إلغاء عملية إنشاء الصوت الجارية والتخلص منها. يتم الاحتفاظ فقط بالمعلومات التي تم إرسالها إلى العميل في سجلّ الجلسة. بعد ذلك، يرسل الخادم رسالة [`BidiGenerateContentServerContent`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentservercontent) للإبلاغ عن الانقطاع.

بعد ذلك، يتجاهل خادم Gemini أي طلبات معلّقة لاستدعاء الدوال ويرسل رسالة `BidiGenerateContentServerContent` تتضمّن أرقام تعريف الطلبات الملغاة.

### Python

```
async for response in session.receive():
    if response.server_content.interrupted is True:
        # The generation was interrupted

        # If realtime playback is implemented in your application,
        # you should stop playing audio and clear queued playback here.
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.interrupted) {
    // The generation was interrupted

    // If realtime playback is implemented in your application,
    // you should stop playing audio and clear queued playback here.
  }
}
```

### الكشف التلقائي عن النشاط الصوتي

بشكل تلقائي، ينفّذ النموذج ميزة &quot;التعرّف على النشاط الصوتي&quot; على دفق مستمر من إدخال الصوت. يمكن ضبط VAD باستخدام الحقل
[`realtimeInputConfig.automaticActivityDetection`](https://ai.google.dev/api/live?hl=ar#RealtimeInputConfig.AutomaticActivityDetection)
في [إعدادات الضبط](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentSetup).

عند إيقاف بث الصوت مؤقتًا لأكثر من ثانية واحدة (على سبيل المثال، لأنّ المستخدم أوقف الميكروفون)، يجب إرسال حدث [`audioStreamEnd`](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end) لمحو أي صوت مخزّن مؤقتًا. يمكن للعميل استئناف إرسال البيانات الصوتية في أي وقت.

### Python

```
# example audio file to try:
# URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
# !wget -q $URL -O sample.pcm
import asyncio
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        audio_bytes = Path("sample.pcm").read_bytes()

        await session.send_realtime_input(
            audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
        )

        # if stream gets paused, send:
        # await session.send_realtime_input(audio_stream_end=True)

        async for response in session.receive():
            if response.text is not None:
                print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
// example audio file to try:
// URL = "https://storage.googleapis.com/generativeai-downloads/data/hello_are_you_there.pcm"
// !wget -q $URL -O sample.pcm
import { GoogleGenAI, Modality } from '@google/genai';
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

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
    config: config,
  });

  // Send Audio Chunk
  const fileBuffer = fs.readFileSync("sample.pcm");
  const base64Audio = Buffer.from(fileBuffer).toString('base64');

  session.sendRealtimeInput(
    {
      audio: {
        data: base64Audio,
        mimeType: "audio/pcm;rate=16000"
      }
    }

  );

  // if stream gets paused, send:
  // session.sendRealtimeInput({ audioStreamEnd: true })

  const turns = await handleTurn();
  for (const turn of turns) {
    if (turn.text) {
      console.debug('Received text: %s\n', turn.text);
    }
    else if (turn.data) {
      console.debug('Received inline data: %s\n', turn.data);
    }
  }

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

باستخدام `send_realtime_input`، ستستجيب واجهة برمجة التطبيقات تلقائيًا للصوت استنادًا إلى VAD. في حين أنّ `send_client_content` يضيف الرسائل إلى سياق النموذج بالترتيب، تم تحسين `send_realtime_input` لتحقيق سرعة الاستجابة على حساب الترتيب الحتمي.

### إعدادات VAD التلقائية

لمزيد من التحكّم في نشاط VAD، يمكنك ضبط المَعلمات التالية. يمكنك الاطّلاع على [مرجع واجهة برمجة التطبيقات](https://ai.google.dev/api/live?hl=ar#automaticactivitydetection) للحصول على مزيد من المعلومات.

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {
        "automatic_activity_detection": {
            "disabled": False, # default
            "start_of_speech_sensitivity": types.StartSensitivity.START_SENSITIVITY_LOW,
            "end_of_speech_sensitivity": types.EndSensitivity.END_SENSITIVITY_LOW,
            "prefix_padding_ms": 20,
            "silence_duration_ms": 100,
        }
    }
}
```

### JavaScript

```
import { GoogleGenAI, Modality, StartSensitivity, EndSensitivity } from '@google/genai';

const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: false, // default
      startOfSpeechSensitivity: StartSensitivity.START_SENSITIVITY_LOW,
      endOfSpeechSensitivity: EndSensitivity.END_SENSITIVITY_LOW,
      prefixPaddingMs: 20,
      silenceDurationMs: 100,
    }
  }
};
```

### إيقاف ميزة "التعرّف التلقائي على النشاط الصوتي"

بدلاً من ذلك، يمكن إيقاف ميزة VAD التلقائية من خلال ضبط
`realtimeInputConfig.automaticActivityDetection.disabled` على `true` في رسالة الإعداد. في هذا الإعداد، يكون العميل مسؤولاً عن رصد كلام المستخدم وإرسال رسالتَي [`activityStart`](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start) و[`activityEnd`](https://ai.google.dev/api/live?hl=ar#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end) في الأوقات المناسبة. لا يتم إرسال `audioStreamEnd` في هذا الإعداد. بدلاً من ذلك، يتم تمييز أي انقطاع في البث برسالة `activityEnd`.

### Python

```
config = {
    "response_modalities": ["AUDIO"],
    "realtime_input_config": {"automatic_activity_detection": {"disabled": True}},
}

async with client.aio.live.connect(model=model, config=config) as session:
    # ...
    await session.send_realtime_input(activity_start=types.ActivityStart())
    await session.send_realtime_input(
        audio=types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
    )
    await session.send_realtime_input(activity_end=types.ActivityEnd())
    # ...
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    }
  }
};

session.sendRealtimeInput({ activityStart: {} })

session.sendRealtimeInput(
  {
    audio: {
      data: base64Audio,
      mimeType: "audio/pcm;rate=16000"
    }
  }

);

session.sendRealtimeInput({ activityEnd: {} })
```

## عدد الرموز المميّزة

يمكنك العثور على إجمالي عدد الرموز المميزة المستهلكة في الحقل [usageMetadata](https://ai.google.dev/api/live?hl=ar#usagemetadata) ضمن رسالة الخادم التي تم إرجاعها.

### Python

```
async for message in session.receive():
    # The server will periodically send messages that include UsageMetadata.
    if message.usage_metadata:
        usage = message.usage_metadata
        print(
            f"Used {usage.total_token_count} tokens in total. Response token breakdown:"
        )
        for detail in usage.response_tokens_details:
            match detail:
                case types.ModalityTokenCount(modality=modality, token_count=count):
                    print(f"{modality}: {count}")
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.usageMetadata) {
    console.debug('Used %s tokens in total. Response token breakdown:\n', turn.usageMetadata.totalTokenCount);

    for (const detail of turn.usageMetadata.responseTokensDetails) {
      console.debug('%s\n', detail);
    }
  }
}
```

## درجة دقة الوسائط

يمكنك تحديد دقة الوسائط المُدخلة من خلال ضبط الحقل
`mediaResolution` كجزء من إعدادات الجلسة:

### Python

```
from google.genai import types

config = {
    "response_modalities": ["AUDIO"],
    "media_resolution": types.MediaResolution.MEDIA_RESOLUTION_LOW,
}
```

### JavaScript

```
import { GoogleGenAI, Modality, MediaResolution } from '@google/genai';

const config = {
    responseModalities: [Modality.AUDIO],
    mediaResolution: MediaResolution.MEDIA_RESOLUTION_LOW,
};
```

## القيود

يُرجى مراعاة القيود التالية في Live API عند التخطيط لمشروعك.

### طُرق الاستجابة

لا تتوافق نماذج الصوت الأصلية إلا مع وضع الاستجابة `AUDIO. إذا كنت بحاجة إلى الحصول على ردّ النموذج كنص، استخدِم ميزة [تحويل الصوت إلى نص](#audio-transcription).

### مصادقة البرنامج

لا توفّر Live API تلقائيًا سوى مصادقة الخادم إلى الخادم. إذا كنت تنفّذ تطبيق Live API باستخدام [أسلوب من العميل إلى الخادم](https://ai.google.dev/gemini-api/docs/live?hl=ar#implementation-approach)، عليك استخدام [رموز مميزة مؤقتة](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ar) للحدّ من المخاطر الأمنية.

### مدة الجلسة

تقتصر مدة الجلسات الصوتية فقط على 15 دقيقة،
بينما تقتصر مدة الجلسات الصوتية والمرئية على دقيقتَين.
ومع ذلك، يمكنك ضبط [تقنيات مختلفة لإدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-session?hl=ar) من أجل تمديد مدة الجلسة إلى أجل غير مسمى.

### قدرة الاستيعاب

يبلغ الحدّ الأقصى لقدرة الاستيعاب في الجلسة:

- ‫128 ألف رمز مميز لنماذج [مصدر إخراج الصوت الأصلي](#native-audio-output)
- ‫32,000 رمز مميز لطُرز Live API الأخرى

## اللغات المتاحة

تتيح Live API اللغات الـ 97 التالية.

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| الأفريقانية | `af` | اللاتفية | `lv` |
| الأكانية | `ak` | الليتوانية | `lt` |
| الألبانية | `sq` | المقدونية | `mk` |
| الأمهرية | `am` | الماليزية | `ms` |
| العربية | `ar` | المالايالامية | `ml` |
| الأرمينية | `hy` | المالطية | `mt` |
| الأسامية | `as` | الماورية | `mi` |
| الأذربيجانية | `az` | المراثية | `mr` |
| الباسك | `eu` | المنغولية | `mn` |
| البيلاروسية | `be` | النيبالية | `ne` |
| البنغالية | `bn` | النرويجية | `no` |
| البوسنية | `bs` | الأوديا | `or` |
| البلغارية | `bg` | الأورومية | `om` |
| البورمية | `my` | البشتو | `ps` |
| الكتالانية | `ca` | الفارسية | `fa` |
| السيبيوانية | `ceb` | البولندية | `pl` |
| الصينية | `zh` | البرتغالية | `pt` |
| الكرواتية | `hr` | البنجابية | `pa` |
| التشيكية | `cs` | الكويتشوا | `qu` |
| الدانماركية | `da` | الرومانية | `ro` |
| الهولندية | `nl` | الرومانشية | `rm` |
| الإنجليزية | `en` | الروسية | `ru` |
| الإستونية | `et` | الصربية | `sr` |
| الفاروية | `fo` | السندية | `sd` |
| الفلبينية | `fil` | السنهالية | `si` |
| الفنلندية | `fi` | السلوفاكية | `sk` |
| الفرنسية | `fr` | السلوفينية | `sl` |
| الغليشيانية | `gl` | الصومالية | `so` |
| الجورجية | `ka` | السوتو الجنوبية | `st` |
| الألمانية | `de` | الإسبانية | `es` |
| اليونانية | `el` | السواحيلية | `sw` |
| الغوجاراتية | `gu` | السويدية | `sv` |
| الهوسا | `ha` | الطاجيكية | `tg` |
| العبرية | `iw` | التاميلية | `ta` |
| الهندية | `hi` | التيلوغوية | `te` |
| الهنغارية | `hu` | التايلاندية | `th` |
| الأيسلندية | `is` | التسوانية | `tn` |
| الإندونيسية | `id` | التركية | `tr` |
| الأيرلندية | `ga` | التركمانية | `tk` |
| الإيطالية | `it` | الأوكرانية | `uk` |
| اليابانية | `ja` | الأوردية | `ur` |
| الكانادا | `kn` | الأوزبكية | `uz` |
| الكازاخية | `kk` | الفيتنامية | `vi` |
| الخميرية | `km` | الويلزية | `cy` |
| الكينيارواندا | `rw` | الفريزيان | `fy` |
| الكورية | `ko` | الولوفية | `wo` |
| الكردية | `ku` | اليوروبا | `yo` |
| القيرغيزية | `ky` | الزولو | `zu` |
| لاو | `lo` |  |  |

## الخطوات التالية

- يمكنك الاطّلاع على دليلَي [استخدام الأدوات](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar) و[إدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-session?hl=ar) للحصول على معلومات أساسية حول استخدام Live API بفعالية.
- جرِّب Live API في [Google AI Studio](https://aistudio.google.com/app/live?hl=ar).
- لمزيد من المعلومات حول نماذج Live API، يُرجى الاطّلاع على [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-2.5-flash-native-audio) في صفحة "النماذج".
- يمكنك تجربة المزيد من الأمثلة في [كتاب وصفات Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=ar) و[كتاب وصفات أدوات Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb?hl=ar) و[نص برمجي للبدء باستخدام Live API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
