---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=de
fetched_at: 2026-10-19T05:33:17.652264+00:00
title: "Videos verstehen \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Videos verstehen

> Informationen zur Videogenerierung finden Sie im Leitfaden zu [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=de).

Gemini-Modelle können Videos verarbeiten und ermöglichen so viele neue Anwendungsfälle für Entwickler, für die in der Vergangenheit domänenspezifische Modelle erforderlich gewesen wären.
Zu den Vision-Funktionen von Gemini gehören die Möglichkeit, Videos zu beschreiben, zu segmentieren und Informationen daraus zu extrahieren, Fragen zu Videoinhalten zu beantworten und auf bestimmte Zeitstempel in einem Video zu verweisen.

Sie können Videos auf folgende Weise als Eingabe für Gemini bereitstellen:

| Eingabemethode | Max. Größe | Empfohlener Anwendungsfall |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (kostenpflichtig) / 2 GB (kostenlos) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), wiederverwendbare Dateien |
| [Cloud Storage-Registrierung](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de#registration) | 2 GB (pro Datei, keine Speicherlimits) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), dauerhafte, wiederverwendbare Dateien |
| [Inline-Daten](#inline-video) | unter 100 MB | Kleine Dateien (unter 100 MB), kurze Dauer (unter 1 Minute), einmalige Eingaben |
| [YouTube-URLs](#youtube) | – | Öffentliche YouTube-Videos |

> **Hinweis:** Die [File API](#upload-video) wird für die meisten Anwendungsfälle empfohlen, insbesondere für Dateien, die größer als 100 MB sind, oder wenn Sie die Datei in mehreren Anfragen wiederverwenden möchten.

Informationen zu anderen Methoden für die Dateieingabe, z. B. die Verwendung externer URLs oder in Google Cloud gespeicherter Dateien, finden Sie im
[Leitfaden zu Methoden für die Dateieingabe](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

### Videodatei hochladen

Der folgende Code lädt ein Beispielvideo herunter, lädt es mit der [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de),
wartet, bis es verarbeitet wurde, und verwendet dann die hochgeladene Dateireferenz, um
das Video zusammenzufassen.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Ok

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Um die Tokeneffizienz und -leistung zu optimieren, sollten Sie die
[agentische Videoverarbeitung](#agentic-video-understanding) verwenden.

Verwenden Sie immer die Files API, wenn die Gesamtgröße der Anfrage (einschließlich Datei, Text-Prompt, Systemanweisungen usw.) größer als 20 MB ist, die Videodauer erheblich ist oder wenn Sie dasselbe Video in mehreren Prompts verwenden möchten.
Die File API akzeptiert Videodateiformate direkt.

Weitere Informationen zum Arbeiten mit Mediendateien finden Sie unter
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=de).

### Videodaten inline übergeben

Anstatt eine Videodatei mit der File API hochzuladen, können Sie kleinere Videos direkt in der Anfrage an `generateContent` übergeben. Dies ist für kürzere Videos mit einer Gesamtgröße von weniger als 20 MB geeignet.

Hier ein Beispiel für die Bereitstellung von Inline-Videodaten:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### YouTube-URLs übergeben

Sie können YouTube-URLs wie folgt direkt als Teil Ihrer Anfrage an die Gemini API übergeben:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: contents,
});
console.log(response.text);
```

### Ok

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.8-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Beschränkungen** :

- In der kostenlosen Stufe können Sie pro Tag maximal 8 Stunden YouTube-Video hochladen.
- Im kostenpflichtigen Abo gibt es kein Limit basierend auf der Videolänge.
- Bei Modellen vor Gemini 2.5 können Sie pro Anfrage nur ein Video hochladen. Bei Gemini 2.5 und neueren Modellen können Sie pro Anfrage maximal 10 Videos hochladen.
- Sie können nur öffentliche Videos hochladen (keine privaten oder nicht gelisteten Videos).

## Agentisches Videoverständnis

Standardmäßig wird bei Videoeingaben eine statische Verarbeitung (Extrahieren von Frames mit 1 FPS) für alle Modelle verwendet, einschließlich Gemini 4.
Die Modelle Gemini 4 Argon, 3.8 Flash, 3.6 Flash und 3.5 Flash Lite unterstützen auch
**agentisches Videoverständnis**, einen optionalen Modus, in dem das Modell die Video
zeitachse dynamisch untersucht, Transkripte selektiv prüft und Frame
raten und Auflösung basierend auf dem Prompt im laufenden Betrieb anpasst.

| **Modus** | **Beschreibung** | **Unterstützte Modelle** |
| --- | --- | --- |
| **Statisch** (Standard) | Extrahiert Frames mit einer festen Rate (1 FPS) und platziert sie in einem Durchgang in den Kontext. Standard für alle Gemini-Modelle, einschließlich Gemini 4. | Alle Gemini-Modelle |
| **Agentisch** | Das Modell navigiert dynamisch durch die Videozeitachse und lädt nur die Inhalte, die basierend auf dem Prompt benötigt werden. Bis zu 88% tokeneffizienter und ~7% höhere Qualität bei Inhalten im Langformat. | Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite |

### Verarbeitungsmodus auswählen

Wählen Sie den Verarbeitungsmodus aus, der Ihrer Videolänge und Ihrem Abfragetyp entspricht:

- **Statisch (Standard)** : Am besten geeignet für kurze Clips (unter 5 Minuten), umfassende Zusammenfassungen des gesamten Videos, bei denen die gesamte Aufnahme relevant ist, latenzempfindliche Abfragen oder Präzision auf Frame-Ebene im gesamten Clip. Bei kurzen Videos oder umfassenden Prompts, bei denen der Großteil des Videos geprüft werden muss, vermeidet die statische Verarbeitung die zusätzlichen Denk-Tokens (`thoughts_token_count`) und Tool-Aufruf-Roundtrips (`tool_use_prompt_token_count`), die durch die Zeitachsen-Navigation entstehen.
- **Agentisch**:Am besten geeignet für Videos im Langformat (über 5–10 Minuten), die Suche nach der Nadel im Heuhaufen oder Abfragen, die auf bestimmte Momente oder Themen abzielen. Das Modell prüft zuerst die Transkripte und lädt nur relevante visuelle Segmente bei Bedarf, wodurch die Tokennutzung für die Videoeingabe um bis zu 88% reduziert wird, ohne das Kontextfenster zu füllen.

> **Hinweis**:Bei langen Videos oder komplexen Prompts, bei denen die agentische Verarbeitung mehr Zeit in Anspruch nimmt, verwenden Sie Streaming (`client.models.generate_content_stream`). Dadurch bleibt die Verbindung aktiv, es werden Zwischenschritte der Problemlösung angezeigt und Zeitüberschreitungen bei der Verbindung oder Authentifizierung werden vermieden.

### Verarbeitungsmodus festlegen

### Python

```
import time
from google import genai
from google.genai import types

client = genai.Client()

video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=video_file.uri,
            mime_type=video_file.mime_type,
            media_processing="AGENTIC",
        ),
        "What are the three main arguments presented?",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" },
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: videoFile.uri,
            mimeType: videoFile.mimeType,
          },
          mediaProcessing: "AGENTIC",
        },
        { text: "What are the three main arguments presented?" },
      ],
    },
  ],
});
console.log(response.text);
```

### Ok

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/lecture.mp4", nil)
parts := []*genai.Part{
    {
        FileData: &genai.FileData{
            FileURI:  uploadedFile.URI,
            MIMEType: uploadedFile.MIMEType,
        },
        MediaProcessing: genai.MediaProcessingAgentic,
    },
    genai.NewPartFromText("What are the three main arguments presented?"),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    contents,
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${file_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {"text": "What are the three main arguments presented?"}
      ]
    }]
  }'
```

