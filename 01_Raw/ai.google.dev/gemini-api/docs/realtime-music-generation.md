---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=id
fetched_at: 2026-05-05T20:40:48.583028+00:00
title: "Pembuatan musik real-time menggunakan Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pembuatan musik real-time menggunakan Lyria RealTime

Gemini API, menggunakan
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=id),
memberikan akses ke model pembuatan musik streaming real-time canggih. API ini memungkinkan developer membuat aplikasi tempat pengguna dapat membuat, mengarahkan, dan memainkan musik instrumental secara interaktif.

Pembuatan musik Lyria RealTime menggunakan koneksi streaming dua arah yang persisten dan latensi rendah menggunakan [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Untuk merasakan apa yang dapat dibuat menggunakan Lyria RealTime, coba di AI Studio menggunakan aplikasi [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=id) atau [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=id).

## Membuat dan mengontrol musik

Lyria RealTime berfungsi mirip dengan [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id)
karena menggunakan Websocket untuk mempertahankan komunikasi real-time dengan model.

Kode berikut menunjukkan cara membuat musik:

### Python

Contoh ini menginisialisasi sesi Lyria RealTime menggunakan
`client.aio.live.music.connect()`, lalu mengirimkan
perintah awal dengan `session.set_weighted_prompts()` bersama dengan
konfigurasi awal menggunakan `session.set_music_generation_config`, memulai
pembuatan musik menggunakan `session.play()`, dan menyiapkan
`receive_audio()` untuk memproses potongan audio yang diterimanya.

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

Contoh ini menginisialisasi sesi Lyria RealTime menggunakan
`client.live.music.connect()`, lalu mengirimkan
perintah awal dengan `session.setWeightedPrompts()` bersama dengan
konfigurasi awal menggunakan `session.setMusicGenerationConfig`, memulai
pembuatan musik menggunakan `session.play()`, dan menyiapkan
callback `onMessage` untuk memproses potongan audio yang diterimanya.

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

Kemudian, Anda dapat menggunakan `session.play()`, `session.pause()`, `session.stop()`, dan `session.reset_context()` untuk memulai, menjeda, menghentikan, atau mereset sesi.

## Mengarahkan musik secara real-time

Anda dapat mengarahkan pembuatan musik secara real time dengan mengirimkan perintah dan memperbarui parameter pembuatan secara real time.

### Perintah RealTime Lyria

Saat streaming aktif, Anda dapat mengirim pesan `WeightedPrompt` baru kapan saja untuk mengubah musik yang dihasilkan. Model akan bertransisi dengan lancar berdasarkan input baru.

Perintah harus mengikuti format yang benar dengan `text` (perintah sebenarnya), dan `weight`. `weight` dapat mengambil nilai apa pun kecuali `0`. `1.0`
biasanya merupakan titik awal yang baik.

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

Perhatikan bahwa transisi model dapat sedikit tiba-tiba saat mengubah perintah secara drastis, jadi sebaiknya terapkan semacam cross-fade dengan mengirimkan nilai bobot perantara ke model.

### Mengupdate konfigurasi

Anda dapat mengarahkan pembuatan musik dengan memperbarui parameter pembuatan musik secara real time. Anda tidak dapat hanya memperbarui parameter, Anda harus menetapkan seluruh
konfigurasi. Jika tidak, kolom lainnya akan direset kembali ke nilai
defaultnya.

Karena memperbarui bpm atau skala adalah perubahan drastis bagi model, Anda juga perlu memberi tahu model untuk mereset konteksnya menggunakan `reset_context()` agar memperhitungkan konfigurasi baru. Tindakan ini tidak akan menghentikan streaming, tetapi akan menjadi transisi yang sulit. Anda tidak perlu melakukannya untuk parameter lainnya.

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

## Panduan perintah untuk Lyria RealTime

Berikut adalah daftar perintah tidak lengkap yang dapat Anda gunakan untuk memicu Lyria RealTime:

- Instrumen: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
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
- Genre Musik: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
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
- Mood/Deskripsi: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Ini hanyalah beberapa contoh, Lyria RealTime dapat melakukan lebih banyak hal. Bereksperimenlah dengan perintah Anda sendiri.

## Praktik terbaik

- Aplikasi klien harus menerapkan buffering audio yang andal untuk memastikan pemutaran yang lancar. Hal ini membantu memperhitungkan jitter jaringan dan sedikit variasi dalam latensi pembuatan.
- Penulisan perintah yang efektif:
  - Berikan gambaran yang jelas. Gunakan kata sifat yang menggambarkan mood, genre, dan instrumentasi.
  - Lakukan iterasi dan arahkan secara bertahap. Daripada mengubah perintah sepenuhnya,
    coba tambahkan atau ubah elemen untuk mengubah musik dengan lebih lancar.
  - Bereksperimenlah dengan bobot pada `WeightedPrompt` untuk memengaruhi seberapa kuat perintah baru memengaruhi pembuatan yang sedang berlangsung.

## Detail teknis

Bagian ini menjelaskan secara spesifik cara menggunakan pembuatan musik RealTime Lyria.

### Spesifikasi

- Format output: Audio PCM 16-bit Mentah
- Frekuensi sampel: 48 kHz
- Saluran: 2 (stereo)

### Kontrol

Pembuatan musik dapat dipengaruhi secara real time dengan mengirim pesan yang berisi:

- `WeightedPrompt`: String teks yang mendeskripsikan ide musik, genre, instrumen, suasana hati, atau karakteristik. Beberapa perintah dapat diberikan untuk memadukan pengaruh. Lihat [di atas](https://ai.google.dev/gemini-api/docs/:?hl=id#steer-music) untuk mengetahui detail selengkapnya tentang cara terbaik untuk memberikan perintah ke
  Lyria RealTime.
- `MusicGenerationConfig`: Konfigurasi untuk proses pembuatan musik, yang memengaruhi karakteristik audio output. Parameter
  mencakup:
  - `guidance`: (float) Rentang: `[0.0, 6.0]`. Default: `4.0`.
    Mengontrol seberapa ketat model mengikuti perintah. Panduan yang lebih tinggi meningkatkan kepatuhan terhadap perintah, tetapi membuat transisi lebih tiba-tiba.
  - `bpm`: (int) Rentang: `[60, 200]`.
    Menetapkan Denyut Per Menit yang Anda inginkan untuk musik yang dihasilkan. Anda perlu menghentikan/memutar atau mereset konteks model agar memperhitungkan bpm baru.
  - `density`: (float) Rentang: `[0.0, 1.0]`.
    Mengontrol kepadatan not/suara musik. Nilai yang lebih rendah menghasilkan musik yang lebih jarang; nilai yang lebih tinggi menghasilkan musik yang "lebih ramai".
  - `brightness`: (float) Rentang: `[0.0, 1.0]`.
    Menyesuaikan kualitas tonal. Nilai yang lebih tinggi menghasilkan audio yang terdengar "lebih cerah", yang umumnya menekankan frekuensi yang lebih tinggi.
  - `scale`: (Enum)
    Menetapkan skala musik (Key dan Mode) untuk pembuatan. Gunakan
    nilai enum [`Scale`](#scale-enum) yang disediakan oleh SDK. Anda perlu menghentikan/memutar atau mereset konteks model agar memperhitungkan skala baru.
  - `mute_bass`: (bool) Default: `False`.
    Mengontrol apakah model mengurangi bass output.
  - `mute_drums`: (bool) Default: `False`.
    Mengontrol apakah output model mengurangi drum output.
  - `only_bass_and_drums`: (bool) Default: `False`.
    Arahkan model untuk mencoba hanya menghasilkan output bass dan drum.
  - `music_generation_mode`: (Enum)
    Menunjukkan kepada model apakah model harus berfokus pada `QUALITY` (nilai default) atau
    `DIVERSITY` musik. Setelan ini juga dapat disetel ke `VOCALIZATION` agar model membuat vokal sebagai instrumen lain (tambahkan sebagai perintah baru).
- `PlaybackControl`: Perintah untuk mengontrol aspek pemutaran, seperti putar, jeda,
  berhenti, atau reset konteks.

Untuk `bpm`, `density`, `brightness`, dan `scale`, jika tidak ada nilai yang diberikan, model akan memutuskan apa yang terbaik sesuai dengan perintah awal Anda.

Parameter yang lebih klasik seperti `temperature` (0,0 hingga 3,0, default 1,1), `top_k`
(1 hingga 1000, default 40), dan `seed` (0 hingga 2.147.483.647, dipilih secara acak secara
default) juga dapat disesuaikan di `MusicGenerationConfig`.

#### Nilai Enum Skala

Berikut adalah semua nilai skala yang dapat diterima model:

| Nilai Enum | Skala / Kunci |
| --- | --- |
| `C_MAJOR_A_MINOR` | C mayor / A minor |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ mayor / B♭ minor |
| `D_MAJOR_B_MINOR` | D mayor / B minor |
| `E_FLAT_MAJOR_C_MINOR` | E♭ mayor / C minor |
| `E_MAJOR_D_FLAT_MINOR` | E mayor / C♯/D♭ minor |
| `F_MAJOR_D_MINOR` | F mayor / D minor |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ mayor / E♭ minor |
| `G_MAJOR_E_MINOR` | G mayor / E minor |
| `A_FLAT_MAJOR_F_MINOR` | A♭ mayor / F minor |
| `A_MAJOR_G_FLAT_MINOR` | A mayor / F♯/G♭ minor |
| `B_FLAT_MAJOR_G_MINOR` | B♭ mayor / G minor |
| `B_MAJOR_A_FLAT_MINOR` | B mayor / G♯/A♭ minor |
| `SCALE_UNSPECIFIED` | Default / Model memutuskan |

Model ini dapat memandu not yang dimainkan, tetapi tidak membedakan antara nada relatif. Jadi, setiap enum sesuai dengan
mayor dan minor relatif. Misalnya, `C_MAJOR_A_MINOR` akan sesuai dengan semua
tombol putih piano, dan `F_MAJOR_D_MINOR` akan menjadi semua tombol putih
kecuali B flat.

### Batasan

- Khusus instrumental: Model hanya menghasilkan musik instrumental.
- Keamanan: Perintah diperiksa oleh filter keamanan. Perintah yang memicu filter
  akan diabaikan dan penjelasan akan ditulis di kolom
  `filtered_prompt` output.
- Pemberian watermark: Audio output selalu diberi watermark untuk identifikasi sesuai dengan prinsip [AI Bertanggung Jawab](https://ai.google/responsibility/principles/?hl=id) kami.

## Langkah berikutnya

- Buat lagu lengkap dan trek vokal dengan [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=id),
- Daripada musik, pelajari cara membuat percakapan multi-penutur menggunakan
  [model TTS](https://ai.google.dev/gemini-api/docs/audio-generation?hl=id),
- Temukan cara membuat [gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) atau [video](https://ai.google.dev/gemini-api/docs/video?hl=id).
- Daripada membuat musik atau audio, cari tahu cara Gemini dapat [memahami file Audio](https://ai.google.dev/gemini-api/docs/audio?hl=id),
- Lakukan percakapan real-time dengan Gemini menggunakan
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id).

Pelajari [Cookbook](https://github.com/google-gemini/cookbook) untuk mengetahui contoh kode dan tutorial lainnya.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
