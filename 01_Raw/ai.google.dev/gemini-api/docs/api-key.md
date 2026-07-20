---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=id
fetched_at: 2026-07-20T04:43:29.892358+00:00
title: "Menggunakan kunci Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Menggunakan kunci Gemini API

Untuk menggunakan Gemini API, Anda harus mengautentikasi permintaan Anda. Anda dapat
melakukan autentikasi menggunakan kunci API standar atau otorisasi.

[Membuat atau melihat Kunci Gemini API](https://aistudio.google.com/apikey?hl=id)

## Jenis kunci API: standar versus otorisasi

Kunci API memberikan akses ke Gemini API, tetapi karakteristik keamanannya berbeda. Gemini API sedang bertransisi dari kunci API standar ke kunci otorisasi untuk meningkatkan keamanan:

- **Kunci API standar**: Mengaitkan permintaan dengan project Google Cloud untuk tujuan penagihan dan kuota. Kunci standar tidak mengidentifikasi pemanggil, yang
  membatasi perincian izin dan kontrol akses yang dapat didukungnya.
- **Kunci otorisasi (auth)**: Terikat langsung ke akun layanan Google Cloud. Saat Anda menggunakan kunci otorisasi, permintaan Anda diproses
  dengan identitas akun layanan yang terikat tersebut, sehingga memungkinkan kontrol
  akses yang terperinci. Kunci otorisasi dibatasi untuk Generative Language API
  (Gemini API) secara default dan memberikan penegakan kunci yang bocor yang bertindak cepat
  yang dengan cepat menghentikan penggunaan kunci yang bocor yang terdeteksi oleh sistem kami.

Untuk memastikan penggunaan yang aman, Gemini API akan beralih dari kunci Standard ke kunci Auth:

- **Kunci autentikasi default**: Semua kunci API baru yang dibuat di Google AI Studio
  akan otomatis dibuat sebagai kunci autentikasi.
- **Kunci yang tidak dibatasi ditolak**: Gemini API menolak permintaan
  dari **kunci standar yang tidak dibatasi**. Kunci API standar yang memiliki pembatasan eksplisit yang diterapkan akan terus berfungsi. Pembatasan ini mencegah
  penggunaan kunci yang tidak sah yang mungkin dibagikan secara publik atau ditautkan ke
  layanan lain.
- **Pada September 2026**: Gemini API akan menolak permintaan dari **kunci Standard**. Anda harus [bermigrasi ke kunci autentikasi](#migrate-to-auth-key)
  sebelum tanggal ini untuk menghindari gangguan layanan. Pastikan untuk memigrasikan ke kunci
  auth sebelum September 2026.

## Mengelola kunci API di Google AI Studio

Anda dapat mengelola project dan kunci langsung di [Google AI Studio](https://aistudio.google.com/apikey?hl=id).

### Project Google Cloud

Setiap kunci API Gemini dikaitkan dengan [project Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=id).
Project Google Cloud mengelola penagihan, kolaborator, dan izin. Google AI Studio menyediakan antarmuka ringan untuk mengakses project ini.

- **Project default**: Jika Anda adalah pengguna baru, Google AI Studio akan otomatis
  membuat project Google Cloud dan kunci API default setelah Anda menyetujui
  Persyaratan Layanan. Anda dapat mengganti nama project ini dengan membuka
  tampilan **Project** di dasbor.
- **Project yang ada**: Jika Anda sudah memiliki akun Google Cloud, AI
  Studio tidak akan membuat project default. Sebagai gantinya, Anda harus mengimpor project yang ada.

### Mengimpor project

Secara default, Google AI Studio tidak menampilkan semua project Google Cloud Anda. Anda harus mengimpor project yang ingin digunakan:

1. Buka [Google AI Studio](https://aistudio.google.com?hl=id).
2. Buka **Dashboard** dari panel kiri, lalu pilih **Projects**.
3. Klik tombol **Impor project**.
4. Telusuri dan pilih project Google Cloud yang ingin Anda impor, lalu
   klik **Impor**.
5. Setelah diimpor, buka halaman **Kunci API** di dasbor untuk membuat kunci di project tersebut.

### Memecahkan masalah izin pembuatan kunci

Jika tombol **Buat kunci API** tidak tersedia dan menampilkan pesan:
*"Anda tidak memiliki izin untuk membuat kunci di project ini"*, berarti Anda tidak memiliki
izin IAM yang diperlukan.

Minta administrator project atau organisasi Google Cloud Anda untuk memberi Anda peran
yang berisi izin berikut (seperti Editor Project):

- `resourcemanager.projects.get`: Memungkinkan AI Studio memverifikasi project.
- `apikeys.keys.create`: Mengizinkan pembuatan kunci.
- `serviceusage.services.enable`: Memastikan Generative Language API diaktifkan.
- `iam.serviceAccounts.create`: Diperlukan untuk membuat akun layanan tertaut.
- `iam.serviceAccountApiKeyBindings.create`: Mengikat akun layanan ke
  kunci API.

Jika tidak bisa mendapatkan akses administratif, Anda dapat membuat project Google Cloud baru yang tidak terkait dengan organisasi untuk membuat kunci Anda.

## Menyiapkan lingkungan Anda

Setelah memiliki kunci, konfigurasikan lingkungan Anda untuk menggunakannya secara aman di aplikasi Anda.

### Opsi 1: Menggunakan variabel lingkungan (direkomendasikan)

Tetapkan variabel lingkungan `GEMINI_API_KEY` atau `GOOGLE_API_KEY`. Library klien Gemini API otomatis mendeteksi dan menggunakan variabel ini. Jika keduanya
disetel, `GOOGLE_API_KEY` akan diprioritaskan.

Pilih sistem operasi Anda untuk menyetel variabel:

### Linux/macOS - Bash

Verifikasi apakah Anda memiliki file konfigurasi bash:

```
~/.bashrc
```

Jika belum, buat dan buka:

```
touch ~/.bashrc && open ~/.bashrc
```

Tambahkan perintah ekspor di akhir file:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Simpan file, lalu terapkan perubahan:

```
source ~/.bashrc
```

### macOS - Zsh

Verifikasi apakah Anda memiliki file konfigurasi zsh:

```
~/.zshrc
```

Jika belum, buat dan buka:

```
touch ~/.zshrc && open ~/.zshrc
```

Tambahkan perintah ekspor:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Simpan file, lalu terapkan perubahan:

```
source ~/.zshrc
```

### Windows

1. Telusuri "Environment Variables" di kotak penelusuran Windows.
2. Klik **Environment Variables** di dialog System Properties.
3. Di bagian **User variables** atau **System variables**, klik **New...**.
4. Tetapkan nama variabel ke `GEMINI_API_KEY` dan nilai ke kunci API Anda.
5. Klik **Oke** untuk menyimpan. Buka sesi terminal baru untuk memuat variabel.

### Opsi 2: Berikan kunci API secara eksplisit dalam kode

Anda dapat meneruskan kunci API secara eksplisit saat menginisialisasi klien. Lakukan ini hanya
jika Anda tidak dapat menggunakan variabel lingkungan.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
    "google.golang.org/genai/interactions"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.5-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.5-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Pengelolaan keamanan dan secret

Perlakukan kunci Gemini API Anda seperti sandi. Jika akun Anda disusupi, orang lain dapat menggunakan kuota project Anda, menimbulkan biaya penagihan yang tidak terduga, dan mengakses resource pribadi.

### Aturan keamanan penting

- **Jaga kerahasiaan kunci**: Jangan pernah melakukan check in kunci API ke dalam sistem kontrol sumber seperti Git.
- **Jangan pernah menampilkan kunci sisi klien dalam produksi**: Jangan menyandikan kunci API secara langsung di aplikasi web atau seluler. Kunci yang dikompilasi dalam kode sisi klien dapat
  diekstrak oleh pengguna. Untuk mengamankan aplikasi sisi klien, jalankan server proxy backend untuk melakukan panggilan API yang sebenarnya.

### Praktik terbaik pengelolaan secret

- **Variabel lingkungan**: Membaca kunci dari variabel lingkungan, bukan dari
  file konfigurasi.
- **Secret Manager**: Untuk produksi, simpan kunci Anda di penyimpanan rahasia yang aman seperti [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=id).
- **Pemberitahuan penagihan**: Siapkan pemberitahuan penagihan di Konsol Google Cloud untuk memberi tahu Anda jika penggunaan atau biaya meningkat tajam.

### Checklist respons kebocoran

Jika Anda menduga kunci API Anda telah bocor:

1. **Buat kunci baru**: Buat kunci pengganti di Google AI Studio atau
   Konsol Cloud.
2. **Perbarui aplikasi Anda**: Deploy kode Anda menggunakan kunci baru.
3. **Nonaktifkan atau hapus kunci yang disusupi**: Nonaktifkan kunci yang bocor di
   Konsol Cloud setelah kunci baru diverifikasi. Jangan hapus kunci lama hingga kunci baru aktif sepenuhnya untuk menghindari periode nonaktif aplikasi.
4. **Audit penggunaan**: Periksa log penagihan dan penggunaan API di Konsol Google Cloud untuk mengidentifikasi aktivitas yang tidak sah.

## Membatasi dan mengamankan kunci Anda

Menambahkan batasan ke kunci API Anda akan meminimalkan potensi kerusakan jika kunci disusupi.

### Menerapkan batasan asal permintaan

Pembatasan asal membatasi alamat IP, situs, atau aplikasi yang dapat menggunakan kunci Anda.

1. Buka [halaman Kredensial Konsol Google Cloud](https://console.cloud.google.com/apis/credentials?hl=id).
2. Pilih project Anda, lalu klik nama kunci API yang ingin Anda batasi.
3. Di bagian **Pembatasan aplikasi**, pilih **Alamat IP** (atau jenis pembatasan yang sesuai untuk lingkungan Anda).
4. Tentukan rentang atau alamat IP yang diizinkan, lalu klik **Simpan**.

### Mengamankan kunci API standar yang tidak dibatasi

Untuk terus menggunakan Gemini API, Anda harus mengamankan kunci yang tidak dibatasi.

#### Metode A: Membatasi kunci hanya untuk Gemini API (AI Studio)

Jika Anda hanya menggunakan kunci untuk Gemini API, amankan kunci tersebut langsung di AI Studio:

1. Di halaman **API Keys** di [Google AI Studio](https://aistudio.google.com/api-keys?hl=id), temukan kunci yang ditandai dengan label
   **Unrestricted**.
2. Arahkan kursor ke label dan klik **Tambahkan batasan** dalam dialog.
3. Pilih **Batasi hanya untuk Gemini API**.
4. Klik **Restrict key** untuk mengonfirmasi.

#### Metode B: Membatasi kunci untuk layanan lain (Konsol Google Cloud)

Jika kunci dibagikan dengan Google API lain (tidak direkomendasikan), batasi di Konsol Cloud. **Catatan: Permintaan Gemini API menggunakan kunci ini akan gagal setelah
pembatasan ini diterapkan.**

1. Buka [halaman Kredensial Konsol Google Cloud](https://console.cloud.google.com/apis/credentials?hl=id).
2. Pilih project dan kunci API.
3. Di bagian **API restrictions**, gunakan drop-down **Select API restrictions** untuk memilih API yang ingin diakses oleh kunci ini. Jangan pilih **Generative
   Language API**.
4. Klik **Simpan**. Buat kunci terpisah yang dibatasi di AI Studio untuk terus menggunakan Gemini API.

### Kunci tidak aktif yang diblokir

Mulai 7 Mei 2026, Gemini API akan memblokir kunci API yang tidak dibatasi yang tidak aktif dalam jangka waktu yang lama. Kunci ini menampilkan tag **Diblokir** di AI Studio. Anda harus membuat kunci baru atau menggunakan kunci terbatas yang ada untuk
melanjutkan.

## Bermigrasi ke kunci autentikasi

Ikuti langkah-langkah berikut untuk membuat kunci API autentikasi baru dan mengupdate aplikasi Anda:

1. Buka [halaman Kunci API AI Studio](https://aistudio.google.com/api-keys?hl=id).
2. Periksa kolom **Jenis Kunci** untuk mengidentifikasi kunci yang tercantum sebagai **Standar**.
3. Klik **Buat kunci API** untuk membuat kunci baru. Semua kunci baru yang dibuat di AI Studio akan otomatis dibuat sebagai kunci autentikasi.
4. Salin kunci API autentikasi baru.
5. Perbarui kode aplikasi, variabel lingkungan, dan konfigurasi deployment apa pun untuk menggunakan kunci API autentikasi baru.
6. Uji aplikasi Anda untuk mengonfirmasi bahwa aplikasi berfungsi dengan benar menggunakan kunci baru.
7. Setelah diverifikasi, hapus atau batalkan kunci traffic lama Anda untuk mencegah penyalahgunaan.

## Batasan

Google AI Studio menerapkan batasan pengelolaan project dan kunci berikut:

- Anda dapat membuat maksimal 10 project sekaligus dari halaman **Project** di Google AI Studio.
- Halaman **API keys** dan **Projects** menampilkan maksimum 100 kunci dan 50 project.
- Hanya kunci API yang tidak dibatasi atau dibatasi secara khusus untuk Generative Language API (Gemini API) yang ditampilkan.

Untuk pengelolaan project lanjutan atau untuk mengubah kunci dengan batasan lain, gunakan
[halaman kredensial Konsol Google Cloud](https://console.cloud.google.com/apis/credentials?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-16 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-16 UTC."],[],[]]
