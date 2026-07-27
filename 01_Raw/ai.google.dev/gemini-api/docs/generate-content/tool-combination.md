---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=it
fetched_at: 2026-07-27T04:48:33.749425+00:00
title: "Combinare strumenti integrati e chiamata di funzione \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Combinare strumenti integrati e chiamata di funzione

Gemini consente la combinazione di [strumenti integrati](https://ai.google.dev/gemini-api/docs/tools?hl=it), come `google_search`, e [chiamate di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) (note anche come *strumenti personalizzati*) in una singola generazione, preservando ed esponendo la cronologia del contesto delle chiamate di strumenti. Le combinazioni di strumenti integrati e personalizzati consentono
workflow complessi e basati su agenti in cui, ad esempio, il modello può basarsi
su dati web in tempo reale prima di richiamare la logica di business specifica.

Ecco un esempio che consente combinazioni di strumenti integrati e personalizzati con
`google_search` e una funzione personalizzata `getWeather`:

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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
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
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

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
    const model = client.getGenerativeModel({
        model: "gemini-3.5-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.5-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## Come funziona

I modelli Gemini 3 utilizzano la *circolazione del contesto degli strumenti* per consentire combinazioni di strumenti integrati e personalizzati. La circolazione del contesto degli strumenti consente di preservare ed esporre il contesto degli strumenti integrati e condividerlo con gli strumenti personalizzati nella stessa chiamata da turno a turno.

### Abilitare la combinazione di strumenti

- Devi impostare il flag `include_server_side_tool_invocations` su `true` per
  attivare la circolazione del contesto dello strumento.
- Includi [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=it#function-declarations), insieme agli strumenti integrati che vuoi utilizzare, per attivare il comportamento della combinazione.
  - Se non includi `function_declarations`, la circolazione del contesto degli strumenti
    agirà comunque sugli strumenti integrati inclusi, a condizione che il flag sia impostato.

### L'API restituisce le parti

In una singola risposta, l'API restituisce le parti `toolCall` e `toolResponse`
per la chiamata di funzione integrata. Per la chiamata di funzione (strumento personalizzato), l'API
restituisce la parte di chiamata `functionCall`, a cui l'utente fornisce la parte
`functionResponse` nel turno successivo.

- `toolCall` e `toolResponse`: l'API restituisce queste parti per preservare il contesto degli strumenti eseguiti sul lato server e il risultato della loro esecuzione per il turno successivo.
- `functionCall` e `functionResponse`: l'API invia la chiamata di funzione
  all'utente da compilare e l'utente restituisce il risultato nella
  risposta della funzione (queste parti sono standard per tutte le [chiamate di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) nell'API Gemini, non uniche per la
  funzionalità di combinazione di strumenti).
- (Solo strumento [Esecuzione del codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it))
  `executableCode` e `codeExecutionResult`:
  Quando utilizzi lo strumento Esecuzione del codice, anziché `functionCall` e
  `functionResponse`, l'API restituisce `executableCode` (il codice generato
  dal modello che deve essere eseguito) e `codeExecutionResult` (il
  risultato del codice eseguibile).

Devi restituire tutte le parti, inclusi tutti i [campi](#critical-fields) che contengono, al modello a ogni turno per mantenere il contesto e consentire le combinazioni di strumenti.

### Campi critici nelle parti restituite

Alcune [parti restituite dall'API](#api-returns-parts) includeranno i campi `id`,
`tool_type` e `thought_signature`. Questi campi sono fondamentali per
mantenere il contesto dello strumento (e quindi per le combinazioni di strumenti); devi
restituire tutte le parti *come indicato nella risposta* nelle richieste successive.

- `id`: un identificatore univoco che mappa una chiamata alla relativa risposta. `id` è **impostato su
  tutte le risposte di chiamata di funzione**, indipendentemente dalla circolazione del contesto dello strumento.
  Devi *fornire* lo stesso `id` nella risposta della funzione
  che l'API fornisce nella chiamata di funzione. Gli strumenti integrati condividono automaticamente
  il `id` tra la chiamata allo strumento e la risposta dello strumento.
  - Presente in tutte le parti relative allo strumento: `toolCall`, `toolResponse`,
    `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: identifica lo strumento specifico utilizzato; il nome dello strumento o della funzione letterale integrata (ad es. `URL_CONTEXT` o `getWeather`).
  - Trovato nelle parti `toolCall` e `toolResponse`.
- `thought_signature`: il contesto criptato effettivo incorporato in **ogni
  parte restituita dall'API**. Il contesto non può essere
  ricostruito senza le firme del pensiero; se non restituisci le firme del pensiero
  per tutte le parti in ogni turno, il modello genererà un errore.
  - Trovato in *tutte* le parti.

### Dati specifici dello strumento

Alcuni strumenti integrati restituiscono argomenti di dati visibili agli utenti specifici per il tipo di strumento.

| Strumento | Argomenti della chiamata allo strumento visibili all'utente (se presenti) | Risposta dello strumento visibile all'utente (se presente) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL da visitare | `urls_metadata` `retrieved_url`: URL sfogliati `url_retrieval_status`: Stato della navigazione |
| **FILE\_SEARCH** | Nessuno | Nessuno |

## Esempio di struttura della richiesta di combinazione di strumenti

La seguente struttura della richiesta mostra la struttura della richiesta del prompt: "Qual è la città più a nord degli Stati Uniti? Che tempo fa lì oggi?". Combina tre strumenti: gli strumenti Gemini integrati `google_search`
e `code_execution` e una funzione personalizzata `get_weather`.

```
{
  "model": "models/gemini-3.5-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Token e prezzi

Tieni presente che le parti `toolCall` e `toolResponse` nelle richieste vengono conteggiate ai fini di
`prompt_token_count`. Poiché questi passaggi dello strumento intermedio sono ora visibili e
restituiti, fanno parte della cronologia della conversazione. Questo vale solo per le *richieste*, non per le *risposte*.

Lo strumento Ricerca Google è un'eccezione a questa regola. La Ricerca Google applica già il proprio modello di prezzi a livello di query, pertanto i token non vengono addebitati due volte (consulta la pagina [Prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it)).

Per saperne di più, consulta la pagina [Token](https://ai.google.dev/gemini-api/docs/tokens?hl=it).

## Limitazioni

- Impostazione predefinita della modalità `VALIDATED` (la modalità `AUTO` non è supportata) quando
  il flag `include_server_side_tool_invocations` è attivato
- Gli strumenti integrati come `google_search` si basano su informazioni relative alla posizione e all'ora corrente, quindi se `system_instruction` o `function_declaration.description` hanno informazioni su posizione e ora in conflitto, la funzionalità di combinazione degli strumenti potrebbe non funzionare correttamente.

## Strumenti supportati

La circolazione del contesto degli strumenti standard si applica agli strumenti lato server (integrati).
Code Execution è anche uno strumento lato server, ma ha una propria soluzione integrata per la
circolazione del contesto. L'utilizzo del computer e la chiamata di funzioni sono strumenti lato client
e dispongono anche di soluzioni integrate per la circolazione del contesto.

| Strumento | Lato esecuzione | Supporto per la circolazione del contesto |
| --- | --- | --- |
| [la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) | Lato server | Supportato |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) | Lato server | Supportato |
| [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) | Lato server | Supportato |
| [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) | Lato server | Supportato |
| [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) | Lato server | Supportato (integrato, utilizza le parti `executableCode` e `codeExecutionResult`) |
| [Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) | Lato client | Supportato (integrato, utilizza le parti `functionCall` e `functionResponse`) |
| [Funzioni personalizzate](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) | Lato client | Supportato (integrato, utilizza le parti `functionCall` e `functionResponse`) |

## Passaggi successivi

- Scopri di più sulla [chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) nell'API Gemini.
- Esplora gli strumenti supportati:
  - [la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)
  - [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)
  - [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-23 UTC."],[],[]]
