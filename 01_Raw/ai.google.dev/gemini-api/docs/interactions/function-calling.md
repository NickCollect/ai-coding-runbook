---
source_url: https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi
fetched_at: 2026-05-11T05:01:09.380568+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini API के साथ फ़ंक्शन कॉलिंग की सुविधा

फ़ंक्शन कॉलिंग की सुविधा की मदद से, मॉडल को बाहरी टूल और एपीआई से कनेक्ट किया जा सकता है.
टेक्स्ट वाले जवाब जनरेट करने के बजाय, मॉडल यह तय करता है कि किसी फ़ंक्शन को कब कॉल करना है. साथ ही, असल दुनिया में होने वाली कार्रवाइयों को पूरा करने के लिए ज़रूरी पैरामीटर उपलब्ध कराता है.
इससे मॉडल, नैचुरल लैंग्वेज और असल दुनिया की गतिविधियों और डेटा के बीच एक पुल की तरह काम कर पाता है. फ़ंक्शन कॉलिंग का इस्तेमाल इन तीन मुख्य कामों के लिए किया जाता है:

- **जानकारी बढ़ाना:** डेटाबेस, एपीआई, और नॉलेज बेस जैसे बाहरी सोर्स से जानकारी ऐक्सेस करना.
- **ज़्यादा सुविधाएं पाना:** कैलकुलेशन करने और मॉडल की सीमाओं को बढ़ाने के लिए, बाहरी टूल का इस्तेमाल करें. जैसे, कैलकुलेटर का इस्तेमाल करना या चार्ट बनाना.
- **कार्रवाइयां करना:** एपीआई का इस्तेमाल करके बाहरी सिस्टम के साथ इंटरैक्ट करना. जैसे, अपॉइंटमेंट शेड्यूल करना, इनवॉइस बनाना, ईमेल भेजना या स्मार्ट होम डिवाइसों को कंट्रोल करना.

मौसम की जानकारी पाएं
मीटिंग शेड्यूल करें
चार्ट बनाएं

### Python

```
from google import genai

schedule_meeting_function = {
    "type": "function",
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string", "description": "Date (e.g., '2024-07-29')"},
            "time": {"type": "string", "description": "Time (e.g., '15:00')"},
            "topic": {"type": "string", "description": "The meeting topic."},
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about Q3 planning.",
    tools=[{"type": "function", **schedule_meeting_function}],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const scheduleMeetingFunction = {
  type: 'function',
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: 'object',
    properties: {
      attendees: { type: 'array', items: { type: 'string' } },
      date: { type: 'string', description: 'Date (e.g., "2024-07-29")' },
      time: { type: 'string', description: 'Time (e.g., "15:00")' },
      topic: { type: 'string', description: 'The meeting topic.' },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.',
  tools: [scheduleMeetingFunction],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

## फ़ंक्शन कॉलिंग की सुविधा कैसे काम करती है

![फ़ंक्शन कॉल करने की सुविधा के बारे में खास जानकारी](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=hi)

फ़ंक्शन कॉलिंग में, आपके ऐप्लिकेशन, मॉडल, और बाहरी फ़ंक्शन के बीच स्ट्रक्चर्ड इंटरैक्शन शामिल होता है:

1. **फ़ंक्शन के बारे में जानकारी देना:** मॉडल को फ़ंक्शन के नाम, पैरामीटर, और मकसद के बारे में जानकारी दें.
2. **फ़ंक्शन के एलान के साथ एलएलएम को कॉल करना:** मॉडल को फ़ंक्शन के एलान के साथ उपयोगकर्ता का प्रॉम्प्ट भेजें.
3. **फ़ंक्शन कोड को लागू करना (आपकी ज़िम्मेदारी):** मॉडल, फ़ंक्शन को *लागू नहीं करता*. नाम और आर्ग्युमेंट निकालें और उन्हें अपने ऐप्लिकेशन में लागू करें.
4. **उपयोगकर्ता के लिए आसान जवाब तैयार करना:** नतीजे को मॉडल को वापस भेजें, ताकि वह उपयोगकर्ता के लिए आसान जवाब तैयार कर सके.

इस प्रोसेस को कई बार दोहराया जा सकता है. यह मॉडल, एक ही टर्न में कई फ़ंक्शन कॉल कर सकता है ([पैरलल फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi#parallel_function_calling)). साथ ही, यह एक के बाद एक फ़ंक्शन कॉल कर सकता है ([कंपोज़िशनल फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=hi#compositional_function_calling)).

### पहला चरण: फ़ंक्शन का एलान तय करना

### Python

```
set_light_values_declaration = {
    "type": "function",
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) -> dict:
    """Set the brightness and color temperature of a room light."""
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
const setLightValuesTool = {
  type: 'function',
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: 'object',
    properties: {
      brightness: { type: 'number', description: 'Light level from 0 to 100' },
      color_temp: { type: 'string', enum: ['daylight', 'cool', 'warm'] },
    },
    required: ['brightness', 'color_temp'],
  },
};

