---
source_url: https://ai.google.dev/gemini-api/docs/interactions?hl=ko
fetched_at: 2026-05-05T13:28:44.719590+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

- [홈](https://ai.google.dev/gemini-api/docs/홈)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [문서](https://ai.google.dev/gemini-api/docs/문서)

의견 보내기

# Interactions API

Interactions API ([베타](https://ai.google.dev/gemini-api/docs/베타))는 Gemini 모델 및 에이전트와 상호작용하기 위한 통합 인터페이스입니다. [`generateContent`](https://ai.google.dev/gemini-api/docs/`generateContent`) API의 개선된 대안으로 상태 관리, 도구 조정, 장기 실행 작업을 간소화합니다. API 스키마의 전체적인 내용은 [API 참조](https://ai.google.dev/gemini-api/docs/API 참조)를 확인하세요. 베타 기간에는 기능과 스키마에 [브레이킹 체인지](https://ai.google.dev/gemini-api/docs/브레이킹 체인지)가 적용될 수 있습니다.
빠르게 시작하려면 [상호작용 API 빠른 시작 노트북](https://ai.google.dev/gemini-api/docs/상호작용 API 빠른 시작 노트북)을 사용해 보세요.

일반 사용
함수 호출
Deep Research 에이전트

다음 예에서는 텍스트 프롬프트로 Interactions API를 호출하는 방법을 보여줍니다.

### Python

```
from google import genai

client = genai.Client()

interaction =  client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction =  await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a short joke about programming.',
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a short joke about programming."
}'
```

## 기본 상호작용

Interactions API는 [기존 SDK](https://ai.google.dev/gemini-api/docs/기존 SDK)를 통해 사용할 수 있습니다. 모델과 상호작용하는 가장 간단한 방법은 텍스트 프롬프트를 제공하는 것입니다. `input`는 문자열, 콘텐츠 객체를 포함하는 목록 또는 역할과 콘텐츠 객체가 있는 턴 목록일 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

interaction =  client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction =  await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a short joke about programming.',
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a short joke about programming."
}'
```

## 대화

멀티턴 대화는 다음 두 가지 방법으로 빌드할 수 있습니다.

- 이전 상호작용을 참조하여 상태를 유지
- 전체 대화 기록을 제공하여 스테이트리스 방식으로

### 상태 저장 대화

대화를 계속하려면 이전 상호작용의 `id`를 `previous_interaction_id` 매개변수에 전달합니다. API는 대화 기록을 기억하므로 새 입력만 보내면 됩니다. 상속되는 필드와 다시 지정해야 하는 필드에 관한 자세한 내용은 [서버 측 상태 관리](https://ai.google.dev/gemini-api/docs/서버 측 상태 관리)를 참고하세요.

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hi, my name is Phil."
)
print(f"Model: {interaction1.outputs[-1].text}")

# 2. Second turn (passing previous_interaction_id)
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is my name?",
    previous_interaction_id=interaction1.id
)
print(f"Model: {interaction2.outputs[-1].text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. First turn
const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Hi, my name is Phil.'
});
console.log(`Model: ${interaction1.outputs[interaction1.outputs.length - 1].text}`);

// 2. Second turn (passing previous_interaction_id)
const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is my name?',
    previous_interaction_id: interaction1.id
});
console.log(`Model: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
```

### REST

```
# 1. First turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Hi, my name is Phil."
}'

# 2. Second turn (Replace INTERACTION_ID with the ID from the previous interaction)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "input": "What is my name?",
#     "previous_interaction_id": "INTERACTION_ID"
# }'
```

#### 이전 스테이트풀 상호작용 가져오기

상호작용 `id`을 사용하여 이전 대화 턴을 가져옵니다.

### Python

```
previous_interaction = client.interactions.get("<YOUR_INTERACTION_ID>")

print(previous_interaction)
```

### 자바스크립트

```
const previous_interaction = await client.interactions.get("<YOUR_INTERACTION_ID>");
console.log(previous_interaction);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/<YOUR_INTERACTION_ID>" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

#### 원본 입력 포함

기본적으로 `interactions.get()`는 모델의 출력만 반환합니다. 응답에 원래 정규화된 입력을 포함하려면 `include_input`를 `true`로 설정합니다.

### Python

```
interaction = client.interactions.get(
    "<YOUR_INTERACTION_ID>",
    include_input=True
)

print(f"Input: {interaction.input}")
print(f"Output: {interaction.outputs}")
```

### 자바스크립트

```
const interaction = await client.interactions.get(
    "<YOUR_INTERACTION_ID>",
    { include_input: true }
);

console.log(`Input: ${JSON.stringify(interaction.input)}`);
console.log(`Output: ${JSON.stringify(interaction.outputs)}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/<YOUR_INTERACTION_ID>?include_input=true" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

### 스테이트리스(Stateless) 대화

클라이언트 측에서 대화 기록을 수동으로 관리할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

conversation_history = [
    {
        "role": "user",
        "content": "What are the three largest cities in Spain?"
    }
]

interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input=conversation_history
)

print(f"Model: {interaction1.outputs[-1].text}")

conversation_history.append({"role": "model", "content": interaction1.outputs})
conversation_history.append({
    "role": "user",
    "content": "What is the most famous landmark in the second one?"
})

interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input=conversation_history
)

print(f"Model: {interaction2.outputs[-1].text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const conversationHistory = [
    {
        role: 'user',
        content: "What are the three largest cities in Spain?"
    }
];

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: conversationHistory
});

console.log(`Model: ${interaction1.outputs[interaction1.outputs.length - 1].text}`);

conversationHistory.push({ role: 'model', content: interaction1.outputs });
conversationHistory.push({
    role: 'user',
    content: "What is the most famous landmark in the second one?"
});

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: conversationHistory
});

console.log(`Model: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
```

### REST

```
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
 -H "Content-Type: application/json" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {
            "role": "user",
            "content": "What are the three largest cities in Spain?"
        },
        {
            "role": "model",
            "content": "The three largest cities in Spain are Madrid, Barcelona, and Valencia."
        },
        {
            "role": "user",
            "content": "What is the most famous landmark in the second one?"
        }
    ]
}'
```

## 멀티모달 기능

이미지 이해 또는 동영상 생성과 같은 멀티모달 사용 사례에 Interactions API를 사용할 수 있습니다.

### 멀티모달 이해

base64로 인코딩된 데이터를 인라인으로 제공하거나, 더 큰 파일의 경우 Files API를 사용하거나, URI 필드에 공개적으로 액세스 가능한 링크를 전달하여 멀티모달 입력을 제공할 수 있습니다. 다음 코드 샘플은 공개 URL 메서드를 보여줍니다.

#### 이미지 이해

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "Describe the image."},
        {
            "type": "image",
            "uri": "YOUR_URL",
            "mime_type": "image/png"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import {GoogleGenAI} from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        {type: 'text', text: 'Describe the image.'},
        {
            type: 'image',
            uri: 'YOUR_URL',
            mime_type: 'image/png'
        }
    ]
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
    {
        "type": "text",
        "text": "Describe the image."
    },
    {
        "type": "image",
        "uri": "YOUR_URL",
        "mime_type": "image/png"
    }
    ]
}'
```

#### 오디오 이해

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What does this audio say?"},
        {
            "type": "audio",
            "uri": "YOUR_URL",
            "mime_type": "audio/wav"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What does this audio say?' },
        {
            type: 'audio',
            uri: 'YOUR_URL',
            mime_type: 'audio/wav'
        }
    ]
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What does this audio say?"},
        {
            "type": "audio",
            "uri": "YOUR_URL",
            "mime_type": "audio/wav"
        }
    ]
}'
```

#### 동영상 이해

### Python

```
from google import genai
client = genai.Client()

print("Analyzing video...")
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is happening in this video? Provide a timestamped summary."},
        {
            "type": "video",
            "uri": "YOUR_URL",
            "mime_type": "video/mp4"
        }
    ]
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

console.log('Analyzing video...');
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What is happening in this video? Provide a timestamped summary.' },
        {
            type: 'video',
            uri: 'YOUR_URL',
            mime_type: 'video/mp4'
        }
    ]
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What is happening in this video?"},
        {
            "type": "video",
            "uri": "YOUR_URL",
            "mime_type": "video/mp4"
        }
    ]
}'
```

#### 문서 (PDF) 이해

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "YOUR_URL",
            "mime_type": "application/pdf"
        }
    ]
)
print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'text', text: 'What is this document about?' },
        {
            type: 'document',
            uri: 'YOUR_URL',
            mime_type: 'application/pdf'
        }
    ],
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "text", "text": "What is this document about?"},
        {
            "type": "document",
            "uri": "YOUR_URL",
            "mime_type": "application/pdf"
        }
    ]
}'
```

### 멀티모달 생성

Interactions API를 사용하여 멀티모달 출력을 생성할 수 있습니다.

#### 이미지 생성

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an image of a futuristic city.",
    response_modalities=["image"]
)

for output in interaction.outputs:
    if output.type == "image":
        print(f"Generated image with mime_type: {output.mime_type}")
        # Save the image
        with open("generated_city.png", "wb") as f:
            f.write(base64.b64decode(output.data))
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-pro-image-preview',
    input: 'Generate an image of a futuristic city.',
    response_modalities: ['image']
});

for (const output of interaction.outputs) {
    if (output.type === 'image') {
        console.log(`Generated image with mime_type: ${output.mime_type}`);
        // Save the image
        fs.writeFileSync('generated_city.png', Buffer.from(output.data, 'base64'));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate an image of a futuristic city.",
    "response_modalities": ["image"]
}'
```

