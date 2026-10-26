---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/music-generation?hl=hi
fetched_at: 2026-10-26T05:42:06.713955+00:00
title: "Lyria 3.5 \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0938\u0902\u0917\u0940\u0924 \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# Lyria 3.5 की मदद से संगीत जनरेट करना

Lyria 3.5, संगीत जनरेट करने की सुविधा वाले Google के मॉडल हैं. ये Gemini API के ज़रिए उपलब्ध हैं. Lyria 3.5 की मदद से, टेक्स्ट प्रॉम्प्ट या इमेज से 44.1 किलोहर्ट्ज़ का अच्छी क्वालिटी वाला स्टीरियो ऑडियो जनरेट किया जा सकता है. ये मॉडल, संगीत की संरचना को बेहतर बनाते हैं. इनमें वोकल, समय के हिसाब से लिरिक्स, और इंस्ट्रुमेंटल अरेंजमेंट शामिल हैं.

Lyria फ़ैमिली में ये मॉडल शामिल हैं:

| मॉडल | मॉडल आईडी | इन स्थितियों में बेहतर है | कुल समय | आउटपुट |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | शॉर्ट वीडियो, क्लिप, लूप, झलक | 30 सेकंड | MP3 |
| **Lyria 3.5** | `lyria-3.5` | पूरे गाने, जिनमें वर्स, कोरस, और ब्रिज शामिल हों | कुछ मिनट (प्रॉम्प्ट के ज़रिए कंट्रोल किया जा सकता है) | MP3 |

दोनों मॉडल का इस्तेमाल, स्टैंडर्ड `generateContent` तरीके और नए [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) का इस्तेमाल करके किया जा सकता है. ये मॉडल, मल्टीमोडल इनपुट (टेक्स्ट और इमेज) के साथ काम करते हैं. साथ ही, **44.1 किलोहर्ट्ज़ का हाई-फ़िडेलिटी स्टीरियो** ऑडियो जनरेट करते हैं.

## म्यूज़िक क्लिप जनरेट करना

Lyria 3 Clip मॉडल, हमेशा **30 सेकंड** की क्लिप जनरेट करता है. कोई क्लिप जनरेट करने के लिए, टेक्स्ट प्रॉम्प्ट के साथ `generateContent` तरीके को कॉल करें. जवाब में, जनरेट किए गए गाने के बोल और गाने के स्ट्रक्चर के साथ-साथ ऑडियो भी शामिल होता है.

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

### ऐप पर जाएं

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

### आराम का समय

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

## पूरा गाना जनरेट करना

`lyria-3.5` मॉडल का इस्तेमाल करके, कुछ मिनटों के गाने जनरेट करें. Pro मॉडल, संगीत के स्ट्रक्चर को समझता है. साथ ही, अलग-अलग वर्स, कोरस, और ब्रिज के साथ कंपोज़िशन बना सकता है. गाने की अवधि तय करने के लिए, अपने प्रॉम्प्ट में अवधि बताएं (जैसे, "दो मिनट का गाना बनाओ") या गाने का स्ट्रक्चर तय करने के लिए [टाइमस्टैंप](#timing) का इस्तेमाल करें.

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

### ऐप पर जाएं

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

### आराम का समय

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

## आउटपुट फ़ॉर्मैट चुनें

डिफ़ॉल्ट रूप से, Lyria 3.5 मॉडल **MP3** फ़ॉर्मैट में ऑडियो जनरेट करते हैं. Lyria 3.5 के लिए, **WAV** (`AUDIO_WAV`) फ़ॉर्मैट में भी आउटपुट का अनुरोध किया जा सकता है. इसके लिए, `generationConfig.responseFormat.audio.mimeType` को `"AUDIO_WAV"` पर सेट करें.

### आराम का समय

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
      "responseFormat": { "audio": { "mimeType": "AUDIO_WAV" } }
    }
  }'
```

## जवाब को पार्स करना

Lyria 3.5 से मिले जवाब में कई हिस्से होते हैं. टेक्स्ट वाले हिस्सों में, जनरेट किए गए बोल या गाने के स्ट्रक्चर का JSON ब्यौरा शामिल होता है. `inline_data` वाले हिस्सों में ऑडियो बाइट होते हैं.

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

### ऐप पर जाएं

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

### आराम का समय

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' | base64 -d > output.mp3
```

