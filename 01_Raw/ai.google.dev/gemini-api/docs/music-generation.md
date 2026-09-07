---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=pl
fetched_at: 2026-09-07T05:47:31.123093+00:00
title: "Generowanie muzyki za pomoc\u0105 Lyrii\u00a03.5 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie muzyki za pomocą Lyrii 3.5

Lyria 3.5 to rodzina modeli generowania muzyki od Google, które są dostępne za pomocą Gemini API. Dzięki Lyrii 3.5 możesz generować wysokiej jakości dźwięk stereo o częstotliwości 44,1 kHz na podstawie promptów tekstowych lub obrazów. Modele te zapewniają spójność strukturalną, w tym wokal, zsynchronizowany tekst i pełne aranżacje instrumentalne.

Rodzina modeli Lyria obejmuje te modele:

| Model | Identyfikator modelu | Urządzenia | Czas trwania | Wyniki |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Krótkie klipy, pętle, zapowiedzi | 30 sekund | MP3 |
| **Lyria 3.5** | `lyria-3.5` | Pełne utwory ze zwrotkami, refrenami i przejściami | Kilka minut (można kontrolować za pomocą prompta) | MP3 |

Oba modele można używać za pomocą nowego
[interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl), który obsługuje dane wejściowe multimodalne (tekst i obrazy) i generuje dźwięk **stereo o wysokiej jakości i częstotliwości 44,1 kHz**
.

## Generowanie klipu muzycznego

Model Lyria 3 Clip zawsze generuje **30-sekundowy** klip. Aby wygenerować klip, wywołaj metodę `interactions.create` z promptem tekstowym. Odpowiedź zawsze zawiera wygenerowany tekst i strukturę utworu wraz z dźwiękiem w schemacie `steps`.

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

### JavaScript

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

### Java

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

Wygenerowane dane muzyczne możesz pobrać za pomocą właściwości `interaction.output_audio`, która zwraca ostatni wygenerowany blok audio. Możesz też pobrać tekst i strukturę utworu za pomocą właściwości `interaction.output_text`. Więcej informacji o właściwościach ułatwiających pracę znajdziesz w artykule
[Omówienie interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl#convenience-properties).

## Generowanie pełnego utworu

Użyj modelu `lyria-3.5`, aby generować pełne utwory trwające kilka minut. Model Pro rozumie strukturę muzyczną i może tworzyć kompozycje z wyraźnymi zwrotkami, refrenami i przejściami. Możesz wpływać na
czas trwania, określając go w prompcie (np. "utwórz 2-minutowy utwór") lub
używając [sygnatur czasowych](#timing) do zdefiniowania struktury.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
});
```

### Java

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

## Wybieranie formatu wyjściowego

Domyślnie modele Lyria 3.5 generują dźwięk w formacie **MP3**. W przypadku Lyrii 3.5 możesz też poprosić o dane wyjściowe w formacie **WAV**, ustawiając `response_format`.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### Java

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

## Parsowanie odpowiedzi

Odpowiedź z Lyrii 3.5 zawiera wiele bloków treści w schemacie `steps`.
Interfejs Interactions API zwraca sekwencję kroków, w których kroki `model_output` zawierają wygenerowaną treść.
Bloki treści tekstowej zawierają wygenerowany tekst lub opis struktury utworu w formacie JSON.
Bloki treści typu `audio` zawierają dane audio zakodowane w formacie base64.

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

### JavaScript

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

### Java

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

#### Przeplatany tekst i muzyka

Ponieważ dane wyjściowe z Lyrii 3.5 są złożone – zawierają oddzielne kroki i bloki wygenerowanego tekstu (tekst) i samego utworu (dźwięk) – właściwości ułatwiające pracę oferują szybki i zalecany skrót.

Jeśli jednak chcesz mieć pełną, programową kontrolę nad surową osią czasu kroków zwracanych przez serwer (np. rejestrować poszczególne bloki treści w miarę ich otrzymywania), możesz ręcznie iterować po `steps`:

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

### JavaScript

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

### Java

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

## Generowanie muzyki na podstawie obrazów

Lyria 3.5 obsługuje dane wejściowe multimodalne – w liście `input` możesz podać do **10 obrazów** wraz z promptem tekstowym, a model skomponuje muzykę inspirowaną treściami wizualnymi.

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

### JavaScript

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

### Java

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

## Podawanie własnego tekstu

Możesz napisać własny tekst i umieścić go w prompcie. Używaj tagów sekcji, takich jak `[Verse]`, `[Chorus]` i `[Bridge]`, aby pomóc modelowi zrozumieć strukturę utworu:

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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

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

## Kontrolowanie czasu i struktury

Za pomocą sygnatur czasowych możesz dokładnie określić, co ma się dziać w określonych momentach utworu. Jest to przydatne do kontrolowania, kiedy instrumenty wchodzą, kiedy tekst jest odtwarzany i jak utwór się rozwija:

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

const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: prompt,
});
```

### Java

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

## Generowanie ścieżek instrumentalnych

