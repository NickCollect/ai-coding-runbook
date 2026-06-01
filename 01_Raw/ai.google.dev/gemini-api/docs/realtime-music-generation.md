---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=it
fetched_at: 2026-06-01T05:59:52.096699+00:00
title: "Generazione di musica in tempo reale con Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generazione di musica in tempo reale con Lyria RealTime

L'API Gemini, che utilizza
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=it),
fornisce l'accesso a un modello di generazione di musica in streaming in tempo reale all'avanguardia. Consente agli sviluppatori di creare applicazioni in cui gli utenti possono creare, controllare e riprodurre musica strumentale in modo interattivo.

La generazione di musica con Lyria RealTime utilizza una connessione di streaming persistente, bidirezionale,
a bassa latenza tramite
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Per scoprire cosa puoi creare con Lyria RealTime, provalo in AI Studio
utilizzando le app [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=it) o
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=it).

## Generare e controllare la musica

Lyria RealTime funziona in modo simile all'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it)
in quanto utilizza i WebSocket per mantenere la comunicazione in tempo reale con il modello.

Il seguente codice mostra come generare musica:

### Python

Questo esempio inizializza la sessione di Lyria RealTime utilizzando `client.aio.live.music.connect()`, quindi invia un prompt iniziale con `session.set_weighted_prompts()` insieme a una configurazione iniziale utilizzando `session.set_music_generation_config`, avvia la generazione di musica utilizzando `session.play()` e configura `receive_audio()` per elaborare i blocchi audio che riceve.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

Questo esempio inizializza la sessione di Lyria RealTime utilizzando `client.live.music.connect()`, quindi invia un prompt iniziale con `session.setWeightedPrompts()` insieme a una configurazione iniziale utilizzando `session.setMusicGenerationConfig`, avvia la generazione di musica utilizzando `session.play()` e configura un callback `onMessage` per elaborare i blocchi audio che riceve.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

Puoi quindi utilizzare `session.play()`, `session.pause()`, `session.stop()` e `session.reset_context()` per avviare, mettere in pausa, interrompere o reimpostare la sessione.

## Controllare la musica in tempo reale

Puoi controllare la generazione di musica in tempo reale inviando prompt e aggiornando i parametri di generazione in tempo reale.

### Prompt di Lyria RealTime

Mentre lo stream è attivo, puoi inviare nuovi messaggi `WeightedPrompt` in qualsiasi momento per modificare la musica generata. Il modello eseguirà una transizione graduale in base al nuovo input.

I prompt devono seguire il formato corretto con un `text` (il prompt effettivo) e un `weight`. Il `weight` può assumere qualsiasi valore tranne `0`. `1.0`
è in genere un buon punto di partenza.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

Tieni presente che le transizioni del modello possono essere un po' brusche quando modifichi drasticamente i prompt, pertanto ti consigliamo di implementare una sorta di dissolvenza incrociata inviando al modello valori di peso intermedi.

### Aggiorna la configurazione

Puoi controllare la generazione di musica aggiornando i parametri di generazione di musica in tempo reale. Non puoi semplicemente aggiornare un parametro, devi impostare l'intera configurazione, altrimenti gli altri campi verranno reimpostati sui valori predefiniti.

Poiché l'aggiornamento del BPM o della scala è una modifica drastica per il modello, dovrai anche indicare di reimpostare il contesto utilizzando `reset_context()` per tenere conto della nuova configurazione. Lo stream non verrà interrotto, ma la transizione sarà difficile. Non è necessario farlo per gli altri parametri.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Guida ai prompt per Lyria RealTime

Di seguito è riportato un elenco non esaustivo di prompt che puoi utilizzare per richiedere a Lyria RealTime:

- Strumenti: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Genere musicale: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Stato d'animo/Descrizione: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Questi sono solo alcuni esempi, Lyria RealTime può fare molto di più. Prova i tuoi prompt.

## Best practice

- Le applicazioni client devono implementare un buffering audio robusto per garantire una riproduzione fluida. In questo modo si tiene conto del jitter di rete e delle lievi variazioni della latenza di generazione.
- Prompt efficaci:
  - Fornisci una descrizione dettagliata. Utilizza aggettivi che descrivono lo stato d'animo, il genere e la strumentazione.
  - Esegui l'iterazione e il controllo in modo graduale. Anziché modificare completamente il prompt, prova ad aggiungere o modificare gli elementi per trasformare la musica in modo più fluido.
  - Prova il peso su `WeightedPrompt` per influenzare la forza con cui un nuovo prompt influisce sulla generazione in corso.

## Dettagli tecnici

Questa sezione descrive le specifiche di come utilizzare la generazione di musica con Lyria RealTime.

### Specifiche

- Formato di output: audio PCM a 16 bit non elaborato
- Frequenza di campionamento: 48 kHz
- Canali: 2 (stereo)

### Controlli

La generazione di musica può essere influenzata in tempo reale inviando messaggi contenenti:

