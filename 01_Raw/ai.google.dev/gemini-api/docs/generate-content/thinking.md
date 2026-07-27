---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=id
fetched_at: 2026-07-27T04:40:18.329065+00:00
title: "Pemikiran Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pemikiran Gemini

[Model seri Gemini 3 dan 2.5](https://ai.google.dev/gemini-api/docs/models?hl=id) menggunakan "proses berpikir" internal yang secara signifikan meningkatkan kemampuan penalaran dan perencanaan multi-langkahnya, sehingga sangat efektif untuk tugas-tugas kompleks seperti coding, matematika tingkat lanjut, dan analisis data.

Panduan ini menunjukkan cara menggunakan kemampuan penalaran Gemini menggunakan
Gemini API.

## Membuat konten dengan pemikiran

Memulai permintaan dengan model pemikiran serupa dengan permintaan pembuatan konten lainnya. Perbedaan utamanya terletak pada penentuan salah satu
[model dengan dukungan pemikiran](#supported-models) di kolom `model`, seperti
yang ditunjukkan dalam contoh [pembuatan teks](https://ai.google.dev/gemini-api/docs/text-generation?hl=id#text-input) berikut:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: prompt,
  });

  console.log(response.text);
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
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## Ringkasan penalaran

Ringkasan pemikiran adalah versi ringkas dari pemikiran mentah model dan menawarkan insight tentang proses penalaran internal model. Perhatikan bahwa
tingkat pemikiran dan anggaran berlaku untuk pemikiran mentah model, bukan untuk ringkasan
pemikiran.

Anda dapat mengaktifkan ringkasan pemikiran dengan menyetel `includeThoughts` ke `true` dalam konfigurasi permintaan. Anda kemudian dapat mengakses ringkasan dengan melakukan iterasi pada `parts` parameter `response`, dan memeriksa boolean `thought`.

Berikut adalah contoh yang menunjukkan cara mengaktifkan dan mengambil ringkasan pemikiran tanpa streaming, yang menampilkan satu ringkasan pemikiran akhir dengan respons:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

Berikut adalah contoh penggunaan berpikir dengan streaming, yang menampilkan ringkasan inkremental
bergulir selama pembuatan:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.5-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## Mengontrol pemikiran

Model Gemini terlibat dalam pemikiran dinamis secara default, dengan otomatis menyesuaikan upaya penalaran berdasarkan kompleksitas permintaan pengguna.
Namun, jika Anda memiliki batasan latensi tertentu atau memerlukan model untuk melakukan penalaran yang lebih mendalam dari biasanya, Anda dapat menggunakan parameter secara opsional untuk mengontrol perilaku berpikir.

### Tingkat penalaran (Gemini 3)

Parameter `thinkingLevel`, yang direkomendasikan untuk model Gemini 3 dan yang lebih baru,
memungkinkan Anda mengontrol perilaku penalaran.

Tabel berikut menjelaskan setelan `thinkingLevel` untuk setiap jenis model:

| Tingkat Berpikir | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gambar Gemini 3.1 Flash-Lite | Gemini 3 Flash | Deskripsi |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | Didukung | Tidak didukung | Didukung (Default) | Didukung (Default) | Didukung | Cocok dengan setelan "tanpa penalaran" untuk sebagian besar kueri. Perhatikan, `minimal` tidak menjamin bahwa penalaran dinonaktifkan, model mungkin bernalar sangat minimal untuk tugas yang kompleks. |
| **`low`** | Didukung | Didukung | Didukung | Tidak Didukung | Didukung | Meminimalkan latensi dan biaya. |
| **`medium`** | Didukung (Default) | Didukung | Didukung | Tidak didukung | Didukung | Pemikiran yang seimbang untuk sebagian besar tugas. |
| **`high`** | Didukung (Dinamis) | Didukung (Default, Dinamis) | Didukung (Dinamis) | Didukung (Dinamis) | Didukung (Default, Dinamis) | Memaksimalkan kedalaman penalaran. Model mungkin memerlukan waktu yang jauh lebih lama untuk mencapai token output pertama (non-pemikiran), tetapi outputnya akan lebih beralasan. |

Contoh berikut menunjukkan cara menetapkan tingkat pemikiran.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

Anda tidak dapat menonaktifkan kemampuan berpikir untuk Gemini 3.1 Pro. Gemini 3 Flash dan Flash-Lite juga tidak mendukung penonaktifan penalaran sepenuhnya.
Jika Anda tidak menentukan tingkat penalaran, Gemini akan menggunakan tingkat penalaran default model Gemini 3 (misalnya, `"high"` untuk Gemini 3.1 Pro, dan `"medium"` untuk Gemini 3.5 Flash).

Model seri Gemini 2.5 tidak mendukung `thinkingLevel`; gunakan `thinkingBudget` sebagai gantinya.

### Anggaran penalaran

Parameter `thinkingBudget`, yang diperkenalkan dengan seri Gemini 2.5, memandu
model tentang jumlah token penalaran tertentu yang akan digunakan untuk melakukan penalaran.

Berikut adalah detail konfigurasi `thinkingBudget` untuk setiap jenis model.
Anda dapat menonaktifkan pemikiran dengan menyetel `thinkingBudget` ke 0.
Menetapkan `thinkingBudget` ke -1 akan mengaktifkan
**pemikiran dinamis**, yang berarti model akan menyesuaikan anggaran berdasarkan
kompleksitas permintaan.

| Model | Setelan default (Anggaran penalaran tidak ditetapkan) | Rentang | Menonaktifkan penalaran | Mengaktifkan pemikiran dinamis |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | Pemikiran dinamis | `128` hingga `32768` | T/A: Tidak dapat menonaktifkan pemikiran | `thinkingBudget = -1` (Default) |
| **2.5 Flash** | Pemikiran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **Pratinjau 2.5 Flash** | Pemikiran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **2.5 Flash Lite** | Model tidak berpikir | `512` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Pratinjau 2.5 Flash Lite** | Model tidak berpikir | `512` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Pratinjau Robotics-ER 1.6** | Pemikiran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |
| **Pratinjau Audio Native Live 2.5 Flash (09-2025)** | Pemikiran dinamis | `0` hingga `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (Default) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

Bergantung pada perintahnya, model dapat melampaui atau tidak memenuhi anggaran token.

## Tanda tangan penalaran

Gemini API bersifat stateless, sehingga model memperlakukan setiap permintaan API secara independen
dan tidak memiliki akses ke konteks pemikiran dari giliran sebelumnya dalam interaksi
multi-giliran.

Untuk memungkinkan pemeliharaan konteks pemikiran di seluruh interaksi multi-turn,
Gemini menampilkan tanda tangan pemikiran, yang merupakan representasi terenkripsi dari
proses pemikiran internal model.

- **Model Gemini 2.5** menampilkan tanda tangan pemikiran saat fitur penalaran diaktifkan dan
  permintaan mencakup [panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#thinking),
  khususnya [deklarasi fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-2).
- **Model Gemini 3** dapat menampilkan tanda tangan pemikiran untuk semua jenis [bagian](https://ai.google.dev/api/caching?hl=id#Part).
  Sebaiknya Anda selalu meneruskan semua tanda tangan seperti yang diterima, tetapi hal ini *wajib* untuk tanda tangan panggilan fungsi. Baca halaman
  [Thought Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id) untuk
  mempelajari lebih lanjut.

Batasan penggunaan lain yang perlu dipertimbangkan dengan panggilan fungsi mencakup:

- Tanda tangan ditampilkan dari model dalam bagian lain dalam respons,
  misalnya panggilan fungsi atau bagian teks.
  [Kembalikan seluruh respons](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-4)
  dengan semua bagian kembali ke model pada giliran berikutnya.
- Jangan menggabungkan bagian dengan tanda tangan.
- Jangan menggabungkan satu bagian dengan tanda tangan dengan bagian lain tanpa tanda tangan.

## Harga

Jika penalaran diaktifkan, harga respons adalah jumlah token output dan token penalaran. Anda bisa mendapatkan total jumlah token pemikiran yang dihasilkan dari kolom `thoughtsTokenCount`.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

Model pemikiran menghasilkan pemikiran lengkap untuk meningkatkan kualitas respons akhir, lalu menghasilkan [ringkasan](#summaries) untuk memberikan insight tentang proses pemikiran. Jadi, harga didasarkan pada token pemikiran penuh yang perlu dihasilkan model untuk membuat ringkasan, meskipun hanya ringkasan yang dihasilkan dari API.

Anda dapat mempelajari lebih lanjut token dalam panduan [Penghitungan token](https://ai.google.dev/gemini-api/docs/tokens?hl=id).

## Praktik terbaik

Bagian ini mencakup beberapa panduan untuk menggunakan model berpikir secara efisien.
Seperti biasa, mengikuti [panduan dan praktik terbaik pembuatan perintah](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id) kami akan memberikan hasil terbaik.

### Proses debug dan pengarahan

- **Tinjau penalaran**: Jika Anda tidak mendapatkan respons yang diharapkan dari model pemikiran, Anda dapat menganalisis ringkasan pemikiran Gemini dengan cermat.
  Anda dapat melihat cara model memecah tugas dan mencapai kesimpulannya, serta menggunakan informasi tersebut untuk mengoreksi hasil yang benar.
- **Memberikan Panduan dalam Penalaran**: Jika Anda menginginkan output yang sangat panjang, Anda dapat memberikan panduan dalam perintah untuk membatasi [jumlah pemikiran](#set-budget) yang digunakan model. Dengan begitu, Anda dapat mencadangkan lebih banyak output token untuk respons Anda.

### Kompleksitas tugas

- **Tugas Mudah (Pemikiran dapat DINONAKTIFKAN):** Untuk permintaan langsung yang tidak memerlukan penalaran yang kompleks, seperti pengambilan atau klasifikasi fakta, pemikiran tidak diperlukan. Contohnya antara lain:
  - "Di mana DeepMind didirikan?"
  - "Apakah email ini meminta rapat atau hanya memberikan informasi?"
- **Tugas Sedang (Default/Beberapa Pemikiran):** Banyak permintaan umum yang diuntungkan dari
  pemrosesan langkah demi langkah atau pemahaman yang lebih mendalam. Gemini dapat menggunakan kemampuan berpikir secara fleksibel untuk tugas-tugas seperti:
  - Menganalogikan fotosintesis dan tumbuh dewasa.
  - Bandingkan dan bedakan mobil listrik dan mobil hibrida.
- **Tugas Sulit (Kemampuan Berpikir Maksimum):** Untuk tantangan yang benar-benar kompleks,
  seperti menyelesaikan soal matematika yang rumit atau tugas coding, sebaiknya tetapkan
  anggaran berpikir yang tinggi. Jenis tugas ini mengharuskan model menggunakan kemampuan penalaran dan perencanaan sepenuhnya, yang sering kali melibatkan banyak langkah internal sebelum memberikan jawaban. Contohnya antara lain:
  - Pecahkan soal 1 di AIME 2025: Temukan jumlah semua bilangan bulat b > 9 yang
    membuat 17b menjadi pembagi 97b.
  - Menulis kode Python untuk aplikasi web yang memvisualisasikan data pasar saham real-time, termasuk autentikasi pengguna. Buat seefisien mungkin.

## Model, alat, dan kemampuan yang didukung

Fitur berpikir didukung di semua model seri 3 dan 2.5.
Anda dapat menemukan semua kemampuan model di halaman
[ringkasan model](https://ai.google.dev/gemini-api/docs/models?hl=id).

Model Penalaran berfungsi dengan semua alat dan kemampuan Gemini. Hal ini memungkinkan
model berinteraksi dengan sistem eksternal, mengeksekusi kode, atau mengakses informasi
real-time, dengan menggabungkan hasilnya ke dalam penalaran dan respons akhir.

Anda dapat mencoba contoh penggunaan alat dengan model pemikiran di
[Buku resep pemikiran][Colab].

## Apa langkah selanjutnya?

- Cakupan pemikiran tersedia di panduan [Kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id#thinking) kami.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-07 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-07 UTC."],[],[]]
