---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=ko
fetched_at: 2026-09-14T05:36:55.571999+00:00
title: "Lyria 3.5\ub85c \uc74c\uc545 \uc0dd\uc131\ud558\uae30 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# Lyria 3.5로 음악 생성하기

Lyria 3.5는 Gemini API를 통해 사용할 수 있는 Google의 음악 생성 모델 제품군입니다. Lyria 3.5를 사용하면 텍스트 프롬프트 또는 이미지에서 고품질의 44.1kHz 스테레오 오디오를 생성할 수 있습니다. 이러한 모델은 보컬, 시간 지정 가사, 전체 악기 편곡 등 구조적 일관성을 제공합니다.

Lyria 제품군에는 다음 모델이 포함됩니다.

| 모델 | 모델 ID | 권장 용도 | 기간 | 출력 |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | 짧은 클립, 연속 재생, 프리뷰 | 30초 | MP3 |
| **Lyria 3.5** | `lyria-3.5` | 절, 후렴, 브리지가 있는 전체 길이 노래 | 몇 분 (프롬프트를 사용하여 제어 가능) | MP3 |

두 모델 모두 새로운 [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)를 사용하여 멀티모달 입력 (텍스트 및 이미지)을 지원하고 **44.1kHz 고음질 스테레오** 오디오를 생성할 수 있습니다.

## 음악 클립 생성

Lyria 3 Clip 모델은 항상 **30초** 길이의 클립을 생성합니다. 클립을 생성하려면 텍스트 프롬프트와 함께 `interactions.create` 메서드를 호출합니다. 대답에는 항상 생성된 가사와 노래 구조가 `steps` 스키마의 오디오와 함께 포함됩니다.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

