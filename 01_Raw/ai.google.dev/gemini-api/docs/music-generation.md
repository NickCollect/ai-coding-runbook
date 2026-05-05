---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=pt-BR
fetched_at: 2026-05-05T20:46:23.005713+00:00
title: "Gerar m\u00fasicas com o Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Gerar músicas com o Lyria 3

O Lyria 3 é a família de modelos de geração de música do Google, disponível
pela API Gemini. Com o Lyria 3, é possível gerar áudio estéreo de alta qualidade e 44, 1 kHz com comandos de texto ou imagens. Esses modelos oferecem coerência estrutural, incluindo vocais, letras sincronizadas e arranjos instrumentais completos.

A família Lyria 3 inclui dois modelos:

| Modelo | ID do modelo | Ideal para | Duração | Saída |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Clipes curtos, loops, prévias | 30 segundos | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Músicas completas com versos, refrões e pontes | Alguns minutos (controláveis por comando) | MP3 |

Os dois modelos podem ser usados com o método `generateContent` padrão e a nova [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br), que aceita entradas multimodais (texto e imagens) e produz áudio **estéreo de alta fidelidade de 44,1 kHz**.

## Gerar um videoclipe

O modelo Lyria 3 Clip sempre gera um clipe de **30 segundos**. Para gerar um
clipe, chame o método `generateContent` com um comando de texto. A resposta sempre inclui a letra e a estrutura da música geradas junto com o áudio.

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

## Gerar uma música completa

