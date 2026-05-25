---
source_url: https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl
fetched_at: 2026-05-25T05:29:09.424312+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wywoływanie funkcji za pomocą interfejsu Gemini API

Wywoływanie funkcji umożliwia łączenie modeli z narzędziami i interfejsami API innych firm.
Zamiast generować odpowiedzi tekstowe, model określa, kiedy wywołać konkretne funkcje, i podaje niezbędne parametry do wykonania działań w rzeczywistym świecie.
Dzięki temu model może stanowić pomost między językiem naturalnym a rzeczywistymi działaniami i danymi. Wywoływanie funkcji ma 3 główne zastosowania:

- **Wzbogacanie wiedzy:** dostęp do informacji ze źródeł zewnętrznych, takich jak bazy danych, interfejsy API i bazy wiedzy.
- **Rozszerzanie możliwości:** używaj narzędzi zewnętrznych do wykonywania obliczeń i przekraczania ograniczeń modelu, np. korzystaj z kalkulatora lub twórz wykresy.
- **Podejmowanie działań:** wchodzenie w interakcję z systemami zewnętrznymi za pomocą interfejsów API, np. planowanie spotkań, tworzenie faktur, wysyłanie e-maili czy sterowanie inteligentnymi urządzeniami domowymi.

Sprawdź pogodę
Zaplanuj spotkanie
Utwórz wykres

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
  -H "Api-Revision: 2026-05-20" \
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

## Jak działa wywoływanie funkcji

![Omówienie wywoływania funkcji](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=pl)

Wywoływanie funkcji obejmuje strukturalną interakcję między aplikacją, modelem i funkcjami zewnętrznymi:

1. **Zdefiniuj deklarację funkcji:** podaj modelowi nazwę, parametry i przeznaczenie funkcji.
2. **Wywołaj LLM za pomocą deklaracji funkcji:** wyślij prompt użytkownika wraz z deklaracjami funkcji do modelu.
3. **Wykonywanie kodu funkcji (Twoja odpowiedzialność):** model *nie* wykonuje funkcji samodzielnie. Wyodrębnij nazwę i argumenty, a następnie wykonaj je w aplikacji.
4. **Utwórz odpowiedź przyjazną dla użytkownika:** wyślij wynik z powrotem do modelu, aby uzyskać ostateczną odpowiedź przyjazną dla użytkownika.

