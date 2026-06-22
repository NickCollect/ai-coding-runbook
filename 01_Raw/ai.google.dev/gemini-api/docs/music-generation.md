---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=zh-TW
fetched_at: 2026-06-22T06:29:30.596616+00:00
title: "\u4f7f\u7528 Lyria 3 \u751f\u6210\u97f3\u6a02 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=zh-tw) 現已推出預先發布版，提供協作規劃、視覺化、MCP 支援等功能。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# 使用 Lyria 3 生成音樂

Lyria 3 是 Google 的音樂生成模型系列，可透過 Gemini API 使用。使用 Lyria 3，你可以根據文字提示或圖片生成高品質的 44.1 kHz 立體聲音訊。這些模型可提供結構一致的音樂，包括人聲、歌詞時間碼和完整樂器編曲。

Lyria 3 系列包含兩種模型：

| 型號 | 模型 ID | 適用情境 | 時間長度 | 輸出 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短片、循環播放、預覽 | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | 包含主歌、副歌和橋段的完整歌曲 | 幾分鐘 (可透過提示控制) | MP3 |

這兩款模型都可透過標準 `generateContent` 方法和新的 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) 使用，支援多模態輸入 (文字和圖片)，並產生 **44.1 kHz 高精準度立體聲**音訊。

## 生成音樂短片

Lyria 3 Clip 模型一律會生成 **30 秒**片段。如要生成短片，請使用文字提示呼叫 `generateContent` 方法。回應一律會包含生成的歌詞和歌曲結構，以及音訊。

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

## 生成完整歌曲

使用 `lyria-3-pro-preview` 模型生成幾分鐘的完整歌曲。Pro 模型可瞭解音樂結構，並創作具有不同主歌、副歌和橋段的樂曲。如要調整時長，可以在提示中指定 (例如「創作 2 分鐘的歌曲」)，或使用[時間戳記](#timing)定義結構。

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="An epic cinematic orchestral piece about a journey home. "
             "Starts with a solo piano intro, builds through sweeping "
             "strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text("An epic cinematic orchestral piece about a journey " +
               "home. Starts with a solo piano intro, builds through " +
               "sweeping strings, and climaxes with a massive wall of sound."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "An epic cinematic orchestral piece about a journey home. "
        + "Starts with a solo piano intro, builds through sweeping "
        + "strings, and climaxes with a massive wall of sound.");
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound."
);
```

## 選取輸出格式

根據預設，Lyria 3 模型會以 **MP3** 格式生成音訊。如果是 Lyria 3 Pro，您也可以在 `generationConfig` 中設定 `response_format`，要求以 **WAV** 格式輸出。

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
  contents: "An atmospheric ambient track.",
  config: config
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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

## 剖析回應

Lyria 3 的回覆包含多個部分，文字部分包含生成的歌詞或歌曲結構的 JSON 說明。含有音訊位元組的部分為 `inline_data`。

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

## 根據圖片生成音樂

Lyria 3 支援多模態輸入，除了文字提示詞，你最多還可提供 **10 張圖片**，模型會根據視覺內容創作音樂。

### Python

```
from PIL import Image

image = Image.open("desert_sunset.jpg")

