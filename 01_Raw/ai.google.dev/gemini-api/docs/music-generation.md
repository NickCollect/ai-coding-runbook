---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=de
fetched_at: 2026-06-01T06:04:46.248701+00:00
title: "Musik mit Lyria\u00a03 generieren \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de) ist jetzt in der Vorabversion mit Funktionen wie gemeinsamer Planung, Visualisierung und MCP-Unterstützung verfügbar.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Musik mit Lyria 3 generieren

Lyria 3 ist die Familie von Musikgenerierungsmodellen von Google, die über die Gemini API verfügbar sind. Mit Lyria 3 können Sie aus Text-Prompts oder Bildern hochwertiges Stereo-Audio mit 44,1 kHz generieren. Diese Modelle liefern strukturelle Kohärenz, einschließlich Gesang, zeitgesteuerter Songtexte und vollständiger Instrumentalarrangements.

Die Lyria 3-Familie umfasst zwei Modelle:

| Modell | Modell-ID | Optimal für | Dauer | Ausgabe |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Kurze Clips, Loops, Vorschauen | 30 Sekunden | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Songs in voller Länge mit Strophen, Refrains und Bridges | Ein paar Minuten (über Prompt steuerbar) | MP3 |

Beide Modelle können mit der Standardmethode `generateContent` und der neuen [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=de) verwendet werden.Sie unterstützen multimodale Eingaben (Text und Bilder) und erzeugen **Stereo-Audio mit 44,1 kHz**.

## Musikclip erstellen

Mit dem Lyria 3-Clip-Modell wird immer ein **30-sekündiger Clip** generiert. Rufen Sie zum Generieren eines Clips die Methode `generateContent` mit einem Text-Prompt auf. Die Antwort enthält immer den generierten Text und die Songstruktur sowie das Audio.

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

### Ok

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

## Song in voller Länge generieren

Mit dem `lyria-3-pro-preview`-Modell können Sie Songs in voller Länge generieren, die einige Minuten dauern. Das Pro-Modell versteht musikalische Strukturen und kann Kompositionen mit unterschiedlichen Strophen, Refrains und Bridges erstellen. Sie können die Dauer beeinflussen, indem Sie sie in Ihrem Prompt angeben (z.B. „Erstelle einen 2‑minütigen Song“) oder indem Sie [Zeitstempel](#timing) verwenden, um die Struktur zu definieren.

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

### Ok

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

## Ausgabeformat auswählen

Standardmäßig generieren die Lyria 3-Modelle Audio im **MP3**-Format. Bei Lyria 3 Pro können Sie die Ausgabe auch im **WAV**-Format anfordern, indem Sie `response_format` in der `generationConfig` festlegen.

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

### Ok

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

## Antwort analysieren

Die Antwort von Lyria 3 besteht aus mehreren Teilen. Textteile enthalten den generierten Songtext oder eine JSON-Beschreibung der Songstruktur. Teile mit `inline_data` enthalten die Audio-Bytes.

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

### Ok

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

## Musik aus Bildern generieren

Lyria 3 unterstützt multimodale Eingaben. Sie können neben Ihrem Textprompt bis zu **10 Bilder** angeben. Das Modell komponiert dann Musik, die von den visuellen Inhalten inspiriert ist.

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

### Ok

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

## Benutzerdefinierte Songtexte eingeben

Sie können Ihren eigenen Songtext schreiben und in den Prompt einfügen. Verwenden Sie Abschnitts-Tags wie `[Verse]`, `[Chorus]` und `[Bridge]`, damit das Modell die Songstruktur besser versteht:

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

### Ok

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

## Zeitplanung und Struktur steuern

Mit Zeitstempeln kannst du genau angeben, was zu bestimmten Zeitpunkten im Song passieren soll. Das ist nützlich, um zu steuern, wann Instrumente einsetzen, wann Texte geliefert werden und wie das Lied voranschreitet:

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

### Ok

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

## Instrumental-Tracks generieren

Für Hintergrundmusik, Game-Soundtracks oder jeden Anwendungsfall, in dem kein Gesang erforderlich ist, können Sie das Modell auffordern, nur Instrumentalstücke zu erstellen:

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

### Ok

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

## Musik in verschiedenen Sprachen generieren

Lyria 3 generiert Songtexte in der Sprache Ihres Prompts. Wenn Sie einen Song mit französischen Texten generieren möchten, schreiben Sie Ihren Prompt auf Französisch. Das Modell passt seinen Gesangsstil und seine Aussprache an die Sprache an.

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

### Ok

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

## Modellintelligenz

Lyria 3 analysiert Ihren Prompt-Prozess, wobei das Modell die musikalische Struktur (Intro, Strophe, Refrain, Bridge usw.) auf Grundlage Ihres Prompts analysiert.
Dies geschieht, bevor das Audio generiert wird, und sorgt für strukturelle Kohärenz und Musikalität.

## Interactions API

Sie können Lyria 3-Modelle mit der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=de) verwenden. Diese API bietet eine einheitliche Schnittstelle für die Interaktion mit Gemini-Modellen und ‑Agents. Sie vereinfacht die Statusverwaltung und die Ausführung von zeitaufwendigen Aufgaben für komplexe multimodale Anwendungsfälle.

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

