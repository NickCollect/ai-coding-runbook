---
source_url: https://ai.google.dev/gemini-api/docs/interactions?hl=pl
fetched_at: 2026-05-05T20:05:34.465654+00:00
title: "Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interactions API

Interfejs Interactions API ([beta](https://ai.google.dev/gemini-api/docs/api-versions?hl=pl)) to ujednolicony interfejs do korzystania z modeli i agentów Gemini. Jest to ulepszona alternatywa dla interfejsu [`generateContent`](https://ai.google.dev/api/generate-content?hl=pl#method:-models.generatecontent)API, która upraszcza zarządzanie stanem, koordynację narzędzi i długotrwałe zadania. Szczegółowy widok schematu interfejsu API znajdziesz w [dokumentacji API](https://ai.google.dev/api/interactions-api?hl=pl). W okresie testów beta funkcje i schematy mogą ulec [istotnym zmianom](#breaking-changes).
Aby szybko rozpocząć, wypróbuj [notatnik z krótkim wprowadzeniem do interfejsu Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=pl).

Ogólne zastosowanie
Wywoływanie funkcji
Agent Deep Research

Poniższy przykład pokazuje, jak wywołać interfejs Interactions API za pomocą prompta tekstowego.

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

### JavaScript

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

## Podstawowe interakcje

Interfejs Interactions API jest dostępny w ramach naszych [dotychczasowych pakietów SDK](#sdk). Najprostszym sposobem interakcji z modelem jest podanie prompta tekstowego. `input` może być ciągiem znaków, listą zawierającą obiekty treści lub listą tur z rolami i obiektami treści.

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

### JavaScript

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

## Rozmowa

Rozmowy wieloetapowe możesz tworzyć na 2 sposoby:

- z zachowaniem stanu przez odniesienie do poprzedniej interakcji,
- bezstanowo, przez podanie całej historii rozmowy;

### Rozmowa z zachowaniem stanu

Aby kontynuować rozmowę, przekaż parametr `id` z poprzedniej interakcji do parametru `previous_interaction_id`. Interfejs API zapamiętuje historię rozmowy, więc musisz tylko wysłać nowe dane wejściowe. Szczegółowe informacje o tym, które pola są dziedziczone, a które należy określić ponownie, znajdziesz w sekcji [Zarządzanie stanem po stronie serwera](#server-side-state).

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

### JavaScript

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

#### Pobieranie poprzednich interakcji stanowych

Używanie interakcji `id` do pobierania poprzednich tur rozmowy.

### Python

```
previous_interaction = client.interactions.get("<YOUR_INTERACTION_ID>")

print(previous_interaction)
```

### JavaScript

```
const previous_interaction = await client.interactions.get("<YOUR_INTERACTION_ID>");
console.log(previous_interaction);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/<YOUR_INTERACTION_ID>" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

#### Uwzględnij pierwotne dane wejściowe

Domyślnie funkcja `interactions.get()` zwraca tylko wyniki modelu. Aby uwzględnić w odpowiedzi oryginalne znormalizowane dane wejściowe, ustaw wartość `include_input` na `true`.

### Python

```
interaction = client.interactions.get(
    "<YOUR_INTERACTION_ID>",
    include_input=True
)

print(f"Input: {interaction.input}")
print(f"Output: {interaction.outputs}")
```

### JavaScript

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

### Rozmowa bezstanowa

Historią rozmów możesz zarządzać ręcznie po stronie klienta.

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

### JavaScript

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

## Możliwości multimodalne

Interfejsu Interactions API możesz używać w przypadku zastosowań multimodalnych, takich jak rozpoznawanie obrazów czy generowanie filmów.

### Rozpoznawanie multimodalne

Dane multimodalne możesz podać w formie zakodowanej w formacie base64 w treści, używając interfejsu Files API w przypadku większych plików lub przekazując publicznie dostępny link w polu uri. W przykładach kodu poniżej pokazujemy metodę publicznego adresu URL.

#### Rozpoznawanie obrazów

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

### JavaScript

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

#### Rozpoznawanie dźwięku

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

### JavaScript

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

#### Rozpoznawanie filmów

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

### JavaScript

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

#### Rozumienie dokumentów (PDF)

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

### JavaScript

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

### Generowanie multimodalne

Za pomocą interfejsu API interakcji możesz generować dane wyjściowe w różnych formatach.

#### Generowanie obrazów

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

### JavaScript

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

##### Konfigurowanie danych wyjściowych obrazu

Wygenerowane obrazy możesz dostosowywać za pomocą `image_config` w `generation_config`, aby kontrolować proporcje i rozdzielczość.

| Parametr | Opcje | Opis |
| --- | --- | --- |
| `aspect_ratio` | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` | Określa stosunek szerokości do wysokości obrazu wyjściowego. |
| `image_size` | `1k`, `2k`, `4k` | Ustawia rozdzielczość obrazu wyjściowego. |

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

### JavaScript

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

#### Generowanie mowy

Generowanie naturalnie brzmiącej mowy na podstawie tekstu za pomocą modelu zamiany tekstu na mowę (TTS).
Skonfiguruj ustawienia głosu, języka i głośnika za pomocą parametru `speech_config`.

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

### JavaScript

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

TTS nie obsługuje strumieniowego przesyłania danych.

##### Generowanie mowy wielu rozmówców

Generuj mowę z udziałem wielu osób, podając ich imiona w prompcie i dopasowując je w `speech_config`.

Prompt powinien zawierać imiona mówców:

```
TTS the following conversation between Alice and Bob:
Alice: Hi Bob, how are you doing today?
Bob: I'm doing great, thanks for asking! How about you?
Alice: Fantastic! I just learned about the Gemini API.
```

Następnie skonfiguruj `speech_config` z pasującymi głośnikami:

```
"generation_config": {
    "speech_config": [
        {"voice": "Zephyr", "speaker": "Alice", "language": "en-US"},
        {"voice": "Puck", "speaker": "Bob", "language": "en-US"}
    ]
}
```

#### Generowanie muzyki

Generuj wysokiej jakości muzykę na podstawie promptów tekstowych za pomocą modeli Lyria 3. Interfejs Interactions API obsługuje zarówno krótkie klipy, jak i pełne utwory z wokalem, tekstem i aranżacją instrumentalną.

Pełny przewodnik po generowaniu muzyki, w tym niestandardowych tekstów, kontroli czasu trwania i przekształcania obrazów w muzykę, znajdziesz w artykule [Generowanie muzyki za pomocą Lyrii 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl).

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

### JavaScript

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

W przypadku pełnych utworów (do ok. 4 minut) użyj modelu `lyria-3-pro-preview`:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. "
          "Starts with a solo piano intro, builds through sweeping "
          "strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

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

## Możliwości agentowe

Interfejs Interactions API jest przeznaczony do tworzenia agentów i interakcji z nimi. Obsługuje wywoływanie funkcji, wbudowane narzędzia, dane wyjściowe o strukturze oraz protokół Model Context Protocol (MCP).

### Agenty

Do wykonywania złożonych zadań możesz używać specjalistycznych agentów, takich jak `deep-research-preview-04-2026`. Więcej informacji o agencie Deep Research w Gemini znajdziesz w przewodniku [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).

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

### JavaScript

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

### Narzędzia i wywoływanie funkcji

W tej sekcji wyjaśniamy, jak używać wywoływania funkcji do definiowania narzędzi niestandardowych oraz jak korzystać z wbudowanych narzędzi Google w ramach interfejsu Interactions API.

#### Wywoływanie funkcji

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

### JavaScript

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

##### Wywoływanie funkcji ze stanem po stronie klienta

Jeśli nie chcesz używać stanu po stronie serwera, możesz zarządzać nim w całości po stronie klienta.

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

### JavaScript

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

##### Wyniki funkcji multimodalnych

Pole `result` w obiekcie `function_result` akceptuje zwykły ciąg znaków lub tablicę obiektów `TextContent` i `ImageContent`. Dzięki temu możesz zwracać obrazy, takie jak zrzuty ekranu lub wykresy, wraz z tekstem z wywołań funkcji, aby model mógł analizować dane wyjściowe wizualne.

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

### JavaScript

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

#### Wbudowane narzędzia

Gemini ma wbudowane narzędzia, takie jak [powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), [powiązanie ze źródłem informacji przy użyciu wyszukiwarki obrazów Google](#image-search-grounding), [powiązanie ze źródłem informacji przy użyciu Map Google](#grounding-with-google-maps), [wykonywanie kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl), [kontekst adresu URL](https://ai.google.dev/gemini-api/docs/url-context?hl=pl) i [korzystanie z komputera](https://ai.google.dev/gemini-api/docs/computer-use?hl=pl).

##### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google

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

### JavaScript

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

##### Powiązanie ze źródłem informacji przy użyciu wyszukiwarki grafiki Google (tylko w przypadku Gemini 3.1 Flash Image)

Uziemienie za pomocą wyszukiwarki grafiki Google umożliwia modelom wykorzystywanie obrazów z internetu pobranych za pomocą wyszukiwarki grafiki Google jako kontekstu wizualnego do generowania obrazów. Wyszukiwanie obrazów to nowy typ wyszukiwania w ramach istniejącego narzędzia Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google, który działa równolegle ze standardowym [wyszukiwaniem w internecie](#grounding-with-google-search).

###### Włączanie wyszukiwania obrazów

Aby poprosić o wyniki w postaci obrazów, dodaj `"image_search"` do tablicy `search_types` w przypadku narzędzia `google_search`.

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

### JavaScript

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

###### Wymagania dotyczące obowiązkowego wyświetlania

Aby zachować zgodność z [Warunkami korzystania z usługi wyszukiwarka Google](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-search), interfejs użytkownika musi implementować 2 różne poziomy atrybucji:

1. **Atrybucja w wyszukiwarce Google**

   Musisz wyświetlać sugestie wyszukiwania „Sprawdź w Google” podane w bloku `google_search_result`.

   - **Pole:** `rendered_content` (HTML/CSS)
   - **Działanie:** wyświetl ten element w pobliżu odpowiedzi modelu w niezmienionej formie.
2. **Atrybucja wydawcy**

   W przypadku każdego wyświetlanego obrazu musisz podać link do „strony zawierającej” (strony docelowej).

   - **Pole:** `url` (znajduje się w tablicy `result`)
   - **Wymaganie:** musisz zapewnić bezpośrednią ścieżkę do strony źródłowej zawierającej obraz, która wymaga tylko jednego kliknięcia. Korzystanie z pośrednich przeglądarek obrazów lub ścieżek wymagających wielu kliknięć jest niedozwolone.

###### Obsługa odpowiedzi opartej na faktach

Poniższy fragment kodu pokazuje, jak obsługiwać przeplatane bloki odpowiedzi w przypadku nieprzetworzonych danych obrazu i obowiązkowego atrybutu.

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

### JavaScript

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

###### Oczekiwany schemat wyjściowy

**Blok obrazu** (typ: `"image"`) zawiera nieprzetworzone dane wizualne wygenerowane lub pobrane przez model.

```
{
  "type": "image",
  "mime_type": "image/png",
  "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..." // Base64 content
}
```

**Blok wyników** (typ: `"google_search_result"`) zawiera obowiązkowe metadane atrybucji powiązane z wyszukiwaniem.

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

##### Grounding z użyciem Map Google

Powiązanie ze źródłem informacji przy użyciu Map Google umożliwia modelom korzystanie z danych Map Google w celu uzyskiwania kontekstu wizualnego, pinezek na mapie i odkrywania informacji na podstawie lokalizacji.

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

### JavaScript

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

###### Wymagania dotyczące korzystania z usługi

Podczas prezentowania wyników powiązania ze źródłem informacji przy użyciu Map Google musisz przestrzegać [Warunków korzystania z usługi Mapy Google](https://ai.google.dev/gemini-api/terms?hl=pl#grounding-with-google-maps).
Musisz poinformować użytkowników o tych wymaganiach dotyczących wyświetlania i je spełniać:

- **Poinformuj użytkownika:** natychmiast po wygenerowaniu treści podaj powiązane źródła w Mapach Google. Źródła muszą być widoczne w ramach jednej interakcji użytkownika.
- **Wyświetl linki:** wygeneruj podgląd linku dla każdego źródła (w tym fragmenty opinii, jeśli są dostępne).
- **Atrybucja do „Map Google”:** postępuj zgodnie z [wskazówkami dotyczącymi atrybucji tekstowej](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=pl#maps-attribution-guidelines).
- **Wyświetl tytuł źródła.**
- **Połącz się ze źródłem** za pomocą podanego adresu URL.
- **Wytyczne dotyczące atrybucji:** nie modyfikuj tekstu „Mapy Google” (wielkość liter, zawijanie). Zapobiegaj tłumaczeniu w przeglądarce za pomocą `translate="no"`.

###### Obsługa odpowiedzi

Poniższy fragment kodu pokazuje, jak przetworzyć odpowiedź, wyodrębniając tekst i cytaty w tekście (w tym fragmenty opinii), aby spełnić wymagania dotyczące wyświetlania.

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

### JavaScript

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

###### Oczekiwany schemat wyjściowy

Podczas korzystania z powiązania ze źródłem informacji przy użyciu Map Google spodziewaj się następującego schematu danych wyjściowych.

**Blok wyników** (typ: `"google_maps_result"`) zawiera uporządkowane dane o miejscu.

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

**Blok tekstu** (typ: `"text"`) zawiera wygenerowane treści z adnotacjami wbudowanymi.

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

##### Wykonanie kodu

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

### JavaScript

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

##### Kontekst adresu URL

Ugruntowanie za pomocą kontekstu adresu URL umożliwia modelowi odczytywanie publicznych adresów URL podanych w prompcie lub na liście narzędzi.

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

### JavaScript

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

###### Obsługa odpowiedzi

Poniższy fragment kodu pokazuje, jak przetworzyć odpowiedź, wyodrębniając tekst i cytaty w tekście (typ `url_citation`).

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

### JavaScript

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

###### Oczekiwany schemat wyjściowy

Gdy używasz kontekstu adresu URL, oczekuj tego schematu danych wyjściowych.

**Blok wywołania** (typ: `"url_context_call"`) zawiera adres URL, który model próbował odczytać.

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

**Blok wyników** (typ: `"url_context_result"`) zawiera stan pobierania.

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

**Blok tekstu** zawiera wygenerowany tekst i cytaty w tekście.

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

##### Korzystanie z komputera

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

### JavaScript

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

###### Obsługa wyników funkcji Korzystanie z komputera

Narzędzie Computer Use to pętla po stronie klienta, więc musisz wykonać działanie (np. otworzyć przeglądarkę) i odesłać wynik do modelu. Wysyłając parametr `function_result` w przypadku działań takich jak `open_web_browser`, pamiętaj, aby przekazać odpowiedź URL na liście wyników, jak pokazano poniżej:

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

##### Wyszukiwanie plików

Ugruntowanie za pomocą wyszukiwania plików umożliwia modelowi wyszukiwanie przesłanych plików w magazynach wyszukiwania plików.

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

### JavaScript

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

###### Obsługa odpowiedzi

Poniższy fragment kodu pokazuje, jak przetworzyć odpowiedź, wyodrębniając tekst i cytaty w tekście (typ `file_citation`).

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

### JavaScript

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

###### Oczekiwany schemat wyjściowy

Podczas korzystania z wyszukiwania plików oczekuj następującego schematu danych wyjściowych.

**Blok połączenia** (typ: `"file_search_call"`) zawiera metadane połączenia.

```
{
  "type": "file_search_call",
  "id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

**Blok wyników** (typ: `"file_search_result"`) zawiera metadane wyniku.

```
{
  "type": "file_search_result",
  "call_id": "filesearch_001",
  "signature": "EkYKIGY5OT..."
}
```

**Blok tekstu** zawiera wygenerowany tekst i cytaty w tekście.

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

#### Łączenie wbudowanych narzędzi i wywoływania funkcji

Możesz używać [wbudowanych narzędzi i wywoływania funkcji](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl) w tym samym żądaniu.

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

### JavaScript

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

##### Informacje o rozpowszechnianiu kontekstu narzędzia

Modele Gemini 3 i nowsze obsługują **przekazywanie kontekstu narzędzia**, aby zachować niezawodną „pamięć” działań po stronie serwera. Gdy zostanie uruchomione wbudowane narzędzie (np. wyszukiwarka Google), interfejs API wygeneruje konkretne części `toolCall` i `toolResponse`. Zawierają one dokładny kontekst, którego model potrzebuje, aby w następnej turze uzasadnić te wyniki.

- **Stanowe (zalecane):** jeśli używasz `previous_interaction_id`, interfejs API automatycznie zarządza tym obiegiem.
- **Bezstanowy:** jeśli zarządzasz historią ręcznie, musisz uwzględnić te bloki w tablicy wejściowej dokładnie tak, jak zostały zwrócone przez interfejs API.

### Protokół kontekstu modelu zdalnego (MCP)

Integracja zdalnego [MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
upraszcza tworzenie agentów, ponieważ umożliwia interfejsowi Gemini API
bezpośrednie wywoływanie narzędzi zewnętrznych hostowanych na serwerach zdalnych.

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

### JavaScript

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

**Ważne informacje:**

- Zdalny MCP działa tylko z serwerami HTTP obsługującymi strumieniowanie (serwery SSE nie są obsługiwane).
- Zdalny MCP nie działa z modelami Gemini 3 (ta funkcja będzie dostępna wkrótce).
- Nazwy serwerów MCP nie powinny zawierać znaku „-” (zamiast tego używaj nazw serwerów w formacie snake\_case).

### Uporządkowane dane wyjściowe (schemat JSON)

Wymuś określone dane wyjściowe JSON, podając schemat JSON w parametrze `response_format`. Jest to przydatne w przypadku zadań takich jak moderowanie, klasyfikowanie czy wyodrębnianie danych.

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

### JavaScript

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

### Łączenie narzędzi i uporządkowanych danych wyjściowych

Łącz wbudowane narzędzia z uporządkowanymi danymi wyjściowymi, aby uzyskać wiarygodny obiekt JSON na podstawie informacji pobranych przez narzędzie.

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

### JavaScript

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

## Funkcje zaawansowane

Dostępne są też dodatkowe funkcje zaawansowane, które zapewniają większą elastyczność w korzystaniu z interfejsu Interactions API.

### Streaming

Otrzymuj odpowiedzi stopniowo w miarę ich generowania.

Gdy `stream=true`, ostatnie zdarzenie `interaction.complete` nie zawiera wygenerowanych treści w polu `outputs`. Zawiera tylko metadane dotyczące użytkowania i stan końcowy. Musisz agregować zdarzenia `content.delta` po stronie klienta, aby odtworzyć pełną odpowiedź lub argumenty wywołania narzędzia.

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

### JavaScript

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

#### Typy zdarzeń strumieniowania

Gdy strumieniowanie jest włączone, interfejs API zwraca zdarzenia wysyłane przez serwer (SSE). Każde zdarzenie ma pole `event_type` wskazujące jego przeznaczenie. Pełna lista typów zdarzeń jest dostępna w [dokumentacji API](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Interaction).

| Typ zdarzenia | Opis |
| --- | --- |
| `interaction.start` | Pierwsze zdarzenie. Zawiera interakcję `id` i początkową `status` (`in_progress`). |
| `interaction.status_update` | Wskazuje zmiany stanu (np. `in_progress`). |
| `content.start` | Oznacza początek nowego bloku wyjściowego. Zawiera `index` i treści `type` (np. `text`, `thought`). |
| `content.delta` | przyrostowe aktualizacje treści, Zawiera częściowe dane kluczowane przez `delta.type`. |
| `content.stop` | Oznacza koniec bloku wyjściowego w miejscu `index`. |
| `interaction.complete` | Ostatnie zdarzenie. Zawiera `id`, `status`, `usage` i metadane. **Uwaga:** `outputs` to `None` – musisz odtworzyć dane wyjściowe ze zdarzeń `content.*`. |
| `error` | Wskazuje, że wystąpił błąd. Zawiera `error.code` i `error.message`. |

#### Odtwarzanie obiektu Interaction na podstawie zdarzeń przesyłanych strumieniowo

W przeciwieństwie do odpowiedzi bez strumieniowania odpowiedzi strumieniowane **nie** zawierają tablicy `outputs`. Musisz odtworzyć dane wyjściowe, gromadząc treści z `content.delta` zdarzeń.

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

### JavaScript

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

#### Wywołania narzędzi do strumieniowania

Gdy korzystasz z narzędzi do przesyłania strumieniowego, model generuje wywołania funkcji jako sekwencję zdarzeń `content.delta` w strumieniu. W przeciwieństwie do tekstu argumenty narzędzia są dostarczane jako kompletne obiekty JSON w ramach jednego zdarzenia `content.delta`. Tablica
`outputs` jest pusta w zdarzeniu `interaction.complete` podczas przesyłania strumieniowego. Musisz rejestrować wywołania narzędzi z różnic, jak pokazano poniżej.

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
            # result = my_tools[chunk.delta.name](**chunk.delta.arguments)
            function_calls[chunk.delta.id] = chunk.delta

    elif chunk.event_type == "interaction.complete":
        print("\n\nAll tools executed. Stream finished.")
```

### JavaScript

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
            // const result = myTools[chunk.delta.name](chunk.delta.arguments);
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

### Konfiguracja

Dostosuj działanie modelu za pomocą `generation_config`.

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

### JavaScript

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

### Myślę

Modele Gemini 2.5 i nowsze przed wygenerowaniem odpowiedzi korzystają z wewnętrznego procesu rozumowania zwanego „myśleniem”. Pomaga to modelowi udzielać lepszych odpowiedzi w przypadku złożonych zadań, takich jak matematyka, kodowanie i wielostopniowe wnioskowanie.

#### Poziom myślenia

Parametr `thinking_level` umożliwia kontrolowanie głębokości rozumowania modelu:

| Poziom | Opis | Obsługiwane modele |
| --- | --- | --- |
| `minimal` | W przypadku większości zapytań odpowiada ustawieniu „bez myślenia”. W niektórych przypadkach modele mogą myśleć w bardzo ograniczony sposób. Minimalizuje opóźnienia i koszty. | **Tylko modele Flash**   (np. Gemini 3 Flash) |
| `low` | Uproszczone rozumowanie, które priorytetowo traktuje czas oczekiwania i oszczędności kosztów w przypadku prostych instrukcji i czatów. | **Wszystkie modele myślenia** |
| `medium` | Zrównoważone myślenie w przypadku większości zadań. | **Tylko modele Flash**   (np. Gemini 3 Flash) |
| `high` | **(Domyślny)** Maksymalizuje głębokość rozumowania. Model może potrzebować znacznie więcej czasu na wygenerowanie pierwszego tokena, ale wynik będzie bardziej przemyślany. | **Wszystkie modele myślenia** |

#### Podsumowania myśli

Proces myślowy modelu jest przedstawiany w postaci **bloków myślowych** (`type: "thought"`) w danych wyjściowych odpowiedzi. Za pomocą parametru `thinking_summaries` możesz określić, czy chcesz otrzymywać podsumowania procesu myślowego w formie czytelnej dla człowieka:

| Wartość | Opis |
| --- | --- |
| `auto` | **(Domyślnie)** Zwraca podsumowania przemyśleń, jeśli są dostępne. |
| `none` | Wyłącza podsumowania myśli. |

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

### JavaScript

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

Każdy blok myśli zawiera pole `signature` (kryptograficzny skrót wewnętrznego stanu rozumowania) i opcjonalne pole `summary` (czytelne dla człowieka podsumowanie rozumowania modelu). `signature` jest zawsze obecny, ale w tych przypadkach blok myśli może zawierać tylko podpis bez podsumowania:

- **Proste żądania:** model nie przeprowadził wystarczającego rozumowania, aby wygenerować podsumowanie.
- **`thinking_summaries: "none"`**: podsumowania są wyraźnie wyłączone.

Kod powinien zawsze obsługiwać bloki myśli, w których pole `summary` jest puste lub nie występuje. Jeśli zarządzasz historią rozmów ręcznie (tryb bezstanowy), musisz uwzględniać bloki myśli wraz z ich podpisami w kolejnych żądaniach, aby potwierdzić autentyczność.

### Praca z plikami

#### Praca z plikami zdalnymi

Dostęp do plików przy użyciu zdalnych adresów URL bezpośrednio w wywołaniu interfejsu API.

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

### JavaScript

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

#### Praca z interfejsem Gemini Files API

Przed użyciem plików prześlij je do [interfejsu Gemini Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

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

### JavaScript

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

### Poziomy wnioskowania Flex i Priority

Za pomocą poziomów wnioskowania w interfejsie Interactions API możesz optymalizować różne potrzeby związane z obciążeniem:

- [Elastyczne](https://ai.google.dev/gemini-api/docs/flex-inference?hl=pl) (`flex`) w celu optymalizacji kosztów; 50% zniżki w stosunku do ceny standardowej.
- [Priorytet](https://ai.google.dev/gemini-api/docs/priority-inference?hl=pl) (`priority`) w przypadku optymalizacji pod kątem opóźnień; najwyższy poziom usług pod względem niezawodności.

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

### JavaScript

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

### Model danych

Więcej informacji o modelu danych znajdziesz w [dokumentacji interfejsu API](https://ai.google.dev/api/interactions-api?hl=pl#data-models). Poniżej znajdziesz ogólny przegląd głównych komponentów.

#### Interakcja

| Właściwość | Typ | Opis |
| --- | --- | --- |
| `id` | `string` | Unikalny identyfikator interakcji. |
| `model`/`agent` | `string` | Użyty model lub agent. Możesz podać tylko jedną wartość. |
| `input` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=pl#data-models) | dane wejściowe. |
| `outputs` | [`Content[]`](https://ai.google.dev/api/interactions-api?hl=pl#data-models) | odpowiedzi modelu; |
| `tools` | [`Tool[]`](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Tool) | używane narzędzia; |
| `previous_interaction_id` | `string` | Identyfikator poprzedniej interakcji w celu uzyskania kontekstu. |
| `stream` | `boolean` | Czy interakcja jest strumieniowa. |
| `status` | `string` | Stan: `completed`, `in_progress`, `requires_action`, `failed` itp. |
| `background` | `boolean` | Określa, czy interakcja odbywa się w trybie działania w tle. |
| `store` | `boolean` | Określa, czy zapisać interakcję. Domyślnie: `true`. Aby zrezygnować, ustaw wartość `false`. |
| `usage` | [Wykorzystanie](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Interaction) | Wykorzystanie tokenów w żądaniu interakcji. |

## Obsługiwane modele i agenci

| Nazwa modelu | Typ | Identyfikator modelu |
| --- | --- | --- |
| Gemini 3.1 Flash-Lite (wersja testowa) | Model | `gemini-3.1-flash-lite-preview` |
| Gemini 3.1 Pro (wersja testowa) | Model | `gemini-3.1-pro-preview` |
| Gemini 3 Flash (wersja testowa) | Model | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | Model | `gemini-2.5-pro` |
| Gemini 2.5 Flash | Model | `gemini-2.5-flash` |
| Gemini 2.5 Flash-lite | Model | `gemini-2.5-flash-lite` |
| Podgląd klipu Lyria 3 | Model | `lyria-3-clip-preview` |
| Lyria 3 Pro (wersja testowa) | Model | `lyria-3-pro-preview` |
| Wersja testowa Deep Research | Agent | `deep-research-pro-preview-12-2025` |
| Wersja testowa Deep Research | Agent | `deep-research-preview-04-2026` |
| Wersja testowa Deep Research | Agent | `deep-research-max-preview-04-2026` |

## Jak działa interfejs Interactions API

Interfejs Interactions API jest oparty na centralnym zasobie: [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=pl#Resource:Interaction).
Symbol `Interaction` oznacza pełną turę w rozmowie lub zadaniu. Działa on jako zapis sesji, zawierający całą historię interakcji, w tym wszystkie dane wejściowe użytkownika, przemyślenia modelu, wywołania narzędzi, wyniki narzędzi i końcowe dane wyjściowe modelu.

Gdy dzwonisz pod numer [`interactions.create`](https://ai.google.dev/api/interactions-api?hl=pl#CreateInteraction), tworzysz nowy zasób `Interaction`.

### Zarządzanie stanem po stronie serwera

W kolejnym wywołaniu możesz użyć `id` zakończonej interakcji, korzystając z parametru `previous_interaction_id`, aby kontynuować rozmowę. Serwer używa tego identyfikatora do pobierania historii rozmów, dzięki czemu nie musisz ponownie wysyłać całej historii czatu.

Zachowywana jest tylko historia rozmów (dane wejściowe i wyjściowe) za pomocą `previous_interaction_id`. Pozostałe parametry mają **zakres interakcji** i mają zastosowanie tylko do konkretnej interakcji, którą obecnie generujesz:

- `tools`
- `system_instruction`
- `generation_config` (w tym `thinking_level`, `temperature` itp.)

Oznacza to, że jeśli chcesz, aby te parametry były stosowane, musisz ponownie określić je w każdej nowej interakcji. Zarządzanie stanem po stronie serwera jest opcjonalne. Możesz też działać w trybie bezstanowym, wysyłając w każdym żądaniu pełną historię rozmowy.

### Przechowywanie danych

Domyślnie wszystkie obiekty Interaction są przechowywane (`store=true`), aby uprościć korzystanie z funkcji zarządzania stanem po stronie serwera (z `previous_interaction_id`), wykonywania w tle (za pomocą `background=true`) i dostrzegalności.

- **Wersja płatna:**  interakcje są przechowywane przez **55 dni**.
- **Poziom bezpłatny:**  interakcje są przechowywane przez **1 dzień**.

Jeśli nie chcesz tego robić, możesz w swojej prośbie ustawić `store=false`. To ustawienie jest niezależne od zarządzania stanem. Możesz zrezygnować z przechowywania danych w przypadku dowolnej interakcji. Pamiętaj jednak, że `store=false` jest niezgodny z `background=true` i uniemożliwia używanie `previous_interaction_id` w kolejnych turach.

Zapisane interakcje możesz w każdej chwili usunąć za pomocą metody usuwania opisanej w [dokumentacji interfejsu API](https://ai.google.dev/api/interactions-api?hl=pl). Interakcje możesz usuwać tylko wtedy, gdy znasz ich identyfikator.

Po wygaśnięciu okresu przechowywania Twoje dane zostaną automatycznie usunięte.

Obiekty interakcji są przetwarzane zgodnie z [warunkami](https://ai.google.dev/gemini-api/terms?hl=pl).

## Sprawdzone metody

- **Współczynnik trafień w pamięci podręcznej:** używanie symbolu `previous_interaction_id` do kontynuowania rozmów ułatwia systemowi korzystanie z niejawnego buforowania historii rozmów, co zwiększa wydajność i obniża koszty.
- **Mieszanie interakcji:** możesz mieszać interakcje z agentem i modelem w ramach jednej rozmowy. Możesz na przykład użyć specjalistycznego agenta, takiego jak agent Deep Research, do wstępnego zbierania danych, a następnie użyć standardowego modelu Gemini do wykonywania kolejnych zadań, takich jak podsumowywanie lub formatowanie, łącząc te kroki za pomocą funkcji `previous_interaction_id`.

## Pakiety SDK

Aby uzyskać dostęp do interfejsu API interakcji, możesz użyć najnowszej wersji pakietów SDK Google GenAI.

- W Pythonie jest to pakiet `google-genai` od wersji `1.55.0`.
- W przypadku JavaScriptu jest to pakiet `@google/genai` od wersji `1.33.0`.

Więcej informacji o instalowaniu pakietów SDK znajdziesz na stronie [Biblioteki](https://ai.google.dev/gemini-api/docs/libraries?hl=pl).

## Ograniczenia

- **Stan wersji beta:** interfejs Interactions API jest dostępny w wersji beta lub w wersji zapoznawczej. Funkcje i schematy mogą ulec zmianie.
- **Zdalne MCP:** Gemini 3 nie obsługuje zdalnego MCP. Ta funkcja będzie dostępna wkrótce.

## Zmiany powodujące niezgodność

Interfejs Interactions API jest obecnie w wersji beta. Aktywnie rozwijamy i udoskonalamy możliwości interfejsu API, schematy zasobów i interfejsy SDK na podstawie rzeczywistego wykorzystania i opinii deweloperów.

W związku z tym **mogą wystąpić zmiany powodujące niezgodność**.
Aktualizacje mogą obejmować zmiany w:

- Schematy danych wejściowych i wyjściowych.
- sygnatury metod pakietu SDK i struktury obiektów;
- konkretne zachowania funkcji,

W przypadku zadań produkcyjnych należy nadal używać standardowego interfejsu API [`generateContent`](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl). Jest to zalecana ścieżka w przypadku stabilnych wdrożeń, która będzie nadal aktywnie rozwijana i utrzymywana.

## Prześlij opinię

Twoja opinia jest kluczowa dla rozwoju interfejsu Interactions API.
Podziel się swoimi przemyśleniami, zgłoś błędy lub poproś o funkcje na naszym [forum społeczności deweloperów Google AI](https://discuss.ai.google.dev/c/gemini-api/4?hl=pl).

## Co dalej?

- Wypróbuj [notatnik z szybkim wprowadzeniem do interfejsu Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=pl).
- Dowiedz się więcej o [agencie Deep Research w Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