## इमेज से संगीत जनरेट करना

Lyria 3.5 में मल्टीमोडल इनपुट इस्तेमाल किए जा सकते हैं. इसमें टेक्स्ट प्रॉम्प्ट के साथ-साथ, ज़्यादा से ज़्यादा **10 इमेज** अपलोड की जा सकती हैं. इसके बाद, यह मॉडल विज़ुअल कॉन्टेंट के हिसाब से संगीत तैयार करेगा.

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

### ऐप पर जाएं

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

### आराम का समय

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

## गाने के बोल अपनी पसंद के मुताबिक जोड़ना

आपके पास खुद के बोल लिखने और उन्हें प्रॉम्प्ट में शामिल करने का विकल्प है. `[Verse]`, `[Chorus]`, और `[Bridge]` जैसे सेक्शन टैग का इस्तेमाल करें, ताकि मॉडल को गाने का स्ट्रक्चर समझने में मदद मिल सके:

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

### ऐप पर जाएं

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

### आराम का समय

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

## समय और स्ट्रक्चर को कंट्रोल करना

टाइमस्टैंप का इस्तेमाल करके, यह तय किया जा सकता है कि गाने के खास पलों में क्या होगा. यह सुविधा, गाने में इंस्ट्रुमेंट और बोल को सही समय पर शामिल करने और गाने को आगे बढ़ाने में मदद करती है:

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

### ऐप पर जाएं

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

### आराम का समय

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

## इंस्ट्रुमेंटल ट्रैक जनरेट करना

बैकग्राउंड म्यूज़िक, गेम के साउंडट्रैक या ऐसे किसी भी इस्तेमाल के लिए जहां वोकल की ज़रूरत नहीं है, मॉडल को सिर्फ़ इंस्ट्रुमेंटल ट्रैक बनाने के लिए कहा जा सकता है:

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

### ऐप पर जाएं

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

### आराम का समय

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

## अलग-अलग भाषाओं में संगीत जनरेट करना

Lyria 3.5, आपके प्रॉम्प्ट की भाषा में गाने के बोल जनरेट करता है. फ़्रेंच भाषा में गाने के बोल जनरेट करने के लिए, फ़्रेंच में प्रॉम्प्ट लिखें. यह मॉडल, भाषा के हिसाब से अपनी आवाज़ की स्टाइल और उच्चारण को अडजस्ट करता है.

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

### ऐप पर जाएं

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

### आराम का समय

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

## मॉडल इंटेलिजेंस

Lyria 3.5 आपके प्रॉम्प्ट का विश्लेषण करता है. इसके बाद, मॉडल आपके प्रॉम्प्ट के आधार पर संगीत के स्ट्रक्चर (इंट्रो, वर्स, कोरस, ब्रिज वगैरह) को समझता है.
यह ऑडियो जनरेट होने से पहले होता है. इससे यह पक्का होता है कि ऑडियो का स्ट्रक्चर सही हो और उसमें संगीत हो.

## Interactions API

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) के साथ Lyria 3.5 मॉडल इस्तेमाल किए जा सकते हैं. यह Gemini मॉडल और एजेंट के साथ इंटरैक्ट करने के लिए एक यूनिफ़ाइड इंटरफ़ेस है. यह मुश्किल मल्टीमोडल इस्तेमाल के उदाहरणों के लिए, स्टेट मैनेजमेंट और लंबे समय तक चलने वाले टास्क को आसान बनाता है.

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