##### 이미지 출력 구성

`generation_config` 내에서 `image_config`를 사용하여 생성된 이미지를 맞춤설정하여 가로세로 비율과 해상도를 제어할 수 있습니다.

| 매개변수 | 옵션 | 설명 |
| --- | --- | --- |
| `aspect_ratio` | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` | 출력 이미지의 가로세로 비율을 제어합니다. |
| `image_size` | `1k`, `2k`, `4k` | 출력 이미지 해상도를 설정합니다. |

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an image of a futuristic city.",
    generation_config={
        "image_config": {
            "aspect_ratio": "9:16",
            "image_size": "2k"
        }
    }
)

for output in interaction.outputs:
    if output.type == "image":
        print(f"Generated image with mime_type: {output.mime_type}")
        # Save the image
        with open("generated_city.png", "wb") as f:
            f.write(base64.b64decode(output.data))
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-pro-image-preview',
    input: 'Generate an image of a futuristic city.',
    generation_config: {
        image_config: {
            aspect_ratio: '9:16',
            image_size: '2k'
        }
    }
});

for (const output of interaction.outputs) {
    if (output.type === 'image') {
        console.log(`Generated image with mime_type: ${output.mime_type}`);
        // Save the image
        fs.writeFileSync('generated_city.png', Buffer.from(output.data, 'base64'));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate an image of a futuristic city.",
    "generation_config": {
        "image_config": {
            "aspect_ratio": "9:16",
            "image_size": "2k"
        }
    }
}'
```

#### 음성 생성

텍스트 음성 변환 (TTS) 모델을 사용하여 텍스트에서 자연스러운 음성 생성
`speech_config` 매개변수를 사용하여 음성, 언어, 스피커 설정을 구성합니다.

### Python

```
import base64
from google import genai
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say the following: WOOHOO This is so much fun!. [laughs]",
    response_modalities=["audio"],
    generation_config={
        "speech_config": [
            {
                "language": "en-us",
                "voice": "kore"
            }
        ]
    }
)

for output in interaction.outputs:
    if output.type == "audio":
        print(f"Generated audio with mime_type: {output.mime_type}")
        # Save the audio as wave file to the current directory.
        wave_file("generated_audio.wav", base64.b64decode(output.data))
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
import wav from 'wav';

async function saveWaveFile(
    filename,
    pcmData,
    channels = 1,
    rate = 24000,
    sampleWidth = 2,
) {
    return new Promise((resolve, reject) => {
        const writer = new wav.FileWriter(filename, {
                channels,
                sampleRate: rate,
                bitDepth: sampleWidth * 8,
        });

        writer.on('finish', resolve);
        writer.on('error', reject);

        writer.write(pcmData);
        writer.end();
    });
}

async function main() {
    const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
    const client = new GoogleGenAI({apiKey: GEMINI_API_KEY});

    const interaction = await client.interactions.create({
        model: 'gemini-3.1-flash-tts-preview',
        input: 'Say the following: WOOHOO This is so much fun!.',
        response_modalities: ['audio'],
        generation_config: {
            speech_config: [
                {
                    language: "en-us",
                    voice: "kore"
                }
            ]
        }
    });

    for (const output of interaction.outputs) {
        if (output.type === 'audio') {
            console.log(`Generated audio with mime_type: ${output.mime_type}`);
            const audioBuffer = Buffer.from(output.data, 'base64');
            // Save the audio as wave file to the current directory
            await saveWaveFile("generated_audio.wav", audioBuffer);
        }
    }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say the following: WOOHOO This is so much fun!.",
    "response_modalities": ["audio"],
    "generation_config": {
        "speech_config": [
            {
                "language": "en-us",
                "voice": "kore"
            }
        ]
    }
}' | jq -r '.outputs[] | select(.type == "audio") | .data' | base64 -d > generated_audio.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i generated_audio.pcm generated_audio.wav
```

TTS는 스트리밍을 지원하지 않습니다.

##### 다중 화자 음성 생성

프롬프트에서 화자 이름을 지정하고 `speech_config`에서 일치시켜 여러 화자가 포함된 음성을 생성합니다.

프롬프트에 화자 이름을 포함해야 합니다.

```
TTS the following conversation between Alice and Bob:
Alice: Hi Bob, how are you doing today?
Bob: I'm doing great, thanks for asking! How about you?
Alice: Fantastic! I just learned about the Gemini API.
```

그런 다음 일치하는 스피커로 `speech_config`를 구성합니다.

```
"generation_config": {
    "speech_config": [
        {"voice": "Zephyr", "speaker": "Alice", "language": "en-US"},
        {"voice": "Puck", "speaker": "Bob", "language": "en-US"}
    ]
}
```

#### 음악 생성

Lyria 3 모델을 사용하여 텍스트 프롬프트에서 고품질 음악을 생성하세요. Interactions API는 보컬, 가사, 악기 편곡이 포함된 짧은 클립과 전체 길이 노래를 모두 지원합니다.

맞춤 가사, 타이밍 제어, 이미지-음악을 비롯한 전체 음악 생성 가이드는 [Lyria 3로 음악 생성하기](https://ai.google.dev/gemini-api/docs/Lyria 3로 음악 생성하기)를 참고하세요.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="Create a 30-second cheerful acoustic folk song with "
          "guitar and harmonica.",
)

for output in interaction.outputs:
    if output.type == "audio":
        print(f"Generated audio with mime_type: {output.mime_type}")
        with open("music.mp3", "wb") as f:
            f.write(base64.b64decode(output.data))
    elif output.type == "text":
        print(f"Lyrics: {output.text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'Create a 30-second cheerful acoustic folk song with ' +
           'guitar and harmonica.',
});

