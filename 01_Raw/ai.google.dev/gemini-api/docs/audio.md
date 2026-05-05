---
source_url: https://ai.google.dev/gemini-api/docs/audio?hl=hi
fetched_at: 2026-05-05T20:49:56.040647+00:00
title: "\u0911\u0921\u093f\u092f\u094b \u0915\u094b \u0938\u092e\u091d\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# ऑडियो को समझना

Gemini, ऑडियो इनपुट का विश्लेषण करके टेक्स्ट में जवाब जनरेट कर सकता है.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=["Describe this audio clip", myfile]
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
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

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
        "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## खास जानकारी

Gemini, ऑडियो इनपुट का विश्लेषण और उसे समझकर, टेक्स्ट में जवाब जनरेट कर सकता है. इससे इन जैसे इस्तेमाल के उदाहरणों को पूरा किया जा सकता है:

- ऑडियो कॉन्टेंट के बारे में जानकारी देना, खास जानकारी देना या सवालों के जवाब देना.
- ऑडियो की ट्रांसक्रिप्ट और अनुवाद उपलब्ध कराना (बोली को टेक्स्ट में बदलना).
- बोली और संगीत में भावनाओं का पता लगाना.
- ऑडियो के खास सेगमेंट का विश्लेषण करना और टाइमस्टैंप उपलब्ध कराना.

फ़िलहाल, Gemini API, रीयल-टाइम ट्रांसक्रिप्ट के इस्तेमाल के उदाहरणों के साथ काम नहीं करता.
रीयल-टाइम में वॉइस और वीडियो इंटरैक्शन के लिए, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi) देखें.
रीयल-टाइम ट्रांसक्रिप्ट की सुविधा के साथ, बोली को टेक्स्ट में बदलने वाले मॉडल इस्तेमाल करने के लिए,
[Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text?hl=hi) का इस्तेमाल करें.

## बोली को टेक्स्ट में बदलना

इस उदाहरण वाले ऐप्लिकेशन में, Gemini API को बोली को ट्रांसक्रिप्ट करने,
उसका अनुवाद करने, और उसकी खास जानकारी देने के लिए प्रॉम्प्ट करने का तरीका दिखाया गया है. इसमें, स्ट्रक्चर्ड आउटपुट का इस्तेमाल करके टाइमस्टैंप और भावनाओं का पता लगाने की सुविधा भी शामिल है.
using [structured outputs](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi).

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
    model="gemini-3-flash-preview",
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
      response_mime_type="application/json",
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
    model: "gemini-3-flash-preview",
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
      responseMimeType: "application/json",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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
        "response_mime_type": "application/json",
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

[[AI Studio Build](https://aistudio.google.com/apps?e=0&hl=hi) को इस उदाहरण वाले ट्रांसक्रिप्ट ऐप्लिकेशन की तरह कोई ऐप्लिकेशन बनाने के लिए प्रॉम्प्ट किया जा सकता है. इसके लिए, आपको सिर्फ़ एक बटन पर क्लिक करना होगा.](https://aistudio.google.com/apps/bundled/echoscript?hl=hi)

![Gemini ऐप्लिकेशन, जो कई भाषाओं में ऑडियो ट्रांसक्रिप्शन की सुविधा देता है](https://ai.google.dev/static/gemini-api/docs/images/audio_understanding_demo.gif?hl=hi)

## ऑडियो इनपुट

Gemini को ऑडियो डेटा इन तरीकों से दिया जा सकता है:

- [कोई ऑडियो फ़ाइल अपलोड करना](#upload-audio) इससे पहले कि आप
  `generateContent` के लिए अनुरोध करें.
- [इनलाइन ऑडियो डेटा पास करें](#inline-audio) अनुरोध के साथ
  `generateContent`.

फ़ाइल इनपुट के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट के तरीके](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi) वाली गाइड देखें.

### ऑडियो फ़ाइल अपलोड करना

ऑडियो फ़ाइल अपलोड करने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) का इस्तेमाल किया जा सकता है.
Files API का इस्तेमाल हमेशा तब करें, जब अनुरोध का कुल साइज़ (जिसमें फ़ाइलें, टेक्स्ट प्रॉम्प्ट, सिस्टम के निर्देश वगैरह शामिल हैं) 20 एमबी से ज़्यादा हो.

यहां दिया गया कोड, एक ऑडियो फ़ाइल अपलोड करता है. इसके बाद, `generateContent` को कॉल करने के लिए, इस फ़ाइल का इस्तेमाल करता है.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=["Describe this audio clip", myfile]
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
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

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
      "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

मीडिया फ़ाइलों के साथ काम करने के बारे में ज़्यादा जानने के लिए, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=hi) देखें.

### इनलाइन ऑडियो डेटा पास करना

ऑडियो फ़ाइल अपलोड करने के बजाय, `generateContent` के लिए अनुरोध में इनलाइन ऑडियो डेटा पास किया जा सकता है:

### Python

```
from google import genai
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
  model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

### Go

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
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

इनलाइन ऑडियो डेटा के बारे में याद रखने योग्य कुछ बातें यहां बताई गई हैं:

- अनुरोध का ज़्यादा से ज़्यादा साइज़ 20 एमबी हो सकता है. इसमें टेक्स्ट प्रॉम्प्ट, सिस्टम के निर्देश, और इनलाइन दी गई फ़ाइलें शामिल हैं. अगर आपकी फ़ाइल के
  साइज़ की वजह से *अनुरोध का कुल साइज़* 20 एमबी से ज़्यादा हो जाता है, तो
  अनुरोध में इस्तेमाल करने के लिए, Files API का इस्तेमाल करके कोई ऑडियो फ़ाइल [अपलोड करें](#upload-audio).
- अगर किसी ऑडियो सैंपल का इस्तेमाल कई बार किया जा रहा है, तो ऑडियो फ़ाइल अपलोड करना ज़्यादा बेहतर है
  .

## ट्रांसक्रिप्ट पाना

ऑडियो डेटा की ट्रांसक्रिप्ट पाने के लिए, प्रॉम्प्ट में इसके बारे में पूछें:

### Python

```
from google import genai

client = genai.Client()
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
    "Generate a transcript of the speech.",
  ]),
});
console.log("result.text=", result.text);
```

### Go

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
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## टाइमस्टैंप का रेफ़रंस देना

`MM:SS` फ़ॉर्मैट वाले टाइमस्टैंप का इस्तेमाल करके, ऑडियो फ़ाइल के खास सेक्शन का रेफ़रंस दिया जा सकता है. उदाहरण के लिए, यहां दिया गया प्रॉम्प्ट, ऐसी ट्रांसक्रिप्ट का अनुरोध करता है जो

- फ़ाइल की शुरुआत से 2 मिनट 30 सेकंड पर शुरू होती है.
- फ़ाइल की शुरुआत से 3 मिनट 29 सेकंड पर खत्म होती है.

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

### Go

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
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

## टोकन की संख्या गिनना

किसी ऑडियो फ़ाइल में टोकन की संख्या जानने के लिए, `countTokens` तरीके को कॉल करें. उदाहरण के लिए:

### Python

```
from google import genai

