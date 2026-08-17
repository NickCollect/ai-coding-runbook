---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=it
fetched_at: 2026-08-17T02:35:23.860550+00:00
title: "Comprensione dell'audio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Comprensione dell'audio

Gemini può analizzare l'input audio e generare risposte di testo.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Vai

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

    localAudioPath := "/path/to/sample.mp3"
    uploadedFile, _ := client.Files.UploadFromPath(
        ctx,
        localAudioPath,
        nil,
    )

    parts := []*genai.Part{
        genai.NewPartFromText("Describe this audio clip"),
        genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Panoramica

Gemini può analizzare e comprendere l'input audio e generare risposte di testo, consentendo casi d'uso come i seguenti:

- Descrivere, riepilogare o rispondere a domande sui contenuti audio.
- Fornire una trascrizione e una traduzione dell'audio (conversione della voce in testo).
- Rilevare le emozioni nella voce e nella musica.
- Analizzare segmenti specifici dell'audio e fornire timestamp.

Al momento, l'API Gemini non supporta i casi d'uso di trascrizione in tempo reale.
Per le interazioni vocali e video in tempo reale, consulta l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).
Per i modelli di conversione della voce in testo dedicati con supporto per la trascrizione in tempo reale,
utilizza l'[API Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text?hl=it).

## Trascrivere la voce in testo

Questa applicazione di esempio mostra come richiedere all'API Gemini di trascrivere,
tradurre e riepilogare la voce, inclusi timestamp e rilevamento delle emozioni
utilizzando [output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM"

def main():
  prompt = """
    Process the audio file and generate a detailed transcription.

    Requirements:
    1. Provide accurate timestamps for each segment (Format: MM:SS).
    2. Detect the primary language of each segment.
    3. If the segment is in a language different than English, also provide the English translation.
    4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
    5. Provide a brief summary of the entire audio at the beginning.
  """

  response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
      types.Content(
        parts=[
          types.Part(
            file_data=types.FileData(
              file_uri=YOUTUBE_URL
            )
          ),
          types.Part(
            text=prompt
          )
        ]
      )
    ],
    config=types.GenerateContentConfig(
      response_format={"text": {"mime_type": "application/json"}},
      response_schema=types.Schema(
        type=types.Type.OBJECT,
        properties={
          "summary": types.Schema(
            type=types.Type.STRING,
            description="A concise summary of the audio content.",
          ),
          "segments": types.Schema(
            type=types.Type.ARRAY,
            description="List of transcribed segments with timestamp.",
            items=types.Schema(
              type=types.Type.OBJECT,
              properties={
                "timestamp": types.Schema(type=types.Type.STRING),
                "content": types.Schema(type=types.Type.STRING),
                "language": types.Schema(type=types.Type.STRING),
                "language_code": types.Schema(type=types.Type.STRING),
                "translation": types.Schema(type=types.Type.STRING),
                "emotion": types.Schema(
                  type=types.Type.STRING,
                  enum=["happy", "sad", "angry", "neutral"]
                ),
              },
              required=["timestamp", "content", "language", "language_code", "emotion"],
            ),
          ),
        },
        required=["summary", "segments"],
      ),
    ),
  )

  print(response.text)

if __name__ == "__main__":
  main()
```

### JavaScript

```
import {
  GoogleGenAI,
  Type
} from "@google/genai";

const ai = new GoogleGenAI({});

const YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

async function main() {
  const prompt = `
      Process the audio file and generate a detailed transcription.

      Requirements:
      1. Provide accurate timestamps for each segment (Format: MM:SS).
      2. Detect the primary language of each segment.
      3. If the segment is in a language different than English, also provide the English translation.
      4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.
      5. Provide a brief summary of the entire audio at the beginning.
    `;

  const Emotion = {
    Happy: 'happy',
    Sad: 'sad',
    Angry: 'angry',
    Neutral: 'neutral'
  };

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: {
      parts: [
        {
          fileData: {
            fileUri: YOUTUBE_URL,
          },
        },
        {
          text: prompt,
        },
      ],
    },
    config: {
      responseFormat: { text: { mimeType: "application/json" } },
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          summary: {
            type: Type.STRING,
            description: "A concise summary of the audio content.",
          },
          segments: {
            type: Type.ARRAY,
            description: "List of transcribed segments with timestamp.",
            items: {
              type: Type.OBJECT,
              properties: {
                timestamp: { type: Type.STRING },
                content: { type: Type.STRING },
                language: { type: Type.STRING },
                language_code: { type: Type.STRING },
                translation: { type: Type.STRING },
                emotion: {
                  type: Type.STRING,
                  enum: Object.values(Emotion)
                },
              },
              required: ["timestamp", "content", "language", "language_code", "emotion"],
            },
          },
        },
        required: ["summary", "segments"],
      },
    },
  });
  const json = JSON.parse(response.text);
  console.log(json);
}