## Anleitung zu Prompts

Ihr Prompt kann so einfach sein wie „ein Folksong über süße Katzen, die Pfützen ausweichen, weiblicher Gesang und das Geräusch von Regen“ oder detailliert und strukturiert wie:

> Ein Synthie-Pop-Track im Stil der 1980er-Jahre mit einem treibenden Beat, flirrenden Synthesizern und einem eingängigen, hymnenhaften Refrain. Der Song soll retrofuturistisch klingen, an klassische Pop-Hits der 80er erinnern und modern produziert sein. Das Tempo sollte flott und tanzbar sein, etwa 120 BPM, mit einer klaren Strophe-Refrain-Struktur und einem eingängigen instrumentalen Hook. Im Lied geht es darum, sich für eine Party fertig zu machen.

Sowohl einfache als auch komplexe Prompts können gute Ergebnisse liefern. Wir empfehlen, diese Tipps auszuprobieren, um herauszufinden, was für Sie am besten funktioniert.

### Genre

Beginnen Sie Ihren Prompt mit dem gewünschten Musikgenre, z. B. Hip-Hop, Rock oder Rap. Sie können eine Mischung aus Genres angeben:

- Eine Mischung aus Metal und Rap
- Eine Kombination aus Death Metal und Oper
- Ein klassisches Stück mit elektronischen Drone-Elementen
- Moderne elektronische Tanzmusik (EDM) gemischt mit Europop

Sie können auch eine Epoche einbeziehen:

- Hip-Hop der frühen 90er
- Französischer Yé-Yé-Pop der 1960er
- Elektronische Experimente der 80er
- Mainstream-Pop der 2000er

Wenn Sie nach bestimmten Genres oder regionalen Varianten wie „Berliner Techno“ oder „Bay Area Hyphy“ fragen, versucht das Modell, diese Essenz zu erfassen, aber das gelingt nicht immer.

### Instrumente

Standardmäßig werden in Lyria 3 Songs mit den Instrumenten und Tools erstellt, die für das jeweilige Genre typisch sind. Sie müssen nicht vorschreibend sein.

Ein Dance-Track enthält jedoch kein Saxofon, es sei denn, Sie bitten darum. Wenn Sie also ein Saxofonsolo möchten, müssen Sie das angeben:

> Ein Dance-Track mit einem treibenden Beat, schimmernden Synthesizern und einem eingängigen, hymnenhaften Refrain. Während der Bridge sollte ein Saxofonsolo erklingen.

Ihr Prompt kann bestimmte Instrumente, deren Klang und die Interaktion der Instrumente untereinander enthalten. Mit dieser Kombination können Sie bestimmte Stimmungen oder Texturen erzeugen:

- Eine schmutzige, verzerrte Basslinie kämpft gegen saubere, knackige Hi-Hats.
- Warme, analoge Synthesizer-Pads, die unter einer trockenen, intimen Akustikgitarre anschwellen
- Eine Klangwand aus mehreren Schichten von verzerrten Gitarren mit vergrabenen, entfernten Gesang

### Songstruktur

Sie können den Verlauf eines Songs in Ihrem Prompt beschreiben. Verwenden Sie Pfeile oder eine Liste, um den Ablauf zu definieren:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Beginne mit einem leisen Klavier-Intro, steigere dich zu einem lauten Vers, falle in die Stille und explodiere dann im Refrain.