response = client.models.generate_content(
    model="lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
    contents,
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
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
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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
  model: "lyria-3-pro-preview",
  contents: new List<Part> {
    Part.FromText("An atmospheric ambient track inspired by the mood and colors in this image."),
    Part.FromBytes(await File.ReadAllBytesAsync("desert_sunset.jpg"), "image/jpeg")
  }
);
```

![](https://storage.googleapis.com/generativeai-downloads/images/desert_sunset.jpg)

## 提供自訂歌詞

你可以自行撰寫歌詞，並加入提示。使用 `[Verse]`、`[Chorus]` 和 `[Bridge]` 等區段標記，協助模型瞭解歌曲結構：

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
    model="lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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

## 控制時間和結構

你可以使用時間戳記，指定歌曲在特定時間點的確切動作。這項功能有助於控制樂器進入的時間、歌詞的傳送時間，以及歌曲的進展方式：

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
    model="lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
    "lyria-3-pro-preview",
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
  model: "lyria-3-pro-preview",
  contents: prompt
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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

## 生成配樂

如要生成背景音樂、遊戲配樂或任何不需要人聲的音樂，可以提示模型生成純音樂曲目：

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

## 生成不同語言的音樂

Lyria 3 會以提示的語言生成歌詞。如要生成法文歌詞的歌曲，請用法文撰寫提示。模型會調整語音風格和發音，配合所選語言。

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="Crée une chanson pop romantique en français sur un "
             "coucher de soleil à Paris. Utilise du piano et de "
             "la guitare acoustique.",
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "lyria-3-pro-preview",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique.",

});
```

### Go

```
result, err := client.Models.GenerateContent(
    ctx,
    "lyria-3-pro-preview",
    genai.Text("Crée une chanson pop romantique en français sur un " +
               "coucher de soleil à Paris. Utilise du piano et de " +
               "la guitare acoustique."),
    nil,
)
```

### Java

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "Crée une chanson pop romantique en français sur un "
        + "coucher de soleil à Paris. Utilise du piano et de "
        + "la guitare acoustique.");
```

### C#

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "Crée une chanson pop romantique en français sur un " +
            "coucher de soleil à Paris. Utilise du piano et de " +
            "la guitare acoustique."
);
```

### REST

```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/lyria-3-pro-preview:generateContent" \
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

## 模型智慧

Lyria 3 會分析提示程序，根據提示透過音樂結構 (前奏、主歌、副歌、橋段等) 推理。這項程序會在生成音訊前執行，確保結構一致性和音樂性。

## 互動 API

您可以使用 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=zh-tw) 存取 Lyria 3 模型，這個 API 提供統一的介面，可與 Gemini 模型和代理程式互動。可簡化複雜多模態用途的狀態管理和長時間執行的工作。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A melancholic jazz fusion track in D minor, " +
          "featuring a smooth saxophone melody, walking bass line, " +
          "and complex drum rhythms.",
)

for output in interaction.outputs:
    if output.text:
        print(output.text)
    elif output.inline_data:
         with open("interaction_output.mp3", "wb") as f:
            f.write(output.inline_data.data)
         print("Audio saved to interaction_output.mp3")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'lyria-3-pro-preview',
  input: 'A melancholic jazz fusion track in D minor, ' +
         'featuring a smooth saxophone melody, walking bass line, ' +
         'and complex drum rhythms.',
});

for (const output of interaction.outputs) {
  if (output.text) {
    console.log(output.text);
  } else if (output.inlineData) {
    const buffer = Buffer.from(output.inlineData.data, 'base64');
    fs.writeFileSync('interaction_output.mp3', buffer);
    console.log('Audio saved to interaction_output.mp3');
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A melancholic jazz fusion track in D minor, featuring a smooth saxophone melody, walking bass line, and complex drum rhythms."
}'
```

## 提示撰寫指南

提示詞可以很簡單，例如「一首關於可愛貓咪躲避水窪的民謠，女聲演唱，並加入雨聲」，也可以詳細且有結構，例如：

> 這首 1980 年代風格的合成器流行樂曲節奏強勁、合成器音色閃耀，副歌朗朗上口，令人振奮。這首歌應帶有復古未來主義的感覺，讓人想起 80 年代的經典流行金曲，並以現代製作方式潤飾。節奏應歡快且適合跳舞，每分鐘約 120 拍，並有清晰的段落和副歌結構，以及令人難忘的樂器旋律。歌詞描述準備參加派對的心情。

簡單和複雜的提示都能產生良好的輸出內容。建議您嘗試這些訣竅，找出最適合自己的做法。

### 類型

在提示中加入想要的音樂類型，例如嘻哈、搖滾和饒舌。你可以指定多種類型：

