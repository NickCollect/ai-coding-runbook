---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=it
fetched_at: 2026-05-05T20:46:09.593356+00:00
title: "Chiamate di funzione con l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Chiamate di funzione con l'API Gemini

La chiamata di funzioni consente di collegare i modelli a strumenti e API esterni.
Anziché generare risposte di testo, il modello determina quando chiamare funzioni specifiche e fornisce i parametri necessari per eseguire azioni nel mondo reale.
In questo modo, il modello può fungere da ponte tra il linguaggio naturale e le azioni e i dati del mondo reale. La chiamata di funzione ha tre casi d'uso principali:

- **Aumenta le conoscenze**:accedi alle informazioni da fonti esterne come
  database, API e knowledge base.
- **Estendi le funzionalità:** utilizza strumenti esterni per eseguire calcoli ed
  estendere i limiti del modello, ad esempio utilizzando una calcolatrice o creando
  grafici.
- **Esegui azioni**:interagisci con sistemi esterni utilizzando le API, ad esempio
  pianificare appuntamenti, creare fatture, inviare email o controllare
  dispositivi per la smart home.

Get Weather (Meteo)
Schedule Meeting (Fissa un incontro)
Create Chart (Crea grafico)

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

## Come funziona la chiamata di funzioni

![Panoramica della chiamata di funzione](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=it)

La chiamata di funzioni prevede un'interazione strutturata tra l'applicazione, il modello e le funzioni esterne. Ecco una panoramica della procedura:

