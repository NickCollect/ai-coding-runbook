---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=ar
fetched_at: 2026-05-05T20:02:27.362653+00:00
title: "\u0627\u0633\u062a\u062f\u0639\u0627\u0621 \u0627\u0644\u062f\u0648\u0627\u0644\u0651 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# استدعاء الدوالّ باستخدام Gemini API

تتيح لك ميزة "استدعاء الدوال" ربط النماذج بالأدوات وواجهات برمجة التطبيقات الخارجية.
وبدلاً من إنشاء ردود نصية، يحدّد النموذج الوقت المناسب لاستدعاء وظائف معيّنة ويقدّم المَعلمات اللازمة لتنفيذ إجراءات واقعية.
يتيح ذلك للنموذج أن يكون بمثابة جسر بين اللغة الطبيعية والإجراءات والبيانات في العالم الحقيقي. تتضمّن ميزة "استدعاء الدالة" 3 حالات استخدام أساسية:

- **تعزيز المعرفة:** الوصول إلى المعلومات من مصادر خارجية، مثل قواعد البيانات وواجهات برمجة التطبيقات وقواعد المعلومات
- **توسيع الإمكانات:** يمكنك استخدام أدوات خارجية لإجراء العمليات الحسابية وتوسيع حدود النموذج، مثل استخدام آلة حاسبة أو إنشاء رسومات بيانية.
- **اتّخاذ إجراءات:** التفاعل مع الأنظمة الخارجية باستخدام واجهات برمجة التطبيقات، مثل تحديد المواعيد أو إنشاء الفواتير أو إرسال الرسائل الإلكترونية أو التحكّم في الأجهزة المنزلية الذكية

الاطّلاع على أحوال الطقس
تحديد موعد اجتماع
إنشاء رسم بياني

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{
      functionDeclarations: [scheduleMeetingFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "schedule_meeting",
            "description": "Schedules a meeting with specified attendees at a given time and date.",
            "parameters": {
              "type": "object",
              "properties": {
                "attendees": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of people attending the meeting."
                },
                "date": {
                  "type": "string",
                  "description": "Date of the meeting (e.g., '2024-07-29')"
                },
                "time": {
                  "type": "string",
                  "description": "Time of the meeting (e.g., '15:00')"
                },
                "topic": {
                  "type": "string",
                  "description": "The subject or topic of the meeting."
                }
              },
              "required": ["attendees", "date", "time", "topic"]
            }
          }
        ]
      }
    ]
  }'
```

## طريقة عمل ميزة "استدعاء الدوال"

![نظرة عامة حول ميزة &quot;استدعاء الدالة&quot;](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=ar)

تتضمّن ميزة "استدعاء الدوال" تفاعلاً منظَّمًا بين تطبيقك والنموذج والدوال الخارجية. في ما يلي تفاصيل العملية:

1. **تحديد تعريف الدالة:** حدِّد تعريف الدالة في الرمز البرمجي لتطبيقك. تصف "تعريفات الدوال" اسم الدالة ومعلماتها والغرض منها للنموذج.
2. **استدعاء واجهة برمجة التطبيقات باستخدام تعريفات الدوال:** أرسِل طلب المستخدم مع تعريفات الدوال إلى النموذج. ويحلّل الطلب ويحدّد ما إذا كان استدعاء دالة سيكون مفيدًا. إذا كان الأمر كذلك، يستجيب النموذج بكائن JSON منظَّم يحتوي على اسم الدالة والمعلَمات ومعرّف فريد `id`
   (تعرض واجهة برمجة التطبيقات هذا المعرّف `id` دائمًا لطُرز Gemini 3\*).
3. **تنفيذ رمز الدالة (مسؤوليتك):** *لا* ينفّذ النموذج الدالة نفسها. يقع على عاتق تطبيقك مسؤولية معالجة الرد والتحقّق من وجود طلب استدعاء دالة. If
   - **نعم**: استخرِج الاسم والوسيطات و`id` الخاصة بالدالة ونفِّذ الدالة المقابلة في تطبيقك.
   - **لا:** قدّم النموذج ردًا نصيًا مباشرًا على الطلب
     (لا يتم التركيز على هذا المسار في المثال، ولكنّه نتيجة محتملة).
4. **إنشاء ردّ سهل الاستخدام:** إذا تم تنفيذ دالة، سجِّل النتيجة وأرسِلها مرة أخرى إلى النموذج، مع الحرص على تضمين `id` المطابق، وذلك في دورة لاحقة من المحادثة. سيستخدم النموذج النتيجة
   لإنشاء ردّ نهائي سهل الاستخدام يتضمّن المعلومات
   من استدعاء الدالة.

يمكن تكرار هذه العملية عدة مرات، ما يتيح إجراء تفاعلات وعمليات سير عمل معقّدة. يتيح النموذج أيضًا استدعاء دوال متعددة
في دورة واحدة ([استدعاء الدوال بالتوازي](#parallel_function_calling))،
وبالتسلسل ([استدعاء الدوال التركيبي](#compositional_function_calling))،
ومع أدوات Gemini المضمّنة ([استخدام أدوات متعددة](#native-tools)).

\* **ربط معرّفات الدوال دائمًا:** يعرض Gemini 3 الآن دائمًا معرّفًا فريدًا
`id` مع كل `functionCall`. أدرِج هذا `id` بالضبط في `functionResponse` حتى يتمكّن النموذج من ربط النتيجة بالطلب الأصلي بدقة.

### الخطوة 1: تحديد تعريف دالة

حدِّد دالة وبيانها ضمن الرمز البرمجي لتطبيقك يسمح للمستخدمين بضبط قيم الإضاءة وإجراء طلب بيانات من واجهة برمجة التطبيقات. يمكن أن تستدعي هذه الدالة خدمات أو واجهات برمجة تطبيقات خارجية.

### Python

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}
```