for (const output of interaction.outputs) {
    if (output.type === 'audio') {
        console.log(`Generated audio with mime_type: ${output.mime_type}`);
        fs.writeFileSync('music.mp3', Buffer.from(output.data, 'base64'));
    } else if (output.type === 'text') {
        console.log(`Lyrics: ${output.text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "Create a 30-second cheerful acoustic folk song with guitar and harmonica."
}'
```

전체 길이 노래 (최대 4분)의 경우 `lyria-3-pro-preview` 모델을 사용합니다.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. "
          "Starts with a solo piano intro, builds through sweeping "
          "strings, and climaxes with a massive wall of sound.",
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'An epic cinematic orchestral piece about a journey home. ' +
           'Starts with a solo piano intro, builds through sweeping ' +
           'strings, and climaxes with a massive wall of sound.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound."
}'
```

## 에이전트 기능

Interactions API는 에이전트를 빌드하고 에이전트와 상호작용하도록 설계되었으며, 함수 호출, 기본 제공 도구, 구조화된 출력, 모델 컨텍스트 프로토콜 (MCP)을 지원합니다.

### 에이전트

복잡한 작업에는 `deep-research-preview-04-2026`와 같은 전문 에이전트를 사용할 수 있습니다. Gemini Deep Research Agent에 대해 자세히 알아보려면 [Deep Research](https://ai.google.dev/gemini-api/docs/Deep Research) 가이드를 참고하세요.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the Deep Research Agent
initial_interaction = client.interactions.create(
    input="Research the history of the Google TPUs with a focus on 2025 and 2026.",
    agent="deep-research-preview-04-2026",
    background=True
)

print(f"Research started. Interaction ID: {initial_interaction.id}")

# 2. Poll for results
while True:
    interaction = client.interactions.get(initial_interaction.id)
    print(f"Status: {interaction.status}")

    if interaction.status == "completed":
        print("\nFinal Report:\n", interaction.outputs[-1].text)
        break
    elif interaction.status in ["failed", "cancelled"]:
        print(f"Failed with status: {interaction.status}")
        break

    time.sleep(10)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Start the Deep Research Agent
const initialInteraction = await client.interactions.create({
    input: 'Research the history of the Google TPUs with a focus on 2025 and 2026.',
    agent: 'deep-research-preview-04-2026',
    background: true
});

console.log(`Research started. Interaction ID: ${initialInteraction.id}`);

// 2. Poll for results
while (true) {
    const interaction = await client.interactions.get(initialInteraction.id);
    console.log(`Status: ${interaction.status}`);

    if (interaction.status === 'completed') {
        console.log('\nFinal Report:\n', interaction.outputs[interaction.outputs.length - 1].text);
        break;
    } else if (['failed', 'cancelled'].includes(interaction.status)) {
        console.log(`Failed with status: ${interaction.status}`);
        break;
    }

    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### REST

```
# 1. Start the Deep Research Agent
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "input": "Research the history of the Google TPUs with a focus on 2025 and 2026.",
    "agent": "deep-research-preview-04-2026",
    "background": true
}'

# 2. Poll for results (Replace INTERACTION_ID with the ID from the previous interaction)
# curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID" \
# -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 도구 및 함수 호출

이 섹션에서는 함수 호출을 사용하여 맞춤 도구를 정의하는 방법과 Interactions API 내에서 Google의 기본 제공 도구를 사용하는 방법을 설명합니다.

#### 함수 호출

### Python

```
from google import genai

client = genai.Client()

# 1. Define the tool
def get_weather(location: str):
    """Gets the weather for a given location."""
    return f"The weather in {location} is sunny."

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
        },
        "required": ["location"]
    }
}

# 2. Send the request with tools
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool]
)

# 3. Handle the tool call
for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Tool Call: {output.name}({output.arguments})")
        # Execute tool
        result = get_weather(**output.arguments)

        # Send result back
        interaction = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": result
            }]
        )
        print(f"Response: {interaction.outputs[-1].text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

// 1. Define the tool
const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

// 2. Send the request with tools
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool]
});

// 3. Handle the tool call
for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Tool Call: ${output.name}(${JSON.stringify(output.arguments)})`);

        // Execute tool (Mocked)
        const result = `The weather in ${output.arguments.location} is sunny.`;

        // Send result back
        interaction = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id:interaction.id,
            input: [{
                type: 'function_result',
                name: output.name,
                call_id: output.id,
                result: result
            }]
        });
        console.log(`Response: ${interaction.outputs[interaction.outputs.length - 1].text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
            },
            "required": ["location"]
        }
    }]
}'

# Handle the tool call and send result back (Replace INTERACTION_ID and CALL_ID)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "previous_interaction_id": "INTERACTION_ID",
#     "input": [{
#         "type": "function_result",
#         "name": "get_weather",
#         "call_id": "FUNCTION_CALL_ID",
#         "result": "The weather in Paris is sunny."
#     }]
# }'
```

##### 클라이언트 측 상태를 사용한 함수 호출

서버 측 상태를 사용하지 않으려면 클라이언트 측에서 모든 상태를 관리하면 됩니다.

### Python

```
from google import genai
client = genai.Client()

functions = [
    {
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
            "type": "object",
            "properties": {
                "attendees": {"type": "array", "items": {"type": "string"}},
                "date": {"type": "string", "description": "Date of the meeting (e.g., 2024-07-29)"},
                "time": {"type": "string", "description": "Time of the meeting (e.g., 15:00)"},
                "topic": {"type": "string", "description": "The subject of the meeting."},
            },
            "required": ["attendees", "date", "time", "topic"],
        },
    }
]

history = [{"role": "user","content": [{"type": "text", "text": "Schedule a meeting for 2025-11-01 at 10 am with Peter and Amir about the Next Gen API."}]}]

# 1. Model decides to call the function
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=history,
    tools=functions
)

# add model interaction back to history
history.append({"role": "model", "content": interaction.outputs})

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name} with arguments {output.arguments}")

        # 2. Execute the function and get a result
        # In a real app, you would call your function here.
        # call_result = schedule_meeting(**json.loads(output.arguments))
        call_result = "Meeting scheduled successfully."

        # 3. Send the result back to the model
        history.append({"role": "user", "content": [{"type": "function_result", "name": output.name, "call_id": output.id, "result": call_result}]})

        interaction2 = client.interactions.create(
            model="gemini-3-flash-preview",
            input=history,
        )
        print(f"Final response: {interaction2.outputs[-1].text}")
    else:
        print(f"Output: {output}")
```

### 자바스크립트

```
// 1. Define the tool
const functions = [
    {
        type: 'function',
        name: 'schedule_meeting',
        description: 'Schedules a meeting with specified attendees at a given time and date.',
        parameters: {
            type: 'object',
            properties: {
                attendees: { type: 'array', items: { type: 'string' } },
                date: { type: 'string', description: 'Date of the meeting (e.g., 2024-07-29)' },
                time: { type: 'string', description: 'Time of the meeting (e.g., 15:00)' },
                topic: { type: 'string', description: 'The subject of the meeting.' },
            },
            required: ['attendees', 'date', 'time', 'topic'],
        },
    },
];

const history = [
    { role: 'user', content: [{ type: 'text', text: 'Schedule a meeting for 2025-11-01 at 10 am with Peter and Amir about the Next Gen API.' }] }
];

// 2. Model decides to call the function
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: history,
    tools: functions
});

// add model interaction back to history
history.push({ role: 'model', content: interaction.outputs });

for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Function call: ${output.name} with arguments ${JSON.stringify(output.arguments)}`);

        // 3. Send the result back to the model
        history.push({ role: 'user', content: [{ type: 'function_result', name: output.name, call_id: output.id, result: 'Meeting scheduled successfully.' }] });

        const interaction2 = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            input: history,
        });
        console.log(`Final response: ${interaction2.outputs[interaction2.outputs.length - 1].text}`);
    }
}
```

##### 멀티모달 함수 결과

`function_result`의 `result` 필드는 일반 문자열 또는 `TextContent` 및 `ImageContent` 객체의 배열을 허용합니다. 이렇게 하면 함수 호출의 텍스트와 함께 스크린샷이나 차트와 같은 이미지를 반환할 수 있으므로 모델이 시각적 출력을 기반으로 추론할 수 있습니다.

### Python

```
import base64
from google import genai

client = genai.Client()

functions = [
    {
        "type": "function",
        "name": "take_screenshot",
        "description": "Takes a screenshot of a specified website.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The URL to take a screenshot of."},
            },
            "required": ["url"],
        },
    }
]

# 1. Model decides to call the function
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Can you take a screenshot of https://google.com and tell me what you see?",
    tools=functions
)

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name}({output.arguments})")

        # 2. Execute the function and load the image
        # Replace with actual function call, pseudo code for reading image from disk
        with open("screenshot.png", "rb") as f:
            base64_image = base64.b64encode(f.read()).decode("utf-8")

        # 3. Return a multimodal result (text + image)
        call_result = [
            {"type": "text", "text": "Screenshot captured successfully."},
            {"type": "image", "mime_type": "image/png", "data": base64_image}
        ]

        response = client.interactions.create(
            model="gemini-3-flash-preview",
            tools=functions,
            previous_interaction_id=interaction.id,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": call_result
            }]
        )
        print(f"Response: {response.outputs[-1].text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const functions = [
    {
        type: 'function',
        name: 'take_screenshot',
        description: 'Takes a screenshot of a specified website.',
        parameters: {
            type: 'object',
            properties: {
                url: { type: 'string', description: 'The URL to take a screenshot of.' },
            },
            required: ['url'],
        },
    }
];

// 1. Model decides to call the function
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Can you take a screenshot of https://google.com and tell me what you see?',
    tools: functions
});

for (const output of interaction.outputs) {
    if (output.type === 'function_call') {
        console.log(`Function call: ${output.name}(${JSON.stringify(output.arguments)})`);

        // 2. Execute the function and load the image
        // Replace with actual function call, pseudo code for reading image from disk
        const base64Image = fs.readFileSync('screenshot.png').toString('base64');

        // 3. Return a multimodal result (text + image)
        const callResult = [
            { type: 'text', text: 'Screenshot captured successfully.' },
            { type: 'image', mime_type: 'image/png', data: base64Image }
        ];

        const response = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            tools: functions,
            previous_interaction_id: interaction.id,
            input: [{
                type: 'function_result',
                name: output.name,
                call_id: output.id,
                result: callResult
            }]
        });
        console.log(`Response: ${response.outputs[response.outputs.length - 1].text}`);
    }
}
```

### REST

```
# 1. Send request with tools (will return a function_call)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Can you take a screenshot of https://google.com and tell me what you see?",
    "tools": [{
        "type": "function",
        "name": "take_screenshot",
        "description": "Takes a screenshot of a specified website.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The URL to take a screenshot of."}
            },
            "required": ["url"]
        }
    }]
}'

# 2. Send multimodal result back (Replace INTERACTION_ID, CALL_ID, and BASE64_IMAGE)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
# -H "Content-Type: application/json" \
# -H "x-goog-api-key: $GEMINI_API_KEY" \
# -d '{
#     "model": "gemini-3-flash-preview",
#     "tools": [{"type": "function", "name": "take_screenshot", "description": "Takes a screenshot of a specified website.", "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}}],
#     "previous_interaction_id": "INTERACTION_ID",
#     "input": [{
#         "type": "function_result",
#         "name": "take_screenshot",
#         "call_id": "CALL_ID",
#         "result": [
#             {"type": "text", "text": "Screenshot captured successfully."},
#             {"type": "image", "mime_type": "image/png", "data": "BASE64_IMAGE"}
#         ]
#     }]
# }'
```

#### 기본 제공 도구

Gemini에는 [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/Google 검색을 사용한 그라운딩), [Google 이미지 검색으로 그라운딩](https://ai.google.dev/gemini-api/docs/Google 이미지 검색으로 그라운딩), [Google 지도 기반 그라운딩](https://ai.google.dev/gemini-api/docs/Google 지도 기반 그라운딩), [코드 실행](https://ai.google.dev/gemini-api/docs/코드 실행), [URL 컨텍스트](https://ai.google.dev/gemini-api/docs/URL 컨텍스트), [컴퓨터 사용](https://ai.google.dev/gemini-api/docs/컴퓨터 사용)과 같은 기본 제공 도구가 있습니다.

##### Google 검색을 사용하는 그라운딩

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the last Super Bowl?",
    tools=[{"type": "google_search"}]
)
# Find the text output (not the GoogleSearchResultContent)
text_output = next((o for o in interaction.outputs if o.type == "text"), None)
if text_output:
    print(text_output.text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Who won the last Super Bowl?',
    tools: [{ type: 'google_search' }]
});
// Find the text output (not the GoogleSearchResultContent)
const textOutput = interaction.outputs.find(o => o.type === 'text');
if (textOutput) console.log(textOutput.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last Super Bowl?",
    "tools": [{"type": "google_search"}]
}'
```

##### Google 이미지 검색을 사용한 그라운딩 (3.1 Flash Image에만 해당)

