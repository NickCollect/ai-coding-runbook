---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar
fetched_at: 2026-05-05T20:42:28.555092+00:00
title: "\u062a\u0648\u0642\u064a\u0639\u0627\u062a \u0627\u0644\u0623\u0641\u0643\u0627\u0631 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# توقيعات الأفكار

توقيعات الأفكار هي تمثيلات مشفّرة لعملية التفكير الداخلية للنموذج، وتُستخدَم للحفاظ على سياق التفكير في التفاعلات المتعددة الخطوات.
عند استخدام نماذج التفكير (مثل سلسلة Gemini 3 و2.5)، قد تعرض واجهة برمجة التطبيقات
حقل `thoughtSignature` ضمن [أجزاء المحتوى](https://ai.google.dev/api/caching?hl=ar#Part)
في الاستجابة (مثل أجزاء `text` أو `functionCall`).

كقاعدة عامة، إذا تلقّيت توقيع فكرة في استجابة نموذج، عليك إرجاعه تمامًا كما تلقّيته عند إرسال سجلّ المحادثة في الدور التالي.
**عند استخدام نماذج Gemini 3، عليك إرجاع توقيعات الأفكار أثناء استدعاء الدالة، وإلا سيظهر لك خطأ في التحقّق من الصحة** (رمز الحالة 4xx).
ويشمل ذلك عند استخدام إعداد مستوى الـ`minimal`
[تفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#thinking-levels) لنموذج Gemini 3
Flash.

## آلية العمل

يوضّح الرسم البياني أدناه معنى "الدور" و "الخطوة" في ما يتعلق بـ
[استدعاء الدالة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في Gemini API. "الدور" هو تبادل واحد وكامل في محادثة بين مستخدم ونموذج. "الخطوة" هي إجراء أو عملية أكثر دقة ينفّذها النموذج، غالبًا كجزء من عملية أكبر لإكمال دور.

![مخطّط بياني يوضّح خطوات استدعاء الدالة](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=ar)

*يركّز هذا المستند على معالجة استدعاء الدالة لنماذج Gemini 3. يُرجى الرجوع
إلى قسم [سلوك النموذج](#model-behavior) للاطّلاع على الاختلافات مع الإصدار 2.5.*

يعرض Gemini 3 توقيعات الأفكار لجميع استجابات النموذج (الاستجابات من واجهة برمجة التطبيقات) التي تتضمّن استدعاء دالة. تظهر توقيعات الأفكار في الحالات التالية:

- عندما تكون هناك [استدعاءات متوازية للدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#parallel_function_calling)
  ، سيحتوي جزء استدعاء الدالة الأول الذي تعرضه استجابة النموذج على
  توقيع فكرة.
- عندما تكون هناك استدعاءات متسلسلة للدوال (متعددة الخطوات)، سيحتوي كل استدعاء دالة على توقيع، وعليك إرجاع جميع التوقيعات.
- ستعرض استجابات النموذج التي لا تتضمّن استدعاء دالة توقيع فكرة داخل الجزء الأخير الذي يعرضه النموذج.

يوضّح الجدول التالي استدعاءات الدوال المتعددة الخطوات، ويجمع بين تعريفَي الأدوار والخطوات ومفهوم التوقيعات الذي تم تقديمه أعلاه:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الدور** | **الخطوة** | **طلب المستخدم** | **استجابة النموذج** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | بدون |

## التوقيعات في أجزاء استدعاء الدالة

عندما ينشئ Gemini `functionCall`، يعتمد على `thought_signature` لمعالجة ناتج الأداة بشكل صحيح في الدور التالي.

- **السلوك**:
  - **استدعاء دالة واحدة**: سيحتوي جزء `functionCall` على `thought_signature`.
  - **استدعاءات متوازية للدوال**: إذا أنشأ النموذج استدعاءات متوازية للدوال
    في استجابة، يتم إرفاق `thought_signature` **بالجزء الأول فقط**
    `functionCall` **لن** تحتوي أجزاء `functionCall` اللاحقة في الاستجابة نفسها على توقيع.
- **المتطلبات**: **عليك** إرجاع هذا التوقيع في الجزء نفسه الذي تم استلامه فيه
  عند إرسال سجلّ المحادثة مرة أخرى.
- **التحقّق من الصحة**: يتم فرض تحقّق صارم من الصحة لجميع استدعاءات الدوال ضمن
  الدور الحالي . (الدور الحالي فقط مطلوب، ولا نتحقّق من صحة الأدوار السابقة)
  - تعود واجهة برمجة التطبيقات إلى السجلّ (من الأحدث إلى الأقدم) للعثور على أحدث رسالة **مستخدم** تحتوي على محتوى عادي (مثل `text`) ( والتي ستكون بداية الدور الحالي). **be** يكون هذا الجزء `functionResponse`.
  - تُعد **جميع** أدوار `functionCall` للنموذج التي تحدث بعد رسالة الاستخدام المحددة جزءًا من الدور.
  - يجب أن يتضمّن **الجزء الأول** من `functionCall` في **كل خطوة** من الدور الحالي
    **thought\_signature**.`thought_signature`
  - إذا حذفت `thought_signature` للجزء الأول من `functionCall` في أي خطوة من الدور الحالي، سيفشل الطلب ويظهر الخطأ 400.
- **إذا لم يتم إرجاع التوقيعات المناسبة، إليك كيفية ظهور الخطأ**
  - نماذج Gemini 3: سيؤدي عدم تضمين التوقيعات إلى ظهور الخطأ 400. ستكون الصياغة على النحو التالي:
    - يفتقد استدعاء الدالة `<Function Call>` في كتلة المحتوى `<index of contents array>`
      إلى `thought_signature`. على سبيل المثال، *استدعاء
      الدالة `FC1` في كتلة المحتوى `1.` يفتقد إلى `thought_signature`.*

### مثال على استدعاء الدالة المتسلسل

يعرض هذا القسم مثالاً على استدعاءات متعددة للدوال حيث يطرح المستخدم سؤالاً معقدًا يتطلب مهام متعددة.

لنلقِ نظرة على مثال لاستدعاء الدالة المتعدد الأدوار حيث يطرح المستخدم
سؤالاً معقدًا يتطلب مهام متعددة: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الدور** | **الخطوة** | **طلب المستخدم** | **استجابة النموذج** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

يوضّح الرمز البرمجي التالي التسلسل في الجدول أعلاه.

**الدور 1، الخطوة 1 (طلب المستخدم)**

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

**الدور 1، الخطوة 1 (استجابة النموذج)**

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

**الدور 1، الخطوة 2 (استجابة المستخدم - إرسال نواتج الأداة)** بما أنّ دور المستخدم هذا لا يحتوي إلا على `functionResponse` (بدون نص جديد)، ما زلنا في الدور 1. علينا
الاحتفاظ بـ `<Signature_A>`.

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

**الدور 1، الخطوة 2 (النموذج)** يقرّر النموذج الآن حجز سيارة أجرة استنادًا إلى ناتج الأداة السابق.

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

**الدور 1، الخطوة 3 (المستخدم - إرسال ناتج الأداة)** لإرسال تأكيد حجز سيارة الأجرة، علينا تضمين التوقيعات لـ **جميع** استدعاءات الدوال في هذه الحلقة (`<Signature A>` + `<Signature B>`).

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

### مثال على استدعاء الدالة المتوازي

لنلقِ نظرة على مثال لاستدعاء الدالة المتوازي حيث يطلب المستخدم
`"Check weather in Paris and London"` لمعرفة المكان الذي يتحقّق فيه النموذج من الصحة.

| **الدور** | **الخطوة** | **طلب المستخدم** | **استجابة النموذج** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | request1="Check the weather in Paris and London" | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | request 2 **=** request1 **+** FC1 ("Paris") + signature + FC2 ("London") | text\_output  (no FCs) | None |

يوضّح الرمز البرمجي التالي التسلسل في الجدول أعلاه.

**الدور 1، الخطوة 1 (طلب المستخدم)**

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

**الدور 1، الخطوة 1 (استجابة النموذج)**

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

**الدور 1، الخطوة 2 (استجابة المستخدم - إرسال نواتج الأداة)** علينا الاحتفاظ بـ
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

قد يعرض Gemini أيضًا `thought_signatures` في الجزء الأخير من الاستجابة في الأجزاء غير التي تتضمّن استدعاء دالة.

- **السلوك**: قد يحتوي جزء المحتوى الأخير (`text, inlineData…`) الذي يعرضه الـ
  نموذج على `thought_signature`.
- **الاقتراح**: **يُنصح** بإرجاع هذه التوقيعات لضمان
  الحفاظ على جودة التفكير العالية للنموذج، خاصةً في ما يتعلق باتّباع التعليمات المعقدة
  أو محاكاة سير عمل الوكيل.
- **التحقّق من الصحة**: **لا** تفرض واجهة برمجة التطبيقات التحقّق من الصحة بشكل صارم. لن يظهر لك خطأ يمنعك من المتابعة إذا حذفتها، ولكن قد ينخفض الأداء.

### النص/الاستدلال في السياق (بدون تحقّق من الصحة)

**الدور 1، الخطوة 1 (استجابة النموذج)**

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

## التوقيعات من أجل التوافق مع OpenAI

توضّح الأمثلة التالية كيفية معالجة توقيعات الأفكار لواجهة برمجة تطبيقات إكمال المحادثة باستخدام التوافق مع [OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar).

### مثال على استدعاء الدالة المتسلسل

هذا مثال على استدعاءات متعددة للدوال حيث يطرح المستخدم سؤالاً معقدًا يتطلب مهام متعددة.

لنلقِ نظرة على مثال لاستدعاء الدالة المتعدد الأدوار حيث يطلب المستخدم `Check flight status for AA100 and book a taxi if delayed` ويمكنك الاطّلاع على ما يحدث عندما يطرح المستخدم سؤالاً معقدًا يتطلب مهام متعددة.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الدور** | **الخطوة** | **طلب المستخدم** | **استجابة النموذج** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

يوضّح الرمز البرمجي التالي التسلسل المحدّد.

**الدور 1، الخطوة 1 (طلب المستخدم)**

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

**الدور 1، الخطوة 1 (استجابة النموذج)**

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

**الدور 1، الخطوة 2 (استجابة المستخدم - إرسال نواتج الأداة)**

بما أنّ دور المستخدم هذا لا يحتوي إلا على `functionResponse` (بدون نص جديد)، ما زلنا في الدور 1 وعلينا الاحتفاظ بـ `<Signature_A>`.

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

**الدور 1، الخطوة 2 (النموذج)**

يقرّر النموذج الآن حجز سيارة أجرة استنادًا إلى ناتج الأداة السابق.

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

**الدور 1، الخطوة 3 (المستخدم - إرسال ناتج الأداة)**

لإرسال تأكيد حجز سيارة الأجرة، علينا تضمين التوقيعات لـ \*\*جميع\*\*
استدعاءات الدوال في هذه الحلقة (`<Signature A>` + `<Signature B>`).

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

### مثال على استدعاء الدالة المتوازي

لنلقِ نظرة على مثال لاستدعاء الدالة المتوازي حيث يطلب المستخدم
`"Check weather in Paris and London"` ويمكنك الاطّلاع على المكان الذي يتحقّق فيه النموذج من الصحة.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **الدور** | **الخطوة** | **طلب المستخدم** | **استجابة النموذج** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

في ما يلي الرمز البرمجي الذي يوضّح التسلسل المحدّد.

**الدور 1، الخطوة 1 (طلب المستخدم)**

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

**الدور 1، الخطوة 1 (استجابة النموذج)**

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

**الدور 1، الخطوة 2 (استجابة المستخدم - إرسال نواتج الأداة)**

عليك الاحتفاظ بـ `<Signature_A>` في الجزء الأول تمامًا كما تم استلامه.

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

1. **كيف يمكنني نقل السجلّ من نموذج مختلف إلى Gemini 3 مع جزء استدعاء دالة في الدور والخطوة الحاليَين؟ عليّ تقديم أجزاء استدعاء دالة
   لم تنشئها واجهة برمجة التطبيقات، وبالتالي لا تحتوي على توقيع فكرة مرتبط بها؟**

   على الرغم من أنّ إدخال كتل مخصّصة لاستدعاء الدالة في الطلب أمر غير مستحسَن بشدة، يمكنك في الحالات التي لا يمكن تجنّبها، مثل تزويد النموذج بمعلومات عن استدعاءات الدوال والاستجابات التي نفّذها العميل بشكل حتمي، أو نقل تتبُّع من نموذج مختلف لا يتضمّن توقيعات أفكار، ضبط التوقيعات الوهمية التالية إما `"context_engineering_is_the_way_to_go"` أو
   `"skip_thought_signature_validator"` في حقل توقيع الفكرة لتخطّي التحقّق من الصحة.
2. **أُرسِل استدعاءات وردودًا متوازية للدوال متداخلة، وتعرض واجهة برمجة التطبيقات الخطأ 400. ما السبب؟**

   عندما تعرض واجهة برمجة التطبيقات استدعاءات متوازية للدوال "FC1 + signature, FC2"، تكون استجابة المستخدم المتوقّعة هي "FC1+ signature, FC2, FR1, FR2". إذا كانت متداخلة على النحو التالي "FC1 + signature, FR1, FC2, FR2"، ستعرض واجهة برمجة التطبيقات الخطأ 400.
3. **أثناء البث، لا يعرض النموذج استدعاء دالة لا يمكنني العثور على
   توقيع الفكرة الخاص به**

   أثناء استجابة نموذج لا تحتوي على استدعاء دالة مع طلب بث، قد يعرض النموذج توقيع الفكرة في جزء يحتوي على جزء محتوى نصي فارغ. يُنصح بتحليل الطلب بالكامل إلى أن يعرض النموذج `finish_reason`.

## توقيعات الأفكار للنماذج المختلفة

[تختلف نماذج Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=ar#gemini-3) ونماذج Gemini 2.5
في سلوكها مع توقيعات الأفكار في استدعاءات الدوال:

- إذا كانت هناك استدعاءات للدوال في استجابة،
  - سيحتوي Gemini 3 دائمًا على التوقيع في الجزء الأول من استدعاء الدالة.
    **يجب** إرجاع هذا الجزء.
  - سيحتوي Gemini 2.5 على التوقيع في الجزء الأول (بغض النظر عن النوع). **يمكنك** إرجاع هذا الجزء.
- إذا لم تكن هناك استدعاءات للدوال في استجابة،
  - سيحتوي Gemini 3 على التوقيع في الجزء الأخير إذا أنشأ النموذج فكرة.
  - لن يحتوي Gemini 2.5 على توقيع في أي جزء.

يُرجى الرجوع إلى صفحة "[المفكّر](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#signatures)" للاطّلاع على مزيد من
تفاصيل المقارنة.
بالنسبة إلى نماذج Gemini 3 Image، يُرجى الاطّلاع على قسم عملية التفكير في دليل
[إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar#thinking-process).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
