---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl
fetched_at: 2026-09-21T05:49:46.116731+00:00
title: "Generowanie tekstu na mow\u0119 (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie tekstu na mowę (TTS)

Interfejs Gemini API może przekształcać tekst wejściowy w dźwięk z jednym lub wieloma mówcami za pomocą funkcji generowania tekstu na mowę (TTS) Gemini.
Generowanie tekstu na mowę (TTS) jest *[kontrolowane](#controllable)*, co oznacza, że możesz używać języka naturalnego do strukturyzowania interakcji i określania *stylu*, *akcentu*, *tempa* i *tonu* dźwięku.

Funkcja TTS różni się od generowania mowy za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl), który jest przeznaczony do interaktywnych, nieustrukturyzowanych danych audio oraz multimodalnych danych wejściowych i wyjściowych. Interfejs Live API sprawdza się w dynamicznych kontekstach konwersacyjnych, a TTS za pomocą interfejsu Gemini API jest dostosowany do scenariuszy, które wymagają dokładnego odczytania tekstu z precyzyjną kontrolą stylu i dźwięku, takich jak generowanie podcastów lub audiobooków.

Z tego przewodnika dowiesz się, jak generować dźwięk z tekstu dla jednego lub wielu mówców.

## Zanim zaczniesz

Używaj wariantu modelu Gemini 2.5 z funkcjami zamiany tekstu na mowę (TTS) Gemini, jak podano w sekcji [Obsługiwane modele](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#supported-models). Aby uzyskać optymalne wyniki, zastanów się, który model najlepiej pasuje do Twojego konkretnego przypadku użycia.

Zanim zaczniesz tworzyć, możesz [przetestować modele TTS Gemini w AI Studio](https://aistudio.google.com/generate-speech?hl=pl).

## TTS z jednym głosem

Aby przekonwertować tekst na dźwięk z jednym mówcą, ustaw tryb odpowiedzi na „audio” i przekaż obiekt `speech_config` z nazwą głosu.
Musisz wybrać nazwę głosu z gotowych [głosów wyjściowych](#voices).

W tym przykładzie zapisujemy wyjściowy dźwięk z modelu w pliku wave:

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    }
)

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
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
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
    });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.SpeechConfig;
import com.google.genai.gaos.models.interactions.SpeechConfigUnion;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.util.Arrays;
import java.util.Base64;
import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;

Client client = new Client();

SpeechConfig speechConfig = SpeechConfig.builder().voice("Kore").build();
GenerationConfig generationConfig =
    GenerationConfig.builder()
        .speechConfig(SpeechConfigUnion.of(Arrays.asList(speechConfig)))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-tts-preview"))
        .input(InteractionsInput.of("Say cheerfully: Have a wonderful day!"))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .generationConfig(generationConfig)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] pcmBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  AudioFormat format = new AudioFormat(24000, 16, 1, true, false);
  AudioInputStream audioInputStream =
      new AudioInputStream(
          new ByteArrayInputStream(pcmBytes), format, pcmBytes.length / format.getFrameSize());
  AudioSystem.write(audioInputStream, AudioFileFormat.Type.WAVE, new File("out.wav"));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
       "type": "audio"
     },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