> **Hinweis**:Um zu prüfen, ob die agentische Verarbeitung verwendet wurde, sehen Sie sich `response.candidates[0].content.parts` an. Das Vorhandensein von `tool_call`- und `tool_response`-Teilen mit dem Tooltyp `MEDIA_PROCESSING` zeigt an, dass das Modell dynamisch durch das Video navigiert hat.

> **Hinweis**:Im Gegensatz zu anderen serverseitigen Tools (z. B. Google Suche oder URL-Kontext) ist bei der agentischen Videoverarbeitung nicht erforderlich, `include_server_side_tool_invocations=True` in `ToolConfig` festzulegen, damit Tool-Aufrufe und -Ergebnisse zurückgegeben oder gestreamt werden. Die `tool_call`- und `tool_response`-Teile
> für die Videonavigation werden automatisch zurückgegeben, wenn
> `media_processing="AGENTIC"` für einen beliebigen Eingabeteil festgelegt ist.

### Antwortstruktur

Wenn die agentische Verarbeitung aktiviert ist, enthält die Antwort zusätzliche Teile, die die interne Navigationsspur offenlegen:

- `tool_call` **Teile** (`tool_type: "MEDIA_PROCESSING"`): werden jedes Mal ausgegeben, wenn das Modell ein Videosegment oder ein Audiotranskript anfordert.
- `tool_response` **Teile** (`tool_type: "MEDIA_PROCESSING"`): das Ergebnis jeder Ladeoperation.

