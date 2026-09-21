---
source_url: https://ai.google.dev/gemini-api/docs/audio?hl=id
fetched_at: 2026-09-21T05:54:34.316906+00:00
title: "Pemahaman audio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemahaman audio

Gemini dapat menganalisis input audio dan menghasilkan respons teks.

### Python

```
from google import genai
import base64

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
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
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mp3" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        "path/to/sample.mp3", UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .uri(uploadedFile.uri().get())
        .mimeType(AudioContentMimeType.of(uploadedFile.mimeType().get()))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# First upload the file, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

## Ringkasan

Gemini dapat menganalisis dan memahami input audio serta menghasilkan respons teks, sehingga memungkinkan kasus penggunaan seperti:

- Mendeskripsikan, meringkas, atau menjawab pertanyaan tentang konten audio
- Transkripsi dan terjemahan (speech to text)
- Diarisasi pembicara (mengidentifikasi pembicara yang berbeda)
- Deteksi emosi dalam ucapan dan musik
- Menganalisis segmen tertentu dengan stempel waktu

Untuk interaksi suara dan video real-time, lihat
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).
Untuk model speech-to-text khusus dengan dukungan untuk transkripsi real-time,
gunakan [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=id).

## Mentranskripsikan ucapan menjadi teks

Contoh ini menunjukkan cara mentranskripsikan, menerjemahkan, dan meringkas ucapan dengan
stempel waktu, diarization pembicara, dan deteksi emosi menggunakan
[output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id).

### Python

```
from google import genai

client = genai.Client()

YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM"

prompt = """
  Process the audio file and generate a detailed transcription.

  Requirements:
  1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).
  2. Provide accurate timestamps for each segment (Format: MM:SS).
  3. Detect the primary language of each segment.
  4. If not English, provide the English translation.
  5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.
  6. Provide a brief summary at the beginning.
"""

response_schema = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "segments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "speaker": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "content": {"type": "string"},
                    "language": {"type": "string"},
                    "emotion": {
                        "type": "string",
                        "enum": ["happy", "sad", "angry", "neutral"]
                    }
                },
                "required": ["speaker", "timestamp", "content", "emotion"]
            }
        }
    },
    "required": ["summary", "segments"]
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": YOUTUBE_URL, "mime_type": "video/mp4"},
        {"type": "text", "text": prompt}
    ],
    response_format=response_schema,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const YOUTUBE_URL = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

const prompt = `
  Process the audio file and generate a detailed transcription.

  Requirements:
  1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).
  2. Provide accurate timestamps for each segment (Format: MM:SS).
  3. Detect the primary language of each segment.
  4. If not English, provide the English translation.
  5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.
  6. Provide a brief summary at the beginning.
`;

const responseSchema = {
    type: "object",
    properties: {
        summary: { type: "string" },
        segments: {
            type: "array",
            items: {
                type: "object",
                properties: {
                    speaker: { type: "string" },
                    timestamp: { type: "string" },
                    content: { type: "string" },
                    language: { type: "string" },
                    emotion: {
                        type: "string",
                        enum: ["happy", "sad", "angry", "neutral"]
                    }
                },
                required: ["speaker", "timestamp", "content", "emotion"]
            }
        }
    },
    required: ["summary", "segments"]
};

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "video", uri: YOUTUBE_URL, mime_type: "video/mp4" },
        { type: "text", text: prompt }
    ],
    response_format: responseSchema,
});

console.log(JSON.parse(interaction.output_text));
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

String youtubeUrl = "https://www.youtube.com/watch?v=ku-N-eS1lgM";

String prompt =
    "Process the audio file and generate a detailed transcription.\n\n"
        + "Requirements:\n"
        + "1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).\n"
        + "2. Provide accurate timestamps for each segment (Format: MM:SS).\n"
        + "3. Detect the primary language of each segment.\n"
        + "4. If not English, provide the English translation.\n"
        + "5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.\n"
        + "6. Provide a brief summary at the beginning.";

Map<String, Object> emotionProp = new HashMap<>();
emotionProp.put("type", "string");
emotionProp.put("enum", Arrays.asList("happy", "sad", "angry", "neutral"));

Map<String, Object> stringType = new HashMap<>();
stringType.put("type", "string");

Map<String, Object> segmentProps = new HashMap<>();
segmentProps.put("speaker", stringType);
segmentProps.put("timestamp", stringType);
segmentProps.put("content", stringType);
segmentProps.put("language", stringType);
segmentProps.put("emotion", emotionProp);

Map<String, Object> segmentItem = new HashMap<>();
segmentItem.put("type", "object");
segmentItem.put("properties", segmentProps);
segmentItem.put("required", Arrays.asList("speaker", "timestamp", "content", "emotion"));

Map<String, Object> segmentsProp = new HashMap<>();
segmentsProp.put("type", "array");
segmentsProp.put("items", segmentItem);

Map<String, Object> properties = new HashMap<>();
properties.put("summary", stringType);
properties.put("segments", segmentsProp);

Map<String, Object> responseSchema = new HashMap<>();
responseSchema.put("type", "object");
responseSchema.put("properties", properties);
responseSchema.put("required", Arrays.asList("summary", "segments"));

