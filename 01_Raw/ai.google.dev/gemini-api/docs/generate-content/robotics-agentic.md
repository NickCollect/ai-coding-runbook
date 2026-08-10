---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=id
fetched_at: 2026-08-10T03:10:34.830322+00:00
title: "Kemampuan visi agentik \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Kemampuan visi agentik

Model Gemini Robotics ER dapat menulis dan menjalankan kode Python untuk memanipulasi gambar dan menerapkan logika sebelum menjawab. Halaman ini membahas contoh eksekusi kode: deteksi objek dengan zoom dan pangkas, pembacaan instrumen, pengukuran cairan, pembacaan papan sirkuit, dan anotasi gambar.

Untuk mengadaptasi contoh ini ke kasus penggunaan Anda sendiri, ganti teks perintah dan file gambar yang diupload dengan milik Anda sendiri. Anda juga dapat menyesuaikan skema JSON yang diminta dalam perintah agar sesuai dengan struktur output yang dibutuhkan aplikasi Anda, atau menambahkan `system_instruction` untuk menerapkan format dan presisi output.

Untuk kode yang dapat dijalankan sepenuhnya, lihat
[Cookbook Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Tingkat penalaran

Anda dapat mengontrol tingkat penalaran untuk menukar latensi dengan akurasi. Tugas spasial seperti deteksi objek berperforma baik dengan tingkat penalaran yang rendah. Tugas kompleks seperti penghitungan atau estimasi berat akan mendapatkan manfaat dari tingkat penalaran yang lebih tinggi.

Contoh berikut menetapkan tingkat penalaran ke `high` untuk tugas penghitungan yang kompleks:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('scene.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        "Identify and count all objects on the table."
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    )
)

print(response.text)
```

Lihat [Penalaran](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=id) untuk mengetahui detailnya.

## Deteksi objek (Zoom dan pangkas)

Contoh berikut menunjukkan cara menggunakan eksekusi kode untuk memperbesar dan memangkas gambar agar tampilan lebih jelas saat mendeteksi objek dan menampilkan kotak pembatas.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Return JSON in the format {label: val, y: val, x: val, y2: val, x2: val} for
the compostable objects in this scene. Please Zoom and crop the image for a
clearer view. Return an annotated image of the final result with the bounding
boxes drawn on it to the API caller as a part of your process.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Output model akan mirip dengan respons json berikut:

```
[
  {"label": "compostable", "y": 256, "x": 482, "y2": 295, "x2": 546},
  {"label": "compostable", "y": 317, "x": 478, "y2": 350, "x2": 542},
  {"label": "compostable", "y": 586, "x": 556, "y2": 668, "x2": 595},
  {"label": "compostable", "y": 463, "x": 669, "y2": 511, "x2": 718},
  {"label": "compostable", "y": 178, "x": 565, "y2": 250, "x2": 609}
]
```

Gambar berikut menampilkan kotak yang ditampilkan dari model.

![Contoh yang menampilkan kotak pembatas untuk objek yang ditemukan](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-bounding-boxes.png?hl=id)

## Membaca pengukur analog dan menerapkan logika

Contoh berikut menunjukkan cara menggunakan model untuk membaca pengukur analog dan melakukan penghitungan waktu. Contoh ini menggunakan instruksi sistem untuk menerapkan output JSON.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('gauge.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read the current value from this gauge. Then, calculate how long
        it will take at the current rate for the value to reach maximum.
        Reply in JSON: {"current_value": val, "max_value": val,
        "time_to_max_minutes": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Mengukur cairan dalam wadah

Contoh berikut menunjukkan cara menggunakan eksekusi kode untuk mengukur tingkat cairan dalam wadah.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('fluid.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Measure the amount of fluid in the container. Reply in JSON:
        {"fluid_level_ml": val, "container_capacity_ml": val,
        "percentage_full": val}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

## Membaca tanda pada papan sirkuit

Contoh berikut menunjukkan cara menggunakan eksekusi kode untuk membaca tanda pada papan sirkuit.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('circuit_board.jpeg', 'rb') as f:
    image_bytes = f.read()

system_instruction = "Be precise. When JSON is requested, reply with ONLY that JSON (no preface, no code block)."

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        """Read all visible component labels and markings on this circuit
        board. Reply in JSON: {"components": [{"label": val,
        "location": [y, x]}]}"""
    ],
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

![Contoh yang menampilkan tanda pada papan sirkuit](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-circuit-board.png?hl=id)

## Anotasi gambar

Contoh berikut menunjukkan cara menggunakan eksekusi kode untuk menganotasi gambar (misalnya, menggambar panah untuk petunjuk pembuangan) dan menampilkan gambar yang diubah.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Load your image
with open('sorting.jpeg', 'rb') as f:
    image_bytes = f.read()

prompt = """
Look at this image and return it as an annotated version using arrows of
different colors to represent which items should go in which bins for
disposal. You must return the final image to the API caller.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        prompt
    ],
    config = types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    )
)

print(response.text)
```

Berikut adalah contoh input gambar.

![Contoh yang menunjukkan jam untuk dibaca](https://ai.google.dev/static/gemini-api/docs/images/robotics/agentic-image-annotation.png?hl=id)

Output model akan mirip dengan berikut ini:

```
  The annotated image shows the suggested disposal locations for the items on the table:
  - **Green bin (Compost/Organic)**: Green chili, red chili, grapes, and cherries.
  - **Blue bin (Recycling)**: Yellow crushed can and plastic container.
  - **Black bin (Trash)**: Chocolate bar wrapper, Welch's packet, and white tissue.
```

## Langkah berikutnya

- [Orkestrasi tugas](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=id) — tugas jangka panjang dengan API robot kustom.
- [Robotika dengan streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=id) — streaming dua arah real-time (khusus Gemini Robotics ER 2).
- [Pemahaman video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=id) — menemukan momen dan klasifikasi progres (khusus Gemini Robotics ER 2).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