Sie müssen diese Teile nicht manuell verarbeiten oder beantworten. Übergeben Sie die vollständige Antwort als Unterhaltungsverlauf und sie werden automatisch verarbeitet.

Wenn `include_thoughts=True` in `ThinkingConfig` festgelegt ist, werden die Schritte der Problemlösung als `thought: true`-Teile angezeigt, die mit den Tool-Aufruf-/Antwortpaaren verschachtelt sind. Wenn die Gedanken deaktiviert sind, wird der Gedankentext weggelassen, aber die Tool-Teile sind weiterhin vorhanden.

Das folgende Beispiel zeigt die Antwortnutzlast mit verschachtelten Tool-Aufruf- und Antwortteilen:

```
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "thought": true,
            "text": "Inspecting transcript for key discussion topics..."
          },
          {
            "thought_signature": "sig_A",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_B",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Loading visual frames to verify slide content..."
          },
          {
            "thought_signature": "sig_C",
            "tool_call": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought_signature": "sig_D",
            "tool_response": {
              "tool_type": "MEDIA_PROCESSING"
            }
          },
          {
            "thought": true,
            "text": "Synthesizing answer from gathered evidence..."
          },
          {
            "text": "The three main arguments presented in the lecture are...",
            "thought_signature": "sig_E"
          }
        ]
      }
    }
  ]
}
```

### Verarbeitungsmodi für verschiedene Videos kombinieren

Sie können für jeden Videoteil in derselben Anfrage unterschiedliche Verarbeitungsmodi festlegen:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_uri(
            file_uri=lecture.uri,
            mime_type=lecture.mime_type,
            media_processing="AGENTIC",  # Use agentic video understanding
        ),
        types.Part.from_uri(
            file_uri=experiment.uri,
            mime_type=experiment.mime_type,
            media_processing="STATIC",  # Use static processing
        ),
        "Compare the lecture content with the experiment results.",
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" },
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: lecture.uri,
            mimeType: lecture.mimeType,
          },
          mediaProcessing: "AGENTIC", // Use agentic video understanding
        },
        {
          fileData: {
            fileUri: experiment.uri,
            mimeType: experiment.mimeType,
          },
          mediaProcessing: "STATIC", // Use static processing
        },
        { text: "Compare the lecture content with the experiment results." },
      ],
    },
  ],
});
console.log(response.text);
```

### Ok

```
lecturePart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  lectureFile.URI,
        MIMEType: lectureFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingAgentic, // Use agentic
}
experimentPart := &genai.Part{
    FileData: &genai.FileData{
        FileURI:  experimentFile.URI,
        MIMEType: experimentFile.MIMEType,
    },
    MediaProcessing: genai.MediaProcessingStatic, // Use static
}
parts := []*genai.Part{
    lecturePart,
    experimentPart,
    genai.NewPartFromText("Compare the lecture content with the experiment results."),
}
contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}
result, _ := client.Models.GenerateContent(ctx, "gemini-3.8-flash", contents, nil)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [
        {
          "file_data": {
            "file_uri": "'${lecture_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "AGENTIC"
        },
        {
          "file_data": {
            "file_uri": "'${experiment_uri}'",
            "mime_type": "video/mp4"
          },
          "media_processing": "STATIC"
        },
        {"text": "Compare the lecture content with the experiment results."}
      ]
    }]
  }'
