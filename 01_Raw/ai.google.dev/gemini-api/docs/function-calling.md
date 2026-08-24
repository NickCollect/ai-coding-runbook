---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=he
fetched_at: 2026-08-24T02:27:32.845419+00:00
title: "\u05e7\u05e8\u05d9\u05d0\u05d4 \u05dc\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d5\u05ea \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# קריאה לפונקציות באמצעות Gemini API

התכונה 'הפעלת פונקציות' מאפשרת לכם לחבר מודלים לכלים ולממשקי API חיצוניים.
במקום ליצור תשובות טקסטואליות, המודל קובע מתי לקרוא לפונקציות ספציפיות ומספק את הפרמטרים הנדרשים לביצוע פעולות בעולם האמיתי.
כך המודל יכול לשמש כגשר בין שפה טבעית לבין פעולות ונתונים בעולם האמיתי. יש 3 תרחישי שימוש עיקריים לבקשה להפעלת פונקציה:

- [**ביצוע פעולות:**](#meeting) אינטראקציה עם מערכות חיצוניות באמצעות ממשקי API, כמו קביעת פגישות, יצירת חשבוניות, שליחת אימיילים או שליטה במכשירים חכמים לבית.
- [**העשרת הידע:**](#weather) גישה למידע ממקורות חיצוניים כמו מסדי נתונים, ממשקי API ומאגרי ידע.
- [**הרחבת היכולות:**](#chart) אפשר להשתמש בכלים חיצוניים כדי לבצע חישובים ולהרחיב את המגבלות של המודל, למשל באמצעות מחשבון או יצירת תרשימים.

בהמשך מפורטות דוגמאות לתרחישי שימוש כאלה:

### קביעת פגישה

בדוגמה הזו מוסבר איך להגדיר פונקציה שמתזמנת פגישה עם משתתפים בשעה ספציפית, כדי לאפשר למודל לנתח בקשות של משתמשים ולהחזיר ארגומנטים מובנים להפעלת פעולות במערכות חיצוניות.

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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
    "model": "gemini-3.6-flash",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type&quot;: "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

### הצגת מזג האוויר

בדוגמה הזו מוסבר איך להגדיר פונקציה שמחלצת נתוני טמפרטורה של מיקום מסוים, וכך מאפשרת למודל להפעיל ממשקי API חיצוניים כדי לענות על שאילתות שדורשות מידע בזמן אמת או מידע חיצוני.

### Python

```
from google import genai

weather_function = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the temperature in London?",
    tools=[weather_function],
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

const weatherFunctionDeclaration = {
  type: 'function',
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: {
        type: 'string',
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "What's the temperature in London?",
  tools: [weatherFunctionDeclaration],
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
    "model": "gemini-3.6-flash",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type";: "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### יצירת תרשים

בדוגמה הזו מוגדרת פונקציה שמייצרת תרשים עמודות מנתונים מובְנים. הדוגמה הזו ממחישה איך המודל יכול להשתמש בכלים חיצוניים כדי לבצע חישובים או ליצור נכסים חזותיים:

### Python

```
from google import genai

create_chart_function = {
    "type": "function",
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "The title for the chart."},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}},
        },
        "required": ["title", "labels", "values"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model=";gemini-3.6-flash",
    input="Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
    tools=[create_chart_function],
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

const createChartFunctionDeclaration = {
  type: 'function',
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and values.',
  parameters: {
    type: 'object',
    properties: {
      title: { type: 'string', description: 'The title for the chart.' },
      labels: { type: 'array', items: { type: 'string' } },
      values: { type: 'array', items: { type: 'number' } },
    },
    required: ['title', 'labels', 'values'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
  tools: [createChartFunctionDeclaration],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Create a bar chart titled '\''Quarterly Sales'\'' with Q1: 50000, Q2: 75000, Q3: 60000.",
    "tools": [{
        "type": "function",
        "name": "create_bar_chart",
        "description": "Creates a bar chart given a title, labels, and values.",
        "parameters": {
          "type": "object",
          "properties": {
            "title": {"type": "string"},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}}
          },
          "required": ["title", "labels", "values"]
        }
    }]
  }'
```

## איך פועלת התקשרות לפונקציות

![סקירה כללית על קריאה להפעלת פונקציות](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=he)

השימוש בפונקציות כולל אינטראקציה מובנית בין האפליקציה, המודל ופונקציות חיצוניות:

1. **הגדרת הצהרת פונקציה:** מגדירים למודל את שם הפונקציה, הפרמטרים והמטרה שלה.
2. **קוראים למודל LLM עם הצהרות על פונקציות:** שולחים את ההנחיה של המשתמש יחד עם ההצהרות על הפונקציות למודל.
3. **הפעלת קוד הפונקציה (באחריותכם):** המודל *לא* מפעיל את הפונקציה בעצמו. מחלקים את השם והארגומנטים ומבצעים את הפעולה באפליקציה.
4. **יצירת תשובה ידידותית למשתמש:** שליחת התוצאה בחזרה למודל כדי לקבל תשובה סופית וידידותית למשתמש.

אפשר לחזור על התהליך הזה כמה פעמים. המודל תומך בהפעלת כמה פונקציות בתור אחד ([הפעלת פונקציות במקביל](#parallel_function_calling)) וברצף ([הפעלת פונקציות בהרכבה](#compositional_function_calling)).

### שלב 1: הגדרת הצהרה על פונקציה

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
                "enum": ["daylight", "cool&>quot;, "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) - dict:
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

### שלב 2: קוראים למודל עם הצהרות על פונקציות

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

const fcStep = in>teraction.steps.find(s = s.type === 'function_call');
console.log(fcStep);
```

המודל מחזיר שלב `function_call` עם `type`, `name` ו-`arguments`:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': &#39;warm', 'brightness': 25}
```

### שלב 3: הפעלת הפונקציה

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

### שלב 4: שליחת התוצאה בחזרה למודל

### Python

```
final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