- 融合金屬樂和饒舌
- 結合死亡金屬和歌劇
- 含有電子無人機元素的古典樂
- 現代電子舞曲 (EDM) 混合歐洲流行音樂

你也可以加入年代：

- 90 年代初期的嘻哈
- 60 年代法國 ye-ye 流行樂
- 80 年代的電子實驗
- 2000 年代主流流行樂

如果提示詞要求生成特定類型或地區變體，例如「柏林鐵克諾」或「灣區 hyphy」，模型會嘗試捕捉該本質，但可能不一定能正確生成。

### 樂器

根據預設，Lyria 3 會使用該音樂類型常見的樂器和工具製作歌曲。不必提供具體的建議。

不過，除非你要求，否則舞曲不會包含薩克斯風。因此，如要生成薩克斯風獨奏，請輸入以下提示：

> 這首舞曲節奏強勁、合成器閃閃發光，副歌朗朗上口，橋段應加入薩克斯風獨奏。

提示可以包括特定樂器、樂器發出的聲音，以及樂器之間的互動方式。您可以運用這種組合營造特定情緒或質感：

- 扭曲的低音線與乾淨俐落的 Hi-Hat 鼓點相互抗衡
- 溫暖的類比合成器墊音在乾燥親切的木吉他下方膨脹
- 多層模糊吉他音效打造的音牆，以及埋在其中的遠處人聲

### 歌曲結構

你可以在提示中列出歌曲的進展。使用箭頭或清單定義流程：

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- 先以輕柔的鋼琴前奏開場，接著進入激昂的段落，然後突然靜默，再爆發進入副歌。

你也可以指定這些區段之間的能量變化：

- 在副歌前營造緊張感，然後在爆發力十足的副歌前歸於寂靜
- 整首歌曲的音量逐漸變大，一次加入一種樂器，直到形成混亂的音牆
- 在橋段後突然停止，接著是無伴奏合唱

你也可以提示要執行動作的確切時間：

- 在 12 秒時建構至高點
- 每隔 2 秒說一次「什麼」
- 副歌從 22 秒開始

### 歌詞

系統預設會生成人聲和歌詞。你可以提供自己的歌詞、要求不要歌詞 (或純音樂)，或引導歌詞生成朝你想要的方向發展。

歌詞會以您輸入提示時使用的語言呈現。你也可以要求以其他語言撰寫歌詞，例如「用法文撰寫歌詞」。

#### 使用自訂歌詞

如要讓模型使用你提供的歌詞，請在提示中加入歌詞，並加上「歌詞：」前置字元：

```
Lyrics:

[Intro]
Oooh, oooh

[Verse 1]
Let's go
Let's go
Go with the flow

[Chorus]
...
```

你可以在歌曲的各個部分加上前置字串，例如 `[Intro]`、`[Verse 1]`、`[Pre-chorus]`、`[Chorus]` 和 `[Outro]`。

如要重複某個字或一行，例如回音或和聲，請將其放在括號中：「Let's go (go)」。

#### 提示模型撰寫歌詞

如要讓 Lyria 3 為你創作歌詞，建議在提示中加入歌詞內容的詳細資訊。否則模型必須從音樂提示推斷主題，結果可能不符合你的需求。

> 歌詞內容是關於失去愛情和心碎的痛苦。這位歌手回憶起過去的戀情，以及隨之湧現的記憶。

如要重複播放副歌，請在提示中要求：

> 歌詞內容是關於失去愛情和心碎的痛苦。歌手回憶起過去的戀情，以及隨之湧現的記憶。強而有力的副歌著重於克服痛苦並繼續前進。

Lyria 3 會根據你要求的音樂類型，自動調整歌詞結構，但你也可以在提示中重新強調這一點。例如：

> EDM 歌曲，不斷重複相同的活力四射詞組。

你也可以提示加入非歌詞的聲音效果，例如：

