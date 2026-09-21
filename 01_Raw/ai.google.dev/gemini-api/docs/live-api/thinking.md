---
source_url: https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=ar
fetched_at: 2026-09-21T05:46:10.802803+00:00
title: "\u0627\u0644\u062a\u0641\u0643\u064a\u0631 \u0641\u064a \u0648\u0627\u062c\u0647\u0629 Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التفكير في واجهة Live API

تتيح واجهة برمجة التطبيقات Gemini Live إجراء محادثات صوتية ثنائية الاتجاه في الوقت الفعلي مع نماذج Gemini.

تعمل النماذج الصوتية العادية بشكل جيد مع الحوارات المباشرة. تتحدث مع النموذج، فينشئ ردًا صوتيًا على الفور. ولكن عندما يتطلّب الطلب تخطيطًا أو تحليلاً معقّدًا أو أدوات خارجية، تصل الردود المباشرة إلى حدّ معيّن. يجب أن يجيب النموذج بدون تقديم أسباب أو أن يتوقف مؤقتًا بدون إصدار أي صوت أثناء انتظار انتهاء الأدوات.

تضيف ميزة &quot;التفكير باستخدام Live API&quot; (`gemini-3.8-live-extended-thinking`) عملية استنتاج في الخلفية إلى جلسات الصوت في الوقت الفعلي. يخطّط النموذج ويستدعي أدوات غير متزامنة في الخلفية، بينما يتحدث بعبارات حوارية طبيعية لإبقاء التفاعل نشطًا.

تغيّر هذه البنية دورة حياة المحادثة بطريقتَين رئيسيتَين:

- **عبارات الحشو الحوارية**: يعرض النموذج تحديثات مؤقتة (مثل "جارٍ التحقّق من خيارات الرحلات الجوية الآن") أثناء تنفيذ الأدوات في الخلفية.
- **تتبُّع حالة التفاعل**: بما أنّ النموذج يمكنه التحدّث عدة مرات
  خلال طلب واحد، يرسل الخادم `interaction_status: "IN_PROGRESS"`
  أثناء المعالجة في الخلفية و`interaction_status: "IDLE"` عند اكتمال
  المهمة بشكل عام.

يقارن المخطّط التالي بين دورات حياة التفاعل بين جلسات Live Voice العادية وميزة "التفكير مع التفسير في الخلفية":

