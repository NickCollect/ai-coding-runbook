---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=pl
fetched_at: 2026-06-29T05:29:16.238639+00:00
title: "Generowanie muzyki w\u00a0czasie rzeczywistym za pomoc\u0105 Lyrii RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie muzyki w czasie rzeczywistym za pomocą Lyrii RealTime

Interfejs Gemini API, który korzysta z
[Lyrii RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=pl),
zapewnia dostęp do najnowocześniejszego modelu generowania muzyki w czasie rzeczywistym. Umożliwia on deweloperom tworzenie aplikacji, w których użytkownicy mogą interaktywnie tworzyć, stale sterować i wykonywać muzykę instrumentalną.

Generowanie muzyki za pomocą Lyrii RealTime wykorzystuje trwałe, dwukierunkowe,
połączenie strumieniowe o niskim opóźnieniu za pomocą
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Aby przekonać się, co można stworzyć za pomocą Lyrii RealTime, wypróbuj ją w AI Studio
korzystając z [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=pl) lub
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=pl) aplikacji.

## Generowanie muzyki i sterowanie nią

Lyria RealTime działa podobnie jak interfejs [Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl)
, ponieważ używa protokołu Websocket do utrzymywania komunikacji z modelem w czasie rzeczywistym.

Poniższy kod pokazuje, jak generować muzykę:

### Python

Ten przykład inicjuje sesję Lyria RealTime za pomocą `client.aio.live.music.connect()`, a następnie wysyła początkowy prompt za pomocą `session.set_weighted_prompts()` wraz z początkową konfiguracją za pomocą `session.set_music_generation_config`, rozpoczyna generowanie muzyki za pomocą `session.play()` i konfiguruje `receive_audio()` do przetwarzania otrzymywanych fragmentów audio.

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

Ten przykład inicjuje sesję Lyria RealTime za pomocą `client.live.music.connect()`, a następnie wysyła początkowy prompt za pomocą `session.setWeightedPrompts()` wraz z początkową konfiguracją za pomocą `session.setMusicGenerationConfig`, rozpoczyna generowanie muzyki za pomocą `session.play()` i konfiguruje wywołanie zwrotne `onMessage` do przetwarzania otrzymywanych fragmentów audio.

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

Następnie możesz użyć `session.play()`, `session.pause()`, `session.stop()` i `session.reset_context()`, aby rozpocząć, wstrzymać, zatrzymać lub zresetować sesję.

## Sterowanie muzyką w czasie rzeczywistym

Możesz sterować generowaniem muzyki w czasie rzeczywistym, wysyłając prompty i aktualizując parametry generowania w czasie rzeczywistym.

### Prompt Lyria RealTime

Gdy strumień jest aktywny, możesz w dowolnym momencie wysyłać nowe wiadomości `WeightedPrompt`, aby zmieniać generowaną muzykę. Model będzie płynnie przechodzić na podstawie nowych danych wejściowych.

Prompty muszą mieć odpowiedni format z elementami `text` (rzeczywisty prompt) i `weight`. Wartość `weight` może przyjmować dowolną wartość z wyjątkiem `0`. Zwykle dobrym punktem wyjścia jest `1.0`.

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

Pamiętaj, że przejścia modelu mogą być nieco nagłe, gdy prompty są drastycznie zmieniane, dlatego zalecamy wdrożenie pewnego rodzaju przenikania przez wysyłanie do modelu wartości pośrednich.

### Aktualizowanie konfiguracji

Możesz sterować generowaniem muzyki, aktualizując parametry generowania muzyki w czasie rzeczywistym. Nie możesz po prostu zaktualizować parametru. Musisz ustawić całą konfigurację, w przeciwnym razie inne pola zostaną zresetowane do wartości domyślnych.

Ponieważ aktualizowanie bpm lub skali jest drastyczną zmianą dla modelu, musisz też poinformować go, aby zresetował swój kontekst za pomocą `reset_context()`, aby uwzględnić nową konfigurację. Nie spowoduje to zatrzymania strumienia, ale będzie to trudne przejście. Nie musisz tego robić w przypadku innych parametrów.

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

