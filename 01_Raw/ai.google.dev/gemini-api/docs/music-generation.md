---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=pl
fetched_at: 2026-05-05T19:48:06.298907+00:00
title: "Generowanie muzyki za pomoc\u0105 Lyrii\u00a03 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie muzyki za pomocą Lyrii 3

Lyria 3 to rodzina modeli generowania muzyki od Google, dostępna w ramach Gemini API. Za pomocą Lyrii 3 możesz generować wysokiej jakości dźwięk stereo o częstotliwości 44,1 kHz na podstawie promptów tekstowych lub obrazów. Modele te zapewniają spójność strukturalną, w tym wokal, zsynchronizowany tekst i pełne aranżacje instrumentalne.

Rodzina modeli Lyria 3 obejmuje 2 modele:

| Model | Identyfikator modelu | Urządzenia | Czas trwania | Wyniki |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | krótkie klipy, pętle, wersje przedpremierowe; | 30 sekund | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | pełne utwory z wersami, refrenami i przejściami; | Kilka minut (można kontrolować za pomocą prompta) | MP3 |

Oba modele można używać za pomocą standardowej metody `generateContent` i nowego [interfejsu API Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=pl), który obsługuje dane wejściowe multimodalne (tekst i obrazy) i generuje **stereofoniczny dźwięk o wysokiej wierności 44,1 kHz**.

## Generowanie klipu muzycznego

Model Lyria 3 Clip zawsze generuje **30-sekundowy** klip. Aby wygenerować klip, wywołaj metodę `generateContent` z promptem tekstowym. Odpowiedź zawsze zawiera wygenerowany tekst i strukturę utworu wraz z dźwiękiem.

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

## Generowanie pełnych utworów

