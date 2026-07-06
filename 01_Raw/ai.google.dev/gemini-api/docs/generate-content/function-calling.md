---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/function-calling?hl=fr
fetched_at: 2026-07-06T05:08:25.236164+00:00
title: "Appel de fonction avec l'API Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Appel de fonction avec l'API Gemini

L'appel de fonction vous permet de connecter des modèles à des outils et API externes.
Au lieu de générer des réponses textuelles, le modèle détermine quand appeler des fonctions spécifiques et fournit les paramètres nécessaires pour exécuter des actions concrètes.
Cela permet au modèle de servir de passerelle entre le langage naturel et les actions et données réelles. L'appel de fonctions présente trois principaux cas d'utilisation :

- [**Effectuer des actions**](#meeting) : interagir avec des systèmes externes à l'aide d'API, par exemple pour planifier des rendez-vous, créer des factures, envoyer des e-mails ou contrôler des appareils domotiques.
- [**Augmenter les connaissances**](#weather) : accéder à des informations provenant de sources externes telles que des bases de données, des API et des bases de connaissances.
- [**Étendre les capacités**](#chart) : utilisez des outils externes pour effectuer des calculs et étendre les limites du modèle, par exemple en utilisant une calculatrice ou en créant des graphiques.

Vous trouverez ci-dessous des exemples de ces cas d'utilisation :

### Planifier une réunion

Cet exemple montre comment définir une fonction qui planifie une réunion avec des participants à une heure spécifique, ce qui permet au modèle d'analyser les demandes des utilisateurs et de renvoyer des arguments structurés pour déclencher des actions dans des systèmes externes.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### Obtenir la météo

Cet exemple montre comment définir une fonction qui récupère les données de température pour un lieu, ce qui permet au modèle d'appeler des API externes pour répondre aux requêtes nécessitant des informations externes ou en temps réel.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

### Créer un graphique

Cet exemple montre comment définir une fonction qui génère un graphique à barres à partir de données structurées. Il illustre la façon dont le modèle peut utiliser des outils externes pour effectuer des calculs ou créer des éléments visuels :

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Fonctionnement des appels de fonction

![Présentation de l&#39;appel de fonction](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=fr)

L'appel de fonction implique une interaction structurée entre votre application, le modèle et les fonctions externes. Voici le détail :

1. **Définissez la déclaration de fonction** : définissez la déclaration de fonction dans le code de votre application. Les déclarations de fonction décrivent au modèle le nom, les paramètres et l'objectif de la fonction.
2. **Appeler l'API avec des déclarations de fonctions** : envoyez la requête de l'utilisateur ainsi que la ou les déclarations de fonctions au modèle. Il analyse la requête et détermine si un appel de fonction serait utile. Si c'est le cas, il répond avec un objet JSON structuré contenant le nom de la fonction, les arguments et un `id` unique (ce `id` est désormais toujours renvoyé par l'API pour les modèles Gemini 3\*).
3. **Exécuter le code de la fonction (votre responsabilité)** : le modèle *n'exécute pas* la fonction lui-même. Il incombe à votre application de traiter la réponse et de vérifier s'il y a un appel de fonction. Si
   - **Oui** : extraire le nom, les arguments et `id` de la fonction, puis exécuter la fonction correspondante dans votre application.
   - **Non** : le modèle a fourni une réponse textuelle directe à la requête (ce flux est moins mis en avant dans l'exemple, mais il s'agit d'un résultat possible).
4. **Crée une réponse conviviale** : si une fonction a été exécutée, capture le résultat et renvoie-le au modèle en veillant à inclure le `id` correspondant, lors d'un tour de conversation ultérieur. Il utilisera le résultat pour générer une réponse finale et conviviale qui intègre les informations de l'appel de fonction.

Ce processus peut être répété sur plusieurs tours, ce qui permet des interactions et des workflows complexes. Le modèle permet également d'appeler plusieurs fonctions en un seul tour ([appel de fonction parallèle](#parallel_function_calling)), de manière séquentielle ([appel de fonction compositionnel](#compositional_function_calling)) et avec les outils Gemini intégrés ([utilisation de plusieurs outils](#native-tools)).

\* **Toujours mapper les ID de fonction** : Gemini 3 renvoie désormais toujours un `id` unique avec chaque `functionCall`. Incluez exactement `id` dans votre `functionResponse` afin que le modèle puisse mapper précisément votre résultat à la requête d'origine.

### Étape 1 : Définir une déclaration de fonction

Définissez une fonction et sa déclaration dans le code de votre application pour permettre aux utilisateurs de définir des valeurs de luminosité et d'effectuer une requête d'API. Cette fonction peut appeler des services ou des API externes.

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

### Étape 2 : Appeler le modèle avec les déclarations de fonction

Une fois que vous avez défini vos déclarations de fonctions, vous pouvez demander au modèle de les utiliser. Il analyse le prompt et les déclarations de fonction, et décide s'il doit répondre directement ou appeler une fonction. Si une fonction est appelée, l'objet de réponse contient une suggestion d'appel de fonction.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

Le modèle renvoie ensuite un objet `functionCall` dans un schéma compatible avec OpenAPI, qui indique comment appeler une ou plusieurs des fonctions déclarées pour répondre à la question de l'utilisateur.

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

### Étape 3 : Exécutez le code de la fonction set\_light\_values

Extrayez les détails de l'appel de fonction de la réponse du modèle, analysez les arguments et exécutez la fonction `set_light_values`.

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

### Étape 4 : Créez une réponse conviviale avec le résultat de la fonction et appelez à nouveau le modèle

Enfin, renvoyez le résultat de l'exécution de la fonction au modèle afin qu'il puisse intégrer ces informations dans sa réponse finale à l'utilisateur.

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
    model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

Le flux d'appel de fonction est terminé. Le modèle a utilisé la fonction `set_light_values` pour effectuer l'action demandée par l'utilisateur.

## Déclarations de fonctions

Lorsque vous implémentez l'appel de fonction dans une requête, vous créez un objet `tools`, qui contient un ou plusieurs `function declarations`. Vous définissez des fonctions à l'aide de JSON, en particulier avec un [sous-ensemble sélectionné](https://ai.google.dev/api/caching?hl=fr#Schema) du format de [schéma OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Une déclaration de fonction peut inclure les paramètres suivants :

- `name` (chaîne) : nom unique de la fonction (`get_weather_forecast`, `send_email`). Utilisez des noms descriptifs sans espaces ni caractères spéciaux (utilisez des traits de soulignement ou la casse mixte).
- `description` (chaîne) : explication claire et détaillée de l'objectif et des fonctionnalités de la fonction. C'est essentiel pour que le modèle comprenne quand utiliser la fonction. Soyez précis et fournissez des exemples si nécessaire ("Trouve les cinémas en fonction de la localisation et, éventuellement, du titre du film actuellement à l'affiche.").
- `parameters` (objet) : définit les paramètres d'entrée attendus par la fonction.
  - `type` (chaîne) : spécifie le type de données global, tel que `object`.
  - `properties` (objet) : liste les paramètres individuels, chacun avec les éléments suivants :
    - `type` (chaîne) : type de données du paramètre, tel que `string`, `integer` ou `boolean, array`.
    - `description` (chaîne) : description de l'objectif et du format du paramètre. Fournis des exemples et des contraintes ("La ville et l'État, par exemple "San Francisco, CA", ou un code postal, par exemple "95616"").
    - `enum` (tableau, facultatif) : si les valeurs des paramètres proviennent d'un ensemble fixe, utilisez "enum" pour lister les valeurs autorisées au lieu de simplement les décrire dans la description. Cela améliore la précision ("enum":
      ["daylight", "cool", "warm"]).
  - `required` (tableau) : tableau de chaînes listant les noms des paramètres obligatoires pour le bon fonctionnement de la fonction.

Vous pouvez également construire des `FunctionDeclarations` à partir de fonctions Python directement à l'aide de `types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Appel de fonction avec des modèles à raisonnement

Les modèles des séries Gemini 3 et 2.5 utilisent un processus de [raisonnement](https://ai.google.dev/gemini-api/docs/thinking?hl=fr) interne pour traiter les requêtes. Cela améliore considérablement les performances des appels de fonction, ce qui permet au modèle de mieux déterminer quand appeler une fonction et quels paramètres utiliser. Étant donné que l'API Gemini est sans état, les modèles utilisent des [signatures de pensée](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr) pour conserver le contexte dans les conversations multitours.

Cette section traite de la gestion avancée des signatures de pensée. Elle n'est nécessaire que si vous créez manuellement des requêtes API (par exemple, via REST) ou si vous manipulez l'historique des conversations.

**Si vous utilisez les [SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=fr) (nos bibliothèques officielles), vous n'avez pas besoin de gérer ce processus.** Les SDK gèrent automatiquement les étapes nécessaires, comme indiqué dans l'[exemple](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#step-4) précédent.

### Gérer manuellement l'historique des conversations

Si vous modifiez manuellement l'historique des conversations au lieu d'envoyer la [réponse précédente complète](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#step-4), vous devez gérer correctement le `thought_signature` inclus dans le tour du modèle.

Suivez ces règles pour vous assurer que le contexte du modèle est préservé :

- Renvoie toujours le `thought_signature` au modèle dans son [`Part`](https://ai.google.dev/api?hl=fr#request-body-structure) d'origine.
- **Incluez toujours le `id` exact du `function_call` dans votre `function_response` afin que l'API puisse mapper le résultat à la requête appropriée.**
- Ne fusionnez pas un `Part` contenant une signature avec un autre qui n'en contient pas. Cela rompt le contexte positionnel de la pensée.
- Ne combinez pas deux `Parts` contenant des signatures, car les chaînes de signature ne peuvent pas être fusionnées.

#### Signatures de réflexion Gemini 3

Dans Gemini 3, tout [`Part`](https://ai.google.dev/api?hl=fr#request-body-structure) d'une réponse de modèle peut contenir une signature de pensée.
Bien que nous recommandions généralement de renvoyer des signatures de tous les types `Part`, il est obligatoire de renvoyer des signatures de réflexion pour l'appel de fonction. Sauf si vous manipulez manuellement l'historique des conversations, le SDK Google GenAI gérera automatiquement les signatures de pensée.

Si vous manipulez l'historique des conversations manuellement, consultez la page [Signatures de pensée](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=fr) pour obtenir des conseils complets et des informations sur la gestion des signatures de pensée pour Gemini 3.

##### Inspecter les signatures de réflexion

Bien que cela ne soit pas nécessaire pour l'implémentation, vous pouvez inspecter la réponse pour voir le `thought_signature` à des fins de débogage ou pédagogiques.

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

Pour en savoir plus sur les limites et l'utilisation des signatures de pensée, ainsi que sur les modèles de pensée en général, consultez la page [Pensée](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#signatures).

## Appel de fonction en parallèle

En plus de l'appel de fonction unique, vous pouvez également appeler plusieurs fonctions à la fois. L'appel de fonction parallèle vous permet d'exécuter plusieurs fonctions à la fois. Il est utilisé lorsque les fonctions ne sont pas dépendantes les unes des autres. Cela peut être utile dans des scénarios tels que la collecte de données provenant de plusieurs sources indépendantes (par exemple, la récupération des informations client à partir de différentes bases de données ou la vérification des niveaux d'inventaire dans différents entrepôts) ou l'exécution de plusieurs actions (par exemple, transformer votre appartement en discothèque).

Lorsque le modèle lance plusieurs appels de fonction en un seul tour, vous n'avez pas besoin de renvoyer les objets `function_result` dans le même ordre que celui dans lequel les objets `function_call` ont été reçus. L'API Gemini associe chaque résultat à l'appel correspondant à l'aide de `id` à partir de la sortie du modèle. Cela vous permet d'exécuter vos fonctions de manière asynchrone et d'ajouter les résultats à votre liste à mesure qu'ils sont terminés.

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

Configurez le mode d'appel de fonction pour autoriser l'utilisation de tous les outils spécifiés.
Pour en savoir plus, consultez [Configurer l'appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#function_calling_modes).

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

chat = client.chats.create(model="gemini-3.5-flash", config=config)
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
    model: 'gemini-3.5-flash',
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

Chacun des résultats imprimés reflète un seul appel de fonction demandé par le modèle. Pour renvoyer les résultats, incluez les réponses dans le même ordre que celui dans lequel elles ont été demandées.

Le SDK Python est compatible avec l'[appel de fonction automatique](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#automatic_function_calling_python_only), qui convertit automatiquement les fonctions Python en déclarations et gère le cycle d'exécution et de réponse des appels de fonction pour vous. Voici un exemple pour le cas d'utilisation de la découverte.

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
    model="gemini-3.5-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Appel de fonction compositionnel

L'appel de fonction compositionnel ou séquentiel permet à Gemini d'associer plusieurs appels de fonction pour répondre à une requête complexe. Par exemple, pour répondre à la requête "Obtiens la température à mon emplacement actuel", l'API Gemini peut d'abord appeler une fonction `get_current_location()`, puis une fonction `get_weather()` qui prend l'emplacement comme paramètre.

L'exemple suivant montre comment implémenter l'appel de fonction compositionnel à l'aide du SDK Python et de l'appel de fonction automatique.

### Python

Cet exemple utilise la fonctionnalité d'appel de fonction automatique du SDK Python `google-genai`. Le SDK convertit automatiquement les fonctions Python au schéma requis, exécute les appels de fonction lorsque le modèle le demande et renvoie les résultats au modèle pour terminer la tâche.

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
    model="gemini-3.5-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Résultat attendu**

Lorsque vous exécutez le code, vous voyez le SDK orchestrer les appels de fonction. Le modèle appelle d'abord `get_weather_forecast`, reçoit la température, puis appelle `set_thermostat_temperature` avec la valeur correcte en fonction de la logique de la requête.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

Cet exemple montre comment utiliser le SDK JavaScript/TypeScript pour effectuer un appel de fonction de composition à l'aide d'une boucle d'exécution manuelle.

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
    model: "gemini-3.5-flash",
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

**Résultat attendu**

Lorsque vous exécutez le code, vous voyez le SDK orchestrer les appels de fonction. Le modèle appelle d'abord `get_weather_forecast`, reçoit la température, puis appelle `set_thermostat_temperature` avec la valeur correcte en fonction de la logique de la requête.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

L'appel de fonction compositionnel est une fonctionnalité native de l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr). Cela signifie que l'API Live peut gérer les appels de fonction de la même manière que le SDK Python.

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

## Modes d'appel de fonction

L'API Gemini vous permet de contrôler la façon dont le modèle utilise les outils fournis (déclarations de fonction). Plus précisément, vous pouvez définir le mode dans le fichier.`function_calling_config`.

- `VALIDATED` : mode par défaut pour la combinaison d'outils (lorsque les outils intégrés ou les sorties structurées sont également activés). Le modèle est contraint de prédire des appels de fonction ou du langage naturel, et garantit le respect du schéma de fonction. Si `allowed_function_names` n'est pas fourni, le modèle sélectionne toutes les déclarations de fonction disponibles. Si `allowed_function_names` est fourni, le modèle choisit parmi l'ensemble de fonctions autorisées. Ce mode réduit les appels de fonction mal formés (par rapport au mode `AUTO`).
- `AUTO` : mode par défaut lorsque seul l'outil function\_declarations est activé.
  Le modèle décide s'il faut générer une réponse en langage naturel ou suggérer un appel de fonction en fonction de la requête et du contexte.
- `ANY` : le modèle est contraint de toujours prédire un appel de fonction et garantit le respect du schéma de la fonction. Si `allowed_function_names` n'est pas spécifié, le modèle peut choisir parmi l'une des déclarations de fonction fournies.
  Si `allowed_function_names` est fourni sous forme de liste, le modèle ne peut choisir que parmi les fonctions de cette liste. Utilisez ce mode lorsque vous avez besoin d'une réponse d'appel de fonction pour chaque requête (le cas échéant).
- `NONE` : le modèle est *interdit* d'effectuer des appels de fonction. Cela équivaut à envoyer une requête sans aucune déclaration de fonction. Utilisez cette option pour désactiver temporairement l'appel de fonction sans supprimer vos définitions d'outils.

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

## Appel de fonction automatique (Python uniquement)

Lorsque vous utilisez le SDK Python, vous pouvez fournir des fonctions Python directement en tant qu'outils.
Le SDK convertit ces fonctions en déclarations, gère l'exécution des appels de fonction et gère le cycle de réponse pour vous. Définissez votre fonction avec des indications de type et une docstring. Pour des résultats optimaux, nous vous recommandons d'utiliser des [docstrings de style Google](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).
Le SDK effectue ensuite automatiquement les opérations suivantes :

1. Détectez les réponses d'appel de fonction du modèle.
2. Appelez la fonction Python correspondante dans votre code.
3. Renvoyez la réponse de la fonction au modèle.
4. Renvoie la réponse textuelle finale du modèle.

Actuellement, le SDK n'analyse pas les descriptions des arguments dans les emplacements de description des propriétés de la déclaration de fonction générée. Au lieu de cela, il envoie l'intégralité de la docstring comme description de la fonction de premier niveau.

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
    model="gemini-3.5-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

Vous pouvez désactiver l'appel de fonction automatique avec :

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Déclaration automatique du schéma de fonction

L'API est capable de décrire les types suivants. Les types `Pydantic` sont autorisés, à condition que les champs définis sur eux soient également composés de types autorisés. Les types de dictionnaire (comme `dict[str: int]`) ne sont pas bien pris en charge ici. N'utilisez pas ces types.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Pour voir à quoi ressemble le schéma inféré, vous pouvez le convertir à l'aide de [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable) :

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

## Utilisation de plusieurs outils : combiner des outils intégrés avec l'appel de fonction

Vous pouvez activer plusieurs outils, en combinant des outils intégrés avec l'appel de fonction dans la même requête.

Les modèles Gemini 3 peuvent combiner des outils intégrés avec l'appel de fonction prêt à l'emploi, grâce à la fonctionnalité de circulation du contexte des outils. Pour en savoir plus, consultez la page [Combiner les outils intégrés et l'appel de fonction](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr).

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
    model="gemini-3.5-flash",
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
    model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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

Pour les modèles antérieurs à la gamme Gemini 3, utilisez l'[API Live](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=fr).

## Réponses de fonction multimodales

Pour les modèles de la série Gemini 3, vous pouvez inclure du contenu multimodal dans les parties de réponse de fonction que vous envoyez au modèle. Le modèle peut traiter ce contenu multimodal lors de son prochain tour pour produire une réponse plus pertinente.
Les types MIME suivants sont acceptés pour le contenu multimodal dans les réponses de fonction :

- **Images** : `image/png`, `image/jpeg`, `image/webp`
- **Documents** : `application/pdf`, `text/plain`

Pour inclure des données multimodales dans une réponse de fonction, ajoutez-les sous forme d'une ou plusieurs parties imbriquées dans la partie `functionResponse`. Chaque partie multimodale doit contenir `inlineData`. Si vous référencez une partie multimodale à partir du champ `response` structuré, elle doit contenir un `displayName` unique.

Vous pouvez également référencer une partie multimodale à partir du champ `response` structuré de la partie `functionResponse` en utilisant le format de référence JSON `{"$ref": "<displayName>"}`. Le modèle remplace la référence par le contenu multimodal lorsqu'il traite la réponse. Chaque `displayName` ne peut être référencé qu'une seule fois dans le champ `response` structuré.

L'exemple suivant montre un message contenant un `functionResponse` pour une fonction nommée `get_image` et une partie imbriquée contenant des données d'image avec `displayName: "instrument.jpg"`. Le champ `response` de `functionResponse` fait référence à cette partie de l'image :

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
  model="gemini-3.5-flash",
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
  model="gemini-3.5-flash",
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
  model: 'gemini-3.5-flash',
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
  model: 'gemini-3.5-flash',
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

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## Appel de fonction avec sortie structurée

Pour les modèles de la famille Gemini 3, vous pouvez utiliser l'appel de fonction avec une [sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr). Cela permet au modèle de prédire des appels de fonction ou des sorties qui respectent un schéma spécifique. Vous recevez ainsi des réponses mises en forme de manière cohérente lorsque le modèle ne génère pas d'appels de fonction.

## Protocole MCP (Model Context Protocol)

Le [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) est une norme ouverte permettant de connecter des applications d'IA à des outils et des données externes.
Le protocole MCP fournit un protocole commun permettant aux modèles d'accéder au contexte, comme les fonctions (outils), les sources de données (ressources) ou les requêtes prédéfinies.

Les SDK Gemini sont compatibles avec le MCP, ce qui réduit le code récurrent et offre l'[appel d'outil automatique](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#automatic_function_calling_python_only) pour les outils MCP. Lorsque le modèle génère un appel d'outil MCP, les SDK clients Python et JavaScript peuvent exécuter automatiquement l'outil MCP et renvoyer la réponse au modèle dans une requête ultérieure, en poursuivant cette boucle jusqu'à ce qu'aucun autre appel d'outil ne soit effectué par le modèle.

Vous trouverez ici un exemple d'utilisation d'un serveur MCP local avec Gemini et le SDK `mcp`.

### Python

Assurez-vous que la dernière version du [SDK `mcp`](https://modelcontextprotocol.io/introduction) est installée sur la plate-forme de votre choix.

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
                model="gemini-3.5-flash",
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

Assurez-vous que la dernière version du SDK `mcp` est installée sur la plate-forme de votre choix.

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
  model: "gemini-3.5-flash",
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

### Limites de la compatibilité MCP intégrée

La prise en charge MCP intégrée est une fonctionnalité [expérimentale](https://ai.google.dev/gemini-api/docs/models?hl=fr#preview) dans nos SDK et présente les limites suivantes :

- Seuls les outils sont acceptés, pas les ressources ni les requêtes
- Il est disponible pour les SDK Python et JavaScript/TypeScript.
- Des modifications destructives peuvent se produire dans les prochaines versions.

L'intégration manuelle des serveurs MCP est toujours possible si ces limites vous empêchent de créer ce que vous souhaitez.

## Modèles compatibles

Cette section liste les modèles et leurs capacités d'appel de fonction. Les modèles expérimentaux ne sont pas inclus. Vous trouverez une présentation complète des fonctionnalités sur la page [Présentation du modèle](https://ai.google.dev/gemini-api/docs/models?hl=fr).

| Modèle | Appel de fonction | Appel de fonction en parallèle | Appel de fonction compositionnel |
| --- | --- | --- | --- |
| [Preview Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fr) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=fr) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fr) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fr) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fr) | ✔️ | ✔️ | ✔️ |

## Bonnes pratiques

- **Descriptions des fonctions et des paramètres** : soyez extrêmement clair et précis dans vos descriptions. Le modèle s'appuie sur ces informations pour choisir la bonne fonction et fournir les arguments appropriés.
- **Nommage** : utilisez des noms de fonctions descriptifs (sans espaces, points ni tirets).
- **Typage fort** : utilisez des types spécifiques (entier, chaîne, enum) pour les paramètres afin de réduire les erreurs. Si un paramètre dispose d'un ensemble limité de valeurs valides, utilisez un enum.
- **Sélection d'outils** : bien que le modèle puisse utiliser un nombre arbitraire d'outils, en fournir trop peut augmenter le risque de sélectionner un outil incorrect ou non optimal. Pour obtenir les meilleurs résultats, essayez de ne fournir que les outils pertinents pour le contexte ou la tâche, en gardant idéalement l'ensemble actif à un maximum de 10 à 20. Envisagez de sélectionner des outils de manière dynamique en fonction du contexte de la conversation si vous disposez d'un grand nombre d'outils.
- **Ingénierie des prompts** :
  - Fournissez du contexte : indiquez au modèle son rôle (par exemple, "Vous êtes un assistant météo serviable.").
  - Donnez des instructions : précisez comment et quand utiliser les fonctions (par exemple, "Ne devinez pas les dates. Utilisez toujours une date future pour les prévisions.").
  - Encouragez la clarification : demandez au modèle de poser des questions de clarification si nécessaire.
  - Pour découvrir d'autres stratégies de conception de ces requêtes, consultez [Workflows agentiques](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr#agentic-workflows). Voici un exemple d'[instruction système](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr#agentic-si-template) testée.
- **Température** : utilisez une température basse (par exemple, 0) pour des appels de fonction plus déterministes et fiables.
- **Validation** : si un appel de fonction a des conséquences importantes (par exemple, passer une commande), validez l'appel auprès de l'utilisateur avant de l'exécuter.
- **Vérifier la raison de la fin** : vérifiez toujours [`finishReason`](https://ai.google.dev/api/generate-content?hl=fr#FinishReason) dans la réponse du modèle pour gérer les cas où le modèle n'a pas réussi à générer un appel de fonction valide.
- **Gestion des erreurs** : implémentez une gestion des erreurs robuste dans vos fonctions pour gérer correctement les entrées inattendues ou les échecs d'API. Renvoie des messages d'erreur informatifs que le modèle peut utiliser pour générer des réponses utiles à l'utilisateur.
- **Sécurité** : faites attention à la sécurité lorsque vous appelez des API externes. Utilisez des mécanismes d'authentification et d'autorisation appropriés. Évitez d'exposer des données sensibles dans les appels de fonction.
- **Limites de jetons** : les descriptions et les paramètres des fonctions sont comptabilisés dans la limite de jetons d'entrée. Si vous atteignez les limites de jetons, envisagez de limiter le nombre de fonctions ou la longueur des descriptions, et de décomposer les tâches complexes en ensembles de fonctions plus petits et plus ciblés.
- **Combinaison de bash et d'outils personnalisés** : si vous créez des applications avec une combinaison de bash et d'outils personnalisés, la version Preview de Gemini 3.1 Pro est fournie avec un point de terminaison distinct disponible via l'API, appelé [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fr#gemini-31-pro-preview-customtools).

## Remarques et limites

- Positionnement des parties d'un appel de fonction : lorsque vous utilisez des déclarations de fonction personnalisées [avec des outils intégrés](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fr) (comme la recherche Google), le modèle peut renvoyer un mélange de parties `functionCall`, `toolCall` et `toolResponse` en un seul tour. Par conséquent, ne partez pas du principe que `functionCall` sera toujours le dernier élément du tableau "parts". Si vous analysez manuellement la réponse JSON, parcourez toujours le tableau "parts" plutôt que de vous fier à la position.
- Seul un [sous-ensemble du schéma OpenAPI](https://ai.google.dev/api/caching?hl=fr#FunctionDeclaration) est accepté.
- En mode `ANY`, l'API peut refuser les schémas très volumineux ou profondément imbriqués. Si vous rencontrez des erreurs, essayez de simplifier les schémas des paramètres et des réponses de votre fonction en raccourcissant les noms des propriétés, en réduisant l'imbrication ou en limitant le nombre de déclarations de fonctions.
- Les types de paramètres acceptés dans Python sont limités.
- L'appel de fonction automatique est une fonctionnalité du SDK Python uniquement.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/24 (UTC)."],[],[]]
