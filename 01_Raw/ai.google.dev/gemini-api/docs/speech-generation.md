---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=it
fetched_at: 2026-08-03T04:32:13.570533+00:00
title: "Generazione di sintesi vocale (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generazione di sintesi vocale (TTS)

L'API Gemini può trasformare l'input di testo in audio con una o più voci utilizzando le funzionalità di generazione di sintesi vocale (TTS) di Gemini.
La generazione di sintesi vocale (TTS) è *[controllabile](#controllable)*,
il che significa che puoi utilizzare il linguaggio naturale per strutturare le interazioni e guidare lo
*stile*, l'*accento*, il *ritmo* e il *tono* dell'audio.

La funzionalità TTS è diversa dalla sintesi vocale fornita tramite l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it), progettata per input e output audio interattivi, non strutturati e multimodali. Mentre l'API Live eccelle
in contesti conversazionali dinamici, la sintesi vocale tramite l'API Gemini
è pensata per scenari che richiedono una recitazione esatta del testo con un controllo
preciso su stile e suono, come la generazione di podcast o audiolibri.

Questa guida mostra come generare audio con uno o più relatori dal testo.

## Prima di iniziare

Assicurati di utilizzare una variante del modello Gemini 2.5 con funzionalità di sintesi vocale (TTS) di Gemini, come indicato nella sezione [Modelli supportati](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#supported-models). Per ottenere risultati ottimali, valuta quale modello si adatta meglio al tuo caso d'uso specifico.

Prima di iniziare a creare, ti consigliamo di [testare i modelli Gemini TTS in AI Studio](https://aistudio.google.com/generate-speech?hl=it).

## TTS con un solo speaker

Per convertire il testo in audio con un solo oratore, imposta la modalità di risposta su "audio" e passa un oggetto `speech_config` con il nome di una voce.
Dovrai scegliere un nome per la voce tra le [voci di output](#voices) predefinite.

Questo esempio salva l'audio di output del modello in un file wave:

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

Puoi recuperare i dati audio generati utilizzando la proprietà `interaction.output_audio`, che restituisce l'ultimo blocco audio generato. Per informazioni dettagliate
sulle proprietà di convenienza, consulta la
[panoramica delle interazioni](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it#convenience-properties).

## TTS multilocutore

Per l'audio multi-speaker, avrai bisogno di un oggetto `multi_speaker_voice_config` con
ogni speaker (fino a 2) configurato come `speaker_voice_config`.
Devi definire ogni `speaker` con gli stessi nomi utilizzati nel
[prompt](#controllable):

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

## Controllare lo stile di sintesi vocale con i prompt

Puoi controllare stile, tono, accento e ritmo utilizzando prompt in linguaggio naturale
sia per la sintesi vocale di una singola persona sia per quella di più persone.
Ad esempio, in un prompt con un solo oratore, puoi dire:

```
Say in an spooky whisper:
"By the pricking of my thumbs...
Something wicked this way comes"
```

In un prompt con più speaker, fornisci al modello il nome di ciascuno e
la trascrizione corrispondente. Puoi anche fornire indicazioni per ogni oratore
singolarmente:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

Prova a utilizzare un'[opzione vocale](#voices) che corrisponda allo stile o all'emozione che vuoi trasmettere, per enfatizzarla ancora di più. Nel prompt precedente, ad esempio,
il tono affannoso di *Encelado* potrebbe enfatizzare "stanco" e "annoiato", mentre
il tono allegro di *Puck* potrebbe completare "entusiasta" e "felice".

## Generare un prompt per la conversione in audio

I modelli TTS generano solo audio, ma puoi utilizzare
[altri modelli](https://ai.google.dev/gemini-api/docs/models?hl=it) per generare prima una trascrizione,
quindi trasmetterla al modello TTS per la lettura ad alta voce.

### Python

```
from google import genai

client = genai.Client()

transcript_interaction = client.interactions.create(
   model="gemini-3.6-flash",
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
   model: "gemini-3.6-flash",
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

## Generazione di sintesi vocale in streaming

Puoi riprodurre in streaming l'audio generato durante la generazione del modello impostando `stream: true`.

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

## Opzioni vocali

I modelli TTS supportano le seguenti 30 opzioni vocali nel campo `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *Luminoso* | **Puck** - *Upbeat* | **Caronte**: *informativa* |
| **Kore** -- *Azienda* | **Fenrir**: *eccitabile* | **Leda** - *Giovane* |
| **Orus** -- *Azienda* | **Aoede** - *Breezy* | **Callirrhoe**: *tranquilla* |
| **Autonoe** -- *Luminoso* | **Enceladus** - *Soffio* | **Iapetus** -- *Cancella* |
| **Umbriel**: *tranquillo* | **Algieba** - *Liscia* | **Despina** -- *Smooth* |
| **Erinome** -- *Sereno* | **Algenib** - *Gravelly* | **Rasalgethi** -- *Priorità informativa* |
| **Laomedeia** - *Upbeat* | **Achernar** - *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Per adulti* | **Pulcherrima** -- *Forward* |
| **Achird**: *amichevole* | **Zubenelgenubi** - *Casual* | **Vindemiatrix** - *Gentle* |
| **Sadachbia**: *Vivace* | **Sadaltager** - *Competente* | **Sulafat**: *calda* |

Puoi ascoltare tutte le opzioni vocali in [AI Studio](https://aistudio.google.com/generate-speech?hl=it).

## Lingue supportate

I modelli di sintesi vocale rilevano automaticamente la lingua di input. Sono supportate le seguenti lingue:

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Arabo | ar | Filippino | fil |
| Bengalese | bn | Finlandese | fi |
| Olandese | nl | Galiziano | gl |
| Inglese | it | Georgiano | ka |
| Francese | fr | Greek | el |
| Tedesco | de | Gujarati | gu |
| Hindi | hi | Creolo haitiano | ht |
| Indonesiano | id | Ebraico | lui |
| Italiano | it | Ungherese | hu |
| Giapponese | ja | Islandese | è |
| Coreano | ko | Giavanese | jv |
| Marathi | mr | Kannada | kn |
| Polacco | pl | Konkani | kok |
| Portoghese | pt | Lao | lo |
| Rumeno | ro | Latino | la |
| Russo | ru | Lettone | lv |
| Spagnolo | es | Lituano | lt |
| Tamil | ta | Lussemburghese | lb |
| Telugu | te | Macedone | mk |
| Thailandese | th | Maithili | mai |
| Turco | tr | Malgascio | mg |
| Ucraino | uk | Malese | ms |
| Vietnamita | vi | Malayalam | ml |
| Afrikaans | af | Mongolo | mn |
| Albanese | sq | Nepalese | ne |
| Amarico | am | Norvegese, bokmål | nb |
| Armeno | hy | Norvegese, nynorsk | nn |
| Azero | az | Odia | o |
| Basco | eu | Pashto | ps |
| Bielorusso | be | Persiano | fa |
| Bulgaro | bg | Punjabi | pa |
| Birmano | my | Serbo | sr |
| Catalano | ca | Sindhi | sd |
| Cebuano | ceb | Singalese | si |
| Cinese, mandarino | cmn | Slovacco | sk |
| Croato | h | Sloveno | sl |
| Ceco | cs | Swahili | sw |
| Danese | da | Svedese | sv |
| Estone | et | Urdu | UK |

## Modelli supportati

| Modello | Unico relatore | Multispeaker |
| --- | --- | --- |
| [Anteprima di Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=it) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=it) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=it) | ✔️ | ✔️ |

## Guida ai prompt

Il modello **Gemini Native Audio Generation Text-to-Speech (TTS)** si differenzia
dai modelli TTS convenzionali perché utilizza un modello linguistico di grandi dimensioni che
sa ***non solo cosa dire, ma anche come dirlo***.

Puoi considerare un prompt avanzato come un'istruzione di sistema che il modello deve
seguire. È un modo per fornire al modello più contesto e controllo sulle
prestazioni.

Per sbloccare questa funzionalità, gli utenti possono immaginarsi di essere registi che impostano una
scena per farla interpretare a un doppiatore virtuale. Per creare un prompt, ti consigliamo di
considerare i seguenti componenti: un **profilo audio** che definisce
l'identità e l'archetipo principali del personaggio; una **descrizione della scena** che
stabilisce l'ambiente fisico e l'atmosfera emotiva; e le **note del
regista** che offrono indicazioni più precise sullo stile, sull'accento e sul
controllo del ritmo.

Fornendo istruzioni dettagliate, come un accento regionale preciso, caratteristiche
paralinguistiche specifiche (ad es. respiro) o il ritmo, gli utenti possono sfruttare la
consapevolezza del contesto del modello per generare prestazioni audio altamente dinamiche, naturali ed espressive. Per un rendimento ottimale, consigliamo che il **copione** e
le indicazioni di regia siano allineati, *in modo che "chi lo dice"* corrisponda a *"cosa viene
detto"* e *"come viene detto"*.

Lo scopo di questa guida è fornire indicazioni fondamentali e stimolare idee per lo sviluppo di esperienze audio utilizzando la generazione audio Gemini TTS. Non vediamo l'ora
di vedere le tue creazioni.

### Tag audio

I tag sono modificatori incorporati come `[whispers]` o `[laughs]` che ti offrono un controllo granulare sulla pubblicazione. Puoi utilizzarli per modificare il tono, il ritmo e
l'atmosfera emotiva di una riga o di una sezione della trascrizione. Puoi anche usarli per
aggiungere interiezioni e altri suoni non verbali alla performance, come
`[cough]`, `[sighs]` o `[gasp]`.

Non esiste un elenco esaustivo dei tag che funzionano e di quelli che non funzionano. Ti consigliamo di
sperimentare con diverse emozioni ed espressioni per vedere come cambia l'output.

Se la trascrizione non è in inglese, per ottenere risultati ottimali ti consigliamo di
utilizzare comunque i tag audio in inglese.

**Utilizzare i tag audio in modo creativo**

Per mostrare il tipo di variabilità che puoi ottenere con i tag audio, ecco una serie di esempi che dicono la stessa cosa, ma la pronuncia cambia in base ai tag utilizzati.

Puoi modificare l'enfasi della recitazione aggiungendo tag all'inizio di una
riga per rendere l'oratore entusiasta, annoiato o riluttante:

- `[excitedly]` Ciao, sono un nuovo modello di sintesi vocale e posso dire le cose
  in molti modi diversi. Come posso aiutarti?
- `[bored]` Ciao, sono un nuovo modello di sintesi vocale…
- `[reluctantly]` Ciao, sono un nuovo modello di sintesi vocale…

I tag possono essere utilizzati anche per modificare il ritmo della pronuncia o per combinare il ritmo
con l'enfasi:

- `[very fast]` Ciao, sono un nuovo modello di sintesi vocale…
- `[very slow]` Ciao, sono un nuovo modello di sintesi vocale…
- `[sarcastically, one painfully slow word at a time]` Ciao, sono un nuovo modello di sintesi vocale…

Hai anche il controllo preciso su sezioni specifiche, il che significa che puoi sussurrare
una parte e urlarne un'altra.

- `[whispers]` Ciao, sono un nuovo modello di sintesi vocale, `[shouting]` e posso
  dire le cose in molti modi diversi. `[whispers]` Come posso aiutarti oggi

Puoi anche sperimentare qualsiasi idea creativa tu voglia:

- `[like a cartoon dog]` Ciao, sono un nuovo modello di sintesi vocale…
- `[like dracula]` Ciao, sono un nuovo modello di sintesi vocale…

I tag di uso comune includono:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

I tag consentono di controllare rapidamente la pubblicazione della trascrizione. Per un controllo
ancora maggiore, puoi combinarli con un prompt di contesto per impostare il tono
e l'atmosfera generale della performance.

### Struttura del prompt

Un prompt efficace include idealmente i seguenti elementi che si combinano per
creare una performance eccezionale:

- **Profilo audio**: stabilisce una persona per la voce, definendo un'identità, un archetipo e qualsiasi altra caratteristica come età, background e così via.
- **Scena**: prepara il terreno. Descrive sia l'ambiente fisico sia l'atmosfera.
- **Note del regista**: indicazioni sul rendimento in cui puoi specificare quali istruzioni sono importanti per il tuo talento virtuale. Alcuni esempi sono
  lo stile, la respirazione, il ritmo, l'articolazione e l'accento.
- **Contesto di esempio**: fornisce al modello un punto di partenza contestuale, in modo che il tuo
  attore virtuale entri in scena in modo naturale.
- **Trascrizione**: il testo che il modello pronuncerà. Per ottenere il massimo rendimento,
  ricorda che l'argomento della trascrizione e lo stile di scrittura devono essere correlati alle
  indicazioni che stai dando.
- **Tag audio**: modificatori che puoi inserire in una trascrizione per cambiare il modo in cui viene riprodotta una parte del testo, ad esempio `[whispers]` o `[shouting]`.

Prompt completo di esempio:

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

### Strategie di prompting dettagliate

Analizza ogni elemento del prompt come segue:

#### Profilo audio

Descrivi brevemente la personalità del personaggio.

- **Nome.** Assegnare un nome al personaggio aiuta a dare un contesto al modello e a migliorare la performance. Fai riferimento al personaggio per nome quando imposti la scena e il contesto.
- **Ruolo.** Identità e archetipo principali del personaggio che si manifestano
  nella scena. Ad es. DJ radiofonico, podcaster, giornalista, ecc.

Esempi:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scena

Imposta il contesto della scena, inclusi posizione, stato d'animo e dettagli ambientali
che stabiliscono il tono e l'atmosfera. Descrivi cosa sta succedendo intorno al
personaggio e come lo influenza. La scena fornisce il contesto ambientale
per l'intera interazione e guida la recitazione in modo sottile
e organico.

Esempi:

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

#### Note del regista

Questa sezione fondamentale include indicazioni specifiche sul rendimento. Puoi saltare tutti
gli altri elementi, ma ti consigliamo di includere questo elemento.

Definisci solo ciò che è importante per il rendimento, facendo attenzione a non
specificare eccessivamente. Troppe regole rigide limiteranno la creatività dei modelli e potrebbero
comportare un rendimento peggiore. Bilancia la descrizione del ruolo e della scena con le
regole specifiche per le prestazioni.

Le indicazioni più comuni sono **Stile, Ritmo e Accento**, ma il modello
non è limitato a queste e non le richiede. Puoi includere istruzioni personalizzate per coprire eventuali dettagli aggiuntivi importanti per il tuo rendimento e fornire tutti i dettagli necessari.

Ad esempio:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Stile:**

Imposta il tono e lo stile del discorso generato. Includi elementi come allegro,
energetico, rilassato, annoiato e così via per guidare la performance. Fornisci una descrizione
e il maggior numero possibile di dettagli: *"Entusiasmo contagioso. L'ascoltatore
deve sentirsi parte di un evento comunitario enorme ed entusiasmante"* funziona
meglio di *"energetico ed entusiasta".*

Puoi anche provare termini popolari nel settore del voiceover, come "sorriso
vocale". Puoi sovrapporre tutte le caratteristiche di stile che vuoi.

Esempi:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Più profondità

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Complesso

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Accento:**

Descrivi l'accento selezionato. Più specifico è il prompt, migliori saranno i risultati. Ad esempio, utilizza "*Accento inglese britannico come si sente a Croydon, Inghilterra*" anziché "*Accento britannico*".

Esempi:

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

**Pacing:**

Il ritmo generale e la sua variazione nel corso del brano.

Esempi:

Semplice

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Più profondità

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Complesso

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

**Prova**

Prova alcuni di questi esempi sull'[app TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=it) e lascia che Gemini ti metta nei panni del regista. Tieni a mente questi suggerimenti per ottenere ottime
performance vocali:

- Ricorda di mantenere la coerenza dell'intero prompt: il copione e la regia vanno di pari passo per creare una performance eccezionale.
- Non sentirti in dovere di descrivere tutto. A volte, lasciare al modello lo spazio per colmare le lacune aiuta a rendere il testo più naturale. (proprio come un attore di talento)
- Se ti senti in difficoltà, chiedi a Gemini di aiutarti a creare il copione o la performance.

## Limitazioni

- I modelli TTS possono ricevere solo input di testo e generare output audio.
- Una sessione TTS ha un limite di [finestra contestuale](https://ai.google.dev/gemini-api/docs/long-context?hl=it) di
  32.000 token.
- Consulta la sezione [Lingue](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#languages) per informazioni sulle lingue supportate.
- La sintesi vocale non supporta lo streaming, tranne quando si utilizza `gemini-3.1-flash-tts-preview`.

I seguenti vincoli si applicano in modo specifico quando si utilizza il modello di anteprima Gemini 3.1 Flash TTS per la generazione di voce:

- **Incoerenza della voce con le istruzioni del prompt:** l'output del modello potrebbe non
  corrispondere sempre rigorosamente al relatore selezionato, facendo sì che l'audio suoni
  in modo diverso dal previsto. Per evitare toni non corrispondenti (ad esempio una voce maschile profonda che tenta di parlare come una bambina), assicurati che il tono e il contesto scritti del prompt siano in linea in modo naturale con il profilo dell'oratore selezionato.
- **Qualità degli output più lunghi:** la qualità e la coerenza della voce potrebbero iniziare a
  diminuire con gli output generati più lunghi di qualche minuto. Ti
  consigliamo di dividere le trascrizioni in parti più piccole.
- **Restituzione occasionale di token di testo:** il modello a volte restituisce token di testo anziché token audio, causando l'esito negativo della richiesta del server con un errore `500`. Poiché questo si verifica in modo casuale in una percentuale molto ridotta di richieste, devi implementare una logica di ripetizione automatica nella tua applicazione per gestirle.
- **Rifiuti errati del classificatore di prompt**:i prompt vaghi potrebbero non attivare il classificatore di sintesi vocale, con conseguente rifiuto della richiesta (`PROHIBITED_CONTENT`) o fare in modo che il modello legga ad alta voce le istruzioni di stile e le note del regista. Convalida i prompt aggiungendo un preambolo chiaro che
  indica al modello di sintetizzare la voce ed etichetta esplicitamente il punto in cui
  inizia la trascrizione effettiva.

## Passaggi successivi

- L'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it) di Gemini offre opzioni di generazione audio interattive che puoi alternare ad altre modalità.
- Per lavorare con gli *input* audio, consulta la guida [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/audio?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