## Przewodnik po promptach dla Lyrii RealTime

Oto niepełna lista promptów, których możesz używać do promptowania Lyrii RealTime:

- Instrumenty: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
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
- Gatunek muzyczny: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
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
- Nastrój/opis: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

To tylko kilka przykładów. Lyria RealTime potrafi znacznie więcej. Eksperymentuj z własnymi promptami.

## Sprawdzone metody

- Aplikacje klienckie muszą implementować niezawodne buforowanie dźwięku, aby zapewnić płynne odtwarzanie. Pomaga to uwzględnić wahania sieci i niewielkie różnice w opóźnieniu generowania.
- Skuteczne promptowanie:
  - Stosuj styl opisowy. Używaj przymiotników opisujących nastrój, gatunek i instrumentację.
  - Iteruj i steruj stopniowo. Zamiast całkowicie zmieniać prompta, spróbuj dodawać lub modyfikować elementy, aby płynniej przekształcać muzykę.
  - Eksperymentuj z wagą w `WeightedPrompt`, aby wpływać na to, jak silnie nowy prompt wpływa na bieżące generowanie.

## Szczegóły techniczne

W tej sekcji opisujemy szczegóły korzystania z generowania muzyki za pomocą Lyrii RealTime.

### Specyfikacja

- Format wyjściowy: surowy dźwięk PCM 16-bitowy
- Częstotliwość próbkowania: 48 kHz
- Liczba kanałów: 2 (stereo)

### Opcje

Na generowanie muzyki można wpływać w czasie rzeczywistym, wysyłając wiadomości zawierające:

- `WeightedPrompt`: ciąg tekstowy opisujący pomysł muzyczny, gatunek, instrument, nastrój lub cechę. Można podać kilka promptów, aby połączyć wpływy. Więcej informacji o tym, jak najlepiej promptować
  Lyrię RealTime, znajdziesz [powyżej](https://ai.google.dev/gemini-api/docs/:?hl=pl#steer-music).
- `MusicGenerationConfig`: konfiguracja procesu generowania muzyki, która wpływa na cechy wyjściowego dźwięku. Parametry obejmują:
  - `guidance`: (float) zakres: `[0.0, 6.0]`. Domyślnie: `4.0`.
    Określa, jak ściśle model ma przestrzegać promptów. Wyższa wartość guidance poprawia zgodność z promptem, ale sprawia, że przejścia są bardziej nagłe.
  - `bpm`: (int) zakres: `[60, 200]`.
    Ustawia liczbę uderzeń na minutę, którą chcesz uzyskać w generowanej muzyce. Aby model uwzględnił nowe bpm, musisz zatrzymać/odtwarzać lub zresetować kontekst.
  - `density`: (float) zakres: `[0.0, 1.0]`.
    Określa gęstość nut/dźwięków. Niższe wartości powodują rzadszą muzykę, a wyższe – „bardziej zajętą”.
  - `brightness`: (float) zakres: `[0.0, 1.0]`.
    Dostosowuje jakość tonalną. Wyższe wartości powodują „jaśniejszy” dźwięk, zwykle podkreślając wyższe częstotliwości.
  - `scale`: (Enum) ustawia skalę muzyczną (tonację i tryb) dla generowania. Użyj wartości typu wyliczeniowego
    [`Scale` udostępnionych przez pakiet SDK.](#scale-enum) Aby model uwzględnił nową skalę, musisz zatrzymać/odtwarzać lub zresetować kontekst.
  - `mute_bass`: (bool) domyślnie: `False`.
    Określa, czy model ma zmniejszać bas w danych wyjściowych.
  - `mute_drums`: (bool) domyślnie: `False`.
    Określa, czy model ma zmniejszać perkusję w danych wyjściowych.
  - `only_bass_and_drums`: (bool) domyślnie: `False`.
    Steruj modelem, aby próbował generować tylko bas i perkusję.
  - `music_generation_mode`: (Enum) wskazuje modelowi, czy ma się skupić na `QUALITY` (wartość domyślna) czy na `DIVERSITY` muzyki. Można też ustawić wartość `VOCALIZATION`, aby model generował wokalizacje jako kolejny instrument (dodaj je jako nowe prompty).
- `PlaybackControl`: polecenia sterowania odtwarzaniem, takie jak odtwarzanie, wstrzymywanie, zatrzymywanie lub resetowanie kontekstu.

Jeśli nie podasz wartości dla `bpm`, `density`, `brightness` i `scale`, model zdecyduje, co jest najlepsze, na podstawie początkowych promptów.

W `MusicGenerationConfig` można też dostosować bardziej klasyczne parametry, takie jak `temperature` (od 0,0 do 3,0, domyślnie 1,1), `top_k` (od 1 do 1000, domyślnie 40) i `seed` (od 0 do 2 147 483 647, domyślnie wybierany losowo).

#### Wartości typu wyliczeniowego Scale

Oto wszystkie wartości skali, które może zaakceptować model:

| Wartość typu wyliczeniowego | Skala / tonacja |
| --- | --- |
| `C_MAJOR_A_MINOR` | C-dur / a-moll |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Des-dur / b-moll |
| `D_MAJOR_B_MINOR` | D-dur / h-moll |
| `E_FLAT_MAJOR_C_MINOR` | Es-dur / c-moll |
| `E_MAJOR_D_FLAT_MINOR` | E-dur / cis-moll/des-moll |
| `F_MAJOR_D_MINOR` | F-dur / d-moll |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Ges-dur / es-moll |
| `G_MAJOR_E_MINOR` | G-dur / e-moll |
| `A_FLAT_MAJOR_F_MINOR` | As-dur / f-moll |
| `A_MAJOR_G_FLAT_MINOR` | A-dur / fis-moll/ges-moll |
| `B_FLAT_MAJOR_G_MINOR` | B-dur / g-moll |
| `B_MAJOR_A_FLAT_MINOR` | H-dur / gis-moll/as-moll |
| `SCALE_UNSPECIFIED` | Domyślna / model decyduje |

Model może kierować odtwarzanymi nutami, ale nie rozróżnia tonacji względnych. Dlatego każdy typ wyliczeniowy odpowiada zarówno względnemu durowi, jak i molowi. Na przykład `C_MAJOR_A_MINOR` odpowiadałby wszystkim białym klawiszom fortepianu, a `F_MAJOR_D_MINOR` – wszystkim białym klawiszom z wyjątkiem b.

### Ograniczenia

- Tylko instrumentalne: model generuje tylko muzykę instrumentalną.
- Bezpieczeństwo: prompty są sprawdzane przez filtry bezpieczeństwa. Prompty, które uruchamiają filtry, będą ignorowane. W takim przypadku w polu `filtered_prompt` danych wyjściowych pojawi się wyjaśnienie.
- Oznaczanie znakami wodnymi: wyjściowy dźwięk jest zawsze oznaczony znakiem wodnym w celu identyfikacji zgodnie z
  naszymi [zasadami odpowiedzialnej AI](https://ai.google/responsibility/principles/?hl=pl).

## Co dalej?

- Generuj całe utwory i ścieżki wokalne za pomocą [Lyrii 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=pl).
- Zamiast muzyki dowiedz się, jak generować rozmowy z udziałem wielu osób za pomocą
  modeli [TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl).
- Dowiedz się, jak generować [obrazy](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl) lub [filmy](https://ai.google.dev/gemini-api/docs/video?hl=pl).
- Zamiast generować muzykę lub dźwięk, dowiedz się, jak Gemini może
  [rozumieć pliki audio](https://ai.google.dev/gemini-api/docs/audio?hl=pl).
- Prowadź rozmowę z Gemini w czasie rzeczywistym za pomocą interfejsu
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl).

Więcej
przykładów kodu i samouczków znajdziesz w [Cookbook](https://github.com/google-gemini/cookbook).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-22 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-22 UTC."],[],[]]
