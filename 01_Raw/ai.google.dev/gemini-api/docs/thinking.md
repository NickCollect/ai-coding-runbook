---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=pl
fetched_at: 2026-09-07T05:40:38.561268+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Gemini

Modele z serii [Gemini 3 i 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pl) korzystają z
„procesu myślenia”, który znacznie poprawia ich zdolność do rozumowania i planowania wieloetapowego,
dzięki czemu są bardzo skuteczne w przypadku złożonych zadań, takich jak
kodowanie, zaawansowana matematyka i analiza danych.

Gdy używasz modelu myślącego, Gemini przeprowadza wewnętrzne rozumowanie przed udzieleniem odpowiedzi. Interfejs API Interactions udostępnia to rozumowanie za pomocą kroków `thought`, czyli specjalnych kroków, które pojawiają się chronologicznie obok wywołań funkcji, danych wejściowych użytkownika lub danych wyjściowych modelu w tablicy `steps`.

Każdy krok myślenia zawiera 2 pola:

| Pole | Wymagane | Opis |
| --- | --- | --- |
| `signature` | ✅ Tak | Zaszyfrowana reprezentacja wewnętrznego stanu rozumowania modelu. Zawsze obecna, nawet gdy model wykonuje minimalne rozumowanie. |
| `summary` | ❌ Nie | Tablica treści (tekstu lub obrazów) podsumowująca rozumowanie. Może być pusta w zależności od konfiguracji [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=pl), tego, czy model przeprowadził wystarczające rozumowanie, lub typu treści (np. obrazy mogą nie mieć podsumowań tekstowych). |

## Z tego powodu podpisy są ograniczone wyłącznie do 2 znanych lokalizacji: kroków `thought` lub wbudowanych kroków narzędzi (takich jak `google\_search\_call` / `google\_search\_result`). Nigdy nie pojawiają się w danych wejściowych użytkownika, danych wyjściowych modelu ani standardowych wywołaniach funkcji.

