---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=ar
fetched_at: 2026-09-21T05:49:15.260170+00:00
title: "\u062a\u0648\u0642\u064a\u0639\u0627\u062a \u0627\u0644\u0623\u0641\u0643\u0627\u0631 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 3.8 Flash متاح الآن. [جرِّبه](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# توقيعات الأفكار

توقيعات الأفكار هي تمثيلات مشفّرة لعملية التفكير الداخلية التي يجريها النموذج، وتُستخدَم للحفاظ على سياق الاستدلال في التفاعلات المتعدّدة الخطوات.
عند استخدام نماذج التفكير (مثل سلسلة Gemini 3 و2.5)، قد تعرض واجهة برمجة التطبيقات الحقل `thoughtSignature` ضمن [أجزاء المحتوى](https://ai.google.dev/api/caching?hl=ar#Part) في الردّ (مثل الأجزاء `text` أو `functionCall`).

كقاعدة عامة، إذا تلقّيت توقيعًا فكريًا في ردّ نموذجي، عليك إعادة إرساله تمامًا كما تلقّيته عند إرسال سجلّ المحادثة في الدور التالي.
**عند استخدام نماذج Gemini 3، يجب إعادة توقيعات الأفكار أثناء
استدعاء الدوال، وإلا سيظهر لك خطأ في التحقّق من الصحة** (رمز الحالة 4xx).
ويشمل ذلك استخدام إعداد `minimal`
[مستوى التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#thinking-levels) في Gemini 3
Flash.

## آلية العمل

يوضّح الرسم البياني أدناه معنى "الدورة" و "الخطوة" في ما يتعلق
[باستدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في Gemini API. "الدورة" هي تبادل واحد وكامل في محادثة بين مستخدم ونموذج. "الخطوة" هي إجراء أو عملية أكثر دقة ينفّذها النموذج، وغالبًا ما تكون جزءًا من عملية أكبر لإكمال دورة المحادثة.

![مخطّط بياني يوضّح خطوات استدعاء الدالة](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=ar)

*يركّز هذا المستند على كيفية التعامل مع ميزة "استدعاء الدالة" في نماذج Gemini 3. راجِع قسم [سلوك النموذج](#model-behavior) لمعرفة التناقضات مع الإصدار 2.5.*

يعرض Gemini 3 توقيعات الأفكار لجميع ردود النموذج (الردود من واجهة برمجة التطبيقات) مع استدعاء دالة. تظهر توقيعات الأفكار في الحالات التالية:

- عندما تكون هناك طلبات [لدوال متوازية](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#parallel_function_calling)، سيحتوي الجزء الأول من طلب الدالة الذي تعرضه استجابة النموذج على توقيع فكري.
- عندما تكون هناك طلبات متسلسلة لاستدعاء الدوال (متعددة الخطوات)، سيكون لكل طلب استدعاء دالة توقيع، ويجب إعادة جميع التواقيع.
- ستعرض ردود النموذج التي لا تتضمّن استدعاء دالة توقيعًا فكريًا داخل الجزء الأخير الذي يعرضه النموذج.

يوضّح الجدول التالي تمثيلاً مرئيًا لعمليات استدعاء الدوال المتعدّدة الخطوات،
حيث يجمع بين تعريفات الأدوار والخطوات ومفهوم التوقيعات
الموضّح أعلاه:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الاستدارة** | **Step** | **طلب المستخدم** | **ردّ النموذج** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | بلا |

## التواقيع في أجزاء استدعاء الدالة

عندما ينشئ Gemini `functionCall`، يعتمد على `thought_signature`
لمعالجة نتيجة الأداة بشكل صحيح في الجولة التالية.

- **السلوك**:
  - **استدعاء دالة واحدة**: سيحتوي الجزء `functionCall` على `thought_signature`.
  - **استدعاء الدوال المتوازية**: إذا أنشأ النموذج استدعاءات دوال متوازية في ردّ، سيتم إرفاق `thought_signature` **بالجزء الأول فقط**
    `functionCall` من الرد.
    **لن** تتضمّن الأجزاء اللاحقة `functionCall` في الاستجابة نفسها توقيعًا.
- **شرط**: **يجب** إرجاع هذه التوقيع في الجزء نفسه الذي تم استلامه فيه عند إعادة إرسال سجلّ المحادثات.
- **التحقّق من الصحة**: يتم فرض التحقّق الصارم من الصحة على جميع طلبات الدوال ضمن المحادثة الحالية . (يجب إدخال الدور الحالي فقط، ولا نتحقّق من الأدوار السابقة)
  - تعود واجهة برمجة التطبيقات إلى سجلّ المحادثات (من الأحدث إلى الأقدم) للعثور على أحدث رسالة **مستخدم** تتضمّن محتوًى عاديًا (مثل `text`) ( وهي بداية الدور الحالي). لن **be** هذا `functionResponse`.
  - يتم اعتبار جميع **منعطفات** النموذج `functionCall` التي تحدث بعد رسالة الاستخدام المحددة هذه جزءًا من المنعطف.
  - يجب أن يتضمّن الجزء **الأول** `functionCall` في **كل خطوة** من الدور الحالي `thought_signature`.
  - إذا حذفت `thought_signature` من الجزء الأول `functionCall` في أي خطوة من خطوات المحادثة الحالية، سيتعذّر تنفيذ الطلب وسيظهر الخطأ 400.
- **في حال عدم عرض التواقيع الصحيحة، إليك كيفية ظهور الخطأ**
  - نماذج Gemini 3: سيؤدي عدم تضمين التواقيع إلى ظهور الخطأ 400. ستكون الصياغة على النحو التالي:
    - يفتقد استدعاء الدالة `<Function Call>` في كتلة المحتوى `<index of contents array>` إلى `thought_signature`. على سبيل المثال، *استدعاء
      الدالة `FC1` في حظر المحتوى `1.` لا يتضمّن `thought_signature`.*

### مثال على استدعاء الدوال التسلسلي

يعرض هذا القسم مثالاً على عدة طلبات لتنفيذ وظائف حيث يطرح المستخدم سؤالاً معقّدًا يتطلّب تنفيذ مهام متعددة.

لنتناول مثالاً على عملية استدعاء دالة تتضمّن عدة مراحل حيث يطرح المستخدم سؤالاً معقّدًا يتطلّب تنفيذ عدة مهام: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الاستدارة** | **Step** | **طلب المستخدم** | **ردّ النموذج** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

يوضّح الرمز التالي التسلسل في الجدول أعلاه.

**الجولة 1، الخطوة 1 (طلب المستخدم)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**الجولة 1، الخطوة 1 (ردّ نموذجي)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**الجولة 1، الخطوة 2 (ردّ المستخدم - إرسال نتائج الأدوات)** بما أنّ هذه الجولة من المحادثة تتضمّن `functionResponse` فقط (بدون نص جديد)، ما زلنا في الجولة 1. علينا الحفاظ على `<Signature_A>`.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**الجولة 1، الخطوة 2 (النموذج)** يقرّر النموذج الآن حجز سيارة أجرة استنادًا إلى
نتائج الأداة السابقة.

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**الجولة 1، الخطوة 3 (المستخدم - إرسال ناتج الأداة)** لإرسال تأكيد حجز سيارة الأجرة، يجب تضمين توقيعات **جميع** طلبات الدوال في هذه الحلقة (`<Signature A>` + `<Signature B>`).

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### مثال على استدعاء الدوال المتوازي

لنتناول مثالاً على استدعاء الدوال المتوازية حيث يطلب المستخدم من
`"Check weather in Paris and London"` معرفة المكان الذي يجري فيه النموذج عملية التحقّق من صحة البيانات.

| **الاستدارة** | **Step** | **طلب المستخدم** | **ردّ النموذج** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("باريس") + التوقيع  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (no FCs) | بلا |

يوضّح الرمز التالي التسلسل في الجدول أعلاه.

**الجولة 1، الخطوة 1 (طلب المستخدم)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**الجولة 1، الخطوة 1 (ردّ نموذجي)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**الجولة 1، الخطوة 2 (ردّ المستخدم - إرسال نتائج الأدوات)** يجب الحفاظ على
`<Signature_A>` في الجزء الأول تمامًا كما تم استلامه.

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## التوقيعات في الأجزاء غير `functionCall`

قد يعرض Gemini أيضًا `thought_signatures` في الجزء الأخير من الرد
في الأجزاء التي لا تتضمّن طلبات تنفيذ وظائف.

- **السلوك**: قد يحتوي الجزء الأخير من المحتوى (`text, inlineData…`) الذي يعرضه النموذج على `thought_signature`.
- **اقتراح**: **ننصح** بعرض هذه التواقيع لضمان
  أن يحافظ النموذج على جودة عالية في الاستدلال، خاصةً في المهام المعقدة التي تتطلّب اتّباع التعليمات
  أو محاكاة سير العمل المستند إلى الوكلاء.
- **التحقّق من الصحة**: **لا** تفرض واجهة برمجة التطبيقات التحقّق من الصحة بشكل صارم. ولن يظهر لك خطأ حظر إذا لم تدرجها، ولكن قد ينخفض الأداء.

### النص/الاستدلال في السياق (بدون التحقّق من الصحة)

**الجولة 1، الخطوة 1 (ردّ نموذجي)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**الدور 2، الخطوة 1 (المستخدم)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## توقيعات التوافق مع OpenAI

توضّح الأمثلة التالية كيفية التعامل مع توقيعات الأفكار لواجهة برمجة تطبيقات لإكمال المحادثة باستخدام [التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar).

### مثال على استدعاء الدوال التسلسلي

هذا مثال على استخدام أدوات متعددة في آن واحد، حيث يطرح المستخدم سؤالاً معقّدًا يتطلّب تنفيذ مهام متعددة.

لنتعرّف على مثال على استخدام وظائف متعددة الأدوار حيث يسأل المستخدم
`Check flight status for AA100 and book a taxi if delayed` ويمكنك الاطّلاع على ما يحدث عندما يطرح المستخدم سؤالاً معقّدًا يتطلّب تنفيذ مهام متعددة.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الاستدارة** | **Step** | **طلب المستخدم** | **ردّ النموذج** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

يتنقّل الرمز التالي خلال التسلسل المحدّد.

**الجولة 1، الخطوة 1 (طلب المستخدم)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**الجولة 1، الخطوة 1 (الردّ النموذجي)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**الجولة 1، الخطوة 2 (ردّ المستخدم - إرسال نواتج الأدوات)**

بما أنّ دور المستخدم هذا لا يحتوي إلا على `functionResponse` (بدون نص جديد)، سنبقى في الدور 1 ويجب الاحتفاظ بـ `<Signature_A>`.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**الجولة 1، الخطوة 2 (نموذج)**

يقرّر النموذج الآن حجز سيارة أجرة استنادًا إلى نتيجة الأداة السابقة.

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**الجولة 1، الخطوة 3 (المستخدم - إرسال ناتج الأداة)**

لإرسال تأكيد حجز سيارة الأجرة، يجب تضمين توقيعات لجميع استدعاءات الدوال في هذه الحلقة (`<Signature A>` + `<Signature B>`).

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### مثال على استدعاء الدوال المتوازي

لنتناول مثالاً على استدعاء الدوال المتوازية حيث يطرح المستخدم السؤال
`"Check weather in Paris and London"` ويمكنك الاطّلاع على المكان الذي يجري فيه النموذج عملية التحقّق.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الاستدارة** | **Step** | **طلب المستخدم** | **ردّ النموذج** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

في ما يلي الرمز البرمجي لتصفّح التسلسل المحدّد.

**الجولة 1، الخطوة 1 (طلب المستخدم)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**الجولة 1، الخطوة 1 (الردّ النموذجي)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**الجولة 1، الخطوة 2 (ردّ المستخدم - إرسال نواتج الأدوات)**

يجب الحفاظ على `<Signature_A>` في الجزء الأول تمامًا كما تم استلامه.

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## الأسئلة الشائعة

1. **كيف يمكنني نقل السجلّ من نموذج مختلف إلى Gemini 3 مع جزء من استدعاء دالة في الخطوة الحالية؟ هل يجب تقديم أجزاء من استدعاء الدالة لم تنشئها واجهة برمجة التطبيقات وبالتالي ليس لديها توقيع فكري مرتبط بها؟**

   مع أنّنا لا ننصح بشدة بإدخال كتل مخصّصة لاستدعاء الدوال في الطلب، يمكنك ضبط التوقيعات الوهمية التالية `"context_engineering_is_the_way_to_go"` أو `"skip_thought_signature_validator"` في حقل توقيع الفكرة لتخطّي عملية التحقّق في الحالات التي لا يمكن تجنُّب ذلك فيها، مثلاً عند تقديم معلومات للنموذج عن استدعاءات الدوال والردود التي نفّذها العميل بشكل حتمي، أو عند نقل عملية تتبُّع من نموذج مختلف لا يتضمّن توقيعات الأفكار.
2. **أرسلُ طلبات استدعاء دالات متوازية متداخلة وردودًا، ويتلقّى واجهة برمجة التطبيقات الرمز 400. ما السبب؟**

   عندما تعرض واجهة برمجة التطبيقات استدعاءات دالات متوازية "FC1 + التوقيع، FC2"، تكون استجابة المستخدم المتوقّعة هي "FC1 + التوقيع، FC2، FR1، FR2". إذا كانت البيانات متداخلة على النحو التالي: "FC1 + signature, FR1, FC2, FR2"، ستعرض واجهة برمجة التطبيقات الخطأ 400.
3. **عند البث وعدم عرض النموذج لطلب دالة، لا يمكنني العثور على
   توقيع الفكرة**

   خلال استجابة نموذج لا تحتوي على مكالمة وظيفة مع طلب بث، قد يعرض النموذج توقيع الفكرة في جزء يتضمّن جزءًا فارغًا من محتوى النص. يُنصح بتحليل الطلب بأكمله إلى أن يعرض النموذج `finish_reason`.

## توقيعات الأفكار لنماذج مختلفة

تتصرّف [نماذج Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-3) ونماذج Gemini 2.5 بشكل مختلف مع توقيعات الأفكار في عمليات استدعاء الدوال:

- إذا كانت هناك استدعاءات للدوال في الرد،
  - سيحتوي Gemini 3 دائمًا على التوقيع في الجزء الأول من استدعاء الدالة.
    **يجب** إرجاع هذا الجزء.
  - سيتضمّن Gemini 2.5 التوقيع في الجزء الأول (بغض النظر عن النوع). **يمكنك** إرجاع هذا الجزء.
- إذا لم تتضمّن الاستجابة أي طلبات وظائف،
  - سيحتوي Gemini 3 على التوقيع في الجزء الأخير إذا أنشأ النموذج فكرة.
  - لن يتضمّن Gemini 2.5 توقيعًا في أي جزء.

يمكنك الرجوع إلى صفحة [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#signatures) للاطّلاع على مزيد من التفاصيل حول المقارنة.
بالنسبة إلى نماذج Gemini 3 Image، يُرجى الاطّلاع على قسم "عملية التفكير" في دليل [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#thinking-process).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-08 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-08 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
