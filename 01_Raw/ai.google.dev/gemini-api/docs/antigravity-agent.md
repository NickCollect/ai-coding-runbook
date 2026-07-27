---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl
fetched_at: 2026-07-27T04:39:28.562396+00:00
title: "Agent Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent Antigravity

Agent Antigravity to ogólnego przeznaczenia zarządzany agent w Gemini API. Pojedyncze wywołanie interfejsu API zapewnia dostęp do agenta, który rozumuje, wykonuje kod, zarządza plikami i przegląda internet w bezpiecznym środowisku Linux Sandbox hostowanym przez Google.

Działa na modelu Gemini 3.6 Flash i korzysta z tego samego środowiska co Antigravity IDE. Możesz skonfigurować model Gemini, który jest podstawą tej funkcji, za pomocą `agent_config`. Dostępne w [interfejsie Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) i [Google AI Studio](https://aistudio.google.com?hl=pl).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Uprawnienia

Każde wywołanie może udostępnić piaskownicę systemu Linux i rozpocząć pętlę korzystania z narzędzi. Agent planuje, wykonuje działania, obserwuje wyniki i powtarza te czynności, aż zadanie zostanie wykonane.

- **Wykonywanie kodu:** uruchamiaj polecenia Bash, Python i Node.js. instalować pakiety, przeprowadzać testy i tworzyć aplikacje.
- **Zarządzanie plikami:** odczytywanie, zapisywanie, edytowanie, wyszukiwanie i wyświetlanie listy plików w piaskownicy. Pliki są zachowywane podczas interakcji.
- **Dostęp do internetu:** wyszukiwanie w Google i pobieranie adresów URL w celu uzyskania danych.
- **Kompaktowanie kontekstu:** automatyczne kompaktowanie kontekstu (wyzwalane przy około 135 tys. tokenów) w celu obsługi długotrwałych sesji wieloetapowych bez utraty kontekstu i przekraczania limitów tokenów.

Więcej informacji o korzystaniu z wieloetapowych interakcji i transmitowaniu znajdziesz w [krótkim wprowadzeniu](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl).

## Obsługiwane narzędzia

Domyślnie agent ma dostęp do tych danych: `code_execution`, `google_search` i `url_context`. Narzędzia systemu plików są włączane automatycznie po określeniu parametru `environment`. Możesz też zdefiniować **funkcje niestandardowe**, aby połączyć agenta z własnymi interfejsami API i narzędziami. Parametr `tools` musisz podać tylko wtedy, gdy dostosowujesz lub ograniczasz domyślny zestaw albo dodajesz funkcje niestandardowe.

| Narzędzie | Wpisz wartość | Opis |
| --- | --- | --- |
| Wykonanie kodu | `code_execution` | Uruchamiaj polecenia powłoki (bash, Python, Node) z przechwytywaniem stdout/stderr. |
| Wyszukiwarka Google | `google_search` | Wyszukiwanie w sieci publicznej. |
| Kontekst adresu URL | `url_context` | pobierać i odczytywać strony internetowe, |
| System plików | *(włączone za pomocą `environment`)* | odczytywać, zapisywać, edytować, wyszukiwać i wyświetlać listę plików w piaskownicy; Brak osobnego typu narzędzia; włączany automatycznie po ustawieniu `environment`. |
| Funkcje niestandardowe | `function` | Zdefiniuj funkcje niestandardowe, o których wykonanie agent może poprosić. Zobacz [Wywoływanie funkcji](#function-calling). |
| Zdalny serwer MCP | `mcp_server` | Rejestrowanie zewnętrznych serwerów Model Context Protocol (MCP) jako narzędzi. Zobacz [serwery MCP](#mcp-servers). |

Aby ograniczyć agenta do określonych narzędzi, przekaż tylko te, których potrzebujesz:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## Wielomodalne wprowadzanie danych

Agent Antigravity obsługuje dane wejściowe multimodalne. Obecnie obsługiwane są tylko dane wejściowe `text` i `image`. Obrazy muszą być podane jako ciągi tekstowe zakodowane w formacie base64 (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## Wywoływanie funkcji

Wywoływanie funkcji umożliwia połączenie agenta Antigravity z zewnętrznymi interfejsami API i bazami danych przez zdefiniowanie niestandardowych narzędzi, które agent może wywoływać. Ogólne informacje znajdziesz w artykule [Wywoływanie funkcji za pomocą interfejsu Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=pl).

Poniższy przykład przedstawia interakcję dwuetapową. Najpierw agent wysyła żądanie niestandardowego wywołania funkcji `get_weather`, a klient wykonuje je i zwraca wynik w drugiej turze.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## Serwery MCP

Możesz połączyć agenta Antigravity z narzędziami zewnętrznymi, rejestrując zdalne serwery MCP (Model Context Protocol). Agent obsługuje zdalne serwery MCP za pomocą przesyłanego strumieniowo protokołu HTTP.

Podczas rejestrowania serwera MCP musisz podać te pola w tablicy `tools`:

| Pole | Typ | Wymagane | Opis |
| --- | --- | --- | --- |
| `type` | ciąg znaków | Tak | Musi to być `"mcp_server"`. |
| `name` | ciąg znaków | Tak | Unikalny identyfikator serwera. Musi składać się wyłącznie z małych liter i cyfr (zgodnie z `^[a-z0-9_-]+$`). |
| `url` | ciąg znaków | Tak | Adres URL punktu końcowego zdalnego serwera MCP. |
| `headers` | obiekt | Nie | Niestandardowe nagłówki (np. uwierzytelnianie) wysyłane z żądaniami. |
| `allowed_tools` | tablica | Nie | Lista nazw narzędzi, które mogą być wykonywane. Jeśli ta opcja zostanie pominięta, wszystkie narzędzia będą dozwolone. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## Wybór modelu

W przypadku `antigravity-preview-05-2026` domyślnym modelem jest **Gemini 3.6 Flash** (`gemini-3.6-flash`). Jeśli pominiesz `agent_config`, agent domyślnie użyje modelu `gemini-3.6-flash`.

Możesz skonfigurować model Gemini, używając `agent_config`, aby zoptymalizować go pod kątem szybkości, kosztów lub możliwości rozumowania.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.5-flash-lite",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.5-flash-lite",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-3.5-flash-lite"
      }
  }'
```

Obsługiwane wartości parametru `agent_config.model` to:

| Model | Wartość w kolumnie `agent_config.model` | Opis |
| --- | --- | --- |
| **Gemini 3.6 Flash** (domyślny) | `gemini-3.6-flash` | Domyślny zrównoważony model do rozumowania, kodowania i korzystania z narzędzi. |
| **Gemini 3.5 Flash** | `gemini-3.5-flash` | Model Flash poprzedniej generacji do ogólnych przepływów pracy agentów. |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | Lekki model zoptymalizowany pod kątem krótkiego czasu oczekiwania i zadań wrażliwych na koszty. |

Podczas tworzenia zarządzanego agenta za pomocą `agents.create` model konfiguruje się w dokładnie taki sam sposób, przekazując `base_agent` i `agent_config`. Pamiętaj, że w przypadku zarządzanego agenta utworzonego za pomocą `agents.create` nie możesz zastąpić modelu w momencie interakcji. Model jest zablokowany na ustawienie, które zostało skonfigurowane podczas tworzenia agenta. Zapewnia to przewidywalne działanie wywoływania narzędzi, spójne debugowanie i przestrzeganie granic bezpieczeństwa.

## Dostosowywanie agenta

Możesz rozszerzyć możliwości agenta Antigravity, dostosowując jego instrukcje, narzędzia i środowisko. Agent obsługuje natywne dla systemu plików podejście do dostosowywania: możesz zamontować pliki, takie jak `AGENTS.md`, z instrukcjami i umiejętnościami w `.agents/skills/` bezpośrednio w piaskownicy lub przekazać konfigurację w linii w momencie interakcji. Możesz iteracyjnie modyfikować konfigurację, a gdy będzie gotowa, zapisać ją jako zarządzanego agenta.

Szczegółowe informacje o tworzeniu niestandardowych agentów znajdziesz w artykule [Tworzenie zarządzanych agentów](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl).

## Wykonywanie w tle

Wykonanie zadań agenta, które wymagają wieloetapowego rozumowania, wykonania kodu lub operacji na plikach, może potrwać kilka minut. Użyj `background=True`, aby uruchomić interakcję asynchronicznie. Interfejs API zwraca od razu identyfikator interakcji, który jest sprawdzany do momentu, aż stan zmieni się na `completed` lub `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

Uruchamianie w tle wymaga `store=True`, które jest domyślnie włączone. Aby otrzymywać aktualizacje postępu w czasie rzeczywistym podczas wykonywania w tle, zapoznaj się z sekcją [Przesyłanie strumieniowe interakcji w tle](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=pl#streaming-background).

Trwającą interakcję w tle możesz anulować za pomocą metody `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**Wieloetapowe wykonywanie z działaniem w tle**

Jeśli interakcja w tle obejmuje narzędzia stanowe (np. wykonywanie kodu w piaskownicy), użyj `environment_id` z zakończonej interakcji, aby kontynuować w tym samym środowisku. Dzięki temu agent będzie mógł kontynuować pracę od miejsca, w którym ją przerwał, zachowując wszystkie pliki i stan.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## Środowiska

Każde wywołanie tworzy lub ponownie wykorzystuje piaskownicę Linuksa. Parametr `environment` może przyjmować 3 postaci:

| Formularz | Opis |
| --- | --- |
| `"remote"` | Utwórz nowe środowisko piaskownicy z ustawieniami domyślnymi. |
| `"env_abc123"` | Użyj ponownie istniejącego środowiska według identyfikatora, zachowując wszystkie pliki i stan. |
| `{...}` | Pełna `EnvironmentConfig` z niestandardowymi źródłami i regułami sieciowymi. |

Szczegółowe informacje o źródłach (Git, GCS, wbudowane), sieciach, cyklu życia i limitach zasobów znajdziesz w sekcji [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).

## Aktywatory

Aktywatory umożliwiają zaplanowanie automatycznego uruchamiania agenta zgodnie z harmonogramem crona. Wyzwalacz wiąże agenta, środowisko, prompt i harmonogram w trwały zasób, który uruchamia się bez interwencji użytkownika. Każde wykonanie ponownie wykorzystuje to samo środowisko, więc pliki utworzone w jednym przebiegu są zachowywane i widoczne w następnym.

### Utwórz aktywator

Utwórz aktywator, określając harmonogram crona, strefę czasową i konfigurację interakcji. Wywoływacz zaczyna działać w stanie `active` i zostanie uruchomiony przy następnym pasującym czasie crona. Zapisz zwrócony element `id`, aby zarządzać wyzwalaczem w kolejnych wywołaniach.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

Żądanie `CreateTrigger` akceptuje te pola:

| Pole | Typ | Wymagane | Opis |
| --- | --- | --- | --- |
| `schedule` | ciąg znaków | Tak | Wyrażenie cron (np. `0 * * * *` w przypadku co godzinę, `0 9 * * 1-5` w przypadku poranków w dni powszednie). |
| `time_zone` | ciąg znaków | Tak | Strefa czasowa IANA (np. `UTC`, `America/Argentina/Buenos_Aires`). |
| `display_name` | ciąg znaków | Nie | Zrozumiała dla człowieka nazwa reguły. |
| `max_consecutive_failures` | liczba całkowita | Nie | Maksymalna liczba niepowodzeń, po której reguła zostanie automatycznie wstrzymana. Domyślnie: 5. |
| `execution_timeout_seconds` | liczba całkowita | Nie | Czas oczekiwania na wykonanie w sekundach. Domyślnie: 600. |
| `interaction` | obiekt | Tak | `CreateInteractionRequest`, który określa agenta, dane wejściowe, narzędzia i środowisko. |

Odpowiedź zawiera te kluczowe pola:

| Pole | Typ | Opis |
| --- | --- | --- |
| `id` | ciąg znaków | Unikalny identyfikator wyzwalacza. Używaj go we wszystkich kolejnych operacjach. |
| `status` | ciąg znaków | Obecny stan: `active`, `paused` lub `disabled`. |
| `next_run_time` | ciąg znaków | Sygnatura czasowa ISO 8601 następnego zaplanowanego wykonania. |
| `consecutive_failure_count` | liczba całkowita | Liczba kolejnych nieudanych wykonań od ostatniego udanego wykonania. |

### Wyświetlanie listy aktywatorów

Pobierz wszystkie wyzwalacze powiązane z projektem.

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Pobieranie wyzwalacza

Pobierz pełną konfigurację i bieżący stan pojedynczego wyzwalacza.

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Wstrzymywanie i wznawianie

Możesz wstrzymać wyzwalacz, aby zatrzymać zaplanowane wykonania, i wznowić go, aby ponownie aktywować harmonogram. Wstrzymanie nie ma wpływu na ręczne wykonywanie.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### Usuń aktywator

trwale usunąć wyzwalacz. Historia poprzednich wykonań nie zostanie usunięta.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Natychmiastowe uruchomienie aktywatora

Uruchamiaj wyzwalacz na żądanie bez czekania na następny zaplanowany czas. Działa to nawet wtedy, gdy wyzwalacz jest wstrzymany.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Wyświetlenie listy uruchomień

Wyświetl historię wykonania wyzwalacza. Każde wykonanie zawiera `status`, sygnatury czasowe, `interaction_id`, za pomocą którego możesz pobrać pełne dane wyjściowe interakcji, oraz `environment_id` potwierdzający, że wszystkie uruchomienia korzystają z tej samej piaskownicy.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Dostępność i ceny

Agent Antigravity jest dostępny w wersji testowej w ramach [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) w Google AI Studio oraz w Gemini API w przypadku projektów na poziomie bezpłatnym i płatnym.

Ceny są oparte na [modelu płatności według wykorzystania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents), który uwzględnia tokeny bazowego modelu Gemini i narzędzia używane przez agenta. W przeciwieństwie do standardowego żądania czatu, które generuje pojedynczy wynik, interakcja z Antigravity to proces oparty na działaniach agenta. Pojedyncze żądanie wywołuje autonomiczny cykl rozumowania, wykonywania narzędzi, uruchamiania kodu i zarządzania plikami. Projekty na poziomie bezpłatnym obejmują bezpłatny limit szybkości i limit wykorzystania.

Interakcje z Antigravity działają w wieloetapowych autonomicznych pętlach i mogą zużywać znaczną liczbę tokenów. Ustaw [limity budżetu](#budget-controls) w żądaniu, aby ograniczyć wykorzystanie tokenów. Możesz też śledzić postępy w czasie rzeczywistym za pomocą [strumieniowania SSE](https://ai.google.dev/gemini-api/docs/streaming?hl=pl) lub anulować uruchomione żądania.

### Ustawienia budżetu

Oprócz [wyboru modelu](#model-selection) ustaw `max_total_tokens` w `agent_config` (z `"type": "antigravity"`), aby ograniczyć łączną liczbę tokenów (dane wejściowe + dane wyjściowe + myślenie), które może wykorzystać interakcja.
Tokeny w pamięci podręcznej nie wliczają się do tego limitu. Gdy agent osiągnie limit, interakcja zostanie przerwana i zwróci wartość `status: "incomplete"`. Limit jest określany w miarę możliwości: rzeczywiste wykorzystanie może go nieznacznie przekroczyć w zależności od tego, kiedy agent sprawdza budżet między poszczególnymi krokami.

Ustaw budżet w prośbie o interakcję w `agent_config` wraz z `agent` i `input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### Kontynuowanie niedokończonej interakcji

Gdy interakcja zostanie przywrócona `status: "incomplete"`, praca agenta i kontekst zostaną zachowane. Wyślij nową interakcję, która odwołuje się do pierwotnej interakcji `id` i `environment_id`, aby kontynuować ją w miejscu, w którym została przerwana. Nowa interakcja ma własny budżet `max_total_tokens`.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### Szacunkowy koszt

Koszty zależą od złożoności zadania. Pracownik obsługi klienta samodzielnie określa, ile wywołań narzędzi, wykonań kodu i operacji na plikach jest potrzebnych. Poniższe szacunki są oparte na przebiegach.

| Kategoria zadania | Tokeny wejściowe | Tokeny wyjściowe | Typowy koszt |
| --- | --- | --- | --- |
| **Badania i synteza informacji** | 100–500 tys. | 10–40 tys. | 0,30–1,00 USD |
| **Generowanie dokumentów i treści** | 100–500 tys. | 15–50 tys. | 0,30–1,30 PLN |
| **Projektowanie procesów i systemów** | 100–400 tys. | 10–30 tys. | 0,25–0,80 USD |
| **Przetwarzanie i analiza danych** | 300 tys.–3 mln | 30 tys.–150 tys. | 0,70–3,25 PLN |

Zwykle w pamięci podręcznej jest przechowywanych 50–70% tokenów wejściowych. Złożone przepływy pracy agenta z wieloma wywołaniami narzędzi mogą w jednej interakcji zgromadzić 3–5 mln tokenów, co wiąże się z kosztem do 5 USD.

**Obliczenia środowiskowe** (procesor, pamięć, wykonywanie w piaskownicy) w okresie wersji testowej **nie są rozliczane**.

## Ograniczenia

- **Stan wersji podglądowej:** agent Antigravity i interfejs Interactions API. Funkcje i schematy mogą ulec zmianie.
- **Nieobsługiwana konfiguracja generowania:** te parametry nie są obsługiwane i zwracają błąd 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Uporządkowane dane wyjściowe:** agent Antigravity nie obsługuje uporządkowanych danych wyjściowych.
- **Niedostępne narzędzia:** `file_search`, `computer_use` i `google_maps` nie są jeszcze obsługiwane.
- **Ograniczenia zdalnego MCP:** transport zdarzeń wysyłanych przez serwer (SSE) nie jest obsługiwany (używaj strumieniowego HTTP). Dodatkowo serwer `name` musi być zapisany wyłącznie małymi literami i zawierać tylko znaki alfanumeryczne (użycie wielkich liter powoduje ogólny błąd `400 Bad Request`).
- **Narzędzie systemu plików:** obecnie nie ma narzędzia systemu plików. Jest ona częścią `environment`.
- **Wymaganie dotyczące sklepu:** wykonywanie agenta za pomocą `background=True` wymaga `store=True`.
- **Wywoływanie funkcji tylko w trybie stanowym:** wywoływanie funkcji jest obsługiwane tylko w trybie stanowym. Aby kontynuować turę, musisz użyć `previous_interaction_id`. Ręczne odtwarzanie historii (tryb bezstanowy) nie jest obsługiwane.
- **Nieobsługiwane typy multimodalne.** Dane wejściowe w postaci audio, wideo i dokumentów nie są obecnie obsługiwane. Dozwolone są tylko tekst i obraz.

## Co dalej?

- [Szybki start:](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl) rozmowy wieloetapowe i streaming.
- [Tworzenie agentów niestandardowych:](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl) instrukcje niestandardowe, umiejętności i zapisywanie agentów.
- [Środowiska:](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl) konfiguracja piaskownicy, źródła, sieć.
- [Agent Deep Research:](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) zadania badawcze o dłuższej formie.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl): bazowy interfejs API.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-21 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-21 UTC."],[],[]]
