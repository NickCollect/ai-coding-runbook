---
source_url: https://ai.google.dev/gemini-api/docs/streaming?hl=pl
fetched_at: 2026-08-17T02:21:30.681408+00:00
title: "Interakcje ze streamingiem \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interakcje ze streamingiem

Podczas tworzenia interakcji możesz ustawić `stream: true`, aby stopniowo przesyłać strumieniowo odpowiedź za pomocą [zdarzeń wysyłanych przez serwer](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Count from 1 to 25.",
    stream=True,
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Count from 1 to 25.",
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Count from 1 to 25.",
    "stream": true
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"1, 2, 3, 4, 5, 6, ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"7, 8, 9, 10, 11, 12, 13,","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":346,"total_input_tokens":11,"input_tokens_by_modality":[{"modality":"text","tokens":11}],"total_cached_tokens":0,"total_output_tokens":90,"total_tool_use_tokens":0,"total_thought_tokens":245},"created":"2026-05-12T18:44:51Z","updated":"2026-05-12T18:44:51Z","service_tier":"standard","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Typy zdarzeń

Każde zdarzenie wysłane przez serwer zawiera nazwane pole `event_type` i powiązane z nim dane JSON. Interfejs Interactions API korzysta z symetrycznego modelu przesyłania strumieniowego, w którym wszystkie treści – tekst, wywołania narzędzi i proces myślowy – przepływają przez spójne zdarzenie **krokowe**.

Każda transmisja ma następujący przepływ zdarzeń:

1. `interaction.created`: interakcja jest tworzona i zawiera metadane (identyfikator, model, stan).
2. Seria **kroków**, z których każdy składa się z:
   - `step.start` zdarzenie wskazujące typ kroku (np. `model_output`, `thought`, `function_call`).
   - Co najmniej 1 zdarzenie `step.delta` z danymi przyrostowymi dotyczącymi tego kroku.
   - `step.stop` zdarzenie oznaczające krok jako ukończony.
3. Wydarzenie `interaction.completed` z ostatecznymi statystykami `usage`.

Gdy ustawisz parametr `stream: false`, interfejs API zwróci pojedynczy obiekt `interaction` z tablicą `steps`. Każdy element w `steps` to w pełni zmontowana wersja jednego cyklu `step.start` → `step.delta` → `step.stop`.

### `interaction.created`

Wysyłane, gdy interakcja zostanie utworzona po raz pierwszy. Zawiera identyfikator interakcji, model i stan początkowy.

```
event: interaction.created
data: {"interaction": {"id": "...", "model": "gemini-3.5-flash", "status": "in_progress", "object": "interaction"}, "event_type": "interaction.created"}
```

### `interaction.status_update`

Sygnalizuje przejście stanu na poziomie interakcji. Może się pojawiać między krokami.

```
event: interaction.status_update
data: {"interaction_id": "...", "status": "in_progress", "event_type": "interaction.status_update"}
```

### `step.start`

Oznacza początek nowego kroku. Zawiera kroki `type` i `index`. Typ kroku określa, jakich typów delty należy oczekiwać i jak krok będzie wyglądać w odpowiedzi bez przesyłania strumieniowego:

| Typ kroku | Oczekiwane typy zmian | Opis |
| --- | --- | --- |
| `model_output` | `text`, `image`, `audio` | Treść ostatecznej odpowiedzi modelu. |
| `thought` | `thought_signature`, `thought_summary` | Rozumowanie w formie łańcucha myśli. Wartość `summary` występuje tylko wtedy, gdy włączona jest wartość `thinking_summaries`. |
| `function_call` | `arguments_delta` | Prośba o wykonanie funkcji przez klienta. Ustawia stan interakcji na `requires_action`. |
| Narzędzia po stronie serwera | Zależy od narzędzia | Narzędzia wykonywane przez interfejs API (np. `google_search_call`, `google_search_result`, `code_execution_call`, `code_execution_result`). |

Pełną listę znajdziesz w [dokumentacji interfejsu API interakcji](https://ai.google.dev/api/interactions-api?hl=pl).

```
event: step.start
data: {"index": 0, "step": {"type": "model_output"}, "event_type": "step.start"}
```

W przypadku wywołań funkcji krok zawiera nazwę funkcji, identyfikator i puste argumenty `{}`.

```
event: step.start
data: {"index": 0, "step": {"type": "function_call", "id":"un6k8t18", "name": "get_weather", "arguments":{}}, "event_type": "step.start"}
```

### `step.delta`

Dane przyrostowe bieżącego kroku. Obiekt `delta` zawiera pole `type`, które określa jego kształt.

**Przykłady:**

**`text`:** przyrostowy token tekstowy z kroku `model_output`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": "Hello, my name is Phil"}, "event_type": "step.delta"}

event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": ", and I live in Germany." }, "event_type": "step.delta"}
```

**`image`:** dane obrazu zakodowane w formacie Base64 z kroku `model_output`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg..."}, "event_type": "step.delta"}
```

**`thought_summary`:** podsumowanie przemyśleń z kroku `thought`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "thought_summary", "content": {"type": "text", "text": "I need to find the GCD..."}}, "event_type": "step.delta"}
```

**`arguments_delta`:** (częściowy) ciąg JSON argumentów wywołania funkcji. Musi być kumulowana w wartościach delta:

```
event: step.delta
data: {"index": 0, "delta": {"type": "arguments_delta", "arguments": "{\"location\": \"San Francisco, CA\"}"}, "event_type": "step.delta"}
```

Oto niektóre z najczęstszych typów zmian. Pełną listę wszystkich typów zmian znajdziesz w [dokumentacji interfejsu Interactions API](https://ai.google.dev/api/interactions-api?hl=pl).

### `step.stop`

Oznacza koniec kroku. Zawiera krok `index`.

```
event: step.stop
data: {"index": 0, "event_type": "step.stop"}
```

### `interaction.completed`

Wysyłane po zakończeniu interakcji. Zawiera obiekt ostatniej interakcji ze statystykami `usage`. W trybie bez strumieniowania jest to sam obiekt odpowiedzi najwyższego poziomu. Nie zawiera w odpowiedzi `steps`.

```
event: interaction.completed
data: {"interaction": {"id": "v1_abc123", "status": "completed", "usage": {"total_input_tokens": 7, "total_output_tokens": 12, "total_tokens": 19}}, "event_type": "interaction.completed"}
```

### `error`

Wysyłane, gdy podczas interakcji wystąpi błąd. Zawiera obiekt błędu z komunikatem i kodem.

```
event: error
data: {"error":{"message":"Deadline expired before operation could complete.","code":"gateway_timeout"},"event_type":"error"}
```

## Przesyłanie strumieniowe za pomocą narzędzi

Interfejs API Interactions obsługuje przesyłanie strumieniowe za pomocą narzędzi po stronie klienta (wywoływanie funkcji) i narzędzi po stronie serwera (wyszukiwarka Google, wykonywanie kodu itp.) w ramach jednego żądania. Podczas przesyłania strumieniowego wywołania narzędzi pojawiają się w strumieniu zdarzeń jako wpisane kroki. W przypadku wywołań funkcji zdarzenie `step.start` przekazuje nazwę funkcji, a zdarzenia `step.delta` przesyłają argumenty jako ciągi znaków JSON (`arguments_delta`). Aby uzyskać pełne argumenty, musisz zgromadzić te różnice.
Narzędzia po stronie serwera, takie jak wyszukiwarka Google, są wykonywane automatycznie przez interfejs API, co powoduje powstanie kroków `google_search_call` i `google_search_result`.

### Strumieniowanie z wywoływaniem funkcji

Aby wykonać wywoływanie funkcji za pomocą przesyłania strumieniowego, klient musi obsługiwać wieloetapową rozmowę:

1. **Tura 1 (żądanie funkcji):** wywołaj funkcję `interactions.create` z parametrem `stream: true` i zdefiniowanym parametrem `tools`. Interfejs API będzie przesyłać strumieniowo `function_call`. Musisz gromadzić ciągi JSON argumentu przyrostowego (`arguments_delta`) z `step.delta` zdarzeń, dopóki interakcja nie zostanie zakończona ze stanem `requires_action`.
2. **Tura 2 (wysyłanie wyniku):** ponownie wywołaj funkcję `interactions.create`, przekazując parametr
   `previous_interaction_id` (pasujący do identyfikatora pierwszej interakcji) i wysyłając blok `function_result` w tablicy `input`. Spowoduje to wznowienie strumienia, co umożliwi modelowi wygenerowanie ostatecznej odpowiedzi.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            }
        },
        "required": ["location"]
    }
}

# Turn 1: Request function call
stream = client.interactions.create(
    model="gemini-3.5-flash",
    tools=[weather_tool],
    input="What is the weather in Paris right now?",
    stream=True,
)

first_interaction_id = None
func_call_id = None
func_call_name = None
func_args_accumulated = ""

for event in stream:
    if event.event_type == "interaction.created":
        first_interaction_id = event.interaction.id
    elif event.event_type == "step.start":
        step = event.step
        if step.type == "function_call":
            func_call_id = step.id
            func_call_name = step.name
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments_delta":
            func_args_accumulated += event.delta.arguments

# Turn 2: Execute tool and send the result back to resume stream
if func_call_id:
    # Execute weather_tool using accumulated arguments
    dummy_result = {
        "content": [{"type": "text", "text": '{"weather": "Sunny and 22°C"}'}]
    }

    stream2 = client.interactions.create(
        model="gemini-3.5-flash",
        previous_interaction_id=first_interaction_id,
        input=[{
            "type": "function_result",
            "name": func_call_name,
            "call_id": func_call_id,
            "result": dummy_result
        }],
        stream=True,
    )

    for event in stream2:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get the current weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// Turn 1: Request function call
const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    tools: [weatherTool],
    input: "What is the weather in Paris right now?",
    stream: true,
});

let firstInteractionId = null;
let funcCallId = null;
let funcCallName = null;
let funcArgsAccumulated = "";

for await (const event of stream) {
    if (event.event_type === "interaction.created") {
        firstInteractionId = event.interaction.id;
    } else if (event.event_type === "step.start") {
        const step = event.step;
        if (step.type === "function_call") {
            funcCallId = step.id;
            funcCallName = step.name;
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "arguments_delta") {
            funcArgsAccumulated += event.delta.arguments;
        }
    }
}

// Turn 2: Execute tool and send the result back to resume stream
if (funcCallId && firstInteractionId && funcCallName) {
    const dummyResult = {
        content: [{ type: "text", text: '{"weather": "Sunny and 22°C"}' }]
    };

    const stream2 = await client.interactions.create({
        model: "gemini-3.5-flash",
        previous_interaction_id: firstInteractionId,
        input: [{
            type: "function_result",
            name: funcCallName,
            call_id: funcCallId,
            result: dummyResult
        }],
        stream: true,
    });

    for await (const event of stream2) {
        if (event.event_type === "step.delta") {
            if (event.delta.type === "text") {
                process.stdout.write(event.delta.text);
            }
        }
    }
}
```

