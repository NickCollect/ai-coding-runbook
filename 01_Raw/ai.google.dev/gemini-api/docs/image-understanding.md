---
source_url: https://ai.google.dev/gemini-api/docs/image-understanding?hl=pl
fetched_at: 2026-08-24T02:30:39.129700+00:00
title: "Interpretacja obrazu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interpretacja obrazu

Modele Gemini są budowane od podstaw z myślą o multimodalności, co umożliwia wykonywanie wielu zadań związanych z przetwarzaniem obrazów i widzeniem komputerowym, w tym m.in. tworzenie podpisów do obrazów, klasyfikację i wizualne odpowiedzi na pytania, bez konieczności trenowania wyspecjalizowanych modeli ML.

Oprócz ogólnych możliwości multimodalnych modele Gemini oferują
**większą dokładność** w konkretnych przypadkach użycia, takich jak [wykrywanie obiektów](#object-detection)
i [segmentacja](#segmentation), dzięki dodatkowemu trenowaniu.

## Przekazywanie obrazów do Gemini

Obrazy możesz przekazywać do Gemini na kilka sposobów:

- [Przekazywanie obrazu za pomocą adresu URL](#url-image): idealne rozwiązanie w przypadku obrazów dostępnych publicznie.
- [Przekazywanie danych obrazu w tekście](#inline-image): w przypadku danych obrazu zakodowanych w formacie Base64.
- [Przesyłanie obrazów za pomocą interfejsu File API](#upload-image): zalecane w przypadku
  większych plików lub ponownego używania obrazów w wielu żądaniach.

### Przekazywanie obrazu za pomocą adresu URL

Obraz możesz przesłać za pomocą interfejsu [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl) i przekazać go
w żądaniu:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const uploadedFile = await client.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Przekazywanie danych obrazu w tekście

Dane obrazu możesz przekazywać jako ciągi tekstowe zakodowane w formacie Base64:

### Python

```
import base64
from google import genai

with open('path/to/small-sample.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            data: base64ImageFile,
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

### Przesyłanie obrazów za pomocą interfejsu File API

W przypadku dużych plików lub aby móc wielokrotnie używać tego samego pliku obrazu, użyj interfejsu Files API. Zapoznaj się z przewodnikiem po interfejsie [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

### Python

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "Caption this image."},
        {
            "type": "image",
            "uri": my_file.uri,
            "mime_type": my_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const myfile = await client.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "Caption this image."},
        {
            type: "image",
            uri: myfile.uri,
            mime_type: myfile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
# First upload the file (see Files API guide for details)
# Then use the file URI in the request:

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Caption this image."},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Promptowanie za pomocą wielu obrazów

W jednym prompcie możesz podać kilka obrazów, dodając do tablicy `input` kilka obiektów obrazu:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": "What is different between these two images?"},
        {
            "type": "image",
            "uri": "https://example.com/image1.jpg",
            "mime_type": "image/jpeg"
        },
        {
            "type": "image",
            "uri": "https://example.com/image2.jpg",
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: [
        {type: "text", text: "What is different between these two images?"},
        {
            type: "image",
            uri: "https://example.com/image1.jpg",
            mime_type: "image/jpeg"
        },
        {
            type: "image",
            uri: "https://example.com/image2.jpg",
            mime_type: "image/jpeg"
        }
    ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "What is different between these two images?"},
      {
        "type": "image",
        "uri": "https://example.com/image1.jpg",
        "mime_type": "image/jpeg"
      },
      {
        "type": "image",
        "uri": "https://example.com/image2.jpg",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

## Wykrywanie obiektów

Modele są trenowane do wykrywania obiektów na obrazie i uzyskiwania ich współrzędnych ramki ograniczającej. Współrzędne względem wymiarów obrazu są skalowane do zakresu [0, 1000]. Musisz przeskalować te współrzędne na podstawie oryginalnego rozmiaru obrazu.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    }
)

bounding_boxes = BoundingBoxes.model_validate_json(interaction.output_text)
print(bounding_boxes)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.";

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    }
  }'
```

Więcej przykładów znajdziesz w [Gemini Cookbook](https://github.com/google-gemini/cookbook).

## Podział na segmenty

Modele Gemini nie tylko wykrywają obiekty, ale też je segmentują i udostępniają ich maski konturów.

Model przewiduje listę JSON, w której każdy element reprezentuje maskę segmentacji. Każdy element ma ramkę ograniczającą („`box_2d`”) w formacie `[ymin, xmin, ymax, xmax]` ze znormalizowanymi współrzędnymi od 0 do 1000, etykietę („`label`”) identyfikującą obiekt oraz maskę segmentacji w ramce ograniczającej jako wielokąt ze współrzędnymi `[x, y]` znormalizowanymi do zakresu 0–1000.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List
import json

client = genai.Client()

prompt = """
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
"""

class BoundingBox(BaseModel):
    box_2d: List[int] = Field(description="The 2D bounding box of the item as [ymin, xmin, ymax, xmax] normalized to 0-1000.")
    mask: List[List[int]] = Field(description="The segmentation mask of the item as a polygon of [x,y] coordinates, normalized to 0-1000.")
    label: str = Field(description="A descriptive label for the item.")

class BoundingBoxes(BaseModel):
    boxes: List[BoundingBox]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "text", "text": prompt},
        {
            "type": "image",
            "uri": "https://example.com/image.png",
            "mime_type": "image/png"
        }
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": BoundingBoxes.model_json_schema()
    },
    generation_config={
        "thinking_level": "minimal"
    }
)

items = BoundingBoxes.model_validate_json(interaction.output_text)
print("Segmentation results:", items)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const client = new GoogleGenAI({});
const prompt = `
Give the segmentation masks for the wooden and glass items.
Output a JSON list of segmentation masks where each entry contains the 2D
bounding box in the key "box_2d", the segmentation mask in key "mask", and
the text label in the key "label". Use descriptive labels.
`;

const boundingBoxesSchema = z.object({
  boxes: z.array(z.object({
    box_2d: z.array(z.number()),
    mask: z.array(z.array(z.number())),
    label: z.string()
  }))
});

const interaction = await client.interactions.create({
  model: "gemini-3.6-flash",
  input: [
    { type: "text", text: prompt },
    {
      type: "image",
      uri: "https://example.com/image.png",
      mime_type: "image/png"
    }
  ],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: z.toJSONSchema(boundingBoxesSchema)
  },
  generation_config: {
    thinking_level: "minimal"
  }
});

const result = boundingBoxesSchema.parse(JSON.parse(interaction.output_text));
console.log(result);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {"type": "text", "text": "Give the segmentation masks for the wooden and glass items.\nOutput a JSON list of segmentation masks where each entry contains the 2D\nbounding box in the key \"box_2d\", the segmentation mask in key \"mask\", and\nthe text label in the key \"label\". Use descriptive labels."},
      {
        "type": "image",
        "uri": "https://example.com/image.png",
        "mime_type": "image/png"
      }
    ],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "boxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "box_2d": { "type": "array", "items": { "type": "integer" } },
                "mask": { "type": "array", "items": { "type": "array", "items": { "type": "integer" } } },
                "label": { "type": "string" }
              },
              "required": ["box_2d", "mask", "label"]
            }
          }
        },
        "required": ["boxes"]
      }
    },
    "generation_config": {
      "thinking_level": "minimal"
    }
  }'
