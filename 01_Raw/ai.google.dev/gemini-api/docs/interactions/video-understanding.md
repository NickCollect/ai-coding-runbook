---
source_url: https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=id
fetched_at: 2026-06-08T05:30:01.827524+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemahaman video

> Untuk mempelajari pembuatan video, lihat panduan [Veo](https://ai.google.dev/gemini-api/docs/video?hl=id).

Model Gemini dapat memproses video, sehingga memungkinkan banyak kasus penggunaan developer yang belum pernah ada sebelumnya yang secara historis memerlukan model khusus domain.
Beberapa kemampuan penglihatan Gemini mencakup kemampuan untuk: mendeskripsikan, menyegmentasikan, dan mengekstrak informasi dari video, menjawab pertanyaan tentang konten video, dan merujuk ke stempel waktu tertentu dalam video.

Anda dapat memberikan video sebagai input ke Gemini dengan cara berikut:

| Metode masukan | Ukuran maks | Kasus penggunaan yang direkomendasikan |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (berbayar) / 2 GB (gratis) | File besar (100 MB+), video panjang (10 menit+), file yang dapat digunakan kembali. |
| [Pendaftaran Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=id#registration) | 2 GB (per file, tanpa batas penyimpanan) | File besar (100 MB+), video panjang (10 menit+), file persisten yang dapat digunakan kembali. |
| [Data Sebaris](#inline-video) | < 100MB | File kecil (<100 MB), durasi singkat (<1 menit), input satu kali. |
| [URL YouTube](#youtube) | T/A | Video YouTube publik. |

> **Catatan:** [File API](#upload-video) direkomendasikan untuk sebagian besar kasus penggunaan, terutama untuk file yang berukuran lebih dari 100 MB atau saat Anda ingin menggunakan kembali file di beberapa permintaan.

Untuk mempelajari metode input file lainnya, seperti menggunakan URL eksternal atau file yang disimpan di Google Cloud, lihat panduan [Metode input file](https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=id).

### Mengupload file video

Kode berikut mendownload video contoh, menguploadnya menggunakan [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=id),
menunggu pemrosesannya selesai, lalu menggunakan referensi file yang diupload untuk
meringkas video.

### Python

```
from google import genai
import base64
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  // Wait for the file to be processed.
  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Selalu gunakan Files API jika total ukuran permintaan (termasuk file, perintah teks, petunjuk sistem, dll.) lebih besar dari 20 MB, durasi video signifikan, atau jika Anda ingin menggunakan video yang sama dalam beberapa perintah.
File API menerima format file video secara langsung.

Untuk mempelajari lebih lanjut cara menggunakan file media, lihat
[Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=id).

### Meneruskan data video secara inline

Daripada mengupload file video menggunakan File API, Anda dapat meneruskan video yang lebih kecil langsung dalam permintaan. Opsi ini cocok untuk
video yang lebih pendek dengan total ukuran permintaan di bawah 20 MB.

Berikut contoh cara memberikan data video inline:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### URL YouTube yang memenuhi syarat

Anda dapat meneruskan URL YouTube langsung ke Gemini API sebagai bagian dari permintaan Anda sebagai berikut:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3-flash-preview',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3-flash-preview",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.steps.at(-1).content[0].text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Batasan:**

- Untuk paket gratis, Anda tidak dapat mengupload lebih dari 8 jam video YouTube per hari.
- Untuk paket berbayar, tidak ada batasan berdasarkan durasi video.
- Untuk model sebelum Gemini 2.5, Anda hanya dapat mengupload 1 video per permintaan. Untuk model Gemini 2.5 dan yang lebih baru, Anda dapat mengupload maksimal 10 video per permintaan.
- Anda hanya dapat mengupload video publik (bukan video pribadi atau tidak publik).

## Lihat stempel waktu dalam konten

Anda dapat mengajukan pertanyaan tentang titik waktu tertentu dalam video menggunakan stempel waktu dalam bentuk `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Mengekstrak insight mendetail dari video

Model Gemini menawarkan kemampuan canggih untuk memahami konten video dengan memproses informasi dari aliran **audio dan visual**. Dengan demikian, Anda dapat mengekstrak serangkaian detail yang kaya, termasuk membuat deskripsi tentang apa yang terjadi dalam video dan menjawab pertanyaan tentang kontennya.

Untuk deskripsi visual, model mengambil sampel video dengan kecepatan **1 frame per detik** (FPS). Frekuensi sampling default ini berfungsi dengan baik untuk sebagian besar konten, tetapi perhatikan bahwa frekuensi ini mungkin tidak menangkap detail dalam video dengan gerakan cepat atau perubahan adegan yang cepat.
Untuk konten dengan gerakan tinggi seperti itu, pertimbangkan untuk [menetapkan kecepatan frame kustom](#custom-frame-rate).

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Format video yang didukung

Gemini mendukung jenis MIME format video berikut:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Detail teknis tentang video

- **Model & konteks yang didukung**: Semua Gemini dapat memproses data video.
  - Model dengan jendela konteks 1 juta token dapat memproses video berdurasi hingga 1 jam pada resolusi media default atau berdurasi 3 jam pada resolusi media rendah.
- **Pemrosesan File API**: Saat menggunakan File API, video disimpan pada 1 frame per detik (FPS) dan audio diproses pada 1 Kbps (satu saluran).
  Stempel waktu ditambahkan setiap detik.
  - Kecepatan ini dapat berubah di masa mendatang untuk meningkatkan kualitas inferensi.
- **Penghitungan token**: Setiap detik video di-tokenisasi sebagai berikut:
  - Frame individual (diambil sampel pada 1 FPS):
    - Jika `media_resolution` disetel ke rendah, frame akan di-tokenisasi pada 66 token per frame.
    - Jika tidak, frame akan di-tokenisasi pada 258 token per frame.
  - Audio: 32 token per detik.
  - Metadata juga disertakan.
  - Total: Sekitar 300 token per detik video pada resolusi media default, atau 100 token per detik video pada resolusi media rendah.
- **Resolusi sedang**: Gemini 3 memperkenalkan kontrol terperinci atas pemrosesan visi multimodal dengan parameter `media_resolution`. Parameter
  `media_resolution` menentukan
  **jumlah maksimum token yang dialokasikan per gambar input atau frame video.**
  Resolusi yang lebih tinggi meningkatkan kemampuan model untuk membaca teks kecil atau mengidentifikasi detail kecil, tetapi meningkatkan penggunaan token dan latensi.

  perhitungan, lihat panduan [token](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=id).
- **Format stempel waktu**: Saat merujuk ke momen tertentu dalam video di perintah Anda, gunakan format `MM:SS` (misalnya, `01:15` untuk 1 menit 15 detik).
- **Praktik terbaik**:

  - Gunakan hanya satu video per permintaan perintah untuk mendapatkan hasil yang optimal.
  - Jika menggabungkan teks dan satu video, tempatkan perintah teks *setelah* bagian video dalam array `input`.
  - Perhatikan bahwa urutan tindakan cepat mungkin kehilangan detail karena kecepatan pengambilan sampel 1 FPS. Pertimbangkan untuk memperlambat klip tersebut jika perlu.

## Langkah berikutnya

Panduan ini menunjukkan cara mengupload file video dan membuat output teks dari input video. Untuk mempelajari lebih lanjut, lihat referensi berikut:

- [Petunjuk sistem](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=id#system-instructions):
  Petunjuk sistem memungkinkan Anda mengarahkan perilaku model berdasarkan kebutuhan dan kasus penggunaan spesifik Anda.
- [Files API](https://ai.google.dev/gemini-api/docs/interactions/files?hl=id): Pelajari lebih lanjut cara mengupload dan mengelola file untuk digunakan dengan Gemini.
- [Strategi perintah file](https://ai.google.dev/gemini-api/docs/interactions/files?hl=id#prompt-guide): Gemini API mendukung perintah dengan data teks, gambar, audio, dan video, yang juga dikenal sebagai perintah multimodal.
- [Panduan keamanan](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=id): Terkadang model AI generatif menghasilkan output yang tidak terduga, seperti output yang tidak akurat, bias, atau menyinggung. Pemrosesan pasca dan evaluasi manusia sangat penting untuk membatasi risiko bahaya dari output tersebut.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-09 UTC."],[],[]]