### REST

**Tura 1:** żądanie wywołania funkcji

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the weather in Paris right now?",
    "stream": true,
    "tools": [
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

**Tura 2:** wyślij wynik funkcji za pomocą symboli `previous_interaction_id` i `call_id` z tury 1.

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "previous_interaction_id": "v1_ChdGUVFJYXBXVUdLVEF4TjhQ...",
    "stream": true,
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "CALL_ID",
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"weather\": \"Sunny and 22°C\"}"
            }
          ]
        }
      }
    ]
  }'
```

### Strumieniowanie za pomocą wielu narzędzi

W tym przykładzie w jednym żądaniu użyto zarówno narzędzia `function`, jak i `google_search`:

### Python

```
from google import genai

client = genai.Client()

tools = [
    {"type": "google_search"},
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]

stream = client.interactions.create(
    model="gemini-3.5-flash",
    tools=tools,
    input="Search what is the largest mountain in Europe and what the weather is there right now?",
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        step = event.step
        print(f"\n--- Step {event.index}: {step.type} ---")
        # Show details for tool steps
        if step.type == "google_search_call":
            print(f"  Search ID: {step.id}")
        elif step.type == "google_search_result":
            print(f"  Result for: {step.call_id}")
        elif step.type == "function_call":
            print(f"  Function: {step.name}({step.arguments})")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "google_search_call":
            print(f"  Queries: {event.delta.arguments}")
        elif event.delta.type == "arguments_delta":
            print(f"  Args chunk: {event.delta.arguments}", end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nStatus: {event.interaction.status}")
        if event.interaction.status == "requires_action":
            print("Action required: provide function call results to continue.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const tools = [
    { type: "google_search" },
    {
        type: "function",
        name: "get_weather",
        description: "Get the current weather in a given location",
        parameters: {
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                }
            },
            required: ["location"]
        }
    }
];

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    tools: tools,
    input: "Search what is the largest mountain in Europe and what the weather is there right now?",
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        const step = event.step;
        console.log(`\n--- Step ${event.index}: ${step.type} ---`);
        // Show details for tool steps
        if (step.type === "google_search_call") {
            console.log(`  Search ID: ${step.id}`);
        } else if (step.type === "google_search_result") {
            console.log(`  Result for: ${step.call_id}`);
        } else if (step.type === "function_call") {
            console.log(`  Function: ${step.name}(${JSON.stringify(step.arguments)})`);
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "google_search_call") {
            console.log(`  Queries: ${JSON.stringify(event.delta.arguments?.queries)}`);
        } else if (event.delta.type === "arguments_delta") {
            process.stdout.write(`  Args chunk: ${event.delta.arguments}`);
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nStatus: ${event.interaction.status}`);
        if (event.interaction.status === "requires_action") {
            console.log("Action required: provide function call results to continue.");
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Search what is the largest mountain in Europe and what the weather is there right now?",
    "stream": true,
    "tools": [
      { "type": "google_search" },
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"id":"mkutnkgn","signature":"","type":"google_search_call"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"google_search_call","arguments":{"queries":["largest mountain in Europe"]}},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"call_id":"mkutnkgn","signature":"","type":"google_search_result"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"google_search_result","is_error":false},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"id":"ktr5aysg","type":"function_call","name":"get_weather","arguments":{}},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"arguments":"{\"location\":\"Mount Elbrus, Russia\"}","type":"arguments_delta"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"requires_action","usage":{"total_tokens":299,"total_input_tokens":138,"input_tokens_by_modality":[{"modality":"text","tokens":138}],"total_cached_tokens":0,"total_output_tokens":20,"total_tool_use_tokens":0,"total_thought_tokens":141},"created":"2026-05-12T17:24:26Z","updated":"2026-05-12T17:24:26Z","service_tier":"standard","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Streaming z myśleniem

Gdy model używa funkcji myślenia, otrzymasz `thought` kroki z 2 rodzajami zmian: `thought_summary` (przyrostowy tekst lub podsumowanie obrazu) i `thought_signature` (zaszyfrowana reprezentacja wewnętrznego rozumowania modelu, wysyłana jako ostatnia zmiana przed `step.stop`). Jeśli funkcja `thinking_summaries` jest włączona, zmiany `thought_summary` przesyłają podsumowanie rozumowania modelu. Więcej informacji o procesie myślowym znajdziesz w [przewodniku po myśleniu](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the greatest common divisor of 1071 and 462?",
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the greatest common divisor of 1071 and 462?",
    generation_config: {
        thinking_summaries: "auto",
    },
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        } else if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the greatest common divisor of 1071 and 462?",
    "stream": true,
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"**Implementing Euclidean Algorithm**\n\nI've just worked through a detailed example applying the Euclidean algorithm to find the GCD of 1071 and 462, confirming its step-by-step nature. The calculations went smoothly, tracking the remainders until zero. My focus is now solidifying the implementation logic, ensuring accuracy and considering potential edge cases. I'll translate this example into code.\n\n\n","type":"text"},"type":"thought_summary"},"event_type":"step.delta"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

...
```

## Przesyłanie strumieniowe z agentami

Interfejs Interactions API obsługuje agentów takich jak Deep Research. Agenci używają `background=True` i zwracają wyniki asynchronicznie, ale możesz też przesyłać strumieniowo interakcje z agentem, aby otrzymywać aktualizacje postępów i kroki pośrednie na bieżąco. Więcej informacji znajdziesz w [przewodniku po wykonywaniu w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) i [przewodniku po dogłębnych badaniach](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the latest advances in quantum computing.",
    stream=True,
    background=True,
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nTotal Tokens: {event.interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "deep-research-preview-04-2026",
    input: "Research the latest advances in quantum computing.",
    stream: true,
    background: true,
    agent_config: {
        type: "deep-research",
        thinking_summaries: "auto"
    }
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nTotal Tokens: ${event.interaction.usage.total_tokens}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Research the latest advances in quantum computing.",
    "stream": true,
    "background": true,
    "agent_config": {
      "type": "deep-research",
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"***Generating research plan***\n\nTo best answer your request, I'm starting by constructing a comprehensive research plan. This will outline the key areas I need to investigate and the strategy I'll use to connect them."},"type":"thought_summary"},"event_type":"step.delta"}

... (additional thought steps) ...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"# The Quantum Inflection Point: Exhaustive Analysis of Hardware, Algorithms, and Market Dynamics in 2026\n\n## Executive Summary\n\n..."},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":1117031,"total_input_tokens":428865,"total_output_tokens":22294,"total_thought_tokens":26213},"created":"2026-05-12T17:24:27Z","updated":"2026-05-12T17:24:27Z","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Strumieniowe generowanie obrazów

