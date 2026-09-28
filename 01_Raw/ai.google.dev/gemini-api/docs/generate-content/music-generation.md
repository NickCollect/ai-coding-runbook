---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=th
fetched_at: 2026-09-28T06:11:53.120629+00:00
title: "\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e40\u0e1e\u0e25\u0e07\u0e14\u0e49\u0e27\u0e22 Lyria 3.5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/generate-content?hl=th)

ส่งความคิดเห็น

# สร้างเพลงด้วย Lyria 3.5

Lyria 3.5 คือกลุ่มโมเดลการสร้างเพลงของ Google ซึ่งพร้อมให้บริการผ่าน Gemini API Lyria 3.5 ช่วยให้คุณสร้างเสียงสเตอริโอคุณภาพสูง 44.1 kHz
จากพรอมต์ข้อความหรือจากรูปภาพได้ โมเดลเหล่านี้ให้ความสอดคล้องเชิงโครงสร้าง
ซึ่งรวมถึงเสียงร้อง เนื้อเพลงที่กำหนดเวลา และการเรียบเรียงดนตรีบรรเลงทั้งหมด

ตระกูล Lyria มีโมเดลต่อไปนี้

| รุ่น | รหัสโมเดล | เหมาะสำหรับ | ระยะเวลา | เอาต์พุต |
| --- | --- | --- | --- | --- |
| **คลิป Lyria 3** | `lyria-3-clip-preview` | คลิปสั้น ลูป ตัวอย่าง | 30 วินาที | MP3 |
| **Lyria 3.5** | `lyria-3.5` | เพลงเต็มความยาวที่มีท่อนร้อง คอรัส และบริดจ์ | 2-3 นาที (ควบคุมได้ผ่านพรอมต์) | MP3 |

คุณสามารถใช้ทั้ง 2 โมเดลได้โดยใช้เมธอด `generateContent` มาตรฐานและ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) ใหม่ ซึ่งรองรับอินพุตแบบมัลติโมดัล (ข้อความและรูปภาพ) และสร้างเสียง **สเตอริโอความเที่ยงตรงสูง 44.1 kHz**

## สร้างมิวสิกคลิป

โมเดลคลิป Lyria 3 จะสร้างคลิปความยาว **30 วินาที**เสมอ หากต้องการสร้าง
คลิป ให้เรียกใช้เมธอด `generateContent` ด้วยพรอมต์ข้อความ คำตอบจะมีเนื้อเพลงและโครงสร้างเพลงที่สร้างขึ้นพร้อมกับเสียงเสมอ

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents="Create a 30-second cheerful acoustic folk song with "
             "guitar and harmonica.",
)

# Parse the response
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        with open("clip.mp3", "wb") as f:
            f.write(part.inline_data.data)
        print("Audio saved to clip.mp3")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "lyria-3-clip-preview",
    contents: "Create a 30-second cheerful acoustic folk song with " +
              "guitar and harmonica.",

  });

  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const buffer = Buffer.from(part.inlineData.data, "base64");
      fs.writeFileSync("clip.mp3", buffer);
      console.log("Audio saved to clip.mp3");
    }
  }
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "lyria-3-clip-preview",
        genai.Text("Create a 30-second cheerful acoustic folk song " +
                   "with guitar and harmonica."),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    for _, part := range result.Candidates[0].Content.Parts {
        if part.Text != "" {
            fmt.Println(part.Text)
        } else if part.InlineData != nil {
            err := os.WriteFile("clip.mp3", part.InlineData.Data, 0644)
            if err != nil {
                log.Fatal(err)
            }
            fmt.Println("Audio saved to clip.mp3")
        }
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.Part;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class GenerateMusicClip {
  public static void main(String[] args) throws IOException {

    try (Client client = new Client()) {
      GenerateContentResponse response = client.models.generateContent(
          "lyria-3-clip-preview",
          "Create a 30-second cheerful acoustic folk song with "
              + "guitar and harmonica.");

      for (Part part : response.parts()) {
        if (part.text().isPresent()) {
          System.out.println(part.text().get());
        } else if (part.inlineData().isPresent()) {
          var blob = part.inlineData().get();
          if (blob.data().isPresent()) {
            Files.write(Paths.get("clip.mp3"), blob.data().get());
            System.out.println("Audio saved to clip.mp3");
          }
        }
      }
    }
  }
}
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-clip-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a 30-second cheerful acoustic folk song with guitar and harmonica."}
      ]
    }]
  }'
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;
using System.IO;