client = genai.Client()
response = client.models.count_tokens(
  model='gemini-3-flash-preview',
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
  model: "gemini-3-flash-preview",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
  ]),
});
console.log(countTokensResponse.totalTokens);
```

### Go

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
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Printf("File %s is %d tokens\n", localAudioPath, tokens.TotalTokens)
}
```

## Google Podcasts के लिए इस्तेमाल किए जा सकने वाले ऑडियो फ़ॉर्मैट

Gemini, इन ऑडियो फ़ॉर्मैट के MIME टाइप के साथ काम करता है:

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF - `audio/aiff`
- AAC - `audio/aac`
- OGG Vorbis - `audio/ogg`
- FLAC - `audio/flac`

## ऑडियो के बारे में तकनीकी जानकारी

- Gemini, ऑडियो के हर सेकंड को 32 टोकन के तौर पर दिखाता है. उदाहरण के लिए, एक मिनट के ऑडियो को 1,920 टोकन के तौर पर दिखाया जाता है.
- Gemini, बोली के अलावा अन्य कॉम्पोनेंट को भी "समझ" सकता है. जैसे, पक्षियों के गाने या सायरन की आवाज़.
- एक प्रॉम्प्ट में, ऑडियो डेटा की ज़्यादा से ज़्यादा लंबाई 9.5 घंटे हो सकती है.
  Gemini, एक प्रॉम्प्ट में ऑडियो फ़ाइलों की *संख्या* पर कोई पाबंदी नहीं लगाता. हालांकि, एक प्रॉम्प्ट में सभी ऑडियो फ़ाइलों की कुल लंबाई 9.5 घंटे से ज़्यादा नहीं हो सकती.
- Gemini, ऑडियो फ़ाइलों को 16 केबीपीएस के डेटा रिज़ॉल्यूशन पर डाउनसैंपल करता है.
- अगर ऑडियो सोर्स में एक से ज़्यादा चैनल हैं, तो Gemini उन चैनलों को मिलाकर एक चैनल बना देता है.

## आगे क्या करना है

इस गाइड में, ऑडियो डेटा के जवाब में टेक्स्ट जनरेट करने का तरीका बताया गया है. ज़्यादा जानने के लिए, ये लेख पढ़ें और वीडियो देखें:

- [फ़ाइल के साथ प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे
  मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सिस्टम के निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions):
  सिस्टम के निर्देशों की मदद से, अपनी
  खास ज़रूरतों और इस्तेमाल के उदाहरणों के हिसाब से मॉडल के व्यवहार को कंट्रोल किया जा सकता है.
- [सुरक्षा से जुड़े दिशा-निर्देश](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=hi): कभी-कभी, जनरेटिव एआई
  मॉडल से ऐसे आउटपुट मिलते हैं जिनकी उम्मीद नहीं होती. जैसे, गलत, पक्षपात वाले या आपत्तिजनक आउटपुट. ऐसे आउटपुट से होने वाले नुकसान के जोखिम को कम करने के लिए, पोस्ट-प्रोसेसिंग और मैन्युअल तरीके से आकलन करना ज़रूरी है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-04-29 (UTC) को अपडेट किया गया."],[],[]]
