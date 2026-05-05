---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419
fetched_at: 2026-05-05T19:50:50.621562+00:00
title: "Llamada a funci\u00f3n con la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Llamada a función con la API de Gemini

La llamada a función te permite conectar modelos a herramientas y APIs externas.
En lugar de generar respuestas de texto, el modelo determina cuándo llamar a funciones específicas y proporciona los parámetros necesarios para ejecutar acciones del mundo real.
Esto permite que el modelo actúe como un puente entre el lenguaje natural y las acciones y los datos del mundo real. Las llamadas a función tienen 3 casos de uso principales:

- **Aumentar el conocimiento:** Accede a información de fuentes externas, como bases de datos, APIs y bases de conocimiento.
- **Extender capacidades:** Usa herramientas externas para realizar cálculos y extender las limitaciones del modelo, como usar una calculadora o crear gráficos.
- **Realizar acciones:** Interactúa con sistemas externos a través de APIs, como programar citas, crear facturas, enviar correos electrónicos o controlar dispositivos inteligentes para la casa.

Get Weather
Schedule Meeting
Create Chart

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

## Cómo funciona la llamada a función

![Descripción general de las llamadas a funciones](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=es-419)

La llamada a funciones implica una interacción estructurada entre tu aplicación, el modelo y las funciones externas. A continuación, se detalla el proceso:

1. **Define la declaración de la función:** Define la declaración de la función en el código de tu aplicación. Las declaraciones de funciones describen el nombre, los parámetros y el propósito de la función al modelo.
2. **Llama a la API con declaraciones de funciones:** Envía la instrucción del usuario junto con las declaraciones de funciones al modelo. Analiza la solicitud y determina si sería útil una llamada a función. Si es así, responde con un objeto JSON estructurado que contiene el nombre de la función, los argumentos y un `id` único (la API siempre devuelve este `id` para los modelos de Gemini 3\*).
3. **Ejecuta el código de la función (es tu responsabilidad):** El modelo *no* ejecuta la función en sí. Es responsabilidad de tu aplicación procesar la respuesta y verificar si hay una llamada a función. Si
   - **Sí**: Extrae el nombre, los argumentos y `id` de la función, y ejecuta la función correspondiente en tu aplicación.
   - **No:** El modelo proporcionó una respuesta de texto directa a la instrucción (este flujo se enfatiza menos en el ejemplo, pero es un resultado posible).
4. **Crea una respuesta fácil de usar:** Si se ejecutó una función, captura el resultado y envíalo de vuelta al modelo. Asegúrate de incluir el `id` coincidente en un turno posterior de la conversación. Usará el resultado para generar una respuesta final y fácil de usar que incorpore la información de la llamada a función.

