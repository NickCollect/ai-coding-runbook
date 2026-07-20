---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=de
fetched_at: 2026-07-20T04:37:50.074680+00:00
title: "Videos verstehen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Videos verstehen

> Weitere Informationen zur Videogenerierung finden Sie im [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de).

Gemini-Modelle können Videos verarbeiten und ermöglichen so viele innovative Anwendungsfälle für Entwickler, für die in der Vergangenheit domänenspezifische Modelle erforderlich gewesen wären.
Gemini kann unter anderem Videos beschreiben, segmentieren und Informationen daraus extrahieren, Fragen zu Videoinhalten beantworten und auf bestimmte Zeitstempel in einem Video verweisen.

Sie haben folgende Möglichkeiten, Videos als Eingabe für Gemini zu verwenden:

| Eingabemethode | Max. Größe | Empfohlener Anwendungsfall |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (kostenpflichtig) / 2 GB (kostenlos) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), wiederverwendbare Dateien. |
| [Cloud Storage-Registrierung](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de#registration) | 2 GB (pro Datei, keine Speicherplatzbeschränkungen) | Große Dateien (über 100 MB), lange Videos (über 10 Minuten), dauerhafte, wiederverwendbare Dateien. |
| [Inlinedaten](#inline-video) | < 100 MB | Kleine Dateien (< 100 MB), kurze Dauer (< 1 Minute), einmalige Eingaben. |
| [YouTube-URLs](#youtube) | – | Öffentliche YouTube-Videos. |

> **Hinweis**:Die [File API](#upload-video) wird für die meisten Anwendungsfälle empfohlen, insbesondere für Dateien, die größer als 100 MB sind, oder wenn Sie die Datei in mehreren Anfragen wiederverwenden möchten.

Informationen zu anderen Dateieingabemethoden, z. B. zur Verwendung externer URLs oder in Google Cloud gespeicherter Dateien, finden Sie im Leitfaden [Dateieingabemethoden](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

### Videodatei hochladen

Im folgenden Code wird ein Beispielvideo heruntergeladen, mit der [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de) hochgeladen, auf die Verarbeitung gewartet und dann die hochgeladene Dateireferenz verwendet, um das Video zusammenzufassen.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
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
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
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
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Verwenden Sie immer die Files API, wenn die Gesamtgröße der Anfrage (einschließlich Datei, Text-Prompt, Systemanweisungen usw.) mehr als 20 MB beträgt, die Videodauer lang ist oder wenn Sie dasselbe Video in mehreren Prompts verwenden möchten.
Die File API akzeptiert Videodateiformate direkt.

Weitere Informationen zum Arbeiten mit Media-Dateien finden Sie unter [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de).

### Videodaten inline übergeben

Anstatt eine Videodatei über die File API hochzuladen, können Sie kleinere Videos direkt im Request übergeben. Diese Methode eignet sich für kürzere Videos mit einer Gesamtanfragegröße von unter 20 MB.

Hier ein Beispiel für die Bereitstellung von Inline-Videodaten:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### YouTube-URLs für Tickets

Sie können YouTube-URLs direkt als Teil Ihrer Anfrage an die Gemini API übergeben:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.5-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Beschränkungen:**

- In der kostenlosen Version können Sie nicht mehr als 8 Stunden YouTube-Videos pro Tag hochladen.
- Bei der kostenpflichtigen Stufe gibt es keine Begrenzung der Videolänge.
- Bei Modellen vor Gemini 2.5 können Sie nur ein Video pro Anfrage hochladen. Bei Gemini 2.5 und späteren Modellen können Sie pro Anfrage maximal 10 Videos hochladen.
- Du kannst nur öffentliche Videos hochladen, keine privaten oder nicht gelisteten Videos.

## Auf Zeitstempel im Inhalt verweisen

Sie können Fragen zu bestimmten Zeitpunkten im Video stellen, indem Sie Zeitstempel im Format `MM:SS` verwenden.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Detaillierte Informationen aus Videos extrahieren

Gemini-Modelle bieten leistungsstarke Funktionen zum Verstehen von Videoinhalten, indem sie Informationen aus **Audio- und visuellen Streams** verarbeiten. So können Sie viele Details extrahieren, z. B. Beschreibungen der Vorgänge in einem Video generieren und Fragen zum Inhalt beantworten lassen.

Für visuelle Beschreibungen wird das Video mit einer Rate von **1 Bild pro Sekunde** (FPS) abgetastet. Diese Standard-Samplingrate eignet sich gut für die meisten Inhalte. Bei Videos mit schnellen Bewegungen oder schnellen Szenenwechseln können jedoch Details verloren gehen.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Unterstützte Videoformate

Gemini unterstützt die folgenden MIME-Typen für Videoformate:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Technische Details zu Videos

- **Unterstützte Modelle und Kontext**: Alle Gemini-Modelle können Videodaten verarbeiten.
  - Modelle mit einem Kontextfenster für 1 Million Tokens können Videos mit einer Länge von bis zu einer Stunde in der Standardauflösung oder bis zu drei Stunden in niedriger Auflösung verarbeiten.
- **Verarbeitung über die File API**: Bei Verwendung der File API werden Videos mit 1 Frame pro Sekunde (FPS) gespeichert und Audio mit 1 Kbps (Einzelkanal) verarbeitet.
  Zeitstempel werden jede Sekunde hinzugefügt.
  - Diese Raten können sich in Zukunft ändern, um die Inferenz zu verbessern.
- **Tokenberechnung**: Jede Sekunde des Videos wird so tokenisiert:
  - Einzelne Frames (mit 1 FPS):
    - Wenn `media_resolution` auf „Niedrig“ festgelegt ist, werden Frames mit 66 Tokens pro Frame tokenisiert.
    - Andernfalls werden Frames mit 258 Tokens pro Frame tokenisiert.
  - Audio: 32 Tokens pro Sekunde.
  - Metadaten sind ebenfalls enthalten.
  - Insgesamt: etwa 300 Tokens pro Sekunde Video bei Standardauflösung oder 100 Tokens pro Sekunde Video bei niedriger Auflösung.
- **Mediale Auflösung**: Mit Gemini 3 wird die multimodale Bildverarbeitung durch den Parameter `media_resolution` detaillierter gesteuert. Der Parameter `media_resolution` bestimmt die **maximale Anzahl von Tokens, die pro Eingabebild oder Videoframes zugewiesen werden.**
  Höhere Auflösungen verbessern die Fähigkeit des Modells, feinen Text zu lesen oder kleine Details zu erkennen, erhöhen aber die Token-Nutzung und die Latenz.

  Weitere Informationen zur Tokenberechnung finden Sie im [Leitfaden zu Tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=de).
- **Format des Zeitstempels**: Wenn Sie in Ihrem Prompt auf bestimmte Momente in einem Video verweisen, verwenden Sie das Format `MM:SS` (z.B. `01:15` für 1 Minute und 15 Sekunden).
- **Best Practices**:

  - Verwenden Sie für optimale Ergebnisse nur ein Video pro Prompt-Anfrage.
  - Wenn Sie Text und ein einzelnes Video kombinieren, platzieren Sie den Text-Prompt im `input`-Array *nach* dem Videoteil.
  - Bei schnellen Aktionssequenzen können aufgrund der Abtastrate von 1 FPS Details verloren gehen. Verlangsame solche Clips bei Bedarf.

## Nächste Schritte

In diesem Leitfaden wird gezeigt, wie Sie Videodateien hochladen und Textausgaben aus Videoeingaben generieren. Weitere Informationen finden Sie in den folgenden Ressourcen:

- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/text-generation?hl=de#system-instructions): Mit Systemanweisungen können Sie das Verhalten des Modells basierend auf Ihren spezifischen Anforderungen und Anwendungsfällen steuern.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=de): Hier finden Sie weitere Informationen zum Hochladen und Verwalten von Dateien für die Verwendung mit Gemini.
- [Strategien für Dateiprompts](https://ai.google.dev/gemini-api/docs/files?hl=de#prompt-guide): Die Gemini API unterstützt Prompts mit Text-, Bild-, Audio- und Videodaten, auch als multimodale Prompts bezeichnet.
- [Sicherheitshinweise](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de): Generative KI-Modelle können manchmal unerwartete Ausgaben liefern, z. B. Ausgaben, die ungenau, voreingenommen oder anstößig sind. Die Nachbearbeitung und menschliche Bewertung sind unerlässlich, um das Risiko von Schäden durch solche Ausgaben zu begrenzen.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-06 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-06 (UTC)."],[],[]]
