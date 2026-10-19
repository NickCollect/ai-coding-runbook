---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=id
fetched_at: 2026-10-19T05:56:14.414282+00:00
title: "Praktik terbaik Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Praktik terbaik Live API

Panduan ini membahas praktik terbaik yang dapat Anda ikuti untuk
mengoptimalkan penggunaan Live API.
Lihat halaman [Mulai menggunakan Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) untuk mengetahui ringkasan dan kode contoh untuk kasus penggunaan umum.

## Merancang petunjuk sistem yang jelas

Untuk mendapatkan performa terbaik dari Live API, sebaiknya miliki serangkaian petunjuk sistem (SI) yang ditentukan dengan jelas yang menentukan persona agen, aturan percakapan, dan pembatas, dalam urutan ini.

Untuk hasil terbaik, pisahkan setiap agen ke dalam SI yang berbeda.

1. **Tentukan persona agen:** Berikan detail tentang nama, peran, dan
   karakteristik pilihan agen. Jika Anda ingin menentukan aksen, pastikan untuk
   menentukan juga bahasa output yang diinginkan (seperti aksen Inggris Raya untuk
   penutur bahasa Inggris).
2. **Tentukan aturan percakapan:** Masukkan aturan ini dalam urutan yang Anda harapkan
   untuk diikuti model. Membatasi elemen percakapan satu kali dan loop percakapan. Contoh:

   - **Elemen sekali pakai:** Kumpulkan detail pelanggan satu kali (seperti nama, lokasi, nomor kartu loyalitas).
   - **Loop percakapan:** Pengguna dapat mendiskusikan rekomendasi, harga, pengembalian, dan pengiriman, serta dapat berpindah dari satu topik ke topik lainnya. Beri tahu model bahwa tidak masalah untuk terlibat dalam loop percakapan ini selama yang diinginkan pengguna.
3. **Tentukan panggilan alat dalam alur dengan kalimat yang berbeda:** Misalnya, jika
   langkah satu kali untuk mengumpulkan detail pelanggan memerlukan pemanggilan `get_user_info`
   fungsi, Anda dapat mengatakan: *Langkah pertama Anda adalah mengumpulkan informasi pengguna. Pertama,
   minta pengguna untuk memberikan nama, lokasi, dan nomor kartu loyalitasnya. Kemudian
   panggil `get_user_info` dengan detail ini.*
4. **Tambahkan pembatasan yang diperlukan:** Berikan pembatasan percakapan umum yang tidak boleh dilakukan model. Jangan ragu untuk memberikan contoh spesifik, misalnya, jika *x* terjadi, Anda ingin model melakukan *y*. Jika Anda masih belum mendapatkan tingkat presisi yang diinginkan, gunakan kata *tanpa salah* untuk memandu model agar presisi.

## Menentukan alat secara tepat

