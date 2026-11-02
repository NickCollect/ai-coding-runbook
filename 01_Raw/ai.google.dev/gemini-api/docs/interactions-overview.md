---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl
fetched_at: 2026-11-02T07:16:25.001252+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interactions API

Interfejs Interactions API to najlepszy sposób na tworzenie aplikacji z wykorzystaniem modeli Gemini i agentów. Od czerwca 2026 r. jest on ogólnie dostępny i zalecany w przypadku wszystkich nowych projektów. Pierwotny interfejs
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pl) API
jest nadal w pełni obsługiwany, choć jest już uważany za starszy.

## Dlaczego warto korzystać z interfejsu Interactions API?

- **Uniwersalny interfejs dla wszystkich aplikacji**: zaprojektowany jako standardowy interfejs dla każdego przypadku użycia, w tym generowania tekstu w jednej turze, rozpoznawania multimodalnego, uporządkowanych danych wyjściowych, orkiestracji narzędzi i Agentic Workflows.
- **Pojedynczy interfejs API dla modeli i agentów**: jeden ujednolicony punkt końcowy i wzorzec do
  bezpośredniego wywoływania standardowych modeli Gemini oraz wyspecjalizowanych agentów (takich
  jak Deep Research i niestandardowi agenci zarządzani).
- **Nowe funkcje od razu po wyjęciu z pudełka**: funkcje takie jak opcjonalny stan rozmowy po stronie serwera za pomocą parametru `previous_interaction_id`, widoczne kroki wykonania do debugowania i renderowania interfejsu oraz [wykonywanie w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) długotrwałych zadań za pomocą parametru `background=true`.
- **Niższe koszty dzięki wyższym współczynnikom trafień w pamięci podręcznej**: w przypadku rozmów wieloetapowych
  opcjonalne zarządzanie stanem po stronie serwera umożliwia wydajniejsze
  buforowanie kontekstu między turami, co zmniejsza koszty tokenów.
- **Miejsce, w którym pojawiają się nowe funkcje**: w przyszłości wszystkie nowe modele, funkcje multimodalne
  , narzędzia i funkcje agenta będą dostępne w interfejsie Interactions
  API.