public class GenerateMusicClip {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "lyria-3-clip-preview",
      contents: "Create a 30-second cheerful acoustic folk song with guitar and harmonica."
    );

    foreach (var part in response.Candidates[0].Content.Parts) {
      if (part.Text != null) {
        Console.WriteLine(part.Text);
      } else if (part.InlineData != null) {
        await File.WriteAllBytesAsync("clip.mp3", part.InlineData.Data);
        Console.WriteLine("Audio saved to clip.mp3");
      }
    }
  }
}
```

## สร้างเพลงแบบเต็มความยาว

ใช้โมเดล `lyria-3.5` เพื่อสร้างเพลงแบบเต็มความยาว 2-3 นาที โมเดล Pro เข้าใจโครงสร้างดนตรีและสามารถสร้าง
ผลงานที่มีท่อนร้อง คอรัส และบริดจ์ที่แตกต่างกัน คุณสามารถกำหนดระยะเวลาได้โดยระบุในพรอมต์ (เช่น "สร้างเพลง 2 นาที") หรือโดยใช้[การประทับเวลา](#timing)เพื่อกำหนดโครงสร้าง

### Python

```
response = client.models.generate_content(
    model="lyria-3.5",
    contents="An epic cinematic orchestral piece about a journey home. "
             "Starts with a solo piano intro, builds through sweeping "
             "strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    genai.Text("An epic cinematic orchestral piece about a journey " +
               "home. Starts with a solo piano intro, builds through " +
               "sweeping strings, and climaxes with a massive wall of sound."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    "An epic cinematic orchestral piece about a journey home. "
        + "Starts with a solo piano intro, builds through sweeping "
        + "strings, and climaxes with a massive wall of sound.");
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."}
      ]
    }]
  }'
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound."
);
```

## เลือกรูปแบบเอาต์พุต

โดยค่าเริ่มต้น โมเดล Lyria 3.5 จะสร้างเสียงในรูปแบบ **MP3** สำหรับ Lyria 3.5 คุณยังขอเอาต์พุตในรูปแบบ **WAV** ได้ด้วยโดยตั้งค่า
`response_format` ใน `generationConfig`

### Python

```
from google.genai import types

response = client.models.generate_content(
    model="lyria-3.5",
    contents="An atmospheric ambient track.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO", "TEXT"],
        response_format={"audio": {"mime_type": "audio/wav"}},
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: "An atmospheric ambient track.",
  config: {
    responseModalities: ["AUDIO", "TEXT"],
    responseFormat: { audio: { mimeType: "audio/wav" } },
  },
});
```

### Go

```
config := &genai.GenerateContentConfig{
    ResponseModalities: []string{"AUDIO", "TEXT"},
    ResponseMIMEType:   "audio/wav",
}

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    genai.Text("An atmospheric ambient track."),
    config,
)
```

### Java

```
GenerateContentConfig config = GenerateContentConfig.builder()
    .responseModalities("AUDIO", "TEXT")
    .responseFormat(ResponseFormat.builder().audio(AudioFormat.builder().mimeType("audio/wav").build()).build())
    .build();

GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    "An atmospheric ambient track.",
    config);
```

### C#

```
var config = new GenerateContentConfig {
  ResponseModalities = { "AUDIO", "TEXT" },
  ResponseMimeType = "audio/wav"
};

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: "An atmospheric ambient track.",
  config: config
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "An atmospheric ambient track."}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO", "TEXT"],
      "responseFormat": { "audio": { "mimeType": "audio/wav" } }
    }
  }'
```

## แยกวิเคราะห์คำตอบ

การตอบกลับจาก Lyria 3.5 มีหลายส่วน ส่วนข้อความมีเนื้อเพลงที่
สร้างขึ้นหรือคำอธิบายโครงสร้างเพลงในรูปแบบ JSON ส่วนที่มี
`inline_data` จะมีไบต์เสียง

### Python

```
lyrics = []
audio_data = None

for part in response.parts:
    if part.text is not None:
        lyrics.append(part.text)
    elif part.inline_data is not None:
        audio_data = part.inline_data.data

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const part of response.candidates[0].content.parts) {
  if (part.text) {
    lyrics.push(part.text);
  } else if (part.inlineData) {
    audioData = Buffer.from(part.inlineData.data, "base64");
  }
}

if (lyrics.length) {
  console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
  fs.writeFileSync("output.mp3", audioData);
}
```

### Go

```
var lyrics []string
var audioData []byte

for _, part := range result.Candidates[0].Content.Parts {
    if part.Text != "" {
        lyrics = append(lyrics, part.Text)
    } else if part.InlineData != nil {
        audioData = part.InlineData.Data
    }
}

if len(lyrics) > 0 {
    fmt.Println("Lyrics:\n" + strings.Join(lyrics, "\n"))
}

