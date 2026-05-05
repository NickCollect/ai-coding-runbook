---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id
fetched_at: 2026-05-05T19:47:27.461253+00:00
title: "Session management with Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Session management with Live API

Di Live API, sesi mengacu pada koneksi persisten
tempat input dan output di-streaming secara terus-menerus melalui koneksi yang sama (baca selengkapnya tentang [cara kerjanya](https://ai.google.dev/gemini-api/docs/live?hl=id)).
Desain sesi unik ini memungkinkan latensi rendah dan mendukung fitur unik, tetapi juga dapat menimbulkan tantangan, seperti batas waktu sesi dan penghentian awal.
Panduan ini membahas strategi untuk mengatasi tantangan pengelolaan sesi yang dapat muncul saat menggunakan Live API.

## Masa aktif sesi

Tanpa kompresi, sesi khusus audio dibatasi hingga 15 menit,
dan sesi audio-video dibatasi hingga 2 menit. Jika batas ini terlampaui, sesi (dan oleh karena itu, koneksi) akan dihentikan, tetapi Anda dapat menggunakan [kompresi jendela konteks](#context-window-compression) untuk memperpanjang sesi hingga durasi yang tidak terbatas.

Masa aktif koneksi juga dibatasi, hingga sekitar 10 menit. Saat koneksi berakhir, sesi juga akan berakhir. Dalam hal ini, Anda dapat mengonfigurasi satu sesi agar tetap aktif di beberapa koneksi menggunakan [kelanjutan sesi](#session-resumption).
Anda juga akan menerima [pesan GoAway](#goaway-message) sebelum
koneksi berakhir, sehingga Anda dapat mengambil tindakan lebih lanjut.

## Kompresi jendela konteks

Untuk mengaktifkan sesi yang lebih panjang dan menghindari penghentian koneksi yang tiba-tiba, Anda dapat mengaktifkan kompresi jendela konteks dengan menyetel kolom [contextWindowCompression](https://ai.google.dev/api/live?hl=id#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression) sebagai bagian dari konfigurasi sesi.

Di [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=id#contextwindowcompressionconfig), Anda dapat mengonfigurasi
[mekanisme jendela geser](https://ai.google.dev/api/live?hl=id#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
dan [jumlah token](https://ai.google.dev/api/live?hl=id#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
yang memicu kompresi.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## Melanjutkan sesi

Untuk mencegah penghentian sesi saat server secara berkala mereset koneksi WebSocket, konfigurasi kolom [sessionResumption](https://ai.google.dev/api/live?hl=id#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption) dalam [konfigurasi penyiapan](https://ai.google.dev/api/live?hl=id#BidiGenerateContentSetup).

Meneruskan konfigurasi ini akan menyebabkan server mengirim pesan [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=id#SessionResumptionUpdate), yang dapat digunakan untuk melanjutkan sesi dengan meneruskan token kelanjutan terakhir sebagai [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=id#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle) dari koneksi berikutnya.

Token kelanjutan berlaku selama 2 jam setelah penghentian sesi terakhir.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## Menerima pesan sebelum sesi terputus

Server mengirim pesan [GoAway](https://ai.google.dev/api/live?hl=id#GoAway) yang menandakan bahwa koneksi saat ini akan segera dihentikan. Pesan ini mencakup [timeLeft](https://ai.google.dev/api/live?hl=id#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left),
yang menunjukkan waktu yang tersisa dan memungkinkan Anda mengambil tindakan lebih lanjut sebelum
koneksi akan dihentikan sebagai DIBATALKAN.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## Menerima pesan saat pembuatan selesai

Server mengirimkan pesan [generationComplete](https://ai.google.dev/api/live?hl=id#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
yang menandakan bahwa model telah selesai membuat respons.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## Langkah berikutnya

Pelajari cara lainnya untuk menggunakan Live API dalam panduan
[Kemampuan](https://ai.google.dev/gemini-api/docs/live?hl=id) lengkap,
halaman [Penggunaan alat](https://ai.google.dev/gemini-api/docs/live-tools?hl=id), atau
[buku resep Live API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-04-29 UTC."],[],[]]