print(final_interaction.output_text)
```

### JavaScript

```
const finalInteraction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.output_text);
```

### בקשה להפעלת פונקציה ללא שמירת מצב

אפשר גם להשתמש בהפעלת פונקציות במצב חסר מצב (stateless) על ידי ניהול היסטוריית השיחות בצד הלקוח והגדרת `store=false`.

במצב חסר מצב, צריך להעביר את ההיסטוריה המלאה של השיחה בשדה `input` של כל בקשה עוקבת. ההיסטוריה הזו צריכה לכלול:
‫1. השלב הראשוני `user_input`.
2. כל השלבים שנוצרו על ידי המודל ומוחזרים בתור 1 (כולל השלבים `thought` ו-`function_call`) בדיוק כפי שהתקבלו.
3. השלב `function_result` שמכיל את הפלט של הפונקציה שהופעלה.

### Python

```
from google import genai
import json

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

for step in interaction.steps:
    history.append(step.model_dump())

fc_step = next(s for s in interaction.steps if s.type == "function_call")
if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)

history.append({
    "type": "function_result",
    "name": fc_step.name,
    "call_id": fc_step.id,
    "result": [{"type": "text", "text": json.dumps(result)}],
})

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "Turn the lights down to a romantic level" }]
    }
  ];

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  history.push(...interaction.st>eps);

  const fcStep = interaction.steps.find(s = s.type === 'function_call');
  let result;
  if (fcStep.name === 'set_light_values') {
    result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  }

  history.push({
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  });

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  console.log(finalInteraction.output_text);
}

await main();
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "Turn the lights down to a romantic level"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "set_light_values",
      "description": "Sets the brightness and color temperature of a light.",
      "parameters": {
        "type": "object",
        "properties": {
          "brightness": {"type": "integer", "description": "Light level from 0 to 100"},
          "color_temp": {"type": "string", "enum": ["daylight", "cool", "warm"]}
        },
        "required": ["brightness", "color_temp"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Extract function call details to execute
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')

# Assume local execution returns: {"brightness": 25, "colorTemperature": "warm"}
RESULT="{\"brightness\": 25, \"colorTemperature\": \"warm\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "Turn the lights down to a romantic level"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"set_light_values\",
      \"description\": \"Sets the brightness and color temperature of a light.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"brightness\": {\"type\": \"integer\"},
          \"color_temp\": {\"type\": \"string\"}
        },
        \"required\": [\"brightness\", \"color_temp\"]
      }
    }]
  }"
