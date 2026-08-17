---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl
fetched_at: 2026-08-17T02:16:34.846115+00:00
title: "Szybki start z zarz\u0105dzanymi agentami \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Szybki start z zarządzanymi agentami

Ten przewodnik zawiera informacje o tworzeniu i używaniu agentów zarządzanych w interfejsie Gemini API na przykładzie agenta [Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=pl). Wykonasz pierwsze wywołanie agenta, poprowadzisz wieloetapową rozmowę, będziesz stopniowo wyświetlać odpowiedź, pobierać pliki z piaskownicy i pracować z agentem zarządzanym Antigravity.

## Uruchamianie pierwszej interakcji z agentem

Pojedyncze wywołanie interfejsu [Interactions API](https://ai.google.dev/gemini-api/docs?hl=pl) powoduje udostępnienie piaskownicy Linux, uruchomienie pętli agenta i zwrócenie wyniku. Określisz 3 parametry:

- Przekaż `agent` jako `"antigravity-preview-05-2026",`, czyli aktualną wersję naszego predefiniowanego agenta zarządzanego ogólnego przeznaczenia.
- Określ `environment="remote"`, aby udostępnić nowe środowisko piaskownicy.
- Utwórz dane wejściowe, określając, co ma robić agent.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Odpowiedź zwraca obiekt `Interaction`. Zapisz `interaction.id` i `interaction.environment_id`, aby kontynuować rozmowę w tej samej piaskownicy. Użyj `interaction.output_text`, aby uzyskać dostęp do ostatecznej odpowiedzi agenta. `interaction.steps` zawiera listę wszystkich kroków wykonanych przez agenta (rozumowanie, wywołania narzędzi, wykonanie kodu).

## Kontynuowanie rozmowy (wieloetapowej)

Interfejs API śledzi 2 niezależne wymiary stanu:

- **Kontekst rozmowy:** historia czatu, ślad uzasadnienia, użycie narzędzia, użycie `previous_interaction_id`.
- [**Stan środowiska:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl) pliki, zainstalowane pakiety i stan piaskownicy, użycie `environment`.

Aby wznowić, przekaż oba w odpowiednim miejscu:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Pliki z etapu 1 (`fibonacci.txt`) są zachowywane na etapie 2. Agent zachowuje też kontekst rozmowy.

Możesz je łączyć i dopasowywać niezależnie:

- **Wyczyść rozmowę, zachowaj pliki:** pomiń `previous_interaction_id`, przekaż tylko identyfikator środowiska za pomocą `environment`, aby rozpocząć nową rozmowę w tym samym obszarze roboczym.
- **Zachowaj rozmowę, nowy obszar roboczy:** przekaż `previous_interaction_id`, ustaw `environment="remote"` dla nowej piaskownicy.

### Automatyczne kompresowanie kontekstu

W długotrwałych rozmowach wieloetapowych surowa historia kroków rozumowania, wywołań narzędzi i zawartości dużych plików może szybko się rozrastać i zajmować znaczną przestrzeń kontekstu. Aby zapobiec błędom związanym z przekroczeniem limitu tokenów i utrzymać koncentrację agenta (zapobiegając „utracie kontekstu”), interfejs API zarządzanych agentów zawiera natywny krok kompresowania kontekstu przy około 135 tys. tokenów. Dzieje się to automatycznie.

## Stopniowe wyświetlanie odpowiedzi

W przypadku długotrwałych zadań możesz stopniowo wyświetlać odpowiedź, aby zobaczyć, jak agent pracuje w czasie rzeczywistym:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
    if event.event_type == "step.stop" and event.usage:
        print(event.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
    if (event.event_type === "step.stop" && event.usage) {
        console.log(event.usage);
    }
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Stopniowe wyświetlanie zwraca delty kroków z przyrostowymi aktualizacjami. Po zakończeniu kroku zdarzenie `step.stop` zawiera skumulowane statystyki wykorzystania. Więcej informacji znajdziesz w
[przewodniku po stopniowym wyświetlaniu](https://ai.google.dev/gemini-api/docs/streaming?hl=pl).

## Pobieranie plików ze środowiska

Gdy agent tworzy pliki w piaskownicy. Pobierz je za pomocą interfejsu Files API za pomocą bezpośredniego żądania HTTP (nie ma jeszcze metody pakietu SDK):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

tar -xf snapshot.tar -C extracted_snapshot
```

## Zapisywanie agenta zarządzanego

W poprzednich krokach użyliśmy domyślnego agenta Antigravity i dostosowaliśmy go w tekście. Gdy skończysz iterować konfigurację (instrukcje, umiejętności, wybór modelu i środowisko), możesz zapisać ją jako agenta zarządzanego, którego można używać wielokrotnie. Dzięki temu możesz wywoływać go za pomocą identyfikatora bez powtarzania konfiguracji.

Gdy zapisujesz agenta, zauważysz symetrię architektury z interakcjami w tekście: określasz `base_agent: "antigravity-preview-05-2026"` i możesz przekazać `agent_config` z wybranym `model`, tak jak w przypadku `interactions.create`. Określasz też `base_environment` (z źródeł lub przez rozwidlenie istniejącego środowiska). Agent będzie używać tej konfiguracji środowiska i modelu w każdej nowej interakcji.

**Ze źródeł:** zdefiniuj źródła w tekście lub z innych źródeł, takich jak GitHub czy Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.6-flash",
    },
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-05-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.6-flash",
    },
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.6-flash"
    },
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Wywoływanie agenta zarządzanego

Po zapisaniu agenta zarządzanego możesz go wywołać za pomocą identyfikatora. Każde wywołanie rozwidla środowisko podstawowe, więc każde uruchomienie zaczyna się od nowa:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Co dalej?

- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl): możliwości, obsługiwane narzędzia, multimodalne wprowadzanie danych, ceny i ograniczenia.
- [Tworzenie zarządzanych agentów](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl): rozszerzanie Antigravity o własne instrukcje, umiejętności i dane.
- [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl): źródła, sieci, cykl życia, limity zasobów.
- [Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl): podstawowy interfejs API dla modeli i agentów.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
