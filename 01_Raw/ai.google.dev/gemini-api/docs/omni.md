---
source_url: https://ai.google.dev/gemini-api/docs/omni?hl=pl
fetched_at: 2026-09-07T05:38:36.299446+00:00
title: "Generowanie i edytowanie film\u00f3w za pomoc\u0105 Gemini Omni Flash \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie i edytowanie filmów za pomocą Gemini Omni Flash

Gemini Omni Flash (`gemini-omni-1.1-flash`) to wydajny model multimodalny zaprojektowany z myślą o szybkim generowaniu i edytowaniu filmów oraz sterowaniu ich charakterem.
Gemini Omni ma te podstawowe funkcje, które odróżniają go od poprzednich modeli wideo:

- **Natywna multimodalność:** przetwarza tekst, obrazy, dźwięk i wideo jednocześnie, co zapewnia bardziej spójne, konsekwentne i kontrolowane dane wyjściowe.
- **Edytowanie w trybie konwersacyjnym:** umożliwia iteracyjne ulepszanie i edytowanie filmów za pomocą rozmowy w języku naturalnym. Jest dostępne dzięki [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl). Opisz, co chcesz zmienić, a model zastosuje zmiany, zachowując te części filmu, które chcesz pozostawić.
- **Wiedza o świecie:** Gemini Omni łączy zrozumienie fizyki z wiedzą Gemini o historii, nauce i kontekście kulturowym, wypełniając lukę między fotorealizmem a znaczącą narracją.

## Generowanie filmu na podstawie tekstu

Generowanie filmu na podstawie prompta tekstowego. Model generuje film z dźwiękiem na podstawie opisu tekstowego. Aby uzyskać jak najlepsze wyniki, pisz prompty zawierające szczegóły, takie jak opis sceny, ruch kamery, oświetlenie i nastrój.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A marble rolling fast on a chain reaction style track, continuous smooth shot."
)
with open("marble.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A marble rolling fast on a chain reaction style track, continuous smooth shot.',
});

if (interaction.output_video?.data) {
  fs.writeFileSync('marble.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A marble rolling fast on a chain reaction style track, continuous smooth shot."
}'
```

### Schemat odpowiedzi REST

Pole wygody `interaction.output_video` jest **dostępne tylko w pakiecie SDK**.
Pobierz dane wyjściowe wideo z tablicy `steps`, gdy używasz bezpośrednio interfejsu API REST.

**Nieprzetworzona struktura JSON REST:**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "AAAAIGZ0eXBpc29t..." // Base64 encoded video data
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

### Sterowanie formatem obrazu

Ustaw `aspect_ratio` na `"9:16"`, aby tworzyć filmy w orientacji pionowej. Domyślnie jest to orientacja pozioma (16:9).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A futuristic city with neon lights and flying cars, cyberpunk style",
    response_format={
        "type": "video",  # optional
        "aspect_ratio": "9:16"  # Supported values: "9:16", "16:9"
    }
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A futuristic city with neon lights and flying cars, cyberpunk style',
  response_format: {
    type: 'video', // optional
    aspect_ratio: '9:16' // Supported values: '9:16', '16:9'
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
 "response_format": {
   "type": "video",
   "aspect_ratio": "9:16"
 }
}'
```

### Rozdzielczość wyjściowa

Kontroluj rozdzielczość wyjściową wygenerowanego filmu za pomocą parametru `resolution` w `response_format`. Domyślna rozdzielczość to 720p.

| Wartość | Opis |
| --- | --- |
| `360p` | rozdzielczość wyjściowa 360p, |
| `720p` | rozdzielczość wyjściowa 720p (domyślna), |
| `1080p` | Wyjście 1080p (zwiększona rozdzielczość) |
| `4k` | Wyjście 4K (większa rozdzielczość) |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A drone shot of a mountain landscape at sunrise.",
    response_format={
        "type": "video",
        "resolution": "1080p",
    },
)
with open("hires.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A drone shot of a mountain landscape at sunrise.',
  response_format: {
    type: 'video',
    resolution: '1080p',
  },
});

