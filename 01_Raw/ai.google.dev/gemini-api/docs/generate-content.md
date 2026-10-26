---
source_url: https://ai.google.dev/gemini-api/docs/generate-content?hl=id
fetched_at: 2026-10-26T05:43:18.961063+00:00
title: "Gemini API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon kini tersedia. [Coba praktikkan](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=id).

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs/generate-content?hl=id)

# Gemini API

Gemini API adalah jalur tercepat dari perintah ke tahap produksi dengan Gemini, Veo,
Nano Banana, dan lainnya. Dengan Vertex AI, Anda dapat mengintegrasikan model generatif ini ke dalam
aplikasi Anda untuk menghasilkan teks dan gambar, menganalisis input multimodal, dan membangun
agen percakapan.

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-4-argon",
    contents="Explain how AI works in a few words",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

await main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-4-argon",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-4-argon",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-4-argon", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

[Mulai membangun](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)

---

## Perkenalkan model kami

[Lihat semua](https://ai.google.dev/gemini-api/docs/models?hl=id)

[auto\_awesome
Gemini 4 Argon
Baru

Model penalaran unggulan kami dengan jendela konteks bersama 1 juta token dan dekode panjang hingga 1 juta token.](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=id)
[spark
Gemini 3.6 Flash
Baru

Model terbaru kami yang menyeimbangkan kecepatan dengan kecerdasan untuk memberikan performa yang kuat dalam tugas agentic dan multimodal.](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=id)
[graphic\_eq
Gemini 3.8 Flash TTS
Baru

Model text-to-speech berkualitas studio dengan akting ekspresif, desain Suara kustom, dan Replikasi suara.](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=id)
[spark
Gemini 3.5 Flash-Lite
Baru

Model bervolume tinggi dan sensitif biaya yang dioptimalkan untuk tugas sub-agen dengan throughput tinggi dan latensi rendah.](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=id)
[spark
Gemini 3.1 Flash-Lite

Model bervolume tinggi dan hemat biaya dengan performa dan kualitas seri Gemini 3.](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id)
[spark
Gemini 3 Flash

Performa kelas terdepan yang menyaingi model yang lebih besar dengan biaya yang jauh lebih rendah.](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id)
[🍌
Nano Banana

Model pembuatan dan pengeditan gambar yang canggih.](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)
[video\_library
Gemini Omni Flash

Model pembuatan dan pengeditan video tercanggih kami.](https://ai.google.dev/gemini-api/docs/omni?hl=id)
[spark
Gemini Robotics

Model bahasa-visi (VLM) yang menghadirkan kemampuan agentic Gemini ke robotika dan memungkinkan penalaran canggih di dunia fisik.](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=id)

## Ketahui Kemampuannya

[imagesmode

Pembuatan Gambar Native (Nano Banana)

Buat dan edit gambar yang sangat kontekstual secara native dengan Gemini 2.5 Flash Image.](https://ai.google.dev/gemini-api/docs/image-generation?hl=id)
[article

Konteks Panjang

Masukkan jutaan token ke model Gemini dan dapatkan pemahaman dari gambar, video, dan dokumen yang tidak terstruktur.](https://ai.google.dev/gemini-api/docs/long-context?hl=id)
[code

Output Terstruktur

Batasi Gemini untuk merespons dengan JSON, format data terstruktur yang cocok untuk pemrosesan otomatis.](https://ai.google.dev/gemini-api/docs/structured-output?hl=id)
[functions

Pemanggilan Fungsi

Membangun Agentic Workflows dengan menghubungkan Gemini ke API dan alat eksternal.](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
[videocam

Pembuatan Video dengan Gemini Omni Flash

Buat konten video berkualitas tinggi dari perintah teks atau gambar dengan model tercanggih kami.](https://ai.google.dev/gemini-api/docs/video?hl=id)
[android\_recorder

Agen Suara dengan Live API

Bangun aplikasi dan agen suara real-time dengan Live API.](https://ai.google.dev/gemini-api/docs/live-api?hl=id)
[build

Alat

Hubungkan Gemini ke dunia melalui alat bawaan seperti Google Penelusuran, Konteks URL, Google Maps, Eksekusi Kode, dan Penggunaan Komputer.](https://ai.google.dev/gemini-api/docs/tools?hl=id)
[stacks

Document Understanding

Proses hingga 1.000 halaman file PDF dengan pemahaman multimodal penuh atau jenis file berbasis teks lainnya.](https://ai.google.dev/gemini-api/docs/document-processing?hl=id)
[cognition\_2

Penalaran

Pelajari cara kemampuan berpikir meningkatkan penalaran untuk tugas dan agen yang kompleks.](https://ai.google.dev/gemini-api/docs/thinking?hl=id)

[Google AI Studio

Uji perintah, kelola kunci API Anda, pantau penggunaan, dan bangun prototipe.](https://aistudio.google.com?hl=id)
[group

Komunitas Developer

Ajukan pertanyaan dan temukan solusi dari developer lain dan engineer Google.](https://discuss.ai.google.dev/c/gemini-api/4?hl=id)
[menu\_book

Referensi API

Temukan informasi mendetail tentang Gemini API dalam dokumentasi referensi resmi.](https://ai.google.dev/api?hl=id)
[sensors

Status

Periksa status Gemini API, Google AI Studio, dan layanan model kami.](https://aistudio.google.com/status?hl=id)

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-22 UTC.

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-22 UTC."],[],[]]
