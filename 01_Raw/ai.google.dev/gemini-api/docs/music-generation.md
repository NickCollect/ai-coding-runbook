---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ja
fetched_at: 2026-09-21T05:57:03.051551+00:00
title: "Lyria 3.5 \u3067\u97f3\u697d\u3092\u751f\u6210\u3059\u308b \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Lyria 3.5 で音楽を生成する

Lyria 3.5 は、Gemini API を介して利用できる Google の音楽生成モデル ファミリーです。Lyria 3.5 を使用すると、テキスト プロンプトや画像から、高品質の 44.1 kHz ステレオ音声を生成できます。これらのモデルは、ボーカル、タイミング付きの歌詞、完全な楽器の編曲など、構造的な一貫性を提供します。

Lyria ファミリーには次のモデルが含まれています。

| モデル | モデル ID | 最適な用途 | 所要時間 | 出力 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | ショート クリップ、ループ、プレビュー | 30 秒 | MP3 |
| **Lyria 3.5** | `lyria-3.5` | A メロ、サビ、ブリッジのあるフルレングスの曲 | 数分（プロンプトで制御可能） | MP3 |

どちらのモデルも新しい [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) を使用して利用できます。マルチモーダル入力（テキストと画像）をサポートし、**44.1 kHz の高忠実度ステレオ**音声を生成します。

## 音楽クリップを生成する

Lyria 3 Clip モデルは常に **30 秒**のクリップを生成します。クリップを生成するには、テキスト プロンプトを使用して `interactions.create` メソッドを呼び出します。レスポンスには、常に生成された歌詞と楽曲の構成が、`steps` スキーマの音声とともに含まれます。

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

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
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(InteractionsInput.of("A short instrumental acoustic guitar piece."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("music.mp3"), audioBytes);
}

interaction.outputText().ifPresent(lyrics -> System.out.println("Lyrics:\n" + lyrics));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

生成された音楽データは、`interaction.output_audio` プロパティを使用して取得できます。このプロパティは、最後に生成されたオーディオ ブロックを返します。`interaction.output_text` プロパティを使用して、曲の歌詞と構成を取得することもできます。コンビニエンス プロパティの詳細については、[インタラクションの概要](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja#convenience-properties)をご覧ください。

## フルレングスの曲を生成する

`lyria-3.5` モデルを使用して、数分間のフルレングスの曲を生成します。Pro モデルは音楽の構成を理解し、明確な A メロ、サビ、ブリッジを含む楽曲を作成できます。プロンプトで指定する（「2 分間の曲を作成して」など）か、[タイムスタンプ](#timing)を使用して構造を定義することで、長さに影響を与えることができます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## 出力形式を選択する

デフォルトでは、Lyria 3.5 モデルは **MP3** 形式で音声を生成します。Lyria 3.5 では、`response_format` を設定して **WAV** 形式で出力をリクエストすることもできます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A beautiful piano melody."))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## レスポンスをパースする

Lyria 3.5 からのレスポンスには、`steps` スキーマ内に複数のコンテンツ ブロックが含まれています。インタラクションは一連のステップを返します。`model_output` ステップには生成されたコンテンツが含まれます。テキスト コンテンツ ブロックには、生成された歌詞または曲の構成の JSON 記述が含まれます。`audio` タイプのコンテンツ ブロックには、base64 でエンコードされた音声データが含まれます。

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] audioBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  Files.write(Paths.get("output.mp3"), audioBytes);
}

if (interaction.outputText().isPresent()) {
  System.out.println("Lyrics:\n" + interaction.outputText().get());
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### 歌詞と音楽が交互に表示される

Lyria 3.5 の出力は複雑で、生成された歌詞（テキスト）と楽曲自体（音声）の個別のステップとブロックが含まれているため、利便性プロパティは高速で推奨されるショートカットを提供します。

ただし、サーバーから返されたステップの未加工のタイムラインをプログラムで完全に制御したい場合（受信した個々のコンテンツ ブロックをログに記録するなど）は、代わりに `steps` を手動で反復処理できます。

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

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

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of("A song about a starry night."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

List<String> lyrics = new ArrayList<>();
byte[] audioData = null;

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof AudioContent) {
            AudioContent audioBlock = (AudioContent) contentBlock;
            if (audioBlock.data().isPresent()) {
              audioData = Base64.getDecoder().decode(audioBlock.data().get());
            }
          } else if (contentBlock instanceof TextContent) {
            TextContent textBlock = (TextContent) contentBlock;
            textBlock.text().ifPresent(lyrics::add);
          }
        }
      }
    }
  }
}

if (!lyrics.isEmpty()) {
  System.out.println("Lyrics:\n" + String.join("\n", lyrics));
}