if (interaction.output_video?.data) {
  fs.writeFileSync('hires.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A drone shot of a mountain landscape at sunrise.",
 "response_format": {
   "type": "video",
   "resolution": "1080p"
 }
}'
```

## Generowanie filmu na podstawie obrazu

Do prompta tekstowego możesz dodać obraz referencyjny. W zależności od prompta model zdecyduje, jak wykorzystać obraz. Jest to przydatne w przypadku zdjęć produktów, ilustracji lub fotografii.

Poniższy przykład pokazuje, jak użyć obrazu referencyjnego przedstawiającego rysunek ryby wyskakującej z wody:

![Rysunek ryby wyskakującej z wody](https://ai.google.dev/static/gemini-api/docs/images/fish-jumping-inputimage.png?hl=pl)

Wpisz ten prompt:

```
turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video
```

Aby wygenerować realistyczny film przedstawiający rysunek.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
)
with open("clownfish.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('clownfish.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$BASE64_IMAGE"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
 ]
}'
```

### Interpolacja pierwszej i ostatniej klatki

Gemini Omni Flash obsługuje interpolację wideo, co umożliwia generowanie filmów, które płynnie przechodzą od obrazu początkowego (pierwszej klatki) do obrazu końcowego (ostatniej klatki).

Podaj 2 obrazy na liście `input` i opisz w prompcie pożądane przejście. Model animuje scenę od pierwszej do ostatniej klatki.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": first_frame_b64, "mime_type": "image/jpeg"},
        {"type": "image", "data": last_frame_b64, "mime_type": "image/jpeg"},
        {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
    ],
)
with open("interpolation.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: firstFrameB64, mime_type: 'image/jpeg' },
    { type: 'image', data: lastFrameB64, mime_type: 'image/jpeg' },
    { type: 'text', text: 'A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('interpolation.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$FIRST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "image", "data": "'"$LAST_FRAME_B64"'", "mime_type": "image/jpeg"},
   {"type": "text", "text": "A smooth cinematic transition from a lush green forest at sunrise to a snowy forest under a starry night sky."}
 ]
}'
```

### Odniesienie do obiektu

Możesz wygenerować film z określonymi obiektami podanymi jako obrazy referencyjne.
Na przykład poniższy kod pokazuje, jak podać 2 obrazy kota i włóczki, aby wygenerować film przedstawiający kota bawiącego się włóczką.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": cat_b64, "mime_type": "image/png"},
        {"type": "image", "data": yarn_b64, "mime_type": "image/png"},
        {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
    ],
)
with open("cat.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: catData, mime_type: 'image/png' },
    { type: 'image', data: yarnData, mime_type: 'image/png' },
    { type: 'text', text: 'A cat playfully batting at a ball of yarn.' }
  ]
});

if (interaction.output_video?.data) {
  fs.writeFileSync('cat.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "image", "data": "'"$CAT_B64"'", "mime_type": "image/png"},
   {"type": "image", "data": "'"$YARN_B64"'", "mime_type": "image/png"},
   {"type": "text", "text": "A cat playfully batting at a ball of yarn."}
 ]
}'
```

### Parametr zadań

Użyj parametru `task` w `video_config`, aby wyraźnie określić zamierzone działanie. Jeśli na przykład chcesz, aby model wygenerował film na podstawie obrazu, możesz ustawić parametr na `image_to_video`. Jeśli nie zostanie ustawiona, model wywnioskuje, czego oczekujesz, na podstawie promptu.

Dozwolone wartości:

- `text_to_video`
- `image_to_video`
- `reference_to_video`
- `edit`
- `extend`

Poniższy przykład pokazuje, jak ustawić tę wartość w przypadku przedstawionego wcześniej przykładu obrazu do filmu.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": base64_image, "mime_type": "image/jpeg"},
        {"type": "text", "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"}
    ],
    generation_config={
      "video_config": {
        "task": "image_to_video",
      }
    },
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';
const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'image', data: base64Image, mime_type: 'image/jpeg' },
    { type: 'text', text: 'turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video' }
  ],
  generationConfig: {
    videoConfig: {
      task: 'image_to_video',
    }
  }
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-omni-1.1-flash",
    "input": [
      {
        "type": "image",
        "data": "'"$BASE64_IMAGE"'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "text",
        "text": "turn this into realistic footage, using the drawing only as a guide for movement, do not show the drawing in the final video"
      }
    ],
    "generation_config": {
      "video_config": {
        "task": "image_to_video"
      }
    }
  }'
```

## Edytowanie filmów z zachowaniem stanu

Generuj film i edytuj go iteracyjnie za pomocą dodatkowych promptów. Każda tura
bazuje na poprzednim wyniku. Model zapamiętuje kontekst filmu i stosuje zmiany, zachowując elementy, o których nie wspominasz. Użyj `previous_interaction_id`, aby śledzić historię rozmowy i stan wygenerowanego filmu bez ponownego przesyłania poprzedniego filmu.

Ten przykład pokazuje, jak wygenerować pierwszy film, a potem go edytować:

### Python

```
import base64
from google import genai

