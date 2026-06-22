---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id
fetched_at: 2026-06-22T06:28:25.523647+00:00
title: "Strategi desain prompt \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Strategi desain prompt

*Desain prompt* adalah proses pembuatan perintah, atau permintaan dalam bahasa alami,
yang mendapatkan respons yang akurat dan berkualitas tinggi dari model bahasa.

Halaman ini memperkenalkan konsep dasar, strategi, dan praktik terbaik untuk membantu Anda mulai mendesain perintah agar dapat memanfaatkan model AI Gemini secara maksimal.

## Panduan perintah khusus topik

Mencari strategi perintah yang lebih spesifik? Lihat panduan perintah lainnya di:

- [Memberikan perintah dengan file media](https://ai.google.dev/gemini-api/docs/files?hl=id#prompt-guide)
- Perintah untuk pembuatan gambar dengan [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=id#imagen-prompt-guide) dan [Pembuatan Gambar Native Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=id#prompt-guide)
- [Memberikan perintah untuk pembuatan video](https://ai.google.dev/gemini-api/docs/video?hl=id#prompt-guide)

Anda dapat menemukan contoh perintah lainnya di [galeri perintah](https://ai.google.dev/gemini-api/prompts?hl=id) yang dimaksudkan untuk menampilkan banyak konsep yang dibagikan dalam panduan ini secara interaktif.

## Petunjuk yang jelas dan spesifik

Cara yang efektif dan efisien untuk menyesuaikan perilaku model adalah dengan memberikan instruksi yang jelas dan spesifik. Petunjuk dapat berupa pertanyaan,
tugas langkah demi langkah, atau serumit memetakan pengalaman dan pola pikir pengguna.

### Input

Input adalah teks yang diperlukan dalam perintah yang harus diberikan respons oleh model. Input dapat berupa pertanyaan yang menjadi model jawaban (masukan pertanyaan), tugas yang dilakukan model (masukan tugas), suatu entitas model beroperasi (input entitas), atau sebagian input yang diselesaikan model atau berlanjut (input penyelesaian).

| **Jenis input** | **Perintah** | **Output yang dihasilkan** |
| --- | --- | --- |
| Pertanyaan | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Tugas | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entitas | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Penyelesaian input sebagian

Model bahasa generatif berfungsi seperti alat pelengkapan otomatis canggih. Jika Anda menyediakan konten sebagian, model dapat memberikan konten lainnya atau yang dianggapnya sebagai kelanjutan dari konten tersebut sebagai respons. Saat melakukannya, jika Anda menyertakan contoh atau konteks, model dapat mempertimbangkan contoh atau konteks tersebut.

Contoh berikut memberikan perintah dengan petunjuk dan input entity:

|  |
| --- |
| **Perintah:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Respons:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Meskipun model melakukan seperti yang diminta, menuliskan petunjuk dalam bahasa alami terkadang dapat menjadi tantangan dan menyisakan banyak hal untuk interpretasi model. Misalnya, menu restoran mungkin berisi banyak item. Untuk mengurangi ukuran respons JSON, Anda mungkin ingin menghilangkan item yang tidak dipesan. Dalam hal ini, Anda dapat memberikan contoh dan awalan respons, lalu membiarkan model melengkapinya:

|  |
| --- |
| **Perintah:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Respons:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Perhatikan bagaimana "cheeseburger" dikecualikan dari output karena bukan bagian
dari pesanan.

Meskipun Anda dapat menentukan format objek respons JSON sederhana menggunakan perintah, sebaiknya gunakan fitur [output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id) Gemini API saat menentukan Skema JSON yang lebih kompleks untuk respons.

### Batasan

Tentukan batasan apa pun dalam membaca perintah atau membuat respons. Anda dapat
memberi tahu model apa yang boleh dan tidak boleh dilakukan. Misalnya, Anda dapat menentukan batasan
dalam perintah tentang panjang ringkasan yang Anda inginkan:

|  |
| --- |
| **Perintah:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Respons:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Format respons

Anda dapat memberikan petunjuk yang menentukan format respons. Misalnya, Anda dapat meminta agar respons diformat sebagai tabel, daftar berbutir, presentasi singkat, kata kunci, kalimat, atau paragraf. Petunjuk sistem berikut memberi tahu model untuk memberikan respons yang lebih komunikatif:

|  |
| --- |
| **Petunjuk sistem**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Perintah**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Respons:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Memformat respons dengan strategi penyelesaian

[Strategi penyelesaian](#completion) juga dapat membantu memformat respons.
Contoh berikut meminta model untuk membuat garis besar esai:

|  |
| --- |
| **Perintah:**    ``` Create an outline for an essay about hummingbirds. ```  **Respons:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

Perintah tidak menentukan format untuk garis besar dan model telah memilih format untuk Anda. Agar model mengembalikan garis besar dalam format tertentu, Anda dapat menambahkan teks yang mewakili awal garis besar dan membiarkan model menyelesaikannya berdasarkan pola yang Anda mulai.

|  |
| --- |
| **Perintah:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Respons:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Prompt zero-shot vs few-shot

Anda dapat menyertakan contoh dalam prompt yang menunjukkan tampilan penerapannya dengan benar pada model. Model mencoba mengidentifikasi pola dan hubungan dari contoh-contoh tersebut dan menerapkannya saat membuat respons. Perintah yang berisi beberapa contoh disebut perintah *few-shot*, sedangkan perintah yang tidak memberikan contoh disebut perintah *zero-shot*. Prompt few-shot sering digunakan
untuk mengatur pemformatan, frasa, cakupan, atau pola umum respons model. Gunakan contoh yang spesifik dan bervariasi untuk membantu model mempersempit fokusnya dan menghasilkan hasil yang lebih akurat.

Sebaiknya selalu sertakan contoh sedikit tembakan dalam perintah Anda. Perintah tanpa
contoh sedikit tembakan cenderung kurang efektif. Bahkan, Anda dapat menghapus
petunjuk dari perintah jika contoh Anda cukup jelas dalam menunjukkan
tugas yang sedang dilakukan.

Petunjuk zero-shot berikut meminta model untuk memilih penjelasan terbaik.

|  |
| --- |
| **Perintah:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Respons:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Jika kasus penggunaan Anda memerlukan model untuk menghasilkan respons yang ringkas, Anda dapat menyertakan
contoh dalam perintah yang memberikan preferensi pada respons yang ringkas.

Perintah berikut memberikan dua contoh yang menunjukkan preferensi terhadap penjelasan yang lebih singkat. Dalam respons, Anda dapat melihat bahwa contoh memandu model untuk memilih penjelasan yang lebih pendek (`Explanation2`) dibandingkan dengan penjelasan yang lebih panjang (`Explanation1`) seperti sebelumnya.

|  |
| --- |
| **Perintah:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Respons:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Jumlah contoh yang optimal

Model seperti Gemini sering kali dapat memahami pola menggunakan beberapa contoh, meskipun Anda mungkin perlu bereksperimen dengan jumlah contoh yang akan diberikan dalam perintah untuk mendapatkan hasil terbaik. Pada saat yang sama, jika Anda menyertakan terlalu banyak contoh, model mungkin akan mulai [melebihi](https://developers.google.com/machine-learning/glossary?hl=id#overfitting) respons terhadap contoh.

### Format yang konsisten

Pastikan struktur dan pemformatan contoh few-shot sama untuk menghindari respons dengan format yang tidak diinginkan. Salah satu tujuan utama menambahkan contoh few-shot dalam perintah adalah untuk menunjukkan format respons kepada model. Oleh karena itu, penting untuk memastikan format yang konsisten di semua contoh, terutama dengan memperhatikan tag XML, spasi kosong, baris baru, dan pemisah contoh.

## Tambahkan konteks

Anda dapat menyertakan petunjuk dan informasi dalam perintah yang diperlukan model
untuk memecahkan masalah, bukan mengasumsikan bahwa model memiliki semua informasi
yang diperlukan. Informasi kontekstual ini membantu model memahami batasan dan detail tugas yang Anda minta.

Contoh berikut meminta model untuk memberikan panduan pemecahan masalah untuk router:

|  |
| --- |
| **Perintah:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Respons:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

Responsnya terlihat seperti informasi pemecahan masalah umum yang tidak spesifik
untuk router atau status lampu indikator LED.

Guna menyesuaikan respons untuk router tertentu, Anda dapat menambahkan prompt dalam panduan pemecahan masalah router sebagai konteks yang dirujuk saat memberikan respons.

|  |
| --- |
| **Perintah:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Respons:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Menguraikan perintah menjadi komponen

Untuk kasus penggunaan yang memerlukan perintah kompleks, Anda dapat membantu model mengelola kompleksitas ini dengan memecah perintah menjadi komponen yang lebih sederhana.

1. **Memecah petunjuk:** Daripada memiliki banyak petunjuk dalam satu perintah, buat satu perintah per petunjuk. Anda dapat memilih perintah mana yang akan diproses berdasarkan input pengguna.
2. **Rangkai perintah:** Untuk tugas kompleks yang melibatkan beberapa langkah berurutan,
   jadikan setiap langkah sebagai perintah dan rangkai perintah tersebut secara berurutan. Dalam rangkaian perintah berurutan ini, output satu perintah dalam urutan menjadi input perintah berikutnya. Output perintah terakhir dalam urutan
   adalah output akhir.
3. **Respons gabungan:** Penggabungan adalah saat Anda ingin melakukan berbagai tugas paralel pada berbagai bagian data dan menggabungkan hasilnya untuk menghasilkan output akhir. Misalnya, Anda dapat memberi tahu model untuk melakukan satu
   operasi pada bagian pertama data, melakukan operasi lain pada bagian data
   lainnya, dan menggabungkan hasilnya.

## Bereksperimen dengan parameter model

Setiap panggilan yang Anda kirim ke model menyertakan parameter value yang mengontrol cara model menghasilkan respons. Model ini dapat memberikan hasil yang berbeda untuk parameter value yang berbeda. Bereksperimenlah dengan parameter value yang berbeda untuk mendapatkan nilai terbaik untuk tugas. Parameter yang tersedia untuk model yang berbeda mungkin berbeda. Parameter yang paling umum adalah sebagai berikut:

1. **Token output maks:** Menentukan jumlah maksimum token yang dapat
   dibuat dalam respons. Token terdiri atas sekitar empat karakter. 100
   token setara dengan sekitar 60-80 kata.
2. **Temperatur:** Temperatur mengontrol tingkat keacakan dalam pemilihan token. Temperatur digunakan untuk pengambilan sampel selama pembuatan respons, yang terjadi saat `topP` dan `topK` diterapkan. Temperatur yang lebih rendah cocok untuk perintah yang memerlukan respons yang lebih deterministik atau kurang terbuka, sedangkan temperatur yang lebih tinggi dapat memberikan hasil yang lebih beragam atau kreatif. Temperatur 0 bersifat deterministik, yang berarti bahwa respons probabilitas tertinggi akan selalu dipilih.
3. **`topK`:** Parameter `topK` mengubah cara model memilih token untuk output. Nilai `topK` 1 berarti token yang dipilih adalah yang paling mungkin di antara semua token dalam kosakata model (disebut juga greedy decoding), sedangkan nilai `topK` 3 berarti token berikutnya dipilih dari antara 3 token yang paling mungkin menggunakan temperatur. Untuk setiap langkah pemilihan token, token `topK` dengan probabilitas tertinggi akan diambil sampelnya. Token kemudian difilter lebih lanjut berdasarkan `topP` dengan token akhir yang dipilih menggunakan pengambilan sampel temperatur.
4. **`topP`:** Parameter `topP` mengubah cara model memilih token untuk output. Token dipilih dari yang paling mungkin hingga yang paling tidak mungkin hingga jumlah probabilitasnya sama dengan nilai `topP`. Misalnya, jika token A, B, dan C memiliki probabilitas 0,3, 0,2, dan 0,1 serta nilai `topP` adalah 0,5, maka model akan memilih A atau B sebagai token berikutnya dengan menggunakan temperatur dan mengecualikan C sebagai kandidat. Nilai `topP` default adalah 0,95.
5. **`stop_sequences`:** Tetapkan urutan penghentian untuk
   memberi tahu model agar berhenti membuat konten. Urutan penghentian dapat berupa
   urutan karakter apa pun. Coba hindari penggunaan urutan karakter yang
   mungkin muncul dalam konten yang dihasilkan.

## Strategi iterasi prompt

Desain prompt terkadang memerlukan beberapa iterasi sebelum
Anda mendapatkan respons yang diinginkan secara konsisten. Bagian ini memberikan
panduan tentang beberapa hal yang dapat Anda coba saat melakukan iterasi pada perintah Anda:

1. **Gunakan frasa yang berbeda:** Penggunaan kata atau frasa yang berbeda dalam perintah Anda sering kali menghasilkan respons yang berbeda dari model meskipun semuanya memiliki arti yang sama. Jika Anda tidak mendapatkan hasil yang diharapkan dari perintah Anda, coba
   susun ulang perintah tersebut.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Beralih ke tugas analog:** Jika Anda tidak dapat membuat model agar mengikuti petunjuk untuk suatu tugas, coba berikan petunjuk untuk tugas analog yang mencapai hasil yang sama.

   Perintah ini memberi tahu model untuk mengategorikan buku dengan menggunakan kategori yang telah ditentukan:

   |  |
   | --- |
   | **Perintah:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Respons:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   Responsnya benar, tetapi modelnya tidak tetap dalam batas opsi. Anda juga ingin membuat model untuk merespons hanya dengan salah satu opsi, bukan
   menggunakan kalimat lengkap. Dalam hal ini, Anda dapat menulis ulang petunjuk sebagai
   pertanyaan pilihan ganda dan meminta model untuk memilih opsi.

   |  |
   | --- |
   | **Perintah:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Respons:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Mengubah urutan konten perintah:** Urutan konten dalam perintah terkadang dapat memengaruhi respons. Coba ubah urutan konten dan lihat pengaruhnya terhadap respons.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Respons penggantian

Respons penggantian adalah respons yang ditampilkan oleh model saat prompt
atau respons memicu filter keamanan. Contoh respons penggantian adalah
"Saya tidak dapat membantu, karena saya hanya model bahasa".

Jika model merespons dengan respons penggantian, coba tingkatkan suhu.

## Perujukan dan eksekusi kode

Gemini dapat menggunakan alat untuk menghindari halusinasi dalam skenario yang berpotensi menghasilkan respons yang salah.

[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) menghubungkan model Gemini ke konten web real-time, dan harus diaktifkan setiap kali model mungkin perlu mengetahui fakta-fakta yang tidak jelas atau terbaru.

[Alat eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id) Gemini memungkinkan model membuat dan menjalankan kode Python, dan harus diaktifkan setiap kali model perlu melakukan perhitungan, penghitungan, atau kalkulasi apa pun.

## Gemini 3

[Model Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-3) dirancang untuk penalaran dan pemahaman petunjuk yang canggih.
Model ini merespons perintah yang langsung, terstruktur dengan baik, dan mendefinisikan tugas serta batasan dengan jelas. Praktik berikut direkomendasikan untuk
hasil optimal dengan Gemini 3:

### Prinsip inti perintah

- **Tulis dengan tepat dan langsung:** Nyatakan tujuan Anda dengan jelas dan ringkas. Hindari
  bahasa yang tidak perlu atau terlalu persuasif.
- **Gunakan struktur yang konsisten:** Gunakan pembatas yang jelas untuk memisahkan berbagai bagian perintah Anda. Tag gaya XML (misalnya, `<context>`, `<task>`) atau heading Markdown efektif. Pilih satu format dan gunakan secara konsisten dalam satu perintah.
- **Tentukan parameter:** Jelaskan secara eksplisit setiap istilah atau parameter yang ambigu.
- **Mengontrol kejelasan output:** Secara default, model Gemini 3 memberikan jawaban yang langsung dan efisien. Jika Anda memerlukan respons yang lebih bersifat percakapan atau lebih mendetail,
  Anda harus secara eksplisit memintanya dalam petunjuk Anda.
- **Tangani input multimodal secara koheren:** Saat menggunakan teks, gambar, audio, atau
  video, perlakukan input tersebut sebagai input kelas yang sama. Pastikan petunjuk Anda dengan jelas
  mereferensikan setiap modalitas sesuai kebutuhan.
- **Prioritaskan petunjuk penting:** Tempatkan batasan perilaku penting, definisi peran (persona), dan persyaratan format output dalam Petunjuk Sistem atau di awal perintah pengguna.
- **Struktur untuk konteks panjang:** Saat memberikan konteks dalam jumlah besar (misalnya, dokumen, kode), berikan semua konteks terlebih dahulu. Tempatkan petunjuk atau pertanyaan spesifik Anda di *akhir* perintah.
- **Konteks penanda:** Setelah blok data yang besar, gunakan frasa transisi
  yang jelas untuk menghubungkan konteks dan kueri Anda, seperti "Berdasarkan
  informasi di atas..."

### Strategi Gemini 3 Flash

- **Akurasi hari ini:** Tambahkan klausa berikut ke petunjuk sistem untuk membantu model memperhatikan bahwa hari ini berada pada tahun 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Akurasi batas informasi:** Tambahkan klausa berikut ke petunjuk sistem agar model mengetahui batas informasinya:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Performa perujukan:** Tambahkan klausa berikut ke petunjuk sistem (dengan pengeditan jika sesuai) untuk meningkatkan kemampuan model dalam merujuk respons pada konteks yang diberikan:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Meningkatkan penalaran dan perencanaan

Model seri Gemini 2.5 dan 3 secara otomatis membuat teks "pemikiran" internal untuk meningkatkan performa penalaran. Oleh karena itu, umumnya tidak perlu membuat model menguraikan, merencanakan, atau menjelaskan langkah-langkah penalaran dalam respons yang ditampilkan. Untuk masalah yang memerlukan penalaran berat, permintaan sederhana seperti "Berpikir keras sebelum menjawab" dapat meningkatkan performa, meskipun dengan biaya token pemikiran tambahan.

Lihat dokumentasi [Proses berpikir Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=id) untuk mengetahui detail selengkapnya.

### Contoh perintah terstruktur

Penggunaan tag atau Markdown membantu model membedakan antara petunjuk, konteks, dan tugas.

**Contoh XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Contoh Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Contoh template yang menggabungkan praktik terbaik

Template ini mencakup prinsip inti untuk memberikan perintah dengan Gemini 3. Selalu
pastikan untuk melakukan iterasi dan modifikasi untuk kasus penggunaan spesifik Anda.

**Petunjuk Sistem:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Perintah Pengguna:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Alur kerja agentic

Untuk alur kerja agentik yang mendalam, sering kali diperlukan petunjuk khusus untuk mengontrol cara model bernalar, merencanakan, dan menjalankan tugas. Meskipun Gemini memberikan performa umum yang kuat, agen yang kompleks sering kali mengharuskan Anda mengonfigurasi pertimbangan antara biaya komputasi (latensi dan token) dan akurasi tugas.

Saat mendesain perintah untuk agen, pertimbangkan dimensi perilaku berikut yang dapat Anda arahkan di agen:

### Penalaran dan strategi

Konfigurasi cara model berpikir dan merencanakan sebelum mengambil tindakan.

- **Dekomposisi logis:** Menentukan seberapa menyeluruh model harus menganalisis batasan, prasyarat, dan urutan operasi.
- **Diagnosis masalah**: Mengontrol kedalaman analisis saat mengidentifikasi penyebab dan penggunaan penalaran abduktif model. Menentukan apakah model harus menerima jawaban yang paling jelas atau menjelajahi penjelasan yang kompleks dan kurang mungkin.
- **Kelengkapan informasi:** Kompromi antara menganalisis setiap kebijakan dan dokumen yang tersedia versus memprioritaskan efisiensi dan kecepatan.

### Eksekusi dan keandalan

Konfigurasi cara agen beroperasi secara mandiri dan menangani hambatan.

- **Kemampuan beradaptasi:** Cara model bereaksi terhadap data baru. Menentukan apakah harus mematuhi rencana awalnya secara ketat atau langsung mengubah rencana saat pengamatan bertentangan dengan asumsi.
- **Persistensi dan Pemulihan:** Tingkat upaya model untuk mengoreksi sendiri kesalahan. Persistensi tinggi meningkatkan tingkat keberhasilan, tetapi berisiko menimbulkan biaya token atau loop yang lebih tinggi.
- **Penilaian Risiko:** Logika untuk mengevaluasi konsekuensi. Secara eksplisit membedakan antara tindakan eksplorasi berisiko rendah (baca) dan perubahan status berisiko tinggi (tulis).

### Interaksi dan output

Konfigurasi cara agen berkomunikasi dengan pengguna dan memformat hasil.

- **Ambiguitas dan penanganan izin:** Menentukan kapan model diizinkan untuk membuat asumsi dan kapan model harus menjeda eksekusi untuk meminta klarifikasi atau izin kepada pengguna.
- **Panjang Teks:** Mengontrol volume teks yang dihasilkan bersamaan dengan panggilan alat. Hal ini menentukan apakah model menjelaskan tindakannya kepada pengguna atau tetap diam selama eksekusi.
- **Presisi dan kelengkapan:** Tingkat kecermatan output yang diperlukan. Menentukan apakah model harus menyelesaikan setiap kasus ekstrem dan memberikan angka yang tepat atau apakah perkiraan kasar dapat diterima.

### Template petunjuk sistem

Petunjuk sistem berikut adalah contoh yang telah dievaluasi oleh peneliti untuk meningkatkan performa pada tolok ukur agentik di mana model harus mematuhi buku peraturan yang kompleks dan berinteraksi dengan pengguna. Hal ini mendorong agen untuk bertindak sebagai pemberi alasan dan perencana yang kuat, menerapkan perilaku tertentu di seluruh dimensi yang tercantum di atas, dan mewajibkan model untuk merencanakan secara proaktif sebelum mengambil tindakan apa pun.

Anda dapat menyesuaikan template ini agar sesuai dengan batasan kasus penggunaan spesifik Anda.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Langkah berikutnya

- Setelah Anda memahami desain perintah dengan lebih baik, coba tulis perintah Anda sendiri menggunakan [Google AI Studio](http://aistudio.google.com?hl=id).
- Untuk mempelajari multimodal prompting, lihat
  [Membuat perintah dengan file media](https://ai.google.dev/gemini-api/docs/files?hl=id#prompt-guide).
- Untuk mempelajari perintah gambar, lihat panduan perintah [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=id#prompt-guide) dan [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=id#imagen-prompt-guide).
- Untuk mempelajari perintah video, lihat [panduan perintah Veo](https://ai.google.dev/gemini-api/docs/video?hl=id#prompt-guide).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-10 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-10 UTC."],[],[]]
