---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ar
fetched_at: 2026-05-11T05:07:33.888830+00:00
title: "\u0625\u0646\u0634\u0627\u0621 \u0645\u0648\u0633\u064a\u0642\u0649 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# إنشاء موسيقى باستخدام Lyria 3

‫Lyria 3 هي مجموعة نماذج من Google لإنشاء الموسيقى، وهي متاحة من خلال Gemini API. باستخدام Lyria 3، يمكنك إنشاء مقاطع صوتية مجسّمة عالية الجودة بتردد 44.1 كيلو هرتز من طلبات نصية أو من صور. تقدّم هذه النماذج محتوًى متماسكًا من الناحية البنيوية، بما في ذلك الغناء والكلمات المتزامنة والترتيبات الموسيقية الكاملة.

تتضمّن مجموعة Lyria 3 نموذجَين:

| الطراز | رقم تعريف الطراز | الأفضل لـ | المدة | الناتج |
| --- | --- | --- | --- | --- |
| **مقطع Lyria 3** | `lyria-3-clip-preview` | المقاطع القصيرة والحلقات المتكررة والمعاينات | ‫30 ثانية | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | أغانٍ كاملة تتضمّن مقاطع ولوازم وجسورًا موسيقية | بضع دقائق (يمكن التحكّم فيها من خلال الطلب) | MP3 |

يمكن استخدام كلا النموذجين من خلال طريقة `generateContent` العادية و[واجهة برمجة التطبيقات الجديدة Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar) التي تتيح إدخال بيانات متعددة الوسائط (نصوص وصور) وإنتاج صوت **استيريو عالي الدقة بتردد 44.1 كيلو هرتز**.

## إنشاء مقطع موسيقي

ينشئ نموذج Lyria 3 Clip دائمًا مقطعًا مدته **30 ثانية**. لإنشاء مقطع، استدعِ الدالة `generateContent` مع طلب نصي. يتضمّن الرد دائمًا الكلمات وبنية الأغنية التي تم إنشاؤها بالإضافة إلى الصوت.

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

### جافا

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

### #C

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

## إنشاء أغنية كاملة

استخدِم نموذج `lyria-3-pro-preview` لإنشاء أغانٍ كاملة المدة تستغرق بضع دقائق. يفهم نموذج Pro البنية الموسيقية ويمكنه إنشاء مقطوعات موسيقية تتضمّن مقاطع شعرية ولازمة وجسرًا موسيقيًا. يمكنك التأثير في المدة من خلال تحديدها في طلبك (مثلاً، "إنشاء أغنية مدتها دقيقتان") أو باستخدام [الطوابع الزمنية](#timing) لتحديد البنية.

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

### جافا

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

### #C

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound."
);
```

## اختيار تنسيق الإخراج

تنشئ نماذج Lyria 3 المحتوى الصوتي بتنسيق **MP3** تلقائيًا. بالنسبة إلى Lyria 3 Pro، يمكنك أيضًا طلب الإخراج بتنسيق **WAV** من خلال ضبط `response_format` في `generationConfig`.

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

### جافا

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

### #C

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

## تحليل الردّ

تتضمّن الاستجابة من Lyria 3 أجزاء متعدّدة. تحتوي الأجزاء النصية على كلمات الأغنية التي تم إنشاؤها أو وصف بتنسيق JSON لبنية الأغنية. تحتوي الأجزاء التي تتضمّن
`inline_data` على وحدات البايت الصوتية.

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

### جافا

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

### #C

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

## إنشاء موسيقى من الصور

يتوافق Lyria 3 مع الإدخالات المتعدّدة الوسائط، إذ يمكنك تقديم ما يصل إلى **10 صور** إلى جانب طلبك النصي، وسينشئ النموذج موسيقى مستوحاة من المحتوى المرئي.

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

### جافا

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

### #C

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

## تقديم كلمات أغنية مخصّصة

يمكنك كتابة كلمات الأغنية الخاصة بك وتضمينها في الطلب. استخدِم علامات الأقسام، مثل `[Verse]` و`[Chorus]` و`[Bridge]`، لمساعدة النموذج في فهم بنية الأغنية:

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

### جافا

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

### #C

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

## التحكّم في التوقيت والبنية

يمكنك تحديد ما يحدث بالضبط في لحظات معيّنة من الأغنية باستخدام الطوابع الزمنية. يفيد ذلك في التحكّم في وقت بدء الآلات الموسيقية ووقت عرض كلمات الأغنية وطريقة تقدّم الأغنية:

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

### جافا

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

### #C

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

## إنشاء مقاطع موسيقية بدون غناء

بالنسبة إلى الموسيقى الخلفية أو المقاطع الصوتية للألعاب أو أي حالة استخدام لا تتطلّب أصواتًا بشرية، يمكنك أن تطلب من النموذج إنشاء مقاطع موسيقية فقط:

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

### جافا

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-clip-preview",
    "A bright chiptune melody in C Major, retro 8-bit "
        + "video game style. Instrumental only, no vocals.");
```