if audioData != nil {
    err := os.WriteFile("output.mp3", audioData, 0644)
    if err != nil {
        log.Fatal(err)
    }
}
```

### Java

```
List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

for (Part part : response.parts()) {
  if (part.text().isPresent()) {
    lyrics.add(part.text().get());
  } else if (part.inlineData().isPresent()) {
    audioData = part.inlineData().get().data().get();
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
}
```

### C#

```
var lyrics = new List<string>();
byte[] audioData = null;

foreach (var part in response.Candidates[0].Content.Parts) {
  if (part.Text != null) {
    lyrics.Add(part.Text);
  } else if (part.InlineData != null) {
    audioData = part.InlineData.Data;
  }
}

if (lyrics.Count > 0) {
  Console.WriteLine("Lyrics:\n" + string.Join("\n", lyrics));
}

if (audioData != null) {
  await File.WriteAllBytesAsync("output.mp3", audioData);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' | base64 -d > output.mp3
```

## สร้างเพลงจากรูปภาพ

Lyria 3.5 รองรับอินพุตหลายรูปแบบ โดยคุณสามารถระบุ**รูปภาพได้สูงสุด 10 ภาพ**
พร้อมกับพรอมต์ข้อความ แล้วโมเดลจะแต่งเพลงที่ได้รับแรงบันดาลใจจาก
เนื้อหาภาพ

### Python

```
from PIL import Image

image = Image.open("desert_sunset.jpg")

response = client.models.generate_content(
    model="lyria-3.5",
    contents=[
        "An atmospheric ambient track inspired by the mood and "
        "colors in this image.",
        image,
    ],
)
```

### JavaScript

```
const imageData = fs.readFileSync("desert_sunset.jpg");
const base64Image = imageData.toString("base64");

const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: [
    { text: "An atmospheric ambient track inspired by the mood " +
            "and colors in this image." },
    {
      inlineData: {
        mimeType: "image/jpeg",
        data: base64Image,
      },
    },
  ],

});
```

### Go

```
imgData, err := os.ReadFile("desert_sunset.jpg")
if err != nil {
    log.Fatal(err)
}

parts := []*genai.Part{
    genai.NewPartFromText("An atmospheric ambient track inspired " +
        "by the mood and colors in this image."),
    &genai.Part{
        InlineData: &genai.Blob{
            MIMEType: "image/jpeg",
            Data:     imgData,
        },
    },
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    contents,
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    Content.fromParts(
        Part.fromText("An atmospheric ambient track inspired by "
            + "the mood and colors in this image."),
        Part.fromBytes(
            Files.readAllBytes(Path.of("desert_sunset.jpg")),
            "image/jpeg")));
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"contents\": [{
      \"parts\":[
          {\"text\": \"An atmospheric ambient track inspired by the mood and colors in this image.\"},
          {
            \"inline_data\": {
              \"mime_type\":\"image/jpeg\",
              \"data\": \"<BASE64_IMAGE_DATA>\"
            }
          }
      ]
    }]
  }"
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: new List<Part> {
    Part.FromText("An atmospheric ambient track inspired by the mood and colors in this image."),
    Part.FromBytes(await File.ReadAllBytesAsync("desert_sunset.jpg"), "image/jpeg")
  }
);
```

![](https://storage.googleapis.com/generativeai-downloads/images/desert_sunset.jpg)

## ระบุเนื้อเพลงที่กำหนดเอง

คุณสามารถเขียนเนื้อเพลงของคุณเองและใส่ไว้ในพรอมต์ได้ ใช้แท็กส่วน
เช่น `[Verse]`, `[Chorus]` และ `[Bridge]` เพื่อช่วยให้โมเดลเข้าใจโครงสร้างเพลง

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

response = client.models.generate_content(
    model="lyria-3.5",
    contents=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: prompt,

});
```

### Go

```
prompt := `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    genai.Text(prompt),
    nil,
)
```

### Java

```
String prompt = """
    Create a dreamy indie pop song with the following lyrics:

    [Verse 1]
    Walking through the neon glow,
    city lights reflect below,
    every shadow tells a story,
    every corner, fading glory.

    [Chorus]
    We are the echoes in the night,
    burning brighter than the light,
    hold on tight, don't let me go,
    we are the echoes down below.

    [Verse 2]
    Footsteps lost on empty streets,
    rhythms sync to heartbeats,
    whispers carried by the breeze,
    dancing through the autumn leaves.
    """;

GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    prompt);
```

### C#

```
var prompt = @"
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
";

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a dreamy indie pop song with the following lyrics: ..."}
      ]
    }]
  }'