Google 이미지 검색을 사용한 그라운딩을 사용하면 모델이 Google 이미지 검색을 통해 검색된 웹 이미지를 이미지 생성의 시각적 컨텍스트로 사용할 수 있습니다. 이미지 검색은 기존의 Google 검색을 사용한 그라운딩 도구 내의 새로운 검색 유형으로, 표준 [웹 검색](https://ai.google.dev/gemini-api/docs/웹 검색)과 함께 작동합니다.

###### 이미지 검색 사용 설정

`google_search` 도구의 `search_types` 배열에 `"image_search"`를 추가하여 이미지 결과를 요청합니다.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.1-flash-image-preview",
    input="Search for an image of a vintage gold bitcoin coin.",
    tools=[{
        "type": "google_search",
        "search_types": ["web_search", "image_search"]
    }]
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    model: 'gemini-3.1-flash-image-preview',
    input: 'Search for an image of a vintage gold bitcoin coin.',
    tools: [{
        type: 'google_search',
        search_types: ['web_search', 'image_search']
    }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.1-flash-image-preview",
    "input": "Search for an image of a vintage gold bitcoin coin.",
    "tools": [{
        "type": "google_search",
        "search_types": ["web_search", "image_search"]
    }]
}'
```

###### 필수 표시 요구사항

[Google 검색 서비스 약관](https://ai.google.dev/gemini-api/docs/Google 검색 서비스 약관)을 준수하려면 UI에서 다음과 같은 두 가지 수준의 저작자 표시를 구현해야 합니다.

1. **Google 검색 기여 분석**

   `google_search_result` 블록에 제공된 'Google에서 확인' 추천 검색어를 표시해야 합니다.

   - **필드:** `rendered_content` (HTML/CSS)
   - **작업:** 이 칩을 모델의 대답 근처에 있는 그대로 렌더링합니다.
2. **게시자 출처 표시**

   표시되는 모든 이미지에 대해 '포함 페이지' (방문 페이지) 링크를 제공해야 합니다.

   - **필드:** `url` (`result` 배열 내에 있음)
   - **요구사항:** 이미지에서 포함된 소스 웹페이지로 바로 연결되는 단일 클릭 경로를 제공해야 합니다. 중간 이미지 뷰어나 다중 클릭 경로를 사용하는 것은 허용되지 않습니다.

###### 그라운딩된 대답 처리

다음 스니펫은 원시 이미지 데이터와 필수 기여 분석 모두에 대해 인터리브된 응답 블록을 처리하는 방법을 보여줍니다.

### Python

```
for output in interaction.outputs:
    # 1. Handle raw multimodal image data
    if output.type == "image":
        print(f"🖼️ Image received: {output.mime_type}")
        # 'data' contains base64-encoded image content
        display_image(output.data, output.mime_type)
    # 2. Handle mandatory Search and Publisher attribution
    elif output.type == "google_search_result":
        # Display Google Search Attribution
        if output.rendered_content:
            render_html_chips(output.rendered_content)

        # Provide Publisher Attribution

        for source in output.result:
            print(f"Source Page: {source['url']}")
```

### 자바스크립트

```
for (const output of interaction.outputs) {
  // 1. Handle raw multimodal image data
  if (output.type === 'image') {
    console.log(`🖼️ Image received: ${output.mimeType}`);
    // 'data' contains base64-encoded image content
    displayImage(output.data, output.mimeType);
  }
    // 2. Handle mandatory Search and Publisher attribution
    else if (output.type === 'google_search_result') {
      // Display Google Search Attribution
      if (output.renderedContent) {
        renderHtmlChips(output.renderedContent);
      }

      // Provide Publisher Attribution

    for (const source of output.result) {
      console.log(`Source Page: ${source.url}`);
    }
  }
}
```

###### 예상 출력 스키마

**이미지 블록** (유형: `"image"`)에는 모델에서 생성하거나 검색한 원시 시각적 데이터가 포함됩니다.

```
{
  "type": "image",
  "mime_type": "image/png",
  "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..." // Base64 content
}
```

**결과 블록** (유형: `"google_search_result"`)에는 검색에 연결된 필수 기여 분석 메타데이터가 포함됩니다.

```
{
  "type": "google_search_result",
  "call_id": "search_002",
  "rendered_content": "<div class=\"search-suggestions\">...</div>", // Google Search Attribution

  "result": [
    {
      "url": "https://example.com/source-page", // Publisher Attribution
      "title": "Source Page Title"
    }
  ]
}
```

##### Google 지도를 사용한 그라운딩

Google 지도 기반 그라운딩을 통해 모델은 시각적 컨텍스트, 지도 핀, 위치 기반 검색에 Google 지도 데이터를 사용할 수 있습니다.

### Python

```
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the best coffee shop near me?",
    tools=[{"type": "google_maps"}]
)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
const client = new GoogleGenAI({});
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What\'s the best coffee shop near me?',
    tools: [{ type: 'google_maps' }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the best coffee shop near me?",
    "tools": [{"type": "google_maps"}]
}'
```

###### 서비스 사용 요구사항

Google 지도 기반 그라운딩 결과를 표시할 때는 [Google 지도 서비스 약관](https://ai.google.dev/gemini-api/docs/Google 지도 서비스 약관)을 따라야 합니다.
사용자에게 다음 사항을 알리고 이러한 표시 요구사항을 충족해야 합니다.

- **사용자에게 알림**: 생성된 콘텐츠 바로 뒤에 연결된 Google 지도 소스를 표시합니다. 소스는 단일 사용자 상호작용 내에서 확인 가능해야 합니다.
- **링크 표시**: 각 소스에 대한 링크 미리보기를 생성합니다 (리뷰 스니펫이 있는 경우 포함).
- **'Google 지도'로 저작자 표시**: [텍스트 저작자 표시 가이드라인](https://ai.google.dev/gemini-api/docs/텍스트 저작자 표시 가이드라인)을 따릅니다.
- **소스 제목을 표시**합니다.
- 제공된 URL을 사용하여 **소스에 연결**합니다.
- **저작자 표시 가이드라인**: 'Google 지도' 텍스트를 수정하지 마세요(대소문자, 줄바꿈). `translate="no"`를 사용하여 브라우저 번역을 방지합니다.

###### 응답 처리

다음 스니펫은 표시 요구사항을 충족하기 위해 텍스트와 인라인 인용 (리뷰 스니펫 포함)을 추출하여 응답을 처리하는 방법을 보여줍니다.

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "place_citation":
                    # Display place citation
                    print(f"- {annotation['name']} (Google Maps): {annotation['url']}")
                    # Display review snippets if available
                    if "review_snippets" in annotation:
                        for snippet in annotation["review_snippets"]:
                            print(f"  - Review: {snippet['title']} ({snippet['url']})")
    elif output.type == "google_maps_result":
        # You can also access the raw place data here if needed for map pins
        pass
```

### 자바스크립트

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'place_citation') {
                    console.log(`- ${annotation.name} (Google Maps): ${annotation.url}`);
                    if (annotation.review_snippets) {
                        for (const snippet of annotation.review_snippets) {
                            console.log(`  - Review: ${snippet.title} (${snippet.url})`);
                        }
                    }
                }
            }
        }
    }
}
```

###### 예상 출력 스키마

Google 지도 기반 그라운딩을 사용할 때는 다음 출력 스키마가 예상됩니다.

**결과 블록** (유형: `"google_maps_result"`)에는 구조화된 장소 데이터가 포함됩니다.

```
{
  "type": "google_maps_result",
  "call_id": "maps_001",
  "result": {
    "places": [
      {
        "place_id": "ChIJ...",
        "name": "Blue Bottle Coffee", // Google Maps Source
        "url": "https://maps.google.com/?cid=...", // Google Maps Link
        "review_snippets": [
          {
            "title": "Amazing single-origin selections",
            "url": "https://maps.google.com/...",
            "review_id": "def456"
          }
        ]
      }
    ],
    "widget_context_token": "widgetcontent/..."
  },
  "signature": "..."
}
```

**텍스트 블록** (유형: `"text"`)에는 인라인 주석이 포함된 생성된 콘텐츠가 포함됩니다.

```
{
  "type": "text",
  "text": "Blue Bottle Coffee (4.5★) on Mint Plaza was rated highly online...",
  "annotations": [
    {
      "type": "place_citation",
      "place_id": "ChIJ...",
      "name": "Blue Bottle Coffee", // Google Maps Source
      "url": "https://maps.google.com/?cid=...", // Google Maps Link
      "review_snippets": [
        {
          "title": "Amazing single-origin selections",
          "url": "https://maps.google.com/...",
          "review_id": "def456"
        }
      ],
      "start_index": 0,
      "end_index": 42
    }
  ]
}
```

##### 코드 실행

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Calculate the 50th Fibonacci number.",
    tools=[{"type": "code_execution"}]
)
print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Calculate the 50th Fibonacci number.',
    tools: [{ type: 'code_execution' }]
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Calculate the 50th Fibonacci number.",
    "tools": [{"type": "code_execution"}]
}'
```

##### URL 컨텍스트

URL 컨텍스트를 사용한 그라운딩을 통해 모델은 프롬프트 또는 도구 목록에 제공된 공개 URL을 읽을 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Summarize the content of https://www.wikipedia.org/",
    tools=[{"type": "url_context"}]
)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Summarize the content of https://www.wikipedia.org/',
    tools: [{ type: 'url_context' }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Summarize the content of https://www.wikipedia.org/",
    "tools": [{"type": "url_context"}]
}'
```

###### 응답 처리

다음 스니펫은 텍스트와 인라인 인용 (`url_citation` 유형)을 추출하여 응답을 처리하는 방법을 보여줍니다.

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "url_citation":
                    print(f"- {annotation['title']}: {annotation['url']}")
```

