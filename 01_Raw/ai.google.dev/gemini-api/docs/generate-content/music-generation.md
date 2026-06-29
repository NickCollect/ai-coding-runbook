---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=ja
fetched_at: 2026-06-29T05:29:07.822808+00:00
title: "Lyria 3 \u3067\u97f3\u697d\u3092\u751f\u6210\u3059\u308b \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Lyria 3 で音楽を生成する

Lyria 3 は、Gemini API を介して利用できる Google の音楽生成モデル ファミリーです。Lyria 3 を使用すると、テキスト プロンプトや画像から、高品質の 44.1 kHz ステレオ音声を生成できます。これらのモデルは、ボーカル、タイミングに合わせた歌詞、完全なインストゥルメンタル アレンジなど、構造的な一貫性を提供します。

Lyria 3 ファミリーには次の 2 つのモデルが含まれています。

| モデル | モデル ID | 最適な用途 | 所要時間 | 出力 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 短いクリップ、ループ、プレビュー | 30 秒 | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | A メロ、サビ、ブリッジのあるフルレングスの曲 | 数分（プロンプトで制御可能） | MP3 |

どちらのモデルも、標準の `generateContent` メソッドと新しい [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) を使用して使用できます。マルチモーダル入力（テキストと画像）をサポートし、**44.1 kHz の高忠実度ステレオ**音声を生成します。

## 音楽クリップを生成する

Lyria 3 Clip モデルは、常に **30 秒**のクリップを生成します。クリップを生成するには、テキスト プロンプトを使用して `generateContent` メソッドを呼び出します。レスポンスには、常に生成された歌詞と曲の構成が音声とともに含まれます。

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

## フルレングスの曲を生成する

