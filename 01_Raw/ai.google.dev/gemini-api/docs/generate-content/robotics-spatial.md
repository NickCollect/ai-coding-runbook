---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=pl
fetched_at: 2026-08-10T03:24:23.542459+00:00
title: "rozumowanie przestrzenne, \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# rozumowanie przestrzenne,

Modele Gemini Robotics ER mogą wskazywać obiekty, śledzić je w filmie, wykrywać za pomocą ramek ograniczających i generować trajektorie ruchu. Wszystkie przykłady na tej stronie używają promptów w języku naturalnym z `generateContent`.

Pełny kod, który można uruchomić, znajdziesz w
[przewodniku Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Wskazywanie obiektów

Poniższy przykład znajduje określone obiekty na obrazie i zwraca ich znormalizowane współrzędne `[y, x]`:

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

# Load your image
with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

image_response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
        PROMPT
    ],
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(image_response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

Wynikiem będzie tablica JSON zawierająca obiekty, z których każdy ma `point` (znormalizowane współrzędne `[y, x]`) i `label` identyfikujący obiekt.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Poniższy obraz przedstawia przykład wyświetlania tych punktów:

![Przykład wyświetlający punkty obiektów na obrazie](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=pl)

## Śledzenie obiektów w filmie

Gemini Robotics ER 2 może też analizować klatki wideo, aby śledzić obiekty w czasie. Listę obsługiwanych formatów wideo znajdziesz w sekcji [Dane wejściowe wideo](https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl#supported-formats).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your video
with open("my-video.mp4", 'rb') as f:
    video_bytes = f.read()

prompt = """
          Point to the red ball in every frame where it appears.
          The answer should follow the json format: [{"point": [y, x],
          "label": <label>}, ...]. The points are in [y, x] format
          normalized to 0-1000. Return one entry per frame that contains
          the object.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=video_bytes,
      mime_type='video/mp4',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

## Wykrywanie obiektów i ramki ograniczające

Oprócz punktów możesz poprosić model o zwrócenie 2D ramek ograniczających, które zapewniają więcej szczegółów przestrzennych wykrytych obiektów.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open("my-image.png", 'rb') as f:
    image_bytes = f.read()

prompt = """
          Detect all objects in this image and return bounding boxes.
          The answer should follow the JSON format:
          [{"label": <label>, "y": <y_min>, "x": <x_min>,
            "y2": <y_max>, "x2": <x_max>}, ...]
          where coordinates are normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/png',
    ),
    prompt
  ],
  config = types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="low")
  )
)

print(image_response.text)
```

## Trajektorie

Gemini Robotics ER 2 może generować sekwencje punktów, które określają trajektorię, co jest przydatne do kierowania ruchem robota.

Ten przykład zawiera prośbę o wygenerowanie trajektorii, która pozwoli przenieść czerwony długopis do organizera, w tym oszacowanie pośrednich punktów trasy. Kod został skrócony, aby pokazać tylko prompt.

### Python

```
prompt = """
          Generate a trajectory for the robotic arm to pick up the red pen
          and place it in the organizer. Return a list of waypoints as JSON:
          [{"step": <int>, "point": [y, x], "action": <description>}, ...]
          where coordinates are normalized to 0-1000.
        """
```

## Tworzenie miejsca na laptopa

Ten przykład pokazuje, jak Gemini Robotics ER może wnioskować o przestrzeni. Prompt prosi model o określenie, który obiekt należy przesunąć, aby zrobić miejsce na inny element.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-with-objects.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Point to the object that I need to remove to make room for my laptop
          The answer should follow the JSON format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

Odpowiedź zawiera współrzędne 2D obiektu, który odpowiada na pytanie użytkownika, w tym przypadku obiektu, który powinien się przesunąć, aby zrobić miejsce na laptopa.

```
[
  {"point": [672, 301], "label": "The object that I need to remove to make room for my laptop"}
]
```

![Przykład pokazujący, który obiekt należy przenieść, aby inny obiekt](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png?hl=pl)

## Pakowanie lunchu

Model może też podawać instrukcje dotyczące zadań wieloetapowych i wskazywać odpowiednie obiekty na każdym etapie. Ten przykład pokazuje, jak model planuje serię czynności, aby spakować lunch.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('path/to/image-of-lunch.jpg', 'rb') as f:
    image_bytes = f.read()

prompt = """
          Explain how to pack the lunch box and lunch bag. Point to each
          object that you refer to. Each point should be in the format:
          [{"point": [y, x], "label": }], where the coordinates are
          normalized between 0-1000.
        """

image_response = client.models.generate_content(
  model="gemini-robotics-er-2-preview",
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    prompt
  ],
  config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(thinking_level="high")
  )
)

print(image_response.text)
```

Odpowiedzią na ten prompt jest zestaw instrukcji krok po kroku, jak spakować lunch na podstawie obrazu wejściowego.

**Obraz wejściowy**

![Obraz przedstawiający pojemnik na lunch i produkty, które można do niego włożyć](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png?hl=pl)

**Dane wyjściowe modelu**

```
Based on the image, here is a plan to pack the lunch box and lunch bag:

1.  **Pack the fruit into the lunch box.** Place the [apple](apple), [banana](banana), [red grapes](red grapes), and [green grapes](green grapes) into the [blue lunch box](blue lunch box).
2.  **Add the spoon to the lunch box.** Put the [blue spoon](blue spoon) inside the lunch box as well.
3.  **Close the lunch box.** Secure the lid on the [blue lunch box](blue lunch box).
4.  **Place the lunch box inside the lunch bag.** Put the closed [blue lunch box](blue lunch box) into the [brown lunch bag](brown lunch bag).
5.  **Pack the remaining items into the lunch bag.** Place the [blue snack bar](blue snack bar) and the [brown snack bar](brown snack bar) into the [brown lunch bag](brown lunch bag).

Here is the list of objects and their locations:
*   [{"point": [899, 440], "label": "apple"}]
*   [{"point": [814, 363], "label": "banana"}]
*   [{"point": [727, 470], "label": "red grapes"}]
*   [{"point": [675, 608], "label": "green grapes"}]
*   [{"point": [706, 529], "label": "blue lunch box"}]
*   [{"point": [864, 517], "label": "blue spoon"}]
*   [{"point": [499, 401], "label": "blue snack bar"}]
*   [{"point": [614, 705], "label": "brown snack bar"}]
*   [{"point": [448, 501], "label": "brown lunch bag"}]
```

## Co dalej?

- [Możliwości agentowe](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=pl) – wykonywanie kodu, odczytywanie instrumentów, dodawanie adnotacji do obrazów.
- [Orkiestracja zadań](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl) – zadania długoterminowe z niestandardowymi interfejsami API robotów.
- [Robotyka ze strumieniowaniem](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) – dwukierunkowe strumieniowanie w czasie rzeczywistym (tylko Gemini Robotics ER 2).
- [Rozumienie wideo](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl) – znajdowanie momentów i klasyfikacja postępów (tylko Gemini Robotics ER 2).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