Interfejs Interactions API obsługuje przesyłanie strumieniowe wielu trybów wyjściowych jednocześnie. Jeśli w `response_format` poprosisz o `text` i `image`, w tym samym strumieniu otrzymasz przeplatany tekst i wygenerowane obrazy.

W poniższym przykładzie użyto modelu `gemini-3.1-flash-image` (Nano Banana 2) do wyszukiwania informacji i generowania opowieści z przeplatanymi ilustracjami.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-image",
    tools=[{"type": "google_search", "search_types": ["web_search", "image_search"]}],
    input="Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format=[
        {"type": "text"},
        {"type": "image"}
    ],
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "image":
            print(f"\n[Image chunk: {len(event.delta.data)} bytes]", end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3.1-flash-image",
    tools: [{ type: "google_search", search_types: ["web_search", "image_search"] }],
    input: "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format: [
        { type: "text" },
        { type: "image" }
    ],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "image") {
            console.log(`\n[Image chunk: ${event.delta.data.length} bytes]`);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    "stream": true,
    "tools": [
      { "type": "google_search",
        "search_types": ["web_search", "image_search"]
      }
    ],
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "response_format": [
      { "type": "text" }, { "type": "image"}
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.1-flash-image"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"text":"Here is a short illustrated story about the Colosseum...\n\n### Part 1: The New Flavian Amphitheater\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":2,"delta":{"text":"### Part 2: The Hypogeum and the Wait\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: step.start
data: {"index":4,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":4,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":4,"delta":{"text":"### Part 3: The Moment of Spectacle\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":4,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":6128,"total_input_tokens":29,"total_output_tokens":6099,"output_tokens_by_modality":[{"modality":"image","tokens":4480}]}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Obsługa nieznanych zdarzeń

Zgodnie z zasadami dotyczącymi wersji interfejsu API z czasem mogą być dodawane nowe typy zdarzeń i typy zmian. Kod powinien prawidłowo obsługiwać nieznane typy zdarzeń – rejestrować i pomijać nierozpoznane zdarzenia, zamiast zgłaszać błąd.

## Co dalej?

- Dowiedz się więcej o [interfejsie Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).
- Poznaj [wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) za pomocą narzędzi.
- Dowiedz się więcej o [myśleniu](https://ai.google.dev/gemini-api/docs/thinking?hl=pl), które pozwala na bardziej zaawansowane wnioskowanie.
- W przypadku długotrwałych zadań wypróbuj [agenta Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).
- Wszystkie typy zdarzeń i typy zmian znajdziesz w [dokumentacji interfejsu Interactions API](https://ai.google.dev/api/interactions-api?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-07 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-07 UTC."],[],[]]
