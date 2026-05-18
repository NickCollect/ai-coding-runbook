---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi
fetched_at: 2026-05-18T05:15:35.747197+00:00
title: "\u0938\u094b\u091a \u0915\u0947 \u0939\u0938\u094d\u0924\u093e\u0915\u094d\u0937\u0930 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# सोच के हस्ताक्षर

**REST API का इस्तेमाल करते समय, आपको सीधे तौर पर थॉट सिग्नेचर के साथ काम करना होगा**. इसके अलावा, अगर *एक से ज़्यादा बार बातचीत करने के दौरान, मैन्युअल तरीके से बातचीत के कुछ हिस्सों को एक्सट्रैक्ट करके वापस भेजा जा रहा है*, तब भी आपको थॉट सिग्नेचर के साथ काम करना होगा.

थॉट सिग्नेचर, मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट (सुरक्षित) किए गए वर्शन होते हैं. इनका इस्तेमाल, एक से ज़्यादा चरणों वाले इंटरैक्शन में तर्क के कॉन्टेक्स्ट को बनाए रखने के लिए किया जाता है.
सोचने-समझने वाले मॉडल (जैसे, Gemini 3 और 2.5 सीरीज़) का इस्तेमाल करते समय, एपीआई जवाब के [कॉन्टेंट वाले हिस्सों](https://ai.google.dev/api/caching?hl=hi#Part) में `thoughtSignature` फ़ील्ड दिखा सकता है. उदाहरण के लिए, `text` या `functionCall` हिस्से.

सामान्य नियम के तौर पर, अगर आपको मॉडल के जवाब में थॉट सिग्नेचर मिलता है, तो आपको बातचीत के इतिहास को अगले टर्न में भेजते समय, उसे ठीक वैसे ही वापस भेजना चाहिए जैसा आपको मिला था.
**Gemini 3 मॉडल का इस्तेमाल करते समय, फ़ंक्शन कॉल के दौरान थॉट सिग्नेचर वापस पास करने होंगे. ऐसा न करने पर, आपको पुष्टि करने से जुड़ी गड़बड़ी** (4xx स्टेटस कोड) मिलेगी.
इसमें Gemini 3 Flash के लिए, `minimal`
[सोचने-समझने की क्षमता](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#thinking-levels) वाली सेटिंग का इस्तेमाल करना भी शामिल है.

## यह कैसे काम करता है

नीचे दिए गए ग्राफ़िक में, Gemini API में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi) से जुड़े "टर्न" और "चरण" का मतलब बताया गया है. "टर्न" का मतलब, उपयोगकर्ता और मॉडल के बीच हुई बातचीत में एक बार में किया गया पूरा एक्सचेंज होता है. "स्टेप" एक बारीक कार्रवाई या ऑपरेशन होता है, जिसे मॉडल पूरा करता है. अक्सर, यह किसी टर्न को पूरा करने के लिए, बड़ी प्रोसेस का हिस्सा होता है.

![फ़ंक्शन कॉल करने के टर्न और चरणों का डायग्राम](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=hi)

*इस दस्तावेज़ में, Gemini 3 मॉडल के लिए फ़ंक्शन कॉलिंग को मैनेज करने के बारे में बताया गया है. 2.5 के साथ अंतर के लिए, [मॉडल के व्यवहार](#model-behavior) सेक्शन देखें.*

Gemini 3, फ़ंक्शन कॉल के साथ, मॉडल के सभी जवाबों (एपीआई से मिले जवाब) के लिए थॉट सिग्नेचर दिखाता है. सोच से जुड़े सिग्नेचर इन मामलों में दिखते हैं:

- [पैरलल फ़ंक्शन](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#parallel_function_calling) कॉल होने पर, मॉडल के जवाब से मिले फ़ंक्शन कॉल के पहले हिस्से में थॉट सिग्नेचर होगा.
- जब फ़ंक्शन कॉल क्रम से किए जाते हैं (एक से ज़्यादा चरण), तो हर फ़ंक्शन कॉल का एक सिग्नेचर होता है. आपको सभी सिग्नेचर वापस भेजने होंगे.
- फ़ंक्शन कॉल के बिना मॉडल के जवाबों में, मॉडल से मिले जवाब के आखिरी हिस्से में थॉट सिग्नेचर दिखेगा.

यहां दी गई टेबल में, एक से ज़्यादा चरणों वाले फ़ंक्शन कॉल का विज़ुअलाइज़ेशन दिया गया है. इसमें, ऊपर बताए गए सिग्नेचर के कॉन्सेप्ट के साथ-साथ, टर्न और चरणों की परिभाषाओं को भी शामिल किया गया है:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **चालू करें** | **चरण** | **उपयोगकर्ता का अनुरोध** | **मॉडल का जवाब** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | कोई नहीं |

## फ़ंक्शन कॉल करने वाले हिस्सों में सिग्नेचर

जब Gemini कोई `functionCall` जनरेट करता है, तो वह `thought_signature` पर भरोसा करता है, ताकि अगले टर्न में टूल के आउटपुट को सही तरीके से प्रोसेस किया जा सके.

- **व्यवहार**:
  - **सिंगल फ़ंक्शन कॉल**: `functionCall` वाले हिस्से में `thought_signature` शामिल होगा.
  - **पैरलल फ़ंक्शन कॉल**: अगर मॉडल, जवाब में पैरलल फ़ंक्शन कॉल जनरेट करता है, तो `thought_signature` को **सिर्फ़ पहले**
    `functionCall` हिस्से में जोड़ा जाता है. एक ही जवाब में मौजूद बाद के `functionCall` हिस्सों में हस्ताक्षर **नहीं** होगा.
- ****ज़रूरी शर्त**: बातचीत का इतिहास वापस भेजते समय, आपको इस हस्ताक्षर को उसी जगह पर वापस भेजना होगा जहां इसे मिला था.**
- **पुष्टि करना**: मौजूदा टर्न में फ़ंक्शन कॉल के लिए, पुष्टि करने की सख्त प्रक्रिया लागू की जाती है . (सिर्फ़ मौजूदा टर्न की ज़रूरत है; हम पिछले टर्न की पुष्टि नहीं करते)
  - एपीआई, इतिहास में सबसे नए से लेकर सबसे पुराने मैसेज तक जाता है, ताकि **उपयोगकर्ता** का ऐसा सबसे हाल का मैसेज मिल सके जिसमें स्टैंडर्ड कॉन्टेंट (जैसे, `text`) शामिल हो. यह मैसेज, मौजूदा बातचीत की शुरुआत में भेजा गया होगा. यह `functionResponse` **be** होगा.
  - **सभी** मॉडल `functionCall` के लिए, इस्तेमाल से जुड़ी जानकारी देने वाले मैसेज के बाद होने वाले सभी टर्न को टर्न का हिस्सा माना जाता है.
  - मौजूदा बातचीत के **हर चरण** में, `functionCall` का **पहला** हिस्सा **ज़रूर** शामिल होना चाहिए. साथ ही, इसमें `thought_signature` भी शामिल होना चाहिए.
  - अगर मौजूदा बातचीत के किसी भी चरण में, पहले `functionCall` हिस्से के लिए `thought_signature` को शामिल नहीं किया जाता है, तो अनुरोध पूरा नहीं होगा और आपको 400 गड़बड़ी का मैसेज मिलेगा.
- **अगर सही सिग्नेचर नहीं मिलते हैं, तो यहां बताया गया है कि आपको गड़बड़ी का मैसेज कैसे दिखेगा**
  - Gemini 3 मॉडल: सिग्नेचर शामिल न करने पर, 400 गड़बड़ी दिखेगी. सूचना इस फ़ॉर्मैट में होगी:
    - `<index of contents array>` कॉन्टेंट ब्लॉक में मौजूद फ़ंक्शन कॉल `<Function Call>` में `thought_signature` मौजूद नहीं है. उदाहरण के लिए, *`1.` कॉन्टेंट ब्लॉक में फ़ंक्शन कॉल `FC1` में `thought_signature` मौजूद नहीं है.*

### फ़ंक्शन को क्रम से कॉल करने का उदाहरण

इस सेक्शन में, एक से ज़्यादा फ़ंक्शन कॉल का उदाहरण दिखाया गया है. इसमें उपयोगकर्ता एक ऐसा मुश्किल सवाल पूछता है जिसके लिए कई टास्क पूरे करने पड़ते हैं.

फ़ंक्शन कॉलिंग के एक ऐसे उदाहरण पर नज़र डालते हैं जिसमें उपयोगकर्ता कई बार बातचीत करता है. इसमें उपयोगकर्ता एक ऐसा मुश्किल सवाल पूछता है जिसके लिए कई टास्क पूरे करने पड़ते हैं: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **चालू करें** | **चरण** | **उपयोगकर्ता का अनुरोध** | **मॉडल का जवाब** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

यहां दिया गया कोड, ऊपर दी गई टेबल में दिए गए क्रम को दिखाता है.

**पहला जवाब, पहला चरण (उपयोगकर्ता का अनुरोध)**

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

**पहला जवाब, पहला चरण (मॉडल का जवाब)**

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

**पहला टर्न, दूसरा चरण (उपयोगकर्ता का जवाब - टूल के आउटपुट भेजना)** इस टर्न में सिर्फ़ `functionResponse` (कोई नया टेक्स्ट नहीं) शामिल है. इसलिए, हम अब भी पहले टर्न में हैं. हमें `<Signature_A>` को सुरक्षित रखना होगा.

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

**पहला जवाब, दूसरा चरण (मॉडल)** मॉडल अब पिछले टूल के आउटपुट के आधार पर टैक्सी बुक करने का फ़ैसला करता है.

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

**पहला जवाब, तीसरा चरण (उपयोगकर्ता - टूल का आउटपुट भेजना)** टैक्सी बुकिंग की पुष्टि भेजने के लिए, हमें इस लूप में **सभी** फ़ंक्शन कॉल के लिए हस्ताक्षर शामिल करने होंगे (`<Signature A>` + `<Signature B>`).

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

### पैरलल फ़ंक्शन कॉलिंग का उदाहरण

आइए, फ़ंक्शन को एक साथ कॉल करने का एक उदाहरण देखते हैं. इसमें उपयोगकर्ता, `"Check weather in Paris and London"` से यह पूछता है कि मॉडल कहां पुष्टि करता है.

| **चालू करें** | **चरण** | **उपयोगकर्ता का अनुरोध** | **मॉडल का जवाब** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + हस्ताक्षर  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (कोई फ़ॉन्ट कलेक्शन नहीं है) | कोई नहीं |

यहां दिया गया कोड, ऊपर दी गई टेबल में दिए गए क्रम को दिखाता है.

**पहला जवाब, पहला चरण (उपयोगकर्ता का अनुरोध)**

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

**पहला जवाब, पहला चरण (मॉडल का जवाब)**

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

**पहले राउंड का दूसरा चरण (उपयोगकर्ता का जवाब - टूल के आउटपुट भेजना)** हमें पहले हिस्से में `<Signature_A>` को ठीक उसी तरह से सुरक्षित रखना होगा जिस तरह से हमें मिला था.

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

## `functionCall` के अलावा अन्य हिस्सों में हस्ताक्षर

Gemini, फ़ंक्शन कॉल के अलावा अन्य हिस्सों में भी जवाब के आखिर में `thought_signatures` दिखा सकता है.

- **व्यवहार**: मॉडल से मिले जवाब (`text, inlineData…`) में `thought_signature` शामिल हो सकता है.
- **सुझाव**: इन सिग्नेचर को वापस लाने का **सुझाव दिया जाता है**, ताकि यह पक्का किया जा सके कि मॉडल अच्छी क्वालिटी की तार्किकता बनाए रखे. खास तौर पर, निर्देशों का पालन करने या एजेंट के तौर पर काम करने के लिए बनाए गए वर्कफ़्लो को सिम्युलेट करने के लिए.
- **पुष्टि करना**: एपीआई, पुष्टि करने की प्रोसेस को सख्ती से लागू **नहीं** करता है. अगर आपने इन कुकी को शामिल नहीं किया है, तो आपको ब्लॉक करने से जुड़ी गड़बड़ी का मैसेज नहीं मिलेगा. हालांकि, ऐसा करने से परफ़ॉर्मेंस खराब हो सकती है.

### टेक्स्ट/संदर्भ के हिसाब से तर्क (पुष्टि नहीं की गई)

**पहला जवाब, पहला चरण (मॉडल का जवाब)**

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

**दूसरा चरण, पहला चरण (उपयोगकर्ता)**

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

## OpenAI के साथ काम करने के लिए सिग्नेचर

यहां दिए गए उदाहरण में बताया गया है कि [OpenAI के साथ काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/openai?hl=hi) का इस्तेमाल करके, चैट पूरे होने के एपीआई के लिए थॉट सिग्नेचर को कैसे मैनेज किया जाता है.

### फ़ंक्शन को क्रम से कॉल करने का उदाहरण

यह एक से ज़्यादा फ़ंक्शन कॉल करने का उदाहरण है. इसमें उपयोगकर्ता एक ऐसा मुश्किल सवाल पूछता है जिसके लिए कई टास्क पूरे करने पड़ते हैं.

आइए, फ़ंक्शन कॉलिंग के एक ऐसे उदाहरण पर नज़र डालें जिसमें कई बार बातचीत की गई है. इसमें उपयोगकर्ता ने `Check flight status for AA100 and book a taxi if delayed` पूछा है. साथ ही, यह भी देखा जा सकता है कि जब उपयोगकर्ता कोई ऐसा मुश्किल सवाल पूछता है जिसके लिए कई टास्क पूरे करने पड़ते हैं, तो क्या होता है.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **चालू करें** | **चरण** | **उपयोगकर्ता का अनुरोध** | **मॉडल का जवाब** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

नीचे दिया गया कोड, दिए गए क्रम के हिसाब से काम करता है.

**पहला जवाब, पहला चरण (उपयोगकर्ता का अनुरोध)**

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

**पहला जवाब, पहला चरण (मॉडल का जवाब)**

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

**पहला राउंड, दूसरा चरण (उपयोगकर्ता का जवाब - टूल के आउटपुट भेजना)**

इस उपयोगकर्ता के टर्न में सिर्फ़ `functionResponse` (कोई नया टेक्स्ट नहीं) है. इसलिए, हम अब भी पहले टर्न में हैं और हमें `<Signature_A>` को बनाए रखना होगा.

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

**पहला जवाब, दूसरा चरण (मॉडल)**

अब मॉडल, पिछले टूल के आउटपुट के आधार पर टैक्सी बुक करने का फ़ैसला लेता है.

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

**टर्न 1, तीसरा चरण (उपयोगकर्ता - टूल का आउटपुट भेजना)**

टैक्सी बुकिंग की पुष्टि करने के लिए, हमें इस लूप (`<Signature A>` + `<Signature B>`) में सभी फ़ंक्शन कॉल के लिए हस्ताक्षर शामिल करने होंगे.

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

### पैरलल फ़ंक्शन कॉलिंग का उदाहरण

आइए, फ़ंक्शन को पैरलल तरीके से कॉल करने का एक उदाहरण देखते हैं. इसमें उपयोगकर्ता `"Check weather in Paris and London"` पूछता है और आपको पता चलता है कि मॉडल कहां पुष्टि करता है.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **चालू करें** | **चरण** | **उपयोगकर्ता का अनुरोध** | **मॉडल का जवाब** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

यहां दिए गए क्रम के हिसाब से कोड दिया गया है.

**पहला जवाब, पहला चरण (उपयोगकर्ता का अनुरोध)**

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

**पहला जवाब, पहला चरण (मॉडल का जवाब)**

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

**पहला राउंड, दूसरा चरण (उपयोगकर्ता का जवाब - टूल के आउटपुट भेजना)**

आपको `<Signature_A>` को पहले हिस्से में ठीक उसी तरह से रखना होगा जैसा आपको मिला था.

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

## अक्सर पूछे जाने वाले सवाल

1. **मैं किसी दूसरे मॉडल से Gemini 3 में चैट का इतिहास कैसे ट्रांसफ़र करूं? साथ ही, मुझे मौजूदा टर्न और चरण में फ़ंक्शन कॉल वाला हिस्सा भी ट्रांसफ़र करना है. क्या मुझे फ़ंक्शन कॉल के उन हिस्सों की जानकारी देनी होगी जिन्हें एपीआई ने जनरेट नहीं किया है और इसलिए, उनसे जुड़ा कोई थॉट सिग्नेचर नहीं है?**

   अनुरोध में कस्टम फ़ंक्शन कॉल ब्लॉक शामिल करने का सुझाव नहीं दिया जाता. हालांकि, कुछ मामलों में ऐसा करना ज़रूरी हो सकता है. जैसे, क्लाइंट की ओर से फ़ंक्शन कॉल और जवाबों के बारे में मॉडल को जानकारी देना या किसी ऐसे मॉडल से ट्रेस ट्रांसफ़र करना जिसमें थॉट सिग्नेचर शामिल नहीं हैं. ऐसे मामलों में, थॉट सिग्नेचर फ़ील्ड में `"context_engineering_is_the_way_to_go"` या `"skip_thought_signature_validator"` के ये डमी सिग्नेचर सेट किए जा सकते हैं, ताकि पुष्टि करने की प्रोसेस को स्किप किया जा सके.
2. **I am sending back interleaved parallel function calls and responses and the
   API is returning a 400. क्यों?**

   जब एपीआई, फ़ंक्शन कॉल "FC1 + हस्ताक्षर, FC2" के समानांतर जवाब देता है, तो उपयोगकर्ता से "FC1+ हस्ताक्षर, FC2, FR1, FR2" जवाब की उम्मीद की जाती है. अगर आपने उन्हें "FC1 + हस्ताक्षर, FR1, FC2, FR2" के तौर पर इंटरलीव किया है, तो एपीआई 400 गड़बड़ी दिखाएगा.
3. **स्ट्रीमिंग के दौरान, मॉडल से फ़ंक्शन कॉल नहीं मिल रहा है. साथ ही, मुझे थॉट सिग्नेचर नहीं मिल रहा है**

   स्ट्रीमिंग के अनुरोध के साथ, मॉडल के जवाब में फ़ंक्शन कॉल (एफ़सी) शामिल न होने पर, मॉडल थॉट सिग्नेचर को ऐसे हिस्से में दिखा सकता है जिसमें टेक्स्ट कॉन्टेंट वाला हिस्सा खाली हो. हमारा सुझाव है कि जब तक मॉडल `finish_reason` नहीं दिखाता, तब तक पूरे अनुरोध को पार्स करें.

## अलग-अलग मॉडल के लिए थॉट सिग्नेचर

[Gemini 3 मॉडल](https://ai.google.dev/gemini-api/docs/models?hl=hi#gemini-3) और Gemini 2.5 मॉडल, फ़ंक्शन कॉल में थॉट सिग्नेचर के साथ अलग-अलग तरीके से काम करते हैं:

- अगर किसी जवाब में फ़ंक्शन कॉल मौजूद हैं, तो
  - Gemini 3 के पहले फ़ंक्शन कॉल वाले हिस्से में हमेशा सिग्नेचर मौजूद होगा.
    उस हिस्से को वापस लाना **ज़रूरी है**.
  - Gemini 2.5 के जवाब के पहले हिस्से में हस्ताक्षर मौजूद होगा. इससे कोई फ़र्क़ नहीं पड़ता कि जवाब किस तरह का है. उस हिस्से को वापस करना **ज़रूरी नहीं है**.
- अगर किसी जवाब में फ़ंक्शन कॉल नहीं हैं, तो
  - अगर मॉडल कोई जवाब जनरेट करता है, तो Gemini 3 के जवाब के आखिर में हस्ताक्षर होगा.
  - Gemini 2.5 के जवाब में किसी भी हिस्से में हस्ताक्षर नहीं होगा.

तुलना से जुड़ी ज़्यादा जानकारी के लिए, [सोचना](https://ai.google.dev/gemini-api/docs/thinking?hl=hi#signatures) पेज देखें.
Gemini 3 Image मॉडल के लिए, [इमेज जनरेट करने](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi#thinking-process) से जुड़ी गाइड में, सोचने की प्रोसेस वाला सेक्शन देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-08 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-08 (UTC) को अपडेट किया गया."],[],[]]
