---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=fr
fetched_at: 2026-06-08T05:34:18.746234+00:00
title: "G\u00e9n\u00e9rer de la musique avec Lyria\u00a03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Générer de la musique avec Lyria 3

Lyria 3 est la famille de modèles de génération de musique de Google, disponible via l'API Gemini. Avec Lyria 3, vous pouvez générer de l'audio stéréo de haute qualité à 44, 1 kHz à partir de requêtes textuelles ou d'images. Ces modèles offrent une cohérence structurelle, y compris les voix, les paroles synchronisées et les arrangements instrumentaux complets.

La famille Lyria 3 comprend deux modèles :

| Modèle | ID du modèle | Application idéale | Durée | Sortie |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clips courts, boucles, extraits | 30 secondes | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Chansons complètes avec des couplets, des refrains et des ponts | Quelques minutes (contrôlables via la requête) | MP3 |

Les deux modèles peuvent être utilisés avec la méthode `generateContent` standard et la nouvelle [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr), qui accepte les entrées multimodales (texte et images) et produit de l'audio **stéréo haute fidélité à 44,1 kHz**.

## Générer un extrait musical

Le modèle Lyria 3 Clip génère toujours un extrait de **30 secondes**. Pour générer un clip, appelez la méthode `generateContent` avec une invite textuelle. La réponse inclut toujours les paroles et la structure du morceau générées, ainsi que l'audio.

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

## Générer une chanson complète