Sie können auch angeben, wie sich die Energieniveaus zwischen diesen Abschnitten ändern:

- Im Pre-Chorus Spannung aufbauen und dann vor einem massiven, explosiven Chorus in die Stille fallen
- Ein Crescendo, das sich im Laufe des Songs steigert, indem nach und nach ein Instrument hinzugefügt wird, bis eine chaotische Klangwand entsteht.
- Plötzlicher Stopp nach der Bridge, gefolgt von einem A-cappella-Refrain

Sie können auch die genaue Uhrzeit angeben, zu der etwas passieren soll:

- Bis zum Drop bei 12 Sekunden
- Jemand sagt alle 2 Sekunden „Was?“
- Der Refrain beginnt bei 22 Sekunden.

### Songtext

Gesang und Songtexte werden standardmäßig generiert. Sie können einen eigenen Songtext angeben, keinen Songtext (oder ein Instrumental) anfordern oder die Generierung des Songtexts in die gewünschte Richtung lenken.

Die Lyrics werden in der Sprache verfasst, in der Sie Ihren Prompt eingeben. Du kannst auch angeben, dass der Text in einer anderen Sprache verfasst werden soll, z. B. „Schreibe den Text auf Französisch“.

#### Eigene Songtexte verwenden

Wenn Sie dem Modell eigene Songtexte zur Verfügung stellen möchten, fügen Sie sie mit dem Präfix „Lyrics:“ in den Prompt ein:

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

Sie können Teile des Songs mit Abschnittstiteln wie `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` und `[Outro]` kennzeichnen.

Wenn ein Wort oder eine Zeile wiederholt werden soll, z. B. als Echo oder von Backgroundsängern, kannst du es in Klammern setzen: „Let’s go (go)“.

#### Modell zum Schreiben von Songtexten auffordern

Wenn Sie möchten, dass Lyria 3 Songtexte für Sie erstellt, sollten Sie in Ihrem Prompt Details dazu angeben, worum es in den Texten gehen soll. Andernfalls muss das Modell ein Thema aus Ihrem Musik-Prompt ableiten, was möglicherweise nicht Ihren Vorstellungen entspricht.

> Der Text handelt von verlorener Liebe und dem Schmerz des Herzschmerzes. Die Sängerin erinnert sich an eine vergangene Beziehung und die Erinnerungen, die zurückkommen.

Wenn Sie einen sich wiederholenden Refrain wünschen, sollten Sie das in Ihrem Prompt angeben:

> Der Text handelt von verlorener Liebe und dem Schmerz des Herzschmerzes. Die Sängerin erinnert sich an eine vergangene Beziehung und die Erinnerungen, die zurückkommen. Ein kraftvoller Refrain konzentriert sich darauf, den Schmerz zu überwinden und weiterzumachen.

Lyria 3 richtet die Struktur des Songtexts automatisch auf die Art von Musik aus, die du anforderst. Du kannst das aber auch in deinem Prompt noch einmal betonen. Beispiel:

> Ein EDM-Track, in dem immer wieder dieselbe energiegeladene Phrase wiederholt wird.

Sie können auch nach Gesangseffekten fragen, die nicht unbedingt Text sind, z. B.:

- Ein sich wiederholendes Sample aus einem Film sagt im gesamten Song „I can't believe this!“ (Ich kann es nicht fassen!).
- Ein energiegeladener Techno-Track. Kurz vor dem Drop stoppt die Musik und eine kleine Stimme sagt: „I don’t know what I’m doing here“ (Ich weiß nicht, was ich hier mache). Dann setzt die Musik wieder ein.
- Der Track beginnt mit einer Unterhaltung darüber, dass die Filme in den 90er-Jahren besser waren als heute. Dann geht der Titel in einen Popsong über.

### Gesang

Sie können angeben, wie der Songtext präsentiert werden soll. Die besten Ergebnisse erzielen Sie, wenn Sie ein detailliertes Sängerprofil mit Angaben zu Geschlecht, Klangfarbe und Tonumfang angeben.