- 歌曲中不斷重複電影中的「我不敢相信！」片段
- 在音樂即將進入高潮前，所有聲音都會停止，然後出現一個小小的聲音說「我不知道我在這裡做什麼」，接著音樂就會進入高潮。
- 這首歌曲的開頭是關於 90 年代電影比現今電影更優秀的對話。接著，這首曲目會轉場至流行歌曲。

### 人聲

你可以提示歌詞的呈現方式，為獲得最佳效果，請詳細指定歌手的個人資料，包括性別、音色和音域。

- **女高音**：音色清澈如水晶，音質靈活高亢。能以輕柔的氣音唱出高音。
- **女中音**：低音域豐富、溫暖且沙啞，帶有煙燻感，略帶聲帶顫音，充滿靈魂且共鳴感十足。
- **男高音**：明亮、高亢、充滿活力。音色年輕，略帶鼻音，高音爆發力十足，能穿透混音。
- **男中音**：深沉、如巧克力般濃郁，且如天鵝絨般柔滑。渾厚胸腔共鳴聲，以輕柔的吟唱方式呈現。
- **飽經風霜的搖滾歌手 (男聲)**：嗓音沙啞粗獷，音色低沉，讓人想起 90 年代的垃圾搖滾。情緒強度過高。

### 其他提示參數

您也可以加入下列參數，進一步調整提示：

- **調性/音階**：指定調性 (例如「G 大調」、「D 小調」)。
- **情緒和氛圍**：使用描述性形容詞 (例如「懷舊」、「激進」、「空靈」、「夢幻」)。
- **長度**：短片模型一律會生成 30 秒的短片。如果是 Pro 模型，請在提示中指定所需長度 (例如「創作 2 分鐘的歌曲」)，或使用時間戳記控制長度。

### 提示詞範例

以下列舉幾個有效的提示：

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 最佳做法

- **先使用 Clip 進行疊代。**使用速度較快的 `lyria-3-clip-preview` 模型測試提示，再使用 `lyria-3-pro-preview` 生成完整長度的內容。
- 提供**清楚明確**的說明，模糊不清的提示會產生一般結果。提及樂器、BPM、調性、情境和結構，以獲得最佳輸出內容。
- **使用章節標記。**`[Verse]`、`[Chorus]`、`[Bridge]` 標記可為模型提供明確的結構。
- **歌詞和指示請分開提供。**提供自訂歌詞時，請清楚區隔歌詞和音樂方向指示。

## 限制

- **安全性**：所有提示都會經過安全篩選器檢查。系統會封鎖觸發篩選器的提示。包括要求特定藝人聲音的提示，或是生成受著作權保護的歌詞。
- **浮水印**：所有生成的音訊都會加上 [SynthID 音訊浮水印](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=zh-tw)，以利識別。這種浮水印人耳無法辨識，不會影響聆聽體驗。
- **多輪編輯**：音樂生成是單輪程序。目前版本的 Lyria 3 不支援透過多個提示詞，反覆編輯或修正生成的片段。
- **長度**：Clip 模型一律會生成 30 秒的短片。Pro 模型會生成幾分鐘的歌曲，確切時長取決於提示。
- **決定性**：即使使用相同提示，每次呼叫的結果也可能不同。

## 後續步驟

- 查看 Lyria 3 模型的[定價](https://ai.google.dev/gemini-api/docs/pricing?hl=zh-tw)，
- 使用 Lyria RealTime [即時串流音樂生成](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=zh-tw)，
- 使用 [TTS 模型](https://ai.google.dev/gemini-api/docs/speech-generation?hl=zh-tw)生成多人對話，
- 瞭解如何生成[圖片](https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-tw)或[影片](https://ai.google.dev/gemini-api/docs/video?hl=zh-tw)，
- 瞭解 Gemini 如何[解讀音訊檔案](https://ai.google.dev/gemini-api/docs/audio?hl=zh-tw)、
- 使用 [Live API](https://ai.google.dev/gemini-api/docs/live?hl=zh-tw) 與 Gemini 即時對話。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-06-19 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-06-19 (世界標準時間)。"],[],[]]
