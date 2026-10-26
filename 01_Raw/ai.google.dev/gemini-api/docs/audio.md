---
source_url: https://ai.google.dev/gemini-api/docs/audio?hl=th
fetched_at: 2026-10-26T05:52:00.115417+00:00
title: "\u0e04\u0e27\u0e32\u0e21\u0e40\u0e02\u0e49\u0e32\u0e43\u0e08\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e40\u0e2a\u0e35\u0e22\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# ความเข้าใจเกี่ยวกับเสียง

Gemini สามารถวิเคราะห์อินพุตเสียงและสร้างคำตอบเป็นข้อความได้

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Describe this audio clip",
        }),
        interactions.NewContent(interactions.AudioContent{
            URI:      genai.Ptr(uploadedFile.URI),
            MimeType: interactions.AudioContentMimeType(uploadedFile.MIMEType).ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

## ภาพรวม

Gemini สามารถวิเคราะห์และทำความเข้าใจอินพุตเสียง รวมถึงสร้างคำตอบที่เป็นข้อความ
ซึ่งช่วยให้ใช้กรณีการใช้งานต่างๆ ได้ เช่น

- อธิบาย สรุป หรือตอบคำถามเกี่ยวกับเนื้อหาเสียง
- การถอดเสียงและการแปล (เสียงพูดเป็นข้อความ)
- การแยกแยะเสียงผู้พูด (ระบุผู้พูดที่แตกต่างกัน)
- การตรวจจับอารมณ์ในคำพูดและดนตรี
- การวิเคราะห์กลุ่มที่เฉพาะเจาะจงด้วยการประทับเวลา

สำหรับการโต้ตอบด้วยเสียงและวิดีโอแบบเรียลไทม์ โปรดดู
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=th)
หากต้องการใช้โมเดล Speech-to-Text เฉพาะที่รองรับการถอดเสียงแบบเรียลไทม์
ให้ใช้ [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=th)

## ถอดเสียงพูดเป็นข้อความ

ตัวอย่างนี้แสดงวิธีถอดเสียง แปล และสรุปคำพูดพร้อม
การประทับเวลา การระบุผู้พูด และการตรวจจับอารมณ์โดยใช้
[เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    youtubeURL := "https://www.youtube.com/watch?v=ku-N-eS1lgM"

    prompt := "Process the audio file and generate a detailed transcription.\n\n" +
        "Requirements:\n" +
        "1. Identify distinct speakers (e.g., Speaker 1, Speaker 2).\n" +
        "2. Provide accurate timestamps for each segment (Format: MM:SS).\n" +
        "3. Detect the primary language of each segment.\n" +
        "4. If not English, provide the English translation.\n" +
        "5. Identify the primary emotion: Happy, Sad, Angry, or Neutral.\n" +
        "6. Provide a brief summary at the beginning."

    responseSchema := map[string]any{
        "type": "object",
        "properties": map[string]any{
            "summary": map[string]any{"type": "string"},
            "segments": map[string]any{
                "type": "array",
                "items": map[string]any{
                    "type": "object",
                    "properties": map[string]any{
                        "speaker":   map[string]any{"type": "string"},
                        "timestamp": map[string]any{"type": "string"},
                        "content":   map[string]any{"type": "string"},
                        "language":  map[string]any{"type": "string"},
                        "emotion": map[string]any{
                            "type": "string",
                            "enum": []string{"happy", "sad", "angry", "neutral"},
                        },
                    },
                    "required": []string{"speaker", "timestamp", "content", "emotion"},
                },
            },
        },
        "required": []string{"summary", "segments"},
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.VideoContent{
            URI:      genai.Ptr(youtubeURL),
            MimeType: interactions.VideoContentMimeTypeVideoMp4.ToPointer(),
        }),
        interactions.NewContent(interactions.TextContent{
            Text: prompt,
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(responseSchema),
            )),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

![แอป Gemini ที่ถอดเสียงแบบหลายภาษา](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=th)

## ป้อนเสียง

คุณระบุข้อมูลเสียงได้ด้วยวิธีต่อไปนี้

- [อัปโหลดไฟล์เสียง](#upload-audio)ก่อนส่งคำขอ
- [ส่งข้อมูลเสียงแบบอินไลน์](#inline-audio)พร้อมกับคำขอ

### อัปโหลดไฟล์เสียง

ใช้ [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) สำหรับไฟล์ที่มีขนาดใหญ่กว่า 20 MB

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

### Go

```
// Upload an audio file using the Files API (recommended for files > 20 MB)
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Describe this audio clip",
        }),
        interactions.NewContent(interactions.AudioContent{
            URI:      genai.Ptr(uploadedFile.URI),
            MimeType: interactions.AudioContentMimeType(uploadedFile.MIMEType).ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

### ส่งข้อมูลเสียงในบรรทัด

สำหรับไฟล์เสียงขนาดเล็กที่มีขนาดคำขอรวมไม่เกิน 20 MB ให้ทำดังนี้

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

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    audioBytes, err := os.ReadFile("path/to/small-sample.mp3")
    if err != nil {
        log.Fatal(err)
    }
    base64Audio := base64.StdEncoding.EncodeToString(audioBytes)

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Describe this audio clip",
        }),
        interactions.NewContent(interactions.AudioContent{
            Data:     genai.Ptr(base64Audio),
            MimeType: interactions.AudioContentMimeTypeAudioMp3.ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

หมายเหตุเกี่ยวกับข้อมูลเสียงในบรรทัด
\* ขนาดคำขอสูงสุดคือ 20 MB โดยรวม (รวมถึงพรอมต์และไฟล์ทั้งหมด)
\* หากต้องการนำกลับมาใช้ใหม่ ให้[อัปโหลดไฟล์](#upload-audio)แทน

## ดูข้อความถอดเสียง

หากต้องการรับข้อความถอดเสียง ให้ขอในพรอมต์โดยใช้คำสั่งต่อไปนี้

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Generate a transcript of the speech.",
        }),
        interactions.NewContent(interactions.AudioContent{
            URI:      genai.Ptr(uploadedFile.URI),
            MimeType: interactions.AudioContentMimeType(uploadedFile.MIMEType).ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

## ดูการประทับเวลา

ใช้รูปแบบ `MM:SS` เพื่ออ้างอิงส่วนที่เฉพาะเจาะจง

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    contents := []interactions.Content{
        interactions.NewContent(interactions.TextContent{
            Text: "Provide a transcript from 02:30 to 03:29.",
        }),
        interactions.NewContent(interactions.AudioContent{
            URI:      genai.Ptr(uploadedFile.URI),
            MimeType: interactions.AudioContentMimeType(uploadedFile.MIMEType).ToPointer(),
        }),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(contents),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

## นับโทเค็น

วิธีนับโทเค็นในไฟล์เสียง

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", &genai.UploadFileConfig{
        MIMEType: "audio/mp3",
    })
    if err != nil {
        log.Fatal(err)
    }

    response, err := client.Models.CountTokens(
        ctx,
        "gemini-3.8-flash",
        []*genai.Content{
            genai.NewContentFromURI(uploadedFile.URI, uploadedFile.MIMEType, genai.RoleUser),
        },
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(response.TotalTokens)
}
```

## รูปแบบเสียงที่รองรับ

Gemini รองรับประเภท MIME ของรูปแบบเสียงต่อไปนี้

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

ดูรายการประเภท MIME และสคีมาพารามิเตอร์ที่รองรับทั้งหมดได้ใน[เอกสารอ้างอิง Interactions API](https://ai.google.dev/api/interactions-api?hl=th#Resource:Content)

## รายละเอียดทางเทคนิคเกี่ยวกับเสียง

- **โทเค็น**: 32 โทเค็นต่อเสียง 1 วินาที (1 นาที = 1,920 โทเค็น)
- **เสียงที่ไม่ใช่เสียงพูด**: Gemini เข้าใจเสียงที่ไม่ใช่เสียงพูด (เสียงนกร้อง เสียงไซเรน ฯลฯ)
- **ความยาวสูงสุด**: เสียงยาว 9.5 ชั่วโมงต่อพรอมต์
- **ความละเอียด**: ดาวน์แซมเปิลเป็น 16 Kbps
- **ช่องสัญญาณ**: เสียงหลายช่องสัญญาณรวมเป็นช่องสัญญาณเดียว

## ขั้นตอนถัดไป

- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th): อัปโหลดและจัดการไฟล์เสียง
- [คำสั่งของระบบ](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#system-instructions)
  ปรับแต่งลักษณะการทำงานของโมเดล
- [เอาต์พุตที่มีโครงสร้าง](https://ai.google.dev/gemini-api/docs/structured-output?hl=th)
  รับผลการถอดเสียงในรูปแบบ JSON

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