```

## הצהרות על פונקציות

הצהרה על פונקציה מועברת ככלי וכוללת:

- ‫`type` (מחרוזת): צריך להיות `"function"` עבור פונקציות בהתאמה אישית.
- ‫`name` (string): שם ייחודי של הפונקציה (אפשר להשתמש בקו תחתון או ב-camelCase).
- ‫`description` (string): הסבר ברור על מטרת הפונקציה.
- ‫`parameters` (אובייקט): פרמטרי הקלט שהפונקציה מצפה לקבל.
  - ‫`type` (string): סוג הנתונים הכולל, כמו `object`.
  - ‫`properties` (אובייקט): פרמטרים נפרדים עם סוג ותיאור.
  - ‫`required` (מערך): שמות פרמטרים נדרשים.

## בקשה להפעלת פונקציה באמצעות מודלים של חשיבה

מודלים מסדרת Gemini 3 משתמשים בתהליך פנימי של ["חשיבה"](https://ai.google.dev/gemini-api/docs/thinking?hl=he) שמשפר את השימוש בפונקציות. ערכות ה-SDK מטפלות באופן אוטומטי ב[חתימות מחשבה](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=he) בשבילכם.

## בקשות מקבילות להפעלת פונקציות

הפעלת כמה פונקציות בבת אחת כשהן בלתי תלויות:

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Turn this place into a party!",
    "tools": [
      {
        "type": "function",
        "name": "power_disco_ball",
        "description": "Powers the disco ball.",
        "parameters": {
          "type": "object",
          "properties": {
            "power": {"type": "boolean"}
          },
          "required": ["power"]
        }
      },
      {
        "type": "function",
        "name": "start_music",
        "description": "Play music.",
        "parameters": {
          "type": "object",
          "properties": {
            "energetic": {"type": "boolean"},
            "loud": {"type": "boolean&quot;}
          },
          "required": ["energetic", "loud"]
        }
      },
      {
        "type": "function",
        "name": "dim_lights",
        "description": "Dim the lights.",
        "parameters": {
          "type": "object",
          "properties": {
            "brightness": {"type": "number"}
          },
          "required": ["brightness"]
        }
      }
    ]
  }'
```

## בקשה להפעלת פונקציה עם קומפוזיציה

אפשר לשרשר כמה קריאות לפונקציות כדי לבצע בקשות מורכבות (למשל, קודם לקבל את המיקום ואז לקבל את מזג האוויר באותו מיקום).

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
    model="gemini-3.6-flash",
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

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherForecastTool = {
  type: 'function',
  name: 'get_weather_forecast',
  description: 'Gets the current weather temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: { type: 'string', description: 'The location' },
    },
    required: ['location'],
  },
};

const setThermostatTemperatureTool = {
  type: 'function',
  name: 'set_thermostat_temperature',
  description: 'Sets the thermostat to a desired temperature.',
  parameters: {
    type: 'object',
    properties: {
      temperature: {
        type: 'integer',
        description: 'The temperature in Celsius',
      },
    },
    required: ['temperature'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
  tools: [
    getWeatherForecastTool,
    setThermostatTemperatureTool,
  ],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  } else if (step.content) {
    for (const part of step.content) {
      if (part.text) {
        console.log(part.text);
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "If it'\''s warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    "tools": [
      {
        "type": "function",
        "name": "get_weather_forecast",
        "description": "Gets the current weather temperature for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string"}
          },
          "required": ["location"]
        }
      },
      {
        "type": "function",
        "name": "set_thermostat_temperature&quot;,
        "description": "Sets the thermostat to a desired temperature.",
        "parameters": {
          "type": "object",
          "properties": {
            "temperature": {"type": "integer"}
          },
          "required": ["temperature"]
        }
      }
    ]
  }'
```

## מצבים של בקשה להפעלת פונקציה

שליטה באופן השימוש של המודל בכלים באמצעות `tool_choice` ב-`generation_config`:

- ‫`auto` (ברירת מחדל): המודל מחליט אם להפעיל פונקציה או להגיב ישירות.
- ‫`any`: המודל מוגבל כך שתמיד יחזה קריאה לפונקציה.
- ‫`none`: המודל לא יכול לבצע קריאות לפונקציות.
- ‫`validated`: המודל מוודא שהפונקציה תואמת לסכימה.

### Python

```
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools&quot;: ["get_current_temperature"]
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
      tools: ['get_current_temperature';]
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
    "model": "gemini-3.6-flash",
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

## שימוש במולטיטול