```

## Kontext-Caching für lange Videos verwenden

Bei Videos, die länger als 10 Minuten sind, oder wenn Sie mehrere Anfragen
für dieselbe Videodatei stellen möchten, verwenden Sie [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de), um
Kosten zu senken und die Latenz zu verbessern. Mit Kontext-Caching können Sie das Video einmal verarbeiten und die Tokens für nachfolgende Abfragen wiederverwenden. Dies ist ideal für Chatsitzungen oder wiederholte Analysen von Inhalten im Langformat.

## Auf Zeitstempel im Inhalt verweisen

Sie können Fragen zu bestimmten Zeitpunkten im Video stellen, indem Sie Zeitstempel im Format `MM:SS` verwenden.

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "What are the examples given at 00:05 and 00:10 supposed to show us?",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "What are the examples given at 00:05 and 00:10 supposed to show us?",
  ],
});
console.log(response.text);
```

### Ok

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("What are the examples given at 00:05 and 00:10 supposed to show us?"),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "What are the examples given at 00:05 and 00:10 supposed to show us?"}
        ]
      }]
    }' 2> /dev/null
```

## Detaillierte Informationen aus Videos extrahieren

Gemini-Modelle bieten leistungsstarke Funktionen zum Verstehen von Videoinhalten, indem sie Informationen aus den **Audio- und visuellen** Streams verarbeiten. So können Sie eine Vielzahl von Details extrahieren, einschließlich der Generierung von Beschreibungen des Geschehens in einem Video und der Beantwortung von Fragen zu dessen Inhalt.

Für visuelle Beschreibungen nimmt das Modell mit einer Rate von **1 Frame pro Sekunde** (FPS) Stichproben aus dem Video. Diese Standard-Abtastrate funktioniert für die meisten Inhalte gut, aber es kann sein, dass Details in Videos mit schnellen Bewegungen oder schnellen Szenenwechseln nicht erfasst werden.
Für solche Inhalte mit vielen Bewegungen sollten Sie [eine benutzerdefinierte Framerate festlegen](#custom-frame-rate).

### Python

```
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        myfile,
        "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
    ],
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    myfile,
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.",
  ],
});
console.log(response.text);
```

### Ok

```
parts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
        "Include timestamps for salient moments."),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3.8-flash",
    []*genai.Content{genai.NewContentFromParts(parts, genai.RoleUser)},
    nil,
)
fmt.Println(result.Text())
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"file_uri": "'"${file_uri}"'", "mime_type": "'"${MIME_TYPE}"'"}},
          {"text": "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."}
        ]
      }]
    }' 2> /dev/null
```

## Videoverarbeitung anpassen

Sie können die Videoverarbeitung in der Gemini API anpassen, indem Sie Clipping-Intervalle festlegen oder eine benutzerdefinierte Framerate-Samplingrate angeben. Diese Anpassungsoptionen
werden nur unterstützt, wenn das Video im Modus `"static"` verarbeitet wird.

### Clipping-Intervalle festlegen

Sie können Videos zuschneiden, indem Sie `videoMetadata` mit Start- und End-Offsets angeben.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.8-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Benutzerdefinierte Framerate festlegen

Sie können eine benutzerdefinierte Framerate-Samplingrate festlegen, indem Sie ein `fps`-Argument an `videoMetadata` übergeben.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.8-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const myfile = await ai.files.upload({
  file: "path/to/sample.mp4",
  mimeType: "video/mp4",
});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: [
    {
      fileData: {
        fileUri: myfile.uri,
        mimeType: myfile.mimeType,
      },
      videoMetadata: {
        fps: 5,
      },
    },
    "Please summarize the video in 3 sentences.",
  ],
});

console.log(response.text);
```