마지막으로 생성된 오디오 블록을 반환하는 `interaction.output_audio` 속성을 사용하여 생성된 음악 데이터를 가져올 수 있습니다. `interaction.output_text` 속성을 사용하여 노래의 가사와 구조를 가져올 수도 있습니다. 편의 속성에 관한 자세한 내용은 [상호작용 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko#convenience-properties)를 참고하세요.

## 전체 길이 노래 생성

`lyria-3.5` 모델을 사용하여 몇 분 길이의 전체 노래를 생성합니다. Pro 모델은 음악 구조를 이해하고 뚜렷한 절, 후렴, 브릿지가 있는 곡을 만들 수 있습니다. 프롬프트에 지정하거나('2분 길이의 노래 만들기' 등) [타임스탬프](#timing)를 사용하여 구조를 정의하여 길이에 영향을 줄 수 있습니다.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody."
}'
```

## 출력 형식 선택

기본적으로 Lyria 3.5 모델은 **MP3** 형식으로 오디오를 생성합니다. Lyria 3.5의 경우 `response_format`를 설정하여 **WAV** 형식으로 출력을 요청할 수도 있습니다.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## 응답 파싱

Lyria 3.5의 대답에는 `steps` 스키마 내에 여러 콘텐츠 블록이 포함되어 있습니다.
상호작용은 단계 시퀀스를 반환하며, 여기서 `model_output` 단계에는 생성된 콘텐츠가 포함됩니다.
텍스트 콘텐츠 블록에는 생성된 가사 또는 노래 구조의 JSON 설명이 포함됩니다.
`audio` 유형의 콘텐츠 블록에는 base64로 인코딩된 오디오 데이터가 포함됩니다.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### 자바스크립트

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### 가사와 음악이 번갈아 표시됨

Lyria 3.5의 출력은 생성된 가사 (텍스트)와 노래 자체 (오디오)를 위한 별도의 단계와 블록을 포함하는 등 복잡하므로 편의 속성은 빠르고 권장되는 바로가기를 제공합니다.

하지만 서버에서 반환된 단계의 원시 타임라인을 프로그래매틱 방식으로 완전히 제어하려면 (예: 수신된 개별 콘텐츠 블록을 로깅) 대신 `steps`를 수동으로 반복하면 됩니다.

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### 자바스크립트

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

## 이미지에서 음악 생성

Lyria 3.5는 멀티모달 입력을 지원합니다. `input` 목록에 텍스트 프롬프트와 함께 최대 **10개의 이미지**를 제공하면 모델이 시각적 콘텐츠에서 영감을 받은 음악을 작곡합니다.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3.5",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### 자바스크립트

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3.5",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3.5",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## 맞춤 가사 제공

직접 가사를 작성하여 프롬프트에 포함할 수 있습니다. `[Verse]`, `[Chorus]`, `[Bridge]`와 같은 섹션 태그를 사용하여 모델이 노래 구조를 이해하도록 돕습니다.

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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### 자바스크립트

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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## 타이밍 및 구조 제어

타임스탬프를 사용하면 노래의 특정 순간에 정확히 어떤 일이 일어나는지 지정할 수 있습니다. 이는 악기가 언제 시작되고, 가사가 언제 전달되고, 노래가 어떻게 진행되는지 제어하는 데 유용합니다.

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

interaction = client.interactions.create(
    model="lyria-3.5",
    input=prompt,
)
```

### 자바스크립트

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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## 연주곡 트랙 생성

배경 음악, 게임 사운드트랙 또는 보컬이 필요하지 않은 사용 사례의 경우 모델에 연주곡 전용 트랙을 생성하도록 프롬프트를 지정할 수 있습니다.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## 다양한 언어로 음악 생성

Lyria 3.5는 프롬프트의 언어로 가사를 생성합니다. 프랑스어 가사가 포함된 노래를 생성하려면 프롬프트를 프랑스어로 작성하세요. 모델이 언어에 맞게 음성 스타일과 발음을 조정합니다.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### 자바

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseModality;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("lyria-3-generate-001"))
        .responseModalities(Arrays.asList(ResponseModality.AUDIO))
        .input(InteractionsInput.of("Upbeat electronic synthwave track"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println("Audio generated: " + interaction.outputAudio().isPresent());
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3.5",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## 모델 인텔리전스

Lyria 3.5는 프롬프트에 따라 모델이 음악 구조 (인트로, 절, 코러스, 브리지 등)를 통해 추론하는 프롬프트 프로세스를 분석합니다.
이는 오디오가 생성되기 전에 발생하며 구조적 일관성과 음악성을 보장합니다.

## 프롬프트 가이드

프롬프트는 '귀여운 고양이가 물웅덩이를 피하는 포크송, 여성 보컬, 빗소리'와 같이 간단할 수도 있고 다음과 같이 상세하고 구조적일 수도 있습니다.

> 강렬한 비트, 반짝이는 신시사이저, 중독성 있는 앤섬 스타일의 코러스가 특징인 1980년대 스타일의 신스팝 트랙입니다. 이 노래는 80년대 클래식 팝 히트곡을 연상시키는 레트로 퓨처리즘 느낌을 주면서도 현대적인 세련됨을 갖춰야 합니다. 템포는 120BPM 정도의 신나고 춤추기 좋은 템포여야 하며, 명확한 절-후렴 구조와 기억에 남는 연주곡 후크가 있어야 합니다. 가사는 파티를 준비하는 기분에 관한 내용입니다.

간단한 프롬프트와 복잡한 프롬프트 모두 좋은 출력을 제공할 수 있습니다. 이 도움말을 참고하여 자신에게 가장 적합한 방법을 찾아보세요.

### 장르

프롬프트의 시작 부분에 원하는 음악 장르(예: 힙합, 록, 랩)를 입력합니다. 다음과 같이 여러 장르를 지정할 수 있습니다.

- 메탈과 랩의 융합
- 데스 메탈과 오페라의 조합
- 전자 드론 요소가 포함된 클래식 곡
- 유로팝과 혼합된 현대적인 일렉트로닉 댄스 음악 (EDM)

연대를 포함할 수도 있습니다.

- 1990년대 초반 힙합
- 60년대 프랑스 예예 팝
- 80년대 전자 음악 실험
- 2000년대 메인스트림 팝

'베를린 테크노' 또는 '베이 지역 하이피'와 같은 맞춤 장르나 지역 변형을 요청하면 모델이 해당 특징을 포착하려고 시도하지만 항상 올바르게 파악하지는 못할 수 있습니다.

### 악기

기본적으로 Lyria 3.5는 장르에 적합한 악기와 도구로 노래를 만듭니다. 명령형일 필요는 없습니다.

하지만 색소폰을 요청하지 않는 한 댄스 트랙에 색소폰이 포함되지는 않습니다. 색소폰 솔로를 원한다면 다음과 같이 프롬프트를 입력해야 합니다.

> 강렬한 비트, 반짝이는 신시사이저, 중독성 있는 앤섬 스타일의 코러스가 특징인 댄스 트랙입니다. 브리지 중에 색소폰 솔로가 나와야 합니다.

프롬프트에는 특정 악기, 악기 소리, 악기 간의 상호작용 방식이 포함될 수 있습니다. 이 조합을 사용하여 특정 분위기나 질감을 만들 수 있습니다.

- 더럽고 왜곡된 베이스 라인이 깨끗하고 선명한 하이햇과 대립합니다.
- 따뜻한 아날로그 신시사이저 패드가 건조하고 친밀한 어쿠스틱 기타 아래에서 부풀어 오름
- 여러 레이어의 퍼지 기타로 만들어진 사운드 벽, 묻혀 있는 듯한 먼 보컬

### 노래 구조

프롬프트에서 노래의 진행을 간략하게 설명할 수 있습니다. 화살표나 목록을 사용하여 흐름을 정의합니다.

- `[Intro]` -> `[Verse 1]` -> `[Chorus]` -> `[Verse 2]` -> `[Chorus]` ->
  `[Bridge]` -> `[Outro]`
- 조용한 피아노 인트로로 시작하여, 시끄러운 벌스로 이어지고, 침묵으로 떨어졌다가, 코러스로 폭발합니다.

이러한 섹션 간에 에너지 수준이 어떻게 변하는지 지정할 수도 있습니다.

- 프리코러스에서 긴장감을 조성한 다음, 대규모의 폭발적인 코러스 전에 조용히 떨어뜨립니다.
- 노래 전체에 걸쳐 점진적으로 크레센도, 혼란스러운 사운드 벽이 될 때까지 한 번에 하나의 악기를 추가
- 브리지 후 갑자기 멈추고 아카펠라 코러스가 이어짐

특정 작업을 실행할 정확한 시간을 지정할 수도 있습니다.

- 12초에 드롭이 발생하도록 빌드
- 2초마다 누군가 '뭐'라고 말함
- 22초에 후렴구가 시작됩니다.

### 가사

보컬과 가사는 기본적으로 생성됩니다. 직접 가사를 제공하거나, 가사 (또는 연주곡)를 요청하지 않거나, 원하는 방향으로 가사 생성을 유도할 수 있습니다.

가사는 프롬프트를 작성한 언어로 표시됩니다. '프랑스어로 가사를 써 줘'와 같이 다른 언어로 가사를 써 달라고 요청할 수도 있습니다.

#### 자체 가사 사용

모델에 자체 가사를 제공하려면 '가사:' 접두사와 함께 프롬프트에 포함하세요.

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

노래의 일부에 `[Intro]`, `[Verse 1]`, `[Pre-chorus]`, `[Chorus]`, `[Outro]`과 같은 섹션 제목을 접두사로 붙일 수 있습니다.

단어나 줄이 반복되도록 하려면(예: 에코 또는 백킹 보컬) 괄호 안에 포함하면 됩니다('Let's go (go)').

#### 모델에 가사 작성 요청

Lyria 3.5가 가사를 만들어 주길 바란다면 프롬프트에 가사의 내용을 자세히 포함하는 것이 좋습니다. 그렇지 않으면 모델이 음악 프롬프트에서 주제를 추론해야 하며 원하는 결과가 아닐 수 있습니다.

> 가사는 잃어버린 사랑과 실연의 고통에 관한 내용입니다. 가수는 과거의 관계와 밀려드는 추억을 회상합니다.

반복되는 후렴구를 원한다면 프롬프트에서 요청하는 것이 좋습니다.

> 가사는 잃어버린 사랑과 실연의 고통에 관한 내용입니다. 가수는 과거의 관계와 밀려드는 추억을 회상합니다. 강렬한 후렴구는 고통을 극복하고 앞으로 나아가는 데 초점을 맞춥니다.

Lyria 3.5는 요청한 음악 유형에 맞게 가사의 구조를 자동으로 조정하지만 프롬프트에서 이를 다시 강조할 수도 있습니다. 예를 들면 다음과 같습니다.

> 동일한 활기찬 문구를 계속 반복하는 EDM 트랙

엄밀히 말해 가사가 아닌 보컬 효과를 요청할 수도 있습니다. 예를 들면 다음과 같습니다.

- 영화의 반복되는 샘플이 노래 전체에 걸쳐 '믿을 수 없어!'라고 말합니다.
- 드롭 직전에 에너지가 넘치는 테크노 트랙이 재생되다가 갑자기 소리가 멈추고 작은 목소리로 '여기서 뭘 해야 할지 모르겠어'라고 말한 후 음악이 드롭됩니다.
- 이 트랙은 90년대 영화가 요즘 영화보다 낫다는 대화로 시작됩니다. 그런 다음 트랙이 팝송으로 전환됩니다.

### 보컬

가사를 어떤 방식으로 전달할지 묻는 메시지를 표시할 수 있습니다. 최상의 결과를 얻으려면 성별, 음색, 보컬 범위가 포함된 자세한 가수 프로필을 지정하세요.

- **여성 소프라노**: 민첩하고 솟아오르는 듯한 음질을 가진 선명하고 수정 같은 음색 공기처럼 가볍고 숨소리가 섞인 질감으로 휘파람 같은 고음을 낼 수 있습니다.
- **여성 알토**: 풍부하고 따뜻하며 허스키한 낮은 음역대 보컬 프라이가 가미된 스모키한 음색으로, 소울풀하고 공명합니다.
- **남성 테너**: 밝고, 날카롭고, 활기찬 느낌입니다. 약간의 비음이 있는 젊은 음색으로, 높은 벨팅 파워로 믹스를 뚫고 나옵니다.
- **남성 바리톤**: 깊고 초콜릿처럼 부드러운 음색입니다. 부드러운 크루닝 전달로 공명하는 가슴 소리
- **노련한 록커 (남성)**: 90년대 그런지를 연상시키는 거친 질감과 자갈 같은 음색이 특징입니다. 감정 강도의 상한이 과장되었습니다.

### 기타 프롬프트 매개변수

다음 매개변수를 포함하여 프롬프트를 추가로 세부 조정할 수도 있습니다.

- **BPM**: 템포를 설정합니다 (예: '120BPM', '70BPM 정도의 느린 템포').
- **조/스케일**: 음악적 조 (예: 'G장조', 'D단조')를 지정합니다.
- **분위기**: 설명하는 형용사 (예: '향수', '공격적', '몽환적', '꿈결 같은')를 사용합니다.
- **길이**: 클립 모델은 항상 30초 길이의 클립을 생성합니다. Pro 모델의 경우 프롬프트에서 원하는 길이를 지정하거나('2분 길이의 노래 만들기' 등) 타임스탬프를 사용하여 길이를 제어합니다.

### 프롬프트 예시

효과적인 프롬프트의 예는 다음과 같습니다.

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## 권장사항

- **먼저 클립으로 반복하세요.** 더 빠른 `lyria-3-clip-preview` 모델을 사용하여 `lyria-3.5`로 전체 길이 생성을 커밋하기 전에 프롬프트를 실험하세요.
- **자세히 설명합니다.** 모호한 프롬프트는 일반적인 결과를 생성합니다. 최상의 결과를 얻기 위해 악기, BPM, 키, 분위기, 구조를 언급합니다.
- **언어를 일치시킵니다.** 가사를 원하는 언어로 프롬프트를 입력합니다.
- **섹션 태그를 사용합니다.** `[Verse]`, `[Chorus]`, `[Bridge]` 태그는 모델이 따라야 할 명확한 구조를 제공합니다.
- **가사와 안내를 구분하세요.** 맞춤 가사를 제공할 때는 음악적 방향 지침과 명확하게 구분하세요.

## 제한사항

- **안전**: 모든 프롬프트는 안전 필터로 확인됩니다. 필터를 트리거하는 프롬프트는 차단됩니다. 여기에는 특정 아티스트의 음성을 요청하거나 저작권이 있는 가사를 생성하도록 요청하는 프롬프트가 포함됩니다.
- **워터마크**: 생성된 모든 오디오에는 식별을 위한 [SynthID 오디오 워터마크](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=ko)가 포함됩니다. 이 워터마크는 사람의 귀에 들리지 않으며 청취 환경에 영향을 주지 않습니다.
- **멀티턴 편집**: 음악 생성은 단일 턴 프로세스입니다.
  현재 버전의 Lyria 3.5에서는 여러 프롬프트를 통해 생성된 클립을 반복적으로 수정하거나 다듬는 것이 지원되지 않습니다.
- **길이**: 클립 모델은 항상 30초 길이의 클립을 생성합니다. Pro 모델은 몇 분 길이의 노래를 생성합니다. 정확한 길이는 프롬프트에 따라 달라질 수 있습니다.
- **결정성**: 동일한 프롬프트로 호출하더라도 호출 간에 결과가 다를 수 있습니다.

## 다음 단계

- Lyria 3.5 모델의 [가격](https://ai.google.dev/gemini-api/docs/pricing?hl=ko)을 확인하세요.
- Lyria RealTime으로 [실시간 스트리밍 음악 생성](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=ko)을 사용해 보세요.
- [TTS 모델](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ko)을 사용하여 여러 화자가 포함된 대화를 생성합니다.
- [이미지](https://ai.google.dev/gemini-api/docs/image-generation?hl=ko) 또는 [동영상](https://ai.google.dev/gemini-api/docs/video?hl=ko)을 생성하는 방법을 알아보세요.
- Gemini가 [오디오 파일을 이해](https://ai.google.dev/gemini-api/docs/audio?hl=ko)하는 방법을 알아보세요.
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ko)를 사용하여 Gemini와 실시간으로 대화합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-10(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-10(UTC)"],[],[]]
