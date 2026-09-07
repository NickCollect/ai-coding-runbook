---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=it
fetched_at: 2026-09-07T05:37:48.091666+00:00
title: "Generare musica con Lyria 3.5 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generare musica con Lyria 3.5

Lyria 3.5 è la famiglia di modelli di generazione di musica di Google, disponibile
tramite l'API Gemini. Con Lyria 3.5, puoi generare audio stereo di alta qualità a 44, 1 kHz
da prompt di testo o da immagini. Questi modelli offrono coerenza strutturale, tra cui voci, testi sincronizzati e arrangiamenti strumentali completi.

La famiglia Lyria include i modelli:

| Modello | ID modello | Ideale per | Durata | Output |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clip corti, loop, anteprime | 30 secondi | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Brani completi con strofe, ritornelli e ponti | Un paio di minuti (controllabile tramite prompt) | MP3 |

Entrambi i modelli possono essere utilizzati con il metodo standard `generateContent` e con la nuova [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it), supportano input multimodali (testo e immagini) e producono audio stereo ad alta fedeltà a **44,1 kHz**.

## Generare un clip musicale

Il modello Lyria 3 Clip genera sempre un clip di **30 secondi**. Per generare un clip, chiama il metodo `generateContent` con un prompt testuale. La risposta include sempre
il testo e la struttura del brano generati insieme all'audio.

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

## Generare un brano completo

Utilizza il modello `lyria-3.5` per generare brani di lunga durata che durano un paio di minuti. Il modello Pro comprende la struttura musicale e può creare
composizioni con strofe, ritornelli e ponti distinti. Puoi influenzare la
durata specificandola nel prompt (ad es. "crea una canzone di 2 minuti") o utilizzando
[timestamp](#timing) per definire la struttura.

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

## Seleziona il formato di output

Per impostazione predefinita, i modelli Lyria 3.5 generano audio in formato **MP3**. Per
Lyria 3.5, puoi anche richiedere l'output in formato **WAV** impostando
`response_format` in `generationConfig`.

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

## Analizza la risposta

La risposta di Lyria 3.5 contiene più parti. Le parti di testo contengono
il testo generato o una descrizione in formato JSON della struttura del brano. Le parti con
`inline_data` contengono i byte audio.

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

## Generare musica dalle immagini

Lyria 3.5 supporta input multimodali: puoi fornire fino a **10 immagini** insieme al prompt testuale e il modello comporrà musica ispirata ai contenuti visivi.

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

## Fornire testi personalizzati

Puoi scrivere i tuoi testi e includerli nel prompt. Utilizza i tag di sezione
come `[Verse]`, `[Chorus]` e `[Bridge]` per aiutare il modello a comprendere la
struttura del brano:

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

## Controllare la tempistica e la struttura

Puoi specificare esattamente cosa succede in momenti specifici del brano utilizzando
i timestamp. Questo è utile per controllare quando entrano gli strumenti, quando vengono fornite le parole e come procede la canzone:

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

## Generare tracce strumentali

Per la musica di sottofondo, le colonne sonore dei giochi o qualsiasi caso d'uso in cui non sono richieste parti vocali, puoi chiedere al modello di produrre tracce solo strumentali:

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

## Generare musica in lingue diverse

Lyria 3.5 genera testi nella lingua del prompt. Per generare una canzone
con un testo in francese, scrivi il prompt in francese. Il modello adatta lo stile
vocale e la pronuncia in base alla lingua.

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

## Intelligenza del modello

Lyria 3.5 analizza il processo di prompt in cui il modello ragiona sulla struttura musicale (intro, strofa, ritornello, bridge e così via) in base al prompt.
Ciò avviene prima della generazione dell'audio e garantisce coerenza strutturale e
musicalità.

## API Interactions

Puoi utilizzare i modelli Lyria 3.5 con l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it),
un'interfaccia unificata per interagire con i modelli e gli agenti Gemini. Semplifica
la gestione dello stato e le attività di lunga durata per casi d'uso multimodali complessi.

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

## Guida ai prompt

Il prompt può essere semplice come "una canzone folk su gatti carini che evitano le pozzanghere,
voce femminile e rumore della pioggia" oppure qualcosa di dettagliato e strutturato
come:

> Un brano synth-pop in stile anni '80 con un ritmo incalzante, sintetizzatori brillanti
> e un ritornello orecchiabile e trascinante. La canzone deve avere un'atmosfera retro-futuristica,
> che ricorda i classici successi pop degli anni '80, con un tocco di modernità. Il
> tempo deve essere allegro e ballabile, intorno ai 120 BPM, con una chiara
> struttura strofa-ritornello e un hook strumentale memorabile. Il testo parla
> della sensazione di prepararsi per una festa.