Use o modelo `lyria-3-pro-preview` para gerar músicas completas que duram alguns minutos. O modelo Pro entende a estrutura musical e pode criar
composições com versos, refrões e pontes distintos. É possível influenciar a duração especificando-a no comando (por exemplo, "crie uma música de 2 minutos") ou usando [carimbos de data/hora](#timing) para definir a estrutura.

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

## Selecionar formato de saída

Por padrão, os modelos do Lyria 3 geram áudio no formato **MP3**. Para o Lyria 3 Pro, também é possível solicitar a saída no formato **WAV** definindo `response_mime_type` em `generationConfig`.

### Python

```
response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents="An atmospheric ambient track.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO", "TEXT"],
        response_mime_type="audio/wav",
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
    responseMimeType: "audio/wav",
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
    .responseMimeType("audio/wav")
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
      "responseMimeType": "audio/wav"
    }
  }'
```

## Analise a resposta

A resposta da Lyria 3 contém várias partes. As partes de texto contêm as letras geradas ou uma descrição JSON da estrutura da música. As partes com
`inline_data` contêm os bytes de áudio.

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

## Gerar música com base em imagens

O Lyria 3 aceita entradas multimodais. Você pode fornecer até **10 imagens** junto com seu comando de texto, e o modelo vai compor músicas inspiradas no conteúdo visual.

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

## Fornecer letras personalizadas

Você pode escrever suas próprias letras e incluí-las no comando. Use tags de seção
como `[Verse]`, `[Chorus]` e `[Bridge]` para ajudar o modelo a entender a
estrutura da música:

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

## Controlar o tempo e a estrutura

É possível especificar exatamente o que acontece em momentos específicos da música usando
carimbos de data/hora. Isso é útil para controlar quando os instrumentos entram, quando as letras
são entregues e como a música progride:

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

## Gerar músicas instrumentais

Para música de fundo, trilhas sonoras de jogos ou qualquer caso de uso em que não sejam necessários vocais, peça ao modelo para produzir músicas apenas instrumentais:

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

## Gerar músicas em diferentes idiomas

O Lyria 3 gera letras no idioma do seu comando. Para gerar uma música com letras em francês, escreva o comando nesse idioma. O modelo adapta o estilo vocal e a pronúncia para corresponder ao idioma.

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

## Inteligência do modelo

O Lyria 3 analisa seu processo de comando em que o modelo raciocina sobre a estrutura musical (introdução, verso, refrão, ponte etc.) com base no seu comando.
Isso acontece antes da geração do áudio e garante coerência estrutural e musicalidade.

## API Interactions

É possível usar os modelos Lyria 3 com a [API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pt-br), uma interface unificada para interagir com modelos e agentes do Gemini. Ela simplifica o gerenciamento de estado e tarefas de longa duração para casos de uso multimodais complexos.

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

## Guia de comandos

Seu comando pode ser simples, como "uma música folk sobre gatos fofos evitando poças, vocais femininos e o barulho da chuva", ou algo detalhado e estruturado, como:

> Uma música synth-pop no estilo dos anos 1980 com uma batida marcante, sintetizadores reverberantes e um refrão cativante e hino. A música precisa ter uma vibe retrofuturista, lembrando os clássicos do pop dos anos 80, com uma produção moderna. O
> tempo precisa ser animado e dançante, em torno de 120 BPM, com uma estrutura
> clara de verso-refrão e um refrão instrumental memorável. A letra fala sobre
> a sensação de se arrumar para uma festa.

Comandos simples e complexos podem gerar boas respostas. Recomendamos que você teste essas dicas para descobrir o que funciona melhor para você.

### Gênero

Comece o comando com o gênero musical que você quer, como hip hop, rock e rap. É possível especificar uma mistura de gêneros:

- Uma fusão de metal e rap
- Uma combinação de death metal e ópera
- Uma peça clássica com elementos de drone eletrônico
- Música eletrônica moderna (EDM) misturada com Europop

Você também pode incorporar uma era:

- Hip-hop do início dos anos 90
- Pop iê-iê francês dos anos 60
- Experimentação eletrônica dos anos 80
- Pop mainstream dos anos 2000

Se você pedir gêneros personalizados ou variantes regionais, como "techno de Berlim" ou "hyphy da área da baía", o modelo vai tentar capturar essa essência, mas nem sempre vai acertar.

### Instrumentos

Por padrão, o Lyria 3 cria músicas com os instrumentos e ferramentas que você esperaria para o gênero. Não é necessário ser prescritivo.

No entanto, uma música de dança não vai incluir um saxofone a menos que você peça. Se você quiser um solo de saxofone, faça o seguinte comando:

> Uma música de dança com uma batida envolvente, sintetizadores brilhantes e um refrão cativante e
> empolgante. Um solo de saxofone deve entrar durante a ponte.

Seu comando pode incluir instrumentos específicos, como eles soam e como eles interagem entre si. Você pode usar essa combinação para criar determinados humores ou texturas:

- Um baixo sujo e distorcido lutando contra hi-hats limpos e nítidos
- Pads de sintetizador analógico quentes aumentando sob um violão acústico seco e intimista
- Uma parede de som criada por várias camadas de guitarras difusas, com vocais distantes e enterrados.

### Estrutura da música

Você pode descrever a progressão de uma música no comando. Use setas ou uma lista para definir o fluxo:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Comece com uma introdução de piano suave, aumente o volume em um verso alto, faça um silêncio e exploda no refrão.

Você também pode especificar como os níveis de energia mudam entre essas seções:

- Crie tensão no pré-refrão e depois faça um silêncio antes de um refrão enorme e
  explosivo
- Crescendo gradual ao longo da música, adicionando um instrumento de cada vez até uma parede caótica de som
- Parada repentina após a ponte, seguida de um refrão a capela

Você também pode pedir o horário exato em que quer que algo aconteça:

- Aumente até uma queda em 12 segundos
- Alguém diz "o quê" a cada 2 segundos
- O refrão começa aos 22 segundos

### Letras

Os vocais e a letra são gerados por padrão. Você pode fornecer suas próprias letras,
pedir para não incluir letras (ou um instrumental) ou direcionar a geração de letras
para o que você quiser.

As letras vão aparecer no idioma em que você escrever o comando. Você também pode pedir para as letras serem escritas em outro idioma, como "Escreva a letra em francês".

#### Usar suas próprias letras

Para dar suas próprias letras ao modelo, inclua-as no comando com um prefixo "Letra:":

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

Você pode prefixar partes da música com títulos de seção como `[Intro]`,
`[Verse 1]`, `[Pre-chorus]`, `[Chorus]` e `[Outro]`.

Se você quiser que uma palavra ou linha seja repetida, como um eco ou por cantores de apoio, inclua entre parênteses: "Vamos (vamos)".

#### Pedir ao modelo para escrever letras de músicas

Se você quiser que o Lyria 3 crie letras para você, é melhor incluir detalhes sobre o tema no comando. Caso contrário, o modelo precisará inferir um assunto com base no comando de música, e talvez não seja o que você quer.

> A letra fala sobre um amor perdido e a dor de um coração partido. A cantora está relembrando um relacionamento passado e as memórias que voltam à tona.

Se quiser um refrão repetido, peça isso no comando:

> A letra fala sobre um amor perdido e a dor de um coração partido. A cantora está relembrando um relacionamento passado e as memórias que voltam à tona. Um refrão forte se concentra em superar a dor e seguir em frente.

O Lyria 3 direciona automaticamente a estrutura da letra para o tipo de música que você está pedindo, mas você também pode reforçar isso no comando. Exemplo:

> Uma música eletrônica que repete a mesma frase energética várias vezes.

Também é possível pedir efeitos vocais que não sejam estritamente letras de músicas, por exemplo:

- Uma amostra repetida de um filme diz "Não consigo acreditar!" ao longo da música.
- Uma música techno de alta energia, logo antes da queda, o som para e uma voz diz: "Não sei o que estou fazendo aqui", e então a música começa.
- A música começa com uma conversa sobre os filmes dos anos 90 serem melhores do que os de hoje. Em seguida, a faixa passa para uma música pop.

### Vocais

Você pode pedir como quer que a letra seja entregue. Para ter os melhores resultados, especifique um perfil detalhado do cantor, incluindo gênero, timbre e extensão vocal.

- **Soprano feminino**: timbre claro e cristalino com uma qualidade ágil e crescente. Capaz de alcançar notas altas com um timbre leve e arejado.
- **Contralto feminino**: alcance mais baixo rico, quente e rouco. Timbre esfumaçado com um toque de vocal fry, cheio de alma e ressonante.
- **Tenor masculino**: brilhante, penetrante e energético. Timbre jovem com um leve toque nasal, que se destaca na mixagem com grande potência de belting.
- **Barítono masculino**: grave, com um toque de chocolate e suave como veludo. Voz de peito ressonante com uma entrega suave e melodiosa.
- **Rocker experiente (masculino)**: rouca e texturizada com um timbre grave, que lembra o grunge dos anos 90. Intervalo superior tenso para intensidade emocional.

### Outros parâmetros de comando

Você também pode incluir estes parâmetros para refinar ainda mais o comando:

- **Tonalidade/escala**: especifique uma tonalidade musical (por exemplo, "em sol maior", "ré menor").
- **Clima e atmosfera**: use adjetivos descritivos (por exemplo, "nostálgico", "agressivo", "etéreo", "onírico").
- **Duração**: o modelo de clipe sempre produz clipes de 30 segundos. Para o modelo Pro, especifique a duração desejada no comando (por exemplo, "crie uma música de 2 minutos") ou use carimbos de data/hora para controlar a duração.

### Exemplos de comandos

Confira alguns exemplos de comandos eficazes:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Práticas recomendadas

- **Itere primeiro com o Clipe.** Use o modelo `lyria-3-clip-preview` mais rápido para
  testar comandos antes de gerar um texto completo com
  `lyria-3-pro-preview`.
- **Faça uma descrição específica**. Comandos vagos produzem resultados genéricos. Mencione instrumentos, BPM, tom, humor e estrutura para ter o melhor resultado.
- **Use tags de seção.** As tags `[Verse]`, `[Chorus]` e `[Bridge]` oferecem ao modelo uma estrutura clara para seguir.
- **Separe a letra das instruções.** Ao fornecer letras personalizadas, separe-as claramente das instruções de direção musical.

## Limitações

- **Segurança**: todos os comandos são verificados por filtros de segurança. Os comandos que acionam os filtros serão bloqueados. Isso inclui comandos que pedem vozes de artistas específicos ou a geração de letras protegidas por direitos autorais.
- **Marca-d'água**: todos os áudios gerados incluem uma [marca-d'água digital do SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pt-br) para identificação. Essa marca-d'água é imperceptível ao ouvido humano e não afeta a experiência de audição.
- **Edição em várias etapas**: a geração de músicas é um processo de uma única etapa.
  A edição iterativa ou o refinamento de um clipe gerado com vários comandos não é compatível com a versão atual do Lyria 3.
- **Duração**: o modelo de clipe sempre gera clipes de 30 segundos. O modelo Pro
  gera músicas que duram alguns minutos. A duração exata pode ser
  influenciada pelo comando.
- **Determinismo**: os resultados podem variar entre as chamadas, mesmo com o mesmo comando.

## A seguir

- Confira os [preços](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br) dos modelos do Lyria 3.
- Teste a [geração de música em tempo real](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pt-br) com o
  Lyria RealTime.
- Gerar conversas com vários locutores usando os [modelos de TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=pt-br).
- Descubra como gerar [imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br) ou [vídeos](https://ai.google.dev/gemini-api/docs/video?hl=pt-br),
- Saiba como o Gemini pode [entender arquivos de áudio](https://ai.google.dev/gemini-api/docs/audio?hl=pt-br),
- Converse em tempo real com o Gemini usando a [API Live](https://ai.google.dev/gemini-api/docs/live?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-04-28 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-04-28 UTC."],[],[]]
