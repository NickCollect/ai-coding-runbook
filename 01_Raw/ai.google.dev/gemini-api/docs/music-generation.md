---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=vi
fetched_at: 2026-05-25T05:20:39.418651+00:00
title: "T\u1ea1o nh\u1ea1c b\u1eb1ng Lyria 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo nhạc bằng Lyria 3

Lyria 3 là nhóm mô hình tạo nhạc của Google, có sẵn thông qua Gemini API. Với Lyria 3, bạn có thể tạo âm thanh nổi chất lượng cao ở tần số 44, 1 kHz từ câu lệnh văn bản hoặc từ hình ảnh. Các mô hình này mang đến sự nhất quán về cấu trúc, bao gồm giọng hát, lời bài hát có dấu thời gian và bản phối nhạc cụ hoàn chỉnh.

Nhóm mô hình Lyria 3 bao gồm 2 mô hình:

| Mô hình | Mã kiểu máy | Phù hợp nhất cho | Thời lượng | Đầu ra |
| --- | --- | --- | --- | --- |
| **Đoạn video Lyria 3** | `lyria-3-clip-preview` | Đoạn video ngắn, video lặp lại, bản xem trước | 30 giây | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Bài hát có thời lượng đầy đủ với các đoạn, điệp khúc, cầu nối | Vài phút (có thể kiểm soát thông qua câu lệnh) | MP3 |

Bạn có thể sử dụng cả hai mô hình này bằng phương thức `generateContent` tiêu chuẩn và [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi) mới, hỗ trợ đầu vào đa phương thức (văn bản và hình ảnh) và tạo ra âm thanh **âm thanh nổi có độ trung thực cao 44,1 kHz**.

## Tạo đoạn nhạc

Mô hình Lyria 3 Clip luôn tạo một đoạn video dài **30 giây**. Để tạo một đoạn video, hãy gọi phương thức `generateContent` bằng một câu lệnh dạng văn bản. Phản hồi luôn bao gồm lời bài hát và cấu trúc bài hát được tạo cùng với âm thanh.

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

## Tạo bài hát có thời lượng đầy đủ

