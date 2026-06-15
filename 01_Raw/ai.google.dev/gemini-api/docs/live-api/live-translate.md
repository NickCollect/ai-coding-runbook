---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=ar
fetched_at: 2026-06-15T06:19:58.177241+00:00
title: "\u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0627\u0644\u0645\u0628\u0627\u0634\u0631\u0629 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الترجمة المباشرة باستخدام Gemini Live API

تتيح Gemini Live API ترجمة الكلام إلى كلام في الوقت الفعلي وبوقت استجابة منخفض بين أكثر من 70 لغة باستخدام نموذج [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=ar). من خلال ضبط Live API باستخدام إعدادات الترجمة، يمكنك بث الصوت بلغة واحدة وتلقّي مصدر إخراج الصوت المترجَم بلغة أخرى، ما يتيح ترجمة سلسة من الصوت إلى الصوت في الوقت الفعلي.

[يمكنك تجربة ميزة "الترجمة المباشرة" في Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=ar)
[نسخ تطبيق المثال من GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar#gemini-live-api-dev)

## مقارنة بين Live Agent و"الترجمة المباشرة"

على الرغم من أنّ كلتيهما تستخدمان Live API، يختلف النموذج الذهني لميزة "الترجمة المباشرة" عن التفاعلات مع الوكيل في الوقت الفعلي.

| Live Agent | الترجمة المباشرة |
| --- | --- |
| **يعمل النموذج كمساعد.** يستمع النموذج ويفكر ويتخذ إجراءات نيابةً عنك. | **يعمل النموذج كمترجم.** يتصرف النموذج كمسار ترجمة في الوقت الفعلي. |
| **يستخدم النموذج تفاعلات مستندة إلى الأدوار.** يعتمد النموذج على فترات التوقف المؤقتة ورصد النية ويتعامل مع المقاطعات. | **يستخدم النموذج معالجة البث المستمر.** يُترجم النموذج الكلام أثناء تحدّث المتحدّث بدون انتظار الأدوار. |
| **يتوافق النموذج مع الأدوات والوكلاء.** يتوافق النموذج بشكلٍ أساسي مع استدعاء الدوال و"بحث Google" والتعليمات. | **يتوافق النموذج مع الترجمة فقط.** يوفّر النموذج ترجمة بوقت استجابة منخفض فقط، ولا يتوافق مع الأدوات أو التعليمات. |
| **متعدد الوظائف بالكامل** : يتوافق النموذج مع إدخالات النصوص والصوت والفيديو والصور. | **يقتصر النموذج على الصوت.** يقتصر الإدخال على الصوت لضمان استيفاء الحدود الصارمة لوقت الاستجابة في الوقت الفعلي. |
| **إعداد دقيق** : يستخدم النموذج التعليمات الخاصة بالإنشاء والكلام والأدوات والنظام. | **إعداد مبسّط** : يمكنك ضبط `target_language_code` وعناصر التحكّم مثل `echo_target_language`. |

## البدء

توضّح الأمثلة التالية كيفية تهيئة عميل والاتصال بـ Live API باستخدام إعدادات الترجمة.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## إرسال الصوت

لبث الإدخالات الصوتية للترجمة، عليك إرسال صوت PCM خام بتنسيق little-endian و16 بت.

- **تنسيق الصوت المُدخَل**: صوت PCM خام بتنسيق little-endian و16 بت بمعدل 16 كيلوهرتز (أحادي).
- **تنسيق الصوت الناتج**: صوت PCM خام بتنسيق little-endian و16 بت بمعدل 24 كيلوهرتز (أحادي).
- **حجم الجزء ووقت الاستجابة**: يمكنك إرسال الصوت بأجزاء تبلغ مدة كل منها 100 ملي ثانية.

توضّح الأمثلة التالية كيفية إرسال أجزاء الصوت إلى الجلسة.

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

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## التهيئة

لتفعيل الترجمة، عليك تحديد `translationConfig` ضِمن `generationConfig` أثناء إعداد الجلسة.

### ضبط رسالة الإعداد

يتوافق `generationConfig` مع الحقول التالية لتفعيل النصوص:

- **`inputAudioTranscription`**: كائن يتيح للنموذج إرسال نصوص صوتية للنص الصوتي المُدخَل، إذا كان متوفرًا.
- **`outputAudioTranscription`**: كائن يتيح للنموذج إرسال نصوص صوتية للنص الصوتي الناتج (المترجَم)، إذا كان متوفرًا.

يتوافق `translationConfig` مع الحقول التالية:

- **`targetLanguageCode`**: رمز اللغة [BCP-47](#supported-languages) للغة التي تريد أن يترجم إليها النموذج (مثل `"pl"` للغة البولندية و`"es"` للإسبانية). الإعداد التلقائي هو `"en"`.
- **`echoTargetLanguage`**: قيمة منطقية تشير إلى كيفية التعامل مع الصوت المُدخَل الذي يكون باللغة المستهدَفة. إذا تم ضبط هذه القيمة على `true`، سيعيد النموذج نطق الصوت المُدخَل الذي يكون باللغة المستهدَفة. إذا تم ضبط هذه القيمة على `false`، سيظل النموذج صامتًا عندما يكون الكلام المُدخَل باللغة المستهدَفة. الإعداد التلقائي هو `false`.

في ما يلي مثال على بنية رسالة الإعداد:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## الرموز المميّزة المؤقتة للتطبيقات من جهة العميل

بالنسبة إلى التطبيقات من جهة العميل إلى جهة الخادم، يمكنك استخدام [الرموز المميّزة المؤقتة](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar) (المتوفّرة حاليًا في `v1alpha`) لتجنُّب عرض مفتاح واجهة برمجة التطبيقات.

عند استخدام الرموز المميّزة المؤقتة مع ميزة "الترجمة المباشرة":

1. عليك استخدام نقطة النهاية `v1alpha`.
2. **إعدادات الحظر:** بشكلٍ تلقائي، عليك تحديد `translationConfig` في قيود إنشاء الرمز المميّز على خادمك. يضمن ذلك حظر إعدادات الترجمة وعدم إمكانية العميل التلاعب بها.
3. **إعدادات إلغاء الحظر:** إذا أردت أن تتمكّن من ضبط `translationConfig` من جهة العميل (على سبيل المثال، للسماح للمستخدم باختيار اللغة المستهدَفة)، عليك إزالتها من طلب إنشاء الرمز المميّز وضبط `"lock_additional_fields": []` بدلاً من ذلك. سيؤدي ذلك إلى إلغاء حظر `translationConfig` ليتم ضبطها من جهة العميل.

### إنشاء رمز مميّز مؤقت مقيّد

توضّح الأمثلة التالية كيفية إنشاء رمز مميّز مؤقت يتضمّن قيودًا على الترجمة.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha'}
)

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
        'http_options': {'api_version': 'v1alpha'},
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    },
});
```

## القيود

- **طُرق الإدخال**: لا يتوافق النموذج مع الترجمة إلا مع الإدخال الصوتي. ولا يتوافق مع إدخال النصوص.
- **تكرار الصوت**: قد يكون تكرار الصوت غير متسق. قد تتغيّر الأصوات بعد فترات توقف مؤقتة طويلة، أو يتم تحديد الجنس الخطأ استنادًا إلى كيفية بدء الكلام، أو قد يتم استخدام صوت واحد أثناء المحادثات السريعة بين عدة متحدثين.
- **اكتشاف اللغة**: يواجه اكتشاف اللغة صعوبة في التعامل مع اللهجات الكثيفة أو اللغات المتشابهة (مثل الإسبانية والبرتغالية) أو التبديل السريع بين اللغات. **ملاحظة:** يجب أن يؤثر ذلك في النص الصوتي المُدخَل فقط. يجب أن تظل رموز اللغة والترجمة النهائية دقيقة.
- **الصوت في الخلفية**: تم تصميم النموذج لفلترة الضوضاء والموسيقى لإنتاج كلام واضح، ولكن قد لا يتم تجاهل كل الصوت في الخلفية.
- **إعادة نطق اللغة المستهدَفة**: عند ضبط `echoTargetLanguage: true`، قد تؤدي الضوضاء في الخلفية أو الموسيقى إلى ظهور تشويش في الصوت المترجَم عندما يكون الصوت المُدخَل باللغة المستهدَفة.

## اللغات المتاحة

تتوفّر ميزة "الترجمة المباشرة" باللغات التالية.

| اللغة | رمز BCP-47 | اللغة | رمز BCP-47 |
| --- | --- | --- | --- |
| الأفريقانية | af | الكازاخية | kk |
| Akan | ak | الخميرية | km |
| الألبانية | sq | الكينيارواندا | rw |
| الأمهرية | am | الكورية | ko |
| العربية | ar | لاو | lo |
| الأرمينية | hy | اللاتفية | lv |
| الأذربيجانية | az | الليتوانية | lt |
| الباسك | eu | المقدونية | mk |
| البيلاروسية | be | الماليزية | ms |
| البنغالية | bn | المالايالامية | ml |
| البلغارية | bg | المراثية | mr |
| البورمية (ميانمار) | my | المنغولية | mn |
| الكتالانية | ca | النيبالية | ne |
| الصينية (المبسطة) | zh-Hans | النرويجية | no, nb |
| الصينية (التقليدية) | zh-Hant | الفارسية | fa |
| الكرواتية | hr | البولندية | pl |
| التشيكية | cs | البرتغالية (البرازيل) | pt-BR |
| الدانماركية | da | برتغالي (البرتغال) | pt-PT |
| الهولندية | nl | البنجابية | pa |
| الإنجليزية | en | الرومانية | ro |
| الإستونية | et | الروسية | ru |
| الفلبينية | fil | الصربية | sr |
| الفنلندية | fi | السندية | sd |
| الفرنسية | fr | السنهالية | si |
| الغليشيانية | gl | السلوفاكية | sk |
| الجورجية | ka | السلوفينية | sl |
| الألمانية | de | الإسبانية | es |
| اليونانية | el | السندانية | su |
| الغوجاراتية | gu | السواحيلية | sw |
| الهوسا | ha | السويدية | sv |
| العبرية | he | التاميلية | ta |
| الهندية | hi | التيلوغوية | te |
| الهنغارية | hu | التايلاندية | th |
| الأيسلندية | is | التركية | tr |
| الإندونيسية | id | الأوكرانية | uk |
| الإيطالية | it | الأوردية | ur |
| اليابانية | ja | الأوزبكية | uz |
| الجافانية | jv | الفيتنامية | vi |
| الكانادا | kn | الزولو | zu |

## الخطوات التالية

- يمكنك قراءة الدليل الكامل حول إمكانات Live API [Capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar).
- يمكنك قراءة دليل [البدء باستخدام حزمة تطوير البرامج (SDK)](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=ar).
- يمكنك قراءة دليل [البدء باستخدام WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ar).
- يمكنك قراءة دليل [الرموز المميّزة المؤقتة](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=ar) للمصادقة الآمنة في التطبيقات من جهة العميل إلى جهة الخادم.
- يمكنك نسخ أمثلة [Live API](https://github.com/google-gemini/gemini-live-api-examples) من GitHub.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-09 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-09 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