![مقارنة بين ميزة &quot;استدعاء الدوال&quot; في Live API وميزة &quot;تتبُّع الحالة&quot;](https://ai.google.dev/static/gemini-api/docs/images/thinking-model-comparison.svg?hl=ar)

## اختيار النموذج المناسب

عند الاختيار بين `gemini-3.8-live` و`gemini-3.8-live-extended-thinking`، يجب مراعاة ثلاثة اعتبارات رئيسية، وهي: وقت استجابة الطلب وتعقيد المهمة وطريقة معالجة حالة العميل.

### حالات استخدام Gemini 3.8 Live

استخدِم `gemini-3.8-live` للوكلاء الحواريين الذين يستندون إلى الصوت ويتطلّبون زمن استجابة منخفضًا، حيث يكون تبادل الأدوار الفوري ضروريًا وتكون المهام مباشرة.

- **مساعدات صوتية حوارية**: تستخدم في فرز طلبات خدمة العملاء، وممارسة اللغات، والبحث الصوتي، وسرد القصص التفاعلية.
- **تنفيذ الأدوات بسرعة**: سير العمل الذي تعرض فيه الأدوات الخارجية النتائج في غضون أجزاء من الثانية (مثل قراءة قيم المستشعر أو التحكّم في الأجهزة الذكية).
- **منطق بسيط من جهة العميل**: التطبيقات التي تتلقّى فيها كل خطوة من المستخدم استجابة واحدة من النموذج، ويشير فيها `turnComplete: true` بشكل موثوق إلى وقت عدم النشاط في الجلسة.

### حالات استخدام ميزة "التفكير المطوّل" في Gemini 3.8 Live

استخدِم `gemini-3.8-live-extended-thinking` عندما يحتاج الوكيل إلى تقييم بيانات معقّدة أو التخطيط لعدة خطوات أو التعامل مع أدوات تستغرق عدة ثوانٍ لتنفيذها.

- **بيانات التشخيص والدعم المتعدّدة الخطوات**: يقدّم وكلاء الدعم الفني بيانات تشخيصية لمشاكل النظام في عدّة سجلّات ورموز أخطاء وعمليات تحقّق من الإعدادات.
- **استرجاع البيانات المنسَّق**: وكلاء السفر والحجز الذين يبحثون عن رحلات جوية ويطلبون معلومات عن الفنادق ويقارنون الأسعار من خلال طلبات بيانات متوازية من واجهة برمجة التطبيقات
- **دروس خصوصية في العلوم والتكنولوجيا والهندسة والرياضيات (STEM) والبرمجة**: وكلاء تعليميون يتحقّقون من صحة الصيغ أو يصحّحون الأخطاء في الرموز البرمجية أو يحلّون المشاكل المنطقية المتعدّدة الخطوات قبل تقديم شرح.
- **وقت استجابة أداة التمويه**: تجارب صوتية تؤدي فيها الدوال التي تستغرق وقتًا طويلاً إلى
  حدوث صمت محرج للمستمع.

### ملخّص الاختلافات الرئيسية

يلخّص الجدول التالي الاختلافات الفنية بين النموذجين:

| الميزة | ‫Gemini 3.8 Live | ‫Gemini 3.8 Live Extended Thinking |
| --- | --- | --- |
| **حالات الاستخدام الأساسية** | وكلاء صوتيون بوقت استجابة منخفض، وأوامر مباشرة، وأدوات سريعة | حلّ المشاكل المتعددة الخطوات، والتخطيط المعقّد، وسير العمل المتعدد الأدوات |
| **نقطة نهاية النموذج** | `gemini-3.8-live` | `gemini-3.8-live-extended-thinking` |
| **بنية الاستدلال** | الاستدلال المتداخل مع ملف تعريف ثابت لوقت الاستجابة (`thinking_level` غير متاح) | الاستدلال في الخلفية القابل للضبط (`thinking_level`: `low`، `medium`، `high`؛ `MINIMAL` غير متاح) |
| **عرض الحدود** | يؤدي `turnComplete: true` إلى إغلاق الدور والعودة إلى وضع الخمول | `turnComplete: true` ينهي الجملة، و`interaction_status` يتحكّم في دورة حياة الجلسة |
| **الكلمات الحشو** | ينتظر النموذج تنفيذ الأداة قبل التحدث | تبث النماذج عبارات حوارية وسيطة أثناء المعالجة |
| **تنفيذ الأداة** | متوافق مع الأدوات المتزامنة (`BLOCKING`) وغير المتزامنة (`NON_BLOCKING`) | يتطلّب إعدادات غير متزامنة (`NON_BLOCKING`) للأدوات |

## مسارات نقل البيانات والدمج

اتّبِع الخطوات التالية لترقية تطبيقات الصوت الحالية أو دمج Thinking في جلسات Live API.

### الترقية من Gemini 3.1 Flash Live

بالنسبة إلى تطبيقات الصوت الحالية التي تستخدم `gemini-3.1-flash-live-preview`، يتطلّب الترقية إلى `gemini-3.8-live` تعديل سلسلة النموذج وحذف `thinking_level` (أو `thinking_config`) من إعداداتك، لأنّ `thinking_level` غير متوافق مع `gemini-3.8-live`:

```
{
  "setup": {
    "model": "models/gemini-3.8-live"
  }
}
```

ستبقى دورة حياة المنعطف وإشارات `turnComplete` متطابقة.

### اعتماد التفكير

لاستخدام `gemini-3.8-live-extended-thinking`، عليك تعديل ثلاث نقاط تكامل:

1. **استخدام `interaction_status` بدلاً من `turnComplete`**: في جلسات Thinking، يمكن للنموذج إصدار عبارات حشو وسيطة أثناء التفكير. افحص الحقل `interaction_status` في رسائل الخادم الواردة
   لإدارة حالة واجهة المستخدم. لا يتم الرجوع إلى وضع الخمول إلا عندما تكون قيمة `interaction_status` هي `IDLE`.

   ### Python

   ```
   status = getattr(message, "interaction_status", None)
   if status == "IDLE":
       # Ready for user input
       set_ui_state("listening")
   elif status == "IN_PROGRESS":
       # Reasoning or executing tools
       set_ui_state("thinking")
   ```

   ### JavaScript

   ```
   if (message.interactionStatus === 'IDLE') {
     // Ready for user input
     setUiState('listening');
   } else if (message.interactionStatus === 'IN_PROGRESS') {
     // Reasoning or executing tools
     setUiState('thinking');
   }
   ```
2. **الإعلان عن دوال غير حظر**: اضبط `"behavior": "NON_BLOCKING"` على جميع تعريفات الدوال. تُشغّل نماذج التفكير الأدوات بشكل غير متزامن في الخلفية أثناء بث التحديثات الشفهية. تعرض أدوات الحظر المتزامنة خطأً.

   ### Python

   ```
   search_flights = types.FunctionDeclaration(
       name="search_flights",
       description="Searches for available flights.",
       behavior="NON_BLOCKING",
       parameters={
           "type": "OBJECT",
           "properties": {
               "destination": {"type": "STRING"},
           },
           "required": ["destination"],
       },
   )
   ```

   ### JavaScript

   ```
   const searchFlights = {
     name: 'search_flights',
     description: 'Searches for available flights.',
     behavior: 'NON_BLOCKING',
     parameters: {
       type: 'OBJECT',
       properties: {
         destination: { type: 'STRING' },
       },
       required: ['destination'],
     },
   };
   ```
3. **ضبط عمق الاستدلال**: اضبط `thinking_config` في إعدادات الجلسة لتعديل مستويات الاستدلال (`low` أو `medium` أو `high`؛ `MINIMAL` غير متاح).

   ### Python

   ```
   config = types.LiveConnectConfig(
       response_modalities=["AUDIO"],
       thinking_config=types.ThinkingConfig(
           thinking_level="low",
       ),
       tools=[types.Tool(function_declarations=[search_flights])],
   )
   ```

   ### JavaScript

   ```
   const config = {
     responseModalities: [Modality.AUDIO],
     thinkingConfig: {
       thinkingLevel: 'low',
     },
     tools: [{ functionDeclarations: [searchFlights] }],
   };
   ```

## المقارنة جنبًا إلى جنب بين البروتوكولات

يقارن هذا القسم رسائل WebSocket التي يتم تبادلها خلال كل مرحلة من مراحل جلسة Live API.

### الخطوة 1: إعداد الجلسة

يتصل كلا النموذجين بنقطة نهاية WebSocket نفسها:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=$API_KEY
```

- **مطابقة**: مصادقة عنوان URL لـ WebSocket ومفتاح واجهة برمجة التطبيقات
- **سلسلة الطراز**: `gemini-3.8-live` مقابل `gemini-3.8-live-extended-thinking`.
- **إعدادات التفكير**: يضيف وضع "أفكاري" `thinkingConfig` لتعديل مستوى التفكير.
- **سلوك الأداة**: يتطلّب التفكير `"behavior": "NON_BLOCKING"` في تعريفات الدوال.

### ‫Gemini 3.8 Live

```
{
  "setup": {
    "model": "models/gemini-3.8-live",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      }
    }
  }
}
```

### ‫Gemini 3.8 Live Extended Thinking

```
{
  "setup": {
    "model": "models/gemini-3.8-live-extended-thinking",
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "prebuiltVoiceConfig": {
            "voiceName": "Puck"
          }
        }
      },
      "thinkingConfig": {
        "thinkingLevel": "LOW"
      }
    },
    "tools": [{
      "functionDeclarations": [{
        "name": "searchFlights",
        "description": "Searches for flights between cities.",
        "behavior": "NON_BLOCKING",
        "parameters": {
          "type": "OBJECT",
          "properties": {
            "destination": { "type": "STRING" }
          },
          "required": ["destination"]
        }
      }]
    }]
  }
}
```

يتلقّى كلا النموذجين إقرارًا من الخادم عند الاتصال:

```
{
  "setupComplete": {}
}
```

### الخطوة 2: إدخال الصوت من المستخدم

تتطابق ميزة بث الصوت في كلا الطرازين. يتم بث أجزاء من بيانات صوتية بتنسيق PCM الأولي بمعدل 16 كيلو هرتز في الوقت الفعلي باستخدام `realtimeInput`:

```
{
  "realtimeInput": {
    "audio": {
      "data": "UklGRiQAAABXQVZF...",
      "mimeType": "audio/pcm;rate=16000"
    }
  }
}
```

### الخطوة 3: استجابة النموذج ودورة حياة الحالة

يبث كلا الطرازين أجزاء صوتية بتنسيق PCM بمعدّل 24 كيلوهرتز في `serverContent.modelTurn`. ومع ذلك، تختلف إدارة دورة الحياة في ما يلي:

#### مسار الردّ المباشر في Gemini 3.8

1. يبث الخادم أجزاء صوتية للرد.
2. يرسل الخادم `turnComplete: true`، ما يشير إلى أنّ النموذج انتهى من التحدث وأنّ الجلسة غير نشطة.

```
// 1. Audio stream chunks
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    }
  }
}

