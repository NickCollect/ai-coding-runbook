---
source_url: https://ai.google.dev/gemini-api/docs/deep-research?hl=pl
fetched_at: 2026-08-24T02:20:11.928516+00:00
title: "Agent Deep Research w\u00a0Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent Deep Research w Gemini

Agent Gemini Deep Research autonomicznie planuje, wykonuje i syntetyzuje wieloetapowe zadania badawcze. Dzięki Gemini potrafi poruszać się po złożonych zasobach informacji, aby tworzyć szczegółowe raporty z cytatami. Nowe funkcje umożliwiają wspólne planowanie z agentem, łączenie się z narzędziami zewnętrznymi za pomocą serwerów MCP, dodawanie wizualizacji (takich jak wykresy) i bezpośrednie przekazywanie dokumentów jako danych wejściowych.

Zadania badawcze obejmują iteracyjne wyszukiwanie i czytanie, a ich wykonanie może potrwać kilka minut. Aby uruchomić agenta asynchronicznie i sprawdzać wyniki lub przesyłać strumieniowo aktualizacje, musisz użyć [wykonywania w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) (ustaw `background=true`). Więcej informacji znajdziesz w sekcji [Obsługa długotrwałych zadań](#long-running-tasks).

Poniższy przykład pokazuje, jak rozpocząć analizę w tle i sprawdzać wyniki.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Obsługiwane wersje

Agent Deep Research jest dostępny w 2 wersjach:

- **Deep Research** (`deep-research-preview-04-2026`): zaprojektowany z myślą o szybkości i wydajności, idealny do przesyłania strumieniowego do interfejsu klienta.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): maksymalna kompleksowość automatycznego zbierania i syntezy kontekstu.

## Planowanie zespołowe

Planowanie oparte na współpracy daje Ci kontrolę nad kierunkiem badań, zanim agent rozpocznie pracę. Możesz przejrzeć i dopracować plan badań przed jego realizacją. Gdy ta opcja jest włączona, agent zwraca proponowany plan badań zamiast natychmiastowego wykonania. Następnie możesz przejrzeć, zmodyfikować lub zatwierdzić plan w ramach interakcji wieloetapowych.

### Krok 1. Poproś o plan

Ustaw `collaborative_planning=True` w pierwszej interakcji. Zamiast pełnego raportu agent zwraca plan badań.

### Python

```
from google import genai

client = genai.Client()

# First interaction: request a research plan
plan_interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Do some research on Google TPUs.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    background=True,
)

# Wait for and retrieve the plan
while (result := client.interactions.get(id=plan_interaction.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const planInteraction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Do some research on Google TPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    background: true
});

let result;
while ((result = await client.interactions.get(planInteraction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Do some research on Google TPUs.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "background": true
}'
```

### Krok 2. Ulepsz plan (opcjonalnie)

Użyj `previous_interaction_id`, aby kontynuować rozmowę i ulepszać plan. Naciśnij `collaborative_planning=True`, aby pozostać w trybie planowania.

### Python

```
# Second interaction: refine the plan
refined_plan = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": True,
    },
    previous_interaction_id=plan_interaction.id,
    background=True,
)

while (result := client.interactions.get(id=refined_plan.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const refinedPlan = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Focus more on the differences between Google TPUs and competitor hardware, and less on the history.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: true
    },
    previous_interaction_id: planInteraction.id,
    background: true
});

let result;
while ((result = await client.interactions.get(refinedPlan.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Focus more on the differences between Google TPUs and competitor hardware, and less on the history.",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": true
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

### Krok 3. Zatwierdź i wykonaj

Ustaw wartość `collaborative_planning=False` (lub pomiń ją), aby zatwierdzić plan i rozpocząć zbieranie informacji.

### Python

```
# Third interaction: approve the plan and kick off research
final_report = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Plan looks good!",
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": False,
    },
    previous_interaction_id=refined_plan.id,
    background=True,
)

while (result := client.interactions.get(id=final_report.id)).status != "completed":
    time.sleep(5)