Wygenerowane dane audio możesz pobrać za pomocą właściwości `interaction.output_audio`, która zwraca ostatni wygenerowany blok audio. Więcej informacji o właściwościach ułatwiających korzystanie z usługi znajdziesz w [omówieniu interakcji](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl#convenience-properties).

## TTS z wieloma rozmówcami

W przypadku dźwięku z wielu głośników potrzebny jest obiekt `multi_speaker_voice_config`, w którym każdy głośnik (maksymalnie 2) jest skonfigurowany jako `speaker_voice_config`.
Każdy parametr `speaker` musisz zdefiniować za pomocą tych samych nazw, które zostały użyte w [prompcie](#controllable):

### Python

```
from google import genai
import wave
import base64

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

 interaction = client.interactions.create(
     model="gemini-3.1-flash-tts-preview",
     input=prompt,
     response_format={"type": "audio"},
     generation_config={
         "speech_config": [
             {"speaker": "Joe", "voice": "Kore"},
             {"speaker": "Jane", "voice": "Puck"}
         ]
     }
 )

wave_file('out.wav', base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
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
   const client = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const interaction = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: prompt,
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { speaker: 'Joe', voice: 'Kore' },
            { speaker: 'Jane', voice: 'Puck' }
         ]
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');

   await saveWaveFile('out.wav', audioBuffer);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.SpeechConfig;
import com.google.genai.gaos.models.interactions.SpeechConfigUnion;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.util.Arrays;
import java.util.Base64;
import javax.sound.sampled.AudioFileFormat;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;

Client client = new Client();

String prompt =
    "TTS the following conversation between Joe and Jane:\n"
        + "Joe: How's it going today Jane?\n"
        + "Jane: Not too bad, how about you?";

SpeechConfig joeConfig = SpeechConfig.builder().speaker("Joe").voice("Kore").build();
SpeechConfig janeConfig = SpeechConfig.builder().speaker("Jane").voice("Puck").build();

GenerationConfig generationConfig =
    GenerationConfig.builder()
        .speechConfig(SpeechConfigUnion.of(Arrays.asList(joeConfig, janeConfig)))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-tts-preview"))
        .input(InteractionsInput.of(prompt))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .generationConfig(generationConfig)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputAudio().isPresent() && interaction.outputAudio().get().data().isPresent()) {
  byte[] pcmBytes = Base64.getDecoder().decode(interaction.outputAudio().get().data().get());
  AudioFormat format = new AudioFormat(24000, 16, 1, true, false);
  AudioInputStream audioInputStream =
      new AudioInputStream(
          new ByteArrayInputStream(pcmBytes), format, pcmBytes.length / format.getFrameSize());
  AudioSystem.write(audioInputStream, AudioFileFormat.Type.WAVE, new File("out.wav"));
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gemini-3.1-flash-tts-preview",
  "input": "TTS the following conversation between Joe and Jane: Joe: Hows it going today Jane? Jane: Not too bad, how about you?",
  "response_format": {
       "type": "audio"
     },
  "generation_config": {
    "speech_config": [
      { "speaker": "Joe", "voice": "Kore" },
      { "speaker": "Jane", "voice": "Puck" }
    ]
  }
}'
```

## Sterowanie stylem mowy za pomocą promptów

Możesz kontrolować styl, ton, akcent i tempo za pomocą promptów w języku naturalnym w przypadku zamiany tekstu na mowę z jednym lub wieloma mówcami.
Na przykład w prompcie z jednym głośnikiem możesz powiedzieć:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

W prompcie z wieloma mówcami podaj modelowi imię i nazwisko każdego z nich oraz odpowiednią transkrypcję. Możesz też podać wskazówki dla każdego głośnika z osobna:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

Aby jeszcze bardziej podkreślić styl lub emocje, które chcesz przekazać, użyj [opcji głosu](#voices), która do nich pasuje. Na przykład w poprzednim prompcie *Enceladus* może podkreślać słowa „zmęczony” i „znudzony”, a *Puck* może uzupełniać słowa „podekscytowany” i „szczęśliwy”.

## Generowanie prompta do przekształcenia w dźwięk

Modele TTS generują tylko dźwięk, ale możesz użyć [innych modeli](https://ai.google.dev/gemini-api/docs/models?hl=pl), aby najpierw wygenerować transkrypcję, a potem przekazać ją do modelu TTS, który ją odczyta.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.8-flash",
   input="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam."""
)
transcript = transcript_interaction.output_text

tts_interaction = client.interactions.create(
   model="gemini-3.1-flash-tts-preview",
   input=transcript,
   response_format={"type": "audio"},
   generation_config={
      "speech_config": [
         {"speaker": "Dr. Anya", "voice": "Kore"},
         {"speaker": "Liam", "voice": "Puck"}
      ]
   }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {

const transcriptInteraction = await client.interactions.create({
   model: "gemini-3.8-flash",
   input: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const ttsInteraction = await client.interactions.create({
   model: "gemini-3.1-flash-tts-preview",
   input: transcriptInteraction.output_text,
   response_format: { type: 'audio' },
   generation_config: {
      speech_config: [
         { speaker: "Dr. Anya", voice: "Kore" },
         { speaker: "Liam", voice: "Puck" }
      ]
   }
  });
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.SpeechConfig;
import com.google.genai.gaos.models.interactions.SpeechConfigUnion;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction transcriptParams =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Generate a short transcript around 100 words that reads "
                    + "like it was clipped from a podcast by excited herpetologists. "
                    + "The hosts names are Dr. Anya and Liam."))
        .build();

Interaction transcriptInteraction =
    client
        .interactions
        .create(CreateInteractionRequestBody.of(transcriptParams))
        .interaction()
        .get();

String transcript = transcriptInteraction.outputText().orElse("");

SpeechConfig anyaConfig = SpeechConfig.builder().speaker("Dr. Anya").voice("Kore").build();
SpeechConfig liamConfig = SpeechConfig.builder().speaker("Liam").voice("Puck").build();

GenerationConfig generationConfig =
    GenerationConfig.builder()
        .speechConfig(SpeechConfigUnion.of(Arrays.asList(anyaConfig, liamConfig)))
        .build();

CreateModelInteraction ttsParams =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-tts-preview"))
        .input(InteractionsInput.of(transcript))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .generationConfig(generationConfig)
        .build();

Interaction ttsInteraction =
    client.interactions.create(CreateInteractionRequestBody.of(ttsParams)).interaction().get();
```

## Generowanie mowy strumieniowej

Możesz przesyłać strumieniowo wygenerowany dźwięk w trakcie jego generowania przez model, ustawiając `stream: true`.

### Python

```
from google import genai
import base64

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-tts-preview",
    input="Say cheerfully: Have a wonderful day!",
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"}
        ]
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: "gemini-3.1-flash-tts-preview",
      input: "Say cheerfully: Have a wonderful day!",
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' }
         ]
      },
      stream: true
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioDelta;
import com.google.genai.gaos.models.interactions.AudioResponseFormat;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.SpeechConfig;
import com.google.genai.gaos.models.interactions.SpeechConfigUnion;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

SpeechConfig speechConfig = SpeechConfig.builder().voice("Kore").build();
GenerationConfig generationConfig =
    GenerationConfig.builder()
        .speechConfig(SpeechConfigUnion.of(Arrays.asList(speechConfig)))
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-tts-preview"))
        .input(InteractionsInput.of("Say cheerfully: Have a wonderful day!"))
        .responseFormat(
            CreateModelInteractionResponseFormat.of(
                ResponseFormat.of(AudioResponseFormat.builder().build())))
        .generationConfig(generationConfig)
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> events = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : events) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta) {
      StepDeltaData deltaData = ((StepDelta) event).delta().orElse(null);
      if (deltaData instanceof AudioDelta) {
        AudioDelta audioDelta = (AudioDelta) deltaData;
        if (audioDelta.data().isPresent()) {
          byte[] audioData = Base64.getDecoder().decode(audioDelta.data().get());
          // Process the audio chunk (e.g. play it or write to a file)
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"       -H "x-goog-api-key: $GEMINI_API_KEY"       -H "Content-Type: application/json"       -H "Api-Revision: 2026-05-20"       --no-buffer       -d '{
    "model": "gemini-3.1-flash-tts-preview",
    "input": "Say cheerfully: Have a wonderful day!",
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## Opcje głosowe

Modele TTS obsługują te 30 opcji głosowych w polu `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *jasny* | **Puck** – *Upbeat* | **Charon** – *Zawiera przydatne informacje* |
| **Kore** – *firma* | **Fenrir** – *pobudliwy* | **Leda** -- *Youthful* |
| **Orus** – *firma* | **Aoede** – *Breezy* | **Callirrhoe** – *spokojny* |
| **Autonoe** – *jasny* | **Enceladus** – *Breathy* | **Iapetus** – *Clear* |
| **Umbriel** – *spokojny* | **Algieba** – *Smooth* | **Despina** – *Smooth* |
| **Erinome** – *Clear* | **Algenib** – *żwirowy* | **Rasalgethi** – *zawiera przydatne informacje* |
| **Laomedeia** – *Upbeat* | **Achernar** – *miękka* | **Alnilam** – *Firm* |
| **Schedar** – *Równomierna* | **Gacrux** – *treści dla dorosłych* | **Pulcherrima** – *Przekaż dalej* |
| **Achird** – *przyjazny* | **Zubenelgenubi** – *zwykłe* | **Vindemiatrix** – *delikatny* |
| **Sadachbia** – *Lively* | **Sadaltager** – *wiedza* | **Sulafat** – *ciepły* |

Wszystkie opcje głosowe możesz usłyszeć w [AI Studio](https://aistudio.google.com/generate-speech?hl=pl).

## Obsługiwane języki

Modele TTS automatycznie wykrywają język wejściowy. Obsługiwane języki:

| Język | Kod BCP-47 | Język | Kod BCP-47 |
| --- | --- | --- | --- |
| arabski | ar | filipiński | fil |
| bengalski | bn | fiński | fi |
| niderlandzki | nl | galicyjski | gl |
| angielski | en | gruziński | ka |
| francuski | fr | grecki | el |
| niemiecki | de | gudżarati | gu |
| hindi | hi | kreolski haitański | ht |
| indonezyjski | id | hebrajski | on |
| włoski | it | węgierski | hu |
| japoński | ja | islandzki | jest |
| koreański | ko | jawajski | jv |
| marathi | mr | kannada | kn |
| polski | pl | konkani | kok |
| portugalski | pt | laotański | lo |
| rumuński | ro | łaciński | la |
| rosyjski | ru | łotewski | lv |
| hiszpański | es | litewski | lt |
| tamilski | ta | luksemburski | lb |
| telugu | te | macedoński | mk |
| tajski | th | maithili | mai |
| turecki | tr | malgaski | mg |
| ukraiński | uk | malajski | ms |
| wietnamski | vi | malajalam | ml |
| afrikaans | af | mongolski | mn |
| albański | sq | nepalski | ne |
| amharski | am | norweski (bokmål), | nb |
| ormiański | hy | norweski (nynorsk), | nn |
| azerski | az | orija | lub |
| baskijski | eu | paszto | ps |
| białoruski | be | perski | fa |
| bułgarski | bg | pendżabski | pa |
| birmański | my | serbski | sr |
| kataloński | ca | sindhi | sd |
| cebuański | ceb | syngaleski | si |
| chiński (mandaryński), | cmn | słowacki | sk |
| chorwacki | godz. | słoweński | sl |
| czeski | cs | suahili | sw |
| duński | da | szwedzki | sv |
| estoński | et | urdu | ur |

## Obsługiwane modele

| Model | Pojedynczy rozmówca | Wielogłośnikowy |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pl) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pl) | ✔️ | ✔️ |
| [Wersja testowa Gemini 2.5 Pro TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=pl) | ✔️ | ✔️ |

## Przewodnik po promptach

Model **Gemini Native Audio Generation Text-to-Speech (TTS)** różni się od tradycyjnych modeli TTS tym, że korzysta z dużego modelu językowego, który ***wie nie tylko, co powiedzieć, ale też jak to zrobić***.

Zaawansowany prompt to instrukcja systemowa dla modelu. Dzięki temu model ma więcej kontekstu i większą kontrolę nad skutecznością.

Aby odblokować tę funkcję, użytkownicy mogą wyobrazić sobie, że są reżyserami, którzy przygotowują scenę dla wirtualnego aktora głosowego. Aby utworzyć prompt, zalecamy uwzględnienie tych elementów: **profilu audio**, który określa podstawową tożsamość i archetyp postaci; **opisu sceny**, który określa środowisko fizyczne i emocjonalny „klimat”; oraz **notatek reżysera**, które zawierają bardziej precyzyjne wskazówki dotyczące stylu, akcentu i tempa.

Dzięki podawaniu szczegółowych instrukcji, takich jak precyzyjny akcent regionalny, konkretne cechy paralingwistyczne (np. oddech) czy tempo, użytkownicy mogą wykorzystywać świadomość kontekstu modelu do generowania bardzo dynamicznych, naturalnych i ekspresyjnych nagrań audio. Aby uzyskać optymalną skuteczność, zalecamy, aby **transkrypcja** i prompty reżyserskie były zgodne, *czyli aby „kto to mówi”* pasowało do *„co jest powiedziane”* i *„jak to jest powiedziane”*.

Celem tego przewodnika jest dostarczenie podstawowych wskazówek i inspiracji podczas tworzenia funkcji audio z wykorzystaniem generowania dźwięku za pomocą Gemini TTS. Z niecierpliwością czekamy na Twoje projekty!

### Tagi audio

Tagi to modyfikatory wstawiane w tekście, np. `[whispers]` lub `[laughs]`, które zapewniają precyzyjną kontrolę nad wyświetlaniem. Możesz ich używać do zmiany tonu, tempa i emocjonalnego wydźwięku wiersza lub fragmentu transkrypcji. Możesz też używać ich do dodawania do występu wykrzykników i innych dźwięków niewerbalnych, takich jak `[cough]`, `[sighs]` czy `[gasp]`.

Nie ma wyczerpującej listy tagów, które działają, a które nie. Zalecamy eksperymentowanie z różnymi emocjami i wyrażeniami, aby sprawdzić, jak zmienia się wynik.

Jeśli transkrypcja nie jest w języku angielskim, zalecamy używanie tagów audio w języku angielskim, aby uzyskać najlepsze wyniki.

**Kreatywne wykorzystanie tagów audio**

Aby pokazać, jak bardzo mogą się różnić tagi audio, przedstawiamy zestaw przykładów, w których przekaz jest taki sam, ale sposób jego przedstawienia zmienia się w zależności od użytych tagów.

Możesz zmienić sposób przekazu, dodając na początku wiersza tagi, które sprawią, że lektor będzie podekscytowany, znudzony lub niechętny:

- `[excitedly]` Cześć, jestem nowym modelem zamiany tekstu na mowę i mogę mówić na wiele sposobów. W czym mogę Ci pomóc?
- `[bored]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[reluctantly]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Tagi mogą też służyć do zmiany tempa odczytu lub łączenia tempa z podkreśleniem:

- `[very fast]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[very slow]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[sarcastically, one painfully slow word at a time]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Masz też precyzyjną kontrolę nad poszczególnymi sekcjami, co oznacza, że możesz szeptać jedną część, a krzyczeć inną.

- `[whispers]` Cześć, jestem nowym modelem zamiany tekstu na mowę `[shouting]` i mogę mówić na wiele różnych sposobów. `[whispers]` W czym mogę Ci dziś pomóc?

Możesz też eksperymentować z dowolnym pomysłem na kreację:

- `[like a cartoon dog]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[like dracula]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Często używane tagi:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Tagi umożliwiają szybkie kontrolowanie dostarczania transkrypcji. Aby mieć jeszcze większą kontrolę, możesz połączyć je z promptem kontekstowym, aby ustawić ogólny ton i atmosferę występu.

### Struktura prompta

Dobry prompt powinien zawierać te elementy, które razem tworzą świetny wynik:

- **Profil audio** – określa osobowość głosu, definiując tożsamość postaci, archetyp i inne cechy, takie jak wiek, pochodzenie itp.
- **Scena** – przygotowuje scenę. Opisuje zarówno środowisko fizyczne, jak i „klimat”.
- **Notatki reżysera** – wskazówki dotyczące skuteczności, w których możesz określić, które instrukcje są ważne dla Twojego wirtualnego talentu. Są to m.in. styl, oddech, tempo, artykulacja i akcent.
- **Przykładowy kontekst** – zapewnia modelowi kontekstowy punkt wyjścia, dzięki czemu wirtualny aktor wchodzi do skonfigurowanej przez Ciebie sceny w naturalny sposób.
- **Transkrypcja** – tekst, który model będzie odczytywać. Aby uzyskać najlepsze wyniki, pamiętaj, że temat transkrypcji i styl pisania powinny być powiązane z podawanymi przez Ciebie wskazówkami.
- **Tagi audio** – modyfikatory, które możesz umieścić w transkrypcji, aby zmienić sposób odczytywania danej części tekstu, np. `[whispers]` lub `[shouting]`.

Przykładowy pełny prompt:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions - no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely
popping off in London right now. If you're stuck on the tube, or just sat
there pretending to work... stop it. Seriously, I see you. Turn this up!
We've got the project roadmap landing in three, two... let's go!
```

### Szczegółowe strategie tworzenia promptów

Rozbij każdy element promptu w ten sposób:

#### Profil audio

Krótko opisz osobowość postaci.

- **Nazwa** Nadanie postaci imienia pomaga modelowi i zapewnia spójność działania. Podczas określania sceny i kontekstu odwołuj się do postaci po imieniu.
- **Rola** Główna tożsamość i archetyp postaci, która występuje w scenie, np. DJ radiowy, podcaster, reporter itp.

Przykłady:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Sceneria

Określ kontekst sceny, w tym lokalizację, nastrój i szczegóły środowiskowe, które nadają ton i klimat. Opisz, co dzieje się wokół postaci i jak to na nią wpływa. Scena zapewnia kontekst środowiskowy dla całej interakcji i w subtelny, naturalny sposób kieruje działaniami aktora.

Przykłady:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### Notatki reżysera

Ta kluczowa sekcja zawiera szczegółowe wskazówki dotyczące skuteczności. Możesz pominąć wszystkie inne elementy, ale zalecamy uwzględnienie tego elementu.

Określ tylko to, co jest ważne dla wydajności, uważając, aby nie przesadzić. Zbyt wiele ścisłych reguł ograniczy kreatywność modeli i może pogorszyć ich skuteczność. Zrównoważ opis roli i sceny ze szczegółowymi zasadami dotyczącymi występu.

Najczęstsze wskazówki to **Styl, tempo i akcent**, ale model nie jest ograniczony do tych wskazówek ani ich nie wymaga. Możesz dodać niestandardowe instrukcje, aby uwzględnić dodatkowe szczegóły ważne dla skuteczności, i podać tyle szczegółów, ile uznasz za konieczne.

Na przykład:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Styl:**

Określa ton i styl wygenerowanej mowy. Wybierz np. „radosny”, „energiczny”, „zrelaksowany”, „znudzony” itp., aby nadać kierunek wykonaniu. Opisz je i podaj jak najwięcej szczegółów: *„Zaraźliwy entuzjazm. Słuchacz powinien czuć, że jest częścią ogromnego, ekscytującego wydarzenia społecznościowego”.* Lepiej jest użyć tego sformułowania niż *„energetyczny i entuzjastyczny”*.

Możesz nawet wypróbować terminy popularne w branży voiceover, takie jak „uśmiech w głosie”. Możesz nałożyć na siebie dowolną liczbę cech stylu.

Przykłady:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Większa głębia

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Złożony

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Akcent:**

Opisz wybrany akcent. Im bardziej szczegółowe informacje podasz, tym lepsze będą wyniki. Na przykład użyj „*akcentu brytyjskiego angielskiego, jakiego używa się w Croydon w Anglii*” zamiast „*akcentu brytyjskiego*”.

Przykłady:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a from Brixton, London
...
```

**Tempo:**

Ogólne tempo i jego zmiany w całym utworze.

Przykłady:

Prosty

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Większa głębia

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Złożony

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

### Wypróbuj

Możesz wypróbować te przykłady w [Bibliotece głosów](https://aistudio.google.com/apps/bundled/voice-library?showPreview=true&hl=pl). Aby uzyskać świetne wykonanie wokalne, postępuj zgodnie z tymi wskazówkami:

- Pamiętaj, aby cały prompt był spójny – skrypt i instrukcje są ze sobą ściśle powiązane i wspólnie tworzą świetne wykonanie.
- Nie musisz opisywać wszystkiego. Czasami pozostawienie modelu miejsca na wypełnienie luk pomaga w naturalności. (Jak utalentowany aktor)
- Jeśli utkniesz w martwym punkcie, poproś Gemini o pomoc w przygotowaniu scenariusza lub występu.

## Ograniczenia

- Modele TTS mogą otrzymywać tylko dane wejściowe w postaci tekstu i generować dane wyjściowe w postaci dźwięku.
- Sesja TTS ma limit [okna kontekstu](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) wynoszący 32 tys. tokenów.
- Więcej informacji o obsługiwanych językach znajdziesz w sekcji [Języki](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#languages).
- Usługa TTS nie obsługuje przesyłania strumieniowego, z wyjątkiem korzystania z `gemini-3.1-flash-tts-preview`.

Poniższe ograniczenia obowiązują w przypadku korzystania z modelu Gemini 3.1 Flash TTS Preview do generowania mowy:

- **Niespójność głosu z instrukcjami prompta:** wygenerowane przez model dane wyjściowe mogą nie zawsze ściśle pasować do wybranego głosu, przez co dźwięk może brzmieć inaczej niż oczekiwano. Aby uniknąć niedopasowania tonów (np. gdy głęboki męski głos próbuje mówić jak mała dziewczynka), upewnij się, że ton i kontekst tekstu w promcie są naturalnie zgodne z profilem wybranego lektora.
- **Jakość dłuższych wyjść:** jakość i spójność mowy mogą zacząć się pogarszać w przypadku wygenerowanych wyjść, które trwają dłużej niż kilka minut. Zalecamy podzielenie transkrypcji na mniejsze części.
- **Sporadyczne zwracanie tokenów tekstowych:** model sporadycznie zwraca tokeny tekstowe zamiast tokenów audio, co powoduje, że serwer odrzuca żądanie z błędem `500`. Dzieje się to losowo w bardzo małym odsetku żądań, dlatego w aplikacji należy zaimplementować automatyczną logikę ponawiania, aby sobie z tym radzić.
- **Fałszywe odrzucenia klasyfikatora promptów:** niejasne prompty mogą nie wywołać klasyfikatora syntezy mowy, co spowoduje odrzucenie żądania (`PROHIBITED_CONTENT`) lub odczytanie przez model instrukcji dotyczących stylu i notatek reżysera. Sprawdzaj skuteczność promptów, dodając jasny wstęp, który instruuje model, aby syntetyzował mowę, i wyraźnie oznaczaj miejsce, w którym zaczyna się rzeczywisty zapis wypowiedzi.

## Co dalej?

- [Interfejs Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) Gemini oferuje interaktywne opcje generowania dźwięku, które możesz przeplatać z innymi trybami.
- Informacje o pracy z *wejściowymi danymi audio* znajdziesz w przewodniku [Rozumienie dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