1. **Definisci la dichiarazione di funzione**:definisci la dichiarazione di funzione nel codice dell'applicazione. Le dichiarazioni di funzione descrivono al modello il nome, i parametri e lo scopo della funzione.
2. **Chiama l'API con le dichiarazioni di funzione:** invia il prompt dell'utente insieme alle dichiarazioni di funzione al modello. Analizza la richiesta e determina
   se una chiamata di funzione potrebbe essere utile. In caso affermativo, risponde con un oggetto JSON strutturato contenente il nome della funzione, gli argomenti e un `id` univoco
   (questo `id` viene ora sempre restituito dall'API per i modelli Gemini 3\*).
3. **Esegui il codice della funzione (tua responsabilità)**: il modello *non*
   esegue la funzione stessa. È responsabilità della tua applicazione
   elaborare la risposta e verificare la presenza di una chiamata di funzione. Se
   - **Sì**: estrai il nome, gli argomenti e `id` della funzione ed esegui
     la funzione corrispondente nella tua applicazione.
   - **No**:il modello ha fornito una risposta di testo diretta al prompt
     (questo flusso è meno enfatizzato nell'esempio, ma è un risultato possibile).
4. **Crea una risposta intuitiva:** se è stata eseguita una funzione, acquisisci il risultato e invialo di nuovo al modello, assicurandoti di includere il `id` corrispondente in un turno successivo della conversazione. Utilizzerà il risultato per
   generare una risposta finale e intuitiva che incorpori le informazioni
   dalla chiamata di funzione.

Questo processo può essere ripetuto più volte, consentendo interazioni e flussi di lavoro complessi. Il modello supporta anche la chiamata di più funzioni
in un singolo turno ([chiamata di funzioni parallela](#parallel_function_calling)), in
sequenza ([chiamata di funzioni compositiva](#compositional_function_calling))
e con gli strumenti Gemini integrati ([utilizzo di più strumenti](#native-tools)).

\* **Mappa sempre gli ID funzione:** Gemini 3 ora restituisce sempre un `id` univoco con ogni `functionCall`. Includi questo `id` esatto nel tuo
`functionResponse` in modo che il modello possa mappare con precisione il risultato alla
richiesta originale.

### Passaggio 1: definisci una dichiarazione di funzione

Definisci una funzione e la relativa dichiarazione all'interno del codice dell'applicazione che consente agli utenti di impostare i valori di luminosità ed effettuare una richiesta API. Questa funzione potrebbe chiamare
servizi o API esterni.

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

### Passaggio 2: chiama il modello con le dichiarazioni di funzione

Una volta definite le dichiarazioni di funzione, puoi chiedere al modello di utilizzarle. Analizza il prompt e le dichiarazioni di funzione e decide se rispondere direttamente o chiamare una funzione. Se viene chiamata una funzione, l'oggetto
della risposta conterrà un suggerimento di chiamata di funzione.

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

Il modello restituisce quindi un oggetto `functionCall` in uno schema compatibile con OpenAPI che specifica come chiamare una o più delle funzioni dichiarate per rispondere alla domanda dell'utente.

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

### Passaggio 3: esegui il codice della funzione set\_light\_values

Estrai i dettagli della chiamata di funzione dalla risposta del modello, analizza gli argomenti
ed esegui la funzione `set_light_values`.

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

### Passaggio 4: crea una risposta intuitiva con il risultato della funzione e chiama di nuovo il modello

Infine, invia il risultato dell'esecuzione della funzione al modello in modo che possa
incorporare queste informazioni nella risposta finale all'utente.

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

In questo modo, il flusso di chiamata della funzione è completato. Il modello ha utilizzato correttamente la funzione `set_light_values` per eseguire l'azione di richiesta dell'utente.

## Dichiarazioni di funzione

Quando implementi la chiamata di funzione in un prompt, crei un oggetto `tools`,
che contiene uno o più `function declarations`. Definisci le funzioni utilizzando
JSON, in particolare con un [sottoinsieme di selezione](https://ai.google.dev/api/caching?hl=it#Schema)
del formato dello [schema OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Una
singola dichiarazione di funzione può includere i seguenti parametri:

- `name` (stringa): un nome univoco per la funzione (`get_weather_forecast`,
  `send_email`). Utilizza nomi descrittivi senza spazi o caratteri speciali
  (utilizza trattini bassi o camelCase).
- `description` (stringa): una spiegazione chiara e dettagliata dello scopo e delle funzionalità della funzione. Questo è fondamentale per consentire al modello di capire quando
  utilizzare la funzione. Sii specifico e fornisci esempi se utili ("Trova
  i cinema in base alla posizione e, facoltativamente, al titolo del film attualmente
  in programmazione nei cinema").
- `parameters` (oggetto): definisce i parametri di input previsti dalla funzione.
  - `type` (stringa): specifica il tipo di dati complessivo, ad esempio `object`.
  - `properties` (oggetto): elenca i singoli parametri, ognuno con:
    - `type` (stringa): il tipo di dati del parametro, ad esempio `string`,
      `integer`, `boolean, array`.
    - `description` (stringa): una descrizione dello scopo e del formato del parametro. Fornisci esempi e vincoli ("La città e lo stato,
      ad es. "San Francisco, CA" o un codice postale, ad es. "95616").
    - `enum` (array, facoltativo): se i valori dei parametri provengono da un insieme fisso, utilizza "enum" per elencare i valori consentiti anziché descriverli semplicemente nella descrizione. In questo modo, la precisione migliora ("enum":
      ["daylight", "cool", "warm"]).
  - `required` (array): un array di stringhe che elenca i nomi dei parametri
    obbligatori per il funzionamento della funzione.

Puoi anche creare `FunctionDeclarations` direttamente dalle funzioni Python utilizzando
`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Chiamata di funzione con modelli di ragionamento

I modelli delle serie Gemini 3 e 2.5 utilizzano un processo di ["ragionamento"](https://ai.google.dev/gemini-api/docs/thinking?hl=it) interno per elaborare le richieste. Ciò
migliora significativamente le prestazioni delle chiamate di funzione,
consentendo al modello di determinare meglio quando chiamare una funzione e quali
parametri utilizzare. Poiché l'API Gemini è stateless, i modelli utilizzano le
[firme di pensiero](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it) per mantenere il contesto
nelle conversazioni multi-turno.

Questa sezione tratta la gestione avanzata delle firme dei pensieri ed è necessaria solo se stai creando manualmente richieste API (ad es. tramite REST) o manipolando la cronologia delle conversazioni.

**Se utilizzi gli [SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=it) (le nostre
librerie ufficiali), non devi gestire questo processo**. Gli SDK
gestiscono automaticamente i passaggi necessari, come mostrato nell'[esempio](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-4) precedente.

### Gestire manualmente la cronologia delle conversazioni

Se modifichi manualmente la cronologia della conversazione, anziché inviare la
[risposta precedente completa](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#step-4), devi
gestire correttamente `thought_signature` incluso nel turno del modello.

Segui queste regole per assicurarti che il contesto del modello venga preservato:

- Restituisci sempre il `thought_signature` al modello all'interno del suo
  [`Part`](https://ai.google.dev/api?hl=it#request-body-structure) originale.
- **Includi sempre l'`id` esatto di `function_call` nel tuo
  `function_response` in modo che l'API possa mappare il risultato alla richiesta corretta.**
- Non unire un `Part` contenente una firma con uno che non la contiene. Questo
  interrompe il contesto posizionale del pensiero.
- Non combinare due `Parts` che contengono entrambe firme, perché le stringhe
  della firma non possono essere unite.

#### Firme di pensiero di Gemini 3

In Gemini 3, qualsiasi [`Part`](https://ai.google.dev/api?hl=it#request-body-structure) di una risposta del modello
può contenere una firma del pensiero.
Sebbene in genere consigliamo di restituire le firme di tutti i tipi di `Part`,
la restituzione delle firme del pensiero è obbligatoria per la chiamata di funzioni. A meno che tu non
manipoli manualmente la cronologia delle conversazioni, l'SDK Google GenAI
gestirà automaticamente le firme dei pensieri.

Se manipoli manualmente la cronologia delle conversazioni, consulta la pagina
[Firme dei pensieri](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=it) per indicazioni
e dettagli completi sulla gestione delle firme dei pensieri per Gemini 3.

##### Ispezione delle firme del pensiero

Sebbene non sia necessario per l'implementazione, puoi esaminare la risposta per visualizzare
`thought_signature` a scopo di debug o didattico.

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

Scopri di più sulle limitazioni e sull'utilizzo delle firme di pensiero e sui modelli di ragionamento in generale nella pagina [Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it#signatures).

## Chiamata di funzione parallela

Oltre alla chiamata di funzioni a singolo turno, puoi anche chiamare più funzioni contemporaneamente. La chiamata di funzione parallela consente di eseguire più funzioni
contemporaneamente e viene utilizzata quando le funzioni non dipendono l'una dall'altra. Questa funzionalità è
utile in scenari come la raccolta di dati da più origini indipendenti, ad esempio
il recupero dei dettagli dei clienti da database diversi o il controllo dei livelli
di inventario in vari magazzini o l'esecuzione di più azioni, ad esempio
la trasformazione del tuo appartamento in una discoteca.

Quando il modello avvia più chiamate di funzioni in un singolo turno, non
devi restituire gli oggetti `function_result` nello stesso ordine in cui sono stati ricevuti gli oggetti `function_call`. L'API Gemini mappa ogni risultato alla chiamata corrispondente utilizzando `id` dall'output del modello. In questo modo puoi
eseguire le funzioni in modo asincrono e aggiungere i risultati all'elenco
man mano che vengono completati.

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

Configura la modalità di chiamata di funzione per consentire l'utilizzo di tutti gli strumenti specificati.
Per saperne di più, puoi leggere informazioni sulla
[configurazione della chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#function_calling_modes).

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

Ciascuno dei risultati stampati riflette una singola chiamata di funzione richiesta dal modello. Per inviare i risultati, includi le risposte nello stesso ordine in cui sono state richieste.

L'SDK Python supporta la [chiamata automatica di funzioni](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#automatic_function_calling_python_only), che converte automaticamente le funzioni Python in dichiarazioni, gestisce l'esecuzione della chiamata di funzione e il ciclo di risposta per te. Di seguito è riportato un esempio per
il caso d'uso della discoteca.

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

## Chiamata di funzione compositiva

La chiamata di funzioni compositiva o sequenziale consente a Gemini di concatenare più chiamate di funzioni per soddisfare una richiesta complessa. Ad esempio, per rispondere a
"Qual è la temperatura nella mia posizione attuale?", l'API Gemini potrebbe prima richiamare
una funzione `get_current_location()` seguita da una funzione `get_weather()` che
accetta la posizione come parametro.

L'esempio seguente mostra come implementare la chiamata di funzioni compositive utilizzando l'SDK Python e la chiamata automatica di funzioni.

### Python

Questo esempio utilizza la funzionalità di chiamata di funzione automatica dell'SDK Python `google-genai`. L'SDK converte automaticamente le funzioni Python nello schema richiesto, esegue le chiamate di funzione quando richieste dal modello e invia i risultati al modello per completare l'attività.

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

**Output previsto**

Quando esegui il codice, vedrai l'SDK orchestrare le chiamate di funzione. Il modello chiama prima `get_weather_forecast`, riceve la
temperatura e poi chiama `set_thermostat_temperature` con il valore
corretto in base alla logica nel prompt.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

Questo esempio mostra come utilizzare l'SDK JavaScript/TypeScript per eseguire chiamate di funzioni compositive utilizzando un ciclo di esecuzione manuale.

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

**Output previsto**

Quando esegui il codice, vedrai l'SDK orchestrare le chiamate di funzione. Il modello chiama prima `get_weather_forecast`, riceve la
temperatura e poi chiama `set_thermostat_temperature` con il valore
corretto in base alla logica nel prompt.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

La chiamata di funzione compositiva è una funzionalità nativa dell'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it). Ciò significa che l'API Live
può gestire la chiamata di funzione in modo simile all'SDK Python.

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

## Modalità di chiamata di funzione

L'API Gemini ti consente di controllare il modo in cui il modello utilizza gli strumenti forniti
(dichiarazioni di funzioni). Nello specifico, puoi impostare la modalità all'interno
di.`function_calling_config`.

- `VALIDATED`: modalità predefinita per la combinazione di strumenti (quando sono attivi anche gli strumenti integrati o
  gli output strutturati). Il modello è vincolato a prevedere chiamate di funzioni o linguaggio naturale e garantisce il rispetto dello schema delle funzioni. Se non viene fornito `allowed_function_names`, il modello sceglie tra tutte le dichiarazioni di funzioni disponibili. Se viene fornito `allowed_function_names`, il modello sceglie dall'insieme di funzioni consentite. Questa modalità riduce le chiamate di funzioni non valide (rispetto alla modalità `AUTO`).
- `AUTO`: modalità predefinita quando è attivato solo lo strumento function\_declarations.
  Il modello decide se generare una risposta in linguaggio naturale o suggerire
  una chiamata di funzione in base al prompt e al contesto.
- `ANY`: il modello è vincolato a prevedere sempre una chiamata di funzione e
  garantisce il rispetto dello schema della funzione. Se `allowed_function_names` non è
  specificato, il modello può scegliere tra una qualsiasi delle dichiarazioni di funzione fornite.
  Se `allowed_function_names` viene fornito come elenco, il modello può scegliere solo tra le funzioni presenti nell'elenco. Utilizza questa modalità quando richiedi una risposta
  alla chiamata di funzione per ogni prompt (se applicabile).
- `NONE`: al modello è *vietato* effettuare chiamate di funzione. Equivale a inviare una richiesta senza dichiarazioni di funzioni. Utilizza questa opzione per
  disattivare temporaneamente le chiamate di funzione senza rimuovere le definizioni degli strumenti.

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

## Chiamata di funzione automatica (solo Python)

Quando utilizzi l'SDK Python, puoi fornire direttamente le funzioni Python come strumenti.
L'SDK converte queste funzioni in dichiarazioni, gestisce l'esecuzione della chiamata di funzione e gestisce il ciclo di risposta. Definisci la funzione con
suggerimenti sul tipo e una docstring. Per risultati ottimali, è consigliabile utilizzare
[stringhe di documentazione in stile Google.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
L'SDK eseguirà automaticamente le seguenti operazioni:

1. Rileva le risposte alla chiamata di funzione del modello.
2. Chiama la funzione Python corrispondente nel codice.
3. Invia la risposta della funzione al modello.
4. Restituisce la risposta di testo finale del modello.

Al momento l'SDK non analizza le descrizioni degli argomenti negli slot
della descrizione della proprietà della dichiarazione di funzione generata. Invece, invia
l'intera docstring come descrizione della funzione di primo livello.

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

Puoi disattivare la chiamata automatica di funzioni con:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Dichiarazione automatica dello schema della funzione

L'API è in grado di descrivere uno qualsiasi dei seguenti tipi. I tipi `Pydantic` sono
consentiti, a condizione che anche i campi definiti siano composti da tipi
consentiti. I tipi di dizionari (come `dict[str: int]`) non sono ben supportati qui, quindi non utilizzarli.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Per vedere l'aspetto dello schema dedotto, puoi convertirlo utilizzando
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

## Utilizzo di più strumenti: combina gli strumenti integrati con le chiamate di funzione

Puoi attivare più strumenti, combinando quelli integrati con la chiamata di funzioni nella stessa richiesta.

I modelli Gemini 3 possono combinare strumenti integrati con la chiamata di funzioni predefinita,
grazie alla funzionalità di circolazione del contesto dello strumento. Per saperne di più, leggi la pagina su
[Combinare strumenti integrati e chiamate di funzione](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it).

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

Per i modelli precedenti alla serie Gemini 3, utilizza l'[API Live](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=it).

## Risposte della funzione multimodale

Per i modelli della serie Gemini 3, puoi includere contenuti multimodali nelle parti di risposta della funzione che invii al modello. Il modello può elaborare
questo contenuto multimodale nel turno successivo per produrre una risposta più informata.
Per i contenuti multimodali nelle risposte delle funzioni sono supportati i seguenti tipi MIME:

- **Google Immagini**: `image/png`, `image/jpeg`, `image/webp`
- **Documenti**: `application/pdf`, `text/plain`

Per includere dati multimodali in una risposta della funzione, includili come una o più
parti nidificate all'interno della parte `functionResponse`. Ogni parte multimodale deve
contenere `inlineData`. Se fai riferimento a una parte multimodale
all'interno del campo `response` strutturato, deve contenere un `displayName` univoco.

Puoi anche fare riferimento a una parte multimodale dal campo `response` strutturato della parte `functionResponse` utilizzando il formato di riferimento JSON `{"$ref": "<displayName>"}`. Il modello sostituisce il riferimento con i contenuti multimodali durante l'elaborazione della risposta. Ogni `displayName` può essere
citato una sola volta nel campo `response` strutturato.

L'esempio seguente mostra un messaggio contenente un `functionResponse` per una funzione denominata `get_image` e una parte nidificata contenente dati immagine con `displayName: "instrument.jpg"`. Il campo `functionResponse` `response`
fa riferimento a questa parte dell'immagine:

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

## Chiamata di funzione con output strutturato

Per i modelli della serie Gemini 3, puoi utilizzare le chiamate di funzione con
[output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it). In questo modo, il modello
può prevedere chiamate di funzioni o output che rispettano uno schema specifico. Di conseguenza,
ricevi risposte formattate in modo coerente quando il modello non genera
chiamate di funzioni.

## Model Context Protocol (MCP)

Il [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) è
uno standard aperto per connettere applicazioni AI a strumenti e dati esterni.
MCP fornisce un protocollo comune per l'accesso al contesto dei modelli, ad esempio funzioni
(strumenti), origini dati (risorse) o prompt predefiniti.

Gli SDK Gemini hanno un supporto integrato per MCP, riducendo il codice boilerplate e
offrendo
[chiamata automatica degli strumenti](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#automatic_function_calling_python_only)
per gli strumenti MCP. Quando il modello genera una chiamata allo strumento MCP, gli SDK client Python e JavaScript possono eseguire automaticamente lo strumento MCP e inviare la risposta al modello in una richiesta successiva, continuando questo ciclo finché il modello non effettua altre chiamate allo strumento.

Qui puoi trovare un esempio di come utilizzare un server MCP locale con Gemini e
`mcp` SDK.

### Python

Assicurati che sia installata l'ultima versione dell'[SDK `mcp`](https://modelcontextprotocol.io/introduction) sulla piattaforma che preferisci.

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

Assicurati che sulla piattaforma
che preferisci sia installata l'ultima versione dell'SDK `mcp`.

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

### Limitazioni con il supporto MCP integrato

Il supporto MCP integrato è una funzionalità [sperimentale](https://ai.google.dev/gemini-api/docs/models?hl=it#preview) dei nostri SDK e presenta le seguenti limitazioni:

- Sono supportati solo gli strumenti, non le risorse né i prompt
- È disponibile per gli SDK Python e JavaScript/TypeScript.
- Nelle release future potrebbero verificarsi modifiche che provocano un errore.

L'integrazione manuale dei server MCP è sempre un'opzione se questi limitano ciò che stai
creando.

## Modelli supportati

Questa sezione elenca i modelli e le relative funzionalità di chiamata di funzione. I modelli sperimentali non sono inclusi. Puoi trovare una panoramica completa delle funzionalità nella pagina [Panoramica modelli](https://ai.google.dev/gemini-api/docs/models?hl=it).

| Modello | Chiamata di funzione | Chiamata di funzione parallela | Chiamata di funzione compositiva |
| --- | --- | --- | --- |
| [Anteprima di Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 3 Flash (anteprima)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=it) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=it) | ✔️ | ✔️ | ✔️ |

## Best practice

- **Descrizioni di funzioni e parametri:** sii estremamente chiaro e specifico nelle
  tue descrizioni. Il modello si basa su questi per scegliere la funzione corretta
  e fornire argomenti appropriati.
- **Denominazione**:utilizza nomi di funzioni descrittivi (senza spazi, punti o
  trattini).
- **Tipizzazione forte**:utilizza tipi specifici (integer, stringa, enum) per i parametri
  per ridurre gli errori. Se un parametro ha un insieme limitato di valori validi, utilizza un'enumerazione.
- **Selezione degli strumenti**:anche se il modello può utilizzare un numero arbitrario di strumenti, fornirne troppi può aumentare il rischio di selezionare uno strumento errato o non ottimale. Per ottenere risultati ottimali, cerca di fornire solo gli strumenti pertinenti
  per il contesto o l'attività, idealmente mantenendo il set attivo a un massimo di
  10-20. Se hai un numero totale elevato di strumenti, valuta la possibilità di selezionare gli strumenti in modo dinamico in base al contesto della conversazione.
- **Prompt engineering:**
  - Fornisci il contesto: indica al modello il suo ruolo (ad es. "Sei un assistente
    meteo utile").
  - Fornisci istruzioni: specifica come e quando utilizzare le funzioni (ad es. "Non
    indovinare le date; utilizza sempre una data futura per le previsioni").
  - Incoraggia i chiarimenti: chiedi al modello di porre domande di chiarimento
    se necessario.
  - Per ulteriori strategie sulla progettazione di questi prompt, consulta [Flussi di lavoro agentici](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it#agentic-workflows). Ecco un esempio di [istruzione di sistema](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it#agentic-si-template) testata.
- **Temperatura**:utilizza una temperatura bassa (ad es. 0) per chiamate di funzioni più deterministiche e affidabili.
- **Convalida**:se una chiamata di funzione ha conseguenze significative (ad es.
  effettuare un ordine), convalidala con l'utente prima di eseguirla.
- **Controlla il motivo del termine:** controlla sempre [`finishReason`](https://ai.google.dev/api/generate-content?hl=it#FinishReason)
  nella risposta del modello per gestire i casi in cui il modello non è riuscito a generare una
  chiamata di funzione valida.
- **Gestione degli errori**: implementa una gestione degli errori efficace nelle tue funzioni per
  gestire correttamente input imprevisti o errori API. Restituisci messaggi di errore informativi
  che il modello può utilizzare per generare risposte utili per l'utente.
- **Sicurezza**:presta attenzione alla sicurezza quando chiami API esterne. Utilizza
  meccanismi di autenticazione e autorizzazione appropriati. Evita di esporre
  dati sensibili nelle chiamate di funzioni.
- **Limiti dei token**:le descrizioni e i parametri delle funzioni vengono conteggiati ai fini del limite di token di input. Se raggiungi i limiti di token, valuta la possibilità di limitare il numero di funzioni o la lunghezza delle descrizioni, suddividi le attività complesse in set di funzioni più piccoli e mirati.
- **Combinazione di bash e strumenti personalizzati** Per chi crea con una combinazione di bash e strumenti personalizzati, l'anteprima di Gemini 3.1 Pro include un endpoint separato disponibile tramite l'API chiamato [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=it#gemini-31-pro-preview-customtools).

## Note e limitazioni

- Posizionamento delle parti della chiamata di funzione: quando utilizzi dichiarazioni di funzioni personalizzate
  [insieme a strumenti integrati](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it) (come la Ricerca Google), il modello potrebbe restituire un mix di parti `functionCall`, `toolCall` e
  `toolResponse` in un singolo turno. Per questo motivo, non dare per scontato che
  `functionCall` sia sempre l'ultimo elemento dell'array delle parti. Se analizzi manualmente la risposta JSON, scorri sempre l'array parts anziché fare affidamento sulla posizione.
- È supportato solo un [sottoinsieme dello schema OpenAPI](https://ai.google.dev/api/caching?hl=it#FunctionDeclaration).
- Per la modalità `ANY`, l'API potrebbe rifiutare schemi molto grandi o con un livello di nidificazione elevato. Se
  si verificano errori, prova a semplificare gli schemi dei parametri e delle risposte della funzione
  riducendo i nomi delle proprietà, diminuendo il livello di nidificazione o limitando il
  numero di dichiarazioni di funzioni.
- I tipi di parametri supportati in Python sono limitati.
- La chiamata di funzione automatica è una funzionalità solo dell'SDK Python.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