client = genai.Client()

# Turn 1: Generate initial video
res1 = client.interactions.create(model="gemini-omni-1.1-flash", input="A woman playing violin outdoors.")

# Turn 2: Edit the previous video
res2 = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=res1.id,
    input="Make the violin invisible."
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(res2.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Turn 1: Generate initial video
const res1 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A woman playing violin outdoors.',
});

// Turn 2: Edit the previous video
const res2 = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  previous_interaction_id: res1.id,
  input: 'Make the violin invisible.',
});

if (res2.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(res2.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "previous_interaction_id": "'"$PREVIOUS_ID"'",
 "input": "Make the violin invisible."
}'
```

Przykład początkowego filmu:

Przykład edytowanego filmu:

Każda tura rozmowy generuje nowy film. Model rozumie kontekst z poprzednich tur, co pozwala wprowadzać stopniowe zmiany, takie jak dostosowywanie oświetlenia czy zamiana tła, bez konieczności ponownego opisywania całej sceny.

### Edytowanie własnych filmów

Prześlij filmy za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl), aby je edytować za pomocą Gemini Omni Flash.

Poniższy przykład pokazuje, jak edytować ten oryginalny film:

### Python

```
import time
import base64
from google import genai

client = genai.Client()

# Upload video using the file API
video_file = client.files.upload(file="Video.mp4")

while video_file.state == "PROCESSING":
    print('Waiting for video to be processed.')
    time.sleep(10)
    video_file = client.files.get(name=video_file.name)

if video_file.state == "FAILED":
  raise ValueError(video_file.state)
print(f'Video processing complete: ' + video_file.uri)

# Edit your video
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"}
    ],
)
with open("example.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload video using the file API
let videoFile = await ai.files.upload({
  file: 'Video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  console.log('Waiting for video to be processed.');
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

if (videoFile.state === 'FAILED') {
  throw new Error(videoFile.state);
}
console.log('Video processing complete: ' + videoFile.uri);

// Edit your video
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material" }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('example.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
#!/bin/bash
VIDEO_B64=$(encode_file "$VIDEO_FILE")

curl -sS -w "\n[HTTP %{http_code}]\n" "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d @- <<EOF > video_editing_response.json
{
  "model": "gemini-omni-1.1-flash",
  "input": [
    {
      "type": "user_input",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "data": "$VIDEO_B64"
        },
        {
          "type": "text",
          "text": "When the person touches the mirror, make the mirror ripple beautifully like liquid, and the person's arm turns into reflective mirror material"
        }
      ]
    }
  ],
  "response_format": { "type": "video" }
}
EOF
```

Przykład edytowanego filmu:

## Pobieranie filmów za pomocą identyfikatora URI

Użyj parametru `delivery="uri"` w `response_format`, aby pobrać wygenerowane filmy o rozmiarze większym niż 4 MB.
Zwraca to adres URI hostowany przez Google, który możesz sprawdzać, dopóki film nie będzie `ACTIVE` przed pobraniem.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Request video via URI delivery
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A beautiful sunset.",
    response_format={"type": "video", "delivery": "uri"}
)

# 2. Extract file name and poll for ACTIVE state
video_output = interaction.output_video
file_name = video_output.uri.split("/")[-1] # Extract ID

print("Waiting for video processing...")
while True:
    f_info = client.files.get(name=f"files/{file_name}")
    if f_info.state.name == "ACTIVE":
        break
    elif f_info.state.name == "FAILED":
        raise RuntimeError("Generation failed.")
    time.sleep(5)

# 3. Download the final video
client.files.download(file=video_output.uri, destination="output.mp4")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});

// 1. Request video via URI delivery
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: 'A beautiful sunset.',
  response_format: { type: 'video', delivery: 'uri' },
});

// 2. Extract file name and poll for ACTIVE state
const videoOutput = interaction.output_video;
const fileId = videoOutput.uri.match(/files\/([a-zA-Z0-9]+)/)[1];
const name = `files/${fileId}`;

console.log("Waiting for video processing...");
while (true) {
  const fInfo = await ai.files.get({ name });
  if (fInfo.state.name === 'ACTIVE') break;
  if (fInfo.state.name === 'FAILED') throw new Error("Generation failed.");
  await new Promise(r => setTimeout(r, 5000));
}

// 3. Download the final video
await ai.files.download({
  file: videoOutput,
  downloadPath: 'output.mp4',
});
console.log("💾 Saved video to output.mp4");
```

### REST

```
#!/bin/bash

# 1. Initial request to generate the video
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY" \
-H "Content-Type: application/json" \
-d '{
 "model": "gemini-omni-1.1-flash",
 "input": "A beautiful sunset over a calm ocean.",
 "response_format": {"type": "video", "delivery": "uri"}
}')

# Extract FILE_ID from the URI (e.g., "files/abc-123" -> "abc-123")
FILE_URI=$(echo $RESPONSE | jq -r '.output_video.uri')
FILE_ID=$(echo $FILE_URI | cut -d'/' -f2)

echo "Video requested (ID: $FILE_ID). Waiting for processing..."

# 2. Polling loop
while true; do
 # Get current file status
 STATUS_JSON=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID?key=$API_KEY")
 STATE=$(echo $STATUS_JSON | jq -r '.state')

 if [ "$STATE" == "ACTIVE" ]; then
   echo "Processing complete! Downloading..."
   break
 elif [ "$STATE" == "FAILED" ]; then
   echo "Error: Generation failed."
   exit 1
 else
   echo "Current state: $STATE... (waiting 5s)"
   sleep 5
 fi
done

# 3. Final download
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/$FILE_ID:download?alt=media&key=$API_KEY" \
--output "output.mp4"

echo "Done! Video saved to output.mp4"
```

**Nieprzetworzona struktura JSON REST (URI):**

```
{
  "steps": [
    { "type": "user_input", "content": [{"type": "text", "text": "..."}] },
    { "type": "thought", "content": [{"text": "...", "type": "thought"}] },
    {
      "type": "model_output",
      "content": [
        {
          "type": "video",
          "mime_type": "video/mp4",
          "uri": "https://generativelanguage.googleapis.com/v1beta/files/...:download?alt=media"
        }
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

## Rozszerzenie wideo

Wydłużanie istniejącego filmu przez wygenerowanie płynnej kontynuacji na końcu klipu. W prompcie opisz, jak ma się rozwijać film, np. `"Extend this video"` lub `"Continue the scene: the camera pans across the mountains"`.
Model analizuje film wejściowy, aby wygenerować jego kontynuację trwającą 3–10 sekund.

Możesz przedłużyć:

- **Filmy wygenerowane przez model (wieloetapowe):** przedłuż wcześniej wygenerowany film, odwołując się do jego `previous_interaction_id`.
- **Przesłane filmy:** podaj przesłany plik wideo (za pomocą interfejsu Files API) wraz z promptem do rozszerzenia.

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload your video using the Files API
video_file = client.files.upload(file="my_video.mp4")

# Extend the video using prompt-based extension
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "text", "text": "Continue the scene."}
    ],
)
with open("extended.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload your video using the Files API
let videoFile = await ai.files.upload({
  file: 'my_video.mp4',
});

while (videoFile.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Extend the video using prompt-based extension
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'text', text: 'Continue the scene.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'"$VIDEO_URI"'"},
   {"type": "text", "text": "Continue the scene."}
 ]
}'
```

### Rozszerzanie za pomocą multimediów referencyjnych

Obrazy referencyjne możesz podać w tablicy `input` wraz z promptem, aby wprowadzić do dłuższego filmu nowe postacie lub elementy:

### Python

```
import base64
from google import genai

client = genai.Client()

# Upload base video and reference image using the Files API
video_file = client.files.upload(file="my_video.mp4")
character_img = client.files.upload(file="character.png")

# Extend the video while introducing the reference character
interaction = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "document", "uri": video_file.uri},
        {"type": "document", "uri": character_img.uri},
        {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
    ],
)
with open("extended_with_character.mp4", "wb") as f:
    f.write(base64.b64decode(interaction.output_video.data))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
const ai = new GoogleGenAI({});

// Upload base video and reference image using the Files API
let videoFile = await ai.files.upload({ file: 'my_video.mp4' });
let characterImg = await ai.files.upload({ file: 'character.png' });

while (videoFile.state === 'PROCESSING' || characterImg.state === 'PROCESSING') {
  await new Promise(r => setTimeout(r, 10000));
  videoFile = await ai.files.get({ name: videoFile.name });
  characterImg = await ai.files.get({ name: characterImg.name });
}

// Extend the video while introducing the reference character
const interaction = await ai.interactions.create({
  model: 'gemini-omni-1.1-flash',
  input: [
    { type: 'document', uri: videoFile.uri },
    { type: 'document', uri: characterImg.uri },
    { type: 'text', text: 'Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave.' }
  ],
});

if (interaction.output_video?.data) {
  fs.writeFileSync('extended_with_character.mp4', Buffer.from(interaction.output_video.data, 'base64'));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?key=$API_KEY"     -H "Content-Type: application/json"     -d '{
 "model": "gemini-omni-1.1-flash",
 "input": [
   {"type": "document", "uri": "'$VIDEO_URI'"},
   {"type": "document", "uri": "'$CHARACTER_IMG_URI'"},
   {"type": "text", "text": "Extend this video: have the character shown in <IMAGE_REF_0> enter the scene and wave."}
 ]
}'
```

### Ograniczenia i wytyczne dotyczące rozszerzeń

Podczas wydłużania filmów pamiętaj o tych zasadach i ograniczeniach:

- **Wypowiadane dialogi w przesłanych filmach:** obecnie nie możesz wydłużyć przesłanego filmu, w którym ktoś mówi, aby dodać dodatkowy dialog (jest to obsługiwane, jeśli postać milczy lub jeśli prompt nie dodaje dialogu).
- **Rozszerzenie głosowe z wieloma turami:** generowanie mówionego dialogu lub mowy jest obsługiwane podczas rozszerzania wcześniej wygenerowanych filmów za pomocą funkcji wieloturnowej (`previous_interaction_id`).
- **Tylko na końcu klipu:** rozszerzenie jest ograniczone do dodawania na końcu filmu.
  Nie możesz dodawać treści na początku ani wydłużać środka klipu.
- **Ograniczenie czasu trwania:** przesyłane filmy do rozszerzenia muszą mieć długość nie większą niż 10 sekund (chyba że używasz wieloetapowych odpowiedzi).
- **Dostępność w poszczególnych regionach:** wydłużanie przesłanych filmów nie jest obecnie dostępne dla użytkowników z Europejskiego Obszaru Gospodarczego (EOG), Szwajcarii i Wielkiej Brytanii (wydłużanie filmów wygenerowanych przez model jest obsługiwane we wszystkich dostępnych regionach).

## Sprawdzone metody

- **Używaj dostarczania URI w przypadku dużych filmów:** w przypadku filmów większych niż 4 MB (w razie dostępności – >720p) używaj `delivery="uri"` w `response_format`, aby uniknąć limitów rozmiaru ładunku.
- **Zoptymalizowana wydajność:** ustaw `background=false`, `store=false` i `stream=false`, aby uzyskać szybsze, synchroniczne generowanie pojedynczych odpowiedzi. Pamiętaj, że ustawienie
  `store=false` oznacza, że wygenerowanego filmu nie będzie można edytować w kolejnych
  rundach za pomocą `previous_interaction_id`.
- **Precyzja promptu:** szczegółowe informacje znajdziesz w sekcji [wskazówki dotyczące promptów](#prompt-guide).

## Ograniczenia

- Przesyłanie i edytowanie obrazów przedstawiających osoby niepełnoletnie nie jest obsługiwane w Europejskim Obszarze Gospodarczym, Szwajcarii i Wielkiej Brytanii.
- Przesyłanie i edytowanie obrazów przedstawiających niektóre rozpoznawalne osoby nie jest obsługiwane.
- Edytowanie lub wydłużanie przesłanych filmów nie jest obecnie dostępne dla użytkowników z Europejskiego Obszaru Gospodarczego (EOG), Szwajcarii i Wielkiej Brytanii (edytowanie i wydłużanie filmów wygenerowanych przez model jest obsługiwane).
- Filmy wejściowe do edycji i rozszerzania muszą mieć podczas przesyłania długość maksymalnie 10 sekund (chyba że rozszerzasz filmy wygenerowane przez model w ramach wieloetapowej konwersacji).
- Rozszerzenie wideo można dodać tylko na końcu filmu. Dodawanie na początku lub w środku klipu nie jest obsługiwane.
- Nie możesz wydłużyć przesłanego filmu, w którym ktoś mówi, aby dodać dodatkowe dialogi (postacie mogą milczeć lub można użyć wieloetapowego rozszerzenia z `previous_interaction_id`).
- Edytowanie głosem nie jest obsługiwane.
- Przesyłanie referencji audio nie jest obsługiwane w bieżącej wersji interfejsu API.
- Referencje wideo najlepiej sprawdzają się w przypadku podobieństw. Dźwięk w referencji wideo jest ignorowany. Filmy referencyjne mogą zawierać maksymalnie 3 klipy, z których każdy może trwać do 3 sekund.
- Odwoływanie się do wielu filmów lub wyciąganie z nich wniosków nie jest obsługiwane. Próba użycia promptów z wieloma filmami może spowodować pogorszenie wydajności modelu lub nieoczekiwane wyniki.
- Udostępniona przepustowość nieobsługiwany.
- Instrukcje systemowe, temperatura, `top_p`, sekwencje zatrzymania i negatywne prompty nie są obsługiwane (negatywne prompty możesz umieścić w zwykłym prompcie, np. „Nie rób X”).
- Używanie filmów z YouTube jako źródła multimediów nie jest obsługiwane.

## Szczegóły techniczne

- Wszystkie wygenerowane filmy zawierają znak wodny SynthID, który jest niewidoczny dla widzów, ale można go wykryć programowo w celu weryfikacji pochodzenia.
- Czas generowania filmów zależy od ich długości, rozdzielczości i bieżącego obciążenia interfejsu API. Generowanie dłuższych filmów w wyższej rozdzielczości zajmuje więcej czasu.
- Omni stosuje filtry bezpieczeństwa treści zarówno do promptów wejściowych, jak i wygenerowanych filmów (różnią się one w zależności od regionu). Prompty, które naruszają zasady użytkowania, są blokowane.
- Język angielski jest w pełni obsługiwany, ale inne języki nie zostały jeszcze ocenione, więc mogą działać, ale wyniki mogą się różnić.

## Przewodnik po tworzeniu promptów w Gemini Omni Flash

W tej sekcji znajdziesz wskazówki i przykłady dotyczące skutecznego promptowania Gemini Omni Flash.

### Pojedyncza scena

Domyślnie Omni Flash spróbuje utworzyć film z kilkoma różnymi ujęciami.
Spróbuje stworzyć ciekawą opowieść na podstawie promptu.

Jeśli chcesz, aby wygenerowany film zawierał tylko jedną scenę, musisz to określić w prompcie:

- w jednej nieprzerwanej scenie,
- w jednym ciągłym ujęciu.
- Brak cięć scen

Na przykład:

```
Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.
```

### Usuwanie niechcianych elementów

Jeśli wygenerowany film zawiera elementy, których nie chcesz, użyj prostych negatywnych promptów, aby ich uniknąć:

- Brak dialogów
- Bez ozdób
- Brak dodatkowych efektów dźwiękowych

### Prompty do edycji

W przypadku edycji wideo najlepiej sprawdzają się proste prompty. Zbyt szczegółowe prompty mogą prowadzić do niezamierzonych zmian.

Oto więcej przykładów prostych promptów do edycji:

- Przekształć ten film w anime
- Załóż tej osobie modny kapelusz
- Zmień oświetlenie, aby było bardziej dramatyczne
- Zmień tekst na znaku na „Omni Flash”

Podczas edytowania konkretnego aspektu filmu dodaj `"Keep everything else the same"`, aby zachować spójność wizualną.

Oto kilka przykładów, które pokazują, jak zastosować tę technikę:

- **Czego unikać:** `In the video of the man sitting on the sofa, please add a small
  black cat that runs from the right side of the screen, jumps onto his lap,
  and then he starts to stroke its head while looking down.`
  - **Uprość:** `Add a cat that jumps onto his lap, he begins to pet it.
    Keep everything else the same.`
- **Czego unikać:** `Please remove the cell phone that the person is holding in
  their hand and fill in the background so it looks like they are just holding
  their hand empty.`
  - **Uprość:** `Make the phone invisible. Keep everything else the
    same.`

### Promptowanie dźwięku

Domyślnie model będzie próbował wygenerować odpowiednią ścieżkę dźwiękową do filmu. Nie zawsze jest to pożądane. W prompcie możesz opisać typ dźwięku, który chcesz uzyskać. Jest to szczególnie ważne, jeśli chcesz użyć w filmie muzyki:

- Dodaj spokojną muzykę w tle
- Film ma energetyczny beat techno
- W tle słychać cichą, metaliczną audycję radiową z odtwarzaną piosenką.

### Zdarzenia związane z czasem

Możesz poprosić o wykonanie określonych czynności w określonych momentach filmu. Nie musisz używać precyzyjnej składni, możesz używać języka naturalnego. Jest to szczególnie przydatne przy tworzeniu własnych cięć scen, rytmu lub szybkich sekwencji.
Przykłady znajdziesz poniżej:

- Po 3 sekundach na scenie pojawia się kobieta.
- W 5 sekundzie w tle zaczyna się refren.
- Co 2 sekundy przełączanie na nową klatkę.
- W sekwencji szybkiego ognia co pół sekundy (12 klatek przy 24 kl./s) zmieniaj scenę na nową lokalizację.

Możesz też użyć składni kodu czasowego:

```
[0-3s] A person is walking
[3-6s] They stop and turn around
[6-10s] They start running
```

### Tworzenie metapromptów

Możesz poprosić Gemini Omni Flash o zwrócenie uwagi na ogólne cechy lub zasady generowania filmów:

- Zwróć uwagę na mikrodetale, wyraz i timing, aby stworzyć bardzo bogatą w szczegóły, ale całkowicie naturalną scenę.
- Opisuj postacie i środowiska bardzo szczegółowo.
  Stosuj zasady projektowania kostiumów do postaci. Opisz dokładnie osoby, przedmioty i obiekty na scenie.
- Dodaj do elementów tła wiele odpowiednich szczegółów, aby scena wyglądała realistycznie i naturalnie.
- Utwórz film z szybko zmieniającymi się ujęciami, w którym co sekundę pojawia się inny rzadki `[thing]`. Dodaj do niego wesołą muzykę i tekst z nazwą obiektu.

### Tekst w filmach

Możesz poprosić o uwzględnienie tekstu w filmie, a Gemini Omni wyrenderuje go w prawidłowy i czytelny sposób. Jeśli w filmie pojawi się tekst, nawet w elementach tła, warto określić, co ma on zawierać.

- Po jednym słowie na ekranie: „czy, wiesz, że, Omni, potrafi, tworzyć, świetne, teksty?” Każde słowo pojawia się na sekundę w innym stylu animacji. Brak dialogów.
- Na znaku drogowym widnieje napis: „This is an AI generation by Omni” (To obraz wygenerowany przez AI od Omni), na fasadzie sklepu jest napis: „All you need AI” (AI, której potrzebujesz), a na tablicy rejestracyjnej samochodu widnieje napis: „OMNI1.1”.

### Prompty do wydłużania filmu

Dzięki Gemini Omni 1.1 Flash możesz wydłużać filmy za pomocą promptów takich jak `"Extend this video"` lub `"The scene continues"`. Możesz wydłużyć filmy o 10 sekund, do łącznej długości 40 sekund.

Omni tworzy rozszerzenie, które zachowuje spójność filmu, ruchu, postaci i dźwięku, wykorzystując jako kontekst ostatnie 10 sekund oryginalnego filmu. Niektóre z ostatnich klatek filmu wejściowego zostaną zmodyfikowane, aby przejście było płynne.

Podczas rozszerzania nadal obowiązują wszystkie wskazówki dotyczące promptów Omni z tego przewodnika:

- Opisz dźwięk w rozszerzonej scenie, zwłaszcza jeśli chcesz go zmienić: `"The music continues into the chorus"`
- Opisz, czy scena jest kontynuowana, czy następuje cięcie do nowej sceny (być może z tymi samymi postaciami): `"Show the same characters in the next scene"`
- Dołączaj obrazy i filmy jako materiały referencyjne, aby zwiększyć dokładność wyników lub wprowadzić nowe postacie: `"The person shown in the reference image enters the scene"`, `"The dog in the reference video <VIDEO_REF_0> jumps onto the sofa"`
- Jeśli używasz sygnatur czasowych lub składni kodu czasowego, 0s odnosi się do początku rozszerzonej części filmu. Jeśli przedłużasz 10-sekundowy film, cięcie sceny w tym prompcie nastąpi po 12 sekundach: `"After 2s cut to a new scene with the same characters"`

### Używanie tagów w promptach do określania ról obrazów i filmów

Za pomocą tagów możesz powiązać przesłane multimedia z określonymi rolami generowania. Dzięki temu możesz określić, czy każdy obraz lub film jest klatką początkową, klatką końcową czy odniesieniem.

#### 1. Proste tagi (zalecane)

W prostych przypadkach, gdy role multimediów są jasne na podstawie prompta, możesz bezpośrednio przypisywać obrazy i filmy do ról:

- **`<FIRST_FRAME>`**: użyj obrazu jako klatki początkowej filmu, np. `<FIRST_FRAME> a woman is walking`
- **`<LAST_FRAME>`**: użyj obrazu jako ostatniej klatki filmu, do której nastąpi przejście. Musi być używany z parametrem `<FIRST_FRAME>`, np. `<FIRST_FRAME> <LAST_FRAME> a woman is walking`
- **`<IMAGE_REF_N>`**: użyj obrazu jako odniesienia, np. `in the
  style of <IMAGE_REF_0> a woman <IMAGE_REF_1> is walking` (łączy odniesienie do stylu z pierwszego obrazu i odniesienie do obiektu z drugiego obrazu).
  Odwołania do obrazów zaczynają się od 0.
- **`<VIDEO_REF_N>`**: używać filmu jako odniesienia do postaci lub obiektu, np.`the person in <VIDEO_REF_0> is playing the violin`. Wartości odniesień do filmów również zaczynają się od 0.

Oto przykład z 6 obrazami referencyjnymi:

```
[0-3s] A studio fashion sequence. Starting with woman <IMAGE_REF_0>, she is holding <IMAGE_REF_1>
[3-6s] Then we see the man <IMAGE_REF_2> holding <IMAGE_REF_3>
[6-10s] And finally another woman <IMAGE_REF_4> who is holding <IMAGE_REF_5> while walking.
```

#### 2. Deklarowanie źródeł i odwołań

W bardziej złożonych przypadkach, w których występuje wiele danych wejściowych multimediów i wiele ról, możesz używać jawnych tagów prefiksów w połączeniu z instrukcjami w języku naturalnym. Na początku prompta należy zadeklarować te źródła i odniesienia.

- `[# Sources <FIRST_FRAME>@Image1]` użyje pierwszego obrazu jako klatki początkowej.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]` użyje pierwszego obrazu jako klatki początkowej, a drugiego jako klatki końcowej.
- `[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]` użyje pierwszego obrazu jako pierwszej i ostatniej klatki, tworząc film, który będzie się zapętlać.
- `[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` użyje pierwszego obrazu jako klatki początkowej, a drugiego jako obrazu referencyjnego.
- `[# Sources <VIDEO_0>@Video1]` użyje filmu jako głównego źródła do edycji lub modyfikacji.
- `[# Sources <PREVIOUS_VIDEO>@Video1]` użyje filmu z poprzedniej tury, aby go przedłużyć.
- `[# References <IMAGE_REF_0>@Image1]` użyje pierwszego obrazu jako odniesienia.
- `[# References <IMAGE_REF_1>@Image2]` użyje drugiego obrazu jako referencyjnego.
- `[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]` użyje obu obrazów jako przykładów.
- `[# References <VIDEO_REF_0>@Video1]` użyje pierwszego filmu jako referencyjnego.
- `[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]` użyje zarówno obrazu, jak i filmu jako materiałów referencyjnych.

Dodaj instrukcje na końcu prompta:

- W przypadku klatki początkowej: `"Use this image as the starting frame."`
- W przypadku zapętlonego filmu za pomocą klatek początkowej i końcowej: `"Use this image as the first frame and the last frame."`
- W przypadku obrazów referencyjnych: `"Use the given image(s) as references for video generation. The images should not be used as literal initial frames."`
- W przypadku filmów referencyjnych: `"Use the given video(s) as references. Do not use them as a source for video editing."`

Przykłady promptów z deklaracjami źródła i referencji:

**Klatka początkowa połączona z obrazem referencyjnym:**

```
[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2] a woman <IMAGE_REF_0> is walking. Use Image1 as the starting frame. Use Image2 as a reference for the video generation.
```

**Film referencyjny z postacią połączony z obrazem referencyjnym obiektu:**

```
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1] The woman in <VIDEO_REF_0> is playing the violin shown in <IMAGE_REF_0>. Use Video1 as a character reference and Image1 as an object reference.
```

## Co dalej?

- Zacznij korzystać z Gemini Omni Flash, eksperymentując w [Omni Quickstart Colab](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Omni.ipynb?hl=pl).
- Dowiedz się, jak pisać jeszcze lepsze prompty, korzystając z naszego [wprowadzenia do projektowania promptów](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-30 UTC."],[],[]]
