---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=pl
fetched_at: 2026-08-31T06:34:10.980209+00:00
title: "Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Gemini

Modele z serii [Gemini 3 i 2.5](https://ai.google.dev/gemini-api/docs/models?hl=pl) korzystają z wewnętrznego
„procesu myślowego”, który znacznie poprawia ich zdolność do rozumowania i planowania wieloetapowego,
dzięki czemu są bardzo skuteczne w złożonych zadaniach, takich jak
kodowanie, zaawansowana matematyka i analiza danych.

Z tego przewodnika dowiesz się, jak korzystać z funkcji myślenia Gemini za pomocą interfejsu Gemini API.

## Generowanie treści z myśleniem

Wysyłanie żądania do modelu myślącego jest podobne do każdego innego żądania generowania treści. Kluczowa różnica polega na określeniu w polu `model` jednego z
[modeli obsługujących myślenie](#supported-models), jak
pokazano w tym przykładzie [generowania tekstu](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#text-input):

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.6-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Podsumowania myśli

Podsumowania myśli to skrócone wersje surowych myśli modelu, które pozwalają zrozumieć wewnętrzny proces rozumowania modelu. Pamiętaj, że poziomy i budżety myślenia dotyczą surowych myśli modelu, a nie podsumowań myśli.

Podsumowania myśli możesz włączyć, ustawiając w konfiguracji żądania wartość `includeThoughts` na `true`. Następnie możesz uzyskać dostęp do podsumowania, iterując po `parts` parametru `response` i sprawdzając wartość logiczną `thought`.

Oto przykład pokazujący, jak włączyć i pobrać podsumowania myśli bez przesyłania strumieniowego, co powoduje zwrócenie w odpowiedzi pojedynczego, końcowego podsumowania myśli:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

A oto przykład użycia myślenia z przesyłaniem strumieniowym, które podczas generowania zwraca stopniowe, przyrostowe podsumowania:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.6-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.6-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.6-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Kontrolowanie myślenia

Modele Gemini domyślnie korzystają z myślenia dynamicznego, automatycznie dostosowując ilość wysiłku związanego z rozumowaniem do złożoności żądania użytkownika.
Jeśli jednak masz określone ograniczenia dotyczące opóźnienia lub chcesz, aby model przeprowadzał bardziej szczegółowe rozumowanie niż zwykle, możesz opcjonalnie użyć parametrów do kontrolowania zachowania myślenia.

### Poziomy myślenia (Gemini 3)

Parametr `thinkingLevel`, zalecany w przypadku modeli Gemini 3 i nowszych, umożliwia kontrolowanie zachowania rozumowania.

W tabeli poniżej znajdziesz szczegółowe informacje o ustawieniach `thinkingLevel` dla każdego typu modelu:

| Poziom myślenia | Gemini 3.6 i 3.5 Flash | Gemini 3.1 Pro | Gemini 3.5 i 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Opis |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Obsługiwane | Nieobsługiwane | Obsługiwane (domyślnie) | Obsługiwane (domyślnie) | Obsługiwane | W przypadku większości zapytań odpowiada ustawieniu „bez myślenia”. Pamiętaj, że `minimal` nie gwarantuje wyłączenia myślenia. W przypadku złożonych zadań model może przeprowadzać bardzo minimalne rozumowanie. |
| **`low`** | Obsługiwane | Obsługiwane | Obsługiwane | Nieobsługiwane | Obsługiwane | Minimalizuje opóźnienie i koszt. |
| **`medium`** | Obsługiwane (domyślnie) | Obsługiwane | Obsługiwane | Nieobsługiwane | Obsługiwane | Zrównoważone myślenie w przypadku większości zadań. |
| **`high`** | Obsługiwane (dynamiczne) | Obsługiwane (domyślnie, dynamiczne) | Obsługiwane (dynamiczne) | Obsługiwane (dynamiczne) | Obsługiwane (domyślnie, dynamiczne) | Maksymalizuje głębokość rozumowania. Model może znacznie dłużej generować pierwszy token wyjściowy (nie wymagający myślenia), ale wynik będzie bardziej starannie przemyślany. |

Poniższy przykład pokazuje, jak ustawić poziom myślenia.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.6-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Nie możesz wyłączyć myślenia w przypadku modelu Gemini 3.1 Pro. Modele Gemini 3 Flash i Flash-Lite
również nie obsługują pełnego wyłączenia myślenia.
Jeśli nie określisz poziomu myślenia, Gemini użyje domyślnego poziomu myślenia modeli Gemini 3 (np. `"high"` w przypadku Gemini 3.1 Pro i `"medium"` w przypadku Gemini 3.5 Flash).

Modele z serii Gemini 2.5 nie obsługują parametru `thinkingLevel`. Zamiast niego użyj parametru `thinkingBudget`.

### Budżety na myślenie

Parametr `thinkingBudget`, wprowadzony w serii Gemini 2.5, informuje model o konkretnej liczbie tokenów myśli, które mają być używane do rozumowania.

Poniżej znajdziesz szczegóły konfiguracji parametru `thinkingBudget` dla każdego typu modelu.
Myślenie możesz wyłączyć, ustawiając wartość `thinkingBudget` na 0.
Ustawienie wartości `thinkingBudget` na -1 włącza
**myślenie dynamiczne**, co oznacza, że model dostosuje budżet do
złożoności żądania.

| Model | Ustawienie domyślne (budżet na myślenie nie jest ustawiony) | Zakres | Wyłącz myślenie | Włącz myślenie dynamiczne |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Myślenie dynamiczne | `128` do `32768` | Nie dotyczy: nie można wyłączyć myślenia | `thinkingBudget = -1` (domyślnie) |
| **2.5 Flash** | Myślenie dynamiczne | `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (domyślnie) |
| **2.5 Flash (wersja testowa)** | Myślenie dynamiczne | `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (domyślnie) |
| **2.5 Flash Lite** | Model nie myśli | `512` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite (wersja testowa)** | Model nie myśli | `512` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 (wersja testowa)** | Myślenie dynamiczne | `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (domyślnie) |
| **2.5 Flash Live Native Audio (wersja testowa) (09-2025)** | Myślenie dynamiczne | `0` do `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (domyślnie) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

W zależności od prompta model może przekroczyć lub nie wykorzystać w pełni budżetu tokenów.

## Podpisy myśli

Interfejs Gemini API jest bezstanowy, więc model traktuje każde żądanie do interfejsu API niezależnie i nie ma dostępu do kontekstu myśli z poprzednich tur interakcji wieloetapowych.

Aby umożliwić zachowanie kontekstu myśli w interakcjach wieloetapowych, Gemini zwraca podpisy myśli, które są zaszyfrowanymi reprezentacjami wewnętrznego procesu myślowego modelu.

- **Modele Gemini 2.5** zwracają podpisy myśli, gdy myślenie jest włączone i
  żądanie zawiera [wywołanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#thinking),
  w szczególności [deklaracje funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-2).
- **Modele Gemini 3** mogą zwracać podpisy myśli dla wszystkich typów [części](https://ai.google.dev/api/caching?hl=pl#Part).
  Zalecamy, aby zawsze przekazywać wszystkie podpisy w takiej postaci, w jakiej zostały odebrane, ale w przypadku podpisów wywołań funkcji jest to *wymagane*. Więcej informacji znajdziesz na stronie
  [Podpisy myśli](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl).

Inne ograniczenia dotyczące użycia, które należy wziąć pod uwagę w przypadku wywoływania funkcji:

- Podpisy są zwracane przez model w innych częściach odpowiedzi, np. w częściach wywołania funkcji lub tekstu.
  [Przekaż modelowi całą odpowiedź](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#step-4)
  ze wszystkimi częściami w kolejnych turach.
- Nie łącz części z podpisami.
- Nie łącz części z podpisem z inną częścią bez podpisu.

## Ceny

Gdy myślenie jest włączone, cena odpowiedzi jest sumą tokenów wyjściowych i tokenów myśli. Łączną liczbę wygenerowanych tokenów myśli możesz uzyskać z pola `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

[Modele myślące generują pełne myśli, aby poprawić jakość ostatecznej
odpowiedzi, a następnie podsumowania](#summaries) aby zapewnić wgląd w
proces myślowy. Dlatego cena jest oparta na pełnych tokenach myśli, które model musi wygenerować, aby utworzyć podsumowanie, mimo że z interfejsu API jest zwracane tylko podsumowanie.

Więcej informacji o tokenach znajdziesz w przewodniku [Liczenie tokenów](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

## Sprawdzone metody

W tej sekcji znajdziesz wskazówki dotyczące efektywnego korzystania z modeli myślących.
Jak zawsze, najlepsze wyniki uzyskasz, jeśli będziesz postępować zgodnie z naszymi [wskazówkami dotyczącymi promptów i sprawdzonymi metodami](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl).

### Debugowanie i sterowanie

- **Sprawdzanie rozumowania**: jeśli nie otrzymujesz oczekiwanej odpowiedzi od modeli myślących, warto dokładnie przeanalizować podsumowania myśli Gemini.
  Możesz zobaczyć, jak model podzielił zadanie i doszedł do wniosku, oraz wykorzystać te informacje, aby uzyskać prawidłowe wyniki.
- **Wskazówki dotyczące rozumowania**: jeśli oczekujesz szczególnie długiego
  wyniku, możesz podać w prompcie wskazówki, aby ograniczyć
  [ilość myślenia](#set-budget), z której korzysta model. Dzięki temu możesz zarezerwować więcej tokenów wyjściowych na potrzeby odpowiedzi.

### Złożoność zadania

- **Łatwe zadania (myślenie może być wyłączone):** w przypadku prostych żądań, które nie wymagają złożonego rozumowania, takich jak wyszukiwanie faktów lub klasyfikacja, myślenie nie jest wymagane. Przykłady:
  - „Gdzie założono DeepMind?”
  - „Czy ten e-mail zawiera prośbę o spotkanie, czy tylko informacje?”
- **Średnio trudne zadania (domyślne/częściowe myślenie):** wiele typowych żądań wymaga pewnego stopnia przetwarzania krok po kroku lub głębszego zrozumienia. Gemini może elastycznie korzystać z funkcji myślenia w przypadku takich zadań jak:
  - Porównanie fotosyntezy i dorastania.
  - Porównanie samochodów elektrycznych i hybrydowych.
- **Trudne zadania (maksymalna zdolność myślenia):** w przypadku naprawdę złożonych wyzwań, takich jak rozwiązywanie złożonych problemów matematycznych lub zadań związanych z kodowaniem, zalecamy ustawienie wysokiego budżetu na myślenie. Tego typu zadania wymagają od modelu pełnego wykorzystania możliwości rozumowania i planowania, często obejmującego wiele wewnętrznych kroków przed udzieleniem odpowiedzi. Przykłady:
  - Rozwiąż zadanie 1 w AIME 2025: znajdź sumę wszystkich podstaw całkowitych b > 9, dla
    których 17b jest dzielnikiem 97b.
  - Napisz kod w Pythonie dla aplikacji internetowej, która wizualizuje dane z giełdy w czasie rzeczywistym, w tym uwierzytelnianie użytkowników. Zadbaj o jak największą wydajność.

## Obsługiwane modele, narzędzia i funkcje

Funkcje myślenia są obsługiwane we wszystkich modelach z serii 3 i 2.5.
Wszystkie możliwości modelu znajdziesz na
[stronie przeglądu modelu](https://ai.google.dev/gemini-api/docs/models?hl=pl).

Modele myślące współpracują ze wszystkimi narzędziami i funkcjami Gemini. Dzięki temu modele mogą wchodzić w interakcje z systemami zewnętrznymi, wykonywać kod lub uzyskiwać dostęp do informacji w czasie rzeczywistym, włączając wyniki do swojego rozumowania i ostatecznej odpowiedzi.

Przykłady użycia narzędzi z modelami myślącymi znajdziesz w [Thinking cookbook][Colab].

## Co dalej?

- Informacje o myśleniu znajdziesz w przewodniku [Zgodność z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