```

![Stół z babeczkami, na którym wyróżniono drewniane i szklane przedmioty](https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpg?hl=pl)

Przykład danych wyjściowych segmentacji z obiektami i maskami segmentacji

## Obsługiwane formaty obrazów

Gemini obsługuje te typy MIME formatów obrazów:

- PNG – `image/png`
- JPEG – `image/jpeg`
- WEBP – `image/webp`
- HEIC – `image/heic`
- HEIF – `image/heif`

Więcej informacji o innych metodach wprowadzania plików znajdziesz w
[przewodniku po metodach wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

## Uprawnienia

Wszystkie wersje modelu Gemini są multimodalne i mogą być używane w wielu zadaniach związanych z przetwarzaniem obrazów i widzeniem komputerowym, w tym m.in. tworzeniem podpisów do obrazów, odpowiadaniem na pytania dotyczące obrazów, klasyfikowaniem obrazów, wykrywaniem obiektów i segmentacją obiektów.

W zależności od wymagań dotyczących jakości i skuteczności Gemini może ograniczyć konieczność używania wyspecjalizowanych modeli ML.

Najnowsze wersje modelu są specjalnie trenowane, aby oprócz ogólnych możliwości, takich jak ulepszone
[wykrywanie obiektów](#object-detection) i [segmentacja](#segmentation), zwiększać dokładność w przypadku
wyspecjalizowanych zadań.

## Ograniczenia i najważniejsze informacje techniczne

### Limit pliku

Modele Gemini obsługują maksymalnie 3600 plików obrazów na żądanie.

### Obliczanie liczby tokenów

- 258 tokenów, jeśli oba wymiary są mniejsze lub równe 384 piksele.
  Większe obrazy są dzielone na kafelki o wymiarach 768 x 768 pikseli, z których każdy kosztuje 258 tokenów.

Przybliżony wzór na obliczanie liczby kafelków jest taki:

- Oblicz rozmiar jednostki przycinania, który wynosi w przybliżeniu: `floor(min(width, height)` / 1,5).
- Podziel każdy wymiar przez rozmiar jednostki przycinania i pomnóż przez siebie, aby uzyskać liczbę kafelków.

Na przykład obraz o wymiarach 960 x 540 będzie miał rozmiar jednostki przycinania równy 360. Podziel każdy wymiar przez 360, a liczba kafelków wyniesie 3 \* 2 = 6.

### Rozdzielczość multimediów

Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem multimodalnego widzenia za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**.
Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają zużycie tokenów i opóźnienie.

## Porady i sprawdzone metody

- Sprawdź, czy obrazy są prawidłowo obrócone.
- Używaj wyraźnych obrazów bez rozmycia.
- Jeśli używasz jednego obrazu z tekstem, umieść prompt tekstowy *przed* obrazem w tablicy `input`.

## Co dalej?

Z tego przewodnika dowiesz się, jak przesyłać pliki obrazów i generować dane wyjściowe tekstowe na podstawie danych wejściowych obrazów. Więcej informacji znajdziesz w tych materiałach:

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl): dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować działaniem modelu na podstawie
  konkretnych potrzeb i przypadków użycia.
- [Strategie tworzenia promptów za pomocą plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): interfejs Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, obrazów, dźwięku i wideo, czyli tworzenie promptów multimodalnych.
- [Wskazówki dotyczące bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl): modele generatywnej
  AI czasami generują nieoczekiwane dane wyjściowe, np. niedokładne,
  stronnicze lub obraźliwe. Przetwarzanie końcowe i ocena przez człowieka są niezbędne, aby ograniczyć ryzyko szkód spowodowanych takimi danymi wyjściowymi.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
