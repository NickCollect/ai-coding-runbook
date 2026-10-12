---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pl
fetched_at: 2026-10-12T06:50:58.862884+00:00
title: "Rozdzielczo\u015b\u0107 multimedi\u00f3w \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# Rozdzielczość multimediów

Parametr `media_resolution` określa, jak interfejs Gemini API przetwarza dane wejściowe multimediów, takie jak obrazy, filmy, dźwięk i dokumenty PDF, poprzez określenie **maksymalnej liczby tokenów** przydzielonych do danych wejściowych multimediów. Umożliwia to zrównoważenie jakości odpowiedzi z opóźnieniem i kosztem. W przypadku danych wejściowych w postaci obrazów i dokumentów przydział tokenów jest skalowany na podstawie ustawienia rozdzielczości, natomiast w przypadku danych wejściowych w postaci dźwięku tokenizacja odbywa się ze stałą szybkością na sekundę na wszystkich poziomach rozdzielczości. Informacje o różnych ustawieniach, wartościach domyślnych i ich odpowiednikach w postaci tokenów znajdziesz w sekcji [Liczba tokenów](#token-counts).

Rozdzielczość multimediów możesz skonfigurować na 2 sposoby:

- [Za część](#per-part-media-resolution) (tylko Gemini 3)
- [Globalnie](#global-media-resolution) w przypadku całego żądania `generateContent` (wszystkie modele multimodalne)

## Rozdzielczość multimediów w poszczególnych częściach (tylko Gemini 3)

Gemini 3 umożliwia ustawienie rozdzielczości multimediów dla poszczególnych obiektów multimedialnych w ramach żądania, co pozwala na szczegółową optymalizację wykorzystania tokenów. W ramach jednego żądania możesz łączyć różne poziomy rozdzielczości. Na przykład używaj wysokiej rozdzielczości w przypadku złożonego diagramu, a niskiej w przypadku obrazu kontekstowego. To ustawienie
zastępuje globalną konfigurację konkretnej części. Domyślne ustawienia znajdziesz w sekcji [Liczba tokenów](#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Globalna rozdzielczość multimediów

Możesz ustawić domyślną rozdzielczość wszystkich komponentów multimedialnych w żądaniu za pomocą parametru
`GenerationConfig`. Jest to obsługiwane przez wszystkie modele multimodalne. Jeśli żądanie zawiera zarówno ustawienia globalne, jak i [ustawienia dotyczące poszczególnych części](#per-part-media-resolution), w przypadku danego elementu pierwszeństwo mają ustawienia dotyczące poszczególnych części.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Dostępne wartości rozdzielczości

Interfejs Gemini API określa te poziomy rozdzielczości multimediów:

- `MEDIA_RESOLUTION_UNSPECIFIED`: ustawienie domyślne. Liczba tokenów na tym poziomie znacznie różni się w przypadku Gemini 3 i starszych modeli Gemini.
- `MEDIA_RESOLUTION_LOW`: mniejsza liczba tokenów, co skutkuje szybszym przetwarzaniem i niższymi kosztami, ale mniejszą szczegółowością.
- `MEDIA_RESOLUTION_MEDIUM`: równowaga między szczegółowością, kosztem i opóźnieniem.
- `MEDIA_RESOLUTION_HIGH`: większa liczba tokenów, która zapewnia modelowi więcej szczegółów, ale wiąże się z większym opóźnieniem i kosztem.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (Tylko w przypadku części): najwyższa liczba tokenów, wymagana w określonych przypadkach użycia, np. w [przypadku korzystania z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

Pamiętaj, że `MEDIA_RESOLUTION_HIGH` zapewnia optymalną wydajność w większości przypadków użycia.

Dokładna liczba tokenów wygenerowanych na każdym z tych poziomów zależy zarówno od **typu multimediów** (obraz, film, dźwięk, PDF), jak i od **wersji modelu**.

## Liczba tokenów

W tabelach poniżej znajdziesz podsumowanie przybliżonej liczby tokenów dla każdej wartości i każdego typu multimediów w poszczególnych rodzinach modeli.`media_resolution`

**Modele Gemini 3**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Obraz** | **Film** | **Dźwięk** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (wartość domyślna) | 1120 | 70 | 25 (na sekundę) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25 (na sekundę) | 280 znaków + tekst natywny |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25 (na sekundę) | 560 + tekst natywny |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25 (na sekundę) | 1120 + Native Text |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | Nie dotyczy | Nie dotyczy | Nie dotyczy |

**Modele Gemini 2.5**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **Obraz** | **Film** | **Dźwięk** | **PDF (zeskanowany)** | **PDF (natywny)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (wartość domyślna) | 256 + Pan & Scan (~2048) | 256 | 32 (na sekundę) | 256 + OCR | 256 znaków + tekst natywny |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32 (na sekundę) | 64 + OCR | 64 + tekst natywny |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32 (na sekundę) | 256 + OCR | 256 znaków + tekst natywny |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 32 (na sekundę) | 256 + OCR | 256 znaków + tekst natywny |

## Wybór odpowiedniej rozdzielczości

- **Domyślna (`UNSPECIFIED`):** zacznij od domyślnej. Jest on dostosowany do zapewnienia dobrej równowagi między jakością, opóźnieniem i kosztem w przypadku najczęstszych zastosowań.
- **`LOW`:** używaj w sytuacjach, w których najważniejsze są koszt i opóźnienie, a szczegółowość ma mniejsze znaczenie.
- **`MEDIUM` / `HIGH`:** zwiększ rozdzielczość, gdy zadanie wymaga zrozumienia skomplikowanych szczegółów w treściach. Jest to często potrzebne w przypadku złożonej analizy wizualnej, odczytywania wykresów lub zrozumienia gęstych dokumentów.
- **`ULTRA HIGH`** – dostępne tylko w przypadku ustawienia dla poszczególnych części. Zalecane w przypadku konkretnych zastosowań, takich jak korzystanie z komputera, lub gdy testy wykazują wyraźną poprawę w porównaniu z `HIGH`.
- **Sterowanie poszczególnymi częściami (Gemini 3):** optymalizuje wykorzystanie tokenów. Na przykład w prompcie z wieloma obrazami użyj `HIGH` w przypadku złożonego diagramu, a `LOW` lub `MEDIUM` w przypadku prostszych obrazów kontekstowych.

**Zalecane ustawienia**

Poniżej znajdziesz listę zalecanych ustawień rozdzielczości multimediów dla każdego obsługiwanego typu multimediów.

|  |  |  |  |
| --- | --- | --- | --- |
| **Typ nośnika** | **Zalecane ustawienie** | **Maksymalna liczba tokenów** | **Wytyczne dotyczące użytkowania** |
| **Obrazy** | `MEDIA_RESOLUTION_HIGH` | 1120 | Zalecane w przypadku większości zadań związanych z analizą obrazów, aby zapewnić najwyższą jakość. |
| **Pliki PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Optymalne do analizy dokumentów; jakość zwykle osiąga maksymalny poziom przy wartości `medium`. Zwiększenie do `high` rzadko poprawia wyniki OCR w przypadku standardowych dokumentów. |
| **Wideo** (ogólne) | `MEDIA_RESOLUTION_LOW` (lub `MEDIA_RESOLUTION_MEDIUM`) | 70 (na klatkę) | **Uwaga:** w przypadku filmów ustawienia `low` i `medium` są traktowane identycznie (70 tokenów), aby zoptymalizować wykorzystanie kontekstu. Wystarcza to w przypadku większości zadań związanych z rozpoznawaniem i opisywaniem działań. |
| **Film** (z dużą ilością tekstu) | `MEDIA_RESOLUTION_HIGH` | 280 (na klatkę) | Wymagane tylko wtedy, gdy przypadek użycia obejmuje odczytywanie gęstego tekstu (OCR) lub drobnych szczegółów w klatkach wideo. |
| **Dźwięk** | `MEDIA_RESOLUTION_UNSPECIFIED` (wartość domyślna) | 25 (na sekundę) w przypadku Gemini 3; 32 (na sekundę) w przypadku Gemini 2.5 | Dźwięk jest tokenizowany według stałej stawki za sekundę we wszystkich obsługiwanych ustawieniach rozdzielczości (`unspecified`, `low`, `medium` i `high`). |

Zawsze testuj i oceniaj wpływ różnych ustawień rozdzielczości na konkretną aplikację, aby znaleźć najlepszy kompromis między jakością, opóźnieniem i kosztem.

## Związek z trybami przetwarzania filmów

Parametry `media_resolution` i przetwarzania kontrolują różne aspekty danych wejściowych wideo:

- `media_resolution` określa **rozdzielczość** każdej klatki (liczbę tokenów na klatkę).
- Elementy sterujące `processing` / `media_processing` określają, **które treści z filmu** są wczytywane do kontekstu.

Oba ustawienia możesz zastosować do tego samego wejścia wideo. Możesz na przykład użyć przetwarzania agentowego z niską rozdzielczością multimediów, aby zminimalizować całkowite zużycie tokenów w przypadku długiego filmu.

Szczegółowe informacje o trybach przetwarzania filmów znajdziesz w przewodniku [Analizowanie filmów przez agenta](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl#agentic-video-understanding).

## Podsumowanie zgodności wersji

- Wyliczenie `MediaResolution` jest dostępne w przypadku wszystkich modeli obsługujących dane wejściowe w postaci multimediów.
- Liczba tokenów powiązana z każdym poziomem wyliczenia **różni się** w przypadku modeli Gemini 3 i wcześniejszych wersji Gemini.
- Ustawienie `media_resolution` w przypadku poszczególnych obiektów `Part` jest **dostępne tylko w modelach Gemini 3**.

## Dalsze kroki

- Więcej informacji o multimodalnych możliwościach interfejsu Gemini API znajdziesz w przewodnikach dotyczących [rozpoznawania obrazów](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=pl), [rozumienia filmów](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=pl), [rozumienia dźwięku](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=pl) i [rozumienia dokumentów](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-19 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-19 UTC."],[],[]]
