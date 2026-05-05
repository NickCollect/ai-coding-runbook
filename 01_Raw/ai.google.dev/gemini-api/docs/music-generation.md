---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=he
fetched_at: 2026-05-05T13:24:48.756362+00:00
title: "\u05d0\u05d9\u05da \u05d9\u05d5\u05e6\u05e8\u05d9\u05dd \u05de\u05d5\u05d6\u05d9\u05e7\u05d4 \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) זמין עכשיו בתצוגה מקדימה עם תכונות כמו תכנון שיתופי, ויזואליזציה, תמיכה ב-MCP ועוד.

- [דף הבית](https://ai.google.dev/gemini-api/docs/דף הבית)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

שליחת משוב

# איך יוצרים מוזיקה באמצעות Lyria 3

‫Lyria 3 היא משפחת מודלים של Google ליצירת מוזיקה, שזמינה דרך Gemini API. עם Lyria 3, אתם יכולים ליצור אודיו סטריאו באיכות גבוהה של 44.1 kHz מהנחיות טקסט או מתמונות. המודלים האלה מספקים קוהרנטיות מבנית, כולל שירה, מילים מתוזמנות ועיבודים מלאים של כלי נגינה.

משפחת Lyria 3 כוללת שני מודלים:

| דגם | מזהה דגם | הכי טוב עבור | משך | פלט |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | קליפים קצרים, לופים, קטעים מקדימים | ‫30 שניות | MP3 |
| ‫**Lyria 3 Pro** | `lyria-3-pro-preview` | שירים באורך מלא עם בתים, פזמונים וגשרים | כמה דקות (ניתן לשלוט באמצעות ההנחיה) | MP3 |

אפשר להשתמש בשני המודלים באמצעות ה-method הרגילה `generateContent` ו-[Interactions API](https://ai.google.dev/gemini-api/docs/Interactions API) החדש, הם תומכים בקלט מולטי-מודאלי (טקסט ותמונות) ומפיקים אודיו **סטריאו באיכות גבוהה של 44.1kHz**.

## יצירת קליפ מוזיקה

מודל Lyria 3 Clip תמיד יוצר קליפ באורך **30 שניות**. כדי ליצור קליפ, קוראים ל-method‏ `generateContent` עם הנחיית טקסט. התשובה תמיד כוללת את המילים שנוצרו ואת מבנה השיר לצד האודיו.

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

### C#‎

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

## יצירת שיר באורך מלא

אפשר להשתמש במודל `lyria-3-pro-preview` כדי ליצור שירים באורך מלא שנמשכים כמה דקות. מודל Pro מבין את המבנה המוזיקלי ויכול ליצור קומפוזיציות עם בתים, פזמונים וגשרים מובחנים. אפשר להשפיע על משך השיר על ידי ציון משך השיר בהנחיה (לדוגמה, 'צור שיר באורך 2 דקות') או על ידי שימוש [בחותמות זמן](https://ai.google.dev/gemini-api/docs/בחותמות זמן) כדי להגדיר את המבנה.

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

### C#‎

```
var response = await client.Models.GenerateContentAsync(
  model: "lyria-3-pro-preview",
  contents: "An epic cinematic orchestral piece about a journey home. " +
            "Starts with a solo piano intro, builds through sweeping " +
            "strings, and climaxes with a massive wall of sound."
);
```

## בחירת פורמט הפלט

כברירת מחדל, מודלים של Lyria 3 יוצרים אודיו בפורמט **MP3**. ב-Lyria 3 Pro, אפשר גם לבקש את הפלט בפורמט **WAV** על ידי הגדרת `response_mime_type` ב-`generationConfig`.

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

### C#‎

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

## ניתוח התשובה

התשובה מ-Lyria 3 מכילה כמה חלקים. חלקים של טקסט מכילים את המילים שנוצרו או תיאור JSON של מבנה השיר. החלקים עם `inline_data` מכילים את בייטים של האודיו.

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

### C#‎

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

## יצירת מוזיקה מתמונות

‫Lyria 3 תומך בקלט מרובה-אופנים – אתם יכולים לספק עד **10 תמונות** לצד הנחיית הטקסט, והמודל ייצור מוזיקה בהשראת התוכן החזותי.

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

### C#‎

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

## ציון מילות שיר מותאמות אישית

אתם יכולים לכתוב מילים משלכם ולכלול אותן בהנחיה. כדי לעזור למודל להבין את מבנה השיר, כדאי להשתמש בתגי קטע כמו `[Verse]`, `[Chorus]` ו-`[Bridge]`:

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

### C#‎

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

](https://ai.google.dev/gemini-api/docs/music-generation?hl=he)

## שליטה בתזמון ובמבנה

אתם יכולים לציין בדיוק מה קורה ברגעים מסוימים בשיר באמצעות חותמות זמן. התכונה הזו שימושית כדי לקבוע מתי כלי נגינה נכנסים, מתי המילים מוצגות ואיך השיר מתקדם:

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

### C#‎

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

## יצירת טראקים אינסטרומנטליים

כדי ליצור מוזיקת רקע, פסקולים למשחקים או כל מקרה שימוש אחר שלא דורש שירה, אפשר להנחות את המודל ליצור טראקים אינסטרומנטליים בלבד:

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

### C#‎

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

## יצירת מוזיקה בשפות שונות

‫Lyria 3 יוצר מילים לשיר בשפה שבה ניתנה ההנחיה. כדי ליצור שיר עם מילים בצרפתית, כותבים את ההנחיה בצרפתית. המודל מתאים את סגנון הקול וההגייה שלו לשפה.

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

### C#‎

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

## הבינה של המודל

מודל Lyria 3 מנתח את תהליך ההנחיה שבו המודל מנמק את המבנה המוזיקלי (פתיחה, בית, פזמון, מעבר וכו') על סמך ההנחיה שלכם.
התהליך הזה מתרחש לפני יצירת האודיו, והוא מבטיח עקביות מבנית ומוזיקליות.

## Interactions API

אתם יכולים להשתמש במודלים של Lyria 3 עם [Interactions API](https://ai.google.dev/gemini-api/docs/Interactions API), ממשק מאוחד לאינטראקציה עם מודלים וסוכנים של Gemini. הוא מפשט את ניהול המצב ומשימות ארוכות טווח בתרחישי שימוש מורכבים עם כמה אמצעי קלט.

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

## מדריך לכתיבת הנחיות

ההנחיה יכולה להיות פשוטה כמו "שיר פולק על חתולים חמודים שנמנעים מלהיכנס לשלוליות,
שירה של אישה ורעש של גשם", או מפורטת ומובנית יותר
כמו:

> טראק סינת'פופ בסגנון שנות ה-80 עם ביט קצבי, סינתיסייזרים מבריקים ופזמון קליט בסגנון המנוני. השיר צריך להיות רטרו-עתידני,
> בסגנון של להיטי פופ קלאסיים משנות ה-80, עם ליטוש הפקה מודרני. הטמפו צריך להיות קצבי ומתאים לריקוד, בסביבות 120 פעימות בדקה, עם מבנה ברור של בית ופזמון וקטע אינסטרומנטלי קליט. מילות השיר מתארות את התחושה של התכוננות למסיבה.

הנחיות פשוטות ומורכבות יכולות להניב תוצאות טובות. מומלץ להתנסות בטיפים האלה כדי למצוא את מה שהכי מתאים לכם.

### ז'אנר

מתחילים את ההנחיה עם ז'אנר המוזיקה הרצוי, כמו היפ-הופ, רוק וראפ. אפשר לציין שילוב של ז'אנרים:

- מיזוג של מטאל וראפ
- שילוב של דת' מטאל ואופרה
- יצירה קלאסית עם אלמנטים אלקטרוניים של צליל רקע
- מוזיקת דאנס אלקטרונית (EDM) מודרנית עם אלמנטים של יורופופ

אפשר גם לשלב תקופה:

- היפ-הופ מתחילת שנות ה-90
- פופ יי-יי צרפתי משנות ה-60
- ניסויים אלקטרוניים משנות ה-80
- פופ מיינסטרים משנות האלפיים

אם תבקשו ז'אנרים מותאמים אישית או וריאציות אזוריות, כמו "טכנו ברלינאי" או "הייפי מאזור המפרץ", המודל ינסה לתפוס את המהות הזו, אבל יכול להיות שהוא לא תמיד יצליח.

### כלי נגינה

כברירת מחדל, Lyria 3 יוצר שירים עם כלי הנגינה והכלים שמתאימים לז'אנר. לא צריך לתת הוראות מדויקות.

עם זאת, טראק של מוזיקת דאנס לא יכלול סקסופון אלא אם תבקשו אותו. לכן, אם רוצים סולו סקסופון, צריך לתת הנחיה:

> טראק לריקודים עם קצב ממריץ, סינתיסייזרים מבריקים ופזמון קליט וסוחף. סולו סקסופון צריך להופיע במהלך הגשר.

ההנחיה יכולה לכלול כלים ספציפיים, איך הם נשמעים ואיך הם פועלים אחד עם השני. אפשר להשתמש בשילוב הזה כדי ליצור מצבי רוח או מרקמים מסוימים:

- קו בס מלוכלך ומעוות נאבק עם צלילי היי-האט נקיים וחדים
- פדים חמים של סינתיסייזר אנלוגי מתגברים מתחת לגיטרה אקוסטית אינטימית ופשוטה
- קיר של צלילים שנוצר על ידי שכבות רבות של גיטרות עם דיסטורשן, עם שירה רחוקה ומוסתרת

### מבנה השיר

אתם יכולים לתאר בהנחיה את ההתקדמות של השיר. משתמשים בחצים או ברשימה כדי להגדיר את התהליך:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- מתחילים עם פתיחה שקטה בפסנתר, עוברים לבית חזק, מגיעים לשקט ואז מתפוצצים בפזמון.

אפשר גם לציין איך רמות האנרגיה משתנות בין הקטעים האלה:

- יוצרים מתח לפני הפזמון, ואז עוברים לשקט לפני פזמון עוצמתי וסוחף
- קצב הולך וגובר לאורך השיר, עם הוספה של כלי נגינה אחד בכל פעם
  עד שנוצר קיר כאוטי של צלילים
- הפסקה פתאומית אחרי הגשר, ואז פזמון א-קפלה

אפשר גם להנחות את Google Assistant לבצע פעולה בשעה מסוימת:

- Build to a drop at 12s
- מישהו אומר "מה" כל 2 שניות
- הפזמון מתחיל ב-0:22

### מילות השיר

השירה והמילים נוצרות כברירת מחדל. אתם יכולים לספק מילים משלכם, לבקש שלא יהיו מילים (או שיהיה קטע אינסטרומנטלי) או לכוון את יצירת המילים לכיוון שאתם רוצים.

המילים של השיר יהיו בשפה שבה כתבתם את ההנחיה. אפשר גם לבקש לכתוב את המילים בשפה אחרת, למשל: "Write the lyrics in French" (כתוב את המילים בצרפתית).

#### שימוש במילים שלכם

כדי לתת למודל מילות שיר משלכם, צריך לכלול אותן בהנחיה עם הקידומת Lyrics:‎:

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

אפשר להוסיף כותרות לחלקים בשיר, כמו `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` ו-`[Outro]`.

אם רוצים שמילה או שורה יחזרו על עצמן, כמו הד או זמרי ליווי, אפשר לכלול אותן בסוגריים: Let's go (go).

#### הנחיה של המודל לכתוב מילים לשיר

אם רוצים ש-Lyria 3 ייצור מילים לשיר, מומלץ לכלול בהנחיה פרטים על מה יהיו המילים. אחרת, המודל יצטרך להסיק את הנושא מההנחיה שנתתם לגבי המוזיקה, ויכול להיות שהתוצאה לא תהיה מה שרציתם.

> המילים הן על אהבה אבודה ועל הכאב של שברון לב. הזמרת נזכרת במערכת יחסים שהייתה לה בעבר ובזיכרונות שצפים ועולים.

אם רוצים פזמון חוזר, כדאי לבקש אותו בהנחיה:

> המילים הן על אהבה אבודה וכאב של שברון לב. הזמרת נזכרת במערכת יחסים שהייתה לה בעבר ובזיכרונות שצפים ועולים. פזמון עוצמתי שמתמקד בהתגברות על הכאב ובמעבר הלאה.

מודל Lyria 3 יכוון אוטומטית את מבנה המילים לסוג המוזיקה שביקשתם, אבל אתם יכולים להדגיש את זה גם בהנחיה. לדוגמה:

> שיר EDM שחוזר על אותו ביטוי אנרגטי שוב ושוב.

אפשר גם להנחות את המודל ליצור אפקטים קוליים שהם לא מילים של שיר, למשל:

- דגימה חוזרת מסרט עם המילים "I can't believe this!‎" (לא ייאמן!) לאורך השיר
- טראק טכנו עם אנרגיה גבוהה, ממש לפני הדרופ הצליל מפסיק לגמרי וקול קטן אומר "I don't know what I'm doing here", ואז המוזיקה מתחילה.
- השיר מתחיל בשיחה על כך שהסרטים של שנות ה-90 היו טובים יותר מהסרטים של היום. ואז הטראק עובר בצורה חלקה לשיר פופ.

### כולל שירה

אפשר לתת הנחיה לגבי אופן הצגת המילים. כדי לקבל את התוצאות הטובות ביותר, כדאי לציין פרופיל מפורט של הזמר או הזמרת, כולל מגדר, גוון ומנעד קולי.

- **סופרן נשי**: צליל ברור וצלול עם גוון קליל ומרחף. היא מסוגלת להגיע לתווים גבוהים עם שריקה, עם מרקם אוורירי ונושם.
- **אלט נשי**: טווח נמוך עשיר, חם וצרוד. גוון קולי מעושן עם נגיעה של קול צרוד, מלא נשמה ומהדהד.
- **טנור גברי**: בהיר, חודר ואנרגטי. גוון קול צעיר עם נגיעה קלה של קול אפי, שמתבלט במיקס עם עוצמת שירה גבוהה.
- **בריטון גברי**: עמוק, עשיר וקטיפתי. קול עמוק ומהדהד עם טון מרגיע ונעים.
- **רוקר מחוספס (גבר)**: צרוד ומחוספס עם גוון חצצי, שמזכיר גראנג' משנות ה-90. מאמץ רב בטווח העליון של העוצמה הרגשית.

### פרמטרים נוספים של הנחיות

אפשר גם לכלול את הפרמטרים האלה כדי לשפר עוד יותר את ההנחיה:

- **טון/סולם**: מציינים טון מוזיקלי (לדוגמה, "בסולם סול מז'ור", "בסולם רה מינור").
- **מצב רוח ואווירה**: השתמשו בשמות תואר תיאוריים (למשל, "נוסטלגי", "אגרסיבי", "שמימי", "חלומות").
- **משך**: מודל הקליפים תמיד יוצר קליפים באורך 30 שניות. במודל Pro, מציינים את האורך הרצוי בהנחיה (לדוגמה, 'צור שיר באורך 2 דקות') או משתמשים בחותמות זמן כדי לשלוט במשך.

### הנחיות לדוגמה

הנה כמה דוגמאות להנחיות יעילות:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## שיטות מומלצות

- **כדאי להתחיל עם קליפ.** כדאי להשתמש במודל המהיר יותר `lyria-3-clip-preview` כדי להתנסות בהנחיות לפני שמתחייבים ליצירה באורך מלא באמצעות `lyria-3-pro-preview`.
- **ספציפיות היא שם המשחק.** הנחיות מעורפלות מניבות תוצאות גנריות. כדי לקבל את התוצאה הכי טובה, כדאי לציין כלי נגינה, BPM, סולם, מצב רוח ומבנה.
- **כדאי להשתמש בתגי קטע.** תגי `[Verse]`, ‏`[Chorus]` ו-`[Bridge]` מספקים למודל מבנה ברור לפעולה.
- **מפרידים בין מילות השיר להוראות.** כשמספקים מילים בהתאמה אישית, צריך להפריד אותן בבירור מההוראות לגבי המוזיקה.

## מגבלות

- **בטיחות**: כל ההנחיות נבדקות על ידי מסנני בטיחות. הנחיות שמפעילות את המסננים ייחסמו. זה כולל הנחיות שמבקשות קולות ספציפיים של אומנים או יצירה של מילות שירים שמוגנות בזכויות יוצרים.
- **סימני מים**: כל האודיו שנוצר כולל [סימן מים באודיו של SynthID](https://ai.google.dev/gemini-api/docs/סימן מים באודיו של SynthID) לצורך זיהוי. סימן המים הזה לא נשמע לאוזן אנושית ולא משפיע על חוויית ההאזנה.
- **עריכה בכמה שלבים**: יצירת מוזיקה היא תהליך חד-שלבי.
  בגרסה הנוכחית של Lyria 3 אין תמיכה בעריכה איטרטיבית או בשיפור של קליפ שנוצר באמצעות כמה הנחיות.
- **אורך**: מודל הקליפים תמיד יוצר קליפים באורך 30 שניות. מודל Pro יוצר שירים באורך של כמה דקות. אפשר להשפיע על האורך המדויק באמצעות ההנחיה.
- **דטרמיניזם**: התוצאות עשויות להיות שונות בין שיחות, גם אם משתמשים באותה הנחיה.

## המאמרים הבאים

- כדאי לעיין ב[תמחור](https://ai.google.dev/gemini-api/docs/תמחור) של מודלים של Lyria 3,
- כדאי לנסות [יצירת מוזיקה בזמן אמת בסטרימינג](https://ai.google.dev/gemini-api/docs/יצירת מוזיקה בזמן אמת בסטרימינג) באמצעות Lyria RealTime,
- יצירת שיחות עם כמה דוברים באמצעות [מודלים של TTS](https://ai.google.dev/gemini-api/docs/מודלים של TTS),
- [איך יוצרים תמונות](https://ai.google.dev/gemini-api/docs/איך יוצרים תמונות) או [סרטונים](https://ai.google.dev/gemini-api/docs/סרטונים)
- [איך Gemini יכול להבין קובצי אודיו](https://ai.google.dev/gemini-api/docs/איך Gemini יכול להבין קובצי אודיו),
- מנהלים שיחה בזמן אמת עם Gemini באמצעות [Live API](https://ai.google.dev/gemini-api/docs/Live API).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://ai.google.dev/gemini-api/docs/מדיניות האתר Google Developers‏).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-04-28 (שעון UTC).

רוצה לתת לנו משוב?