### 자바스크립트

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'url_citation') {
                    console.log(`- ${annotation.title}: ${annotation.url}`);
                }
            }
        }
    }
}
```

###### 예상 출력 스키마

URL 컨텍스트를 사용하는 경우 다음 출력 스키마가 예상됩니다.

**호출 차단** (유형: `"url_context_call"`)에는 모델이 읽으려고 시도한 URL이 포함됩니다.

```
{
  "type": "url_context_call",
  "id": "browse_001",
  "arguments": {
    "urls": ["https://www.wikipedia.org/"]
  },
  "signature": "EkYKIGY5OT..."
}
```

**결과 블록** (유형: `"url_context_result"`)에는 검색 상태가 포함됩니다.

```
{
  "type": "url_context_result",
  "call_id": "browse_001",
  "result": {
    "url": "https://www.wikipedia.org/",
    "status": "URL_RETRIEVAL_STATUS_SUCCESS"
  },
  "signature": "EkYKIGY5OT..."
}
```

**텍스트 블록**에는 생성된 텍스트와 인라인 인용이 포함됩니다.

```
{
  "type": "text",
  "text": "Wikipedia is a free online encyclopedia...",
  "annotations": [
    {
      "type": "url_citation",
      "url": "https://www.wikipedia.org/",
      "title": "Wikipedia — Main Page",
      "start_index": 0,
      "end_index": 42
    }
  ]
}
```

##### 컴퓨터 사용

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-2.5-computer-use-preview-10-2025",
    input="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    tools=[{
        "type": "computer_use",
        "environment": "browser",
        "excludedPredefinedFunctions": ["drag_and_drop"]
    }]
)

# The response will contain tool calls (actions) for the computer interface
# or text explaining the action
for output in interaction.outputs:
    print(output)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-2.5-computer-use-preview-10-2025',
    input: 'Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.',
    tools: [{
        type: 'computer_use',
        environment: 'browser',
        excludedPredefinedFunctions: ['drag_and_drop']
    }]
});

// The response will contain tool calls (actions) for the computer interface
// or text explaining the action
interaction.outputs.forEach(output => console.log(output));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-computer-use-preview-10-2025",
    "input": "Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout.",
    "tools": [{
        "type": "computer_use",
        "environment": "browser",
        "excludedPredefinedFunctions": ["drag_and_drop"]
    }]
}'
```

###### Computer Use 함수 결과 처리

Computer Use는 클라이언트 측 도구 루프이므로 작업을 실행하고 (예: 브라우저 열기) 결과를 모델에 다시 전송해야 합니다. `open_web_browser`과 같은 작업에 `function_result`를 전송할 때는 아래와 같이 결과 목록에 URL 응답을 전달해야 합니다.

```
{
  "type": "function_result",
  "name": "open_web_browser",
  "call_id": "5q6h0z70",
  "result": [
    {
      "type": "text",
      "text": "{\"url\": \"https://google.com\", \"safety_acknowledgement\":true}"
    },
    {
      "type": "image",
      "data": "iVBORw0KGgoAAAANSUhEUgAA...",
      "mime_type": "image/png"
    }
  ]
}
```

##### 파일 검색

파일 검색으로 그라운딩을 사용하면 모델이 파일 검색 스토어에서 업로드된 파일을 검색할 수 있습니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me about the book 'I, Claudius'",
    tools=[{"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]}]
)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "Tell me about the book 'I, Claudius'",
    tools: [{ type: 'file_search', file_search_store_names: ['fileSearchStores/my-store-name'] }]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me about the book 'I, Claudius'",
    "tools": [{"type": "file_search", "file_search_store_names": ["fileSearchStores/my-store-name"]}]
}'
```

###### 응답 처리

다음 스니펫은 텍스트와 인라인 인용 (`file_citation` 유형)을 추출하여 응답을 처리하는 방법을 보여줍니다.

### Python

```
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
        if output.annotations:
            print("\nSources:")
            for annotation in output.annotations:
                if annotation.get("type") == "file_citation":
                    print(f"- {annotation['file_name']} ({annotation['document_uri']}):")
                    print(f"  Snippet: {annotation['source']}")
```

### 자바스크립트

```
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
        if (output.annotations) {
            console.log('\nSources:');
            for (const annotation of output.annotations) {
                if (annotation.type === 'file_citation') {
                    console.log(`- ${annotation.fileName} (${annotation.documentUri}):`);
                    console.log(`  Snippet: ${annotation.source}`);
                }
            }
        }
    }
}
```

###### 예상 출력 스키마

파일 검색을 사용할 때는 다음 출력 스키마가 예상됩니다.

**통화 차단** (유형: `"file_search_call"`)에는 통화 메타데이터가 포함됩니다.

```
{
  "type": "file_search_call",
  "id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

**결과 블록** (유형: `"file_search_result"`)에는 결과 메타데이터가 포함됩니다.

```
{
  "type": "file_search_result",
  "call_id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

**텍스트 블록**에는 생성된 텍스트와 인라인 인용이 포함됩니다.

```
{
  "type": "text",
  "text": "The book 'I, Claudius' is a historical novel by Robert Graves...",
  "annotations": [
    {
      "type": "file_citation",
      "document_uri": "fileSearchStores/my-store-name/documents/abc",
      "file_name": "book_summaries.pdf",
      "source": "Claudius is the narrator of this historical novel...",
      "start_index": 0,
      "end_index": 60
    }
  ]
}
```

#### 기본 제공 도구와 함수 호출 결합

동일한 요청에서 [기본 제공 도구와 함수 호출](https://ai.google.dev/gemini-api/docs/기본 제공 도구와 함수 호출)을 함께 사용할 수 있습니다.

### Python

```
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

tools = [
    {"type": "google_search"},  # Built-in tool
    get_weather                 # Custom tool (callable)
]

# Turn 1: Initial request with both tools enabled
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for output in interaction.outputs:
    if output.type == "function_call":
        print(f"Function call: {output.name} (ID: {output.id})")
        # Execute your custom function locally
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        # Turn 2: Provide the function result back to the model.
        # Passing `previous_interaction_id` automatically circulates the
        # built-in Google Search context (and thought signatures) from Turn 1
        interaction_2 = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": output.name,
                "call_id": output.id,
                "result": json.dumps(result)
            }]
        )

        for output in interaction_2.outputs:
            if output.type == "text":
                print(output.text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool              // Custom tool
];

// Turn 1: Initial request with both tools enabled
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const output of interaction.outputs) {
    if (output.type == "function_call") {
        console.log(`Function call: ${output.name} (ID: ${output.id})`);
        // Execute your custom function locally
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        // Turn 2: Provide the function result back to the model.
        // Passing `previous_interaction_id` automatically circulates the
        // built-in Google Search context (and thought signatures) from Turn 1
        const interaction_2 = await client.interactions.create({
            model: "gemini-3-flash-preview",
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: "function_result",
                name: output.name,
                call_id: output.id,
                result: JSON.stringify(result)
            }]
        });

        for (const output_2 of interaction_2.outputs) {
            if (output_2.type == "text") {
                console.log(output_2.text);
            }
        }
    }
}
```

### REST

```
# Turn 1: Initial request with both tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the northernmost city in the United States? What is the weather like there today?",
    "tools": [
        {"type": "google_search"},
        {
            "type": "function",
            "name": "get_weather",
            "description": "Gets the weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
                },
                "required": ["location"]
            }
        }
    ]
}'

# Assuming Turn 1 returns a function_call for get_weather,
# replace INTERACTION_ID and CALL_ID with values from Turn 1 response.
# Turn 2: Provide the function result back to the model.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "tools": [
        {"type": "google_search"},
        {
            "type": "function",
            "name": "get_weather",
            "description": "Gets the weather for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
                },
                "required": ["location"]
            }
        }
    ],
    "input": [{
        "type": "function_result",
        "name": "get_weather",
        "call_id": "CALL_ID",
        "result": "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"
    }]
}'
```

##### 도구 컨텍스트 순환 이해

Gemini 3 이상의 모델은 서버 측 작업의 신뢰할 수 있는 '메모리'를 유지하기 위해 **도구 컨텍스트 순환**을 지원합니다. Google 검색과 같은 내장 도구가 트리거되면 API가 특정 `toolCall` 및 `toolResponse` 부분을 생성합니다. 이러한 부분에는 모델이 다음 턴에서 이러한 결과를 추론하는 데 필요한 정확한 컨텍스트가 포함되어 있습니다.

- **스테이트풀(Stateful)(권장)**: `previous_interaction_id`를 사용하는 경우 API가 이 순환을 자동으로 관리합니다.
- **상태 비저장**: 기록을 수동으로 관리하는 경우 API에서 반환된 대로 이러한 블록을 입력 배열에 포함해야 합니다.

### 원격 모델 컨텍스트 프로토콜 (MCP)

원격 [MCP](https://ai.google.dev/gemini-api/docs/MCP) 통합을 사용하면 Gemini API가 원격 서버에 호스팅된 외부 도구를 직접 호출할 수 있으므로 에이전트 개발이 간소화됩니다.

### Python

```
import datetime
from google import genai

client = genai.Client()

mcp_server = {
    "type": "mcp_server",
    "name": "weather_service",
    "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
}

