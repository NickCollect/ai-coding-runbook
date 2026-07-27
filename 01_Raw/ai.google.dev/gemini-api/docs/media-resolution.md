---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl
fetched_at: 2026-07-27T04:50:41.843370+00:00
title: "Rozdzielczo\u015b\u0107 multimedi\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozdzielczość multimediów

Parametr `media_resolution` określa, jak interfejs Gemini API przetwarza dane multimedialne, takie jak obrazy, filmy i dokumenty PDF, poprzez określenie **maksymalnej liczby tokenów** przydzielonych na dane multimedialne. Dzięki temu możesz zrównoważyć jakość odpowiedzi z opóźnieniem i kosztem. Więcej informacji o różnych ustawieniach, wartościach domyślnych i ich odpowiednikach w tokenach znajdziesz w sekcji [Liczba tokenów](#token-counts).

Możesz skonfigurować rozdzielczość multimediów dla poszczególnych obiektów multimedialnych (elementów treści) w żądaniu (tylko w Gemini 3).

## Rozdzielczość multimediów dla poszczególnych elementów treści (tylko w Gemini 3)

Gemini 3 umożliwia ustawienie rozdzielczości multimediów dla poszczególnych obiektów multimedialnych w żądaniu, co pozwala na precyzyjną optymalizację wykorzystania tokenów. W jednym żądaniu możesz używać różnych poziomów rozdzielczości. Na przykład możesz użyć wysokiej rozdzielczości w przypadku złożonego diagramu i niskiej rozdzielczości w przypadku prostego obrazu kontekstowego.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Dostępne wartości rozdzielczości

Interfejs Gemini API definiuje te poziomy rozdzielczości multimediów:

- `unspecified` (nieokreślona): ustawienie domyślne. Liczba tokenów na tym poziomie znacznie różni się w zależności od tego, czy używasz Gemini 3, czy wcześniejszych modeli Gemini.
- `low` (niska): mniejsza liczba tokenów, co przekłada się na szybsze przetwarzanie i niższe koszty, ale mniejszą szczegółowość.
- `medium` (średnia): równowaga między szczegółowością, kosztem i opóźnieniem.
- `high` (wysoka): większa liczba tokenów, co zapewnia modelowi więcej szczegółów, ale wiąże się z większym opóźnieniem i kosztem.
- `ultra_high` (bardzo wysoka) (tylko w przypadku poszczególnych elementów treści): największa liczba tokenów, wymagana w określonych przypadkach użycia, np. podczas korzystania z [komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

Pamiętaj, że w większości przypadków użycia optymalną skuteczność zapewnia ustawienie `high`.

Dokładna liczba tokenów generowanych na każdym z tych poziomów zależy zarówno od **typu multimediów** (obraz, film, PDF), jak i **wersji modelu**.

## Liczba tokenów

W tabelach poniżej znajdziesz podsumowanie przybliżonej liczby tokenów dla każdej wartości `media_resolution` i typu multimediów w przypadku poszczególnych rodzin modeli.

**Modele Gemini 3**

| MediaResolution | Obraz | Wideo | PDF |
| --- | --- | --- | --- |
| `unspecified` (domyślna) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + tekst natywny |
| `medium` | 560 | 70 | 560 + tekst natywny |
| `high` | 1120 | 280 | 1120 + tekst natywny |
| `ultra_high` | 2240 | Nie dotyczy | Nie dotyczy |

## Wybór odpowiedniej rozdzielczości

- **Domyślna (`unspecified`):** zacznij od ustawienia domyślnego. Jest ono dostosowane do większości typowych przypadków użycia, aby zapewnić dobrą równowagę między jakością, opóźnieniem i kosztem.
- **`low`:** używaj w sytuacjach, w których najważniejsze są koszt i opóźnienie, a szczegółowość jest mniej istotna.
- **`medium` / `high`:** zwiększ rozdzielczość, gdy zadanie wymaga zrozumienia złożonych szczegółów w multimediach. Jest to często konieczne w przypadku złożonej analizy wizualnej, odczytywania wykresów lub zrozumienia obszernych dokumentów.
- **`ultra_high`** – dostępne tylko w przypadku ustawienia dla poszczególnych elementów treści. Zalecane w określonych przypadkach użycia, np. podczas korzystania z komputera, lub gdy testy wykazują wyraźną poprawę w porównaniu z ustawieniem `high`.
- **Sterowanie dla poszczególnych elementów treści (Gemini 3):** optymalizuje wykorzystanie tokenów. Na przykład w przypadku prompta z wieloma obrazami użyj ustawienia `high` w przypadku złożonego diagramu oraz `low` lub `medium` w przypadku prostszych obrazów kontekstowych.

**Zalecane ustawienia**

Poniżej znajdziesz zalecane ustawienia rozdzielczości multimediów dla każdego obsługiwanego typu multimediów.

| Typ mediów | Zalecane ustawienie | Maks. liczba tokenów | Wytyczne dotyczące użytkowania |
| --- | --- | --- | --- |
| **Obrazy** | `high` | 1120 | Zalecane w przypadku większości zadań analizy obrazów, aby zapewnić maksymalną jakość. |
| **Pliki PDF** | `medium` | 560 | Optymalne do zrozumienia dokumentu. Jakość zwykle osiąga poziom nasycenia przy ustawieniu `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Wideo** (ogólne) | `low` (lub `medium`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Jest to wystarczające w przypadku większości zadań związanych z rozpoznawaniem działań i opisem. |
| **Wideo** (z dużą ilością tekstu) | `high` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie gęstego tekstu (OCR) lub małych szczegółów w klatkach wideo. |

Zawsze testuj i oceniaj wpływ różnych ustawień rozdzielczości na swoją aplikację, aby znaleźć najlepszy kompromis między jakością, opóźnieniem i kosztem.

## Podsumowanie zgodności wersji

- Ustawienie `resolution` w przypadku poszczególnych elementów treści jest **dostępne tylko w modelach Gemini 3**.

## Dalsze kroki

- Więcej informacji o możliwościach multimodalnych interfejsu Gemini API znajdziesz w przewodnikach dotyczących [rozumienia obrazów](https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl), [rozumienia filmów](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl) i [rozumienia dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-06 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-06 UTC."],[],[]]