```

[

](https://storage.googleapis.com/generativeai-downloads/songs/Neon%20Echoes_Lyrics.webm)

## ควบคุมเวลาและโครงสร้าง

คุณสามารถระบุสิ่งที่เกิดขึ้นในช่วงเวลาที่เฉพาะเจาะจงในเพลงได้โดยใช้
การประทับเวลา ซึ่งมีประโยชน์ในการควบคุมเวลาที่เครื่องดนตรีเริ่มเล่น เวลาที่เนื้อเพลง
ปรากฏ และวิธีที่เพลงดำเนินไป ดังนี้

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

response = client.models.generate_content(
    model="lyria-3.5",
    contents=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: prompt,

});
```

### Go

```
prompt := `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`

result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    genai.Text(prompt),
    nil,
)
```

### Java

```
String prompt = """
    [0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
                  vinyl crackle.
    [0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
                  and gentle vocals singing about a rainy morning.
    [0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
                  synth leads. The lyrics are hopeful and uplifting.
    [0:50 - 1:00] Outro: Fade out with the piano melody alone.
    """;

GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    prompt);
```

### C#

```
var prompt = @"
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
";

var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "[0:00 - 0:10] Intro: ..."}
      ]
    }]
  }'
```

## สร้างแทร็กบรรเลง

สำหรับเพลงประกอบ ซาวด์แทร็กเกม หรือกรณีการใช้งานใดๆ ที่ไม่จำเป็นต้องมีเสียงร้อง คุณสามารถแจ้งให้โมเดลสร้างแทร็กที่มีเฉพาะดนตรีได้โดยทำดังนี้

### Python

```
response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents="A bright chiptune melody in C Major, retro 8-bit "
             "video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-clip-preview",
  contents: "A bright chiptune melody in C Major, retro 8-bit " +
            "video game style. Instrumental only, no vocals.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-clip-preview",
    genai.Text("A bright chiptune melody in C Major, retro 8-bit " +
               "video game style. Instrumental only, no vocals."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-clip-preview",
    "A bright chiptune melody in C Major, retro 8-bit "
        + "video game style. Instrumental only, no vocals.");
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-clip-preview",
  contents: "A bright chiptune melody in C Major, retro 8-bit " +
            "video game style. Instrumental only, no vocals."
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-clip-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."}
      ]
    }]
  }'
```

## สร้างเพลงในภาษาต่างๆ

Lyria 3.5 จะสร้างเนื้อเพลงในภาษาของพรอมต์ หากต้องการสร้างเพลง
ที่มีเนื้อร้องเป็นภาษาฝรั่งเศส ให้เขียนพรอมต์เป็นภาษาฝรั่งเศส โมเดลจะปรับรูปแบบการร้อง
และการออกเสียงให้ตรงกับภาษา

### Python

```
response = client.models.generate_content(
    model="lyria-3.5",
    contents="Crée une chanson pop romantique en français sur un "
             "coucher de soleil à Paris. Utilise du piano et de "
             "la guitare acoustique.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3.5",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3.5",
    genai.Text("Crée une chanson pop romantique en français sur un " +
               "coucher de soleil à Paris. Utilise du piano et de " +
               "la guitare acoustique."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3.5",
    "Crée une chanson pop romantique en français sur un "
        + "coucher de soleil à Paris. Utilise du piano et de "
        + "la guitare acoustique.");
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3.5",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique."
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3.5:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."}
      ]
    }]
  }'
```

## ความสามารถของโมเดล

Lyria 3.5 จะวิเคราะห์กระบวนการพรอมต์ของคุณ โดยโมเดลจะพิจารณาโครงสร้างดนตรี (ท่อนนำ ท่อนร้อง คอรัส บริดจ์ ฯลฯ)
ตามพรอมต์ของคุณ
ซึ่งจะเกิดขึ้นก่อนที่จะสร้างเสียง และช่วยให้มั่นใจได้ถึงความสอดคล้องของโครงสร้างและความเป็นดนตรี

## Interactions API