### #C

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

## إنشاء موسيقى بلغات مختلفة

تنشئ Lyria 3 كلمات الأغاني باللغة التي تستخدمها في طلبك. لإنشاء أغنية
بكلمات فرنسية، اكتب طلبك باللغة الفرنسية. ويعدّل النموذج أسلوبه الصوتي وطريقة لفظه لتتطابق مع اللغة.

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

### جافا

```
GenerateContentResponse response = client.models.generateContent(
    "lyria-3-pro-preview",
    "Crée une chanson pop romantique en français sur un "
        + "coucher de soleil à Paris. Utilise du piano et de "
        + "la guitare acoustique.");
```

### #C

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

## ذكاء النموذج

يحلّل Lyria 3 عملية الطلب التي تتضمّن
النموذج الذي يحلّل البنية الموسيقية (المقدمة، والمقطع، والجوقة، والجسر الموسيقي، وما إلى ذلك)
استنادًا إلى طلبك.
يحدث ذلك قبل إنشاء الصوت ويضمن التماسك البنيوي والانسجام الموسيقي.

## واجهة Interactions API

يمكنك استخدام نماذج Lyria 3 مع [واجهة برمجة التطبيقات Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)، وهي واجهة موحّدة للتفاعل مع نماذج Gemini ووكلاء Gemini. فهي تبسّط إدارة الحالة والمهام الطويلة الأمد لحالات الاستخدام المعقّدة المتعدّدة الوسائط.

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

## دليل كتابة الطلبات

يمكن أن يكون طلبك بسيطًا، مثل "أغنية شعبية عن قطط لطيفة تتجنّب البرك،
أداء صوتي نسائي وصوت المطر"، أو مفصّلاً ومنظّمًا،
مثل:

> أغنية من نوع "سينثبوب" مستوحاة من الثمانينات، تتضمّن إيقاعًا حيويًا وأصواتًا خلفية براقة من آلات توليف وجوقة آسرة ومؤثرة. يجب أن تعكس الأغنية طابعًا قديمًا مستقبليًا،
> يذكّر بأغاني البوب الكلاسيكية من الثمانينات، مع لمسة عصرية. يجب أن يكون الإيقاع سريعًا ومناسبًا للرقص، حوالي 120 نبضة في الدقيقة، مع بنية واضحة من مقاطع شعرية ولازمة موسيقية، بالإضافة إلى لحن آلي جذاب. تتحدث كلمات الأغنية عن
> الشعور بالاستعداد لحفلة.

يمكن أن تمنحك الطلبات البسيطة والمعقّدة نتائج جيدة. ننصحك بتجربة هذه النصائح للعثور على ما يناسبك بشكل أفضل.

### النوع

ابدأ طلبك بنوع الموسيقى الذي تريده، مثل الهيب هوب والروك والراب. يمكنك تحديد مزيج من الأنواع الموسيقية:

- مزيج من موسيقى الروك والراب
- مزيج من موسيقى الموت والموسيقى الأوبرالية
- مقطوعة كلاسيكية تتضمّن عناصر إلكترونية
- موسيقى رقص إلكترونية حديثة (EDM) ممزوجة بموسيقى البوب الأوروبية

يمكنك أيضًا تضمين حقبة:

- موسيقى الهيب هوب في أوائل التسعينيات
- موسيقى "بوب" فرنسية من الستينيات
- تجارب إلكترونية في الثمانينيات
- موسيقى البوب الرائجة في العقد الأول من القرن الحادي والعشرين

إذا طلبت أنواعًا مخصّصة أو أشكالاً إقليمية، مثل "تكنو برلين" أو "هيفي من منطقة الخليج"، سيحاول النموذج التقاط هذا الجوهر، ولكن قد لا ينجح دائمًا في ذلك.

### آلات

ستنشئ Lyria 3 تلقائيًا أغاني تتضمّن الآلات الموسيقية والأدوات التي تتوقّعها لهذا النوع من الموسيقى. ليس عليك أن تكون إلزاميًا.

ومع ذلك، لن تتضمّن أغنية رقص مقطعًا من الساكسفون إلا إذا طلبت ذلك. لذا، إذا أردت معزوفة منفردة على الساكسفون، عليك تقديم الطلب التالي:

> أغنية رقص ذات إيقاع قوي وأصوات تركيبية براقة وجوقة جذابة تشبه الأغاني الوطنية يجب أن يكون هناك مقطع منفرد لآلة الساكسفون خلال الجزء الانتقالي.

يمكن أن يتضمّن طلبك آلات موسيقية محدّدة، وطريقة عزفها، وكيفية تفاعلها مع بعضها البعض. يمكنك استخدام هذه المجموعة لإنشاء بعض الأجواء أو الملمس:

- خطّ جهير مشوّه وغير واضح يتناغم مع أصوات قبّعات عالية واضحة ونقية
- أصوات خلفية دافئة من آلة توليف تناظرية تتصاعد تحت غيتار أكويستك بلمسة دافئة وقريبة
- جدار صوتي تم إنشاؤه من طبقات متعددة من غيتارات مشوّشة، مع أصوات غنائية بعيدة ومخفية

### بنية الأغنية

يمكنك تحديد تسلسل الأغنية في طلبك. استخدِم الأسهم أو القائمة لتحديد التسلسل:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- ابدأ بمقدمة هادئة على البيانو، ثم انتقِل إلى مقطع صوتي مرتفع، ثم إلى صمت، ثم إلى جوقة صاخبة.

يمكنك أيضًا تحديد كيفية تغيُّر مستويات الطاقة بين هذه الأقسام:

- بناء التشويق في المقطع التمهيدي، ثم الانتقال إلى الصمت قبل مقطع كورَس ضخم ومثير
- تصاعد تدريجي في مستوى الصوت طوال الأغنية، مع إضافة آلة موسيقية واحدة في كل مرة
  إلى أن يصبح الصوت صاخبًا
- توقّف مفاجئ بعد المقطع الانتقالي، يليه مقطع كورال بدون آلات موسيقية

يمكنك أيضًا تحديد الوقت الدقيق الذي تريد أن يحدث فيه أمر معيّن:

- إنشاء فيديو قصير مدته 12 ثانية
- يقول شخص ما "ماذا" كل ثانيتَين
- تبدأ اللازمة عند الثانية 22

### كلمات الأغنية

يتم إنشاء الأصوات الغنائية وكلمات الأغاني تلقائيًا. يمكنك تقديم كلمات الأغنية الخاصة بك أو طلب عدم تضمين كلمات (أو تضمين مقطوعة موسيقية فقط) أو توجيه عملية إنشاء الكلمات إلى الاتجاه الذي تريده.