print(result.steps[-1].content[0].text)
```

### JavaScript

```
const finalReport = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Plan looks good!',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        collaborative_planning: false
    },
    previous_interaction_id: refinedPlan.id,
    background: true
});

let result;
while ((result = await client.interactions.get(finalReport.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}
console.log(result.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Plan looks good!",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "collaborative_planning": false
    },
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID",
    "background": true
}'
```

## Wizualizacja

Gdy `visualization` jest ustawione na `"auto"`, agent może generować wykresy i inne elementy wizualne, aby wspierać wyniki swoich badań.
Wygenerowane obrazy są uwzględniane w krokach odpowiedzi i przesyłane strumieniowo jako delty `image`. Aby uzyskać najlepsze wyniki, w zapytaniu wyraźnie poproś o elementy wizualne, np. „Dołącz wykresy pokazujące trendy na przestrzeni czasu” lub „Wygeneruj grafiki porównujące udziały w rynku”. Ustawienie `visualization` na `"auto"` włącza tę funkcję, ale agent generuje wizualizacje tylko wtedy, gdy jest o to proszony w prompcie.

### Python

```
import base64
import time

from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Analyze global semiconductor market trends. Include graphics showing market share changes.",
    agent_config={
        "type": "deep-research",
        "visualization": "auto",
    },
    background=True,
)

print(f"Research started: {interaction.id}")

while (result := client.interactions.get(id=interaction.id)).status != "completed":
    time.sleep(5)

for step in result.steps:
    if step.type == "model_output":
        for content_item in step.content:
            if content_item.type == "text":
                print(content_item.text)
            elif content_item.type == "image" and content_item.data:
                image_bytes = base64.b64decode(content_item.data)
                print(f"Received image: {len(image_bytes)} bytes")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Analyze global semiconductor market trends. Include graphics showing market share changes.',
    agent_config: {
        type: 'deep-research',
        visualization: 'auto'
    },
    background: true
});

console.log(`Research started: ${interaction.id}`);

let result;
while ((result = await client.interactions.get(interaction.id)).status !== 'completed') {
    await new Promise(r => setTimeout(r, 5000));
}