today = datetime.date.today().strftime("%d %B %Y")

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="What is the weather like in New York today?",
    tools=[mcp_server],
    system_instruction=f"Today is {today}."
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const mcpServer = {
    type: 'mcp_server',
    name: 'weather_service',
    url: 'https://gemini-api-demos.uc.r.appspot.com/mcp'
};

const today = new Date().toDateString();

const interaction = await client.interactions.create({
    model: 'gemini-2.5-flash',
    input: 'What is the weather like in New York today?',
    tools: [mcpServer],
    system_instruction: `Today is ${today}.`
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-2.5-flash",
    "input": "What is the weather like in New York today?",
    "tools": [{
        "type": "mcp_server",
        "name": "weather_service",
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }],
    "system_instruction": "Today is '"$(date +"%du%Bt%Y")"' YYYY-MM-DD>."
}'
```

**중요사항:**

- 원격 MCP는 스트리밍 가능 HTTP 서버에서만 작동합니다 (SSE 서버는 지원되지 않음).
- 원격 MCP는 Gemini 3 모델에서 작동하지 않습니다 (곧 지원 예정).
- MCP 서버 이름에 '-' 문자를 포함하면 안 됩니다 (대신 snake\_case 서버 이름을 사용하세요).

### 구조화된 출력 (JSON 스키마)

`response_format` 매개변수에 JSON 스키마를 제공하여 특정 JSON 출력을 강제합니다. 이 기능은 조정, 분류, 데이터 추출과 같은 작업에 유용합니다.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal, Union
client = genai.Client()

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"]

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format=ModerationResult.model_json_schema(),
)

parsed_output = ModerationResult.model_validate_json(interaction.outputs[-1].text)
print(parsed_output)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import { z } from 'zod';
const client = new GoogleGenAI({});

const moderationSchema = z.object({
    decision: z.union([
        z.object({
            reason: z.string().describe('The reason why the content is considered spam.'),
            spam_type: z.enum(['phishing', 'scam', 'unsolicited promotion', 'other']).describe('The type of spam.'),
        }).describe('Details for content classified as spam.'),
        z.object({
            summary: z.string().describe('A brief summary of the content.'),
            is_safe: z.boolean().describe('Whether the content is safe for all audiences.'),
        }).describe('Details for content classified as not spam.'),
    ]),
});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format: z.toJSONSchema(moderationSchema),
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    "response_format": {
        "type": "object",
        "properties": {
            "decision": {
                "type": "object",
                "properties": {
                    "reason": {"type": "string", "description": "The reason why the content is considered spam."},
                    "spam_type": {"type": "string", "description": "The type of spam."}
                },
                "required": ["reason", "spam_type"]
            }
        },
        "required": ["decision"]
    }
}'
```

### 도구와 구조화된 출력 결합

기본 제공 도구를 구조화된 출력과 결합하여 도구에서 검색한 정보를 기반으로 신뢰할 수 있는 JSON 객체를 가져옵니다.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal, Union

client = genai.Client()

class SpamDetails(BaseModel):
    reason: str = Field(description="The reason why the content is considered spam.")
    spam_type: Literal["phishing", "scam", "unsolicited promotion", "other"]

class NotSpamDetails(BaseModel):
    summary: str = Field(description="A brief summary of the content.")
    is_safe: bool = Field(description="Whether the content is safe for all audiences.")

class ModerationResult(BaseModel):
    decision: Union[SpamDetails, NotSpamDetails]

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Moderate the following content: 'Congratulations! You've won a free cruise. Click here to claim your prize: www.definitely-not-a-scam.com'",
    response_format=ModerationResult.model_json_schema(),
    tools=[{"type": "url_context"}]
)

parsed_output = ModerationResult.model_validate_json(interaction.outputs[-1].text)
print(parsed_output)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import { z } from 'zod'; // Assuming zod is used for schema generation, or define manually
const client = new GoogleGenAI({});

const obj = z.object({
    winning_team: z.string(),
    score: z.string(),
});
const schema = z.toJSONSchema(obj);

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Who won the last euro?',
    tools: [{ type: 'google_search' }],
    response_format: schema,
});
console.log(interaction.outputs[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the last euro?",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "object",
        "properties": {
            "winning_team": {"type": "string"},
            "score": {"type": "string"}
        }
    }
}'
```

## 고급 기능

또한 Interactions API를 사용할 때 더 많은 유연성을 제공하는 고급 기능도 있습니다.

### 스트리밍

생성되는 대로 점진적으로 응답을 수신합니다.

`stream=true`인 경우 최종 `interaction.complete` 이벤트의 `outputs` 필드에 생성된 콘텐츠가 포함되지 않습니다. 사용 메타데이터와 최종 상태만 포함합니다. 전체 응답 또는 도구 호출 인수를 재구성하려면 클라이언트 측에서 `content.delta` 이벤트를 집계해야 합니다.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain quantum entanglement in simple terms.",
    stream=True
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
        elif chunk.delta.type == "thought_summary":
            print(getattr(chunk.delta.content, "text", ""), end="", flush=True)
    elif chunk.event_type == "interaction.complete":
        print(f"\n\n--- Stream Finished ---")
        print(f"Total Tokens: {chunk.interaction.usage.total_tokens}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Explain quantum entanglement in simple terms.',
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text' && 'text' in chunk.delta) {
            process.stdout.write(chunk.delta.text);
        } else if (chunk.delta.type === 'thought_summary' && chunk.delta.content) {
            process.stdout.write(chunk.delta.content.text || '');
        }
    } else if (chunk.event_type === 'interaction.complete') {
        console.log('\n\n--- Stream Finished ---');
        console.log(`Total Tokens: ${chunk.interaction.usage.total_tokens}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Explain quantum entanglement in simple terms.",
    "stream": true
}'
```

#### 스트리밍 이벤트 유형

스트리밍이 사용 설정되면 API는 서버 전송 이벤트 (SSE)를 반환합니다. 각 이벤트에는 목적을 나타내는 `event_type` 필드가 있습니다. 이벤트 유형의 전체 목록은 [API 참조](https://ai.google.dev/gemini-api/docs/API 참조)에서 확인할 수 있습니다.

| 이벤트 유형 | 설명 |
| --- | --- |
| `interaction.start` | 첫 번째 이벤트입니다. 상호작용 `id`과 초기 `status` (`in_progress`)을 포함합니다. |
| `interaction.status_update` | 상태 변경 (예: `in_progress`)을 나타냅니다. |
| `content.start` | 새 출력 블록의 시작을 표시합니다. `index` 및 콘텐츠 `type` (예: `text`, `thought`)이 포함됩니다. |
| `content.delta` | 증분 콘텐츠 업데이트 `delta.type`로 키가 지정된 부분 데이터를 포함합니다. |
| `content.stop` | `index`에서 출력 블록의 끝을 표시합니다. |
| `interaction.complete` | 최종 이벤트입니다. `id`, `status`, `usage`, 메타데이터를 포함합니다. **참고:** `outputs`는 `None`이므로 `content.*` 이벤트에서 출력을 재구성해야 합니다. |
| `error` | 오류가 발생했음을 나타냅니다. `error.code` 및 `error.message`를 포함합니다. |

#### 스트리밍 이벤트에서 상호작용 객체 재구성

비스트리밍 응답과 달리 스트리밍 응답에는 `outputs` 배열이 포함되지 **않습니다**. `content.delta` 이벤트의 콘텐츠를 누적하여 출력을 재구성해야 합니다.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Write a haiku about Python programming.",
    stream=True
)

# Accumulate outputs by index
outputs = {}
usage = None

for chunk in stream:
    if chunk.event_type == "content.start":
        outputs[chunk.index] = {"type": chunk.content.type}

    elif chunk.event_type == "content.delta":
        output = outputs[chunk.index]
        if chunk.delta.type == "text":
            output["text"] = output.get("text", "") + chunk.delta.text
        elif chunk.delta.type == "thought_signature":
            output["signature"] = chunk.delta.signature
        elif chunk.delta.type == "thought_summary":
            output["summary"] = output.get("summary", "") + getattr(chunk.delta.content, "text", "")

    elif chunk.event_type == "interaction.complete":
        usage = chunk.interaction.usage

# Final outputs list (sorted by index)
final_outputs = [outputs[i] for i in sorted(outputs.keys())]
print(f"\n\nOutputs: {final_outputs}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Write a haiku about Python programming.',
    stream: true,
});

// Accumulate outputs by index
const outputs = new Map();
let usage = null;

for await (const chunk of stream) {
    if (chunk.event_type === 'content.start') {
        outputs.set(chunk.index, { type: chunk.content.type });

    } else if (chunk.event_type === 'content.delta') {
        const output = outputs.get(chunk.index);
        if (chunk.delta.type === 'text') {
            output.text = (output.text || '') + chunk.delta.text;
            process.stdout.write(chunk.delta.text);
        } else if (chunk.delta.type === 'thought_signature') {
            output.signature = chunk.delta.signature;
        } else if (chunk.delta.type === 'thought_summary') {
            output.summary = (output.summary || '') + (chunk.delta.content?.text || '');
        }

    } else if (chunk.event_type === 'interaction.complete') {
        usage = chunk.interaction.usage;
    }
}

// Final outputs list (sorted by index)
const finalOutputs = [...outputs.entries()]
    .sort((a, b) => a[0] - b[0])
    .map(([_, output]) => output);
console.log(`\n\nOutputs:`, finalOutputs);
```

#### 스트리밍 도구 호출