Content videoContent =
    VideoContent.builder()
        .uri(youtubeUrl)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(ResponseFormat.of(responseSchema)))
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
    "input": [
      {
        "type": "video",
        "uri": "https://www.youtube.com/watch?v=ku-N-eS1lgM",
        "mime_type": "video/mp4"
      },
      {
        "type": "text",
        "text": "Transcribe with speaker diarization and emotion detection."
      }
    ],
    "response_format": {
        "type": "object",
        "properties": {
          "summary": {"type": "string"},
          "segments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "speaker": {"type": "string"},
                "timestamp": {"type": "string"},
                "content": {"type": "string"},
                "emotion": {"type": "string", "enum": ["happy", "sad", "angry", "neutral"]}
              }
            }
          }
        }
      }
  }'
```

![Aplikasi Gemini transkripsi audio multibahasa](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=id)

## Input audio

Anda dapat memberikan data audio dengan cara berikut:

- [Upload file audio](#upload-audio) sebelum membuat permintaan.
- [Teruskan data audio inline](#inline-audio) dengan permintaan.

### Mengupload file audio

Gunakan [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id) untuk file yang lebih besar dari 20 MB.

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" }
});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
// Upload an audio file using the Files API (recommended for files > 20 MB)
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        "path/to/sample.mp3", UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .uri(uploadedFile.uri().get())
        .mimeType(AudioContentMimeType.of(uploadedFile.mimeType().get()))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "uri": "YOUR_FILE_URI",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

### Meneruskan data audio inline

Untuk file audio kecil dengan ukuran total permintaan di bawah 20 MB:

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {
            "type": "audio",
            "data": base64.b64encode(audio_bytes).decode('utf-8'),
            "mime_type": "audio/mp3"
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

const audioData = fs.readFileSync("path/to/small-sample.mp3", {
    encoding: "base64"
});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        {type: "text", text: "Describe this audio clip"},
        {
            type: "audio",
            data: audioData,
            mime_type: "audio/mp3"
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] audioBytes = Files.readAllBytes(Paths.get("path/to/small-sample.mp3"));
String base64Audio = Base64.getEncoder().encodeToString(audioBytes);

Content textContent = TextContent.builder().text("Describe this audio clip").build();
Content audioContent =
    AudioContent.builder()
        .data(base64Audio)
        .mimeType(AudioContentMimeType.AUDIO_MP3)
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this audio clip"},
      {
        "type": "audio",
        "data": "'$(base64 $B64FLAGS $AUDIO_PATH)'",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

Catatan tentang data audio inline:
\* Ukuran permintaan maksimum adalah total 20 MB (termasuk perintah dan semua file)
\* Untuk penggunaan ulang, [upload file](#upload-audio) saja

## Mendapatkan transkrip

Untuk mendapatkan transkrip, minta di perintah:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Generate a transcript of the speech."},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: "Generate a transcript of the speech." },
        {
            type: "audio",
            uri: uploadedFile.uri,
            mime_type: uploadedFile.mimeType
        }
    ]
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        "path/to/sample.mp3", UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent = TextContent.builder().text("Generate a transcript of the speech.").build();
Content audioContent =
    AudioContent.builder()
        .uri(uploadedFile.uri().get())
        .mimeType(AudioContentMimeType.of(uploadedFile.mimeType().get()))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

## Merujuk pada stempel waktu

Gunakan format `MM:SS` untuk merujuk bagian tertentu:

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Provide a transcript from 02:30 to 03:29."},
        {
            "type": "audio",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: "Provide a transcript from 02:30 to 03:29." },
        { type: "audio", uri: uploadedFile.uri, mime_type: "audio/mp3" }
    ]
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        "path/to/sample.mp3", UploadFileConfig.builder().mimeType("audio/mp3").build());

Content textContent =
    TextContent.builder().text("Provide a transcript from 02:30 to 03:29.").build();
Content audioContent =
    AudioContent.builder()
        .uri(uploadedFile.uri().get())
        .mimeType(AudioContentMimeType.of(uploadedFile.mimeType().get()))
        .build();

List<Content> contents = Arrays.asList(textContent, audioContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

## Menghitung token

Menghitung token dalam file audio:

### Python

```
response = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=[uploaded_file]
)
print(response)
```

### JavaScript

```
const response = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: [
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(response.totalTokens);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        "path/to/sample.mp3", UploadFileConfig.builder().mimeType("audio/mp3").build());

CountTokensResponse response =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromUri(uploadedFile.uri().get(), uploadedFile.mimeType().get()))),
        null);

System.out.println(response);
```

## Format audio yang didukung

Gemini mendukung jenis MIME format audio berikut:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 - `audio/l16`
- Opus - `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Untuk mengetahui daftar lengkap jenis MIME dan skema parameter yang didukung, lihat [referensi Interactions API](https://ai.google.dev/api/interactions-api?hl=id#Resource:Content).

## Detail teknis tentang audio

- **Token**: 32 token per detik audio (1 menit = 1.920 token)
- **Non-ucapan**: Gemini memahami suara non-ucapan (kicauan burung, sirene, dll.)
- **Panjang maksimum**: audio berdurasi 9,5 jam per perintah
- **Resolusi**: Di-downsample menjadi 16 Kbps
- **Saluran**: Audio multisaluran digabungkan ke satu saluran

## Langkah berikutnya

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id): Mengupload dan mengelola file audio
- [Petunjuk sistem](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#system-instructions):
  Menyesuaikan perilaku model
- [Output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id):
  Mendapatkan hasil transkripsi dalam format JSON

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-18 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-18 UTC."],[],[]]