Sử dụng mô hình `lyria-3-pro-preview` để tạo các bài hát dài từ một đến hai phút. Mô hình Pro hiểu rõ cấu trúc âm nhạc và có thể tạo ra các bản nhạc có các đoạn, điệp khúc và cầu nối riêng biệt. Bạn có thể điều chỉnh thời lượng bằng cách chỉ định thời lượng trong câu lệnh (ví dụ: "tạo một bài hát dài 2 phút") hoặc bằng cách sử dụng [dấu thời gian](#timing) để xác định cấu trúc.

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

## Chọn định dạng đầu ra

Theo mặc định, các mô hình Lyria 3 tạo âm thanh ở định dạng **MP3**. Đối với Lyria 3 Pro, bạn cũng có thể yêu cầu đầu ra ở định dạng **WAV** bằng cách đặt `response_format` trong `generationConfig`.

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

## Phân tích cú pháp phản hồi

Phản hồi của Lyria 3 có nhiều phần. Các phần văn bản chứa lời bài hát được tạo hoặc nội dung mô tả bằng JSON về cấu trúc bài hát. Các phần có `inline_data` chứa các byte âm thanh.

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

## Tạo nhạc từ hình ảnh

Lyria 3 hỗ trợ dữ liệu đầu vào đa phương thức – bạn có thể cung cấp tối đa **10 hình ảnh** cùng với câu lệnh văn bản và mô hình sẽ sáng tác nhạc dựa trên nội dung trực quan.

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

## Cung cấp lời bài hát tuỳ chỉnh

Bạn có thể tự viết lời bài hát và đưa lời bài hát đó vào câu lệnh. Sử dụng các thẻ phần như `[Verse]`, `[Chorus]` và `[Bridge]` để giúp mô hình hiểu cấu trúc bài hát:

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

## Kiểm soát thời gian và cấu trúc

Bạn có thể chỉ định chính xác những gì xảy ra tại các thời điểm cụ thể trong bài hát bằng cách sử dụng dấu thời gian. Việc này rất hữu ích để kiểm soát thời điểm nhạc cụ bắt đầu, thời điểm lời bài hát được chuyển và cách bài hát tiến triển:

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

## Tạo bản nhạc không lời

Đối với nhạc nền, nhạc trò chơi hoặc bất kỳ trường hợp sử dụng nào không yêu cầu giọng hát, bạn có thể yêu cầu mô hình tạo ra các bản nhạc chỉ có nhạc cụ:

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

## Tạo nhạc bằng nhiều ngôn ngữ

Lyria 3 tạo lời bài hát bằng ngôn ngữ trong câu lệnh của bạn. Để tạo một bài hát có lời bằng tiếng Pháp, hãy viết câu lệnh bằng tiếng Pháp. Mô hình này điều chỉnh phong cách giọng nói và cách phát âm cho phù hợp với ngôn ngữ.

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

## Trí tuệ của mô hình

Lyria 3 phân tích quy trình tạo câu lệnh của bạn, trong đó mô hình suy luận thông qua cấu trúc âm nhạc (đoạn giới thiệu, đoạn thơ, điệp khúc, đoạn chuyển, v.v.) dựa trên câu lệnh của bạn.
Việc này diễn ra trước khi âm thanh được tạo và đảm bảo tính nhất quán về cấu trúc cũng như tính nhạc.

## Interactions API

Bạn có thể sử dụng các mô hình Lyria 3 với [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi) (API Tương tác);
đây là một giao diện hợp nhất để tương tác với các mô hình và tác nhân Gemini. Thư viện này đơn giản hoá việc quản lý trạng thái và các tác vụ chạy trong thời gian dài cho các trường hợp sử dụng phức tạp có nhiều phương thức.

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

## Hướng dẫn đặt câu lệnh

Câu lệnh của bạn có thể đơn giản như "một bài hát dân ca về những chú mèo dễ thương tránh vũng nước, giọng nữ và tiếng mưa", hoặc chi tiết và có cấu trúc như:

> Một bản nhạc synth-pop mang phong cách thập niên 1980 với nhịp điệu mạnh mẽ, tiếng đàn synthesizer vang vọng và một điệp khúc bắt tai, đầy cảm hứng. Bài hát phải mang hơi hướng hoài cổ pha lẫn hiện đại, gợi nhớ đến những bản nhạc pop kinh điển của thập niên 80, nhưng được sản xuất theo phong cách hiện đại. Nhịp độ phải sôi động và có thể nhảy theo, khoảng 120 BPM, có cấu trúc rõ ràng giữa đoạn thơ và điệp khúc, cùng một đoạn nhạc không lời bắt tai. Lời bài hát nói về cảm giác chuẩn bị cho một bữa tiệc.

Cả câu lệnh đơn giản và phức tạp đều có thể mang lại kết quả tốt. Bạn nên thử nghiệm những mẹo này để tìm ra cách phù hợp nhất với mình.

### Thể loại

Bắt đầu câu lệnh bằng thể loại nhạc bạn muốn, chẳng hạn như hip hop, rock và rap. Bạn có thể chỉ định nhiều thể loại:

- Sự kết hợp giữa metal và rap
- Kết hợp giữa death metal và opera
- Một bản nhạc cổ điển có các yếu tố âm thanh điện tử
- Nhạc dance điện tử (EDM) hiện đại kết hợp với nhạc Europop

Bạn cũng có thể kết hợp một kỷ nguyên:

- Nhạc hip-hop đầu thập niên 90
- Nhạc pop Pháp theo phong cách yé-yé thập niên 60
- Thử nghiệm với nhạc điện tử vào những năm 80
- Nhạc pop đại chúng thập niên 2000

Nếu bạn yêu cầu các thể loại hoặc biến thể theo khu vực cụ thể, chẳng hạn như "nhạc techno Berlin" hoặc "nhạc hyphy vùng Vịnh", mô hình sẽ cố gắng nắm bắt được bản chất đó, nhưng không phải lúc nào cũng chính xác.

### Nhạc cụ

Theo mặc định, Lyria 3 sẽ tạo các bài hát có nhạc cụ và công cụ mà bạn mong đợi cho thể loại đó. Bạn không cần phải đưa ra chỉ dẫn cụ thể.

Tuy nhiên, một bản nhạc dance sẽ không có kèn saxophone trừ phi bạn yêu cầu. Vì vậy, nếu muốn có một bản độc tấu saxophone, bạn cần phải yêu cầu Gemini tạo:

> Một bản nhạc dance với nhịp điệu mạnh mẽ, âm thanh điện tử lấp lánh và một điệp khúc bắt tai, đầy cảm hứng. Một đoạn solo saxophone sẽ xuất hiện trong phần chuyển tiếp.

Câu lệnh của bạn có thể bao gồm các nhạc cụ cụ thể, âm thanh của chúng và cách chúng tương tác với nhau. Bạn có thể sử dụng sự kết hợp này để tạo ra một số tâm trạng hoặc kết cấu nhất định:

- Một đường bassline méo mó, bẩn thỉu đối lập với tiếng hi-hat sạch sẽ, sắc nét
- Âm nền ấm áp của đàn synthesizer analog vang lên dưới tiếng đàn guitar mộc mạc, gần gũi
- Một bức tường âm thanh được tạo ra từ nhiều lớp guitar mờ, với giọng hát bị chôn vùi, xa xôi

### Cấu trúc bài hát

Bạn có thể phác thảo tiến trình của một bài hát trong câu lệnh. Sử dụng mũi tên hoặc danh sách để xác định quy trình:

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- Bắt đầu bằng đoạn nhạc piano nhẹ nhàng, chuyển sang một đoạn nhạc mạnh mẽ, rồi đột ngột im lặng, sau đó bùng nổ vào đoạn điệp khúc.

Bạn cũng có thể chỉ định cách mức năng lượng thay đổi giữa các phần này:

- Tạo cao trào ở đoạn tiền điệp khúc, sau đó giảm âm lượng xuống mức im lặng trước khi điệp khúc bùng nổ
- Tăng dần âm lượng trong suốt bài hát, thêm từng nhạc cụ một cho đến khi tạo ra một bức tường âm thanh hỗn loạn
- Ngừng đột ngột sau đoạn chuyển, tiếp theo là một đoạn điệp khúc hát chay

Bạn cũng có thể đưa ra câu lệnh về thời điểm chính xác mà bạn muốn một việc gì đó xảy ra:

- Tạo hiệu ứng tăng dần đến đoạn thả ở giây thứ 12
- Có người nói "gì" mỗi 2 giây
- Đoạn điệp khúc bắt đầu ở giây thứ 22

### Lời nhạc

Giọng hát và lời bài hát được tạo theo mặc định. Bạn có thể cung cấp lời bài hát của riêng mình, yêu cầu không có lời bài hát (hoặc chỉ có nhạc không lời) hoặc định hướng việc tạo lời bài hát theo hướng bạn muốn.

Lời bài hát sẽ bằng ngôn ngữ mà bạn viết câu lệnh. Bạn cũng có thể yêu cầu viết lời bài hát bằng một ngôn ngữ khác, chẳng hạn như "Viết lời bài hát bằng tiếng Pháp".

#### Sử dụng lời bài hát của riêng bạn

Để cung cấp lời bài hát của riêng bạn cho mô hình, hãy thêm lời bài hát vào câu lệnh bằng tiền tố "Lời bài hát:":

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

Bạn có thể thêm tiêu đề phần vào đầu các phần của bài hát, chẳng hạn như `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]` và `[Outro]`.

Nếu muốn một từ hoặc dòng được lặp lại, chẳng hạn như tiếng vọng hoặc giọng hát bè, bạn có thể đặt từ hoặc dòng đó trong dấu ngoặc đơn: "Let's go (go)".

#### Đưa ra câu lệnh để mô hình viết lời bài hát

Nếu muốn Lyria 3 viết lời bài hát cho bạn, tốt nhất là bạn nên đưa thông tin chi tiết về nội dung của lời bài hát vào câu lệnh. Nếu không, mô hình sẽ cần suy luận một chủ đề từ câu lệnh về nhạc của bạn và chủ đề đó có thể không phải là chủ đề bạn muốn.

> Lời bài hát nói về tình yêu đã mất và nỗi đau của sự thất tình. Bài hát này là nỗi hoài niệm của một ca sĩ về mối quan hệ trong quá khứ và những kỷ niệm ùa về.

Nếu bạn muốn có một điệp khúc lặp lại, hãy yêu cầu trong câu lệnh:

> Lời bài hát nói về tình yêu đã mất và nỗi đau của sự thất tình. Bài hát này là nỗi hoài niệm của một ca sĩ về mối tình đã qua và những kỷ niệm ùa về. Điệp khúc mạnh mẽ tập trung vào việc vượt qua nỗi đau và tiếp tục bước tiếp.

Lyria 3 sẽ tự động điều chỉnh cấu trúc của lời bài hát theo loại nhạc mà bạn yêu cầu, nhưng bạn cũng có thể nhấn mạnh lại điều này trong câu lệnh. Ví dụ:

> Một bản nhạc EDM lặp đi lặp lại cùng một cụm từ tràn đầy năng lượng.

Bạn cũng có thể yêu cầu các hiệu ứng giọng hát không phải là lời bài hát, chẳng hạn như:

- Một đoạn nhạc mẫu lặp lại trong một bộ phim có câu "Tôi không thể tin được!" xuyên suốt bài hát
- Một bản nhạc techno tràn đầy năng lượng, ngay trước khi nhạc giảm âm lượng, âm thanh dừng lại và một giọng nói nhỏ vang lên "Tôi không biết mình đang làm gì ở đây", sau đó nhạc giảm âm lượng.
- Bài hát bắt đầu bằng một cuộc trò chuyện về việc các bộ phim trong thập niên 90 hay hơn ngày nay. Sau đó, bài hát chuyển sang một bài hát pop.

### Vocals

Bạn có thể đưa ra câu lệnh về cách bạn muốn lời bài hát được cung cấp. Để có kết quả tốt nhất, hãy chỉ định một hồ sơ chi tiết về ca sĩ, bao gồm giới tính, âm sắc và quãng giọng.

- **Nữ cao**: Âm sắc trong trẻo, tinh khiết, linh hoạt và cao vút. Có khả năng hát những nốt cao bằng giọng huýt sáo với chất giọng thoáng, có hơi.
- **Nữ trung**: Giọng trầm ấm, dày và khàn. Giọng khàn khàn, có chút giọng chiên trứng, đầy cảm xúc và vang vọng.
- **Nam cao**: Tươi sáng, mạnh mẽ và tràn đầy năng lượng. Âm sắc trẻ trung, hơi khàn, nổi bật trong bản phối với giọng hát cao đầy nội lực.
- **Nam trung**: Trầm, ngọt ngào và mượt mà như nhung. Giọng ngực vang vọng, êm dịu và du dương.
- **Weathered Rocker (Nam)**: Giọng khàn và gai góc với âm sắc thô ráp, gợi nhớ đến nhạc grunge của thập niên 90. Phạm vi trên bị căng cho cường độ cảm xúc.

### Các tham số khác của câu lệnh

Bạn cũng có thể thêm các tham số này để tinh chỉnh câu lệnh hơn nữa:

- **Khoá/Gam**: Nêu rõ một khoá nhạc (ví dụ: "in G major", "D minor").
- **Tâm trạng và bầu không khí**: Sử dụng tính từ mô tả (ví dụ: "hoài niệm", "mạnh mẽ", "siêu thực", "mơ màng").
- **Thời lượng**: Mô hình Đoạn trích luôn tạo ra các đoạn trích dài 30 giây. Đối với mô hình Pro, hãy chỉ định độ dài mong muốn trong câu lệnh (ví dụ: "tạo một bài hát dài 2 phút") hoặc dùng dấu thời gian để kiểm soát thời lượng.

### Câu lệnh mẫu

Sau đây là một số ví dụ về câu lệnh hiệu quả:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Các phương pháp hay nhất

- **Lặp lại với Đoạn video trước.** Sử dụng mô hình `lyria-3-clip-preview` nhanh hơn để thử nghiệm các câu lệnh trước khi tạo một hình ảnh dài bằng `lyria-3-pro-preview`.
- **Mô tả cụ thể.** Câu lệnh mơ hồ sẽ tạo ra kết quả chung chung. Đề cập đến nhạc cụ, số nhịp/phút, khoá nhạc, tâm trạng và cấu trúc để có kết quả tốt nhất.
- **Sử dụng thẻ phần.** Thẻ `[Verse]`, `[Chorus]`, `[Bridge]` giúp mô hình có cấu trúc rõ ràng để tuân theo.
- **Tách lời bài hát khỏi hướng dẫn.** Khi cung cấp lời bài hát tuỳ chỉnh, hãy tách biệt rõ ràng lời bài hát đó với hướng dẫn về chỉ dẫn âm nhạc.

## Các điểm hạn chế

- **An toàn**: Tất cả câu lệnh đều được bộ lọc an toàn kiểm tra. Những câu lệnh kích hoạt bộ lọc sẽ bị chặn. Quy định này áp dụng cho cả những câu lệnh yêu cầu giọng nói của một nghệ sĩ cụ thể hoặc việc tạo ra lời bài hát có bản quyền.
- **Tạo hình mờ**: Tất cả âm thanh được tạo đều có [thuỷ vân âm thanh SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=vi) để nhận dạng. Hình mờ này không thể nhận thấy bằng tai thường và không ảnh hưởng đến trải nghiệm nghe.
- **Chỉnh sửa nhiều lượt**: Tính năng tạo nhạc là một quy trình một lượt.
  Phiên bản Lyria 3 hiện tại không được hỗ trợ việc chỉnh sửa lặp đi lặp lại hoặc tinh chỉnh một đoạn video được tạo thông qua nhiều câu lệnh.
- **Độ dài**: Mô hình Đoạn video luôn tạo ra các đoạn video dài 30 giây. Mô hình Pro tạo ra các bài hát có thời lượng vài phút; thời lượng chính xác có thể bị ảnh hưởng thông qua câu lệnh của bạn.
- **Tính xác định**: Kết quả có thể khác nhau giữa các lệnh gọi, ngay cả khi dùng cùng một câu lệnh.

## Bước tiếp theo

- Kiểm tra [giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) của các mô hình Lyria 3,
- Thử [tạo nhạc trực tuyến theo thời gian thực](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=vi) bằng Lyria RealTime,
- Tạo các cuộc trò chuyện có nhiều người nói bằng [các mô hình TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=vi),
- Khám phá cách tạo [hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) hoặc [video](https://ai.google.dev/gemini-api/docs/video?hl=vi),
- Tìm hiểu cách Gemini có thể [hiểu tệp âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi),
- Trò chuyện theo thời gian thực với Gemini bằng [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-13 UTC."],[],[]]