Prompt semplici e complessi possono fornire buoni risultati. Ti consigliamo di
sperimentare con questi suggerimenti per trovare la soluzione più adatta a te.

### Genere

Inizia il prompt con il genere musicale che preferisci, ad esempio hip hop, rock e
rap. Puoi specificare un mix di generi:

- Una fusione di metal e rap
- Una combinazione di death metal e opera
- Un brano classico con elementi di droni elettronici
- Musica dance elettronica (EDM) moderna mixata con Europop

Puoi anche incorporare un'era:

- Hip hop dei primi anni '90
- Pop ye-ye francese degli anni '60
- Sperimentazione elettronica anni '80
- Pop mainstream degli anni 2000

Se richiedi generi personalizzati o varianti regionali, come "techno berlinese" o
"hyphy della Bay Area", il modello tenterà di catturare l'essenza, ma potrebbe
non riuscirci sempre.

### Strumenti

Per impostazione predefinita, Lyria 3.5 crea brani con gli strumenti che ti aspetteresti per il genere. Non è necessario essere prescrittivi.

Tuttavia, una traccia dance non includerà un sassofono a meno che tu non lo chieda. Quindi, se vuoi un assolo di sassofono, devi richiederlo:

> Una traccia dance con un ritmo incalzante, sintetizzatori scintillanti e un ritornello orecchiabile
> che fa venire voglia di cantare. Durante il bridge deve entrare un assolo di sassofono.

Il prompt può includere strumenti specifici, il loro suono e il modo in cui
interagiscono tra loro. Puoi utilizzare questa combinazione per creare determinati stati d'animo
o texture:

- Una linea di basso sporca e distorta che contrasta con hi-hat puliti e nitidi
- Pad di sintetizzatore analogico caldi che si gonfiano sotto una chitarra acustica secca e intima
- Un muro di suono creato da più livelli di chitarre fuzz, con voci lontane e
  sepolte

### Struttura del brano

Puoi descrivere la progressione di un brano nel prompt. Utilizza le frecce o un elenco
per definire il flusso:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Inizia con un intro di pianoforte tranquillo, passa a una strofa potente, poi a un
  silenzio e infine esplodi nel ritornello.

Puoi anche specificare come cambiano i livelli di energia tra queste sezioni:

- Crea tensione nel pre-chorus, poi passa al silenzio prima di un chorus massiccio ed
  esplosivo
- Crescendo graduale durante il brano, con l'aggiunta di uno strumento alla volta
  fino a un muro di suono caotico
- Interruzione improvvisa dopo il ponte, seguita da un coro a cappella

Puoi anche richiedere l'ora esatta in cui vuoi che accada qualcosa:

- Crea un drop a 12 secondi
- Qualcuno dice "cosa" ogni 2 secondi
- Il ritornello inizia a 22 secondi

### Testo

La voce e i testi vengono generati per impostazione predefinita. Puoi fornire i tuoi testi,
richiedere di non includere testi (o una versione strumentale) o indirizzare la generazione dei testi
nella direzione che preferisci.

I testi saranno nella lingua in cui scrivi il prompt. Puoi anche chiedere
che il testo sia in un'altra lingua, ad esempio "Scrivi il testo in francese".

#### Utilizzo dei propri testi

Per fornire al modello i tuoi testi, includili nel prompt con il prefisso "Lyrics:":

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

Puoi aggiungere un prefisso alle parti del brano con titoli di sezione come `[Intro]`,
`[Verse 1]`, `[Pre-chorus]`, `[Chorus]` e `[Outro]`.

Se vuoi che una parola o una riga venga ripetuta, come un eco o dai coristi,
puoi includerla tra parentesi: "Let's go (go)".

#### Chiedere al modello di scrivere i testi

Se vuoi che Lyria 3.5 crei i testi per te, è meglio includere dettagli
su cosa tratteranno i testi nel prompt. In caso contrario, il modello deve
dedurre un soggetto dal prompt musicale e potrebbe non essere quello che vuoi.

> Il testo parla di un amore perduto e del dolore di una delusione amorosa. Il cantante sta
> ricordando una relazione passata e i ricordi che gli tornano
> in mente.

Se vuoi un ritornello ripetuto, è utile chiederlo nel prompt:

> Il testo parla di un amore perduto e del dolore di una delusione amorosa. Il cantante sta
> ricordando una relazione passata e i ricordi che gli tornano
> in mente. Un ritornello potente si concentra sul superamento del dolore e sul voltare pagina.

Lyria 3.5 indirizzerà automaticamente la struttura del testo verso il tipo di musica che stai richiedendo, ma puoi riaffermarlo anche nel prompt. Ad esempio:

> Un brano di musica elettronica che ripete la stessa frase energica più e più volte.

Puoi anche richiedere effetti vocali che non sono strettamente testi, ad esempio:

- Un campione ripetuto di un film dice "Non ci posso credere!" per tutta la durata della canzone
- Un brano techno ad alta energia, proprio prima del drop la musica si interrompe e una
  vocina dice "Non so cosa ci faccio qui", poi la musica riprende.
- La traccia si apre con una conversazione sui film degli anni '90 che erano
  migliori di quelli di oggi. Poi la traccia si trasforma in un brano pop.

### Voce

Puoi specificare come vuoi che vengano forniti i testi. Per ottenere i risultati migliori, specifica un profilo dettagliato del cantante che includa genere, timbro ed estensione vocale.

- **Soprano femminile**: timbro chiaro e cristallino con una qualità agile e impetuosa. Capace di raggiungere note alte e fischiettanti con una consistenza ariosa e soffice.
- **Contralto femminile**: gamma bassa ricca, calda e rauca. Timbro fumoso con un
  tocco di vocal fry, pieno di anima e risonante.
- **Tenore maschile**: brillante, penetrante ed energico. Timbro giovanile con una
  leggera sfumatura nasale, che si distingue nel mix con una potenza vocale elevata.
- **Baritono maschile**: profondo, cioccolatoso e vellutato. Voce profonda
  con un tono dolce e melodioso.
- **Weathered Rocker (uomo)**: voce roca e ruvida con un timbro granuloso,
  che ricorda il grunge degli anni '90. Gamma superiore tesa per l'intensità emotiva.

### Altri parametri del prompt

Puoi anche includere questi parametri per perfezionare ulteriormente il prompt:

- **Tonalità/Scala**: specifica una tonalità musicale (ad es. "in sol maggiore", "re minore").
- **Stato d'animo e atmosfera**: utilizza aggettivi descrittivi (ad es. "nostalgico",
  "aggressivo", "etereo", "onirico").
- **Durata**: il modello Clip produce sempre clip di 30 secondi. Per il modello Pro, specifica la durata desiderata nel prompt (ad es. "crea una canzone di 2 minuti") o utilizza i timestamp per controllare la durata.

### Prompt di esempio

Ecco alcuni esempi di prompt efficaci:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Best practice

- **Esegui l'iterazione con Clip.** Utilizza il modello `lyria-3-clip-preview` più veloce per
  sperimentare con i prompt prima di eseguire una generazione completa con
  `lyria-3.5`.
- **Usa un testo specifico.** I prompt vaghi producono risultati generici. Menziona strumenti,
  BPM, tonalità, stato d'animo e struttura per ottenere il miglior output.
- **Utilizza i tag di sezione.** I tag `[Verse]`, `[Chorus]` e `[Bridge]` forniscono al modello
  una struttura chiara da seguire.
- **Separa i testi dalle istruzioni.** Quando fornisci testi personalizzati, separali chiaramente
  dalle istruzioni per la direzione musicale.

## Limitazioni

- **Sicurezza**: tutti i prompt vengono controllati dai filtri di sicurezza. I prompt che attivano
  i filtri verranno bloccati. Ciò include i prompt che richiedono voci di artisti specifici o la generazione di testi protetti da copyright.
- **Filigrana**: tutto l'audio generato include una
  [filigrana audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=it) per
  l'identificazione. Questa filigrana è impercettibile all'orecchio umano e
  non influisce sull'esperienza di ascolto.
- **Modifica multi-turno**: la generazione di musica è un processo in un solo passaggio.
  L'editing iterativo o il perfezionamento di un clip generato tramite più prompt non è
  supportato nella versione attuale di Lyria 3.5.
- **Durata**: il modello Clip genera sempre clip di 30 secondi. Il modello Pro
  genera brani che durano un paio di minuti; la durata esatta può essere
  influenzata dal prompt.
- **Determinismo**: i risultati possono variare tra le chiamate, anche con lo stesso prompt.

## Passaggi successivi

- Consulta i [prezzi](https://ai.google.dev/gemini-api/docs/generate-content/pricing?hl=it) dei modelli Lyria 3.5.
- Prova la [generazione di musica in streaming in tempo reale](https://ai.google.dev/gemini-api/docs/generate-content/realtime-music-generation?hl=it) con
  Lyria RealTime,
- Genera conversazioni con più interlocutori con i
  [modelli TTS](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it),
- Scopri come generare [immagini](https://ai.google.dev/gemini-api/docs/generate-content/image-generation?hl=it) o [video](https://ai.google.dev/gemini-api/docs/generate-content/video?hl=it),
- Scopri come Gemini può [comprendere i file audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=it),
- Avvia una conversazione in tempo reale con Gemini utilizzando l'[API Live](https://ai.google.dev/gemini-api/docs/generate-content/live?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-04 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-04 UTC."],[],[]]