function setLightValues(brightness, color_temp) {
  return { brightness: brightness, colorTemperature: color_temp };
}
```

### दूसरा चरण: फ़ंक्शन के बारे में जानकारी देकर मॉडल को कॉल करना

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

# Find the function call step
fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

// Find the function call step
const fcStep = interaction.steps.find(s => s.type === 'function_call');
console.log(fcStep);
```

मॉडल, `function_call` चरण में `type`, `name`, और `arguments` दिखाता है:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': 'warm', 'brightness': 25}
```

### तीसरा चरण: फ़ंक्शन को लागू करना

### Python

```
fc_step = next(s for s in interaction.steps if s.type == "function_call")

if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)
    print(f"Function execution result: {result}")
```

### JavaScript

```
const fcStep = interaction.steps.find(s => s.type === 'function_call');

let result;
if (fcStep.name === 'set_light_values') {
  result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### चौथा चरण: नतीजे को मॉडल के पास वापस भेजना

### Python

```
final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "function_result",
            "name": fc_step.name,
            "call_id": fc_step.id,
            "result": [{"type": "text", "text": json.dumps(result)}],
        }
    ],
    tools=[set_light_values_declaration],
    previous_interaction_id=interaction.id,
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
const finalInteraction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

## फ़ंक्शन के एलान

फ़ंक्शन के एलान को टूल के तौर पर पास किया जाता है. इसमें ये शामिल हैं:

- `type` (स्ट्रिंग): कस्टम फ़ंक्शन के लिए, इसकी वैल्यू `"function"` होनी चाहिए.
- `name` (string): फ़ंक्शन का यूनीक नाम (अंडरस्कोर या कैमल केस का इस्तेमाल करें).
- `description` (string): फ़ंक्शन के मकसद के बारे में साफ़ तौर पर जानकारी.
- `parameters` (ऑब्जेक्ट): वे इनपुट पैरामीटर जिनकी ज़रूरत फ़ंक्शन को होती है.
  - `type` (स्ट्रिंग): यह कुल डेटा टाइप होता है, जैसे कि `object`.
  - `properties` (object): टाइप और ब्यौरे के साथ अलग-अलग पैरामीटर.
  - `required` (ऐरे): पैरामीटर के नाम डालना ज़रूरी है.

## सूझ-बूझ वाले मॉडल के साथ फ़ंक्शन कॉलिंग की सुविधा

Gemini 3 और 2.5 सीरीज़ के मॉडल, ["सोचने"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=hi) की इंटरनल प्रोसेस का इस्तेमाल करते हैं. इससे फ़ंक्शन कॉलिंग की सुविधा बेहतर होती है.
SDK, आपके लिए [थॉट सिग्नेचर](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=hi) अपने-आप मैनेज करते हैं.

## पैरलल फ़ंक्शन कॉलिंग

जब कई फ़ंक्शन एक-दूसरे पर निर्भर न हों, तब उन्हें एक साथ कॉल करें:

### Python

```
power_disco_ball = {"type": "function", "name": "power_disco_ball", "description": "Powers the disco ball.",
    "parameters": {"type": "object", "properties": {"power": {"type": "boolean"}}, "required": ["power"]}}
start_music = {"type": "function", "name": "start_music", "description": "Play music.",
    "parameters": {"type": "object", "properties": {"energetic": {"type": "boolean"}, "loud": {"type": "boolean"}}, "required": ["energetic", "loud"]}}
dim_lights = {"type": "function", "name": "dim_lights", "description": "Dim the lights.",
    "parameters": {"type": "object", "properties": {"brightness": {"type": "number"}}, "required": ["brightness"]}}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn this place into a party!",
    tools=[power_disco_ball, start_music, dim_lights],
    generation_config={"tool_choice": "any"},
)

for step in interaction.steps:
    if step.type == "function_call":
        args = ", ".join(f"{key}={val}" for key, val in step.arguments.items())
        print(f"{step.name}({args})")
```

### JavaScript

```
const powerDiscoBall = { type: 'function', name: 'power_disco_ball', description: 'Powers the disco ball.',
  parameters: { type: 'object', properties: { power: { type: 'boolean' } }, required: ['power'] } };