Ten proces można powtarzać w wielu turach. Model obsługuje wywoływanie wielu funkcji w ramach jednej tury ([równoległe wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl#parallel_function_calling)) i sekwencyjnie ([kompozycyjne wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl#compositional_function_calling)).

### Krok 1. Zdefiniuj deklarację funkcji

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

### Krok 2. Wywołaj model z deklaracjami funkcji

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
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
  model: 'gemini-3-flash-preview',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');
console.log(fcStep);
```

Model zwraca krok `function_call` z wartościami `type`, `name` i `arguments`:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': 'warm', 'brightness': 25}
```

### Krok 3. Wykonaj funkcję

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

### Krok 4. Prześlij wynik z powrotem do modelu

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

print(final_interaction.output_text)
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

console.log(finalInteraction.output_text);
```

### Wywoływanie funkcji bezstanowych

Możesz też używać wywoływania funkcji w trybie bezstanowym, zarządzając historią rozmów po stronie klienta i ustawiając wartość `store=false`.

W trybie bezstanowym musisz przekazywać pełną historię rozmowy w polu `input` każdej kolejnej prośby. Historia musi zawierać:
1. Początkowy krok `user_input`.
2. Wszystkie wygenerowane przez model kroki zwrócone w turze 1 (w tym kroki `thought` i `function_call`) w takiej postaci, w jakiej zostały otrzymane.
3. Krok `function_result` zawierający dane wyjściowe wykonanej funkcji.

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
    model="gemini-3-flash-preview",
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
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  history.push(...interaction.steps);

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
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
    model: 'gemini-3-flash-preview',
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
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
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
  -H "Api-Revision: 2026-05-20" \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
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

## Deklaracje funkcji

Deklaracja funkcji jest przekazywana jako narzędzie i zawiera:

- `type` (ciąg znaków): w przypadku funkcji niestandardowych musi mieć wartość `"function"`.
- `name` (ciąg znaków): unikalna nazwa funkcji (używaj podkreśleń lub notacji camelCase).
- `description` (string): jasne wyjaśnienie celu funkcji.
- `parameters` (obiekt): parametry wejściowe, których oczekuje funkcja.
  - `type` (string): ogólny typ danych, np. `object`.
  - `properties` (obiekt): poszczególne parametry z typem i opisem.
  - `required` (tablica): nazwy parametrów obowiązkowych.

## Wywoływanie funkcji za pomocą modeli myślących

Modele z serii Gemini 3 i 2.5 korzystają z wewnętrznego procesu [„myślenia”](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=pl), który ulepsza wywoływanie funkcji.
Zestawy SDK automatycznie obsługują [sygnatury myśli](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=pl).

## Równoległe wywoływanie funkcji

Wywołuj wiele funkcji jednocześnie, jeśli są od siebie niezależne:

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

## Wywoływanie funkcji kompozycyjnych

Łącz ze sobą wiele wywołań funkcji w przypadku złożonych żądań (np. najpierw pobierz lokalizację, a potem prognozę pogody dla tej lokalizacji).

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

## Tryby wywoływania funkcji

Kontroluj sposób, w jaki model korzysta z narzędzi, używając `tool_choice` w `generation_config`:

- `auto` (domyślnie): model decyduje, czy wywołać funkcję, czy odpowiedzieć bezpośrednio.
- `any`: model jest ograniczony do zawsze przewidywania wywołania funkcji.
- `none`: model nie może wywoływać funkcji.
- `validated` (wersja testowa): model zapewnia zgodność ze schematem funkcji.

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
  -H "Api-Revision: 2026-05-20" \
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

## Korzystanie z narzędzi

W tym samym żądaniu możesz włączyć kilka narzędzi, łącząc narzędzia wbudowane z wywoływaniem funkcji. Modele Gemini 3 mogą łączyć wbudowane narzędzia z wywoływaniem funkcji w interakcjach. Przekazywanie `previous_interaction_id`
automatycznie rozpowszechnia wbudowany kontekst narzędzia.

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
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
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
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
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

        console.log(interaction_2.output_text);
    }
}
```

## Odpowiedzi funkcji multimodalnych

W przypadku modeli z serii Gemini 3 możesz uwzględniać treści multimodalne w częściach odpowiedzi funkcji, które wysyłasz do modelu. Model może przetworzyć te treści multimodalne w kolejnej turze, aby wygenerować bardziej szczegółową odpowiedź.

Aby uwzględnić dane multimodalne w odpowiedzi funkcji, dodaj je jako co najmniej 1 blok treści w polu `result` kroku `function_result`. Każdy blok treści musi określać swój `type` (np. `"text"`, `"image"`).

Ten przykład pokazuje, jak w ramach interakcji wysłać do modelu odpowiedź funkcji zawierającą dane obrazu:

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

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const toolCall = interaction.steps.find(s => s.type === 'function_call');

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

console.log(finalInteraction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
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

## Wywoływanie funkcji z uporządkowanymi danymi wyjściowymi

W przypadku modeli z serii Gemini 3 połącz wywoływanie funkcji z [danymi wyjściowymi w formacie strukturalnym](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=pl), aby uzyskiwać odpowiedzi w jednolitym formacie.

## Zdalny MCP (Model Context Protocol)

Interfejs API interakcji obsługuje łączenie się ze zdalnymi serwerami MCP, aby zapewnić modelowi dostęp do narzędzi i usług zewnętrznych. Serwer `name` i `url` podajesz w konfiguracji narzędzi.

Podczas korzystania z usługi Remote MCP pamiętaj o tych ograniczeniach:

- **Typy serwerów:** zdalny MCP działa tylko z serwerami HTTP obsługującymi strumieniowanie. Serwery SSE (Server-Sent Events) nie są obsługiwane.
- **Obsługa modeli:** zdalny MCP nie działa obecnie z modelami Gemini 3. Obsługa Gemini 3 będzie dostępna wkrótce.
- **Nazewnictwo:** nazwy serwerów MCP nie powinny zawierać znaku `-`. Użyj w zamian nazw serwerów `snake_case`.

| Pole | Typ | Wymagane | Opis |
| --- | --- | --- | --- |
| `type` | `string` | Tak | Musi to być `"mcp_server"`. |
| `name` | `string` | Nie | Wyświetlana nazwa serwera MCP. |
| `url` | `string` | Nie | Pełny adres URL punktu końcowego serwera MCP. |
| `headers` | `object` | Nie | Pary klucz-wartość wysyłane jako nagłówki HTTP z każdym żądaniem do serwera (np. tokeny uwierzytelniania). |
| `allowed_tools` | `array` | Nie | Ogranicz narzędzia, z których agent może korzystać na serwerze. |

### Przykład

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
  -H "Api-Revision: 2026-05-20" \
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

## Strumieniowanie wywołań narzędzi

Gdy korzystasz z narzędzi ze strumieniowaniem, model generuje wywołania funkcji jako sekwencję zdarzeń `step.delta` w strumieniu. Argumenty narzędzia można przesyłać strumieniowo jako argumenty częściowe za pomocą funkcji `arguments`. Przed wykonaniem wywołań narzędzi musisz zagregować te zmiany, aby odtworzyć pełne wywołania.

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
  -H "Api-Revision: 2026-05-20" \
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

## Sprawdzone metody

- **Opisy funkcji i parametrów:** podawaj jasne i konkretne informacje.
- **Nazewnictwo:** używaj opisowych nazw bez spacji i znaków specjalnych.
- **Silne typowanie:** używaj konkretnych typów (liczba całkowita, ciąg znaków, wyliczenie).
- **Wybór narzędzi:** utrzymuj aktywny zestaw na poziomie maksymalnie 10–20 narzędzi.
- **Inżynieria promptów:** podaj kontekst i instrukcje.
- **Weryfikacja:** weryfikuj wywołania funkcji przed ich wykonaniem.
- **Obsługa błędów:** wdróż niezawodną obsługę błędów.
- **Bezpieczeństwo:** używaj odpowiedniego uwierzytelniania w przypadku zewnętrznych interfejsów API.

## Uwagi i ograniczenia

- Obsługiwany jest tylko [podzbiór schematu OpenAPI](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=pl#FunctionDeclaration).
- W przypadku trybu `any` interfejs API może odrzucać bardzo duże lub głęboko zagnieżdżone schematy.
- Obsługiwane typy parametrów w Pythonie są ograniczone.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-19 UTC."],[],[]]