W przypadku muzyki w tle, ścieżek dźwiękowych do gier lub innych zastosowań, w których nie jest wymagany wokal, możesz poprosić model o wygenerowanie ścieżek instrumentalnych:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### Java

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

## Generowanie muzyki w różnych językach

Lyria 3.5 generuje tekst w języku prompta. Aby wygenerować utwór z tekstem w języku francuskim, napisz prompt w tym języku. Model dostosowuje styl wokalny i wymowę do języka.

### Python

```
interaction = client.interactions.create(
    model="lyria-3.5",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3.5',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### Java

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

## Inteligencja modelu

Lyria 3.5 analizuje proces prompta, w którym model wnioskuje na podstawie prompta o strukturze muzycznej (intro, zwrotka, refren, przejście itp.).
Dzieje się to przed wygenerowaniem dźwięku i zapewnia spójność strukturalną oraz muzykalność.

## Przewodnik po promptach

Im bardziej szczegółowy prompt, tym lepsze wyniki. Oto, co możesz uwzględnić, aby kierować generowaniem:

- **Gatunek**: określ gatunek lub mieszankę gatunków (np. „lo-fi hip hop”,
  „jazz fusion”, „cinematic orchestral”).
- **Instrumenty**: wymień konkretne instrumenty (np. "fortepian Fender Rhodes",
  "gitara slide", "automat perkusyjny TR-808").
- **BPM**: ustaw tempo (np. „120 BPM”, „wolne tempo około 70 BPM”).
- **Tonacja/skala**: określ tonację muzyczną (np. „w tonacji G-dur”, „d-moll”).
- **Nastrój i atmosfera**: używaj przymiotników opisowych (np. „nostalgiczny”,
  „agresywny”, „etericzny”, „marzycielski”).
- **Struktura**: używaj tagów takich jak `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` lub sygnatur czasowych, aby kontrolować postęp utworu.
- **Czas trwania**: model Clip zawsze generuje 30-sekundowe klipy. W przypadku modelu Pro określ zamierzoną długość w prompcie (np. „utwórz 2-minutowy utwór”) lub użyj sygnatur czasowych, aby kontrolować czas trwania.

### Przykładowe prompty

Oto kilka przykładów skutecznych promptów:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Sprawdzone metody

- **Najpierw iteruj za pomocą modelu Clip.** Użyj szybszego modelu `lyria-3-clip-preview`, aby eksperymentować z promptami, zanim zdecydujesz się na wygenerowanie pełnego utworu za pomocą modelu `lyria-3.5`.
- **Unikaj ogólników.** Niejasne prompty dają ogólne wyniki. Aby uzyskać najlepsze wyniki, wymień instrumenty, BPM, tonację, nastrój i strukturę.
- **Dopasuj język.** Prompt powinien być napisany w języku, w którym chcesz uzyskać tekst.
- **Używaj tagów sekcji.** Tagi `[Verse]`, `[Chorus]` i `[Bridge]` dają modelowi jasną strukturę do naśladowania.
- **Oddziel tekst od instrukcji.** Podczas podawania własnego tekstu wyraźnie oddziel go od instrukcji dotyczących kierunku muzycznego.

## Ograniczenia

- **Bezpieczeństwo**: wszystkie prompty są sprawdzane przez filtry bezpieczeństwa. Prompty, które aktywują filtry, zostaną zablokowane. Obejmuje to prompty, które proszą o głosy konkretnych artystów lub wygenerowanie tekstów chronionych prawem autorskim.
- **Znaki wodne**: wszystkie wygenerowane dźwięki zawierają
  [znak wodny audio SynthID](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=pl) do
  identyfikacji. Ten znak wodny jest niewidoczny dla ludzkiego ucha i nie wpływa na wrażenia słuchowe.
- **Edycja wieloetapowa**: generowanie muzyki to proces jednoetapowy.
  W obecnej wersji Lyrii 3.5 nie jest obsługiwana iteracyjna edycja ani ulepszanie wygenerowanego klipu za pomocą wielu promptów.
- **Długość**: model Clip zawsze generuje 30-sekundowe klipy. Model Pro generuje utwory trwające kilka minut. Na dokładny czas trwania można wpływać za pomocą prompta.
- **Determinizm**: wyniki mogą się różnić w zależności od wywołania, nawet w przypadku tego samego prompta.

## Co dalej?

- Sprawdź [ceny](https://ai.google.dev/gemini-api/docs/pricing?hl=pl) modeli Lyria 3.5.
- Wypróbuj [generowanie muzyki w czasie rzeczywistym](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pl)
  za pomocą Lyrii RealTime.
- Generuj rozmowy z udziałem wielu osób za pomocą modeli
  [TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).
- Dowiedz się, jak generować [obrazy](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) lub [filmy](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- Dowiedz się, jak Gemini może [rozumieć pliki audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl).
- Prowadź rozmowę w czasie rzeczywistym z Gemini za pomocą interfejsu
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-04 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-04 UTC."],[],[]]