const startMusic = { type: 'function', name: 'start_music', description: 'Play music.',
  parameters: { type: 'object', properties: { energetic: { type: 'boolean' }, loud: { type: 'boolean' } }, required: ['energetic', 'loud'] } };
const dimLights = { type: 'function', name: 'dim_lights', description: 'Dim the lights.',
  parameters: { type: 'object', properties: { brightness: { type: 'number' } }, required: ['brightness'] } };

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn this place into a party!',
  tools: [powerDiscoBall, startMusic, dimLights],
  generation_config: { tool_choice: 'any' },
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

## कंपोज़िशनल फ़ंक्शन कॉलिंग

मुश्किल अनुरोधों के लिए, एक साथ कई फ़ंक्शन कॉल को जोड़ें. उदाहरण के लिए, पहले जगह की जानकारी पाएं, फिर उस जगह के मौसम की जानकारी पाएं.

### Python

```
get_weather_forecast_declaration = {
    "type": "function",
    "name": "get_weather_forecast",
    "description": "Gets the current weather temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The location"},
        },
        "required": ["location"],
    },
}

set_thermostat_temperature_declaration = {
    "type": "function",
    "name": "set_thermostat_temperature",
    "description": "Sets the thermostat to a desired temperature.",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "integer",
                "description": "The temperature in Celsius",
            },
        },
        "required": ["temperature"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    tools=[
        get_weather_forecast_declaration,
        set_thermostat_temperature_declaration,
    ],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
    elif hasattr(step, "content") and step.content:
         for part in step.content:
             if hasattr(part, "text"):
                 print(part.text)
```

## फ़ंक्शन कॉल करने के मोड

`generation_config` में `tool_choice` का इस्तेमाल करके, यह कंट्रोल करें कि मॉडल टूल का इस्तेमाल कैसे करे:

- `auto` (डिफ़ॉल्ट): मॉडल यह तय करता है कि किसी फ़ंक्शन को कॉल करना है या सीधे जवाब देना है.
- `any`: मॉडल को हमेशा फ़ंक्शन कॉल का अनुमान लगाने के लिए सीमित किया जाता है.
- `none`: मॉडल को फ़ंक्शन कॉल करने की अनुमति नहीं है.
- `validated` (झलक): मॉडल यह पक्का करता है कि फ़ंक्शन स्कीमा का पालन किया गया हो.

### Python

```
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools": ["get_current_temperature"]
        }
    }
}
```

### JavaScript

```
const generation_config = {
  tool_choice: {
    allowed_tools: {
      mode: 'any',
      tools: ['get_current_temperature']
    }
  }
};
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the temperature in Boston?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string"}
        },
        "required": ["location"]
      }
    }],
    "generation_config": {
      "tool_choice": {
        "allowed_tools": {
          "mode": "any",
          "tools": ["get_current_temperature"]
        }
      }
    }
  }'
```

## मल्टी-टूल का इस्तेमाल

एक ही अनुरोध में, फ़ंक्शन कॉलिंग के साथ-साथ पहले से मौजूद टूल को मिलाकर, कई टूल चालू किए जा सकते हैं. Gemini 3 मॉडल, इंटरैक्शन में बिल्ट-इन टूल को फ़ंक्शन कॉलिंग की सुविधा के साथ जोड़ सकते हैं. `previous_interaction_id` पास करने पर, बिल्ट-इन टूल का कॉन्टेक्स्ट अपने-आप शेयर हो जाता है.

### Python

```
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "get_weather",
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

tools = [
    {"type": "google_search"},  # Built-in tool
    get_weather                 # Custom tool
]

# Turn 1: Initial request with both tools enabled
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        # Execute your custom function locally
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        # Turn 2: Provide the function result back to the model.
        # Passing `previous_interaction_id` automatically circulates the
        # built-in Google Search context from Turn 1
        interaction_2 = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool              // Custom tool
];

// Turn 1: Initial request with both tools enabled
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        // Execute your custom function locally
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        // Turn 2: Provide the function result back to the model.
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.steps.at(-1).content[0].text);
    }
}
```

## टेक्स्ट, इमेज, और वीडियो वगैरह का इस्तेमाल करके की गई क्वेरी के जवाब

Gemini 3 सीरीज़ के मॉडल के लिए, फ़ंक्शन के जवाब वाले उन हिस्सों में मल्टीमॉडल कॉन्टेंट शामिल किया जा सकता है जिन्हें मॉडल को भेजा जाता है. मॉडल, इस मल्टीमॉडल कॉन्टेंट को अपने अगले टर्न में प्रोसेस कर सकता है, ताकि ज़्यादा जानकारी वाला जवाब दिया जा सके.