Domyślnie interfejs Interactions API przechowuje żądania, dzięki czemu możesz korzystać z funkcji zarządzania stanem po stronie serwera za pomocą parametru `previous_interaction_id`. Możesz włączyć zachowanie bezstanowe, ustawiając parametr `store=false`. Szczegółowe informacje znajdziesz w sekcji [Przechowywanie danych](#data-storage-retention).

## Rozpocznij

- **Skonfiguruj agenta kodowania**: połącz się z **Gemini Docs MCP** i zainstaluj
  umiejętność `gemini-api-dev`, aby zapewnić asystentowi bezpośredni dostęp do
  najnowszych dokumentów dla programistów i sprawdzonych metod. Szczegółowe instrukcje znajdziesz w przewodniku
  [Konfigurowanie agenta kodowania](https://ai.google.dev/gemini-api/docs/coding-agents?hl=pl).
- **Migracja z `generateContent`**: jeśli masz już integrację,
  postępuj zgodnie z instrukcjami w [przewodniku po migracji](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=pl), aby
  przejść na interfejs Interactions API.
- **Pierwsze kroki**: postępuj zgodnie z instrukcjami w przewodniku [Pierwsze kroki z interfejsem Interactions API
  guide](https://ai.google.dev/gemini-api/docs/get-started?hl=pl).

### Przewodniki po funkcjach

Z tych przewodników dowiesz się więcej o konkretnych możliwościach interfejsu Interactions API. Na tych stronach możesz użyć przełącznika, aby przełączać się między interfejsami generateContent i Interactions API:

- [Generowanie tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl)
- [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl)
- [Rozumienie obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl)
- [Rozumienie dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl)
- [Rozumienie filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl)
- [Przetwarzanie dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl)
- [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
- [Uporządkowane dane wyjściowe](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl)
- [Agent Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl)
- [Wnioskowanie Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl)
- [Wnioskowanie priorytetowe](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl)

## Jak działa interfejs Interactions API

Interfejs Interactions API opiera się na podstawowym zasobie: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Interaction). `Interaction` reprezentuje pełną turę w rozmowie lub zadaniu. Działa jako rekord sesji, który zawiera całą historię interakcji jako chronologiczną sekwencję **kroków wykonania**. Te kroki obejmują myśli modelu, wywołania narzędzi po stronie serwera lub klienta i wyniki (np. `function_call` i `function_result`) oraz końcowe `model_output`. Przechowywany zasób (pobierany za pomocą `interactions.get`) zawiera też kroki `user_input` dla pełnego kontekstu, chociaż odpowiedź `interactions.create` zwraca tylko kroki wygenerowane przez model.

Gdy wywołujesz
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=pl#CreateInteraction), tworzysz nowy `Interaction` zasób:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### Zarządzanie stanem po stronie serwera

Aby kontynuować rozmowę, możesz użyć parametru
`previous_interaction_id` w kolejnym wywołaniu, podając `id` zakończonej interakcji. Serwer używa tego identyfikatora do pobierania historii rozmowy, dzięki czemu nie musisz ponownie wysyłać całej historii czatu:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

Parametr `previous_interaction_id` zachowuje tylko historię rozmowy (dane wejściowe i wyjściowe) za pomocą parametru `previous_interaction_id`. Pozostałe parametry są **zakresem interakcji** i mają zastosowanie tylko do konkretnej interakcji, którą obecnie generujesz:

- `tools`
- `system_instruction`
- `generation_config` (w tym `thinking_level`, `temperature` itp.)

Oznacza to, że jeśli chcesz, aby te parametry były stosowane, musisz je ponownie określić w każdej nowej interakcji. Zarządzanie stanem po stronie serwera jest opcjonalne. Możesz też działać w trybie bezstanowym, wysyłając pełną historię rozmowy w każdym żądaniu.

### Przechowywanie danych

Domyślnie interfejs API przechowuje wszystkie obiekty Interaction (`store=true`), aby
uprościć korzystanie z funkcji zarządzania stanem po stronie serwera (za pomocą
`previous_interaction_id`), [wykonywania w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) (za pomocą `background=true`) i
obserwacji.

- **Płatny poziom**: system przechowuje interakcje przez **55 dni**.
- **Poziom bezpłatny**: system przechowuje interakcje przez **1 dzień**.

Jeśli nie chcesz tego robić, możesz ustawić parametr `store=false` w żądaniu. To ustawienie jest niezależne od zarządzania stanem. Możesz zrezygnować z przechowywania dowolnej interakcji. Pamiętaj jednak, że
`store=false` jest niezgodny z [wykonywaniem w tle](https://ai.google.dev/gemini-api/docs/background-execution?hl=pl) i uniemożliwia używanie
`previous_interaction_id` w kolejnych turach.

W przypadku projektów na płatnym poziomie możesz skonfigurować okres przechowywania w
[AI Studio](https://aistudio.google.com/logs?hl=pl), aby automatycznie oznaczać logi do
usunięcia z pamięci projektu po 7, 14, 28 lub 55 dniach. Krótszy okres przechowywania może wpłynąć na pobieranie wcześniejszych rozmów.

Przechowywane interakcje możesz w każdej chwili usunąć programowo za pomocą metody
[`delete`](https://ai.google.dev/api/interactions-api?hl=pl#deleteInteraction),
która wymaga identyfikatora interakcji. W AI Studio możesz też wyświetlać logi przechowywanych
interakcji i nimi zarządzać, w tym usuwać je z pamięci projektu, w
[AI Studio](https://aistudio.google.com/logs?hl=pl).

Po upływie okresu przechowywania Twoje dane zostaną automatycznie usunięte.

Obiekty Interactions są przetwarzane zgodnie z [warunkami](https://ai.google.dev/gemini-api/terms?hl=pl).

### Wyświetlanie interakcji w AI Studio

Interfejs API przechowuje żądania Interactions API wykonane z parametrem `store=true` w przypadku projektów na płatnym poziomie. Możesz je wyświetlić bezpośrednio na stronie
[Logi w Google AI Studio](https://aistudio.google.com/logs?hl=pl). Więcej informacji znajdziesz w przewodniku
[Logi](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=pl).

## Sprawdzone metody

- **Współczynnik trafień w pamięci podręcznej**: buforowanie niejawne jest obsługiwane w trybie stanowym i
  bezstanowym (patrz
  [Szybki start](https://ai.google.dev/gemini-api/docs/get-started?hl=pl#4_multi-turn_conversations)). Używanie parametru `previous_interaction_id` (stanowego) do kontynuowania rozmów umożliwia systemowi łatwiejsze korzystanie z buforowania niejawnego w przypadku historii rozmów, co zwiększa wydajność i obniża koszty.
- **Mieszanie interakcji**: możesz dowolnie łączyć interakcje agenta i
  modelu w ramach rozmowy. Na przykład do wstępnego zbierania danych możesz użyć wyspecjalizowanego agenta, takiego jak agent Deep Research, a następnie użyć standardowego modelu Gemini do wykonywania kolejnych zadań, takich jak podsumowywanie lub formatowanie, łącząc te kroki za pomocą parametru `previous_interaction_id`.

## Obsługiwane modele i agenci

| Nazwa modelu | Typ | Identyfikator modelu |
| --- | --- | --- |
| Gemini 4 Argon | Model | `gemini-4-argon` |
| Gemini 3.8 Flash | Model | `gemini-3.8-flash` |
| Gemini 3.6 Flash | Model | `gemini-3.6-flash` |
| Gemini 3.1 Pro (wersja testowa) | Model | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | Model | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | Model | `gemini-3.1-flash-lite` |
| Gemini 3 Flash (wersja testowa) | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Gemini 3 Pro Image | Model | `gemini-3-pro-image` |
| Gemini 3.1 Flash Image | Model | `gemini-3.1-flash-image` |
| Gemini 3.1 Flash TTS (wersja testowa) | Model | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | Model | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | Model | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | Model | `lyria-3.5` |
| Lyria 3 Clip (wersja testowa) | Model | `lyria-3-clip-preview` |
| Lyria 3 Pro (wersja testowa) | Model | `lyria-3-pro-preview` |
| Deep Research (wersja testowa) | Agent | `deep-research-preview-04-2026` |
| Deep Research (wersja testowa) | Agent | `deep-research-max-preview-04-2026` |
| Antigravity (wersja testowa) | Agent | `antigravity-preview-09-2026` |

## Pakiety SDK

Aby uzyskać dostęp do interfejsu Interactions API, możesz użyć najnowszej wersji pakietów SDK Google GenAI.

- W Pythonie jest to pakiet `google-genai` w wersji `2.3.0` lub nowszej.
- W JavaScript jest to pakiet `@google/genai` w wersji `2.3.0` lub nowszej.
- W Go jest to pakiet `google.golang.org/genai`.
- W Javie jest to pakiet `com.google.genai:google-genai`.

Więcej informacji o instalowaniu pakietów SDK znajdziesz na stronie
[Biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

## Ograniczenia

- **Zdalny MCP**: Gemini 3 nie obsługuje zdalnego MCP. Ta funkcja będzie dostępna już wkrótce.
- **Zgodność modelu wieloetapowego**: jeśli w
  rozmowie (stanowej lub bezstanowej) używasz różnych modeli, kolejne modele muszą obsługiwać
  dane wyjściowe poprzednich modeli jako dane wejściowe. Jeśli np. wygenerujesz obraz za pomocą modelu `gemini-3.1-flash-image`, nie możesz kontynuować tej rozmowy z modelem, który nie akceptuje danych wejściowych w postaci obrazu (np. z modelem obsługującym tylko tekst lub modelem generującym muzykę, takim jak Lyria).

Te funkcje są obsługiwane przez interfejs
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=pl) API, ale **nie są jeszcze
dostępne** w interfejsie Interactions API:

- **[Interfejs Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=pl)**
- **[Automatyczne wywoływanie funkcji (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=pl#automatic_function_calling_python_only)**
- **[Buforowanie jawne](https://ai.google.dev/gemini-api/docs/caching?hl=pl)**: pamiętaj, że w interfejsie Interactions API jest dostępne buforowanie niejawne po stronie serwera
  za pomocą parametru `previous_interaction_id`.

## Prześlij opinię

Twoja opinia jest kluczowa dla rozwoju interfejsu Interactions API.
Podziel się swoimi przemyśleniami, zgłoś błędy lub poproś o funkcje na naszym
[forum społeczności programistów AI od Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=pl).

## Co dalej?

- Wypróbuj [notatnik z szybkim wprowadzeniem do interfejsu Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=pl).
- Dowiedz się więcej o agencie Deep Research w [Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-15 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-15 UTC."],[],[]]