스트리밍과 함께 도구를 사용하면 모델은 스트림에서 `content.delta` 이벤트 시퀀스로 함수 호출을 생성합니다. 텍스트와 달리 도구 인수는 단일 `content.delta` 이벤트 내에서 완전한 JSON 객체로 제공됩니다. 스트리밍 중에 `interaction.complete` 이벤트에서 `outputs` 배열이 비어 있으므로 아래와 같이 델타에서 도구 호출을 캡처해야 합니다.

### Python

```
from google import genai
import json

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state"}
        },
        "required": ["location"]
    }
}

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the weather in Paris?",
    tools=[weather_tool],
    stream=True
)

# A map to capture tool calls by their ID as they arrive
function_calls = {}

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text" and chunk.delta.text:
            print(chunk.delta.text, end="", flush=True)

        elif chunk.delta.type == "function_call":
            print(f"\nExecuting {chunk.delta.name} immediately...")
            # result = my_tools[chunk.delta.name](https://ai.google.dev/gemini-api/docs/chunk.delta.name)
            function_calls[chunk.delta.id] = chunk.delta

    elif chunk.event_type == "interaction.complete":
        print("\n\nAll tools executed. Stream finished.")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state' }
        },
        required: ['location']
    }
};

const stream = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'What is the weather in Paris?',
    tools: [weatherTool],
    stream: true,
});

const toolCalls = new Map();

for await (const chunk of stream) {
    if (chunk.event_type === 'content.delta') {
        if (chunk.delta.type === 'text' && chunk.delta.text) {
            process.stdout.write(chunk.delta.text);

        } else if (chunk.delta.type === 'function_call') {
            console.log(`\nExecuting ${chunk.delta.name} immediately...`);
            // const result = myTools[chunk.delta.name](https://ai.google.dev/gemini-api/docs/chunk.delta.name);
            toolCalls.set(chunk.delta.id, chunk.delta);
        }
    } else if (chunk.event_type === 'interaction.complete') {
        console.log('\n\nAll tools executed. Stream finished.');
    }
}
```

### REST

```
# When streaming via SSE, capture function_call data from content.delta events.
# The 'arguments' field arrives as a complete JSON object once generated.

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

### 구성

`generation_config`로 모델의 동작을 맞춤설정합니다.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a story about a brave knight.",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 500,
        "thinking_level": "low",
    }
)

print(interaction.outputs[-1].text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Tell me a story about a brave knight.',
    generation_config: {
        temperature: 0.7,
        max_output_tokens: 500,
        thinking_level: 'low',
    }
});

console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Tell me a story about a brave knight.",
    "generation_config": {
        "temperature": 0.7,
        "max_output_tokens": 500,
        "thinking_level": "low"
    }
}'
```

### 생각 중

Gemini 2.5 이상의 모델은 대답을 생성하기 전에 '사고'라는 내부 추론 프로세스를 사용합니다. 이를 통해 모델은 수학, 코딩, 다단계 추론과 같은 복잡한 작업에 대해 더 나은 대답을 생성할 수 있습니다.

#### 사고 수준

`thinking_level` 파라미터를 사용하면 모델의 추론 깊이를 제어할 수 있습니다.

| 수준 | 설명 | 지원되는 모델 |
| --- | --- | --- |
| `minimal` | 대부분의 질문에 대해 '생각하지 않음' 설정과 일치합니다. 경우에 따라 모델이 매우 최소한으로만 생각할 수 있습니다. 지연 시간과 비용을 최소화합니다. | **Flash 모델만 해당**   (예: Gemini 3 Flash) |
| `low` | 간단한 안내 따르기 및 채팅을 위해 지연 시간과 비용 절감을 우선시하는 가벼운 추론 | **모든 사고 모델** |
| `medium` | 대부분의 작업에 균형 잡힌 사고를 제공합니다. | **Flash 모델만 해당**   (예: Gemini 3 Flash) |
| `high` | **(기본값)** 추론 깊이를 극대화합니다. 모델이 첫 번째 토큰에 도달하기까지 시간이 더 오래 걸릴 수 있지만, 출력은 더 신중하게 추론됩니다. | **모든 사고 모델** |

#### 사고 요약

모델의 사고는 응답 출력에 **사고 블록** (`type: "thought"`)으로 표시됩니다. `thinking_summaries` 매개변수를 사용하여 사고 과정의 인간이 읽을 수 있는 요약을 수신할지 여부를 제어할 수 있습니다.

| 값 | 설명 |
| --- | --- |
| `auto` | **(기본값)** 사용 가능한 경우 생각 요약을 반환합니다. |
| `none` | 생각 요약을 사용 중지합니다. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Solve this step by step: What is 15% of 240?",
    generation_config={
        "thinking_level": "high",
        "thinking_summaries": "auto"
    }
)

for output in interaction.outputs:
    if output.type == "thought":
        print(f"Thinking: {output.summary}")
    elif output.type == "text":
        print(f"Answer: {output.text}")
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Solve this step by step: What is 15% of 240?',
    generation_config: {
        thinking_level: 'high',
        thinking_summaries: 'auto'
    }
});