// 2. Turn completion -> Signals client to switch UI to Idle/Listening
{
  "serverContent": {
    "turnComplete": true
  }
}
```

#### مسار الردود في ميزة "التفكير الموسّع" في Gemini 3.8 Live

1. **الكلمات الحشو**: يصدر النموذج كلامًا وسيطًا (مثل
   *"جارٍ البحث عن رحلات جوية إلى دبي..."*) مع `turnComplete: true` و`interactionStatus: "IN_PROGRESS"`.
2. **استدعاء الأداة غير المتزامن**: يرسل الخادم استدعاء الأداة بينما يظل `interactionStatus` `"IN_PROGRESS"`، ما يشير إلى أنّ الخادم يعالج حاليًا الدورات المتعددة الخطوات وينتظر استجابة الأداة.
3. **ردّ الأداة**: ينفّذ العميل الدالة ويعرض الناتج.
4. **الردّ النهائي**: يقدّم الخادم الإجابة الكاملة مع
   `turnComplete: true` و`interactionStatus: "IDLE"`.

```
// 1. Spoken verbal filler while background reasoning proceeds
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "turnComplete": true,
    "interactionStatus": "IN_PROGRESS"
  }
}

// 2. Asynchronous tool call emitted with IN_PROGRESS status
{
  "toolCall": {
    "functionCalls": [
      {
        "id": "call_123",
        "name": "searchFlights",
        "args": {
          "destination": "Seattle"
        }
      }
    ]
  },
  "interactionStatus": "IN_PROGRESS"
}

