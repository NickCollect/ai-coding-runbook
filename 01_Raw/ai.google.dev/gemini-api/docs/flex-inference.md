---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=id
fetched_at: 2026-05-05T13:16:07.265483+00:00
title: "Inferensi fleksibel \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/Deep Research Gemini) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

- [Beranda](https://ai.google.dev/gemini-api/docs/Beranda)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokumen](https://ai.google.dev/gemini-api/docs/Dokumen)

Kirim masukan

# Inferensi fleksibel

Gemini Flex API adalah tingkat inferensi yang menawarkan pengurangan biaya sebesar 50% dibandingkan dengan tarif standar, sebagai imbalan atas latensi variabel dan ketersediaan upaya terbaik. API ini dirancang untuk beban kerja yang toleran terhadap latensi yang memerlukan pemrosesan sinkron, tetapi tidak memerlukan performa real-time dari API standar.

## Cara menggunakan Flex

Untuk menggunakan tingkat Flex, tentukan `service_tier` sebagai `flex` di
isi permintaan. Secara default, permintaan menggunakan tingkat standar jika kolom ini tidak diisi.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
  }
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
        "gemini-3-flash-preview",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Cara kerja inferensi Flex

Inferensi Gemini Flex menjembatani kesenjangan antara API standar dan waktu penyelesaian 24 jam [Batch API](https://ai.google.dev/gemini-api/docs/Batch API). Layanan ini memanfaatkan kapasitas komputasi di luar jam sibuk yang dapat dihentikan untuk memberikan solusi hemat biaya bagi tugas latar belakang dan alur kerja berurutan.

| Fitur | Lipat | Prioritas | Standar | Batch |
| --- | --- | --- | --- | --- |
| **Harga** | Diskon 50% | 75-100% lebih banyak daripada Standard | Harga penuh | Diskon 50% |
| **Latensi** | Menit (target 1–15 menit) | Rendah (Detik) | Detik ke menit | Hingga 24 jam |
| **Keandalan** | Upaya terbaik (Dapat Dihapus) | Tinggi (Tidak rontok) | Tinggi / Sedang tinggi | Tinggi (untuk throughput) |
| **Antarmuka** | Sinkron | Sinkron | Sinkron | Asinkron |

### Manfaat utama

- **Efisiensi biaya**: Penghematan yang signifikan untuk evaluasi non-produksi, agen latar belakang, dan pengayaan data.
- **Gesekan rendah**: Tidak perlu mengelola objek batch, ID tugas, atau polling; cukup tambahkan satu parameter ke permintaan yang ada.
- **Alur kerja sinkron**: Ideal untuk rangkaian API berurutan di mana permintaan berikutnya bergantung pada output permintaan sebelumnya, sehingga lebih fleksibel daripada Batch untuk alur kerja agentik.

### Kasus penggunaan

- **Evaluasi offline**: Menjalankan pengujian regresi atau papan peringkat "LLM sebagai juri".
- **Agen latar belakang**: Tugas berurutan seperti pembaruan CRM, pembuatan profil, atau moderasi konten yang dapat ditunda beberapa menit.
- **Riset dengan anggaran terbatas**: Eksperimen akademis yang memerlukan volume token tinggi dengan anggaran terbatas.

### Batas kapasitas

Traffic inferensi fleksibel dihitung dalam [batas kapasitas](https://ai.google.dev/gemini-api/docs/batas kapasitas) umum Anda; tidak
menawarkan batas kapasitas yang diperluas seperti [Batch API](https://ai.google.dev/gemini-api/docs/Batch API).

### Kapasitas yang dapat dikurangi

Traffic fleksibel diperlakukan dengan prioritas yang lebih rendah. Jika terjadi lonjakan traffic standar, permintaan Fleksibel dapat didahulukan atau dikeluarkan untuk memastikan kapasitas bagi pengguna prioritas tinggi. Jika Anda mencari inferensi prioritas tinggi, lihat
[Inferensi prioritas](https://ai.google.dev/gemini-api/docs/Inferensi prioritas)

### Kode error

Jika kapasitas Flex tidak tersedia atau sistem mengalami kemacetan, API akan
menampilkan kode error standar:

- **503 Layanan Tidak Tersedia**: Sistem saat ini mencapai batas kapasitas.
- **429 Too Many Requests**: Batas frekuensi atau kehabisan resource.

### Tanggung jawab klien

- **Tidak ada penggantian sisi server**: Untuk mencegah biaya yang tidak terduga, sistem tidak akan otomatis mengupgrade permintaan Flex ke paket Standar jika kapasitas Flex penuh.
- **Percobaan ulang**: Anda harus menerapkan logika percobaan ulang sisi klien sendiri dengan
  backoff eksponensial.
- **Waktu tunggu**: Karena permintaan Flex mungkin berada dalam antrean, sebaiknya
  perpanjang waktu tunggu sisi klien menjadi 10 menit atau lebih untuk menghindari penutupan
  koneksi sebelum waktunya.

## Menyesuaikan periode tunggu

Anda dapat mengonfigurasi waktu tunggu per permintaan untuk REST API dan library klien,
serta waktu tunggu global hanya saat menggunakan library klien.

Selalu pastikan waktu tunggu sisi klien Anda mencakup periode waktu tunggu server yang diinginkan (misalnya, 600 detik+ untuk antrean tunggu Flex). SDK mengharapkan nilai waktu tunggu dalam
milidetik.

### Waktu tunggu per permintaan

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3-flash-preview",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3-flash-preview",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
     }
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3-flash-preview",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

Saat melakukan panggilan REST, Anda dapat mengontrol waktu tunggu menggunakan kombinasi header HTTP dan opsi `curl`:

- Header **`X-Server-Timeout` (waktu tunggu sisi server)**: Header ini menyarankan durasi waktu tunggu yang disukai (default 600 detik) ke server Gemini API. Server
  akan mencoba mematuhinya, tetapi tidak dijamin. Nilai harus dalam
  detik.
- **`--max-time` di `curl` (Waktu Tunggu Sisi Klien)**: Opsi `curl --max-time
  <seconds>` menetapkan batas ketat pada total waktu (dalam detik) yang akan ditunggu `curl`
  hingga seluruh operasi selesai. Ini adalah pengamanan sisi klien.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### Waktu tunggu global

Jika ingin semua panggilan API yang dilakukan melalui instance `genai.Client` tertentu
(khusus library klien) memiliki waktu tunggu default, Anda dapat mengonfigurasi ini saat
menginisialisasi klien menggunakan `http_options` dan `genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3-flash-preview",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
    }
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3-flash-preview")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## Menerapkan percobaan ulang

Karena Flex dapat dihentikan dan gagal dengan error 503, berikut contoh penerapan logika percobaan ulang secara opsional untuk melanjutkan permintaan yang gagal:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3-flash-preview",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3-flash-preview",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3-flash-preview",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3-flash-preview"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## Harga

Inferensi fleksibel dihargai 50% dari [API standar](https://ai.google.dev/gemini-api/docs/API standar)
dan ditagih per token.

## Model yang didukung

Model berikut mendukung inferensi Flex:

| Model | Inferensi fleksibel |
| --- | --- |
| [Pratinjau Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/Pratinjau Gemini 3.1 Flash-Lite) | ✔️ |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/Pratinjau Gemini 3.1 Pro) | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/Pratinjau Gemini 3 Flash) | ✔️ |
| [Pratinjau Gambar Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/Pratinjau Gambar Gemini 3 Pro) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Pro) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash) | ✔️ |
| [Gambar Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/Gambar Gemini 2.5 Flash) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/Gemini 2.5 Flash-Lite) | ✔️ |

## Langkah berikutnya

Baca opsi [inferensi dan pengoptimalan](https://ai.google.dev/gemini-api/docs/inferensi dan pengoptimalan) Gemini lainnya:

- [Inferensi prioritas](https://ai.google.dev/gemini-api/docs/Inferensi prioritas) untuk latensi ultra-rendah.
- [Batch API](https://ai.google.dev/gemini-api/docs/Batch API) untuk pemrosesan asinkron dalam waktu 24 jam.
- [Penyimpanan cache konteks](https://ai.google.dev/gemini-api/docs/Penyimpanan cache konteks) untuk mengurangi biaya token input.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Lisensi Creative Commons Attribution 4.0), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://ai.google.dev/gemini-api/docs/Lisensi Apache 2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://ai.google.dev/gemini-api/docs/Kebijakan Situs Google Developers). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-04-29 UTC.

Ada masukan untuk kami?