`lyria-3-pro-preview` モデルを使用して、数分間のフルレングスの曲を生成します。Pro モデルは音楽の構成を理解し、明確な A メロ、サビ、ブリッジを含む楽曲を作成できます。プロンプトで指定する（「2 分間の曲を作成して」など）か、[タイムスタンプ](#timing)を使用して構造を定義することで、長さに影響を与えることができます。

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

## 出力形式を選択する

デフォルトでは、Lyria 3 モデルは **MP3** 形式で音声を生成します。Lyria 3 Pro では、`generationConfig` で `response_format` を設定して、**WAV** 形式で出力をリクエストすることもできます。

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

## レスポンスをパースする

Lyria 3 からのレスポンスには複数のパートが含まれています。テキスト部分には、生成された歌詞または曲の構成の JSON 記述が含まれます。`inline_data` を含むパーツには音声バイトが含まれます。

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

## 画像から音楽を生成する

Lyria 3 はマルチモーダル入力をサポートしています。テキスト プロンプトとともに最大 **10 枚の画像**を提供すると、モデルは視覚的なコンテンツにインスピレーションを得た音楽を作曲します。

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

## カスタム歌詞を提供する

独自の歌詞を書いて、プロンプトに含めることができます。`[Verse]`、`[Chorus]`、`[Bridge]` などのセクション タグを使用して、モデルが曲の構成を理解できるようにします。

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

## タイミングと構造を制御する

タイムスタンプを使用すると、曲の特定の瞬間に何が起こるかを正確に指定できます。これは、楽器の開始タイミング、歌詞の配信タイミング、曲の進行方法を制御するのに役立ちます。

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

## インストゥルメンタル トラックを生成する

バックグラウンド ミュージック、ゲームのサウンドトラック、ボーカルを必要としないユースケースでは、モデルにインストゥルメンタルのみのトラックを生成するように指示できます。

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

## さまざまな言語で音楽を生成する

Lyria 3 は、プロンプトの言語で歌詞を生成します。フランス語の歌詞を含む曲を生成するには、プロンプトをフランス語で記述します。モデルは、言語に合わせて音声スタイルと発音を調整します。

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

## モデル インテリジェンス

Lyria 3 は、プロンプトに基づいてモデルが音楽構造（イントロ、ヴァース、コーラス、ブリッジなど）を推論するプロンプト プロセスを分析します。これはオーディオが生成される前に行われ、構造的な一貫性と音楽性が確保されます。

## Interactions API

Lyria 3 モデルは、Gemini モデルとエージェントを操作するための統合インターフェースである [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) で使用できます。複雑なマルチモーダル ユースケースの状態管理と長時間実行タスクを簡素化します。

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

## プロンプト ガイド

プロンプトは、「かわいい猫が水たまりを避けるフォークソング、女性ボーカルと雨の音」のような簡単なものでも、次のような詳細で構造化されたものでもかまいません。

> ドライビング ビート、きらめくシンセサイザー、キャッチーでアンセムのようなコーラスが特徴の、1980 年代風のシンセポップ トラック。レトロフューチャリスティックな雰囲気で、80 年代のクラシックなポップ ヒットを彷彿とさせるような曲にしてください。現代的なプロダクションの磨きをかけてください。テンポはアップビートで踊りやすい、120 BPM 程度。明確なヴァースとコーラスの構成で、印象的なインストゥルメンタルのフックがある。歌詞はパーティーの準備をしているときの気持ちについてです。

単純なプロンプトと複雑なプロンプトの両方で、適切な出力を得ることができます。これらのヒントを試して、自分に最適な方法を見つけることをおすすめします。

### ジャンル

プロンプトの先頭に、ヒップホップ、ロック、ラップなど、希望する音楽のジャンルを指定します。ジャンルを組み合わせて指定できます。

- メタルとラップの融合
- デスメタルとオペラの組み合わせ
- 電子ドローン要素を含むクラシック音楽
- モダンなエレクトロニック ダンス ミュージック（EDM）とユーロポップをミックス

時代を組み込むこともできます。

- 90 年代初頭のヒップホップ
- 60 年代のフレンチ イエイエ ポップ
- 80 年代のエレクトロニック実験
- 2000 年代のメインストリーム ポップ

「ベルリン テクノ」や「ベイエリア ハイフィー」などの特定のジャンルや地域バリエーションをリクエストすると、モデルはその本質を捉えようとしますが、必ずしも正しく捉えられるとは限りません。

### 楽器

デフォルトでは、Lyria 3 はジャンルに合った楽器とツールを使用して曲を作成します。指示的である必要はありません。

ただし、ダンス トラックにサックスを含めるには、リクエストする必要があります。サックスのソロをリクエストする場合は、次のようにプロンプトを入力する必要があります。

> ドライビング ビート、きらめくシンセサイザー、キャッチーでアンセムのようなコーラスが特徴のダンス トラック。ブリッジでサックスのソロが入るようにしてください。

プロンプトには、特定の楽器、その音、楽器同士の相互作用を含めることができます。この組み合わせを使用して、特定の雰囲気やテクスチャを作成できます。

- 汚れた歪んだベースラインと、クリーンでキレのあるハイハットが対立している
- 暖かくアナログなシンセサイザーのパッドが、ドライで親密なアコースティック ギターの下で盛り上がっていく
- ファジーなギターの音が何層にも重なり、埋もれたような遠いボーカルが聞こえるサウンドウォール

### 曲の構成

プロンプトで曲の進行を概説できます。矢印またはリストを使用してフローを定義します。

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- 静かなピアノのイントロから始まり、大きな音量のバースに移行し、静寂に落ち、コーラスで爆発します。

これらのセクション間のエネルギー レベルの変化を指定することもできます。

- プリコーラスで緊張感を高め、コーラスの直前で静寂に落とす
- 曲全体を通して徐々にクレッシェンドし、楽器を 1 つずつ追加して、混沌とした音の壁を築き上げる
- ブリッジの後に突然停止し、アカペラのコーラスが続く

特定の時刻に何かを実行するよう指示することもできます。

- 12 秒でドロップにビルド
- 2 秒ごとに「何？」と言う
- サビは 22 秒から始まります

### 歌詞

ボーカルと歌詞はデフォルトで生成されます。独自の歌詞を指定したり、歌詞なし（またはインストゥルメンタル）をリクエストしたり、歌詞の生成を希望する方向に誘導したりできます。

歌詞は、プロンプトの言語で作成されます。「歌詞をフランス語で書いて」など、別の言語で歌詞をリクエストすることもできます。

#### 独自の歌詞を使用する

モデルに独自の歌詞を指定するには、プロンプトに「歌詞:」という接頭辞を付けて歌詞を含めます。

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

曲の一部に、`[Intro]`、`[Verse 1]`、`[Pre-chorus]`、`[Chorus]`、`[Outro]` などのセクション タイトルをプレフィックスとして追加できます。

エコーやバック シンガーのように、単語や行を繰り返したい場合は、「Let's go (go)」のように、かっこで囲みます。

#### 歌詞の作成をモデルに指示する

Lyria 3 に歌詞を作成させる場合は、歌詞の内容に関する詳細をプロンプトに含めることをおすすめします。そうしないと、モデルは音楽プロンプトから被写体を推測する必要があり、ユーザーが望むものとは異なる可能性があります。

> 歌詞は、失恋と失恋の痛みを歌っています。歌手は過去の恋愛と、そのときに感じた思い出を振り返っています。

コーラスを繰り返したい場合は、プロンプトでそのように指定するとよいでしょう。

> 歌詞は、失恋と失恋の痛みを歌っています。歌手は過去の恋愛と、そのときに感じた思い出を回想しています。力強いコーラスは、痛みを乗り越えて前進することに焦点を当てています。

Lyria 3 は、リクエストされた音楽のタイプに合わせて歌詞の構成を自動的に調整しますが、プロンプトでこの点を強調することもできます。次に例を示します。

> 同じエネルギッシュなフレーズを何度も繰り返す EDM トラック。

歌詞以外のボーカル効果を求めることもできます。たとえば、次のようにします。

- 映画の「信じられない！」というセリフが曲全体にわたって繰り返されている
- ドロップの直前に音がすべて止まり、「I don't know what I'm doing here」（ここで何をしているのかわからない）という小さな声が聞こえ、その後音楽がドロップする、ハイエナジーなテクノ トラック。
- この曲は、90 年代の映画は今よりも優れていたという会話から始まります。その後、ポップソングに移行します。

### ボーカル

歌詞の表示方法をプロンプトで指定できます。最適な結果を得るには、性別、音色、音域をカバーする詳細な歌手のプロフィールを指定します。

- **女性ソプラノ**: 透明感のあるクリスタルのような音色で、軽快で伸びのある音質。息の混じったエアリーなテクスチャで、口笛のような高音を出すことができます。
- **女性アルト**: 豊かで温かみのあるハスキーな低音域。スモーキーな音色で、ボーカル フライのニュアンスがあり、ソウルフルで共鳴する。
- **男性テノール**: 明るく、鋭く、エネルギッシュ。若々しい音色で、鼻にかかったようなわずかなエッジがあり、高いベルティング パワーでミックスを切り裂く。
- **男性バリトン**: 深みがあり、チョコレートのような滑らかさ。心地よい歌声で、胸に響くような声。
- **Weathered Rocker（男性）**: 90 年代のグランジを彷彿とさせる、ザラつきのある質感と砂利のような音色。感情の強さの上限を超えている。

### その他のプロンプト パラメータ

これらのパラメータを含めて、プロンプトをさらに調整することもできます。

- **キー/スケール**: 音楽のキーを指定します（例: 「ト長調」、「ニ短調」）。
- **ムードと雰囲気**: 説明的な形容詞（「ノスタルジック」、「アグレッシブ」、「幽玄」、「夢のような」など）を使用します。
- **再生時間**: クリップモデルは常に 30 秒のクリップを生成します。Pro モデルの場合は、プロンプトで希望する長さを指定するか（例: 「2 分間の曲を作成して」）、タイムスタンプを使用して長さを制御します。

### プロンプトの例

効果的なプロンプトの例を次に示します。

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## ベスト プラクティス

- **まず Clip でイテレーションを行います。**高速な `lyria-3-clip-preview` モデルを使用して、`lyria-3-pro-preview` でフルレングスの生成をコミットする前にプロンプトをテストします。
- **具体的に記述しましょう。**曖昧なプロンプトでは、一般的な結果が生成されます。最適な出力を得るために、楽器、BPM、キー、ムード、構成について言及します。
- **セクションタグを使用します。**`[Verse]`、`[Chorus]`、`[Bridge]` タグを使用すると、モデルが従うべき明確な構造が提供されます。
- **歌詞と手順を分ける。**カスタム歌詞を提供する場合は、音楽の指示と明確に区別してください。

## 制限事項

- **安全性**: すべてのプロンプトは安全フィルタによってチェックされます。フィルタをトリガーするプロンプトはブロックされます。これには、特定のアーティストの声や著作権で保護された歌詞の生成をリクエストするプロンプトが含まれます。
- **透かし**: 生成されたすべての音声には、識別用の [SynthID オーディオ ウォーターマーク](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ja)が含まれます。この透かしは人間の耳には聞こえず、リスニング体験に影響しません。
- **マルチターン編集**: 音楽生成はシングルターン プロセスです。現在のバージョンの Lyria 3 では、複数のプロンプトを使用して生成されたクリップを繰り返し編集または調整することはできません。
- **長さ**: クリップモデルは常に 30 秒のクリップを生成します。Pro モデルでは、数分間の曲が生成されます。正確な長さはプロンプトで調整できます。
- **決定論**: 同じプロンプトでも、呼び出しごとに結果が異なる場合があります。

## 次のステップ

- Lyria 3 モデルの[料金](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=ja)を確認する。
- Lyria RealTime を使用して、[リアルタイムのストリーミング音楽生成](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=ja)をお試しください。
- [TTS モデル](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=ja)を使用して複数の話者による会話を生成する。
- [画像](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=ja)や[動画](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=ja)を生成する方法について説明します。
- Gemini が[音声ファイルを理解する](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=ja)仕組みについて説明します。
- [Live API](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=ja) を使用して、Gemini とリアルタイムで会話できます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-23 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-23 UTC。"],[],[]]