await main();
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
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=ku-N-eS1lgM",
                "mime_type": "video/mp4"
              }
            },
            {
              "text": "Process the audio file and generate a detailed transcription.\n\nRequirements:\n1. Provide accurate timestamps for each segment (Format: MM:SS).\n2. Detect the primary language of each segment.\n3. If the segment is in a language different than English, also provide the English translation.\n4. Identify the primary emotion of the speaker in this segment. You MUST choose exactly one of the following: Happy, Sad, Angry, Neutral.\n5. Provide a brief summary of the entire audio at the beginning."
            }
          ]
        }
      ],
      "generation_config": {
        "response_format": {"text": {"mime_type": "application/json"}},
        "response_schema": {
          "type": "OBJECT",
          "properties": {
            "summary": {
              "type": "STRING",
              "description": "A concise summary of the audio content."
            },
            "segments": {
              "type": "ARRAY",
              "description": "List of transcribed segments with timestamp.",
              "items": {
                "type": "OBJECT",
                "properties": {
                  "timestamp": { "type": "STRING" },
                  "content": { "type": "STRING" },
                  "language": { "type": "STRING" },
                  "language_code": { "type": "STRING" },
                  "translation": { "type": "STRING" },
                  "emotion": {
                    "type": "STRING",
                    "enum": ["happy", "sad", "angry", "neutral"]
                  }
                },
                "required": ["timestamp", "content", "language", "language_code", "emotion"]
              }
            }
          },
          "required": ["summary", "segments"]
        }
      }
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