Użyj modelu `lyria-3-pro-preview`, aby wygenerować pełne utwory trwające kilka minut. Model Pro rozumie strukturę muzyczną i może tworzyć kompozycje z wyraźnymi zwrotkami, refrenami i przejściami. Możesz wpłynąć na czas trwania utworu, podając go w prompcie (np. „utwórz 2-minutową piosenkę”) lub używając [sygnatur czasowych](#timing) do zdefiniowania struktury.

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

## Wybierz format wyjściowy

Domyślnie modele Lyria 3 generują dźwięk w formacie **MP3**. W przypadku Lyrii 3 Pro możesz też poprosić o wygenerowanie danych wyjściowych w formacie **WAV**, ustawiając `response_mime_type` w `generationConfig`.

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

## Analizowanie odpowiedzi

Odpowiedź z Lyrii 3 zawiera wiele części. Części tekstowe zawierają wygenerowany tekst piosenki lub opis struktury utworu w formacie JSON. Części z `inline_data` zawierają bajty audio.

przechodź przez wszystkie części i sprawdzaj typ każdej z nich.

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

## Generowanie muzyki na podstawie obrazów

Lyria 3 obsługuje dane wejściowe multimodalne – możesz przesłać maksymalnie **10 obrazów**
wraz z promptem tekstowym, a model skomponuje muzykę inspirowaną treściami wizualnymi.

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

## Podaj własny tekst

Możesz napisać własny tekst i uwzględnić go w prompcie. Używaj tagów sekcji, takich jak `[Verse]`, `[Chorus]` i `[Bridge]`, aby pomóc modelowi zrozumieć strukturę utworu:

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

## Kontrolowanie czasu i struktury

Za pomocą sygnatur czasowych możesz określić, co dokładnie ma się dziać w konkretnych momentach utworu. Jest to przydatne do kontrolowania, kiedy wchodzą instrumenty, kiedy pojawiają się słowa i jak rozwija się utwór:

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

## Generowanie utworów instrumentalnych

W przypadku muzyki w tle, ścieżek dźwiękowych do gier lub innych zastosowań, w których nie są wymagane wokale, możesz poprosić model o wygenerowanie utworów instrumentalnych:

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

## Generowanie muzyki w różnych językach

Lyria 3 generuje tekst w języku prompta. Aby wygenerować utwór z tekstem w języku francuskim, napisz prompt w tym języku. Model dostosowuje styl głosu i wymowę do języka.

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

## Inteligencja modelu

Lyria 3 analizuje proces promptowania, w którym model wnioskuje na podstawie prompta o strukturze muzycznej (intro, zwrotka, refren, bridge itp.).
Dzieje się to przed wygenerowaniem dźwięku i zapewnia spójność strukturalną oraz muzykalność.

## Interactions API

Możesz używać modeli Lyria 3 z [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=pl), czyli ujednoliconego interfejsu do interakcji z modelami i agentami Gemini. Upraszcza zarządzanie stanem i długotrwałymi zadaniami w przypadku złożonych zastosowań multimodalnych.

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

## Przewodnik po promptach

Prompt może być tak prosty jak „piosenka folkowa o słodkich kotach unikających kałuż, śpiewana przez kobietę, z odgłosami deszczu” lub bardziej szczegółowy i złożony, np.:

> Utwór synth-popowy w stylu lat 80. z dynamicznym rytmem, mieniącymi się syntezatorami i chwytliwym, hymnicznym refrenem. Utwór powinien mieć retro-futurystyczny charakter, przypominający klasyczne hity pop z lat 80., ale z nowoczesną produkcją. Tempo powinno być szybkie i zachęcające do tańca, około 120 BPM, z wyraźną strukturą zwrotka-refren i zapamiętywalnym instrumentalnym motywem. Tekst opowiada o przygotowaniach do imprezy.

Zarówno proste, jak i złożone prompty mogą dać dobre wyniki. Zalecamy eksperymentowanie z tymi wskazówkami, aby znaleźć najlepsze rozwiązanie dla siebie.

### Gatunek

Zacznij prompt od gatunku muzyki, np. hip-hop, rock i rap. Możesz określić mieszankę gatunków:

- Połączenie metalu i rapu
- Połączenie death metalu i opery
- Klasyczny utwór z elementami elektronicznymi
- Nowoczesna elektroniczna muzyka taneczna (EDM) zmiksowana z europopem

Możesz też uwzględnić epokę:

- Hip-hop z początku lat 90.
- Francuski pop ye-ye z lat 60.
- Eksperymenty z elektroniką w latach 80.
- Pop z pierwszej dekady XXI wieku

Jeśli poprosisz o wygenerowanie muzyki w określonym gatunku lub wariancie regionalnym, np. „techno z Berlina” lub „hyphy z Bay Area”, model spróbuje uchwycić ten charakter, ale nie zawsze mu się to uda.

### Instrumenty

Domyślnie Lyria 3 tworzy utwory z instrumentami i narzędziami, których można się spodziewać w danym gatunku. Nie musisz być zbyt szczegółowy.

Jednak utwór taneczny nie będzie zawierał saksofonu, chyba że o to poprosisz. Jeśli chcesz, aby w utworze pojawiła się partia solowa saksofonu, musisz to zaznaczyć w prompcie:

> Utwór taneczny z pulsującym rytmem, błyszczącymi syntezatorami i wpadającym w ucho, hymnicznym refrenem. Podczas bridge’a powinno pojawić się solo na saksofonie.

Prompt może zawierać konkretne instrumenty, ich brzmienie i sposób, w jaki ze sobą współdziałają. Możesz użyć tej kombinacji, aby stworzyć określony nastrój lub teksturę:

- Brudna, zniekształcona linia basu walcząca z czystymi, wyrazistymi hi-hatami
- Ciepłe, analogowe pady syntezatorowe narastające pod suchą, intymną gitarą akustyczną
- Ściana dźwięku stworzona przez wiele warstw rozmytych gitar z ukrytym, odległym wokalem.

### Struktura utworu

W prompcie możesz opisać progresję utworu. Aby zdefiniować przepływ, użyj strzałek lub listy:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Zacznij od cichego intra na pianinie, przejdź do głośnej zwrotki, zrób przerwę, a potem przejdź do refrenu.

Możesz też określić, jak zmienia się poziom energii między tymi sekcjami:

- Buduj napięcie w prechorusie, a potem wycisz utwór przed potężnym, wybuchowym refrenem.
- Stopniowe crescendo w całym utworze, dodawanie po jednym instrumencie, aż do chaotycznej ściany dźwięku.
- Nagłe zatrzymanie po moście, a następnie chór a cappella

Możesz też podać dokładną godzinę, o której ma się coś wydarzyć:

- Budowanie do momentu spadku w 12 sekundzie
- Ktoś co 2 sekundy mówi „co”
- Refren zaczyna się w 22 sekundzie

### Tekst

Wokale i teksty są generowane domyślnie. Możesz podać własne teksty, poprosić o brak tekstów (lub o wersję instrumentalną) albo pokierować generowaniem tekstów w wybranym przez siebie kierunku.

Tekst piosenki będzie w języku, w którym napiszesz prompt. Możesz też poprosić o tekst w innym języku, np. „Napisz tekst w języku francuskim”.

#### Używanie własnych tekstów

Aby podać modelowi własny tekst, dodaj go do promptu z prefiksem „Lyrics:” (Tekst:):

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

Możesz dodać do części utworu tytuły sekcji, takie jak `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` i `[Outro]`.

Jeśli chcesz, aby słowo lub wiersz się powtarzał, np. jako echo lub w wykonaniu chórzystów, możesz umieścić go w nawiasach: „Let's go (go)”.

#### Promptowanie modelu do pisania tekstów

Jeśli chcesz, aby Lyria 3 napisała dla Ciebie tekst piosenki, najlepiej podaj w prompcie szczegóły dotyczące tego, o czym ma być ten tekst. W przeciwnym razie model będzie musiał wywnioskować temat na podstawie promptu dotyczącego muzyki, a wynik może nie być zgodny z Twoimi oczekiwaniami.

> Tekst opowiada o utraconej miłości i bólu złamanego serca. Piosenkarka wspomina dawny związek i zalewają ją wspomnienia.

Jeśli chcesz, aby refren się powtarzał, poproś o to w prompcie:

> Tekst opowiada o utraconej miłości i bólu złamanego serca. Piosenkarka wspomina dawny związek i zalewają ją wspomnienia. Potężny refren skupia się na przezwyciężeniu bólu i ruszeniu dalej.

Lyria 3 automatycznie dostosuje strukturę tekstu do rodzaju muzyki, o którą prosisz, ale możesz to również podkreślić w prompcie. Na przykład:

> Utwór EDM, w którym w kółko powtarza się to samo energiczne wyrażenie.

Możesz też poprosić o efekty wokalne, które nie są ściśle związane z tekstem, np.:

- W utworze powtarza się fragment filmu z dialogiem „Nie wierzę w to!”.
- Energetyczny utwór techno. Tuż przed kulminacją dźwięk nagle się urywa i słychać cichy głos, który mówi: „Nie wiem, co tu robię”. Potem następuje kulminacja.
- Utwór rozpoczyna się rozmową o tym, że filmy z lat 90. były lepsze niż te, które powstają obecnie. Następnie utwór przechodzi w piosenkę popową.

### Wokale

Możesz określić, w jaki sposób chcesz otrzymać tekst. Aby uzyskać najlepsze wyniki, podaj szczegółowy profil wokalisty, w tym płeć, barwę i zakres głosu.

- **Sopran żeński:** czysta, krystaliczna barwa głosu o zwinnej, wznoszącej się jakości. Potrafi osiągać wysokie tony o powietrznej, zwiewnej fakturze.
- **Alt żeński:** bogaty, ciepły i chrapliwy niższy zakres. Głos o dymnym brzmieniu z elementami fry, pełen duszy i rezonansu.
- **Tenor męski**: jasny, przenikliwy i energiczny. Młodzieńczy tembr z lekkim nosowym zabarwieniem, przebijający się przez miks dzięki wysokiej mocy beltingu.
- **Baryton męski:** głęboki, czekoladowy i aksamitnie gładki. Głos z głębi klatki piersiowej, kojący i miękki.
- **Weathered Rocker (Male)**: chrapliwy i szorstki głos o grubym brzmieniu, przypominający grunge z lat 90. Wysoki zakres intensywności emocjonalnej.

### Inne parametry promptu

Aby jeszcze bardziej doprecyzować prompt, możesz też dodać te parametry:

- **Tonacja:** podaj tonację (np. „w tonacji G-dur”, „d-moll”).
- **Nastrój i atmosfera:** używaj przymiotników opisowych (np. „nostalgiczny”, „agresywny”, „etericzny”, „marzycielski”).
- **Czas trwania:** model Clip zawsze tworzy 30-sekundowe klipy. W przypadku modelu Pro określ w prompcie żądaną długość (np. „utwórz 2-minutową piosenkę”) lub użyj sygnatur czasowych, aby kontrolować czas trwania.

### Przykładowe prompty

Oto kilka przykładów skutecznych promptów:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Sprawdzone metody

- **Najpierw iteruj za pomocą funkcji Clip.** Używaj szybszego modelu `lyria-3-clip-preview`, aby eksperymentować z promptami, zanim zdecydujesz się na wygenerowanie pełnej wersji za pomocą modelu `lyria-3-pro-preview`.
- **Unikaj ogólników.** Niejasne prompty dają ogólne wyniki. Aby uzyskać najlepszy wynik, podaj instrumenty, tempo, tonację, nastrój i strukturę.
- **Używaj tagów sekcji.** Tagi `[Verse]`, `[Chorus]` i `[Bridge]` nadają modelowi wyraźną strukturę, której może się trzymać.
- **Oddziel słowa piosenki od instrukcji.** Podczas podawania niestandardowego tekstu wyraźnie oddziel go od instrukcji dotyczących kierunku muzycznego.

## Ograniczenia

- **Bezpieczeństwo:** wszystkie prompty są sprawdzane przez filtry bezpieczeństwa. Prompty, które aktywują filtry, zostaną zablokowane. Obejmuje to prompty, które wymagają konkretnych głosów artystów lub generowania tekstów chronionych prawem autorskim.
- **Dodawanie znaków wodnych:** wszystkie wygenerowane pliki audio zawierają [znak wodny audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pl), który umożliwia identyfikację. Ten znak wodny jest niesłyszalny dla ludzkiego ucha i nie wpływa na jakość odsłuchu.
- **Edytowanie wieloetapowe:** generowanie muzyki to proces jednoetapowy.
  Iteracyjne edytowanie lub ulepszanie wygenerowanego klipu za pomocą wielu promptów nie jest obsługiwane w obecnej wersji Lyrii 3.
- **Długość:** model Clip zawsze generuje 30-sekundowe klipy. Model Pro generuje utwory trwające kilka minut. Na dokładny czas trwania może wpływać prompt.
- **Determinacja:** wyniki mogą się różnić w zależności od połączenia, nawet w przypadku tego samego prompta.

## Co dalej?

- Sprawdź [ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) modeli Lyria 3.
- Wypróbuj [generowanie muzyki w czasie rzeczywistym](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pl) za pomocą Lyrii RealTime.
- generować rozmowy z udziałem wielu osób za pomocą [modeli TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=pl),
- Dowiedz się, jak generować [obrazy](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) i [filmy](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- Dowiedz się, jak Gemini może [rozumieć pliki audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl),
- Prowadź rozmowy z Gemini w czasie rzeczywistym za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-28 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-28 UTC."],[],[]]