### आराम का समय

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A melancholic jazz fusion track in D minor, featuring a smooth saxophone melody, walking bass line, and complex drum rhythms."
}'
```

## प्रॉम्प्ट से जुड़ी गाइड

संगीत की शैलियों, वाद्ययंत्रों, गाने के स्ट्रक्चर, पसंद के मुताबिक़ बोल, और वोकल डिलीवरी स्टाइल के लिए असरदार प्रॉम्प्ट तैयार करने का तरीक़ा जानने के लिए, [Lyria प्रॉम्प्ट गाइड](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=hi) देखें.

## सबसे सही तरीके

- **सबसे पहले क्लिप बनाएं.** `lyria-3.5` की मदद से पूरा वीडियो जनरेट करने से पहले, प्रॉम्प्ट के साथ एक्सपेरिमेंट करने के लिए, तेज़ `lyria-3-clip-preview` मॉडल का इस्तेमाल करें.
- **सटीक जानकारी दें.** अस्पष्ट प्रॉम्प्ट से सामान्य नतीजे मिलते हैं. बेहतरीन आउटपुट पाने के लिए, वाद्य यंत्रों, बीपीएम, की, मूड, और स्ट्रक्चर के बारे में बताएं.
- **आपकी भाषा से मेल खाती हो.** आपको जिस भाषा में गाने के बोल चाहिए उसमें प्रॉम्प्ट दें.
- **सेक्शन टैग का इस्तेमाल करें.** `[Verse]`, `[Chorus]`, `[Bridge]` टैग, मॉडल को
  एक साफ़ स्ट्रक्चर देते हैं, ताकि वह उसे फ़ॉलो कर सके.
- **गाने के बोलों को निर्देशों से अलग रखें.** अपनी पसंद के मुताबिक़ गाने के बोल देते समय, उन्हें संगीत से जुड़े निर्देशों से साफ़ तौर पर अलग करें.

## सीमाएं

- **सुरक्षा**: सभी प्रॉम्प्ट की जांच, सुरक्षा फ़िल्टर से की जाती है. फ़िल्टर ट्रिगर करने वाले प्रॉम्प्ट ब्लॉक कर दिए जाएँगे. इसमें ऐसे प्रॉम्प्ट शामिल हैं जिनमें किसी कलाकार की आवाज़ या कॉपीराइट वाले गाने के बोल जनरेट करने का अनुरोध किया गया हो.
- **वॉटरमार्क**: जनरेट किए गए सभी ऑडियो में, [SynthID ऑडियो वॉटरमार्क](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=hi) शामिल होता है, ताकि उनकी पहचान की जा सके. यह वॉटरमार्क लोगों को सुनाई नहीं देता और इससे संगीत सुनने के अनुभव पर कोई असर नहीं पड़ता.
- **एक से ज़्यादा बार बदलाव करने की सुविधा**: संगीत जनरेट करने की सुविधा, एक बार में ही काम करती है.
  Lyria 3.5 के मौजूदा वर्शन में, जनरेट की गई क्लिप में बार-बार बदलाव करने या कई प्रॉम्प्ट का इस्तेमाल करके उसे बेहतर बनाने की सुविधा उपलब्ध नहीं है.
- **अवधि**: Clip मॉडल हमेशा 30 सेकंड की क्लिप जनरेट करता है. Pro मॉडल, कुछ मिनटों की अवधि वाले गाने जनरेट करता है. गानों की सटीक अवधि, आपके प्रॉम्प्ट के हिसाब से तय हो सकती है.
- **डिटरमिनिज़्म**: एक ही प्रॉम्प्ट के लिए, अलग-अलग कॉल के नतीजे अलग-अलग हो सकते हैं.

## आगे क्या करना है

- Lyria 3.5 मॉडल की [कीमत](https://ai.google.dev/gemini-api/docs/pricing?hl=hi) देखें.
- Lyria RealTime की मदद से, [रीयल-टाइम में संगीत जनरेट करने और उसे स्ट्रीम करने](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi) की सुविधा आज़माएँ.
- [टीटीएस मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) की मदद से, एक से ज़्यादा स्पीकर वाली बातचीत जनरेट करें.
- [इमेज](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) या [वीडियो](https://ai.google.dev/gemini-api/docs/video?hl=hi) जनरेट करने का तरीक़ा जानें.
- जानें कि Gemini, [ऑडियो फ़ाइलों को कैसे समझ सकता है](https://ai.google.dev/gemini-api/docs/audio?hl=hi).
- [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi) का इस्तेमाल करके, Gemini के साथ रीयल-टाइम में बातचीत करें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-19 (UTC) को अपडेट किया गया."],[],[]]