ستكون كلمات الأغنية باللغة التي تكتب بها طلبك. يمكنك أيضًا طلب كتابة كلمات الأغنية بلغة أخرى، مثل "اكتب كلمات الأغنية باللغة الفرنسية".

#### استخدام كلمات الأغنية الخاصة بك

لتزويد النموذج بكلمات الأغاني الخاصة بك، عليك تضمينها في الطلب مع البادئة "Lyrics:" (كلمات الأغاني:)

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

يمكنك إضافة بادئة إلى أجزاء من الأغنية باستخدام عناوين أقسام مثل `[Intro]` و`[Verse 1]` و`[Pre-chorus]` و`[Chorus]` و`[Outro]`.

إذا أردت تكرار كلمة أو سطر، مثلاً كصدى أو من خلال المغنّين المساندين، يمكنك تضمينه بين قوسين: "هيا بنا (هيا بنا)".

#### توجيه الطلبات إلى النموذج لكتابة كلمات الأغاني

إذا أردت أن تنشئ لك Lyria 3 كلمات أغنية، من الأفضل تضمين تفاصيل حول موضوع الأغنية في طلبك. وإلا سيحتاج النموذج إلى استنتاج موضوع من طلبك الموسيقي، وقد لا يكون هذا الموضوع هو ما تريده.

> تتحدث كلمات الأغنية عن الحب الضائع وألم الانفصال. تتذكر المغنية علاقة سابقة والذكريات التي تعود إلى ذهنها.

إذا أردت الحصول على مقطع متكرّر، من المفيد أن تطلب ذلك في طلبك:

> تتحدث كلمات الأغنية عن الحب الضائع وألم الانفصال. تتذكر المغنية علاقة سابقة والذكريات التي تعود إلى ذهنها. وتركز اللازمة القوية على التغلّب على الألم والمضي قدمًا.

ستوجّه Lyria 3 تلقائيًا بنية كلمات الأغنية نحو نوع الموسيقى الذي تطلبه، ولكن يمكنك إعادة التأكيد على ذلك في طلبك أيضًا. على سبيل المثال:

> أغنية إلكترونية راقصة تكرّر العبارة الحماسية نفسها مرارًا وتكرارًا

يمكنك أيضًا طلب تأثيرات صوتية ليست كلمات أغنية، مثل:

- تتضمّن الأغنية عيّنة متكرّرة من فيلم تقول "لا أصدّق هذا!"
- أغنية تكنو حماسية، قبل أن تتوقف الموسيقى تمامًا ويقول صوت صغير "لا أعرف ما الذي أفعله هنا"، ثم تبدأ الموسيقى.
- تبدأ الأغنية بمحادثة حول أنّ الأفلام في التسعينيات كانت أفضل من الأفلام الحالية. ثم تنتقل الأغنية إلى أغنية بوب.

### الغناء

يمكنك تقديم طلب بشأن طريقة عرض كلمات الأغنية. للحصول على أفضل النتائج، حدِّد ملفًا شخصيًا مفصّلاً للمغني يشمل الجنس والنبرة والمجال الصوتي.

- **صوت نسائي عالٍ**: صوت واضح ونقي يتميّز بالخفة والارتفاع. تتميز بقدرتها على إصدار نغمات عالية صافية مع نسيج صوتي خفيف.
- **صوت ألتو نسائي**: نطاق صوتي منخفض غني ودافئ وأجش صوت مدخّن مع لمسة من صوت مقلي، صوت روحي ورنّان.
- **صوت التينور الرجالي**: صوت حاد ونشيط ومشرق نبرة صوت شبابية مع
  حدة أنفية طفيفة، تخترق المزيج بقوة عالية.
- **صوت رجالي منخفض**: عميق، ودافئ، وناعم. صوت جهوري
  رنان يقدّم أداءً هادئًا ومريحًا.
- **المغني المخضرم (ذكر)**: صوت أجش وخشن مع نبرة حادة،
  يذكّرنا بموسيقى الغرنج في التسعينيات. نطاق صوتي مرتفع متوتر للتعبير عن المشاعر القوية