// 3. Client executes function and returns result
{
  "toolResponse": {
    "functionResponses": [
      {
        "response": {
          "output": {
            "flight": "DL 145",
            "price": "$145"
          }
        },
        "id": "call_123"
      }
    ]
  }
}

// 4. Final spoken answer delivered -> session transitions to IDLE when done
{
  "serverContent": {
    "modelTurn": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "audio/pcm;rate=24000",
            "data": "..."
          }
        }
      ]
    },
    "interactionStatus": "IDLE",
    "turnComplete": true
  }
}
```

## أمثلة على تنفيذ حزمة تطوير البرامج (SDK)

توضّح الأمثلة التالية كيفية ضبط إعدادات ميزة &quot;أفكار جديدة&quot; والتعامل معها
`interaction_status` باستخدام حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.8-live-extended-thinking"

# Define non-blocking function declaration
search_flights = types.FunctionDeclaration(
    name="search_flights",
    description="Searches for available flights to a destination.",
    behavior="NON_BLOCKING",
    parameters={
        "type": "OBJECT",
        "properties": {
            "destination": {"type": "STRING"}
        },
        "required": ["destination"]
    }
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    thinking_config=types.ThinkingConfig(
        thinking_level="low"
    ),
    tools=[types.Tool(function_declarations=[search_flights])]
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session connected with Thinking")

        async for message in session.receive():
            # Inspect interaction status for server lifecycle tracking
            status = getattr(message, "interaction_status", None)
            if status:
                print(f"Interaction status: {status}")

            # Handle audio output parts
            if message.server_content and message.server_content.model_turn:
                for part in message.server_content.model_turn.parts:
                    if part.inline_data:
                        # Process 24kHz audio chunk
                        pass

            # Handle asynchronous tool call
            if message.tool_call:
                for call in message.tool_call.function_calls:
                    print(f"Executing tool: {call.name}")
                    # Simulate function execution
                    response = types.FunctionResponse(
                        id=call.id,
                        name=call.name,
                        response={"result": "Flight DL 145 ($145)"}
                    )
                    await session.send_tool_response(
                        function_responses=[response]
                    )

            # Status is IDLE when reasoning and all turns are complete
            if status == "IDLE":
                print("Session is idle and ready for user input.")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.8-live-extended-thinking';

const searchFlights = {
  name: 'search_flights',
  description: 'Searches for available flights to a destination.',
  behavior: 'NON_BLOCKING',
  parameters: {
    type: 'OBJECT',
    properties: {
      destination: { type: 'STRING' }
    },
    required: ['destination']
  }
};

const config = {
  responseModalities: [Modality.AUDIO],
  thinkingConfig: {
    thinkingLevel: 'low'
  },
  tools: [{ functionDeclarations: [searchFlights] }]
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Session connected'),
      onmessage: async (event) => {
        const message = JSON.parse(event.data);

        if (message.interactionStatus) {
          console.log(`Interaction status: ${message.interactionStatus}`);
        }

        if (message.toolCall) {
          for (const call of message.toolCall.functionCalls) {
            console.log(`Executing tool: ${call.name}`);
            session.sendToolResponse({
              functionResponses: [{
                id: call.id,
                name: call.name,
                response: { result: 'Flight DL 145 ($145)' }
              }]
            });
          }
        }

        if (message.interactionStatus === 'IDLE') {
          console.log('Session is idle and waiting for input.');
        }
      }
    }
  });
}

main();
```

## الخطوات التالية

- اطّلِع على صفحتَي نموذجَي [Gemini 3.8 Live](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=ar) و[Gemini 3.8 Live Extended Thinking](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=ar).
- راجِع جدول [مقارنة النماذج](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=ar#model-comparison) للحصول على مقارنات تفصيلية بين الميزات في جميع نماذج Live API.
- يمكنك الاطّلاع على مزيد من المعلومات حول ميزة "استدعاء الدوال" في دليل [استخدام أداة Live API Tool](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ar).
- راجِع [إدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=ar) للتعامل مع استئناف الجلسة ودورة حياة السياق.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-17 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-17 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