Utilisez le modèle `lyria-3-pro-preview` pour générer des titres complets de quelques minutes. Le modèle Pro comprend la structure musicale et peut créer des compositions avec des couplets, des refrains et des ponts distincts. Vous pouvez influencer la durée en la spécifiant dans votre requête (par exemple, "crée une chanson de deux minutes") ou en utilisant des [codes temporels](#timing) pour définir la structure.

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

## Sélectionner le format de sortie

Par défaut, les modèles Lyria 3 génèrent de l'audio au format **MP3**. Pour Lyria 3 Pro, vous pouvez également demander le résultat au format **WAV** en définissant `response_format` dans `generationConfig`.

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

## Analyser la réponse

La réponse de Lyria 3 comporte plusieurs parties. Les parties textuelles contiennent les paroles générées ou une description JSON de la structure du morceau. Les parties avec `inline_data` contiennent les octets audio.

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

## Générer de la musique à partir d'images

Lyria 3 accepte les entrées multimodales. Vous pouvez fournir jusqu'à **10 images** en plus de votre requête textuelle. Le modèle composera de la musique inspirée du contenu visuel.

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

## Fournir des paroles personnalisées

Vous pouvez écrire vos propres paroles et les inclure dans la requête. Utilisez des balises de section comme `[Verse]`, `[Chorus]` et `[Bridge]` pour aider le modèle à comprendre la structure du morceau :

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

## Contrôler le timing et la structure

Vous pouvez spécifier exactement ce qui se passe à des moments précis de la chanson à l'aide de codes temporels. Cela permet de contrôler le moment où les instruments entrent en jeu, où les paroles sont diffusées et comment le morceau progresse :

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

## Générer des pistes instrumentales

Pour la musique de fond, les bandes originales de jeux ou tout cas d'utilisation où les voix ne sont pas nécessaires, vous pouvez demander au modèle de produire des pistes instrumentales uniquement :

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

## Générer de la musique dans différentes langues

Lyria 3 génère des paroles dans la langue de votre requête. Pour générer une chanson avec des paroles en français, rédigez votre requête en français. Le modèle adapte son style vocal et sa prononciation à la langue.

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

## Intelligence du modèle

Lyria 3 analyse le processus de votre requête, où le modèle raisonne à travers la structure musicale (intro, couplet, refrain, pont, etc.) en fonction de votre requête.
Cela se produit avant la génération de l'audio et garantit la cohérence structurelle et la musicalité.

## API Interactions

Vous pouvez utiliser les modèles Lyria 3 avec l'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=fr), une interface unifiée pour interagir avec les modèles et les agents Gemini. Il simplifie la gestion de l'état et des tâches de longue durée pour les cas d'utilisation multimodaux complexes.

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

## Guide sur les requêtes

Votre requête peut être aussi simple que "une chanson folk sur des chats mignons qui évitent les flaques d'eau, avec des voix féminines et le bruit de la pluie", ou plus détaillée et structurée, comme :

> Un titre synth-pop des années 1980 avec un rythme entraînant, des synthétiseurs scintillants et un refrain accrocheur et entraînant. Le morceau doit avoir une ambiance rétro-futuriste, rappelant les tubes pop classiques des années 80, avec une production moderne et soignée. Le tempo doit être entraînant et dansant, autour de 120 BPM, avec une structure couplet-refrain claire et un refrain instrumental mémorable. Les paroles parlent du sentiment de se préparer pour une fête.

Les requêtes simples et complexes peuvent générer de bons résultats. Nous vous recommandons de tester ces conseils pour trouver ce qui vous convient le mieux.

### Genre

Commencez votre requête par le genre de musique que vous souhaitez, comme hip-hop, rock ou rap. Vous pouvez spécifier une combinaison de genres :

- Un mélange de métal et de rap
- Un mélange de death metal et d'opéra
- Morceau classique avec des éléments de drone électronique
- Musique électronique moderne pour danser (EDM) mélangée à de l'Europop

Vous pouvez également inclure une époque :

- Hip-hop du début des années 90
- Pop yé-yé française des années 60
- Expérimentations électroniques des années 80
- Pop mainstream des années 2000

Si vous demandez des genres ou des variantes régionales spécifiques, comme "techno berlinoise" ou "hyphy de la baie de San Francisco", le modèle tentera de capturer cette essence, mais il ne réussira pas toujours.

### Instruments

Par défaut, Lyria 3 crée des chansons avec les instruments et les outils que vous attendez pour le genre. Vous n'avez pas besoin d'être prescriptif.

Toutefois, un morceau de danse n'inclura pas de saxophone, sauf si vous le demandez. Pour obtenir un solo de saxophone, vous devez le demander :

> Un titre de danse avec un rythme entraînant, des synthétiseurs scintillants et un refrain accrocheur et entraînant. Un solo de saxophone doit être joué pendant le pont.

Votre requête peut inclure des instruments spécifiques, leur sonorité et la façon dont ils interagissent les uns avec les autres. Vous pouvez utiliser cette combinaison pour créer certaines ambiances ou textures :

- Une ligne de basse sale et déformée qui se bat contre des charlestons clairs et nets
- Pads de synthétiseur analogiques chaleureux et gonflés sous une guitare acoustique sèche et intime
- Un mur de son créé par plusieurs couches de guitares saturées, avec des voix lointaines et enfouies

### Structure d'un titre

Vous pouvez décrire la progression d'un titre dans votre requête. Utilisez des flèches ou une liste pour définir le flux :

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Commence par une introduction au piano calme, monte en puissance pour un couplet fort, retombe dans le silence, puis explose dans le refrain.

Vous pouvez également spécifier comment les niveaux d'énergie changent entre ces sections :

- Créez de la tension dans le pré-refrain, puis passez au silence avant un refrain massif et explosif.
- Crescendo progressif tout au long du morceau, ajoutant un instrument à la fois jusqu'à un mur de son chaotique
- Arrêt soudain après le pont, suivi d'un refrain a cappella

Vous pouvez également indiquer l'heure exacte à laquelle vous souhaitez qu'une action se produise :

- Build to a drop at 12s
- Quelqu'un dit "quoi" toutes les deux secondes
- Le refrain commence à 22 s

### Paroles

Les voix et les paroles sont générées par défaut. Vous pouvez fournir vos propres paroles, demander à ce qu'il n'y en ait pas (ou qu'il s'agisse d'un instrumental) ou orienter la génération de paroles dans la direction de votre choix.

Vos paroles seront dans la langue dans laquelle vous rédigez votre requête. Vous pouvez également demander à ce que les paroles soient dans une autre langue, par exemple "Écris les paroles en français".

#### Utiliser vos propres paroles

Pour fournir vos propres paroles au modèle, incluez-les dans la requête avec le préfixe "Paroles :" :

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

Vous pouvez ajouter des titres de section comme `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` et `[Outro]` au début de certaines parties du titre.

Si vous souhaitez qu'un mot ou une ligne soient répétés, comme un écho ou par des choristes, vous pouvez l'inclure entre parenthèses : "Let's go (go)".

#### Demander au modèle d'écrire des paroles

Si vous souhaitez que Lyria 3 crée des paroles pour vous, il est préférable d'inclure dans votre requête des détails sur le thème des paroles. Sinon, le modèle devra déduire un sujet à partir de votre requête musicale, et il se peut que le résultat ne soit pas celui que vous souhaitez.

> Les paroles parlent d'un amour perdu et de la douleur d'un cœur brisé. La chanteuse se remémore une relation passée et les souvenirs qui lui reviennent en mémoire.

Si vous souhaitez un refrain répété, il est utile de le préciser dans votre requête :

> Les paroles parlent d'un amour perdu et de la douleur d'un cœur brisé. La chanteuse se remémore une relation passée et les souvenirs qui lui reviennent en mémoire. Un refrain puissant se concentre sur le fait de surmonter la douleur et de passer à autre chose.

Lyria 3 orientera automatiquement la structure des paroles vers le type de musique que vous demandez, mais vous pouvez également le préciser dans votre requête. Exemple :

> Un titre de musique électronique qui répète la même phrase énergique encore et encore.

Vous pouvez également demander des effets vocaux qui ne sont pas strictement des paroles, par exemple :

- Un sample répété d'un film dit "Je n'arrive pas à y croire !" tout au long du titre.
- Un morceau techno très énergique, juste avant le drop, le son s'arrête complètement et une petite voix dit "Je ne sais pas ce que je fais ici", puis la musique reprend.
- Le morceau s'ouvre sur une conversation sur les films des années 90, qui seraient meilleurs que ceux d'aujourd'hui. Le titre se transforme ensuite en chanson pop.

### Chant

Vous pouvez indiquer comment vous souhaitez que les paroles soient présentées. Pour obtenir les meilleurs résultats, spécifiez un profil de chanteur détaillé, en indiquant le genre, le timbre et la tessiture.

- **Soprano féminine** : timbre clair et cristallin, avec une qualité agile et aérienne. Capable d'atteindre des notes aiguës sifflantes avec une texture aérienne et haletante.
- **Alto féminin** : registre grave riche, chaleureux et rauque. Timbre enfumé avec une touche de fry vocal, soul et résonnant.
- **Ténor masculin** : voix brillante, perçante et énergique. Timbre juvénile avec une légère nasalité, qui se démarque dans le mix avec une grande puissance de voix.
- **Baryton masculin** : voix profonde, chocolatée et veloutée. Voix de poitrine résonnante avec un ton doux et mélodieux.
- **Rockeur usé (homme)** : voix rauque et texturée avec un timbre graveleux, qui rappelle le grunge des années 90. Registre supérieur tendu pour l'intensité émotionnelle.

### Autres paramètres de requête

Vous pouvez également inclure les paramètres suivants pour affiner davantage votre requête :

- **Tonalité/Gamme** : spécifiez une tonalité musicale (par exemple, "en sol majeur", "en ré mineur").
- **Ambiance** : utilisez des adjectifs descriptifs (par exemple, "nostalgique", "agressif", "éthéré", "rêveur").
- **Durée** : le modèle Clip produit toujours des extraits de 30 secondes. Pour le modèle Pro, spécifiez la durée souhaitée dans votre requête (par exemple, "crée une chanson de deux minutes") ou utilisez des codes temporels pour contrôler la durée.

### Exemples de prompts

Voici quelques exemples de requêtes efficaces :

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Bonnes pratiques

- **Commencez par itérer avec Clip.** Utilisez le modèle `lyria-3-clip-preview` plus rapide pour tester des requêtes avant de vous engager dans une génération complète avec `lyria-3-pro-preview`.
- **Soyez précis.** Les requêtes vagues produisent des résultats génériques. Pour obtenir les meilleurs résultats, mentionnez les instruments, le tempo, la tonalité, l'humeur et la structure.
- **Utilisez des tags de section.** Les balises `[Verse]`, `[Chorus]` et `[Bridge]` fournissent au modèle une structure claire à suivre.
- **Séparez les paroles des instructions.** Lorsque vous fournissez des paroles personnalisées, séparez-les clairement de vos instructions de direction musicale.

## Limites

- **Sécurité** : toutes les requêtes sont vérifiées par des filtres de sécurité. Les requêtes qui déclenchent les filtres seront bloquées. Cela inclut les requêtes demandant des voix d'artistes spécifiques ou la génération de paroles protégées par des droits d'auteur.
- **Filigranes** : tous les contenus audio générés incluent un [filigrane audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=fr) pour l'identification. Ce filigrane est imperceptible à l'oreille humaine et n'affecte pas l'expérience d'écoute.
- **Édition multitours** : la génération de musique est un processus monotour.
  L'édition itérative ou l'affinage d'un extrait généré à l'aide de plusieurs prompts ne sont pas pris en charge dans la version actuelle de Lyria 3.
- **Durée** : le modèle Clip génère toujours des extraits de 30 secondes. Le modèle Pro génère des titres qui durent quelques minutes. La durée exacte peut être influencée par votre requête.
- **Déterminisme** : les résultats peuvent varier d'un appel à l'autre, même avec le même prompt.

## Étape suivante

- Consultez les [tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr) des modèles Lyria 3.
- Essayez la [génération de musique en streaming et en temps réel](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=fr) avec Lyria RealTime.
- Générez des conversations à plusieurs locuteurs avec les [modèles TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).
- Découvrez comment générer des [images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) ou des [vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Découvrez comment Gemini peut [comprendre les fichiers audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr),
- Discutez en temps réel avec Gemini à l'aide de l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/01 (UTC)."],[],[]]
