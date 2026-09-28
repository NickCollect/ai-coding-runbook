---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=ar
fetched_at: 2026-09-28T06:30:54.446058+00:00
title: "\u0627\u0644\u0646\u0633\u062e \u0627\u0644\u0645\u0628\u0627\u0634\u0631 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# النسخ المباشر باستخدام Gemini Live API

تتيح واجهة Gemini Live API تحويل الكلام إلى نص في الوقت الفعلي وبزمن استجابة منخفض باستخدام نموذج [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=ar). من خلال الربط بواجهة Live API عبر WebSockets أو استخدام حزمة تطوير البرامج (SDK) الخاصة بالذكاء الاصطناعي التوليدي من Google، يمكنك بث إدخال صوتي مستمر وتلقّي نصوص متزايدة ومباشرة في الوقت الفعلي أثناء حدوث الكلام.

[تجربة ميزة "النسخ المباشر" في Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=ar)
[فتح كتاب وصفات Colabcode](https://github.com/google-gemini/cookbook)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar#gemini-live-api-dev)

من خلال الاستفادة من واجهة برمجة التطبيقات Gemini Live، تتيح منصات المطوّرين، مثل
[Agora](https://docs.agora.io/en/ai/models/asr/gemini) و[Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration) و[LiveKit](https://docs.livekit.io/agents/models/stt/gemini/) و[Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google) و[Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) و[Vision Agents](https://visionagents.ai/integrations/stt/gemini)، للمطوّرين إنشاء واجهات عالية الأداء تعمل بالصوت ونشرها بسهولة. وتدير هذه المنصات بنية أساسية معقّدة لبث الوسائط في الوقت الفعلي وراء الكواليس، ما يتيح للمطوّرين التركيز بشكل كامل على تصميم تجربة المستخدم.

## مقارنة بين ميزة "الرد المباشر على المكالمات الهاتفية" وميزة "تحويل الصوت إلى نص مباشرةً"

مع أنّ كلتا الميزتين تستخدمان اتصال البث الثنائي الاتجاه Live API، تعمل ميزة "الكتابة المباشرة" كمسار مخصّص للتعرّف على الكلام بزمن استجابة منخفض بدلاً من أن تكون وكيل محادثة.

| الميزة | موظّف دعم يقدّم خدمة مباشرة | تحويل الصوت إلى نص مباشرةً |
| --- | --- | --- |
| **الدور الأساسي** | مساعد محادثة يستمع ويحلّل ويجيب. | مسار تحويل الكلام إلى نص في الوقت الفعلي الذي يحوّل الصوت الوارد إلى نص |
| **طريقة الرد** | المحتوى الصوتي والنصي المنطوق (`response_modalities=["AUDIO"]`) | نصوص البث المباشر (`response_modalities=["TEXT"]`) |
| **نمط التفاعل** | حوار قائم على التناوب مع رصد فترات التوقف والمقاطعات | معالجة البث المتواصل أثناء تحدث المتحدث |
| **الميزات المتاحة** | استدعاء الدالة و&quot;بحث Google&quot; وتعليمات النظام | تحديد اللغة المفضّلة للكلام (`custom_vocabulary`)، ورصد اللغة، ورصد النشاط الصوتي اليدوي والمختلط، والنسخ الذكي |
| **مصدر الإدخال** | متعدد الوسائط: الصوت والفيديو والصور والنصوص | إدخال الصوت (تنسيق PCM الأولي 16 بت) |

## البدء

توضّح الأمثلة التالية كيفية فتح جلسة بث ثنائي الاتجاه باستخدام `gemini-3.5-transcribe-live` وتلقّي نصوص في الوقت الفعلي.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## النصوص المؤقتة والنهائية المحوَّلة من الصوت

عندما يتم بث الصوت إلى Live API، يرسل الخادم حقلَي كتابة متكاملَين ضمن `server_content`:

- **`interim_input_transcription`**: فرضيات جزئية تخمينية يتم تعديلها أثناء تحدث المتحدث بنشاط، مع تأخير منخفض. تحدث هذه التحديثات الجزئية بسرعة وبأقل تأخير ممكن. استخدِم `interim_input_transcription` لعرض ترجمة وشرح متجاوبَين لواجهة المستخدم المباشرة أو لمعاينة الترجمة والشرح.
- ‫**`input_transcription`**: النص النهائي الذي يتم إرساله عندما يتوقف المتحدث مؤقتًا أو تنتهي الجملة أو يتم الانتهاء من الكلام. وبعد إصداره، يمثّل هذا النص النسخة الموثوقة التي قدّمها النموذج لهذا الجزء من الكلام. في وضع "التحويل الذكي للصوت إلى نص"، سيشمل ذلك الردّ المنقّح والمنسّق.

يوضّح المثال التالي كيفية عرض النتائج الجزئية المؤقتة للبث المباشر وإرسال النصوص النهائية:

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## إرسال الصوت

بث أجزاء الصوت عبر الاتصال النشط بتنسيق PCM الخام 16 بت

- **تنسيق الصوت:** Raw 16-bit PCM بمعدل 16 كيلوهرتز (أحادي، little-endian).
- **حجم الأجزاء:** أرسِل الصوت في أجزاء تبلغ مدة كل منها 100 ملي ثانية (من 1,024 إلى 2,048 إطارًا).
- **نوع MIME:** `audio/pcm;rate=16000` (أو معدّل البيانات في الملف الصوتي المطابق)

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## ميزات تحويل الصوت إلى نص

### التعرّف التلقائي على اللغة

يؤدي حذف `language_codes` أو ضبط `language_codes=[]` إلى تفعيل ميزة "التعرّف التلقائي على اللغة". يرصد النموذج بشكل ديناميكي اللغة المحكية في جميع الجُمل، بما في ذلك المحادثات المتعددة اللغات والتبديل بين اللغات.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### تلميح اللغة المحدّدة

قدِّم رموز لغة BCP-47 صريحة (على سبيل المثال، `["es-ES"]` للإسبانية أو `["fr-FR"]` للفرنسية) لتفضيل التعرّف على لغات معيّنة (راجِع [اللغات المتوافقة](#supported-languages)).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### تفضيل المفردات المخصّصة

قدِّم قائمة تضم ما يصل إلى 1,000 عبارة أو اسم علم أو اسم علامة تجارية أو مصطلح فني في `custom_vocabulary` لتوجيه التعرّف على الكلام نحو مصطلحات معيّنة (عادةً ما يتم تحقيق أفضل النتائج باستخدام ما يصل إلى 100 مصطلح).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### التحويل الذكي للصوت إلى نص

اضبط تنسيق إخراج النص باستخدام المَعلمة `mode` في `input_audio_transcription`:

- **`VERBATIM` (الإعداد التلقائي)**: ينتج عنه نسخة طبق الأصل من كل ما يُقال، مع الحفاظ على الكلمات الحشو الخام ("أمم" و"آه" و"مثل") والتكرار والبدايات الخاطئة.
- **`SMART` (التحويل الذكي للصوت إلى نص)**: تنظيف النص وتنظيمه لتسهيل قراءته:

  - **إزالة أخطاء الكلام**: يزيل هذا الخيار كلمات الحشو والتلعثم وبدايات الجمل الخاطئة.
  - **التصحيحات الذاتية المضمّنة**: تحلّ المشاكل في التصحيحات المنطوقة بشكل طبيعي.
  - **التنسيق المنظَّم**: ينسّق تلقائيًا القوائم والنقاط والأرقام والتواريخ وفواصل الفقرات.
  - **القواعد النحوية واستخدام الأحرف الكبيرة والصغيرة**: يتم تطبيق قواعد الترقيم واستخدام الأحرف الكبيرة والصغيرة بشكل طبيعي.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## استراتيجيات رصد النشاط الصوتي (VAD)

### ميزة "التعرّف التلقائي على النشاط الصوتي" (الإعداد التلقائي)

بشكلٍ تلقائي، ترصد ميزة "التعرّف التلقائي على النشاط الصوتي" من جهة الخادم متى يبدأ المتحدث ومتى يتوقف عن الكلام.

### التعرّف المختلط على الصوت

تجمع [ميزة "التعرّف على النشاط الصوتي" المختلطة](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar#hybrid-vad) بين ميزة "التعرّف التلقائي على بداية الكلام" من جهة الخادم وميزة "التعرّف على نهاية الكلام" من جهة العميل لإكمال الدور بدون أي تأخير:

1. **تظل ميزة "التعرّف التلقائي على نشاط الصوت" من جهة الخادم مفعَّلة** لرصد بدايات الكلام بدقة باستخدام مساحة بادئة للصوت، ما يمنع اقتطاع الكلمات الأولى.
2. **رصد الصمت من جهة العميل باستخدام ميزة "الرصد الصوتي"**: عندما ترصد ميزة "الرصد الصوتي" المحلية على الجهاز أنّ المتحدث توقّف عن الكلام، يرسل العميل إشارة `audio_stream_end` على الفور.
3. **الإنهاء السريع**: يتعامل الخادم مع `audio_stream_end` كطلب فوري لإنهاء المحادثة، ويتجاوز وقت الانتظار التلقائي للصمت من جهة الخادم ويعرض النص النهائي بأقل وقت استجابة.
4. **الخيار الاحتياطي**: إذا تعذّر تشغيل VAD من جهة العميل، يعمل VAD من جهة الخادم كخيار احتياطي تلقائي.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### التعرّف اليدوي على النشاط الصوتي (الضغط للتحدّث)

بالنسبة إلى واجهات جهاز الاتصال اللاسلكي أو أزرار الضغط والتحدث، عليك إيقاف ميزة "التعرّف التلقائي على النشاط الصوتي" بالكامل والتحكّم في حدود التبديل بشكلٍ صريح باستخدام `activity_start` و`activity_end`:

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## الرموز المميزة المؤقتة في تطبيقات العميل

بالنسبة إلى التطبيقات التي تتواصل بين العميل والخادم (مثل تطبيقات الأجهزة الجوّالة أو تطبيقات الويب التي تبث المحتوى مباشرةً من ميكروفون)، استخدِم [الرموز المميزة المؤقتة](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar) لتجنُّب عرض مفتاح واجهة برمجة التطبيقات في رمز العميل.

أنشئ رمزًا مميزًا مؤقتًا محدود الاستخدام على خادمك قبل بدء اتصال العميل:

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## اللغات المتاحة

تتوفّر اللغات ورموز اللغة BCP-47 التالية في ميزة "النسخ المباشر" من Gemini 3.5:

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| الأفريقانية | `af-ZA` | اليابانية | `ja-JP` |
| الأمهرية | `am-ET` | الجافانية | `jv-ID` |
| العربية (مصر) | `ar-EG` | كابوفيرديانو | `kea-CV` |
| الأرمينية | `hy-AM` | الكانادا | `kn-IN` |
| الأسامية | `as-IN` | الكازاخستانية | `kk-KZ` |
| أذربيجان | `az-AZ` | الكورية | `ko-KR` |
| البيلاروسية | `be-BY` | القيرغيزية | `ky-KG` |
| البنغالية (بنغلاديش) | `bn-BD` | اللاتفية | `lv-LV` |
| البنغالية (الهند) | `bn-IN` | اللينجالا | `ln-CD` |
| البوسنية | `bs-BA` | الليتوانية | `lt-LT` |
| البلغارية | `bg-BG` | المقدونية | `mk-MK` |
| البلغارية (الأرومانية) | `rup-BG` | الماليزية | `ms-MY` |
| البورمية | `my-MM` | المالايالامية | `ml-IN` |
| الكانتونية (التقليدية) | `yue-Hant-HK` | المالطية | `mt-MT` |
| الكتالانية | `ca-ES` | الصينية الماندرين (المبسطة) | `cmn-Hans-CN` |
| السيبيوانية | `ceb` | المراثية | `mr-IN` |
| الخميرية القياسية | `km-KH` | المنغولية | `mn-MN` |
| الكرواتية | `hr-HR` | النيبالية | `ne-NP` |
| التشيكية | `cs-CZ` | النرويجية | `nb-NO` |
| الدانماركية | `da-DK` | الأوريا | `or-IN` |
| الهولندية | `nl-NL` | البولندية | `pl-PL` |
| الإنجليزية (بريطانيا العظمى) | `en-GB` | البرتغالية (البرازيل) | `pt-BR` |
| الإنجليزية (الهند) | `en-IN` | البرتغالية (البرتغال) | `pt-PT` |
| الإنجليزية (الولايات المتحدة) | `en-US` | البنجابية | `pa-IN` |
| الإستونية | `et-EE` | البنجابية (نص غورموخي) | `pa-Guru-IN` |
| الفارسية | `fa-IR` | الرومانية | `ro-RO` |
| الفلبينية | `fil-PH` | الروسية | `ru-RU` |
| الفنلندية | `fi-FI` | الصربية | `sr-RS` |
| الفرنسية | `fr-FR` | السندية (الخط العربي) | `sd-Arab-IN` |
| الغليشيانية | `gl-ES` | السلوفاكية | `sk-SK` |
| الجورجية | `ka-GE` | السلوفينية | `sl-SI` |
| الألمانية | `de-DE` | الإسبانية (أمريكا اللاتينية) | `es-419` |
| اليونانية | `el-GR` | الإسبانية (الولايات المتحدة) | `es-US` |
| الغوجاراتية | `gu-IN` | السواحيلية (كينيا) | `sw-KE` |
| الهوسا | `ha-NG` | السويدية | `sv-SE` |
| العبرية | `he-IL` | الطاجيكية | `tg-TJ` |
| الهندية | `hi-IN` | التيلوغوية | `te-IN` |
| الهنغارية | `hu-HU` | التايلاندية | `th-TH` |
| الأيسلندية | `is-IS` | التركية | `tr-TR` |
| الإنجليزية الهندية | `en-IN` | الأوكرانية | `uk-UA` |
| الإندونيسية | `id-ID` | الأوزبكية | `uz-UZ` |
| الإيطالية | `it-IT` | الفيتنامية | `vi-VN` |

## مرجع المَعلمة

ضبط ميزة "تحويل الصوت إلى نص مباشرةً" باستخدام الحقول في `input_audio_transcription` و`realtime_input_config`:

| المَعلمة | النوع | الوصف |
| --- | --- | --- |
| `language_codes` | مصفوفة سلاسل | رموز اللغة المستخدَمة في المعيار BCP-47 (مثل `["en-US"]`). في حال حذفها أو تركها فارغة (`[]`)، يرصد النموذج اللغة تلقائيًا ويتعامل مع الكلام المتعدد اللغات. |
| `custom_vocabulary` | مصفوفة سلاسل | ما يصل إلى 1,000 عبارة مخصّصة أو اختصار أو اسم علامة تجارية أو اسم علم لتوجيه ميزة "التعرّف على الكلام" |
| `mode` | سلسلة | وضع "تحويل الصوت إلى نص": `"VERBATIM"` (تلقائي) أو `"SMART"` (تحويل الصوت إلى نص بذكاء). عند ضبطها على `"SMART"`، يزيل النموذج كلمات الحشو وينسّق القوائم ويصحّح الأخطاء في الكلام. |
| `automatic_activity_detection.disabled` | منطقي | اضبط القيمة على `true` لإيقاف ميزة "رصد النشاط الصوتي" التلقائي وإرسال إشارتَي `activityStart` و`activityEnd` يدويًا. |

### حقول استجابة الخادم

| الحقل | الوصف |
| --- | --- |
| `server_content.interim_input_transcription` | فرضية النسخ الجزئي المؤقت ذات وقت الاستجابة المنخفض التي يتم إصدارها باستمرار أثناء تحدث المستخدم بشكل نشط |
| `server_content.input_transcription` | يتم إصدار نص نهائي وموثوق به عند انتهاء نوبة الكلام. |

## القيود

- **مدة الجلسة:** تتيح جلسات "الكتابة المباشرة" البث المتواصل لمدة تصل إلى 10 دقائق.
- **تحديد هوية المتحدث:** لا تتوفّر ميزة تحديد هوية المتحدث في جلسات البث المباشر. بالنسبة إلى ميزة "تحديد هوية المتحدث"، استخدِم نقطة النهاية غير المتدفقة [تحويل الصوت إلى نص](https://ai.google.dev/gemini-api/docs/transcribe?hl=ar#speaker-diarization).
- **الطوابع الزمنية على مستوى الكلمات:** لا تتوافق الطوابع الزمنية على مستوى الكلمات مع Live API. تبعث Live API طوابع زمنية على مستوى الجملة (`interim_input_transcription` و`input_transcription`).
- **المفردات المخصّصة:** يمكنك تقديم ما يصل إلى 1,000 عبارة في `custom_vocabulary`، ولكن عادةً ما يتم تحقيق أفضل النتائج باستخدام ما يصل إلى 100 عبارة.
- **التوافق مع الأوضاع:** تزيل ميزة "النسخ الذكي" (`"mode": "SMART"`) الكلمات الحشو وتنسّق النص الذي يراعي النية، ولكن لا يمكن دمجها مع التعليقات التوضيحية للكلمات.

## الخطوات التالية

- يمكنك الاطّلاع على [مستندات "تحويل الصوت إلى نص في Gemini"](https://ai.google.dev/gemini-api/docs/transcribe?hl=ar) للملفات الصوتية غير المتدفقة.
- اطّلِع على [نظرة عامة على Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=ar) لبرامج الوكلاء الحوارية الصوتية.
- يمكنك الاطّلاع على [دليل "الترجمة المباشرة"](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ar) للحصول على ترجمة فورية للمحادثات الصوتية.
- راجِع [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#gemini-3.5-transcribe-live) لمعرفة أسعار البث المباشر باستخدام Live API.
- اطّلِع على [دليل إمكانات Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-10 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-10 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