for (const step of result.steps) {
    if (step.type === 'model_output') {
        for (const contentItem of step.content) {
            if (contentItem.type === 'text') {
                console.log(contentItem.text);
            } else if (contentItem.type === 'image' && contentItem.data) {
                console.log(`[Image Output: ${contentItem.data.substring(0, 20)}...]`);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Analyze global semiconductor market trends. Include graphics showing market share changes.",
    "agent_config": {
        "type": "deep-research",
        "visualization": "auto"
    },
    "background": true
}'
```

## Obsługiwane narzędzia

Funkcja Deep Research obsługuje wiele wbudowanych i zewnętrznych narzędzi. Domyślnie (gdy nie podano parametru `tools`) agent ma dostęp do wyszukiwarki Google, kontekstu adresu URL i wykonywania kodu. Możesz wyraźnie określić narzędzia, aby ograniczyć lub rozszerzyć możliwości agenta.

| Narzędzie | Wpisz wartość | Opis |
| --- | --- | --- |
| Wyszukiwarka Google | `google_search` | Wyszukiwanie w sieci publicznej. Ta opcja jest domyślnie włączona. |
| Kontekst adresu URL | `url_context` | czytać i podsumowywać treści na stronach internetowych; Ta opcja jest domyślnie włączona. |
| Wykonanie kodu | `code_execution` | wykonywać kod w celu przeprowadzania obliczeń i analizy danych, Ta opcja jest domyślnie włączona. |
| Serwer MCP | `mcp_server` | Łączenie się ze zdalnymi serwerami MCP w celu uzyskania dostępu do narzędzi zewnętrznych. |
| Wyszukiwanie plików | `file_search` | Wyszukiwanie w przesłanych korpusach dokumentów. |

### Wyszukiwarka Google

Włącz wyszukiwarkę Google jako jedyne narzędzie:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="What are the latest developments in quantum computing?",
    tools=[{"type": "google_search"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'What are the latest developments in quantum computing?',
    tools: [{ type: 'google_search' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "What are the latest developments in quantum computing?",
    "tools": [{"type": "google_search"}],
    "background": true
}'
```

### Kontekst adresu URL

Umożliwienie agentowi odczytywania i streszczania konkretnych stron internetowych:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Summarize the content of https://www.wikipedia.org/.",
    tools=[{"type": "url_context"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Summarize the content of https://www.wikipedia.org/.',
    tools: [{ type: 'url_context' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Summarize the content of https://www.wikipedia.org/.",
    "tools": [{"type": "url_context"}],
    "background": true
}'
```

### Wykonanie kodu

Zezwól agentowi na wykonywanie kodu do obliczeń i analizy danych:

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Calculate the 50th Fibonacci number.",
    "agent": "deep-research-preview-04-2026",
    "tools": [{"type": "code_execution"}],
    "background": true
}'
```

### Serwery MCP

Łącz się ze zdalnymi serwerami MCP, aby umożliwić agentowi dostęp do narzędzi i usług zewnętrznych.

W konfiguracji narzędzi podaj serwer `name` i `url`. Możesz też przekazywać dane logowania i ograniczać narzędzia, z których może korzystać agent.

| Pole | Typ | Wymagane | Opis |
| --- | --- | --- | --- |
| `type` | `string` | Tak | Musi to być `"mcp_server"`. |
| `name` | `string` | Nie | Wyświetlana nazwa serwera MCP. |
| `url` | `string` | Nie | Pełny adres URL punktu końcowego serwera MCP. |
| `headers` | `object` | Nie | Pary klucz-wartość wysyłane jako nagłówki HTTP z każdym żądaniem do serwera (np. tokeny uwierzytelniania). |
| `allowed_tools` | `array` | Nie | Ogranicz narzędzia na serwerze, z których agent może korzystać. |

#### Podstawowe użycie

### Python

```
interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ],
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ],
    background: true
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ],
    "background": true
}'
```

### Wyszukiwanie plików

Udostępnij agentowi własne dane za pomocą narzędzia [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Compare our 2025 fiscal year report against current public web news.",
    agent="deep-research-preview-04-2026",
    background=True,
    tools=[
        {
            "type": "file_search",
            "file_search_store_names": ['fileSearchStores/my-store-name']
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Compare our 2025 fiscal year report against current public web news.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    tools: [
        { type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] },
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Compare our 2025 fiscal year report against current public web news.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "tools": [
        {"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]},
    ]
}'
```

## Sterowanie i formatowanie

Możesz sterować danymi wyjściowymi agenta, podając w prompcie konkretne instrukcje formatowania. Umożliwia to dzielenie raportów na określone sekcje i podsekcje, dodawanie tabel danych oraz dostosowywanie tonu do różnych odbiorców (np. „techniczny”, „dla kadry kierowniczej”, „nieformalny”).

W tekście wejściowym wyraźnie określ żądany format wyjściowy.

### Python

```
prompt = """
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
"""

interaction = client.interactions.create(
    input=prompt,
    agent="deep-research-preview-04-2026",
    background=True
)
```

### JavaScript

```
const prompt = `
Research the competitive landscape of EV batteries.

Format the output as a technical report with the following structure:
1. Executive Summary
2. Key Players (Must include a data table comparing capacity and chemistry)
3. Supply Chain Risks
`;

const interaction = await client.interactions.create({
    input: prompt,
    agent: 'deep-research-preview-04-2026',
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of EV batteries.\n\nFormat the output as a technical report with the following structure: \n1. Executive Summary\n2. Key Players (Must include a data table comparing capacity and chemistry)\n3. Supply Chain Risks",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'
```

## Dane wejściowe multimodalne

Deep Research obsługuje dane wejściowe w różnych formatach, w tym obrazy i dokumenty (PDF), co umożliwia agentowi analizowanie treści wizualnych i przeprowadzanie wyszukiwania w internecie w kontekście podanych danych wejściowych.

### Python

```
import time
from google import genai

client = genai.Client()

prompt = """Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground."""

interaction = client.interactions.create(
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"
        }
    ],
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started: {interaction.id}")

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.steps[-1].content[0].text)
        break
    elif interaction.status == "failed":
        print(f"Research failed: {interaction.error}")
        break
    time.sleep(10)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const prompt = `Analyze the interspecies dynamics and behavioral risks present
in the provided image of the African watering hole. Specifically, investigate
the symbiotic relationship between the avian species and the pachyderms
shown, and conduct a risk assessment for the reticulated giraffes based on
their drinking posture relative to the specific predator visible in the
foreground.`;

const interaction = await client.interactions.create({
    input: [
        { type: 'text', text: prompt },
        {
            type: 'image',
            mime_type: "image/jpeg",
            uri: 'https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg'
        }
    ],
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started: ${interaction.id}`);

while (true) {
    const result = await client.interactions.get(interaction.id);
    if (result.status === 'completed') {
        console.log(result.steps.at(-1).content[0].text);
        break;
    } else if (result.status === 'failed') {
        console.log(`Research failed: ${result.error}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the research task with image input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": [
        {"type": "text", "text": "Analyze the interspecies dynamics and behavioral risks present in the provided image of the African watering hole. Specifically, investigate the symbiotic relationship between the avian species and the pachyderms shown, and conduct a risk assessment for the reticulated giraffes based on their drinking posture relative to the specific predator visible in the foreground."},
        {"type": "image", "mime_type": "image/jpeg", "uri": "https://storage.googleapis.com/generativeai-downloads/images/generated_elephants_giraffes_zebras_sunset.jpg"}
    ],
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Rozumienie dokumentów

Rozumienie dokumentów umożliwia przekazywanie dokumentów bezpośrednio jako danych wejściowych multimodalnych.
Agent analizuje podane dokumenty i przeprowadza badania na podstawie ich treści.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "https://arxiv.org/pdf/1706.03762",
            "mime_type": "application/pdf",
        },
    ],
    background=True,
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'https://arxiv.org/pdf/1706.03762',
            mime_type: 'application/pdf'
        }
    ],
    background: true
});
```

### REST

```
# 1. Start the research task with document input
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "deep-research-preview-04-2026",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {"type": "document", "uri": "https://arxiv.org/pdf/1706.03762", "mime_type": "application/pdf"}
    ],
    "background": true
}'
```

## Obsługa długotrwałych zadań

Deep Research to wieloetapowy proces obejmujący planowanie, wyszukiwanie, czytanie i pisanie. Ten cykl zwykle przekracza standardowe limity czasu oczekiwania synchronicznych wywołań interfejsu API.

Przedstawiciele muszą korzystać z usługi `background=True`. Interfejs API od razu zwraca obiekt częściowy
`Interaction`. Za pomocą właściwości `id` możesz pobrać interakcję na potrzeby ankiety. Stan interakcji zmieni się z `in_progress` na `completed` lub `failed`. Szczegółowy przewodnik zarządzania zadaniami w tle znajdziesz w artykule [Wykonywanie w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl).

### Streaming

Deep Research obsługuje przesyłanie strumieniowe, dzięki czemu możesz otrzymywać aktualizacje w czasie rzeczywistym dotyczące postępów w badaniach, w tym podsumowania przemyśleń, dane wyjściowe w postaci tekstu i wygenerowane obrazy.
Musisz ustawić wartości `stream=True` i `background=True`.

Aby otrzymywać pośrednie kroki rozumowania (myśli) i informacje o postępach, musisz włączyć **podsumowania myślenia**, ustawiając wartość `thinking_summaries` na `"auto"` w `agent_config`. Bez tego strumień może dostarczać tylko wyniki końcowe.

#### Typy zdarzeń strumienia

| Typ zdarzenia | Typ delty | Opis |
| --- | --- | --- |
| `step.delta` | `thought` | Pośredni krok rozumowania agenta. |
| `step.delta` | `text` | Część ostatecznego tekstu wyjściowego. |
| `step.delta` | `image` | Wygenerowany obraz (zakodowany w formacie base64). |

W tym przykładzie rozpoczyna się zadanie badawcze i przetwarzanie strumienia z automatycznym ponownym łączeniem. Śledzi ona `interaction_id` i `last_event_id`, dzięki czemu w przypadku utraty połączenia (np. po upływie 600-sekundowego limitu czasu) może wznowić działanie od miejsca, w którym zostało przerwane.

### Python

```
from google import genai

client = genai.Client()

interaction_id = None
last_event_id = None
is_complete = False

def process_stream(stream):
    global interaction_id, last_event_id, is_complete
    for event in stream:
        if event.event_type == "interaction.created":
            interaction_id = event.interaction.id
        if event.event_id:
            last_event_id = event.event_id
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "thought":
                print(f"Thought: {event.delta.text}", flush=True)
        elif event.event_type in ("interaction.completed", "interaction.error"):
            is_complete = True

stream = client.interactions.create(
    input="Research the history of Google TPUs.",
    agent="deep-research-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"},
)
process_stream(stream)

# Reconnect if the connection drops
while not is_complete and interaction_id:
    status = client.interactions.get(interaction_id)
    if status.status != "in_progress":
        break
    stream = client.interactions.get(
        id=interaction_id, stream=True, last_event_id=last_event_id,
    )
    process_stream(stream)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

let interactionId;
let lastEventId;
let isComplete = false;

async function processStream(stream) {
    for await (const event of stream) {
        if (event.type === 'interaction.created') {
            interactionId = event.interaction.id;
        }
        if (event.event_id) lastEventId = event.event_id;
        if (event.type === 'step.delta') {
            if (event.delta.type === 'text') {
                process.stdout.write(event.delta.text);
            } else if (event.delta.type === 'thought') {
                console.log(`Thought: ${event.delta.text}`);
            }
        } else if (['interaction.completed', 'interaction.error'].includes(event.type)) {
            isComplete = true;
        }
    }
}

const stream = await client.interactions.create({
    input: 'Research the history of Google TPUs.',
    agent: 'deep-research-preview-04-2026',
    background: true,
    stream: true,
    agent_config: { type: 'deep-research', thinking_summaries: 'auto' },
});
await processStream(stream);

// Reconnect if the connection drops
while (!isComplete && interactionId) {
    const status = await client.interactions.get(interactionId);
    if (status.status !== 'in_progress') break;
    const resumeStream = await client.interactions.get(interactionId, {
        stream: true, last_event_id: lastEventId,
    });
    await processStream(resumeStream);
}
```

### REST

```
# 1. Start the stream (save the INTERACTION_ID from the interaction.start event
#    and the last "event_id" you receive)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of Google TPUs.",
    "agent": "deep-research-preview-04-2026",
    "background": true,
    "stream": true,
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
}'