אפשר להפעיל כמה כלים ולשלב בין כלים מובנים לבין קריאות לפונקציות באותה בקשה. מודלים של Gemini 3 יכולים לשלב כלים מובנים עם קריאה לפונקציות (function calling) מחוץ לקופסה באינטראקציות. העברת `previous_interaction_id`
תפיץ אוטומטית את ההקשר של הכלי המובנה.

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
    {"type": "google_search"},
    get_weather               
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        interaction_2 = client.interactions.create(
            model="gemini-3.6-flash",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.output_text)
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
    weatherTool            
];

let interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3.6-flash',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.output_text);
    }
}
```

### REST

```
# Turn 1: Send request with built-in google_search tool and custom weather tool
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ]
  }'

# Turn 2: Provide function result and pass previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "INTERACTION_ID",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          &quot;type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ],
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "call_123",
        "result": [{"type": "text", "text": "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"}]
      }
    ]
  }'
```

## תשובות של פונקציות מרובות מצבים

במודלים מסדרת Gemini 3, אפשר לכלול תוכן מולטימודאלי בחלקים של תגובת הפונקציה ששולחים למודל. המודל יכול לעבד את התוכן הרב-מודאלי הזה בתור הבא כדי לספק תשובה מושכלת יותר.

כדי לכלול נתונים מרובי-אופנים בתשובה של פונקציה, צריך לכלול אותם כאחד או יותר בלוקים של תוכן בשדה `result` של שלב `function_result`. בכל בלוק תוכן צריך לציין את `type` (למשל `"text"`,‏ `"image"`).

בדוגמה הבאה אפשר לראות איך לשלוח בחזרה למודל בתגובה לפונקציה נתוני תמונה במהלך אינטראקציה:

### Python

```
import base64
from google import genai
import requests

client = genai.Client()

tool_call = next(s for s in interaction.steps if s.type == "function_call")

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
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

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const toolCall = interaction.step>s.find(s = s.type === 'function_call');

const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
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