if (audioData != null) {
  Files.write(Paths.get("output.mp3"), audioData);
}
```

## 画像から音楽を生成する

Lyria 3.5 はマルチモーダル入力をサポートしています。`input` リストでテキスト プロンプトとともに最大 **10 枚の画像**を指定すると、モデルは視覚的なコンテンツからインスピレーションを得て音楽を作曲します。

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
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

byte[] imageBytes = Files.readAllBytes(Paths.get("desert_sunset.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

Content textContent =
    TextContent.builder()
        .text("An atmospheric ambient track inspired by the mood and colors in this image.")
        .build();
Content imageContent =
    ImageContent.builder()
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .data(imageB64)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction response =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "Create a dreamy indie pop song with the following lyrics:\n\n"
        + "[Verse 1]\n"
        + "Walking through the neon glow,\n"
        + "city lights reflect below,\n"
        + "every shadow tells a story,\n"
        + "every corner, fading glory.\n\n"
        + "[Chorus]\n"
        + "We are the echoes in the night,\n"
        + "burning brighter than the light,\n"
        + "hold on tight, don't let me go,\n"
        + "we are the echoes down below.\n\n"
        + "[Verse 2]\n"
        + "Footsteps lost on empty streets,\n"
        + "rhythms sync to heartbeats,\n"
        + "whispers carried by the breeze,\n"
        + "dancing through the autumn leaves.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

String prompt =
    "[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.\n"
        + "[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals singing about a rainy morning.\n"
        + "[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics are hopeful and uplifting.\n"
        + "[0:50 - 1:00] Outro: Fade out with the piano melody alone.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## インストゥルメンタル トラックを生成する

BGM、ゲームのサウンドトラック、ボーカルを必要としないユースケースでは、モデルにインストゥルメンタルのみのトラックを生成するように指示できます。

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-clip-preview"))
        .input(
            InteractionsInput.of(
                "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## さまざまな言語で音楽を生成する

Lyria 3.5 は、プロンプトの言語で歌詞を生成します。フランス語の歌詞を含む曲を生成するには、プロンプトをフランス語で記述します。モデルは、言語に合わせて音声スタイルと発音を調整します。

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3.5"))
        .input(
            InteractionsInput.of(
                "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## モデル インテリジェンス

Lyria 3.5 は、プロンプトに基づいてモデルが音楽構造（イントロ、ヴァース、コーラス、ブリッジなど）を推論するプロンプト プロセスを分析します。これはオーディオが生成される前に行われ、構造的な一貫性と音楽性が確保されます。

## プロンプト ガイド

音楽のジャンル、楽器、曲の構成、カスタム歌詞、ボーカルのスタイルに効果的なプロンプトを作成する方法については、[Lyria プロンプト ガイド](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=ja)をご覧ください。

## ベスト プラクティス

- **まず Clip でイテレーションを行います。**高速な `lyria-3-clip-preview` モデルを使用して、`lyria-3.5` でフルレングスの生成をコミットする前にプロンプトをテストします。
- **具体的に記述しましょう。**曖昧なプロンプトでは、ありきたりな結果しか得られません。最適な出力を得るために、楽器、BPM、キー、ムード、構造について言及します。
- **言語を一致させます。**歌詞の言語でプロンプトを入力します。
- **セクションタグを使用します。**`[Verse]`、`[Chorus]`、`[Bridge]` タグを使用すると、モデルが従うべき明確な構造が提供されます。
- **歌詞と指示を分ける。**カスタム歌詞を指定する場合は、音楽の指示と明確に区別してください。

## 制限事項

- **安全性**: すべてのプロンプトは安全フィルタによってチェックされます。フィルタをトリガーするプロンプトはブロックされます。これには、特定のアーティストの音声や著作権で保護された歌詞の生成をリクエストするプロンプトが含まれます。
- **透かし**: 生成されたすべての音声には、識別用の [SynthID オーディオ ウォーターマーク](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ja)が含まれています。この透かしは人間の耳には聞こえず、リスニング体験に影響しません。
- **マルチターン編集**: 音楽生成はシングルターン プロセスです。現在のバージョンの Lyria 3.5 では、複数のプロンプトを使用して生成されたクリップを繰り返し編集または調整することはできません。
- **長さ**: クリップモデルは常に 30 秒のクリップを生成します。Pro モデルでは、数分間の曲が生成されます。正確な長さはプロンプトで調整できます。
- **決定論**: 同じプロンプトでも、呼び出しごとに結果が異なる場合があります。

## 次のステップ

- Lyria 3.5 モデルの[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja)を確認する。
- Lyria RealTime で[リアルタイムのストリーミング音楽生成](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ja)を試してみましょう。
- [TTS モデル](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ja)を使用して、複数の話者による会話を生成します。
- [画像](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja)や[動画](https://ai.google.dev/gemini-api/docs/video?hl=ja)を生成する方法をご確認ください。
- Gemini が[音声ファイルを理解する](https://ai.google.dev/gemini-api/docs/audio?hl=ja)仕組みを確認する。
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) を使用して、Gemini とリアルタイムで会話できます。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-09-18 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-09-18 UTC。"],[],[]]
