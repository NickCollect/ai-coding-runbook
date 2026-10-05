---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=id
fetched_at: 2026-10-05T06:28:35.395566+00:00
title: "Membuat musik dengan Lyria 3.5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

Kirim masukan

# Membuat musik dengan Lyria 3.5

Lyria 3.5 adalah serangkaian model pembuatan musik Google, yang tersedia melalui Gemini API. Dengan Lyria 3.5, Anda dapat menghasilkan audio stereo 44, 1 kHz berkualitas tinggi dari perintah teks atau dari gambar. Model ini memberikan koherensi struktural, termasuk vokal, lirik yang disesuaikan waktunya, dan aransemen instrumental lengkap.

Keluarga Lyria mencakup model:

| Model | ID Model | Paling cocok untuk | Durasi | Output |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Klip pendek, loop, pratinjau | 30 detik | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Lagu berdurasi penuh dengan bait, refrain, jembatan | Beberapa menit (dapat dikontrol melalui perintah) | MP3 |

Kedua model dapat digunakan menggunakan metode `generateContent` standar dan [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) baru, yang mendukung input multimodal (teks dan gambar), serta menghasilkan audio **stereo fidelitas tinggi 44,1 kHz**.

## Membuat klip musik

Model Klip Lyria 3 selalu menghasilkan klip **30 detik**. Untuk membuat klip, panggil metode `generateContent` dengan perintah teks. Respons selalu
mencakup lirik dan struktur lagu yang dibuat bersama dengan audio.

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

## Membuat lagu berdurasi penuh

Gunakan model `lyria-3.5` untuk membuat lagu berdurasi penuh yang berdurasi beberapa menit. Model Pro memahami struktur musik dan dapat membuat komposisi dengan bait, refrain, dan jembatan yang berbeda. Anda dapat memengaruhi
durasi dengan menentukannya dalam perintah (misalnya, "buat lagu berdurasi 2 menit") atau dengan
menggunakan [stempel waktu](#timing) untuk menentukan struktur.

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

## Pilih format output

Secara default, model Lyria 3.5 menghasilkan audio dalam format **MP3**. Untuk
Lyria 3.5, Anda juga dapat meminta output dalam format **WAV** dengan menyetel
`response_format` di `generationConfig`.

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

## Mengurai respons

Respons dari Lyria 3.5 berisi beberapa bagian. Bagian teks berisi lirik yang dibuat atau deskripsi JSON dari struktur lagu. Bagian dengan
`inline_data` berisi byte audio.

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

## Membuat musik dari gambar

Lyria 3.5 mendukung input multimodal — Anda dapat memberikan hingga **10 gambar** bersama dengan perintah teks Anda dan model akan membuat musik yang terinspirasi oleh konten visual tersebut.

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

## Menyediakan lirik kustom

Anda dapat menulis lirik Anda sendiri dan menyertakannya dalam perintah. Gunakan tag bagian
seperti `[Verse]`, `[Chorus]`, dan `[Bridge]` untuk membantu model memahami
struktur lagu:

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

## Mengontrol waktu dan struktur

Anda dapat menentukan secara tepat apa yang terjadi pada momen tertentu dalam lagu menggunakan stempel waktu. Hal ini berguna untuk mengontrol kapan instrumen masuk, kapan lirik
disampaikan, dan bagaimana progres lagu:

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

## Membuat trek instrumental

Untuk musik latar, soundtrack game, atau kasus penggunaan apa pun yang tidak memerlukan vokal, Anda dapat meminta model untuk menghasilkan trek khusus instrumental:

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

## Membuat musik dalam berbagai bahasa

Lyria 3.5 membuat lirik dalam bahasa perintah Anda. Untuk membuat lagu dengan lirik dalam bahasa Prancis, tulis perintah Anda dalam bahasa Prancis. Model ini menyesuaikan gaya
vokal dan pengucapannya agar sesuai dengan bahasa.

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

## Kecerdasan model

Lyria 3.5 menganalisis proses perintah Anda saat model melakukan penalaran melalui struktur musik (intro, bait, chorus, jembatan, dll.) berdasarkan perintah Anda.
Hal ini terjadi sebelum audio dibuat dan memastikan koherensi struktural dan musikalitas.

## Interactions API

Anda dapat menggunakan model Lyria 3.5 dengan [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id);
antarmuka terpadu untuk berinteraksi dengan model dan agen Gemini. Alat ini menyederhanakan pengelolaan status dan tugas yang berjalan lama untuk kasus penggunaan multimodal yang kompleks.

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

## Panduan penulisan perintah

Untuk mempelajari cara membuat perintah yang efektif untuk genre musik, instrumen,
struktur lagu, lirik kustom, dan gaya penyampaian vokal, lihat
[panduan perintah Lyria](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=id).

## Praktik terbaik

- **Lakukan iterasi dengan Klip terlebih dahulu.** Gunakan model `lyria-3-clip-preview` yang lebih cepat untuk bereksperimen dengan perintah sebelum melakukan pembuatan video panjang dengan `lyria-3.5`.
- **Jadilah spesifik.** Perintah yang tidak jelas akan menghasilkan hasil yang umum. Sebutkan instrumen,
  BPM, nada dasar, mood, dan struktur untuk output terbaik.
- **Cocokkan bahasa Anda.** Berikan perintah dalam bahasa yang Anda inginkan untuk liriknya.
- **Gunakan tag bagian.** Tag `[Verse]`, `[Chorus]`, `[Bridge]` memberikan struktur yang jelas untuk diikuti model.
- **Pisahkan lirik dari petunjuk.** Saat memberikan lirik kustom, pisahkan dengan jelas dari petunjuk arahan musik Anda.

## Batasan

- **Keamanan**: Semua perintah diperiksa oleh filter keamanan. Perintah yang memicu
  filter akan diblokir. Hal ini mencakup perintah yang meminta suara artis tertentu atau pembuatan lirik yang dilindungi hak cipta.
- **Pemberian watermark**: Semua audio yang dihasilkan menyertakan
  [watermark audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=id) untuk
  identifikasi. Watermark ini tidak dapat didengar oleh telinga manusia dan tidak memengaruhi pengalaman mendengarkan.
- **Pengeditan berkelanjutan**: Pembuatan musik adalah proses satu putaran.
  Pengeditan atau penyempurnaan klip yang dihasilkan secara berulang melalui beberapa perintah tidak didukung dalam Lyria 3.5 versi saat ini.
- **Durasi**: Model Klip selalu menghasilkan klip berdurasi 30 detik. Model Pro membuat lagu berdurasi beberapa menit; durasi yang tepat dapat dipengaruhi melalui perintah Anda.
- **Determinisme**: Hasil dapat bervariasi antar-panggilan, bahkan dengan perintah yang sama.

## Langkah berikutnya

- Lihat [harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id) untuk model Lyria 3.5.
- Coba [pembuatan musik streaming real-time](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=id) dengan Lyria RealTime.
- Buat percakapan multi-pembicara dengan
  [model TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id).
- Temukan cara membuat [gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) atau
  [video](https://ai.google.dev/gemini-api/docs/video?hl=id).
- Cari tahu cara Gemini dapat [memahami file audio](https://ai.google.dev/gemini-api/docs/audio?hl=id).
- Lakukan percakapan real-time dengan Gemini menggunakan
  [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-01 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-01 UTC."],[],[]]