Standardmäßig wird 1 Frame pro Sekunde (FPS) aus dem Video gesampelt. Für lange Videos sollten Sie eine niedrige Framerate (unter 1) festlegen. Dies ist besonders nützlich für meist statische Videos (z.B. Vorträge). Verwenden Sie eine höhere Framerate für Videos, die eine detaillierte zeitliche Analyse erfordern, z. B. das Verstehen von schnellen Aktionen oder die Verfolgung von Bewegungen mit hoher Geschwindigkeit.

## Unterstützte Videoformate

Gemini unterstützt die folgenden MIME-Typen für Videoformate:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Technische Details zu Videos

- **Unterstützte Modelle und Kontext**: Alle Gemini-Modelle können Videodaten verarbeiten.
  - Modelle mit einem Kontextfenster von 1 Million Tokens können standardmäßig Videos mit einer Länge von bis zu 3 Stunden (bei niedriger Media-Auflösung) oder bis zu 1 Stunde (bei hoher Media-Auflösung) verarbeiten.
- **Verarbeitungsmodi**: Gemini 4 Argon, 3.8 Flash, 3.6 Flash, 3.5 Flash Lite,
  und neuere Modelle unterstützen zwei Videoverarbeitungsmodi:
  - **Statisch**: Frames werden mit 1 FPS extrahiert und in den Kontext gesetzt (Standard
    für alle Modelle). Audio wird mit 1 kbit/s (einzelner Kanal) verarbeitet.
    Zeitstempel werden jede Sekunde hinzugefügt. Am besten geeignet für kurze Clips oder wenn jeder Frame wichtig ist (z. B. Frame-by-Frame-Prüfung). Beachten Sie, dass schnelle Aktionssequenzen aufgrund der Abtastrate von 1 FPS Details verlieren können.
  - **Agentisch**: Das Modell navigiert dynamisch durch das Video und lädt
    Transkript und/oder Frames und/oder Audio bei Bedarf. Dadurch werden bis zu 88 % weniger Tokens für Inhalte im Langformat verwendet. Die Navigation kann jedoch die Zeit bis zum ersten Token (Time to First Token, TTFT) und die Gesamtzahl der Tokens bei kurzen Clips (unter 5 Minuten) oder umfassenden Abfragen aufgrund der internen Problemlösung und Tool-Roundtrips erhöhen.
    Die Antworten enthalten `MEDIA_PROCESSING`-Tool-Aufruf- und -Antwortteile, um den Kontext der Problemlösung über mehrere Turns hinweg beizubehalten. Am besten geeignet für Videos im Langformat und gezielte Abfragen, um die Tokenkosten und die Antwortqualität zu optimieren. Wird von Gemini 4 Argon, 3.8 Flash, 3.6 Flash und 3.5 Flash Lite unterstützt. Weitere Informationen finden Sie unter
    [Agentisches Videoverständnis](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=de#agentic-video-understanding).
- **Tokenberechnung (statischer Modus)**: Jede Sekunde des Videos wird wie
  folgt
  tokenisiert:
  - Einzelne Frames (gesampelt mit 1 FPS):
    - Wenn `media_resolution` auf „low“ gesetzt ist, werden Frames mit 66 Tokens pro Frame tokenisiert.
    - Andernfalls werden Frames mit 258 Tokens pro Frame tokenisiert.
  - Audio: 32 Tokens pro Sekunde.
  - Metadaten sind ebenfalls enthalten.
  - Gesamt: Etwa 100 Tokens pro Sekunde Video bei der Standard-Media-Auflösung (niedrig) oder etwa 300 Tokens pro Sekunde Video bei hoher Media-Auflösung.
- **Tokenberechnung (agentischer Modus)**: Die Tokennutzung variiert je nach Inhalt
  skomplexität und der Navigationsstrategie des Modells. Tokens für die Navigation, die während der Videoerkundung generiert werden
  , werden als **Denk-Tokens**
  (`thoughts_token_count`) gezählt, während Frames, Audio und Transkripte, die bei Bedarf geladen werden
  , als Tool-Prompt-Tokens (`tool_use_prompt_token_count`) gezählt werden.
  Bei der agentischen Verarbeitung werden für Inhalte im Langformat in der Regel bis zu 88% weniger Tokens insgesamt verwendet als bei der statischen Verarbeitung
  , da das Modell nur das Transkript und/oder die Frames und/oder das Audio lädt
  , die zum Beantworten des Prompts erforderlich sind (siehe den
  [Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=de#video-token-usage)).
- **Media-Auflösung**: Mit Gemini 3 wird mit dem Parameter `media_resolution` eine detaillierte Steuerung der multimodalen
  Vision-Verarbeitung eingeführt. Der Parameter `media_resolution` bestimmt die **maximale Anzahl von Tokens, die pro Eingabebild oder Videoframe zugewiesen werden**. Höhere Auflösungen verbessern die Fähigkeit des Modells, kleinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Tokennutzung und die Latenz. Die Parameter `media_resolution` und `media_processing` sind unabhängig: Sie können beide für denselben Videoteil festlegen.

Weitere Informationen zur Tokenberechnung finden Sie im
[Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=de).

- **Zeitstempelformat**: Wenn Sie in Ihrem Prompt auf bestimmte Momente in einem Video verweisen, verwenden Sie das `MM:SS` Format (z.B. `01:15` für 1 Minute und 15 Sekunden).
- **Prompt-Platzierung**: Wenn Sie Text und ein einzelnes Video kombinieren, platzieren Sie den Text-Prompt
  *nach* dem Videoteil im `contents` Array.
- **Zeitüberschreitungen bei langen Anfragen**: Bei Videos, die eine längere
  Verarbeitungszeit oder eine komplexe mehrstufige Problemlösung erfordern, verwenden Sie Streaming
  (`client.models.generate_content_stream`). Bei synchronen Anfragen ohne Streaming,
  bei denen bei hoher Nachfrage Back-End-Wiederholungsversuche auftreten, können die Gültigkeitszeiträume für
  Verbindungs- oder Authentifizierungstokens überschritten werden, was zu
  unerwarteten `401 Unauthorized` oder Zeitüberschreitungsfehlern führen kann. Durch Streaming bleibt die Verbindung aktiv und es werden Zwischenschritte der Problemlösung und der Fortschritt des Tool-Aufrufs angezeigt.

## Nächste Schritte

- [Medienauflösung](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=de): Steuern Sie die
  Auflösung von Videoframes, um ein ausgewogenes Verhältnis zwischen Qualität und Tokennutzung zu erreichen.
- [Tokens](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=de): Informationen zur Tokenisierung von Videoinhalten
  im statischen und agentischen Verarbeitungsmodus.
- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=de#system-instructions):
  Mit Systemanweisungen können Sie das Verhalten des Modells entsprechend Ihren
  spezifischen Anforderungen und Anwendungsfällen steuern.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de): Weitere Informationen zum Hochladen und Verwalten von
  Dateien zur Verwendung mit Gemini.
- [Strategien für Prompts mit Dateien](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide): Die Gemini
  API unterstützt Prompts mit Text-, Bild-, Audio- und Videodaten, auch als
  multimodale Prompts bezeichnet.
- [Sicherheitshinweise](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de): Generative KI
  Modelle liefern manchmal unerwartete Ausgaben, z. B. Ausgaben, die ungenau, voreingenommen oder anstößig sind. Nachbearbeitung und menschliche Bewertung sind unerlässlich, um das Risiko von Schäden durch solche Ausgaben zu begrenzen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-13 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-13 (UTC)."],[],[]]