console.log(finalInteraction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
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

## בקשה להפעלת פונקציה עם פלט מובנה

במודלים מסדרת Gemini 3, אפשר לשלב קריאה לפונקציה עם [פלט מובנה](https://ai.google.dev/gemini-api/docs/structured-output?hl=he) כדי לקבל תשובות בפורמט עקבי.

## ‫MCP (Model Context Protocol) מרוחק

‫Interactions API תומך בחיבור לשרתי MCP מרוחקים כדי לתת למודל גישה לכלים ולשירותים חיצוניים. אתם מספקים את השרת `name` ואת `url` בהגדרת הכלים.

כשמשתמשים ב-Remote MCP, חשוב לשים לב למגבלות הבאות:

- **סוגי שרתים**: שרת MCP מרוחק פועל רק עם שרתי HTTP שניתן להזרים מהם. אין תמיכה בשרתי SSE (אירועים שנשלחים מהשרת).
- **שמות**: שמות של שרתי MCP לא יכולים לכלול את התו `-`. במקום זאת, צריך להשתמש בשמות השרתים `snake_case`.

| שדה | סוג | נדרש | תיאור |
| --- | --- | --- | --- |
| `type` | `string` | כן | חייב להיות `"mcp_server"`. |
| `name` | `string` | לא | השם המוצג של שרת ה-MCP. |
| `url` | `string` | לא | כתובת ה-URL המלאה של נקודת הקצה של שרת ה-MCP. |
| `headers` | `object` | לא | צמדי מפתח/ערך שנשלחים ככותרות HTTP עם כל בקשה לשרת (לדוגמה, אסימוני אימות). |
| `allowed_tools` | `array` | לא | הגבלת הכלים בשרת שהסוכן יכול להשתמש בהם. |

### דוגמה

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Check the weather in San Francisco.",
    tools=[
        {
            "type": "mcp_server",
            "name": "weather",
            "url";: "https://gemini-api-demos.uc.r.appspot.com/mcp",
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Check the weather in San Francisco.',
    tools: [
        {
            type: 'mcp_server',
            name: 'weather',
            url: 'https://gemini-api-demos.uc.r.appspot.com/mcp'
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
    "model": "gemini-3.6-flash",
    "input": "Check the weather in San Francisco.",
    "tools": [
        {
            "type": "mcp_server",
            &quot;name": "weather",
            "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
        }
    ]
}'
```

## העברת קריאות לכלי בסטרימינג

כשמשתמשים בכלים עם סטרימינג, המודל יוצר קריאות לפונקציות כרצף של אירועים בסטרימינג.`step.delta` אפשר להזרים ארגומנטים של כלים כארגומנטים חלקיים באמצעות `arguments`. כדי לשחזר את הקריאות המלאות לכלים לפני שמריצים אותן, צריך לצבור את השינויים האלה.

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
    model="gemini-3.6-flash",
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
    model: 'gemini-3.6-flash',
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
    } else if (evT>ype === 'interaction.completed' || evType === 'interaction.complete') {
        toolCalls = Array.from(currentCalls.values()).map(call = ({
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
    "model": "gemini-3.6-flash",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties&quot;: {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

## שיטות מומלצות

- **תיאורים של פונקציות ופרמטרים:** הקפידו להיות ברורים וספציפיים.
- **שמות:** צריך להשתמש בשמות תיאוריים ללא רווחים או תווים מיוחדים.
- **הקלדה חזקה:** שימוש בסוגים ספציפיים (מספר שלם, מחרוזת, enum).
- **בחירת כלים:** כדאי להגדיר את האפשרות 'פעיל' ל-10 עד 20 כלים לכל היותר.
- **הנדסת הנחיות:** מספקים הקשר והוראות.
- **אימות:** אימות של קריאות לפונקציות לפני ההפעלה.
- **טיפול בשגיאות:** צריך להטמיע טיפול בשגיאות בצורה חזקה.
- **אבטחה:** השתמשו באימות מתאים לממשקי API חיצוניים.

## פתרונות עקיפים לדרישות הטקסט של כלי ההכנה

**בעיה:** אם ההנחיה שלכם דורשת מהמודל ליצור טקסט מובנה (XML,‏ YAML,‏ JSON וכו') (לדוגמה, `<UPDATE>...</UPDATE>`) מיד לפני ביצוע קריאה לכלי, יכול להיות שהקריאה לכלי תיכשל מדי פעם עם `Malformed_Function_Call`.

**פתרונות:** הפתרונות הבאים יעזרו לכם לפתור את הבעיה:

- **מומלץ:** מנחים את המודל להוסיף את ההערות שלו לפני השימוש בכלי בתוך קריאה ייעודית לפונקציה `update()` במקום בטקסט גולמי (פרטים בהמשך).
- מנחים את המודל לכתוב הערות ככותרות Markdown ‏ (`# UPDATE`, `## PLAN`) במקום כטקסט מובנה.
- לא לחייב את המודל להפיק טקסט לפני קריאות לכלים.

### פתרון עדיף: עטיפת הערות העבודה בקריאה ייעודית לפונקציה

במקום ההוראה המקורית:

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags with<in `UP>DATE`.
```

צריך להשתמש בהוראה המעודכנת הזו:

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

בנוסף, צריך לעדכן את כל ההפניות לפורמט ה-XML הישן של `<UPDATE>` בבקשת הלקוח. לאחר מכן מוסיפים את הצהרת הפונקציה המתאימה לפונקציית העדכון:

```
{
  "name": "update",
  "description": "Update working notes (previous step analysis, plan, next step, external note).",
  "parameters": {
    "type": "OBJECT",
    "properties": {
      "previous_step": {
        "type": "STRING",
        "description": "Key findings and outcomes since the previous step."
      },
      "plan": {
        "type": "STRING",
        "description": "The current status of the plan."
      },
      "next_step": {
        "type": "STRING",
        "description": "Brief explanation of the immediate next action according to the plan."
      },
      "external": {
        ";type": "STRING",
        "description": "A short, plain-language note shown to the User about what you are ABOUT TO DO next."
      }
    },
    "required": [
      "previous_step",
      "plan",
      "next_step",
      "external"
    ]
  }
}
```

לאחר מכן, המודל יבצע שתי קריאות באותו השלב: הקריאה `update()` שמחליפה את ה-XML המובנה, והקריאה בפועל לפונקציה שהוא רוצה לבצע.

## הערות ומגבלות

- יש תמיכה רק ב[קבוצת משנה של סכימת OpenAPI](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=he#FunctionDeclaration).
- במצב `any`, יכול להיות שה-API ידחה סכימות גדולות מאוד או סכימות עם קינון עמוק.
- סוגי הפרמטרים הנתמכים ב-Python מוגבלים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-30 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-30 (שעון UTC)."],[],[]]