Puoi richiedere a [AI Studio Build](https://aistudio.google.com/apps?e=0&hl=it) di creare
un'app proprio come
[questa app di trascrizione di esempio](https://aistudio.google.com/apps/bundled/echoscript?hl=it)
con un clic di un pulsante.

![Un'app Gemini per la trascrizione audio multilingue](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=it)

## Audio di input

Puoi fornire dati audio a Gemini nei seguenti modi:

- [Carica un file audio](#upload-audio) prima di inviare una richiesta a
  `generateContent`.
- [Trasmetti i dati audio in linea](#inline-audio) con la richiesta a
  `generateContent`.

Per scoprire di più su altri metodi di input dei file, consulta la
[guida Metodi di input dei file](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=it).

### Caricare un file audio

Puoi utilizzare l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=it) per caricare un file audio.
Utilizza sempre l'API Files quando la dimensione totale della richiesta (inclusi file, prompt di testo, istruzioni di sistema e così via) è superiore a 20 MB.

Il seguente codice carica un file audio e poi lo utilizza in una chiamata a `generateContent`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Vai

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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

Per scoprire di più su come lavorare con i file multimediali, consulta
[l'API Files](https://ai.google.dev/gemini-api/docs/files?hl=it).

### Trasmettere dati audio in linea

Anziché caricare un file audio, puoi trasmettere i dati audio in linea nella richiesta a `generateContent`:

### Python

```
from google import genai
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[
    'Describe this audio clip',
    types.Part.from_bytes(
      data=audio_bytes,
      mime_type='audio/mp3',
    )
  ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64AudioFile = fs.readFileSync("path/to/small-sample.mp3", {
  encoding: "base64",
});

const contents = [
  { text: "Please summarize the audio." },
  {
    inlineData: {
      mimeType: "audio/mp3",
      data: base64AudioFile,
    },
  },
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### Vai

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

  audioBytes, _ := os.ReadFile("/path/to/small-sample.mp3")

  parts := []*genai.Part{
      genai.NewPartFromText("Describe this audio clip"),
    &genai.Part{
      InlineData: &genai.Blob{
        MIMEType: "audio/mp3",
        Data:     audioBytes,
      },
    },
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

Ecco alcuni aspetti da tenere presente sui dati audio in linea:

- La dimensione massima della richiesta è di 20 MB, inclusi prompt di testo, istruzioni di sistema e file forniti in linea. Se la dimensione del file fa sì che la *dimensione totale della richiesta* superi i 20 MB, utilizza l'API Files per [caricare un file audio](#upload-audio) da utilizzare nella richiesta.
- Se utilizzi un campione audio più volte, è più efficiente
  [caricare un file audio](#upload-audio).

## Ottenere una trascrizione

Per ottenere una trascrizione dei dati audio, basta richiederla nel prompt:

### Python

```
from google import genai

client = genai.Client()
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-3.6-flash',
  contents=[prompt, myfile]
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
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const result = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
    "Generate a transcript of the speech.",
  ]),
});
console.log("result.text=", result.text);
```

### Vai

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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Generate a transcript of the speech."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## Fare riferimento ai timestamp

Puoi fare riferimento a sezioni specifiche di un file audio utilizzando timestamp nel formato `MM:SS`. Ad esempio, il seguente prompt richiede una trascrizione che

- Inizia a 2 minuti e 30 secondi dall'inizio del file.
- Termina a 3 minuti e 29 secondi dall'inizio del file.

### Python

```
# Create a prompt containing timestamps.
prompt = "Provide a transcript of the speech from 02:30 to 03:29."
```

### JavaScript

```
// Create a prompt containing timestamps.
const prompt = "Provide a transcript of the speech from 02:30 to 03:29."
```

### Vai

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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromText("Provide a transcript of the speech " +
                            "between the timestamps 02:30 and 03:29."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## Contare i token

Chiama il metodo `countTokens` per ottenere un conteggio del numero di token in un file audio. Ad esempio:

### Python

```
from google import genai

client = genai.Client()
response = client.models.count_tokens(
  model='gemini-3.6-flash',
  contents=[myfile]
)

print(response)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const countTokensResponse = await ai.models.countTokens({
  model: "gemini-3.6-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
  ]),
});
console.log(countTokensResponse.totalTokens);
```

### Vai

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

  localAudioPath := "/path/to/sample.mp3"
  uploadedFile, _ := client.Files.UploadFromPath(
      ctx,
      localAudioPath,
      nil,
  )

  parts := []*genai.Part{
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }
  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  tokens, _ := client.Models.CountTokens(
      ctx,
      "gemini-3.6-flash",
      contents,
      nil,
  )

  fmt.Printf("File %s is %d tokens\n", localAudioPath, tokens.TotalTokens)
}
```

## Formati audio supportati

Gemini supporta i seguenti tipi MIME di formato audio:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG Vorbis - `audio/ogg`
- FLAC - `audio/flac`

## Dettagli tecnici sull'audio

- Gemini rappresenta ogni secondo di audio come 32 token; ad esempio, un minuto di audio è rappresentato da 1920 token.
- Gemini può "comprendere" i componenti non vocali, come il canto degli uccelli o le sirene.
- La lunghezza massima supportata dei dati audio in un singolo prompt è di 9,5 ore.
  Gemini non limita il *numero* di file audio in un singolo prompt; tuttavia, la lunghezza totale combinata di tutti i file audio in un singolo prompt non può superare le 9,5 ore.
- Gemini esegue il downsampling dei file audio a una risoluzione dei dati di 16 Kbps.
- Se la sorgente audio contiene più canali, Gemini li combina in un unico canale.

## Passaggi successivi

Questa guida mostra come generare testo in risposta ai dati audio. Per scoprire di più, consulta le seguenti risorse:

- [Strategie di prompt dei file](https://ai.google.dev/gemini-api/docs/files?hl=it#prompt-guide): l'
  API Gemini supporta i prompt con dati di testo, immagini, audio e video, noti
  anche come prompt multimodali.
- [Istruzioni di sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions):
  Le istruzioni di sistema ti consentono di indirizzare il comportamento del modello in base alle tue
  esigenze e ai tuoi casi d'uso specifici.
- [Linee guida sulla sicurezza](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it): a volte i modelli di AI generativa
  producono output imprevisti, ad esempio output imprecisi,
  distorti o offensivi. L'elaborazione post-elaborazione e la valutazione umana sono essenziali per limitare il rischio di danni derivanti da questi output.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
