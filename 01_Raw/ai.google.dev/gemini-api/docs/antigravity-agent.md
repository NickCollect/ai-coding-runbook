---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl
fetched_at: 2026-06-08T05:39:28.628420+00:00
title: "Agent Antigravity \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Agent Antigravity

Agent Antigravity to zarządzany agent do zwykłych obciążeń w interfejsie Gemini API. Pojedyncze wywołanie interfejsu API zapewnia dostęp do agenta, który rozumuje, wykonuje kod, zarządza plikami i przegląda internet w bezpiecznym środowisku Linux Sandbox hostowanym przez Google.

Jest oparty na modelu Gemini 3.5 Flash i korzysta z tego samego środowiska co Antigravity IDE. Dostępne w ramach [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) i [Google AI Studio](https://aistudio.google.com?hl=pl).

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## Uprawnienia

Każde wywołanie może udostępnić piaskownicę systemu Linux i rozpocząć pętlę używania narzędzi. Agent planuje, działa, obserwuje wyniki i powtarza te czynności, aż zadanie zostanie wykonane.

- **Wykonywanie kodu:** uruchamiaj polecenia Bash, Python i Node.js. instalować pakiety, przeprowadzać testy i tworzyć aplikacje.
- **Zarządzanie plikami:** odczytywanie, zapisywanie, edytowanie, wyszukiwanie i wyświetlanie listy plików w piaskownicy. Pliki są zachowywane podczas interakcji.
- **Dostęp do internetu:** wyszukiwanie w Google i pobieranie adresów URL w celu uzyskania danych.
- **Kompaktowanie kontekstu:** automatyczne kompaktowanie kontekstu (wyzwalane przy około 135 tys. tokenów) w celu obsługi długotrwałych sesji wieloetapowych bez utraty kontekstu i przekraczania limitów tokenów.

Więcej informacji o korzystaniu z wielu tur i transmitowaniu znajdziesz w [krótkim wprowadzeniu](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl).

## Obsługiwane narzędzia

Domyślnie agent ma dostęp do `code_execution`, `google_search` i `url_context`. Narzędzia systemu plików są włączane automatycznie, gdy określisz parametr `environment`. Parametr `tools` musisz podać tylko wtedy, gdy dostosowujesz lub ograniczasz domyślny zestaw.

| Narzędzie | Wpisz wartość | Opis |
| --- | --- | --- |
| Wykonanie kodu | `code_execution` | Uruchamiaj polecenia powłoki (bash, Python, Node) z przechwytywaniem stdout/stderr. |
| Wyszukiwarka Google | `google_search` | wyszukiwać w sieci publicznej, |
| Kontekst adresu URL | `url_context` | pobierać i odczytywać strony internetowe, |
| System plików | *(włączone za pomocą `environment`)* | odczytywać, zapisywać, edytować, wyszukiwać i wyświetlać listę plików w piaskownicy; Nie ma oddzielnego typu narzędzia. Jest włączany automatycznie, gdy ustawiona jest opcja `environment`. |

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
-H "Api-Revision: 2026-05-20" \
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
-H "Api-Revision: 2026-05-20" \
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

## Dostosowywanie agenta

Możesz rozszerzyć możliwości agenta Antigravity, dostosowując jego instrukcje, narzędzia i środowisko. Agent obsługuje natywne dla systemu plików podejście do dostosowywania: możesz zamontować pliki, takie jak `AGENTS.md`, zawierające instrukcje i umiejętności w `.agents/skills/` bezpośrednio w piaskownicy lub przekazać konfigurację w linii w momencie interakcji. Możesz iteracyjnie zmieniać konfigurację w tekście, a potem zapisać ją jako agenta zarządzanego, gdy będzie gotowa.

Szczegółowe informacje o tworzeniu niestandardowych agentów znajdziesz w artykule [Building Managed Agents](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl) (Tworzenie zarządzanych agentów).

## Środowiska

Każde wywołanie tworzy lub ponownie wykorzystuje piaskownicę systemu Linux. Parametr `environment` może przyjmować 3 formy:

| Formularz | Opis |
| --- | --- |
| `"remote"` | Utwórz nową piaskownicę z ustawieniami domyślnymi. |
| `"env_abc123"` | Użyj ponownie istniejącego środowiska według identyfikatora, zachowując wszystkie pliki i stan. |
| `{...}` | Pełna `EnvironmentConfig` z niestandardowymi źródłami i regułami sieciowymi. |

Szczegółowe informacje o źródłach (Git, GCS, wbudowane), sieciach, cyklu życia i limitach zasobów znajdziesz w sekcji [Środowiska](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl).

## Dostępność i ceny

Agent Antigravity jest dostępny w wersji podglądowej w ramach [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl) w Google AI Studio i Gemini API.

Ceny są oparte na [modelu płatności według wykorzystania](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#pricing-for-agents), który zależy od tokenów bazowego modelu Gemini i narzędzi używanych przez agenta. W przeciwieństwie do standardowego żądania czatu, które generuje pojedynczy wynik, interakcja Antigravity to przepływ pracy oparty na agentach. Pojedyncze żądanie wywołuje autonomiczne pętle rozumowania, wykonywania narzędzi, uruchamiania kodu i zarządzania plikami.

### Szacunkowy koszt

Koszty zależą od złożoności zadania. Pracownik obsługi klienta samodzielnie określa, ile wywołań narzędzi, wykonań kodu i operacji na plikach jest potrzebnych. Poniższe szacunki są oparte na przebiegach.

| Kategoria zadania | Tokeny wejściowe | Tokeny wyjściowe | Typowy koszt |
| --- | --- | --- | --- |
| **Badania i synteza informacji** | 100 tys.–500 tys. | 10–40 tys. | 0,30–1,00 USD |
| **Generowanie dokumentów i treści** | 100 tys.–500 tys. | 15–50 tys. | 0,30–1,30 PLN |
| **Projektowanie procesów i systemów** | 100–400 tys. | 10–30 tys. | 0,25–0,80 USD |
| **Przetwarzanie i analiza danych** | 300 tys.–3 mln | 30 tys.–150 tys. | 0,70–3,25 PLN |

Zwykle w pamięci podręcznej jest przechowywanych 50–70% tokenów wejściowych. Złożone przepływy pracy agenta z wieloma wywołaniami narzędzi mogą w ramach jednej interakcji zgromadzić 3–5 mln tokenów, co wiąże się z kosztem do 5 USD.

**Obliczenia środowiskowe** (procesor, pamięć, wykonywanie w piaskownicy) **nie są rozliczane** w okresie wersji testowej.

## Ograniczenia

- **Stan wersji testowej:** agent Antigravity i interfejs Interactions API są dostępne w wersji testowej. Funkcje i schematy mogą ulec zmianie.
- **Nieobsługiwana konfiguracja generowania:** te parametry nie są obsługiwane i zwracają błąd 400: `temperature`, `top_p`, `top_k`, `stop_sequences`, `max_output_tokens`.
- **Uporządkowane dane wyjściowe:** agent Antigravity nie obsługuje uporządkowanych danych wyjściowych.
- **Niedostępne narzędzia:** `file_search`, `computer_use`, `google_maps`, `function_calling` i `mcp` nie są jeszcze obsługiwane.
- **Narzędzie systemu plików:** obecnie nie ma narzędzia systemu plików. Jest ona częścią `environment`.
- **Informacje:** agent nie obsługuje `background=True` i wymaga `store=True`.
- **Nieobsługiwane typy multimodalne.** Dane wejściowe w postaci audio, wideo i dokumentów nie są obecnie obsługiwane. Dozwolone są tylko tekst i obraz.

## Co dalej?

- [Szybki start:](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=pl) rozmowy wieloetapowe i streaming.
- [Tworzenie agentów niestandardowych:](https://ai.google.dev/gemini-api/docs/custom-agents?hl=pl) instrukcje niestandardowe, umiejętności i zapisywanie agentów.
- [Środowiska:](https://ai.google.dev/gemini-api/docs/agent-environment?hl=pl) konfiguracja piaskownicy, źródła, sieć.
- [Agent Deep Research:](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=pl) zadania badawcze o dłuższej formie.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl): bazowy interfejs API.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-05-20 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-05-20 UTC."],[],[]]