- `WeightedPrompt`: una stringa di testo che descrive un'idea musicale, un genere, uno strumento, uno stato d'animo o una caratteristica. È possibile fornire più prompt per combinare le influenze. Per maggiori dettagli su come richiedere al meglio
  Lyria RealTime, consulta la sezione [precedente](https://ai.google.dev/gemini-api/docs/:?hl=it#steer-music).
- `MusicGenerationConfig`: configurazione per il processo di generazione di musica, che influenza le caratteristiche dell'audio di output. I parametri includono:
  - `guidance`: (float) intervallo: `[0.0, 6.0]`. Valore predefinito: `4.0`.
    Controlla la rigorosità con cui il modello segue i prompt. Una guida più elevata migliora l'aderenza al prompt, ma rende le transizioni più brusche.
  - `bpm`: (int) intervallo: `[60, 200]`.
    Imposta i battiti al minuto che vuoi per la musica generata. Devi interrompere/riprodurre o reimpostare il contesto affinché il modello tenga conto del nuovo BPM.
  - `density`: (float) intervallo: `[0.0, 1.0]`.
    Controlla la densità delle note/dei suoni musicali. I valori più bassi producono musica più sparsa, mentre i valori più alti producono musica più "intensa".
  - `brightness`: (float) intervallo: `[0.0, 1.0]`.
    Regola la qualità tonale. I valori più alti producono audio con un suono più "brillante", in genere enfatizzando le frequenze più alte.
  - `scale`: (Enum) imposta la scala musicale (chiave e modalità) per la generazione. Utilizza i
    [`Scale` valori enum](#scale-enum) forniti dall'SDK. Devi interrompere/riprodurre o reimpostare il contesto affinché il modello tenga conto della nuova scala.
  - `mute_bass`: (bool) valore predefinito: `False`.
    Controlla se il modello riduce i bassi degli output.
  - `mute_drums`: (bool) valore predefinito: `False`.
    Controlla se il modello riduce la batteria degli output.
  - `only_bass_and_drums`: (bool) valore predefinito: `False`.
    Indica al modello di provare a generare solo bassi e batteria.
  - `music_generation_mode`: (Enum) indica al modello se deve concentrarsi sulla `QUALITY` (valore predefinito) o sulla `DIVERSITY` della musica. Può anche essere impostato su `VOCALIZATION` per consentire al modello di generare vocalizzazioni come un altro strumento (aggiungile come nuovi prompt).
- `PlaybackControl`: comandi per controllare gli aspetti della riproduzione, ad esempio riproduci, metti in pausa, interrompi o reimposta il contesto.

Per `bpm`, `density`, `brightness` e `scale`, se non viene fornito alcun valore, il modello deciderà qual è il migliore in base ai prompt iniziali.

Anche i parametri più classici come `temperature` (da 0.0 a 3.0, valore predefinito 1.1), `top_k` (da 1 a 1000, valore predefinito 40) e `seed` (da 0 a 2.147.483.647, selezionato in modo casuale per impostazione predefinita) sono personalizzabili in `MusicGenerationConfig`.

#### Valori enum della scala

Di seguito sono riportati tutti i valori della scala che il modello può accettare:

| Valore enum | Scala / chiave |
| --- | --- |
| `C_MAJOR_A_MINOR` | Do maggiore / La minore |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Re♭ maggiore / Si♭ minore |
| `D_MAJOR_B_MINOR` | Re maggiore / Si minore |
| `E_FLAT_MAJOR_C_MINOR` | Mi♭ maggiore / Do minore |
| `E_MAJOR_D_FLAT_MINOR` | Mi maggiore / Do♯/Re♭ minore |
| `F_MAJOR_D_MINOR` | Fa maggiore / Re minore |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol♭ maggiore / Mi♭ minore |
| `G_MAJOR_E_MINOR` | Sol maggiore / Mi minore |
| `A_FLAT_MAJOR_F_MINOR` | La♭ maggiore / Fa minore |
| `A_MAJOR_G_FLAT_MINOR` | La maggiore / Fa♯/Sol♭ minore |
| `B_FLAT_MAJOR_G_MINOR` | Si♭ maggiore / Sol minore |
| `B_MAJOR_A_FLAT_MINOR` | Si maggiore / Sol♯/La♭ minore |
| `SCALE_UNSPECIFIED` | Valore predefinito / Il modello decide |

Il modello è in grado di guidare le note riprodotte, ma non distingue tra le chiavi relative. Pertanto, ogni enum corrisponde sia alla relativa maggiore che alla relativa minore. Ad esempio, `C_MAJOR_A_MINOR` corrisponderebbe a tutti i tasti bianchi di un pianoforte e `F_MAJOR_D_MINOR` a tutti i tasti bianchi tranne il Si♭.

### Limitazioni

- Solo strumentale: il modello genera solo musica strumentale.
- Sicurezza: i prompt vengono controllati dai filtri di sicurezza. I prompt che attivano i filtri verranno ignorati e nel campo `filtered_prompt` dell'output verrà scritta una spiegazione.
- Filigrana: l'audio di output è sempre filigranato per l'identificazione in base ai nostri principi di AI responsabile
  [responsabile](https://ai.google/responsibility/principles/?hl=it).

## Passaggi successivi

- Genera brani completi e tracce vocali con [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=it),
- Anziché musica, scopri come generare conversazioni con più speaker utilizzando
  i [modelli TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it),
- Scopri come generare [immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it) o [video](https://ai.google.dev/gemini-api/docs/video?hl=it),
- Anziché generare musica o audio, scopri come Gemini può
  [comprendere i file audio](https://ai.google.dev/gemini-api/docs/audio?hl=it),
- Avvia una conversazione in tempo reale con Gemini utilizzando l'
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).

Esplora il [ricettario](https://github.com/google-gemini/cookbook) per altri
esempi di codice e tutorial.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-28 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-28 UTC."],[],[]]
