---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=pl
fetched_at: 2026-08-17T02:25:52.834273+00:00
title: "Wywo\u0142ywanie funkcji za pomoc\u0105 interfejsu Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wywoływanie funkcji za pomocą interfejsu Gemini API

Wywoływanie funkcji umożliwia łączenie modeli z narzędziami zewnętrznymi i interfejsami API.
Zamiast generować odpowiedzi tekstowe, model określa, kiedy wywołać określone funkcje, i podaje niezbędne parametry do wykonania działań w rzeczywistym świecie.
Dzięki temu model może stanowić pomost między językiem naturalnym a rzeczywistymi działaniami i danymi. Wywoływanie funkcji ma 3 główne zastosowania:

- [**Podejmowanie działań:**](#meeting) wchodzenie w interakcje z systemami zewnętrznymi za pomocą interfejsów API, np. planowanie spotkań, tworzenie faktur, wysyłanie e-maili czy sterowanie inteligentnymi urządzeniami domowymi.
- [**Wzbogacanie wiedzy:**](#weather) dostęp do informacji ze źródeł zewnętrznych, takich jak bazy danych, interfejsy API i bazy wiedzy.
- [**Rozszerzanie możliwości:**](#chart) używaj narzędzi zewnętrznych do wykonywania obliczeń i przekraczania ograniczeń modelu, np. korzystaj z kalkulatora lub twórz wykresy.

Przykłady tych przypadków użycia znajdziesz poniżej:

### Zaplanuj spotkanie

Ten przykład pokazuje, jak zdefiniować funkcję, która planuje spotkanie z uczestnikami o określonej godzinie, umożliwiając modelowi analizowanie żądań użytkowników i zwracanie uporządkowanych argumentów w celu wywoływania działań w systemach zewnętrznych.

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

### Pobierz pogodę

Ten przykład pokazuje, jak zdefiniować funkcję, która pobiera dane o temperaturze w danej lokalizacji, umożliwiając modelowi wywoływanie zewnętrznych interfejsów API w celu odpowiadania na zapytania wymagające informacji w czasie rzeczywistym lub informacji zewnętrznych.

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
weather_function = {
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

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What's the temperature in London?",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = get_current_temperature(**function_call.args)
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
const weatherFunctionDeclaration = {
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      location: {
        type: Type.STRING,
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "What's the temperature in London?",
  config: {
    tools: [{
      functionDeclarations: [weatherFunctionDeclaration]
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
  // const result = await getCurrentTemperature(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "What'\''s the temperature in London?"
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
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

### Utwórz wykres

Ten przykład pokazuje, jak zdefiniować funkcję, która generuje wykres słupkowy na podstawie danych strukturalnych. Pokazuje on, jak model może używać narzędzi zewnętrznych do wykonywania obliczeń lub tworzenia zasobów wizualnych:

### Python

```
import os
from google import genai
from google.genai import types

# Define the function declaration for the model
create_chart_function = {
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and corresponding values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title for the chart.",
            },
            "labels": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of labels for the data points (e.g., ['Q1', 'Q2', 'Q3']).",
            },
            "values": {
                "type": "array",
                "items": {"type": "number"},
                "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).",
            },
        },
        "required": ["title", "labels", "values"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[create_chart_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here using a charting library:
    #  result = create_bar_chart(**function_call.args)
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
const createChartFunctionDeclaration = {
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and corresponding values.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      title: {
        type: Type.STRING,
        description: 'The title for the chart.',
      },
      labels: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of labels for the data points (e.g., ["Q1", "Q2", "Q3"]).',
      },
      values: {
        type: Type.ARRAY,
        items: { type: Type.NUMBER },
        description: 'List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).',
      },
    },
    required: ['title', 'labels', 'values'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.6-flash',
  contents: "Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
  config: {
    tools: [{
      functionDeclarations: [createChartFunctionDeclaration]
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
  // const result = await createBarChart(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Create a bar chart titled ''Quarterly Sales'' with data: Q1: 50000, Q2: 75000, Q3: 60000."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "create_bar_chart",
            "description": "Creates a bar chart given a title, labels, and corresponding values.",
            "parameters": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string",
                  "description": "The title for the chart."
                },
                "labels": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of labels for the data points (e.g., [''Q1'', ''Q2'', ''Q3''])."
                },
                "values": {
                  "type": "array",
                  "items": {"type": "number"},
                  "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000])."
                }
              },
              "required": ["title", "labels", "values"]
            }
          }
        ]
      }
    ]
  }'
```

## Jak działa wywoływanie funkcji

![wywoływanie funkcji
omówienie](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=pl)

Wywoływanie funkcji obejmuje strukturalną interakcję między aplikacją, modelem i funkcjami zewnętrznymi. Oto zestawienie procesu:

1. **Zdefiniuj deklarację funkcji:** zdefiniuj deklarację funkcji w kodzie aplikacji. Deklaracje funkcji opisują nazwę, parametry i przeznaczenie funkcji dla modelu.
2. **Wywoływanie interfejsu API za pomocą deklaracji funkcji:** wysyłaj do modelu prompt użytkownika wraz z deklaracjami funkcji. Analizuje żądanie i określa, czy wywołanie funkcji będzie przydatne. Jeśli tak, odpowiada uporządkowanym obiektem JSON zawierającym nazwę funkcji, argumenty i unikalny identyfikator `id` (ten identyfikator `id` jest teraz zawsze zwracany przez interfejs API w przypadku modeli Gemini 3\*).
3. **Wykonywanie kodu funkcji (Twoja odpowiedzialność):** model *nie* wykonuje samej funkcji. Obowiązkiem aplikacji jest przetworzenie odpowiedzi i sprawdzenie, czy zawiera ona wywołanie funkcji. Jeśli
   - **Tak**: wyodrębnij nazwę, argumenty i `id` funkcji, a następnie wykonaj odpowiednią funkcję w aplikacji.
   - **Nie:** model udzielił bezpośredniej odpowiedzi tekstowej na prompt (w przykładzie ten proces jest mniej podkreślony, ale jest możliwym wynikiem).
4. **Utwórz przyjazną dla użytkownika odpowiedź:** jeśli funkcja została wykonana, przechwyć wynik i odeślij go do modelu, pamiętając o uwzględnieniu pasującego `id` w kolejnej turze rozmowy. Na podstawie wyniku wygeneruje ostateczną, przyjazną dla użytkownika odpowiedź, która będzie zawierać informacje z wywołania funkcji.

Ten proces może się powtarzać wielokrotnie, co umożliwia złożone interakcje i przepływy pracy. Model obsługuje też wywoływanie wielu funkcji w ramach jednej tury ([równoległe wywoływanie funkcji](#parallel_function_calling)), sekwencyjnie ([kompozycyjne wywoływanie funkcji](#compositional_function_calling)) oraz za pomocą wbudowanych narzędzi Gemini ([korzystanie z wielu narzędzi](#native-tools)).

\* **Zawsze mapuj identyfikatory funkcji:** Gemini 3 zawsze zwraca unikalny identyfikator funkcji z każdym wywołaniem funkcji.`id``functionCall` W odpowiedzi umieść dokładnie ten ciąg znaków `id`,`functionResponse` aby model mógł dokładnie przypisać wynik do pierwotnego żądania.

### Krok 1. Zdefiniuj deklarację funkcji

Zdefiniuj w kodzie aplikacji funkcję i jej deklarację, które pozwolą użytkownikom ustawiać wartości światła i wysyłać żądania do interfejsu API. Funkcja ta może wywoływać usługi zewnętrzne lub interfejsy API.

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

### Krok 2. Wywołaj model z deklaracjami funkcji

Po zdefiniowaniu deklaracji funkcji możesz poprosić model o ich użycie. Analizuje prompt i deklaracje funkcji oraz decyduje, czy odpowiedzieć bezpośrednio, czy wywołać funkcję. Jeśli wywoływana jest funkcja, obiekt odpowiedzi będzie zawierać sugestię wywołania funkcji.

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

Model zwraca następnie obiekt `functionCall` w schemacie zgodnym z OpenAPI, który określa, jak wywołać co najmniej jedną zadeklarowaną funkcję, aby odpowiedzieć na pytanie użytkownika.

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

### Krok 3. Wykonaj kod funkcji set\_light\_values

Wyodrębnij szczegóły wywołania funkcji z odpowiedzi modelu, przeanalizuj argumenty i wykonaj funkcję `set_light_values`.

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

### Krok 4. Utwórz przyjazną dla użytkownika odpowiedź z wynikiem funkcji i ponownie wywołaj model

Na koniec wyślij wynik wykonania funkcji z powrotem do modelu, aby mógł on uwzględnić te informacje w ostatecznej odpowiedzi dla użytkownika.

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
    model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

To ostatni element procesu wywoływania funkcji. Modelowi udało się użyć funkcji
`set_light_values` do wykonania działania, o które prosił użytkownik.

## Deklaracje funkcji

Gdy zaimplementujesz wywoływanie funkcji w prompcie, utworzysz obiekt `tools`, który zawiera co najmniej 1 obiekt `function declarations`. Funkcje definiujesz za pomocą kodu JSON, a konkretnie za pomocą [wybranego podzbioru](https://ai.google.dev/api/caching?hl=pl#Schema) formatu [schematu OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Deklaracja pojedynczej funkcji może zawierać te parametry:

- `name` (ciąg znaków): unikalna nazwa funkcji (`get_weather_forecast`,
  `send_email`). Używaj opisowych nazw bez spacji i znaków specjalnych (używaj podkreśleń lub notacji camelCase).
- `description` (string): jasne i szczegółowe wyjaśnienie celu i możliwości funkcji. Jest to kluczowe, aby model wiedział, kiedy użyć funkcji. Podaj szczegółowe informacje i przykłady, jeśli to pomoże („Wyszukuje kina na podstawie lokalizacji i opcjonalnie tytułu filmu, który jest obecnie wyświetlany w kinach”).
- `parameters` (obiekt): określa parametry wejściowe, których oczekuje funkcja.
  - `type` (string): określa ogólny typ danych, np. `object`.
  - `properties` (obiekt): zawiera listę poszczególnych parametrów, z których każdy ma:
    - `type` (string): typ danych parametru, np. `string`, `integer`, `boolean, array`.
    - `description` (string): opis przeznaczenia i formatu parametru. Podaj przykłady i ograniczenia („Miasto i stan, np. „San Francisco, CA” lub kod pocztowy, np. „95616””).
    - `enum` (tablica, opcjonalnie): jeśli wartości parametru pochodzą ze stałego zbioru, użyj „enum”, aby wyświetlić listę dozwolonych wartości zamiast tylko opisywać je w opisie. Zwiększa to dokładność („enum”:
      [„daylight”, „cool”, „warm”]).
  - `required` (tablica): tablica ciągów znaków zawierająca nazwy parametrów, które są wymagane do działania funkcji.

Możesz też tworzyć `FunctionDeclarations` bezpośrednio z funkcji Pythona za pomocą `types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Wywoływanie funkcji za pomocą modeli myślących

Modele Gemini 3 i 2.5 wykorzystują wewnętrzny proces [„myślenia”](https://ai.google.dev/gemini-api/docs/thinking?hl=pl), aby analizować żądania. To znacznie poprawia skuteczność wywoływania funkcji, dzięki czemu model może lepiej określać, kiedy wywołać funkcję i których parametrów użyć. Interfejs Gemini API jest bezstanowy, więc modele używają [sygnatur myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl), aby zachować kontekst w rozmowach wieloetapowych.

Ta sekcja dotyczy zaawansowanego zarządzania sygnaturami myśli i jest potrzebna tylko wtedy, gdy ręcznie tworzysz żądania interfejsu API (np. za pomocą REST) lub manipulujesz historią rozmów.

**Jeśli używasz [pakietów SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=pl) (naszych oficjalnych bibliotek), nie musisz zarządzać tym procesem**. Zestawy SDK automatycznie wykonują niezbędne czynności, jak pokazano we wcześniejszym [przykładzie](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-4).

### Ręczne zarządzanie historią rozmów

Jeśli zmodyfikujesz historię rozmowy ręcznie, zamiast wysyłać [pełną poprzednią odpowiedź](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-4), musisz prawidłowo obsłużyć znak `thought_signature` zawarty w odpowiedzi modelu.

Aby zachować kontekst modelu, postępuj zgodnie z tymi zasadami:

- Zawsze odsyłaj `thought_signature` do modelu w oryginalnym [`Part`](https://ai.google.dev/api?hl=pl#request-body-structure).
- **Zawsze uwzględniaj dokładny `id` z `function_call` w `function_response`, aby interfejs API mógł przypisać wynik do prawidłowego żądania.**
- Nie łącz `Part` zawierającego podpis z `Part`, który go nie zawiera. To
  zaburza kontekst pozycyjny myśli.
- Nie łącz 2 elementów `Parts`, które zawierają podpisy, ponieważ ciągi znaków podpisu nie mogą być scalane.

#### Sygnatury myśli Gemini 3

W Gemini 3 każdy [`Part`](https://ai.google.dev/api?hl=pl#request-body-structure) odpowiedzi modelu może zawierać podpis myśli.
Zalecamy zwracanie sygnatur wszystkich typów `Part`, ale w przypadku wywoływania funkcji przekazywanie sygnatur myśli jest obowiązkowe. O ile nie manipulujesz historią rozmów ręcznie, pakiet Google GenAI SDK będzie automatycznie obsługiwać sygnatury myśli.

Jeśli ręcznie manipulujesz historią rozmów, zapoznaj się ze stroną [Podpisy myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl), aby uzyskać pełne wskazówki i szczegółowe informacje o obsłudze podpisów myśli w przypadku Gemini 3.

##### Sprawdzanie podpisów myśli

Nie jest to konieczne do wdrożenia, ale możesz sprawdzić odpowiedź, aby zobaczyć `thought_signature` na potrzeby debugowania lub edukacyjne.

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

Więcej informacji o ograniczeniach i używaniu sygnatur myśli oraz o modelach myślenia znajdziesz na stronie [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#signatures).

## Równoległe wywoływanie funkcji

Oprócz wywoływania pojedynczych funkcji możesz też wywoływać wiele funkcji jednocześnie. Równoległe wywoływanie funkcji umożliwia wykonywanie wielu funkcji jednocześnie i jest używane, gdy funkcje nie są od siebie zależne. Jest to przydatne w sytuacjach takich jak zbieranie danych z wielu niezależnych źródeł, np. pobieranie szczegółów klientów z różnych baz danych, sprawdzanie poziomu zapasów w różnych magazynach lub wykonywanie wielu działań, takich jak przekształcenie mieszkania w dyskotekę.

Jeśli model inicjuje wiele wywołań funkcji w jednej turze, nie musisz zwracać obiektów `function_result` w tej samej kolejności, w jakiej zostały odebrane obiekty `function_call`. Interfejs Gemini API mapuje każdy wynik z powrotem na odpowiednie wywołanie za pomocą parametru `id` z danych wyjściowych modelu. Dzięki temu możesz wykonywać funkcje asynchronicznie i dołączać wyniki do listy po ich zakończeniu.

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

Skonfiguruj tryb wywoływania funkcji, aby umożliwić korzystanie ze wszystkich określonych narzędzi.
Więcej informacji znajdziesz w artykule o [konfigurowaniu wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#function_calling_modes).

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

chat = client.chats.create(model="gemini-3.6-flash", config=config)
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
    model: 'gemini-3.6-flash',
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

Każdy z wydrukowanych wyników odzwierciedla pojedyncze wywołanie funkcji, o które poprosił model. Aby odesłać wyniki, umieść odpowiedzi w tej samej kolejności, w jakiej zostały przesłane w żądaniu.

Pakiet Python SDK obsługuje [automatyczne wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#automatic_function_calling_python_only), które automatycznie przekształca funkcje Pythona w deklaracje i obsługuje cykl wykonywania wywołań funkcji i odpowiedzi. Poniżej znajdziesz przykład dla przypadku użycia disco.

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
    model="gemini-3.6-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Wywoływanie funkcji kompozycyjnych

Kompozycyjne lub sekwencyjne wywoływanie funkcji umożliwia Gemini łączenie ze sobą wielu wywołań funkcji w celu realizacji złożonej prośby. Na przykład, aby odpowiedzieć na pytanie „Jaka jest temperatura w mojej bieżącej lokalizacji?”, interfejs Gemini API może najpierw wywołać funkcję `get_current_location()`, a potem funkcję `get_weather()`, która przyjmuje lokalizację jako parametr.

Poniższy przykład pokazuje, jak zaimplementować wywoływanie funkcji kompozycyjnych za pomocą pakietu SDK Pythona i automatycznego wywoływania funkcji.

### Python

W tym przykładzie użyto funkcji automatycznego wywoływania funkcji w `google-genai`pakiecie Python SDK. Pakiet SDK automatycznie przekształca funkcje Pythona w wymagany schemat, wykonuje wywołania funkcji na żądanie modelu i wysyła wyniki z powrotem do modelu, aby dokończyć zadanie.

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
    model="gemini-3.6-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Oczekiwane dane wyjściowe**

Po uruchomieniu kodu zobaczysz, jak pakiet SDK koordynuje wywołania funkcji. Model najpierw wywołuje funkcję `get_weather_forecast`, otrzymuje temperaturę, a następnie wywołuje funkcję `set_thermostat_temperature` z prawidłową wartością na podstawie logiki w prompcie.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

Ten przykład pokazuje, jak używać pakietu SDK JavaScript/TypeScript do wywoływania funkcji kompozycyjnych za pomocą ręcznej pętli wykonywania.

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
    model: "gemini-3.6-flash",
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

**Oczekiwane dane wyjściowe**

Po uruchomieniu kodu zobaczysz, jak pakiet SDK koordynuje wywołania funkcji. Model najpierw wywołuje funkcję `get_weather_forecast`, otrzymuje temperaturę, a następnie wywołuje funkcję `set_thermostat_temperature` z prawidłową wartością na podstawie logiki w prompcie.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

Kompozycyjne wywoływanie funkcji to natywna funkcja [Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl). Oznacza to, że Live API może obsługiwać wywoływanie funkcji podobnie jak pakiet SDK w Pythonie.

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

## Tryby wywoływania funkcji

Interfejs Gemini API umożliwia kontrolowanie sposobu, w jaki model korzysta z udostępnionych narzędzi (deklaracji funkcji). Tryb możesz ustawić w sekcji`function_calling_config`.

- `VALIDATED`: domyślny tryb łączenia narzędzi (gdy włączone są też wbudowane narzędzia lub dane wyjściowe w formie strukturalnej). Model jest ograniczony do przewidywania wywołań funkcji lub języka naturalnego i zapewnia zgodność ze schematem funkcji. Jeśli nie podasz parametru `allowed_function_names`, model wybierze jedną z dostępnych deklaracji funkcji. Jeśli podano `allowed_function_names`, model wybiera z zestawu dozwolonych funkcji. Ten tryb zmniejsza liczbę nieprawidłowych wywołań funkcji (w porównaniu z trybem `AUTO`).
- `AUTO`: domyślny tryb, gdy włączone jest tylko narzędzie function\_declarations.
  Model decyduje, czy wygenerować odpowiedź w języku naturalnym, czy zaproponować wywołanie funkcji na podstawie prompta i kontekstu.
- `ANY`: model jest ograniczony do zawsze przewidywania wywołania funkcji i zapewnia zgodność ze schematem funkcji. Jeśli nie podasz `allowed_function_names`, model może wybrać dowolną z podanych deklaracji funkcji.
  Jeśli `allowed_function_names` jest podana jako lista, model może wybierać tylko funkcje z tej listy. Użyj tego trybu, gdy w przypadku każdego promptu wymagana jest odpowiedź wywołania funkcji (w stosownych przypadkach).
- `NONE`: model *nie może* wywoływać funkcji. Jest to równoznaczne z wysłaniem żądania bez deklaracji funkcji. Użyj tej opcji, aby tymczasowo wyłączyć wywoływanie funkcji bez usuwania definicji narzędzi.

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

## Automatyczne wywoływanie funkcji (tylko Python)

Jeśli używasz pakietu Python SDK, możesz udostępniać funkcje Pythona bezpośrednio jako narzędzia.
Pakiet SDK przekształca te funkcje w deklaracje, zarządza wykonywaniem wywołań funkcji i obsługuje cykl odpowiedzi. Zdefiniuj funkcję za pomocą wskazówek dotyczących typu i ciągu dokumentującego. Aby uzyskać optymalne wyniki, zalecamy używanie [ciągów dokumentujących w stylu Google](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).
Pakiet SDK automatycznie:

1. wykrywać odpowiedzi modelu na wywołanie funkcji;
2. Wywołaj w kodzie odpowiednią funkcję Pythona.
3. Wyślij odpowiedź funkcji z powrotem do modelu.
4. Zwraca ostateczną odpowiedź tekstową modelu.

Pakiet SDK nie analizuje obecnie opisów argumentów w celu umieszczenia ich w polach opisu właściwości wygenerowanej deklaracji funkcji. Zamiast tego wysyła cały ciąg dokumentu jako opis funkcji najwyższego poziomu.

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
    model="gemini-3.6-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

Automatyczne wywoływanie funkcji możesz wyłączyć za pomocą tego kodu:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Automatyczna deklaracja schematu funkcji

Interfejs API może opisywać dowolny z tych typów. Dozwolone są typy `Pydantic`, o ile zdefiniowane w nich pola również składają się z dozwolonych typów. Typy słownikowe (np. `dict[str: int]`) nie są tutaj dobrze obsługiwane, więc nie używaj ich.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Aby zobaczyć, jak wygląda wywnioskowany schemat, możesz go przekonwertować za pomocą tego polecenia:[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable)

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

## Korzystanie z wielu narzędzi: łączenie wbudowanych narzędzi z wywoływaniem funkcji

Możesz włączyć wiele narzędzi, łącząc narzędzia wbudowane z wywoływaniem funkcji w tym samym żądaniu.

Modele Gemini 3 mogą łączyć wbudowane narzędzia z wywoływaniem funkcji od razu po wyjęciu z pudełka dzięki funkcji obiegu kontekstu narzędzia. Więcej informacji znajdziesz na stronie [Łączenie wbudowanych narzędzi i wywoływania funkcji](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

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
    model="gemini-3.6-flash",
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
    model="gemini-3.6-flash",
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
        model: "gemini-3.6-flash",
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

W przypadku modeli starszych niż seria Gemini 3 użyj [interfejsu Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=pl).

## Odpowiedzi funkcji multimodalnych

W przypadku modeli z serii Gemini 3 możesz uwzględniać treści multimodalne w częściach odpowiedzi funkcji, które wysyłasz do modelu. Model może przetworzyć te treści multimodalne w kolejnej turze, aby wygenerować bardziej przemyślaną odpowiedź.
W przypadku treści multimodalnych w odpowiedziach funkcji obsługiwane są te typy MIME:

- **Grafika:** `image/png`, `image/jpeg`, `image/webp`
- **Dokumenty:** `application/pdf`, `text/plain`

Aby uwzględnić dane multimodalne w odpowiedzi funkcji, dodaj je jako co najmniej 1 element zagnieżdżony w elemencie `functionResponse`. Każda część multimodalna musi zawierać `inlineData`. Jeśli odwołujesz się do komponentu multimodalnego z poziomu pola strukturalnego `response`, musi ono zawierać unikalny atrybut `displayName`.

Możesz też odwołać się do części multimodalnej w ramach strukturalnego `response`pola`functionResponse` części, używając formatu odwołania JSON`{"$ref": "<displayName>"}`. Podczas przetwarzania odpowiedzi model zastępuje odniesienie treściami multimodalnymi. Każdy element `displayName` może być przywoływany tylko raz w polu strukturalnym `response`.

Poniższy przykład pokazuje wiadomość zawierającą `functionResponse` dla funkcji o nazwie `get_image` i zagnieżdżoną część zawierającą dane obrazu z `displayName: "instrument.jpg"`. Pole `functionResponse`'s `response` odnosi się do tej części obrazu:

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
  model="gemini-3.6-flash",
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
  model="gemini-3.6-flash",
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
  model: 'gemini-3.6-flash',
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
  model: 'gemini-3.6-flash',
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## Wywoływanie funkcji z uporządkowanymi danymi wyjściowymi

W przypadku modeli z serii Gemini 3 możesz używać wywoływania funkcji z [danymi wyjściowymi w formacie strukturalnym](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl). Dzięki temu model może przewidywać wywołania funkcji lub dane wyjściowe zgodne z określonym schematem. Dzięki temu otrzymujesz odpowiedzi w spójnym formacie, gdy model nie generuje wywołań funkcji.

## Model Context Protocol (MCP)

[Protokół Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) to otwarty standard łączenia aplikacji AI z narzędziami zewnętrznymi i danymi.
MCP to wspólny protokół, który umożliwia modelom dostęp do kontekstu, takiego jak funkcje (narzędzia), źródła danych (zasoby) lub predefiniowane prompty.

Pakiety SDK Gemini mają wbudowaną obsługę MCP, co zmniejsza ilość powtarzalnego kodu i umożliwia [automatyczne wywoływanie narzędzi](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#automatic_function_calling_python_only) MCP. Gdy model wygeneruje wywołanie narzędzia MCP, pakiet SDK klienta w językach Python i JavaScript może automatycznie wykonać to narzędzie i odesłać odpowiedź do modelu w kolejnym żądaniu. Ta pętla będzie się powtarzać, dopóki model nie wygeneruje kolejnych wywołań narzędzi.

Tutaj znajdziesz przykład użycia lokalnego serwera MCP z Gemini i pakietem SDK`mcp`.

### Python

Sprawdź, czy na wybranej platformie jest zainstalowana najnowsza wersja [`mcp` pakietu SDK](https://modelcontextprotocol.io/introduction).

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
                model="gemini-3.6-flash",
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

Sprawdź, czy na wybranej platformie masz zainstalowaną najnowszą wersję pakietu `mcp` SDK.

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
  model: "gemini-3.6-flash",
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

### Ograniczenia wbudowanej obsługi MCP

Wbudowana obsługa MCP to [eksperymentalna](https://ai.google.dev/gemini-api/docs/models?hl=pl#preview) funkcja w naszych pakietach SDK, która ma te ograniczenia:

- Obsługiwane są tylko narzędzia, a nie zasoby ani prompty
- Jest on dostępny w pakietach SDK w językach Python i JavaScript/TypeScript.
- W kolejnych wersjach mogą wystąpić zmiany powodujące niezgodność.

Jeśli te ograniczenia utrudniają Ci tworzenie, zawsze możesz zintegrować serwery MCP ręcznie.

## Obsługiwane modele

W tej sekcji znajdziesz listę modeli i ich możliwości wywoływania funkcji. Nie obejmuje modeli eksperymentalnych. Szczegółowy przegląd możliwości znajdziesz na stronie [informacji o modelu](https://ai.google.dev/gemini-api/docs/models?hl=pl).

| Model | Wywoływanie funkcji | Równoległe wywoływanie funkcji | Wywoływanie funkcji kompozycyjnych |
| --- | --- | --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Pro (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=pl) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=pl) | ✔️ | ✔️ | ✔️ |

## Sprawdzone metody

- **Opisy funkcji i parametrów:** opisy powinny być bardzo jasne i konkretne. Model korzysta z nich, aby wybrać odpowiednią funkcję i podać właściwe argumenty.
- **Nazewnictwo:** używaj opisowych nazw funkcji (bez spacji, kropek ani myślników).
- **Silne typowanie:** używaj konkretnych typów (liczba całkowita, ciąg znaków, wyliczenie) w przypadku parametrów, aby zmniejszyć liczbę błędów. Jeśli parametr ma ograniczony zestaw prawidłowych wartości, użyj wyliczenia.
- **Wybór narzędzia:** model może używać dowolnej liczby narzędzi, ale podanie zbyt wielu może zwiększyć ryzyko wybrania nieprawidłowego lub nieoptymalnego narzędzia. Aby uzyskać najlepsze wyniki, staraj się udostępniać tylko odpowiednie narzędzia w kontekście danego zadania. Najlepiej, aby aktywny zestaw narzędzi nie przekraczał 10–20. Jeśli masz dużą łączną liczbę narzędzi, rozważ dynamiczne wybieranie narzędzi na podstawie kontekstu rozmowy.
- **Inżynieria promptów:**
  - Podaj kontekst: określ rolę modelu (np. „Jesteś pomocnym asystentem pogodowym”).
  - Podaj instrukcje: określ, jak i kiedy używać funkcji (np. „Nie zgaduj dat. W przypadku prognoz zawsze używaj daty przyszłej”).
  - Zachęcaj do wyjaśnień: poproś model, aby w razie potrzeby zadawał pytania wyjaśniające.
  - Więcej strategii projektowania tych promptów znajdziesz w artykule [Przepływy pracy oparte na agentach](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl#agentic-workflows). Oto przykład przetestowanej [instrukcji systemowej](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl#agentic-si-template).
- **Temperatura:** używaj niskiej temperatury (np. 0), aby uzyskać bardziej deterministyczne i niezawodne wywołania funkcji.
- **Weryfikacja:** jeśli wywołanie funkcji ma istotne konsekwencje (np. złożenie zamówienia), przed jego wykonaniem poproś użytkownika o potwierdzenie.
- **Sprawdź przyczynę zakończenia:** zawsze sprawdzaj [`finishReason`](https://ai.google.dev/api/generate-content?hl=pl#FinishReason) w odpowiedzi modelu, aby obsługiwać przypadki, w których model nie wygenerował prawidłowego wywołania funkcji.
- **Obsługa błędów:** zaimplementuj w funkcjach niezawodną obsługę błędów, aby prawidłowo obsługiwać nieoczekiwane dane wejściowe lub awarie interfejsu API. Zwracaj informacyjne komunikaty o błędach, których model może używać do generowania przydatnych odpowiedzi dla użytkownika.
- **Bezpieczeństwo:** zachowaj ostrożność podczas wywoływania zewnętrznych interfejsów API. Używaj odpowiednich mechanizmów uwierzytelniania i autoryzacji. Unikaj ujawniania danych wrażliwych w wywołaniach funkcji.
- **Limity tokenów:** opisy funkcji i parametry wliczają się do limitu tokenów wejściowych. Jeśli osiągasz limity tokenów, rozważ ograniczenie liczby funkcji lub długości opisów albo podziel złożone zadania na mniejsze, bardziej szczegółowe zestawy funkcji.
- **Połączenie narzędzi bash i niestandardowych**: dla osób, które korzystają z połączenia narzędzi bash i niestandardowych, Gemini 3.1 Pro (wersja testowa) udostępnia oddzielny punkt końcowy dostępny przez interfejs API o nazwie [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=pl#gemini-31-pro-preview-customtools).

## Obejścia wymagań dotyczących tekstu przed narzędziem

**Problem:** jeśli prompt wymaga od modelu wygenerowania tekstu strukturalnego (XML, YAML, JSON itp.). (np. `<UPDATE>...</UPDATE>`) bezpośrednio przed wywołaniem narzędzia, wywołanie narzędzia może czasami zakończyć się niepowodzeniem z błędem `Malformed_Function_Call`.

**Rozwiązania:** ten problem można rozwiązać za pomocą tych obejść:

- **ZALECANE:** poinstruuj model, aby umieszczał notatki przed użyciem narzędzia w wywołaniu funkcji `update()` zamiast w postaci zwykłego tekstu (szczegóły poniżej).
- Poproś model o zapisywanie notatek jako nagłówków Markdown (`# UPDATE`, `## PLAN`) zamiast tekstu strukturalnego.
- Nie wymagaj od modelu generowania tekstu przed wywołaniami narzędzi.

### Preferowane obejście: umieść notatki robocze w wywołaniu funkcji

Zamiast oryginalnej instrukcji:

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags with<in `UP>DATE`.
```

Skorzystaj z tej zaktualizowanej instrukcji:

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

i zaktualizować wszystkie odwołania do starego formatu XML `<UPDATE>` w żądaniu klienta. Następnie dodaj odpowiednią deklarację funkcji aktualizacji:

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

Następnie w tym samym kroku model wykona 2 wywołania: wywołanie `update()`, które zastępuje strukturalny kod XML, oraz rzeczywiste wywołanie funkcji, które chce wykonać.

## Uwagi i ograniczenia

- Pozycjonowanie części wywołania funkcji: gdy używasz deklaracji funkcji niestandardowych [wraz z narzędziami wbudowanymi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl) (takimi jak wyszukiwarka Google), model może w jednej turze zwracać części `functionCall`, `toolCall` i `toolResponse`. Z tego powodu nie zakładaj, że `functionCall` zawsze będzie ostatnim elementem w tablicy części. Jeśli ręcznie analizujesz odpowiedź JSON, zawsze iteruj po tablicy części, zamiast polegać na pozycji.
- Obsługiwany jest tylko [podzbiór schematu OpenAPI](https://ai.google.dev/api/caching?hl=pl#FunctionDeclaration).
- W przypadku trybu `ANY` interfejs API może odrzucać bardzo duże lub głęboko zagnieżdżone schematy. Jeśli napotkasz błędy, spróbuj uprościć schematy parametrów funkcji i odpowiedzi, skracając nazwy właściwości, zmniejszając zagnieżdżenie lub ograniczając liczbę deklaracji funkcji.
- Obsługiwane typy parametrów w Pythonie są ograniczone.
- Automatyczne wywoływanie funkcji jest dostępne tylko w pakiecie Python SDK.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