किसी फ़ंक्शन के जवाब में मल्टीमॉडल डेटा शामिल करने के लिए, उसे `result` चरण के `result` फ़ील्ड में एक या उससे ज़्यादा कॉन्टेंट ब्लॉक के तौर पर शामिल करें.`function_result` हर कॉन्टेंट ब्लॉक में, उसका `type` (जैसे, `"text"`, `"image"`) तय किया जाना चाहिए.

इस उदाहरण में दिखाया गया है कि किसी इंटरैक्शन में, इमेज का डेटा शामिल करने वाले फ़ंक्शन के जवाब को मॉडल को वापस कैसे भेजा जाता है:

### Python

```
import base64
from google import genai
import requests

client = genai.Client()

# Find the function call step
tool_call = next(s for s in interaction.steps if s.type == "function_call")

# Execute your tool to get image bytes
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction.id,
    input=[
        {
            "type": "function_result",
            "name": tool_call.name,
            "call_id": tool_call.id,
            "result": [
                {"type": "text", "text": "instrument.jpg"},
                {
                    "type": "image",
                    "mime_type": "image/jpeg",
                    "data": base64_image_data,
                },
            ],
        }
    ],
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Find the function call step
const toolCall = interaction.steps.find(s => s.type === 'function_call');

// Execute your tool to get image bytes and convert to base64
// (Implementation depends on your environment)
const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction.id,
    input: [{
        type: 'function_result',
        name: toolCall.name,
        call_id: toolCall.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }]
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [
      {
        "type": "function_result",
        "name": "get_image",
        "call_id": "call_123",
        "result": [
          {"type": "text", "text": "instrument.jpg"},
          {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "BASE64_IMAGE_DATA"
          }
        ]
      }
    ]
  }'
```

## स्ट्रक्चर्ड आउटपुट के साथ फ़ंक्शन कॉलिंग

Gemini 3 सीरीज़ के मॉडल के लिए, फ़ंक्शन कॉलिंग को [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=hi) के साथ जोड़ें, ताकि जवाब एक ही फ़ॉर्मैट में मिलें.

## रिमोट एमसीपी (मॉडल कॉन्टेक्स्ट प्रोटोकॉल)

Interactions API, रिमोट एमसीपी सर्वर से कनेक्ट करने की सुविधा देता है. इससे मॉडल को बाहरी टूल और सेवाओं का ऐक्सेस मिलता है. टूल कॉन्फ़िगरेशन में, सर्वर `name` और `url` की जानकारी दी जाती है.

रिमोट एमसीपी का इस्तेमाल करते समय, इन बातों का ध्यान रखें:

- **सर्वर के टाइप**: रिमोट एमसीपी, सिर्फ़ स्ट्रीम किए जा सकने वाले एचटीटीपी सर्वर के साथ काम करता है. एसएसई (Server-Sent Events) सर्वर काम नहीं करते.
- **मॉडल के साथ काम करने की सुविधा**: फ़िलहाल, रिमोट एमसीपी, Gemini 3 मॉडल के साथ काम नहीं करता. Gemini 3 के लिए सहायता जल्द ही उपलब्ध होगी.
- **नाम**: एमसीपी सर्वर के नामों में `-` वर्ण शामिल नहीं होना चाहिए. इसके बजाय, `snake_case` सर्वर के नाम इस्तेमाल करें.

| फ़ील्ड | प्रकार | ज़रूरी है | ब्यौरा |
| --- | --- | --- | --- |
| `type` | `string` | हां | `"mcp_server"` होना चाहिए. |
| `name` | `string` | नहीं | एमसीपी सर्वर का डिसप्ले नेम. |
| `url` | `string` | नहीं | एमसीपी सर्वर के एंडपॉइंट का पूरा यूआरएल. |
| `headers` | `object` | नहीं | हर अनुरोध के साथ सर्वर को भेजे गए एचटीटीपी हेडर के तौर पर कुंजी-वैल्यू पेयर (उदाहरण के लिए, पुष्टि करने वाले टोकन). |
| `allowed_tools` | `array` | नहीं | यह तय करें कि एजेंट, सर्वर के किन टूल को कॉल कर सकता है. |