Inicjowanie interakcji z modelem myślącym jest podobne do każdego innego żądania interakcji. Określ jeden z [modeli z obsługą myślenia](#thinking-levels) w polu `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
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
        .input(InteractionsInput.of("Explain the concept of Occam's Razor and provide a simple example."))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Podsumowania myśli

Podsumowania myśli zawierają informacje o wewnętrznym procesie rozumowania modelu.
Domyślnie zwracane są tylko dane wyjściowe. Podsumowania myśli możesz włączyć za pomocą `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
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
        .input(InteractionsInput.of("Explain the concept of Occam's Razor and provide a simple example."))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

W tych przypadkach blok myśli może zawierać **tylko podpis bez podsumowania**:

- Proste żądania, w których model nie przeprowadził wystarczającego rozumowania, aby wygenerować podsumowanie.
- `thinking_summaries: "none"`, w którym podsumowania są wyraźnie wyłączone.
- Niektóre typy treści myśli, takie jak obrazy, mogą nie mieć podsumowań tekstowych.

Twój kod powinien zawsze obsługiwać bloki myśli, w których pole `summary` jest puste lub nieobecne.

## Strumieniowanie z myśleniem

Użyj strumieniowania, aby otrzymywać przyrostowe podsumowania myśli podczas generowania.
Bloki myśli są dostarczane za pomocą zdarzeń wysyłanych przez serwer (SSE) z 2 różnymi typami delta:

| Typ delta | Zawiera | Kiedy wysłano |
| --- | --- | --- |
| `thought_summary` | Treść podsumowania tekstowego lub obrazu | Co najmniej 1 delta z przyrostowym podsumowaniem |
| `thought_signature` | Podpis kryptograficzny | Ostatnia delta przed `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
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
        .input(InteractionsInput.of("Explain the concept of Occam's Razor and provide a simple example."))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Odpowiedź strumieniowa korzysta ze zdarzeń wysyłanych przez serwer (SSE) i składa się z kroków i zdarzeń, np.:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Kontrolowanie myślenia

Modele Gemini domyślnie korzystają z myślenia dynamicznego, automatycznie dostosowując ilość rozumowania do złożoności żądania. To zachowanie możesz kontrolować za pomocą parametru `thinking_level`.

| Model | Domyślne myślenie | Obsługiwane poziomy |
| --- | --- | --- |
| gemini-3.8-flash | Wł. (średni) | niski, średni, wysoki |
| gemini-3.7-flash | Wł. (średni) | niski, średni, wysoki |
| gemini-3.6-flash | Wł. (średni) | minimalny, niski, średni, wysoki |
| gemini-3.5-flash-lite | Wł. (minimalny) | minimalny, niski, średni, wysoki |
| gemini-3.1-pro-preview | Wł. (wysoki) | niski, średni, wysoki |
| gemini-3.1-flash-lite-image | Wł. (minimalny) | minimalny, wysoki |
| gemini-3-flash-preview | Wł. (wysoki) | minimalny, niski, średni, wysoki |
| gemini-3-pro-preview | Wł. (wysoki) | niski, wysoki |
| gemini-3.5-flash | Wł. (średni) | minimalny, niski, średni, wysoki |
| gemini-2.5-pro | Wł. | niski, średni, wysoki |
| gemini-2.5-flash | Wł. | niski, średni, wysoki |
| gemini-2.5-flash-lite | Wył. | niski, średni, wysoki |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
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
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
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
        .input(InteractionsInput.of("Explain the concept of Occam's Razor and provide a simple example."))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Podpisy myśli

Podpisy myśli to zaszyfrowane reprezentacje wewnętrznego rozumowania modelu. Są one wymagane do zachowania ciągłości rozumowania w interakcjach wieloetapowych.

Interfejs API Interactions znacznie upraszcza obsługę podpisów myśli w porównaniu z interfejsem API `generateContent`.

### Tryb stanowy (zalecany)

Domyślnie, gdy używasz interfejsu API Interactions w trybie stanowym (ustawiając `store: true` i przekazując `previous_interaction_id` w kolejnych turach), serwer automatycznie zarządza stanem rozmowy, w tym wszystkimi blokami myśli i podpisami. W tym trybie nie musisz nic robić z podpisami. Są one obsługiwane w całości po stronie serwera.

### Tryb bezstanowy

Jeśli samodzielnie zarządzasz stanem rozmowy (tryb bezstanowy) i przekazujesz pełną historię danych wejściowych i wyjściowych w każdym żądaniu:

- **MUSISZ** zawsze ponownie wysyłać wszystkie bloki `thought` dokładnie tak, jak zostały odebrane z modelu.
- **NIE POWINIENEŚ** usuwać ani modyfikować bloków myśli w historii, ponieważ zawierają one podpisy wymagane do kontynuowania rozumowania przez model.
- Podczas przełączania modeli w ramach sesji nadal należy ponownie wysyłać bloki myśli poprzedniego modelu. Backend zarządza zgodnością.

## Ceny

Gdy myślenie jest włączone, cena odpowiedzi jest sumą tokenów wyjściowych i tokenów myślenia. Łączną liczbę wygenerowanych tokenów myślenia możesz uzyskać z pola `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
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
        .input(InteractionsInput.of("Explain the concept of Occam's Razor and provide a simple example."))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

Modele myślące generują pełne myśli, aby poprawić jakość ostatecznej
odpowiedzi, a następnie wyświetlają [podsumowania](#summaries), aby zapewnić wgląd w
proces myślenia. Ceny są oparte na pełnych tokenach myśli, które model musi wygenerować, mimo że interfejs API wyświetla tylko podsumowanie.

Więcej informacji o tokenach znajdziesz w przewodniku po [zliczaniu tokenów](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Sprawdzone metody

Aby efektywnie korzystać z modeli myślących, postępuj zgodnie z tymi wskazówkami.

- **Sprawdzaj rozumowanie**: analizuj podsumowania myśli, aby zrozumieć błędy i ulepszyć prompty.
- **Kontroluj budżet na myślenie**: poproś model, aby mniej myślał w przypadku długich danych wyjściowych, aby zaoszczędzić tokeny.
- **Proste zadania**: używaj minimalnego lub niskiego myślenia do wyszukiwania faktów lub klasyfikacji (np. „Gdzie założono DeepMind?”).
- **Umiarkowane zadania**: używaj domyślnego myślenia do porównywania pojęć lub kreatywnego rozumowania (np. porównaj samochody elektryczne i hybrydowe).
- **Złożone zadania**: używaj maksymalnego myślenia do zaawansowanego kodowania, matematyki lub planowania wieloetapowego (np. rozwiązywania zadań matematycznych AIME).

## Co dalej?

- [Generowanie tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl): podstawowe odpowiedzi tekstowe
- [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl): łączenie z narzędziami
- [Przewodnik po Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=pl): funkcje specyficzne dla modelu

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-04 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-04 UTC."],[],[]]
