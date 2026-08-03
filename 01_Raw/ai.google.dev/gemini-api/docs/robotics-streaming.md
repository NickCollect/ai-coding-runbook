---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id
fetched_at: 2026-08-03T04:36:53.611711+00:00
title: "Robotika dengan streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Robotika dengan streaming

Endpoint model `gemini-robotics-er-2-streaming-preview` mengekspos endpoint streaming khusus yang terintegrasi dengan [Live
API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=id), sehingga memungkinkan interaksi dua arah secara real-time antara aplikasi Anda dan robot. Hal ini membuatnya
cocok untuk agen yang memerlukan loop umpan balik cepat dan respons reaktif terhadap
lingkungan.

[Coba di Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=id)
[Meng-clone aplikasi contoh dari GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Kasus penggunaan

- **Koordinasi multi-robot**: Beberapa robot yang mengomunikasikan status tugas
  dan mendelegasikan subtugas melalui sesi bersama.
- **Pemantauan berkelanjutan**: Robot yang mengamati suatu adegan dan memicu tindakan saat peristiwa tertentu terjadi, seperti saat kontainer mencapai tingkat pengisian tertentu.
- **Gudang dan logistik**: Agen pengambilan dan pengemasan yang memverifikasi item secara visual, melacak progres pengemasan, dan memulihkan dari error.

## Spesifikasi teknis

Tabel berikut menguraikan spesifikasi teknis untuk
Live API:

| Kategori | Detail |
| --- | --- |
| Modalitas input | Audio (audio PCM 16-bit mentah, 16 kHz, little-endian), gambar (JPEG <= 1 FPS), teks |
| Modalitas output | Teks |
| Protokol | Koneksi WebSocket stateful (WSS) |

## Membangun penyiapan agentic

Setiap agen robotik yang dibangun di Live API mengikuti tiga langkah:

1. **Mendeklarasikan kemampuan robot sebagai alat.** Setiap tindakan yang dapat dilakukan robot —
   bernavigasi, menggenggam, berbicara — menjadi deklarasi fungsi dengan nama,
   deskripsi, dan skema parameter. Tindakan fisik harus menggunakan
   `"behavior": "BLOCKING"` sehingga model menunggu robot selesai sebelum
   memilih langkah berikutnya.
2. **Streaming input multimodal ke sesi persisten.** Buka sesi `live.connect`
   dan biarkan sesi tetap terbuka selama tugas berlangsung. Mengirim frame video, audio, atau teks saat diterima dari sensor robot Anda.
3. **Menangani panggilan alat dalam loop penerimaan.** Setiap kali model memilih tindakan, model akan mengirim pesan `tool_call`. Loop penerimaan Anda menjalankan
   fungsi terhadap robot SDK Anda dan mengirim kembali `tool_response`. Sesi tetap terbuka, dan model memilih tindakan berikutnya berdasarkan hasilnya.

Bagian berikut menunjukkan cara menerapkan langkah-langkah ini ke tiga pola umum:
loop agen dasar, pemantauan adegan proaktif dengan heartbeat, dan perutean
ucapan melalui TTS sebagai alat.

## Mengatur robot melalui panggilan fungsi

Contoh berikut menunjukkan ketiga langkah yang digabungkan dalam satu skrip
Python.

Langkah 1 — definisi alat — mendeklarasikan kemampuan robot sebagai deklarasi fungsi. Fungsi `navigate` menggunakan `"behavior": "BLOCKING"` sehingga
model menunggu robot mencapai titik jalan sebelum memanggil alat lain.
Tambahkan lebih banyak deklarasi fungsi dalam daftar yang sama untuk mengekspos kemampuan robot tambahan.

Langkah 2 — helper input — menampilkan tiga fungsi yang mengalirkan input modalitas yang berbeda ke dalam sesi: `send_text` untuk perintah, `send_image` untuk frame kamera dengan perintah teks opsional, dan `send_audio` untuk audio PCM mentah dari mikrofon.

Langkah 3 — loop penerimaan — berjalan secara bersamaan dan menangani dua jenis pesan:
pesan `server_content` (output teks model) dan pesan `tool_call`
(model yang meminta tindakan robot). Saat panggilan alat tiba, loop memanggil
`execute_tool` — stub yang Anda ganti dengan SDK robot asli — lalu mengirim kembali
`execute_tool` sehingga model dapat memilih tindakan berikutnya.`tool_response`

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

Loop penerimaan tetap aktif setelah setiap respons alat. Model ini membuat
dan merevisi rencana jangka panjang tanpa Anda mengenkode seluruh urutan tindakan
terlebih dahulu.

## Penalaran ruang-waktu proaktif

Live API melakukan streaming video, tetapi frame video saja tidak memicu giliran penalaran baru. Frame video harus disertai dengan perintah teks atau audio untuk memicu respons model. Lihat
[Kemampuan Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=id) untuk
detail selengkapnya.

Untuk mengaktifkan penalaran proaktif, terapkan **detak jantung**: kirim frame kamera terbaru secara berkala, diikuti dengan perintah teks singkat yang memaksa model untuk memeriksa pemandangan dan membuat keputusan yang jelas. Input video dibatasi kecepatan frame-nya menjadi
satu frame per detik.

Tambahkan coroutine ini bersama dengan loop penerimaan dari bagian sebelumnya. Tugas ini
berjalan sebagai tugas `asyncio` terpisah dalam sesi yang sama:

```
async def heartbeat(session, camera):  # camera is your robot camera API
    while True:
        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )
        await asyncio.sleep(1)
```

Anda tidak perlu menjeda detak jantung selama tindakan robot. Jika digunakan sebagai
**detektor keberhasilan implisit**, dengan terus menjalankannya, model dapat terus
mengamati tindakan yang sedang berlangsung (melacak apakah cengkeraman aman, penuangan
tepat sasaran, atau objek ditempatkan dengan benar) dan bereaksi saat
hasilnya menjadi jelas.

Pesan detak jantung berfungsi sebagai giliran pengguna dan mengganggu pembuatan model yang sedang berlangsung.
Lihat
[Panduan Live API tentang gangguan](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=id#interruptions)
untuk memahami cara Live API menangani perilaku ini.

## Output audio melalui TTS eksternal

Gemini Robotics ER 2 menampilkan teks. Aplikasi Anda merutekan respons yang telah selesai
ke penyedia TTS terpisah (seperti
[Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id)) melalui callback yang disuntikkan.
Hal ini membuat latensi ucapan, pemilihan suara, dan perilaku interupsi tetap di bawah kendali Anda, dan memungkinkan Anda mengganti backend TTS tanpa mengubah logika agen.

Anda juga dapat mendeklarasikan TTS sebagai alat sehingga model memperlakukan "ucapkan sesuatu" sama seperti "gerakkan lengan". Tambahkan deklarasi fungsi berikut ke daftar `tools`
dari bagian pertama:

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

Dengan membungkus TTS dalam deklarasi fungsi, model menangani ucapan melalui jalur panggilan alat yang sama dengan tindakan robot lainnya. Aplikasi Anda memenuhi panggilan dengan callback yang disuntikkan.

## Contoh di GitHub

Untuk contoh kerja lengkap, termasuk demo pengambilan camilan robot Spot dan pan-tilt hello world Tinybot, lihat [contoh Robotics Live API](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## Langkah berikutnya

- [Pemahaman video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=id) — menemukan momen dan mengklasifikasikan progres.
- [Orkestrasi tugas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=id) — tugas dengan cakupan waktu panjang tanpa streaming.
- [Ringkasan Live API](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=id) — dokumentasi API Live lengkap.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-31 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-31 UTC."],[],[]]