Este proceso se puede repetir varias veces, lo que permite interacciones y flujos de trabajo complejos. El modelo también admite llamar a varias funciones en un solo turno ([llamada a funciones paralelas](#parallel_function_calling)), en secuencia ([llamada a funciones de composición](#compositional_function_calling)) y con herramientas integradas de Gemini ([uso de varias herramientas](#native-tools)).

\* **Siempre asigna IDs de funciones:** Gemini 3 ahora siempre devuelve un `id` único con cada `functionCall`. Incluye este `id` exacto en tu `functionResponse` para que el modelo pueda asignar con precisión tu resultado a la solicitud original.

### Paso 1: Define una declaración de función

Define una función y su declaración dentro del código de la aplicación que permita a los usuarios establecer valores de luz y realizar una solicitud a la API. Esta función podría llamar a servicios o APIs externos.

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

### Paso 2: Llama al modelo con declaraciones de funciones

Una vez que hayas definido las declaraciones de funciones, puedes indicarle al modelo que las use. Analiza la instrucción y las declaraciones de funciones, y decide si responder directamente o llamar a una función. Si se llama a una función, el objeto de respuesta contendrá una sugerencia de llamada a función.

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

Luego, el modelo devuelve un objeto `functionCall` en un esquema compatible con OpenAPI que especifica cómo llamar a una o más de las funciones declaradas para responder la pregunta del usuario.

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

### Paso 3: Ejecuta el código de la función set\_light\_values

Extrae los detalles de la llamada a función de la respuesta del modelo, analiza los argumentos y ejecuta la función `set_light_values`.

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

### Paso 4: Crea una respuesta fácil de usar con el resultado de la función y vuelve a llamar al modelo

Por último, envía el resultado de la ejecución de la función al modelo para que pueda incorporar esta información en su respuesta final al usuario.

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

Esto completa el flujo de llamadas a funciones. El modelo usó correctamente la función `set_light_values` para realizar la acción de solicitud del usuario.

## Declaraciones de funciones

Cuando implementas la llamada a función en una instrucción, creas un objeto `tools`, que contiene uno o más `function declarations`. Defines funciones con JSON, específicamente con un [subconjunto seleccionado](https://ai.google.dev/api/caching?hl=es-419#Schema) del formato del [esquema de OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Una sola declaración de función puede incluir los siguientes parámetros:

- `name` (cadena): Es un nombre único para la función (`get_weather_forecast`, `send_email`). Usa nombres descriptivos sin espacios ni caracteres especiales (usa guiones bajos o camelCase).
- `description` (cadena): Explicación clara y detallada del propósito y las capacidades de la función. Esto es fundamental para que el modelo comprenda cuándo usar la función. Sé específico y proporciona ejemplos si es útil ("Encuentra cines según la ubicación y, de manera opcional, el título de la película que se está proyectando en los cines").
- `parameters` (objeto): Define los parámetros de entrada que espera la función.
  - `type` (cadena): Especifica el tipo de datos general, como `object`.
  - `properties` (objeto): Enumera parámetros individuales, cada uno con lo siguiente:
    - `type` (cadena): Es el tipo de datos del parámetro, como `string`, `integer` o `boolean, array`.
    - `description` (cadena): Es una descripción del propósito y el formato del parámetro. Proporciona ejemplos y restricciones ("La ciudad y el estado, p. ej., "San Francisco, CA" o un código postal, p. ej., "95616"").
    - `enum` (matriz, opcional): Si los valores del parámetro provienen de un conjunto fijo, usa "enum" para enumerar los valores permitidos en lugar de solo describirlos en la descripción. Esto mejora la precisión ("enum":
      ["daylight", "cool", "warm"]).
  - `required` (matriz): Es una matriz de cadenas que enumera los nombres de los parámetros que son obligatorios para que la función opere.

También puedes construir `FunctionDeclarations` directamente a partir de funciones de Python con `types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Llamada a función con modelos de pensamiento

Los modelos de las series Gemini 3 y 2.5 usan un proceso interno de ["pensamiento"](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419) para razonar las solicitudes. Esto mejora significativamente el rendimiento de las llamadas a funciones, lo que permite que el modelo determine mejor cuándo llamar a una función y qué parámetros usar. Dado que la API de Gemini no tiene estado, los modelos usan [firmas de pensamiento](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=es-419) para mantener el contexto en las conversaciones de varios turnos.

En esta sección, se abarca la administración avanzada de las firmas de pensamiento y solo es necesaria si compilas solicitudes de API de forma manual (p.ej., a través de REST) o manipulas el historial de conversaciones.

**Si usas los [SDKs de IA generativa de Google](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419) (nuestras bibliotecas oficiales), no necesitas administrar este proceso**. Los SDKs controlan automáticamente los pasos necesarios, como se muestra en el [ejemplo](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#step-4) anterior.

### Cómo administrar el historial de conversaciones de forma manual

Si modificas el historial de conversación de forma manual, en lugar de enviar la [respuesta anterior completa](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#step-4), debes controlar correctamente el `thought_signature` incluido en el turno del modelo.

Sigue estas reglas para asegurarte de que se conserve el contexto del modelo:

- Siempre envía el `thought_signature` de vuelta al modelo dentro de su [`Part`](https://ai.google.dev/api?hl=es-419#request-body-structure) original.
- **Siempre incluye el `id` exacto del `function_call` en tu `function_response` para que la API pueda asignar el resultado a la solicitud correcta.**
- No combines un `Part` que contiene una firma con uno que no la tiene. Esto rompe el contexto posicional del pensamiento.
- No combines dos `Parts` que contengan firmas, ya que las cadenas de firma no se pueden combinar.

#### Firmas de pensamiento de Gemini 3

En Gemini 3, cualquier [`Part`](https://ai.google.dev/api?hl=es-419#request-body-structure) de una respuesta del modelo puede contener una firma de pensamiento.
Si bien, en general, recomendamos devolver firmas de todos los tipos `Part`, devolver firmas de pensamiento es obligatorio para la llamada a funciones. A menos que manipules el historial de conversación de forma manual, el SDK de GenAI de Google controlará las firmas de pensamiento automáticamente.

Si manipulas el historial de conversaciones de forma manual, consulta la página [Firmas de pensamientos](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=es-419) para obtener orientación completa y detalles sobre el manejo de las firmas de pensamientos para Gemini 3.

##### Cómo inspeccionar las firmas de pensamiento

Si bien no es necesario para la implementación, puedes inspeccionar la respuesta para ver el `thought_signature` con fines de depuración o educativos.

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

Obtén más información sobre las limitaciones y el uso de las firmas de pensamiento, y sobre los modelos de pensamiento en general, en la página [Pensamiento](https://ai.google.dev/gemini-api/docs/thinking?hl=es-419#signatures).

## Llamada a función paralela

Además de las llamadas a funciones de un solo turno, también puedes llamar a varias funciones a la vez. Las llamadas a funciones paralelas te permiten ejecutar varias funciones a la vez y se usan cuando las funciones no dependen entre sí. Esto es útil en situaciones como la recopilación de datos de varias fuentes independientes, como la recuperación de detalles del cliente de diferentes bases de datos o la verificación de los niveles de inventario en varios almacenes, o la realización de varias acciones, como convertir tu departamento en una discoteca.

Cuando el modelo inicia varias llamadas a funciones en un solo turno, no es necesario que devuelvas los objetos `function_result` en el mismo orden en que se recibieron los objetos `function_call`. La API de Gemini asigna cada resultado a su llamada correspondiente con el `id` de la salida del modelo. Esto te permite ejecutar tus funciones de forma asíncrona y agregar los resultados a tu lista a medida que se completan.

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

Configura el modo de llamada a función para permitir el uso de todas las herramientas especificadas.
Para obtener más información, puedes leer sobre la [configuración de llamadas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#function_calling_modes).

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

Cada uno de los resultados impresos refleja una sola llamada a función que solicitó el modelo. Para devolver los resultados, incluye las respuestas en el mismo orden en que se solicitaron.

El SDK de Python admite las [llamadas automáticas a funciones](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#automatic_function_calling_python_only), que convierten automáticamente las funciones de Python en declaraciones y controlan el ciclo de ejecución y respuesta de las llamadas a funciones por ti. A continuación, se muestra un ejemplo del caso de uso de la discoteca.

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

## Llamada a función compositiva

La composición o la secuencia de llamadas a funciones permite que Gemini encadene varias llamadas a funciones para satisfacer una solicitud compleja. Por ejemplo, para responder "Obtén la temperatura en mi ubicación actual", la API de Gemini podría invocar primero una función `get_current_location()` seguida de una función `get_weather()` que toma la ubicación como parámetro.

En el siguiente ejemplo, se muestra cómo implementar la llamada a función compositiva con el SDK de Python y la llamada a función automática.

### Python

En este ejemplo, se usa la función de llamada automática a funciones del SDK de `google-genai` para Python. El SDK convierte automáticamente las funciones de Python al esquema requerido, ejecuta las llamadas a funciones cuando el modelo lo solicita y envía los resultados al modelo para completar la tarea.

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

**Resultado esperado**

Cuando ejecutes el código, verás que el SDK coordina las llamadas a funciones. Primero, el modelo llama a `get_weather_forecast`, recibe la temperatura y, luego, llama a `set_thermostat_temperature` con el valor correcto según la lógica de la instrucción.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

En este ejemplo, se muestra cómo usar el SDK de JavaScript/TypeScript para realizar llamadas a funciones de composición con un bucle de ejecución manual.

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

**Resultado esperado**

Cuando ejecutes el código, verás que el SDK coordina las llamadas a funciones. Primero, el modelo llama a `get_weather_forecast`, recibe la temperatura y, luego, llama a `set_thermostat_temperature` con el valor correcto según la lógica de la instrucción.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

La llamada a función compositiva es una función nativa de la [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419). Esto significa que la API en vivo puede controlar la llamada a función de manera similar al SDK de Python.

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

## Modos de llamada a función

La API de Gemini te permite controlar cómo el modelo usa las herramientas proporcionadas (declaraciones de funciones). Específicamente, puedes establecer el modo dentro de `function_calling_config`.

- `VALIDATED`: Es el modo predeterminado para la combinación de herramientas (cuando también se habilitan las herramientas integradas o las salidas estructuradas). El modelo está restringido para predecir llamadas a funciones o lenguaje natural, y garantiza el cumplimiento del esquema de funciones. Si no se proporciona `allowed_function_names`, el modelo elige entre todas las declaraciones de funciones disponibles. Si se proporciona `allowed_function_names`, el modelo elige entre el conjunto de funciones permitidas. Este modo reduce las llamadas a funciones con formato incorrecto (en comparación con el modo `AUTO`).
- `AUTO`: Es el modo predeterminado cuando solo está habilitada la herramienta function\_declarations.
  El modelo decide si generar una respuesta de lenguaje natural o sugerir una llamada a función según la instrucción y el contexto.
- `ANY`: El modelo está restringido para predecir siempre una llamada a función y garantiza el cumplimiento del esquema de la función. Si no se especifica `allowed_function_names`, el modelo puede elegir cualquiera de las declaraciones de funciones proporcionadas.
  Si `allowed_function_names` se proporciona como una lista, el modelo solo puede elegir entre las funciones de esa lista. Usa este modo cuando necesites una respuesta de llamada a función para cada instrucción (si corresponde).
- `NONE`: El modelo tiene *prohibido* realizar llamadas a funciones. Esto equivale a enviar una solicitud sin ninguna declaración de función. Usa esta opción para inhabilitar temporalmente las llamadas a funciones sin quitar las definiciones de tus herramientas.

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

## Llamadas automáticas a funciones (solo en Python)

Cuando usas el SDK de Python, puedes proporcionar funciones de Python directamente como herramientas.
El SDK convierte estas funciones en declaraciones, administra la ejecución de la llamada a función y controla el ciclo de respuesta por ti. Define tu función con sugerencias de tipo y una cadena de documentación. Para obtener resultados óptimos, se recomienda usar [docstrings al estilo de Google.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
Luego, el SDK hará lo siguiente automáticamente:

1. Detecta respuestas de llamadas a funciones del modelo.
2. Llama a la función de Python correspondiente en tu código.
3. Envía la respuesta de la función al modelo.
4. Devuelve la respuesta de texto final del modelo.

Actualmente, el SDK no analiza las descripciones de los argumentos en las ranuras de descripción de la propiedad de la declaración de la función generada. En cambio, envía toda la cadena de documentación como la descripción de la función de nivel superior.

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

Puedes inhabilitar las llamadas a funciones automáticas con el siguiente código:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Declaración automática del esquema de la función

La API puede describir cualquiera de los siguientes tipos. Se permiten los tipos `Pydantic`, siempre y cuando los campos definidos en ellos también se compongan de tipos permitidos. Aquí no se admiten bien los tipos de diccionario (como `dict[str: int]`), así que no los uses.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Para ver cómo se ve el esquema inferido, puedes convertirlo con [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

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

## Uso de varias herramientas: Combina herramientas integradas con llamadas a funciones

Puedes habilitar varias herramientas y combinar las integradas con la llamada a funciones en la misma solicitud.

Los modelos de Gemini 3 pueden combinar herramientas integradas con la llamada a función lista para usar, gracias a la función de circulación del contexto de la herramienta. Para obtener más información, consulta la página sobre [cómo combinar herramientas integradas y llamadas a funciones](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

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

Para los modelos anteriores a la serie Gemini 3, usa la [API de Live](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=es-419).

## Respuestas de funciones multimodales

En el caso de los modelos de la serie Gemini 3, puedes incluir contenido multimodal en las partes de la respuesta de la función que envías al modelo. El modelo puede procesar este contenido multimodal en su siguiente turno para producir una respuesta más fundamentada.
Se admiten los siguientes tipos de MIME para el contenido multimodal en las respuestas de funciones:

- **Imágenes**: `image/png`, `image/jpeg`, `image/webp`
- **Documentos**: `application/pdf`, `text/plain`

Para incluir datos multimodales en la respuesta de una función, inclúyelos como una o más partes anidadas dentro de la parte `functionResponse`. Cada parte multimodal debe contener `inlineData`. Si haces referencia a una parte multimodal desde el campo `response` estructurado, debe contener un `displayName` único.

También puedes hacer referencia a una parte multimodal desde el campo `response` estructurado de la parte `functionResponse` con el formato de referencia JSON `{"$ref": "<displayName>"}`. El modelo sustituye la referencia por el contenido multimodal cuando procesa la respuesta. Cada `displayName` solo se puede hacer referencia una vez en el campo `response` estructurado.

En el siguiente ejemplo, se muestra un mensaje que contiene un `functionResponse` para una función llamada `get_image` y una parte anidada que contiene datos de imágenes con `displayName: "instrument.jpg"`. El campo `response` del `functionResponse` hace referencia a esta parte de la imagen:

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

## Llamada a función con resultados estructurados

En el caso de los modelos de la serie Gemini 3, puedes usar la llamada a función con [salida estructurada](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419). Esto permite que el modelo prediga llamadas a funciones o resultados que se ajusten a un esquema específico. Como resultado, recibirás respuestas con formato coherente cuando el modelo no genere llamadas a funciones.

## Protocolo de contexto del modelo (MCP)

El [Protocolo de contexto del modelo (MCP)](https://modelcontextprotocol.io/introduction) es un estándar abierto para conectar aplicaciones de IA con herramientas y datos externos.
El MCP proporciona un protocolo común para que los modelos accedan al contexto, como funciones (herramientas), fuentes de datos (recursos) o instrucciones predefinidas.

Los SDKs de Gemini tienen compatibilidad integrada con el MCP, lo que reduce el código estándar y ofrece [llamadas automáticas a herramientas](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419#automatic_function_calling_python_only) para las herramientas del MCP. Cuando el modelo genera una llamada a la herramienta de MCP, el SDK del cliente de Python y JavaScript puede ejecutar automáticamente la herramienta de MCP y enviar la respuesta al modelo en una solicitud posterior, y continuar este bucle hasta que el modelo no realice más llamadas a herramientas.

Aquí puedes encontrar un ejemplo de cómo usar un servidor de MCP local con Gemini y el SDK de `mcp`.

### Python

Asegúrate de que la versión más reciente del [SDK de `mcp`](https://modelcontextprotocol.io/introduction) esté instalada en la plataforma que elijas.

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

Asegúrate de que la versión más reciente del SDK de `mcp` esté instalada en la plataforma que elijas.

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

### Limitaciones con la compatibilidad integrada con MCP

La compatibilidad integrada con MCP es una función [experimental](https://ai.google.dev/gemini-api/docs/models?hl=es-419#preview) de nuestros SDKs y tiene las siguientes limitaciones:

- Solo se admiten herramientas, no recursos ni instrucciones
- Está disponible para los SDKs de Python y JavaScript/TypeScript.
- Es posible que se produzcan cambios rotundos en versiones futuras.

La integración manual de los servidores de MCP siempre es una opción si estos limitan lo que estás compilando.

## Modelos compatibles

En esta sección, se enumeran los modelos y sus capacidades de llamadas a funciones. No se incluyen los modelos experimentales. Puedes encontrar una descripción general completa de las capacidades en la página [Descripción general del modelo](https://ai.google.dev/gemini-api/docs/models?hl=es-419).

| Modelo | Llamada a función | Llamada a función paralela | Llamada a función compositiva |
| --- | --- | --- | --- |
| [Versión preliminar de Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Versión preliminar de Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Versión preliminar de Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=es-419) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=es-419) | ✔️ | ✔️ | ✔️ |

## Prácticas recomendadas

- **Descripciones de funciones y parámetros:** Sé muy claro y específico en tus descripciones. El modelo se basa en estos datos para elegir la función correcta y proporcionar argumentos adecuados.
- **Nombres:** Usa nombres de funciones descriptivos (sin espacios, puntos ni guiones).
- **Tipificación fuerte:** Usa tipos específicos (número entero, cadena, enumeración) para los parámetros y, así, reducir los errores. Si un parámetro tiene un conjunto limitado de valores válidos, usa una enumeración.
- **Selección de herramientas:** Si bien el modelo puede usar una cantidad arbitraria de herramientas, proporcionar demasiadas puede aumentar el riesgo de seleccionar una herramienta incorrecta o subóptima. Para obtener los mejores resultados, intenta proporcionar solo las herramientas pertinentes para el contexto o la tarea. Lo ideal es mantener el conjunto activo en un máximo de 10 a 20. Considera la selección dinámica de herramientas según el contexto de la conversación si tienes una gran cantidad total de herramientas.
- **Ingeniería de instrucciones:**
  - Proporciona contexto: Dile al modelo cuál es su rol (p. ej., "Eres un asistente del clima útil").
  - Da instrucciones: Especifica cómo y cuándo usar funciones (p. ej., "No adivines fechas; siempre usa una fecha futura para las previsiones").
  - Fomenta la aclaración: Indica al modelo que haga preguntas aclaratorias si es necesario.
  - Consulta [Flujos de trabajo basados en agentes](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419#agentic-workflows) para obtener más estrategias sobre el diseño de estas instrucciones. Este es un ejemplo de una [instrucción del sistema](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=es-419#agentic-si-template) probada.
- **Temperatura:** Usa una temperatura baja (p.ej., 0) para obtener llamadas a funciones más determinísticas y confiables.
- **Validación:** Si una llamada a función tiene consecuencias significativas (p.ej., realizar un pedido), valida la llamada con el usuario antes de ejecutarla.
- **Verifica el motivo de finalización:** Siempre verifica [`finishReason`](https://ai.google.dev/api/generate-content?hl=es-419#FinishReason) en la respuesta del modelo para controlar los casos en los que el modelo no pudo generar una llamada a función válida.
- **Manejo de errores**: Implementa un manejo de errores sólido en tus funciones para controlar con elegancia entradas inesperadas o fallas de la API. Devuelve mensajes de error informativos que el modelo puede usar para generar respuestas útiles para el usuario.
- **Seguridad:** Ten en cuenta la seguridad cuando llames a APIs externas. Usa mecanismos de autenticación y autorización adecuados. Evita exponer datos sensibles en las llamadas a funciones.
- **Límites de tokens:** Las descripciones y los parámetros de las funciones se incluyen en el límite de tokens de entrada. Si alcanzas los límites de tokens, considera limitar la cantidad de funciones o la longitud de las descripciones, y divide las tareas complejas en conjuntos de funciones más pequeños y enfocados.
- **Combinación de bash y herramientas personalizadas**: Para quienes compilan con una combinación de bash y herramientas personalizadas, la versión preliminar de Gemini 3.1 Pro incluye un extremo independiente disponible a través de la API llamado [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=es-419#gemini-31-pro-preview-customtools).

## Notas y limitaciones

- Posicionamiento de las partes de la llamada a función: Cuando se usan declaraciones de funciones personalizadas [junto con herramientas integradas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419) (como la Búsqueda de Google), el modelo puede devolver una combinación de partes `functionCall`, `toolCall` y `toolResponse` en un solo turno. Por este motivo, no supongas que `functionCall` siempre será el último elemento del array de partes. Si analizas manualmente la respuesta JSON, siempre itera el array de partes en lugar de depender de la posición.
- Solo se admite un [subconjunto del esquema de OpenAPI](https://ai.google.dev/api/caching?hl=es-419#FunctionDeclaration).
- En el modo `ANY`, la API puede rechazar esquemas muy grandes o anidados de forma profunda. Si encuentras errores, intenta simplificar los esquemas de parámetros y respuestas de tu función acortando los nombres de las propiedades, reduciendo el anidamiento o limitando la cantidad de declaraciones de funciones.
- Los tipos de parámetros admitidos en Python son limitados.
- La llamada automática a funciones es una función exclusiva del SDK de Python.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