### الخطوة 2: استدعاء النموذج باستخدام تعريفات الدوال

بعد تحديد تعريفات الدوال، يمكنك أن تطلب من النموذج استخدامها. ويحلّل الطلب وتعريفات الدوال ويقرّر ما إذا كان سيردّ مباشرةً أو سيستدعي دالة. إذا تم استدعاء دالة، سيحتوي عنصر الاستجابة على اقتراح باستدعاء دالة.

### Python

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [
    types.Content(
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]
    )
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{
    functionDeclarations: [setLightValuesFunctionDeclaration]
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [
  {
    role: 'user',
    parts: [{ text: 'Turn the lights down to a romantic level' }]
  }
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

بعد ذلك، يعرض النموذج كائن `functionCall` في مخطط متوافق مع OpenAPI يحدّد كيفية طلب إحدى الدوال المحدّدة أو أكثر من أجل الرد على سؤال المستخدم.

### Python

```
id='8f2b1a3c' args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

### JavaScript

```
{
  id: '8f2b1a3c',
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}
```

### الخطوة 3: تنفيذ رمز الدالة set\_light\_values

استخرِج تفاصيل طلب استدعاء الدالة من ردّ النموذج، وحلِّل الوسيطات، ونفِّذ الدالة `set_light_values`.

### Python

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### الخطوة 4: إنشاء ردّ سهل الاستخدام يتضمّن نتيجة الدالة واستدعاء النموذج مرة أخرى

أخيرًا، أرسِل نتيجة تنفيذ الدالة إلى النموذج ليتمكّن من دمج هذه المعلومات في الرد النهائي الذي يقدّمه للمستخدم.

### Python

```
from google import genai
from google.genai import types

# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
    id=tool_call.id,
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

client = genai.Client()
final_response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=config,
    contents=contents,
)

print(final_response.text)
```

### JavaScript

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result },
  id: tool_call.id
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

بهذا تنتهي عملية استدعاء الدوال. استخدم النموذج الدالة
`set_light_values` بنجاح لتنفيذ الإجراء المطلوب من المستخدم.

## تعريفات الدوال

عند تنفيذ ميزة "استدعاء الدوال" في طلب، يمكنك إنشاء عنصر `tools` يحتوي على عنصر `function declarations` واحد أو أكثر. يمكنك تحديد الدوال باستخدام JSON، وتحديدًا باستخدام [مجموعة فرعية من select](https://ai.google.dev/api/caching?hl=ar#Schema) من تنسيق [مخطط OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). يمكن أن يتضمّن تعريف الدالة الواحدة المَعلمات التالية:

- ‫`name` (string): اسم فريد للدالة (`get_weather_forecast`،
  `send_email`). استخدِم أسماء وصفية بدون مسافات أو أحرف خاصة
  (استخدِم الشرطات السفلية أو camelCase).
- `description` (سلسلة): شرح واضح ومفصّل للغرض من الدالة وإمكاناتها. هذا الإجراء ضروري لكي يفهم النموذج متى يجب استخدام الدالة. كن محدّدًا وقدِّم أمثلة إذا كان ذلك مفيدًا ("يعثر على دور السينما استنادًا إلى الموقع الجغرافي وعنوان الفيلم اختياريًا، والذي يتم عرضه حاليًا في دور السينما").
- `parameters` (كائن): يحدّد مَعلمات الإدخال التي تتوقّعها الدالة.
  - `type` (سلسلة): تحدّد نوع البيانات العام، مثل `object`.
  - ‫`properties` (عنصر): يدرج المَعلمات الفردية، ويتضمّن كل منها ما يلي:
    - `type` (سلسلة): نوع بيانات المَعلمة، مثل `string` أو `integer` أو `boolean, array`
    - ‫`description` (سلسلة): وصف لغرض المَعلمة وتنسيقها. قدِّم أمثلة وقيودًا ("المدينة والولاية،
      مثل 'سان فرانسيسكو، كاليفورنيا' أو رمز بريدي مثل '95616'").
    - ‫`enum` (مصفوفة، اختياري): إذا كانت قيم المَعلمات من مجموعة ثابتة، استخدِم "enum" لإدراج القيم المسموح بها بدلاً من مجرد وصفها في الوصف. يؤدي ذلك إلى تحسين الدقة ("enum":
      ["daylight", "cool", "warm"]).
  - ‫`required` (مصفوفة): مصفوفة من السلاسل النصية تسرد أسماء المَعلمات التي يجب توفّرها لكي تعمل الدالة.

يمكنك أيضًا إنشاء `FunctionDeclarations` من دوال Python مباشرةً باستخدام
`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## استدعاء الدوال باستخدام نماذج التفكير

تستخدم نماذج Gemini 3 و2.5 سلسلة عملية ["تفكير"](https://ai.google.dev/gemini-api/docs/thinking?hl=ar) داخلية للاستدلال على الطلبات. يؤدي ذلك إلى تحسين أداء ميزة &quot;استدعاء الدوال&quot; بشكل كبير، ما يسمح للنموذج بتحديد الوقت المناسب لاستدعاء دالة معيّنة والمعلَمات التي يجب استخدامها. بما أنّ Gemini API لا يحتفظ بأي بيانات، تستخدم النماذج [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) للحفاظ على السياق في المحادثات المتعددة الأدوار.

يتناول هذا القسم الإدارة المتقدّمة لتوقيعات الأفكار، ولا يكون ضروريًا إلا إذا كنت تنشئ طلبات واجهة برمجة التطبيقات يدويًا (مثل REST) أو تتلاعب بسجلّ المحادثات.

**إذا كنت تستخدم [حِزم تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي](https://ai.google.dev/gemini-api/docs/libraries?hl=ar) (مكتباتنا الرسمية)، لن تحتاج إلى إدارة هذه العملية**. تتولّى حِزم تطوير البرامج (SDK) تلقائيًا تنفيذ الخطوات اللازمة، كما هو موضّح في [المثال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-4) السابق.

### إدارة سجلّ المحادثات يدويًا

في حال تعديل سجلّ المحادثات يدويًا، بدلاً من إرسال [الردّ السابق الكامل](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-4)، عليك التعامل بشكل صحيح مع `thought_signature` المضمّن في ردّ النموذج.

اتّبِع هذه القواعد لضمان الحفاظ على سياق النموذج:

- يجب دائمًا إرسال `thought_signature` مرة أخرى إلى النموذج داخل [`Part`](https://ai.google.dev/api?hl=ar#request-body-structure) الأصلي.
- **احرص دائمًا على تضمين `id` نفسه من `function_call` في `function_response`، كي تتمكّن واجهة برمجة التطبيقات من ربط النتيجة بالطلب الصحيح.**
- لا تدمج `Part` تحتوي على توقيع مع `Part` لا تحتوي على توقيع. يؤدي ذلك إلى
  إزالة السياق الموضعي للفكرة.
- لا تدمج بين ملفَي `Parts` يحتويان على تواقيع، لأنّه لا يمكن دمج سلاسل التواقيع.

#### توقيعات أفكار Gemini 3

في Gemini 3، قد يحتوي أي [`Part`](https://ai.google.dev/api?hl=ar#request-body-structure) من ردّ النموذج
على توقيع فكري.
على الرغم من أنّنا ننصح بشكل عام بعرض التوقيعات من جميع أنواع `Part`، إلا أنّ عرض توقيعات الأفكار إلزامي عند استخدام ميزة "استدعاء الدوال". ما لم يتم التلاعب بسجلّ المحادثات يدويًا، ستتعامل حزمة تطوير البرامج (SDK) من Google للذكاء الاصطناعي التوليدي مع توقيعات الأفكار تلقائيًا.

إذا كنت تتلاعب بسجلّ المحادثات يدويًا، يُرجى الرجوع إلى صفحة [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) للحصول على إرشادات وتفاصيل كاملة حول كيفية التعامل مع توقيعات الأفكار في Gemini 3.

##### فحص توقيعات الأفكار

مع أنّ ذلك ليس ضروريًا، يمكنك فحص الردّ للاطّلاع على
`thought_signature` لأغراض تصحيح الأخطاء أو تعليمية.

### Python

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))
```

### JavaScript

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}
```

يمكنك الاطّلاع على مزيد من المعلومات حول القيود والاستخدامات المتعلقة بالتوقيعات الفكرية ونماذج التفكير بشكل عام في صفحة [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar#signatures).

## استدعاء الدوال بشكل متوازٍ

بالإضافة إلى استدعاء الدوال في دورة واحدة، يمكنك أيضًا استدعاء دوال متعددة في الوقت نفسه. تتيح لك ميزة "تنفيذ الدوال بالتوازي" تنفيذ دوال متعددة في الوقت نفسه، ويتم استخدامها عندما لا تكون الدوال معتمدة على بعضها البعض. ويكون ذلك مفيدًا في سيناريوهات مثل جمع البيانات من مصادر مستقلة متعددة، مثل استرداد تفاصيل العملاء من قواعد بيانات مختلفة أو التحقّق من مستويات المخزون في مستودعات مختلفة أو تنفيذ إجراءات متعددة مثل تحويل شقتك إلى ديسكو.

عندما يبدأ النموذج عدة طلبات استدعاء للدوال في دورة واحدة، ليس عليك عرض كائنات `function_result` بالترتيب نفسه الذي تم استلام كائنات `function_call` به. تربط Gemini API كل نتيجة بالطلب المقابل باستخدام `id` من ناتج النموذج. يتيح لك ذلك تنفيذ الدوال بشكل غير متزامن وإلحاق النتائج بقائمتك عند اكتمالها.

### Python

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}
```

### JavaScript

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
  }
};
```

اضبط وضع "استدعاء الدوال" للسماح باستخدام جميع الأدوات المحدّدة.
لمزيد من المعلومات، يمكنك الاطّلاع على مقالة [ضبط ميزة "استدعاء الدوال"](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#function_calling_modes).

### Python

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-3-flash-preview", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args}) - ID: {fn.id}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{
        functionDeclarations: houseFns
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-3-flash-preview',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args}) - ID: ${fn.id}`);
}
```

تعكس كل نتيجة مطبوعة استدعاءً واحدًا للدالة قد طلبه النموذج. لإعادة إرسال النتائج، يجب تضمين الردود بالترتيب نفسه الذي تم طلبها به.

يتيح حزمة تطوير البرامج (SDK) الخاصة بلغة Python [استدعاء الدوال تلقائيًا](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#automatic_function_calling_python_only)،
ما يؤدي إلى تحويل دوال Python تلقائيًا إلى تعريفات، والتعامل مع دورة التنفيذ والاستجابة لطلب استدعاء الدالة. في ما يلي مثال على حالة استخدام &quot;الديسكو&quot;.

### Python

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## استدعاء الدوال التركيبية

تتيح ميزة &quot;استدعاء الدوال التركيبي أو التسلسلي&quot; لـ Gemini ربط عدة استدعاءات للدوال معًا لتلبية طلب معقّد. على سبيل المثال، للإجابة عن السؤال "ما هي درجة الحرارة في موقعي الجغرافي الحالي؟"، قد تستدعي Gemini API أولاً الدالة `get_current_location()`، ثم الدالة `get_weather()` التي تأخذ الموقع الجغرافي كمعلَمة.

يوضّح المثال التالي كيفية تنفيذ استدعاء الدوال التركيبية باستخدام حزمة تطوير البرامج (SDK) للغة Python واستدعاء الدوال التلقائي.

### Python

يستخدم هذا المثال ميزة استدعاء الدوال التلقائي في
`google-genai` Python SDK. تحوّل حزمة تطوير البرامج (SDK) تلقائيًا دوال Python إلى المخطط المطلوب، وتنفّذ طلبات الدوال عند طلبها من النموذج، وترسل النتائج مرة أخرى إلى النموذج لإكمال المهمة.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**الناتج المتوقّع**

عند تشغيل الرمز، ستلاحظ أنّ حزمة تطوير البرامج (SDK) تنظّم عمليات استدعاء الدوال. يستدعي النموذج أولاً `get_weather_forecast`، ويتلقّى درجة الحرارة، ثم يستدعي `set_thermostat_temperature` بالقيمة الصحيحة استنادًا إلى المنطق الوارد في الطلب.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

يوضّح هذا المثال كيفية استخدام حزمة تطوير البرامج (SDK) المستندة إلى JavaScript/TypeScript لتنفيذ استدعاءات الدوال التركيبية باستخدام حلقة تنفيذ يدوية.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [
  {
    functionDeclarations: [
      {
        name: "get_weather_forecast",
        description:
          "Gets the current weather temperature for a given location.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            location: {
              type: Type.STRING,
            },
          },
          required: ["location"],
        },
      },
      {
        name: "set_thermostat_temperature",
        description: "Sets the thermostat to a desired temperature.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            temperature: {
              type: Type.NUMBER,
            },
          },
          required: ["temperature"],
        },
      },
    ],
  },
];

// Prompt for the model
let contents = [
  {
    role: "user",
    parts: [
      {
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
      },
    ],
  },
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
      id: functionCall.id,
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [
        {
          functionCall: functionCall,
        },
      ],
    });
    contents.push({
      role: "user",
      parts: [
        {
          functionResponse: functionResponsePart,
        },
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}
```

**الناتج المتوقّع**

عند تشغيل الرمز، ستلاحظ أنّ حزمة تطوير البرامج (SDK) تنظّم عمليات استدعاء الدوال. يستدعي النموذج أولاً `get_weather_forecast`، ويتلقّى درجة الحرارة، ثم يستدعي `set_thermostat_temperature` بالقيمة الصحيحة استنادًا إلى المنطق الوارد في الطلب.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

استدعاء الدوال التركيبية هو إحدى الميزات الأصلية في [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=ar). وهذا يعني أنّ Live API يمكنها التعامل مع استدعاء الدوال بشكل مشابه لحزمة تطوير البرامج (SDK) في Python.

### Python

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [
    {'code_execution': {}},
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}
]

await run(prompt, tools=tools, modality="AUDIO")
```

### JavaScript

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [
  { codeExecution: {} },
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }
];

await run(prompt, tools=tools, modality="AUDIO")
```

## أوضاع استدعاء الدالة

تتيح لك Gemini API التحكّم في طريقة استخدام النموذج للأدوات المقدَّمة (تعريفات الدوال). على وجه التحديد، يمكنك ضبط الوضع ضمن
`function_calling_config`.

- ‫`VALIDATED`: الوضع التلقائي لدمج الأدوات (عند تفعيل الأدوات المضمّنة أو النتائج المنظَّمة أيضًا). يقتصر النموذج على توقّع إما طلبات الدوال أو اللغة الطبيعية، ويضمن الالتزام بمخطط الدوال. في حال عدم توفير `allowed_function_names`، يختار النموذج من جميع تعريفات الدوال المتاحة. إذا تم توفير `allowed_function_names`، يختار النموذج من مجموعة الدوال المسموح بها. يقلّل هذا الوضع من عدد طلبات الدوال غير الصالحة (مقارنةً بالوضع `AUTO`).
- ‫`AUTO`: الوضع التلقائي عند تفعيل أداة function\_declarations فقط
  يقرّر النموذج ما إذا كان سينشئ ردًا بلغة طبيعية أو سيقترح استدعاء دالة استنادًا إلى الطلب والسياق.
- `ANY`: يكون النموذج مقيّدًا بالتوقّع دائمًا لاستدعاء دالة، ويضمن الالتزام بمخطط الدالة. إذا لم يتم تحديد `allowed_function_names`، يمكن للنموذج الاختيار من أي من تعريفات الدوال المقدَّمة.
  إذا تم تقديم `allowed_function_names` كقائمة، يمكن للنموذج الاختيار فقط من الدوال في تلك القائمة. استخدِم هذا الوضع عندما تحتاج إلى ردّ على طلب تنفيذ دالة
  لكل طلب (إذا كان ذلك منطبقًا).
- ‫`NONE`: *محظور* على النموذج إجراء استدعاءات الدوال. وهذا الإجراء يعادل إرسال طلب بدون أي تعريفات للدوال. يمكنك استخدام هذه السمة لإيقاف ميزة "استدعاء الدوال" مؤقتًا بدون إزالة تعريفات الأدوات.

### Python

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)
```

### JavaScript

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};
```

## استدعاء الدالة تلقائيًا (في Python فقط)

عند استخدام حزمة تطوير البرامج (SDK) الخاصة بلغة Python، يمكنك تقديم دوال Python مباشرةً كأدوات.
تحوّل حزمة تطوير البرامج (SDK) هذه الدوال إلى تعريفات، وتدير عملية تنفيذ استدعاء الدالة، وتتعامل مع دورة الاستجابة نيابةً عنك. حدِّد الدالة باستخدام تلميحات الأنواع وسلسلة التوثيق. للحصول على أفضل النتائج، ننصحك باستخدام
[سلاسل مستندات بتنسيق Google.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
سيقوم حِزمة تطوير البرامج (SDK) بعد ذلك تلقائيًا بما يلي:

1. رصد الردود على استدعاءات الدوال من النموذج
2. استدعِ دالة Python المناسبة في الرمز البرمجي.
3. إرسال ردّ الدالة إلى النموذج
4. عرض الردّ النصي النهائي للنموذج

لا تحلّل حزمة تطوير البرامج (SDK) حاليًا أوصاف الوسيطات إلى خانات وصف السمة في تعريف الدالة الذي تم إنشاؤه. بدلاً من ذلك، يرسل السلسلة بأكملها كوصف للدالة ذات المستوى الأعلى.

### Python

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

يمكنك إيقاف استدعاء الدوال التلقائي باستخدام:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### بيان مخطط الدالة التلقائي

يمكن لواجهة برمجة التطبيقات وصف أي من الأنواع التالية. يُسمح باستخدام أنواع `Pydantic`، طالما أنّ الحقول المحدّدة فيها تتألف أيضًا من أنواع مسموح بها. لا تتوافق أنواع القواميس (مثل `dict[str: int]`) مع هذه الميزة، لذا لا تستخدمها.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

للاطّلاع على شكل المخطط الاستنتاجي، يمكنك تحويله باستخدام
[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

### Python

```
from google import genai
from google.genai import types

def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

client = genai.Client()
fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())
```

## استخدام أدوات متعددة: الجمع بين الأدوات المضمّنة وميزة "استدعاء الدوال"

يمكنك تفعيل أدوات متعددة، والجمع بين الأدوات المضمّنة واستدعاء الدوال في الطلب نفسه.

يمكن لنماذج Gemini 3 الجمع بين الأدوات المضمّنة وميزة &quot;استدعاء الدوال&quot; الجاهزة للاستخدام، وذلك بفضل ميزة &quot;تداول سياق الأداة&quot;. يمكنك الاطّلاع على صفحة [الجمع بين الأدوات المضمّنة واستدعاء الدوال](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar) لمزيد من المعلومات.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

بالنسبة إلى النماذج التي تسبق سلسلة Gemini 3، استخدِم [Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ar).

## استجابات الوظائف المتعددة الوسائط

بالنسبة إلى نماذج سلسلة Gemini 3، يمكنك تضمين محتوى متعدد الوسائط في أجزاء استجابة الدالة التي ترسلها إلى النموذج. يمكن للنموذج معالجة هذا المحتوى المتعدد الوسائط في دوره التالي لتقديم ردّ أكثر دقة.
تتوفّر أنواع MIME التالية للمحتوى المتعدد الوسائط في ردود الدوال:

- **الصور**: `image/png` و`image/jpeg` و`image/webp`
- **المستندات**: `application/pdf`، `text/plain`

لتضمين بيانات متعددة الوسائط في ردّ الدالة، أدرِجها كجزء واحد أو أكثر من الأجزاء المضمّنة في الجزء `functionResponse`. يجب أن يحتوي كل جزء متعدد الوسائط على `inlineData`. إذا أشرت إلى جزء متعدد الوسائط من داخل حقل `response` الخاص بالبيانات المنظَّمة، يجب أن يحتوي على `displayName` فريد.

يمكنك أيضًا الإشارة إلى جزء متعدد الوسائط من داخل حقل `response` المنظَّم الخاص بالجزء `functionResponse` باستخدام تنسيق مرجع JSON `{"$ref": "<displayName>"}`. يستبدل النموذج المرجع بالمحتوى المتعدد الوسائط عند معالجة الرد. يمكن الإشارة إلى كل `displayName` مرة واحدة فقط في الحقل `response` المنظَّم.

يعرض المثال التالي رسالة تحتوي على `functionResponse` لوظيفة باسم `get_image` وجزء مضمّن يحتوي على بيانات صورة مع `displayName: "instrument.jpg"`. يشير الحقل `response` الخاص بـ `functionResponse` إلى جزء الصورة هذا:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          id=function_call.id,
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'user',
    parts: [
      {
        functionResponse: {
          id: functionCall.id,
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData]
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "id": "UNIQUE_CALL_ID_HERE",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

## استدعاء الدالة مع الناتج المنظَّم

بالنسبة إلى طُرز سلسلة Gemini 3، يمكنك استخدام ميزة &quot;استدعاء الدوال&quot; مع
[الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar). يتيح ذلك للنموذج توقّع استدعاءات الدوال أو النتائج التي تلتزم بمخطط معيّن. نتيجةً لذلك، ستتلقّى ردودًا منسَّقة بشكل متّسق عندما لا ينشئ النموذج استدعاءات الدوال.

## بروتوكول سياق النموذج (MCP)

[بروتوكول سياق النموذج (MCP)](https://modelcontextprotocol.io/introduction) هو معيار مفتوح المصدر لربط تطبيقات الذكاء الاصطناعي بالأدوات والبيانات الخارجية.
يوفر بروتوكول سياق النموذج المُدار (MCP) بروتوكولاً مشتركًا للنماذج للوصول إلى السياق، مثل الدوال (الأدوات) أو مصادر البيانات (الموارد) أو الطلبات المحدّدة مسبقًا.

تتضمّن حِزم تطوير البرامج (SDK) من Gemini إمكانية استخدام MCP، ما يقلّل من رمز النص النموذجي ويوفّر ميزة [استدعاء الأدوات تلقائيًا](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#automatic_function_calling_python_only) لأدوات MCP. عندما ينشئ النموذج طلبًا لاستخدام أداة MCP، يمكن لحزمة تطوير البرامج (SDK) الخاصة بلغة Python وJavaScript تنفيذ أداة MCP تلقائيًا وإرسال الردّ إلى النموذج في طلب لاحق، مع مواصلة هذه العملية إلى أن يتوقف النموذج عن إرسال طلبات لاستخدام الأدوات.

في ما يلي مثال على كيفية استخدام خادم MCP محلي مع Gemini و`mcp` SDK.

### Python

تأكَّد من تثبيت أحدث إصدار من
[حزمة تطوير البرامج (SDK)](https://modelcontextprotocol.io/introduction) على
النظام الأساسي الذي تختاره.`mcp`

```
pip install mcp
```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```

### JavaScript

تأكَّد من تثبيت أحدث إصدار من حزمة تطوير البرامج (SDK) `mcp` على المنصة التي تختارها.

```
npm install @modelcontextprotocol/sdk
```

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();
```

### القيود المفروضة على التوافق المضمّن مع منصّات إدارة الموافقة

تتوفّر ميزة دعم MCP المضمّنة [تجريبيًا](https://ai.google.dev/gemini-api/docs/models?hl=ar#preview) في حِزم SDK، وتخضع للقيود التالية:

- تتوفّر الأدوات فقط، وليس المراجع أو الطلبات
- تتوفّر هذه الميزة لحزمة تطوير البرامج (SDK) الخاصة بلغة Python وJavaScript/TypeScript.
- قد تحدث تغييرات غير متوافقة مع الإصدارات السابقة في الإصدارات المستقبلية.

يمكنك دائمًا دمج خوادم MCP يدويًا إذا كانت هذه الخوادم تفرض قيودًا على ما تنشئه.

## النماذج المتوافقة

يسرد هذا القسم النماذج وإمكاناتها في استدعاء الدوال. ولا يشمل ذلك النماذج التجريبية. يمكنك الاطّلاع على نظرة عامة شاملة حول الإمكانات في صفحة [نظرة عامة على النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | استدعاء الدالة | استدعاء الدوال بشكل متوازٍ | استدعاء الدوال التركيبية |
| --- | --- | --- | --- |
| [إصدار تجريبي من Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ | ✔️ | ✔️ |
| [معاينة Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=ar) | ✔️ | ✔️ | ✔️ |
| [معاينة Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ | ✔️ | ✔️ |
| [‫Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ | ✔️ | ✔️ |
| [‫2.0 Flash في Gemini](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=ar) | ✔️ | ✔️ | ✔️ |

## أفضل الممارسات

- **أوصاف الوظائف والمَعلمات:** يجب أن تكون أوصافك واضحة ودقيقة للغاية. ويعتمد النموذج على هذه المعلومات لاختيار الوظيفة الصحيحة وتقديم الوسيطات المناسبة.
- **التسمية:** استخدِم أسماء دوال وصفية (بدون مسافات أو نقاط أو شرطات).
- **الكتابة القوية:** استخدِم أنواعًا محدّدة (عدد صحيح، سلسلة، تعداد) للمَعلمات
  للحدّ من الأخطاء. إذا كانت إحدى المَعلمات تتضمّن مجموعة محدودة من القيم الصالحة، استخدِم نوع البيانات
  enum.
- **اختيار الأدوات:** على الرغم من أنّ النموذج يمكنه استخدام عدد غير محدود من الأدوات، إلا أنّ توفير عدد كبير جدًا منها قد يزيد من خطر اختيار أداة غير صحيحة أو غير مثالية. للحصول على أفضل النتائج، احرص على توفير الأدوات ذات الصلة فقط بالسياق أو المهمة، مع الحفاظ على المجموعة النشطة عند 10 إلى 20 أداة كحد أقصى. ننصحك باختيار الأدوات بشكل ديناميكي استنادًا إلى سياق المحادثة إذا كان لديك عدد كبير من الأدوات.
- **هندسة الطلبات:**
  - قدِّم سياقًا: أخبر النموذج بدوره (مثلاً، "أنت مساعد
    مفيد بشأن الطقس").
  - تقديم التعليمات: حدِّد كيفية استخدام الدوال ومتى يجب استخدامها (مثلاً، "لا تخمّن التواريخ، بل استخدِم دائمًا تاريخًا مستقبليًا للتوقعات").
  - تشجيع التوضيح: اطلب من النموذج طرح أسئلة توضيحية
    إذا لزم الأمر.
  - يمكنك الاطّلاع على [سير العمل المستند إلى الوكلاء](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar#agentic-workflows)
    للحصول على استراتيجيات إضافية حول تصميم هذه الطلبات. في ما يلي مثال على [تعليمات نظام](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar#agentic-si-template) تم اختبارها.
- **درجة العشوائية:** استخدِم درجة عشوائية منخفضة (مثل 0) للحصول على استدعاءات دالة أكثر حتمية وموثوقية.
- **التحقّق من الصحة:** إذا كان لاستدعاء دالة عواقب كبيرة (مثل تقديم طلب)، يجب التحقّق من صحة الاستدعاء مع المستخدم قبل تنفيذه.
- **التحقّق من سبب الإنهاء:** احرص دائمًا على التحقّق من [`finishReason`](https://ai.google.dev/api/generate-content?hl=ar#FinishReason)
  في ردّ النموذج للتعامل مع الحالات التي تعذّر فيها على النموذج إنشاء
  استدعاء دالة صالح.
- **معالجة الأخطاء**: اتّخِذ إجراءات فعالة لمعالجة الأخطاء في الدوال من أجل التعامل مع الإدخالات غير المتوقّعة أو الأعطال في واجهة برمجة التطبيقات. عرض رسائل خطأ مفيدة يمكن للنموذج استخدامها لإنشاء ردود مفيدة للمستخدم.
- **الأمان:** يُرجى مراعاة الأمان عند استدعاء واجهات برمجة التطبيقات الخارجية. استخدام آليات المصادقة والتفويض المناسبة تجنَّب عرض البيانات الحسّاسة في استدعاءات الدوال.
- **حدود الرموز المميزة:** يتم احتساب أوصاف الدوال ومعلَماتها ضمن الحد الأقصى لعدد الرموز المميزة التي يمكنك إدخالها. إذا كنت تواجه مشاكل بسبب حدود الرموز المميزة، ننصحك بالحدّ من عدد الدوال أو طول الأوصاف، أو بتقسيم المهام المعقّدة إلى مجموعات دوال أصغر وأكثر تركيزًا.
- **مزيج من bash والأدوات المخصّصة** بالنسبة إلى المطوّرين الذين يستخدمون مزيجًا من bash والأدوات المخصّصة، يتوفّر الإصدار التجريبي من Gemini 3.1 Pro مع نقطة نهاية منفصلة يمكن الوصول إليها من خلال واجهة برمجة التطبيقات باسم [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar#gemini-31-pro-preview-customtools).

## الملاحظات والقيود

- تحديد موضع أجزاء استدعاءات الدوال: عند استخدام تعريفات الدوال المخصّصة [إلى جانب الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar) (مثل &quot;بحث Google&quot;)، قد يعرض النموذج مزيجًا من أجزاء `functionCall` و`toolCall` و`toolResponse` في ردّ واحد. لهذا السبب، لا تفترض أنّ `functionCall` سيكون دائمًا العنصر الأخير في مصفوفة الأجزاء. إذا كنت تحلّل استجابة JSON يدويًا، احرص دائمًا على تكرار مصفوفة الأجزاء بدلاً من الاعتماد على الموضع.
- لا يتوافق سوى [جزء من مخطط OpenAPI](https://ai.google.dev/api/caching?hl=ar#FunctionDeclaration).
- بالنسبة إلى الوضع `ANY`، قد ترفض واجهة برمجة التطبيقات المخططات الكبيرة جدًا أو المتداخلة بشكل كبير. إذا واجهت أخطاء، حاوِل تبسيط مخططات مَعلمات الدالة والاستجابة من خلال تقصير أسماء السمات أو تقليل التداخل أو الحدّ من عدد تعريفات الدوال.
- أنواع المَعلمات المتوافقة في Python محدودة.
- لا تتوفّر ميزة استدعاء الدوال تلقائيًا إلا في حزمة تطوير البرامج (SDK) الخاصة بلغة Python.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-04-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