- **Weiblicher Sopran**: Klarer, kristalliner Klang mit einer agilen, schwebenden Qualität. Sie kann pfeifende hohe Töne mit einer luftigen, gehauchten Textur erreichen.
- **Weiblicher Alt**: Kräftiger, warmer und heiserer tiefer Bereich. Rauchige Klangfarbe mit einem Hauch von Vocal Fry, gefühlvoll und resonierend.
- **Tenor**: Hell, durchdringend und energiegeladen. Jugendliches Timbre mit einer leichten nasalen Note, die sich mit hoher Belting-Power durch den Mix schneidet.
- **Männlicher Bariton**: Tief, schokoladig und samtweich. Resonante Bruststimme mit beruhigender, sanfter Vortragsweise.
- **Weathered Rocker (Male)**: Heiser und rau mit einem kiesigen Timbre, das an Grunge aus den 90er-Jahren erinnert. Angespannte obere Grenze für emotionale Intensität.

### Weitere Prompt-Parameter

Sie können auch die folgenden Parameter einfügen, um Ihren Prompt weiter zu verfeinern:

- **Tonart/Skala**: Geben Sie eine Tonart an, z.B. „in G-Dur“ oder „D-Moll“.
- **Stimmung und Atmosphäre**: Verwenden Sie beschreibende Adjektive (z.B. „nostalgisch“, „aggressiv“, „ätherisch“, „vertäumt“).
- **Dauer**: Das Clip-Modell erstellt immer 30-sekündige Clips. Geben Sie beim Pro-Modell die gewünschte Länge in Ihrem Prompt an (z.B. „Erstelle einen 2-minütigen Song“) oder verwenden Sie Zeitstempel, um die Dauer zu steuern.

### Beispiele für Prompts

Beispiele für effektive Prompts:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Best Practices

- **Zuerst mit Clip iterieren**: Mit dem schnelleren Modell `lyria-3-clip-preview` können Sie mit Prompts experimentieren, bevor Sie eine vollständige Generierung mit `lyria-3-pro-preview` starten.
- **Beschreiben Sie das Angebot möglichst genau.** Vage Prompts führen zu allgemeinen Ergebnissen. Geben Sie Instrumente, BPM, Tonart, Stimmung und Struktur an, um die besten Ergebnisse zu erzielen.
- **Abschnittstags verwenden**: Die Tags `[Verse]`, `[Chorus]` und `[Bridge]` geben dem Modell eine klare Struktur vor.
- **Trenne Songtexte von Anweisungen.** Wenn Sie benutzerdefinierte Liedtexte angeben, trennen Sie diese deutlich von Ihren Anweisungen zur musikalischen Ausrichtung.

## Beschränkungen

- **Sicherheit**: Alle Prompts werden von Sicherheitsfiltern geprüft. Prompts, die die Filter auslösen, werden blockiert. Dazu gehören Prompts, in denen bestimmte Künstlerstimmen oder die Generierung von urheberrechtlich geschützten Texten angefordert werden.
- **Wasserzeichen**: Alle generierten Audioinhalte enthalten ein [SynthID-Audio-Wasserzeichen](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=de) zur Identifizierung. Dieses Wasserzeichen ist für das menschliche Ohr nicht wahrnehmbar und hat keine Auswirkungen auf das Hörerlebnis.
- **Bearbeitung in mehreren Schritten**: Die Musikgenerierung ist ein Prozess, der in einem Schritt erfolgt.
  Das iterative Bearbeiten oder Verfeinern eines generierten Clips durch mehrere Prompts wird in der aktuellen Version von Lyria 3 nicht unterstützt.
- **Länge**: Das Clip-Modell generiert immer 30-sekündige Clips. Das Pro-Modell generiert Songs, die einige Minuten lang sind. Die genaue Dauer kann durch Ihren Prompt beeinflusst werden.
- **Determinismus**: Die Ergebnisse können zwischen den Aufrufen variieren, auch wenn derselbe Prompt verwendet wird.

## Nächste Schritte

- [Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de) für Lyria 3-Modelle
- Probieren Sie [Musikgenerierung in Echtzeit](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=de) mit Lyria RealTime aus.
- Unterhaltungen mit mehreren Sprechern mit den [TTS-Modellen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) generieren
- [Bilder](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) oder [Videos](https://ai.google.dev/gemini-api/docs/video?hl=de) generieren
- [Informationen dazu, wie Gemini Audiodateien verstehen kann](https://ai.google.dev/gemini-api/docs/audio?hl=de)
- Mit der [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de) können Sie sich in Echtzeit mit Gemini unterhalten.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-05-28 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-05-28 (UTC)."],[],[]]