### مَعلمات الطلبات الأخرى

يمكنك أيضًا تضمين هذه المَعلمات لتحسين طلبك بشكل أكبر:

- **المفتاح الموسيقي/المقياس الموسيقي**: حدِّد مفتاحًا موسيقيًا (مثل "في سلم G الكبير" أو "في سلم D الصغير").
- **المزاج والأجواء**: استخدِم صفات وصفية (مثل "حنين" أو "عدواني" أو "أثيري" أو "حالم").
- **المدة**: ينتج نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. بالنسبة إلى طراز Pro، حدِّد المدة المطلوبة في طلبك (مثلاً، "أريد إنشاء أغنية مدتها دقيقتان") أو استخدِم الطوابع الزمنية للتحكّم في المدة.

### أمثلة على الطلبات

إليك بعض الأمثلة على الطلبات الفعّالة:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## أفضل الممارسات

- **التكرار باستخدام Clip أولاً** استخدِم النموذج الأسرع `lyria-3-clip-preview` لتجربة الطلبات قبل الالتزام بإنشاء أغنية كاملة باستخدام `lyria-3-pro-preview`.
- **الدقة** تؤدي الطلبات الغامضة إلى نتائج عامة. اذكر الآلات الموسيقية وسرعة الإيقاع والمفتاح الموسيقي والحالة المزاجية والبنية للحصول على أفضل نتيجة.
- **استخدام علامات الأقسام** تمنح العلامات `[Verse]` و`[Chorus]` و`[Bridge]` النموذج بنية واضحة يجب اتّباعها.
- **فصل كلمات الأغنية عن التعليمات:** عند تقديم كلمات أغنية مخصّصة، يجب فصلها بوضوح عن تعليمات التوجيه الموسيقي.

## القيود

- **الأمان**: تتحقّق فلاتر الأمان من جميع الطلبات. سيتم حظر الطلبات التي تؤدي إلى تشغيل الفلاتر. ويشمل ذلك الطلبات التي تطلب أصوات فنّانين معيّنين أو إنشاء كلمات أغاني محمية بحقوق الطبع والنشر.
- **وضع العلامات المائية**: تتضمّن جميع المقاطع الصوتية التي يتم إنشاؤها [علامة مائية لمقطع صوتي من SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ar) لتحديدها. هذه العلامة المائية غير مسموعة بالأذن البشرية ولا تؤثر في تجربة الاستماع.
- **التعديل المتعدد**: عملية إنشاء الموسيقى هي عملية من خطوة واحدة.
  لا يتيح الإصدار الحالي من Lyria 3 تعديل المقاطع التي تم إنشاؤها أو تحسينها بشكل متكرر من خلال طلبات متعددة.
- **المدة**: ينشئ نموذج "المقطع" دائمًا مقاطع مدتها 30 ثانية. ينشئ نموذج Pro أغاني تستغرق بضع دقائق، ويمكن التأثير في المدة الدقيقة من خلال الطلب.
- **التحديد**: قد تختلف النتائج بين المكالمات، حتى مع استخدام الطلب نفسه.

## الخطوات التالية

- اطّلِع على [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) لنماذج Lyria 3
- جرِّب [إنشاء الموسيقى في الوقت الفعلي](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ar) مع
  ‫Lyria RealTime،
- إنشاء محادثات بين عدة أشخاص باستخدام
  [نماذج تحويل النص إلى كلام](https://ai.google.dev/gemini-api/docs/audio-generation?hl=ar)
- تعرَّف على كيفية إنشاء [صور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) أو [فيديوهات](https://ai.google.dev/gemini-api/docs/video?hl=ar).
- تعرَّف على كيفية [فهم Gemini للملفات الصوتية](https://ai.google.dev/gemini-api/docs/audio?hl=ar)،
- إجراء محادثة فورية مع Gemini باستخدام
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