for (const output of interaction.outputs) {
    if (output.type === 'thought') {
        console.log(`Thinking: ${output.summary}`);
    } else if (output.type === 'text') {
        console.log(`Answer: ${output.text}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": "Solve this step by step: What is 15% of 240?",
    "generation_config": {
        "thinking_level": "high",
        "thinking_summaries": "auto"
    }
}'
```

모든 사고 블록에는 `signature` 필드 (내부 추론 상태의 암호화 해시)와 선택적 `summary` 필드 (모델의 추론에 관한 사람이 읽을 수 있는 요약)가 포함됩니다. `signature`는 항상 표시되지만 다음과 같은 경우 생각 블록에 요약 없이 서명만 포함될 수 있습니다.

- **간단한 요청**: 모델이 요약을 생성할 만큼 충분히 추론하지 않았습니다.
- **`thinking_summaries: "none"`**: 요약이 명시적으로 사용 중지됨

코드는 항상 `summary`가 비어 있거나 없는 경우 생각 블록을 처리해야 합니다. 대화 기록을 수동으로 관리하는 경우 (스테이트리스 모드) 진위 여부를 검증하기 위해 후속 요청에 서명이 포함된 생각 블록을 포함해야 합니다.

### 파일 작업

#### 원격 파일 작업

API 호출에서 원격 URL을 직접 사용하여 파일에 액세스합니다.

### Python

```
from google import genai
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "image",
            "uri": "https://github.com/<github-path>/cats-and-dogs.jpg",
        },
        {"type": "text", "text": "Describe what you see."}
    ],
)
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        {
            type: 'image',
            uri: 'https://github.com/<github-path>/cats-and-dogs.jpg',
        },
        { type: 'text', text: 'Describe what you see.' }
    ],
});
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {
            "type": "image",
            "uri": "https://github.com/<github-path>/cats-and-dogs.jpg"
        },
        {"type": "text", "text": "Describe what you see."}
    ]
}'
```

#### Gemini Files API 사용

파일을 사용하기 전에 Gemini [Files API](https://ai.google.dev/gemini-api/docs/Files API)에 업로드합니다.

### Python

```
from google import genai
import time
import requests
client = genai.Client()

# 1. Download the file
url = "https://github.com/philschmid/gemini-samples/raw/refs/heads/main/assets/cats-and-dogs.jpg"
response = requests.get(url)
with open("cats-and-dogs.jpg", "wb") as f:
    f.write(response.content)

# 2. Upload to Gemini Files API
file = client.files.upload(file="cats-and-dogs.jpg")

# 3. Wait for processing
while client.files.get(name=file.name).state != "ACTIVE":
    time.sleep(2)

# 4. Use in Interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "image",
            "uri": file.uri,
        },
        {"type": "text", "text": "Describe what you see."}
    ],
)
for output in interaction.outputs:
    if output.type == "text":
        print(output.text)
```

### 자바스크립트

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';
import fetch from 'node-fetch';
const client = new GoogleGenAI({});

// 1. Download the file
const url = 'https://github.com/philschmid/gemini-samples/raw/refs/heads/main/assets/cats-and-dogs.jpg';
const filename = 'cats-and-dogs.jpg';
const response = await fetch(url);
const buffer = await response.buffer();
fs.writeFileSync(filename, buffer);

// 2. Upload to Gemini Files API
const myfile = await client.files.upload({ file: filename, config: { mimeType: 'image/jpeg' } });

// 3. Wait for processing
while ((await client.files.get({ name: myfile.name })).state !== 'ACTIVE') {
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// 4. Use in Interaction
const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
        { type: 'image', uri: myfile.uri, },
        { type: 'text', text: 'Describe what you see.' }
    ],
});
for (const output of interaction.outputs) {
    if (output.type === 'text') {
        console.log(output.text);
    }
}
```

### REST

```
# 1. Upload the file (Requires File API setup)
# See https://ai.google.dev/gemini-api/docs/files for details.
# Assume FILE_URI is obtained from the upload step.

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3-flash-preview",
    "input": [
        {"type": "image", "uri": "FILE_URI"},
        {"type": "text", "text": "Describe what you see."}
    ]
}'
```

### 유연한 추론 및 우선순위 추론 티어

상호작용 API와 함께 추론 티어를 사용하여 다양한 워크로드 요구사항에 맞게 최적화할 수 있습니다.

- 비용 최적화를 위한 [Flex](https://ai.google.dev/gemini-api/docs/Flex) (`flex`): 표준 가격에서 50% 할인
- 지연 시간 최적화를 위한 [우선순위](https://ai.google.dev/gemini-api/docs/우선순위) (`priority`)입니다. 가장 높은 신뢰성 서비스 등급입니다.

### Python

```
import google.genai as genai

client = genai.Client()

try:
    interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input="Analyze this dataset for trends...",
        service_tier='flex'
    )
    print(interaction.outputs[-1].text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### 자바스크립트

```
 import { GoogleGenAI } from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const interaction = await client.interactions.create({
             model: 'gemini-3-flash-preview',
             input: 'Analyze this dataset for trends...',
             service_tier: 'flex'
         });
         console.log(interaction.outputs[interaction.outputs.length - 1].text);
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }
 }
 await main();
```

### REST

```
 curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
 -H "Content-Type: application/json" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -d '{
     "model": "gemini-3-flash-preview",
     "input": "Analyze this dataset for trends...",
     "service_tier": "flex"
 }'
```

### 데이터 모델

[API 참조](https://ai.google.dev/gemini-api/docs/API 참조)에서 데이터 모델에 대해 자세히 알아보세요. 다음은 주요 구성요소를 간략하게 설명한 것입니다.

#### 상호작용

| 속성 | 유형 | 설명 |
| --- | --- | --- |
| `id` | `string` | 상호작용의 고유 식별자입니다. |
| `model`/`agent` | `string` | 사용된 모델 또는 에이전트입니다. 하나만 제공할 수 있습니다. |
| `input` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=ko#data-models) | 제공된 입력입니다. |
| `outputs` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=ko#data-models) | 모델의 대답입니다. |
| `tools` | [`Tool[]`](https://ai.google.dev/api/interactions-api?hl=ko#Resource:Tool) | 사용된 도구입니다. |
| `previous_interaction_id` | `string` | 컨텍스트의 이전 상호작용 ID입니다. |
| `stream` | `boolean` | 상호작용이 스트리밍인지 여부입니다. |
| `status` | `string` | 상태: `completed`, `in_progress`, `requires_action`, `failed` 등 |
| `background` | `boolean` | 상호작용이 백그라운드 모드에 있는지 여부입니다. |
| `store` | `boolean` | 상호작용을 저장할지 여부입니다. 기본값: `true` `false`로 설정하여 선택 해제합니다. |
| `usage` | [사용 정보](https://ai.google.dev/gemini-api/docs/사용 정보) | 상호작용 요청의 토큰 사용량입니다. |

## 지원되는 모델 및 에이전트

| 모델 이름 | 유형 | 모델 ID |
| --- | --- | --- |
| Gemini 3.1 Flash-Lite 프리뷰 | 모델 | `gemini-3.1-flash-lite-preview` |
| Gemini 3.1 Pro 프리뷰 | 모델 | `gemini-3.1-pro-preview` |
| Gemini 3 Flash 프리뷰 | 모델 | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | 모델 | `gemini-2.5-pro` |
| Gemini 2.5 Flash | 모델 | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | 모델 | `gemini-2.5-flash-lite` |
| Lyria 3 클립 미리보기 | 모델 | `lyria-3-clip-preview` |
| Lyria 3 Pro 미리보기 | 모델 | `lyria-3-pro-preview` |
| Deep Research 미리보기 | 에이전트 | `deep-research-pro-preview-12-2025` |
| Deep Research 미리보기 | 에이전트 | `deep-research-preview-04-2026` |
| Deep Research 미리보기 | 에이전트 | `deep-research-max-preview-04-2026` |

## Interactions API 작동 방식

Interactions API는 중앙 리소스인 [**`Interaction`**](https://ai.google.dev/gemini-api/docs/**`Interaction`**)를 중심으로 설계되었습니다.
`Interaction`는 대화 또는 작업의 완전한 턴을 나타냅니다. 모든 사용자 입력, 모델 생각, 도구 호출, 도구 결과, 최종 모델 출력을 비롯한 전체 상호작용 기록이 포함된 세션 레코드 역할을 합니다.

[`interactions.create`](https://ai.google.dev/gemini-api/docs/`interactions.create`)에 대한 호출을 하면 새 `Interaction` 리소스가 생성됩니다.

### 서버 측 상태 관리

`previous_interaction_id` 매개변수를 사용하여 후속 호출에서 완료된 상호작용의 `id`를 사용하여 대화를 계속할 수 있습니다. 서버는 이 ID를 사용하여 대화 기록을 가져오므로 전체 채팅 기록을 다시 전송하지 않아도 됩니다.

대화 기록 (입력 및 출력)만 `previous_interaction_id`를 사용하여 보존됩니다. 다른 매개변수는 **상호작용 범위**이며 현재 생성 중인 특정 상호작용에만 적용됩니다.

- `tools`
- `system_instruction`
- `generation_config` (`thinking_level`, `temperature` 등 포함)

즉, 이러한 매개변수를 적용하려면 새 상호작용마다 다시 지정해야 합니다. 이 서버 측 상태 관리는 선택사항입니다. 각 요청에서 전체 대화 기록을 전송하여 상태 비저장 모드로 작동할 수도 있습니다.

### 데이터 스토리지 및 보관

기본적으로 모든 상호작용 객체는 서버 측 상태 관리 기능 (`previous_interaction_id` 사용), 백그라운드 실행 (`background=true` 사용), 모니터링 가능성 목적의 사용을 간소화하기 위해 저장 (`store=true`)됩니다.

- **유료 등급**: 상호작용은 **55일** 동안 보관됩니다.
- **무료 등급**: 상호작용이 **1일** 동안 보관됩니다.

이를 원치 않는 경우 요청에서 `store=false`를 설정하면 됩니다. 이 컨트롤은 상태 관리와 별개입니다. 모든 상호작용에 대해 저장소를 선택 해제할 수 있습니다. 하지만 `store=false`는 `background=true`과 호환되지 않으며 후속 턴에 `previous_interaction_id`를 사용하는 것을 방지합니다.

[API 참조](https://ai.google.dev/gemini-api/docs/API 참조)에 있는 삭제 메서드를 사용하여 언제든지 저장된 상호작용을 삭제할 수 있습니다. 상호작용 ID를 알고 있는 경우에만 상호작용을 삭제할 수 있습니다.

보관 기간이 만료되면 데이터가 자동으로 삭제됩니다.

상호작용 객체는 [약관](https://ai.google.dev/gemini-api/docs/약관)에 따라 처리됩니다.

## 권장사항

- **캐시 적중률**: `previous_interaction_id`를 사용하여 대화를 계속하면 시스템에서 대화 기록에 대한 암시적 캐싱을 더 쉽게 활용할 수 있으므로 성능이 개선되고 비용이 절감됩니다.
- **상호작용 혼합**: 대화 내에서 에이전트와 모델 상호작용을 자유롭게 혼합할 수 있습니다. 예를 들어 Deep Research 에이전트와 같은 전문 에이전트를 사용하여 초기 데이터 수집을 수행한 다음 표준 Gemini 모델을 사용하여 요약 또는 재포맷과 같은 후속 작업을 수행하여 이러한 단계를 `previous_interaction_id`와 연결할 수 있습니다.

## SDK

최신 버전의 Google 생성형 AI SDK를 사용하여 Interactions API에 액세스할 수 있습니다.

- Python에서는 `1.55.0` 버전부터 `google-genai` 패키지입니다.
- JavaScript에서는 `1.33.0` 버전부터 `@google/genai` 패키지입니다.

[라이브러리](https://ai.google.dev/gemini-api/docs/라이브러리) 페이지에서 SDK를 설치하는 방법을 자세히 알아보세요.

## 제한사항

- **베타 상태**: Interactions API는 베타/미리보기 상태입니다. 기능과 스키마는 변경될 수 있습니다.
- **원격 MCP**: Gemini 3는 원격 MCP를 지원하지 않습니다. 곧 지원될 예정입니다.

## 브레이킹 체인지

Interactions API는 현재 초기 베타 단계입니다. Google은 실제 사용량과 개발자 의견을 기반으로 API 기능, 리소스 스키마, SDK 인터페이스를 적극적으로 개발하고 개선하고 있습니다.

따라서 **브레이킹 체인지가 발생할 수 있습니다**.
업데이트에는 다음 항목의 변경사항이 포함될 수 있습니다.

- 입력 및 출력 스키마입니다.
- SDK 메서드 서명 및 객체 구조
- 구체적인 기능 동작입니다.

프로덕션 워크로드의 경우 표준 [`generateContent`](https://ai.google.dev/gemini-api/docs/`generateContent`) API를 계속 사용해야 합니다. 안정적인 배포를 위한 권장 경로로 유지되며 계속 적극적으로 개발되고 유지관리됩니다.

## 의견

여러분의 의견은 Interactions API 개발에 매우 중요합니다.
[Google AI 개발자 커뮤니티 포럼](https://ai.google.dev/gemini-api/docs/Google AI 개발자 커뮤니티 포럼)에서 의견을 공유하거나 버그를 신고하거나 기능을 요청하세요.

## 다음 단계

- [Interactions API 빠른 시작 노트북](https://ai.google.dev/gemini-api/docs/Interactions API 빠른 시작 노트북)을 사용해 보세요.
- [Gemini Deep Research Agent](https://ai.google.dev/gemini-api/docs/Gemini Deep Research Agent)에 대해 자세히 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0 라이선스)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://ai.google.dev/gemini-api/docs/Apache 2.0 라이선스)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://ai.google.dev/gemini-api/docs/Google Developers 사이트 정책)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?
