---
source_url: https://ai.google.dev/gemini-api/docs/latest-model?hl=pl
fetched_at: 2026-09-21T05:50:21.057657+00:00
title: "Nowo\u015bci w\u00a0Gemini\u00a03.8 Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Nowości w Gemini 3.8 Flash

[Zobacz wszystkie modele](https://ai.google.dev/gemini-api/docs/models?hl=pl)

Model Gemini 3.8 Flash (`gemini-3.8-flash`) jest ogólnie dostępny i gotowy do użycia w środowisku produkcyjnym. To nasz najbardziej inteligentny model Flash, zaprojektowany z myślą o długoterminowym inżynierii oprogramowania, autonomicznych agentach i złożonych przepływach pracy w przedsiębiorstwach.

Z tego przewodnika dowiesz się, co nowego w modelu Gemini 3.8 Flash, jakie zmiany wprowadziliśmy w interfejsie API, zobaczysz przykłady kodu i uzyskasz wskazówki dotyczące migracji.

## Nowy model

| Model | Identyfikator modelu | Domyślny poziom rozumowania | Ceny | Opis |
| --- | --- | --- | --- | --- |
| Gemini 3.8 Flash | `gemini-3.8-flash` | `medium` | Model 3.8 Flash jest dostępny do końca roku w cenie początkowej 0,75 USD za 1 mln tokenów wejściowych i 3,75 USD za 1 mln tokenów wyjściowych. Więcej informacji znajdziesz w [cenniku](https://ai.google.dev/gemini-api/docs/pricing?hl=pl). | Nasz najbardziej inteligentny model Flash, zaprojektowany z myślą o długoterminowym inżynierii oprogramowania, autonomicznych agentach i złożonych przepływach pracy w przedsiębiorstwach. |

Model Gemini 3.8 Flash obsługuje okno kontekstu o rozmiarze 1 mln tokenów, maksymalnie 64 tys. tokenów wyjściowych, dostrajane poziomy rozumowania (`low`, `medium`, `high`) oraz ten sam kompleksowy zestaw wbudowanych narzędzi.

Pełne specyfikacje znajdziesz na stronie modelu [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pl). Szczegóły dotyczące cen promocyjnych znajdziesz w [sekcji Ceny](#pricing) poniżej lub na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-3.8-flash).

## Krótkie wprowadzenie

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a three.js script that renders a realistic 3D black hole."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a three.js script that renders a realistic 3D black hole.",
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
        .input(
            InteractionsInput.of(
                "Write a three.js script that renders a realistic 3D black hole."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a three.js script that renders a realistic 3D black hole."
  }'
```

## Co nowego w modelu Gemini 3.8 Flash

- **Długoterminowa inżynieria oprogramowania:** zapewnia dobre wyniki w rzeczywistych testach porównawczych kodowania, złożonym refaktoryzacji wielu plików i deterministycznym wykonywaniu narzędzi. Szczegółowe informacje znajdziesz w [metodologii oceny](https://deepmind.google/models/evals-methodology/gemini-3-8-flash/?hl=pl).
- **Agenci autonomiczni:** umożliwiają tworzenie odpornych przepływów pracy związanych z planowaniem wieloetapowym i zarządzaniem narzędziami, co znacznie zmniejsza liczbę nieudanych pętli i błędów.
- **Złożone przepływy pracy w przedsiębiorstwach:** zapewniają większą dokładność, głębokie rozumowanie i wysoką rzetelność faktów w wymagających zadaniach domenowych i potokach danych na dużą skalę.
- **Domyślny model dla agentów zarządzanych:** domyślny agent dla agentów zarządzanych – [agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl) – korzysta teraz z modelu Gemini 3.8 Flash. Pakiet [Antigravity SDK](https://antigravity.google/docs/sdk/overview/?hl=pl) domyślnie korzysta też z modelu Gemini 3.8 Flash.
- **Ceny promocyjne:** model Gemini 3.8 Flash jest dostępny w cenie promocyjnej 0,75 USD za 1 mln tokenów wejściowych i 3,75 USD za 1 mln tokenów wyjściowych do 31 grudnia 2026 r. Standardowe ceny w wysokości 1,50 USD za 1 mln tokenów wejściowych i 7,50 USD za 1 mln tokenów wyjściowych zaczną obowiązywać 1 stycznia 2027 r.

Model Gemini 3.8 Flash może z założenia używać więcej tokenów w przypadku dłuższych i bardziej złożonych zadań. Aby zapewnić lepsze wyniki w przypadku trudnych, wieloetapowych celów, model wykonuje mniejsze kroki rozumowania, iteracyjnie wywołuje narzędzia i weryfikuje swoją pracę. Nie każdy przepływ pracy wymaga takiego poziomu weryfikacji. W przypadku codziennych zadań możesz zmniejszyć wysiłek związany z [rozumowaniem](#understanding-reasoning-levels), aby ograniczyć zużycie tokenów. Model Gemini 3.7 Flash jest nadal w pełni obsługiwany.

## Poziomy rozumowania

Model Gemini 3.8 Flash umożliwia elastyczne kontrolowanie opóźnienia i inteligencji poprzez dostosowanie poziomu rozumowania modelu:

- **Niski nakład pracy związany z myśleniem**: skraca czas odpowiedzi w przypadku zadań krytycznych pod względem opóźnienia, takich jak potoki reagowania na incydenty, czat w czasie rzeczywistym, pisanie wersji roboczych i szybka analiza danych.
- **Średni (domyślny):** najlepsza jakość w przypadku większości zadań. Zalecany w przypadku złożonego kodu i zastosowań agentowych, zapewniający większą dokładność przy pierwszym przejściu.
- **Nakład pracy związany z myśleniem**: maksymalizuje możliwości rozumowania i zarządzania narzędziami modelu. Najlepszy do głębokiego rozumowania, matematyki i trudnych zadań wieloetapowych.

W tym przykładzie ustawiamy `thinking_level` na `medium` w przypadku złożonego żądania analizy kodu:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    generation_config={
        "thinking_level": "medium"  # Balanced reasoning effort for complex tasks
    }
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
  generation_config: {
    thinking_level: "medium"
  }
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely."))
        .generationConfig(
            GenerationConfig.builder()
                .thinkingLevel(ThinkingLevel.MEDIUM) // Balanced reasoning effort for complex tasks
                .build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Analyze this payment processing pipeline for race conditions during retry attempts and rewrite the transaction locks safely.",
    "generation_config": {
      "thinking_level": "medium"
    }
  }'
```

## Zaktualizowany agent Antigravity

Dzięki lepszej wydajności i rozumowaniu agent [Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl) w Gemini Managed Agents jest teraz domyślnie tworzony za pomocą modelu Gemini 3.8 Flash.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=(
        "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
        "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
        "Check search indexing with Google Search for site:web.dev. "
        "Format the output as a side-by-side scorecard table with prioritized fixes."
    ),
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
  environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent(AgentOption.of("antigravity-preview-09-2026"))
        .input(
            InteractionsInput.of(
                "Audit https://web.dev for performance, Core Web Vitals, and SEO. "
                    + "Query Google's PageSpeed Insights API for both Mobile and Desktop strategies. "
                    + "Check search indexing with Google Search for site:web.dev. "
                    + "Format the output as a side-by-side scorecard table with prioritized fixes."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Audit https://web.dev for performance, Core Web Vitals, and SEO. Query Google'\''s PageSpeed Insights API for both Mobile and Desktop strategies. Check search indexing with Google Search for site:web.dev. Format the output as a side-by-side scorecard table with prioritized fixes.",
    "environment": "remote"
}'
```

Podstawowy model Gemini [można skonfigurować](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=pl#model-selection) za pomocą `agent_config`.

## Lista kontrolna migracji

```
  `/gemini-api-dev migrate my app to Gemini 3.8 Flash`
```

### Migracja do modelu gemini-3.8-flash

- **Zaktualizuj identyfikator modelu:** zmień ciąg docelowego modelu na `gemini-3.8-flash`.
- **Usuń wycofane parametry próbkowania:**
  - Usuń parametry `temperature`, `top_p` i `top_k` z konfiguracji generowania.
  - Zastąp parametr `thinking_budget` ciągiem wyliczeniowym `thinking_level`. Pamiętaj, że model 3.8 Flash nie obsługuje parametru `minimal`.
  - Usuń parametr `candidate_count` (nieobsługiwany w Gemini 3 i nowszych wersjach).
- **Wymuś reguły weryfikacji tury:**
  - Ujednolicaj rozmowy wieloetapowe na podstawie parametru `previous_interaction_id` po stronie serwera.
  - Usuń wstępnie wypełnione tury modelu.
- **Sprawdź wywoływanie funkcji:**
  - Umieść zasoby multimodalne w ładunku odpowiedzi.
  - Sformatuj instrukcje w tekście za pomocą `\n\n`.
  - Jeśli widzisz błędy `Malformed_Function_Call` związane z tekstem przed narzędziem, zapoznaj się z [obejściami wymagań dotyczących tekstu przed narzędziem](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#workarounds-for-pre-tool-text-requirements).
  - Tylko w przypadku korzystania z interfejsu generateContent API: upewnij się, że wszystkie obiekty `FunctionResponse` zawierają parametry `call_id` i `name`.
- **Podstawowe wymagania Gemini 3:** informacje o aktualizacjach pakietu SDK i zachowaniu sygnatury myśli znajdziesz na [liście kontrolnej migracji do Gemini 3.5](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=pl#migration).

## Ceny

Do 31 grudnia 2026 r. możesz korzystać z cen promocyjnych w Google AI Studio i Gemini Enterprise Agent Platform w przypadku modeli Gemini 3.8 Flash, Gemini 3.7 Flash i Gemini 3.6 Flash. Standardowe ceny zaczną obowiązywać 1 stycznia 2027 r. Pełne progi cenowe znajdziesz na [stronie z cennikiem](https://ai.google.dev/gemini-api/docs/pricing?hl=pl#gemini-3.8-flash).

## Dalsze kroki

- Zapoznaj się ze specyfikacjami interfejsu API w [omówieniu modeli](https://ai.google.dev/gemini-api/docs/models?hl=pl).
- Poznaj zarządzanie wieloma agentami w [omówieniu interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl).
- Testuj i dopracowuj podpowiedzi w [Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