คุณสามารถใช้โมเดล Lyria 3.5 กับ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) ซึ่งเป็นอินเทอร์เฟซแบบรวมสำหรับการโต้ตอบกับโมเดลและเอเจนต์ของ Gemini
ซึ่งช่วยลดความซับซ้อน
ในการจัดการสถานะและงานที่ใช้เวลานานสำหรับกรณีการใช้งานหลายรูปแบบที่ซับซ้อน

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3.5",
    input="A melancholic jazz fusion track in D minor, " +
          "featuring a smooth saxophone melody, walking bass line, " +
          "and complex drum rhythms.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("interaction_output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))
    print("Audio saved to interaction_output.mp3")

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'lyria-3.5',
  input: 'A melancholic jazz fusion track in D minor, ' +
         'featuring a smooth saxophone melody, walking bass line, ' +
         'and complex drum rhythms.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('interaction_output.mp3', Buffer.from(generatedAudio.data, 'base64'));
  console.log('Audio saved to interaction_output.mp3');
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A melancholic jazz fusion track in D minor, featuring a smooth saxophone melody, walking bass line, and complex drum rhythms."
}'
```

## คำแนะนำในการเขียนพรอมต์

ดูวิธีสร้างพรอมต์ที่มีประสิทธิภาพสำหรับแนวเพลง เครื่องดนตรี โครงสร้างเพลง เนื้อเพลงที่กำหนดเอง และสไตล์การร้องได้ที่[คู่มือการใช้พรอมต์ของ Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=th)

## แนวทางปฏิบัติแนะนำ

- **ทำซ้ำด้วยฟีเจอร์คลิปก่อน** ใช้`lyria-3-clip-preview`โมเดลที่เร็วกว่าเพื่อ
  ทดลองใช้พรอมต์ก่อนที่จะสร้างเนื้อหาแบบเต็มด้วย
  `lyria-3.5`
- **ใช้คำที่เฉพาะเจาะจง** พรอมต์ที่คลุมเครือจะให้ผลลัพธ์ทั่วไป ระบุเครื่องดนตรี
  BPM, คีย์, อารมณ์ และโครงสร้างเพื่อให้ได้ผลลัพธ์ที่ดีที่สุด
- **เลือกภาษาที่ต้องการ** ป้อนพรอมต์ในภาษาที่คุณต้องการให้เนื้อเพลงเป็น
- **ใช้แท็กส่วน** แท็ก `[Verse]`, `[Chorus]`, `[Bridge]` ช่วยให้โมเดลมีโครงสร้างที่ชัดเจน
  ให้ทำตาม
- **แยกเนื้อเพลงออกจากวิธีการ** เมื่อระบุเนื้อเพลงที่กำหนดเอง ให้แยกเนื้อเพลงออกจากคำสั่งเกี่ยวกับทิศทางดนตรีอย่างชัดเจน

## ข้อจำกัด

- **ความปลอดภัย**: ตัวกรองความปลอดภัยจะตรวจสอบพรอมต์ทั้งหมด ระบบจะบล็อกพรอมต์ที่ทริกเกอร์
  ตัวกรอง ซึ่งรวมถึงพรอมต์ที่ขอเสียงของศิลปินที่เฉพาะเจาะจง
  หรือการสร้างเนื้อเพลงที่มีลิขสิทธิ์
- **การใส่ลายน้ำ**: เสียงที่สร้างขึ้นทั้งหมดจะมี[ลายน้ำเสียง SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=th) สำหรับการระบุตัวตน ลายน้ำนี้จะมองไม่เห็นด้วยตาเปล่าและ
  ไม่ส่งผลต่อประสบการณ์การฟัง
- **การแก้ไขแบบผ่านการสนทนาไปมา**: การสร้างเพลงเป็นกระบวนการแบบครั้งเดียว
  การแก้ไขซ้ำหรือการปรับแต่งคลิปที่สร้างขึ้นผ่านพรอมต์หลายรายการ
  ไม่รองรับใน Lyria เวอร์ชัน 3.5 ปัจจุบัน
- **ความยาว**: โมเดลคลิปจะสร้างคลิปความยาว 30 วินาทีเสมอ โมเดล Pro
  สร้างเพลงที่มีความยาว 2-3 นาที โดยระยะเวลาที่แน่นอนจะ
  ขึ้นอยู่กับพรอมต์ของคุณ
- **การกำหนด**: ผลลัพธ์อาจแตกต่างกันไปในแต่ละการเรียกใช้ แม้จะใช้พรอมต์เดียวกันก็ตาม

## ขั้นตอนถัดไป

- ดู[ราคา](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=th)ของโมเดล Lyria 3.5
- ลอง[การสร้างเพลงแบบสตรีมมิงแบบเรียลไทม์](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=th)ด้วย
  Lyria RealTime
- สร้างการสนทนาที่มีผู้พูดหลายคนด้วย[โมเดล TTS](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=th)
- ดูวิธีสร้าง[รูปภาพ](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=th)หรือ[วิดีโอ](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=th)
- ดูว่า Gemini [เข้าใจไฟล์เสียง](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=th)ได้อย่างไร
- สนทนากับ Gemini แบบเรียลไทม์โดยใช้
  [Live API](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-18 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-18 UTC"],[],[]]