### उदाहरण

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-2.5-flash',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-flash",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ]
}'
```

## स्ट्रीम टूल कॉल

स्ट्रीमिंग की सुविधा वाले टूल का इस्तेमाल करते समय, मॉडल फ़ंक्शन कॉल जनरेट करता है. ये कॉल, स्ट्रीम पर `step.delta` इवेंट के क्रम के तौर पर जनरेट होते हैं. `arguments` का इस्तेमाल करके, टूल के आर्ग्युमेंट को आंशिक आर्ग्युमेंट के तौर पर स्ट्रीम किया जा सकता है. इन डेल्टा को इकट्ठा करके, टूल कॉल को फिर से बनाया जाना चाहिए. इसके बाद ही, उन्हें लागू किया जाना चाहिए.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state"}
        },
        "required": ["location"]
    }
}

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool],
    stream=True
)

current_calls = {}
tool_calls = []

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            current_calls[event.index] = {
                "id": event.step.id,
                "name": event.step.name,
                "arguments": ""
            }
            # Handle arguments provided in step.start
            if hasattr(event.step, "arguments") and event.step.arguments:
                if isinstance(event.step.arguments, dict):
                    current_calls[event.index]["arguments"] = json.dumps(event.step.arguments)
                else:
                    current_calls[event.index]["arguments"] = event.step.arguments
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            if event.index in current_calls:
                current_calls[event.index]["arguments"] += event.delta.partial_arguments
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)

    elif event.event_type == "interaction.completed":
        for index, call in current_calls.items():
            args = call["arguments"]
            if args:
                args = json.loads(args)
            else:
                args = {}

            tool_calls.append({
                "type": "function_call",
                "id": call["id"],
                "name": call["name"],
                "arguments": args
            })

        print(f"\nFinal tool calls ready to execute:")
        print(json.dumps(tool_calls, indent=2))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state' }
        },
        required: ['location']
    }
};

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool],
    stream: true,
});

const currentCalls = new Map();
let toolCalls = [];

for await (const event of stream) {
    const evType = event.event_type;
    if (evType === 'step.start') {
        if (event.step.type === 'function_call') {
            currentCalls.set(event.index, {
                id: event.step.id,
                name: event.step.name,
                arguments: ''
            });
            // Handle arguments provided in step.start
            if (event.step.arguments) {
                if (typeof event.step.arguments === 'object') {
                    currentCalls.get(event.index).arguments = JSON.stringify(event.step.arguments);
                } else {
                    currentCalls.get(event.index).arguments = event.step.arguments;
                }
            }
        }
    } else if (evType === 'step.delta') {
        if (event.delta.type === 'arguments') {
            if (currentCalls.has(event.index)) {
                currentCalls.get(event.index).arguments += event.delta.partial_arguments;
            }
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (evType === 'interaction.completed' || evType === 'interaction.complete') {
        toolCalls = Array.from(currentCalls.values()).map(call => ({
            type: 'function_call',
            id: call.id,
            name: call.name,
            arguments: call.arguments ? JSON.parse(call.arguments) : {}
        }));
        console.log('\nFinal tool calls ready to execute:');
        console.log(JSON.stringify(toolCalls, null, 2));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

## सबसे सही तरीके

- **फ़ंक्शन और पैरामीटर की जानकारी:** साफ़ और सटीक जानकारी दें.
- **नाम देना:** ऐसे नाम इस्तेमाल करें जिनमें स्पेस या खास वर्ण न हों.
- **स्ट्रॉन्ग टाइपिंग:** खास टाइप (पूर्णांक, स्ट्रिंग, enum) का इस्तेमाल करें.
- **टूल चुनना:** ज़्यादा से ज़्यादा 10 से 20 टूल चालू रखें.
- **प्रॉम्प्ट इंजीनियरिंग:** प्रॉम्प्ट में कॉन्टेक्स्ट और निर्देश दें.
- **पुष्टि करना:** फ़ंक्शन कॉल को लागू करने से पहले उनकी पुष्टि करें.
- **गड़बड़ी ठीक करना:** गड़बड़ी ठीक करने की सुविधा लागू करें.
- **सुरक्षा:** बाहरी एपीआई के लिए, पुष्टि करने के सही तरीके का इस्तेमाल करें.

## ध्यान देने वाली बातें और सीमाएं

- सिर्फ़ [OpenAPI स्कीमा के सबसेट](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=hi#FunctionDeclaration) का इस्तेमाल किया जा सकता है.
- `any` मोड के लिए, एपीआई बहुत बड़े या डीपली नेस्ट किए गए स्कीमा को अस्वीकार कर सकता है.
- Python में इस्तेमाल किए जा सकने वाले पैरामीटर टाइप सीमित हैं.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-05-09 (UTC) को अपडेट किया गया."],[],[]]