# 2. If the connection drops, reconnect with your saved IDs
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID?stream=true&last_event_id=LAST_EVENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Dodatkowe pytania i interakcje

Po przesłaniu przez pracownika obsługi klienta ostatecznego raportu możesz kontynuować rozmowę, korzystając z `previous_interaction_id`. Dzięki temu możesz poprosić o wyjaśnienie, podsumowanie lub rozwinięcie określonych sekcji badania bez konieczności ponownego rozpoczynania całego zadania.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="Can you elaborate on the second point in the report?",
    model="gemini-3.1-pro-preview",
    previous_interaction_id="COMPLETED_INTERACTION_ID"
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    input: 'Can you elaborate on the second point in the report?',
    model: 'gemini-3.1-pro-preview',
    previous_interaction_id: 'COMPLETED_INTERACTION_ID'
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Can you elaborate on the second point in the report?",
    "model": "gemini-3.1-pro-preview",
    "previous_interaction_id": "COMPLETED_INTERACTION_ID"
}'
```

## Kiedy warto używać agenta Deep Research w Gemini

Deep Research to **agent**, a nie tylko model. Najlepiej sprawdza się w przypadku zbiorów zadań, które wymagają podejścia „analityk w pudełku”, a nie czatu o niskim poziomie opóźnień.

| Funkcja | Standardowe modele Gemini | Agent Deep Research w Gemini |
| --- | --- | --- |
| **Opóźnienie** | Sekundy | Minuty (asynchroniczne/w tle) |
| **Proces** | Generowanie –> dane wyjściowe | Planowanie –> Wyszukiwanie –> Czytanie –> Iteracja –> Wynik |
| **Dane wyjściowe** | tekst konwersacyjny, kod, krótkie podsumowania; | Szczegółowe raporty, długie analizy, tabele porównawcze |
| **Najlepsze zastosowania** | Chatboty, wyodrębnianie, pisanie kreatywne | analiza rynku, należyta staranność, przeglądy literatury, analiza konkurencji; |

## Konfiguracja agenta

Funkcja Deep Research używa parametru `agent_config` do kontrolowania zachowania.
Przekaż go jako słownik z tymi polami:

| Pole | Typ | Domyślny | Opis |
| --- | --- | --- | --- |
| `type` | `string` | Wymagane | Musi to być `"deep-research"`. |
| `thinking_summaries` | `string` | `"none"` | Ustaw wartość `"auto"`, aby otrzymywać pośrednie kroki rozumowania podczas przesyłania strumieniowego. Aby wyłączyć tę funkcję, ustaw wartość `"none"`. |
| `visualization` | `string` | `"auto"` | Ustaw wartość `"auto"`, aby włączyć wykresy i obrazy generowane przez agenta. Aby wyłączyć tę funkcję, ustaw wartość `"off"`. |
| `collaborative_planning` | `boolean` | `false` | Ustaw na `true`, aby włączyć wieloetapowe sprawdzanie planu przed rozpoczęciem wyszukiwania. |

### Python

```
agent_config = {
    "type": "deep-research",
    "thinking_summaries": "auto",
    "visualization": "auto",
    "collaborative_planning": False,
}

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the competitive landscape of cloud GPUs.",
    agent_config=agent_config,
    background=True,
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: 'deep-research-preview-04-2026',
    input: 'Research the competitive landscape of cloud GPUs.',
    agent_config: {
        type: 'deep-research',
        thinking_summaries: 'auto',
        visualization: 'auto',
        collaborative_planning: false,
    },
    background: true,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the competitive landscape of cloud GPUs.",
    "agent": "deep-research-preview-04-2026",
    "agent_config": {
        "type": "deep-research",
        "thinking_summaries": "auto",
        "visualization": "auto",
        "collaborative_planning": false
    },
    "background": true
}'
```

## Dostępność i ceny

Do agenta Deep Research w Gemini możesz uzyskać dostęp za pomocą interfejsu Interactions API w Google AI Studio i Gemini API.

Ceny są oparte na [modelu płatności za wykorzystanie](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents), który zależy od podstawowych modeli Gemini i narzędzi używanych przez agenta. W odróżnieniu od standardowych żądań czatu, w których przypadku żądanie prowadzi do jednego wyniku, zadanie Deep Research to proces oparty na działaniach agenta. Pojedyncze żądanie wywołuje autonomiczne zapętlenie planowania, wyszukiwania, czytania i wnioskowania.

### Szacunkowy koszt

Koszty zależą od głębokości wymaganych badań. Agent samodzielnie określa, ile czytania i wyszukiwania jest potrzebne, aby odpowiedzieć na Twój prompt.

- **Deep Research** (`deep-research-preview-04-2026`): w przypadku typowego zapytania wymagającego umiarkowanej analizy agent może użyć około 80 zapytań, około 250 tys. tokenów wejściowych (ok. 50–70% z nich może być w pamięci podręcznej) i około 60 tys. tokenów wyjściowych.
  - **Szacunkowa suma:** od 1,00 PLN do 3,00 PLN za zadanie
- **Deep Research Max** (`deep-research-max-preview-04-2026`): w przypadku dogłębnej analizy konkurencji lub szczegółowego badania due diligence agent może użyć do ok. 160 zapytań, ok. 900 tys. tokenów wejściowych (ok. 50–70% – z pamięci podręcznej) i ok. 80 tys. tokenów wyjściowych.
  - **Szacunkowa suma:** od 3 do 7 PLN za zadanie

## kwestie bezpieczeństwa;

Przyznanie agentowi dostępu do internetu i plików prywatnych wymaga starannego rozważenia zagrożeń związanych z bezpieczeństwem.

- **Wstrzykiwanie promptów za pomocą plików:** agent odczytuje zawartość podanych przez Ciebie plików. Upewnij się, że przesłane dokumenty (pliki PDF, pliki tekstowe) pochodzą z zaufanych źródeł. Złośliwy plik może zawierać ukryty tekst, który ma na celu manipulowanie danymi wyjściowymi agenta.
- **Ryzyko związane z treściami w internecie:** agent przeszukuje publiczny internet. Stosujemy co prawda zaawansowane filtry bezpieczeństwa, ale istnieje ryzyko, że agent natrafi na złośliwe strony internetowe i je przetworzy. Zalecamy sprawdzenie `citations` podanych w odpowiedzi, aby zweryfikować źródła.
- **Eksfiltracja:** zachowaj ostrożność, prosząc agenta o podsumowanie poufnych danych wewnętrznych, jeśli zezwalasz mu też na przeglądanie internetu.

## Sprawdzone metody

- **Pytaj o nieznane:** podaj agentowi instrukcje dotyczące postępowania w przypadku brakujących danych.
  Na przykład dodaj do promptu *„Jeśli konkretne dane za 2025 r. nie są dostępne, wyraźnie zaznacz, że są to prognozy lub że są niedostępne, zamiast je szacować”*.
- **Podaj kontekst:** ugruntuj wiedzę agenta, podając informacje lub ograniczenia bezpośrednio w prompcie wejściowym.
- **Korzystaj z planowania zespołowego:** w przypadku złożonych zapytań włącz planowanie zespołowe, aby przed wykonaniem zadania przejrzeć i dopracować plan badań.
- **Wprowadzanie danych w różnych formatach:** agent Deep Research obsługuje wprowadzanie danych w różnych formatach.
  Używaj go ostrożnie, ponieważ zwiększa koszty i ryzyko przepełnienia okna kontekstu.

## Ograniczenia

- **Niestandardowe narzędzia:** obecnie nie możesz udostępniać niestandardowych narzędzi do wywoływania funkcji, ale możesz używać zdalnych serwerów MCP (Model Context Protocol) z agentem Deep Research.
- **Uporządkowane dane wyjściowe:** agent Deep Research nie obsługuje obecnie uporządkowanych danych wyjściowych.
- **Maksymalny czas wyszukiwania:** agent Deep Research ma maksymalny czas wyszukiwania wynoszący 60 minut. Większość zadań powinna zostać ukończona w ciągu 20 minut.
- **Wymagania dotyczące sklepu:** uruchomienie agenta za pomocą `background=True` wymaga
  `store=True`.
- **Wyszukiwarka Google:** [wyszukiwarka Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) jest domyślnie włączona, a do wyników opartych na wiedzy stosowane są [określone ograniczenia](https://ai.google.dev/gemini-api/terms?hl=pl#use-restrictions2).

## Co dalej?

- Dowiedz się więcej o [interfejsie Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).
- Dowiedz się, jak korzystać z własnych danych za pomocą narzędzia [Wyszukiwanie plików](https://ai.google.dev/gemini-api/docs/file-search?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-14 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-14 UTC."],[],[]]