Saat menggunakan alat dengan Live API, berikan definisi alat yang spesifik.
Pastikan untuk memberi tahu Gemini dalam kondisi apa panggilan alat harus
dipanggil. Untuk mengetahui detail selengkapnya, lihat [Definisi alat](#tool-definitions-example) di bagian contoh.

## Menyusun perintah yang efektif

- **Gunakan perintah yang jelas:** Berikan contoh tentang apa yang boleh dan tidak boleh dilakukan model dalam perintah, dan coba batasi perintah menjadi satu perintah per persona atau peran dalam satu waktu. Daripada menggunakan perintah multi-halaman yang panjang, sebaiknya gunakan penggabungan perintah. Model ini menghasilkan performa terbaik pada tugas dengan panggilan fungsi tunggal.
- **Memberikan perintah dan informasi awal:** Live API mengharapkan
  input pengguna sebelum merespons. Agar Live API memulai percakapan, sertakan perintah yang memintanya untuk menyapa pengguna atau memulai percakapan. Sertakan informasi tentang pengguna agar Live API
  dapat mempersonalisasi ucapan tersebut.

## Menentukan bahasa

Model audio Live API otomatis mendeteksi dan beradaptasi dengan bahasa lisan pengguna tanpa memerlukan kode bahasa eksplisit.

Jika Anda ingin model merespons dalam bahasa tertentu, sertakan petunjuk
sebagai bagian dari petunjuk sistem Anda:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Streaming

Saat menerapkan audio real-time, ikuti praktik terbaik berikut:

- **Ukuran Chunk dan Latensi**: Kirim audio dalam chunk 20 md hingga 40 md.
- **Penanganan Interupsi**: Saat pengguna berbicara saat model sedang membalas, server akan mengirim pesan `server_content` dengan `"interrupted": true`. Anda
  harus segera membuang buffer audio sisi klien untuk mencegah agen
  terus berbicara dengan pengguna.

## Pengelolaan konteks

Gunakan `ContextWindowCompressionConfig` untuk sesi panjang, karena token audio native terakumulasi dengan cepat (sekitar 25 token per detik audio).

## Buffering klien

Jangan melakukan buffering audio input secara signifikan (seperti 1 detik) sebelum mengirim. Kirim
chunk kecil (20 md - 100 md) untuk meminimalkan latensi.

## Pengambilan ulang sampel

Pastikan aplikasi klien Anda melakukan pengambilan sampel ulang input mikrofon (sering kali 44,1 kHz atau 48 kHz) menjadi 16 kHz sebelum transmisi.

## Pengelolaan sesi

Ikuti panduan ini untuk menangani siklus proses sesi dan memastikan pengalaman pengguna yang andal:

- **Aktifkan kompresi jendela konteks:** Token audio terakumulasi sekitar 25 token per detik. Tanpa kompresi, sesi khusus audio
  dibatasi hingga 15 menit dan sesi audio-video hingga 2 menit. Aktifkan
  [kompresi jendela konteks](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id#context-window-compression)
  untuk memperpanjang sesi dengan durasi tidak terbatas.
- **Menerapkan kelanjutan sesi:** Server dapat mereset koneksi WebSocket secara berkala. Gunakan
  [pelanjutan sesi](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id#session-resumption)
  untuk terhubung kembali dengan lancar tanpa kehilangan konteks. Pertahankan token kelanjutan terbaru dari `SessionResumptionUpdate` pesan dan teruskan sebagai handle saat terhubung kembali. Token pelanjutan berlaku selama 2 jam setelah sesi terakhir berakhir.
- **Menangani pesan GoAway:** Server mengirim pesan
  [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id#goaway-message)
  sebelum menghentikan koneksi. Dengarkan pesan ini dan gunakan kolom
  `timeLeft` untuk mengakhiri atau menghubungkan kembali dengan baik sebelum koneksi
  ditutup.
- **Tangani sinyal generationComplete:** Gunakan pesan
  [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id#generation-complete-message)
  untuk mengetahui kapan model telah selesai membuat respons, sehingga aplikasi
  Anda dapat memperbarui UI-nya atau melanjutkan ke tindakan berikutnya.

Untuk mengetahui detail penerapan, lihat artikel
[Pengelolaan sesi](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=id).

## Contoh

Contoh ini menggabungkan praktik terbaik dan [pedoman untuk desain petunjuk sistem](#system-instruction-guidelines) guna memandu performa model sebagai pelatih karier.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Definisi alat

JSON ini menentukan fungsi relevan yang dipanggil dalam contoh pelatih karier.
Untuk hasil terbaik saat menentukan fungsi, sertakan nama, deskripsi,
parameter, dan kondisi pemanggilan.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Penetapan harga dan penagihan

Gemini Live API ditagih berdasarkan penggunaan token. Karena Live API mempertahankan sesi WebSocket persisten, penagihan mengikuti model gabungan berdasarkan jendela konteks aktif.

### Jendela konteks sesi (biaya gabungan)

API mengenakan biaya per giliran untuk semua token yang ada di jendela konteks sesi. "Giliran" ditentukan sebagai satu input pengguna dan respons model yang sesuai.

- **Akumulasi:** Jendela konteks mencakup token baru dari giliran saat ini ditambah semua token yang terakumulasi dari giliran sebelumnya.
- **Penagihan ulang:** Token sebelumnya diproses ulang dan diperhitungkan di setiap giliran baru, hingga ukuran jendela konteks yang Anda konfigurasi. Seiring durasi sesi yang bertambah, biaya per giliran akan meningkat karena histori percakapan diproses ulang.

### Token dan transkripsi audio

Live API secara native bersifat multimodal. Fitur ini mempertahankan histori percakapan sebagai token audio mentah untuk mempertahankan nuansa dan nada akustik.

- **Penagihan audio:** API menagih Anda untuk token audio native yang terakumulasi dengan tarif input audio standar pada setiap giliran.
- **Biaya tambahan transkripsi:** Jika transkripsi audio ke teks diaktifkan (`inputAudioTranscription` atau `outputAudioTranscription`), API akan mengenakan biaya untuk semua token teks yang dihasilkan untuk transkripsi dengan tarif output token teks selain biaya token audio standar.

### Mengelola biaya dengan batas konteks

Untuk mencegah pertumbuhan biaya yang tidak terbatas dalam sesi panjang, konfigurasikan ukuran
jendela konteks menggunakan `contextWindowCompression`.

Dengan menetapkan pemicu kompresi (misalnya, 25.000 token) dan jendela geser (misalnya, 8.000 token), API akan otomatis mengeluarkan token yang lebih lama setelah batas tercapai. Kemudian, API akan menagih giliran berikutnya hanya untuk histori yang dipertahankan ditambah token baru.

### Audio proaktif

Jika audio proaktif diaktifkan, API akan mengenakan biaya untuk token input selama
API Live mendengarkan, dan mengenakan biaya untuk token output hanya saat API
merespons.

- **Catatan untuk Gemini 3.8:** Audio proaktif diaktifkan secara permanen di
  `gemini-3.8-live` dan `gemini-3.8-live-extended-thinking`.
- **Catatan untuk Gemini 3.1:** Audio proaktif tidak didukung di
  `gemini-3.1-flash-live-preview`. Untuk model ini, API hanya menagih
  audio saat Anda secara aktif melakukan streaming input.

Untuk mengetahui informasi harga mendetail, lihat
[halaman harga Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-09-17 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-09-17 UTC."],[],[]]
