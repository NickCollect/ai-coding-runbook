---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=id
fetched_at: 2026-05-25T05:27:42.706750+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Eksekusi kode

Gemini API menyediakan alat eksekusi kode yang memungkinkan model untuk membuat dan menjalankan kode Python. Kemudian, model dapat belajar secara iteratif dari hasil eksekusi kode hingga mencapai output akhir. Anda dapat menggunakan eksekusi kode untuk membangun aplikasi yang memanfaatkan penalaran berbasis kode. Misalnya, Anda dapat menggunakan eksekusi kode untuk menyelesaikan persamaan atau memproses teks. Anda juga dapat menggunakan [library](#supported-libraries) yang disertakan dalam lingkungan eksekusi kode untuk melakukan tugas yang lebih khusus.

Gemini hanya dapat mengeksekusi kode di Python. Anda tetap dapat meminta Gemini untuk membuat kode dalam bahasa lain, tetapi model tidak dapat menggunakan alat eksekusi kode untuk menjalankannya.

## Mengaktifkan eksekusi kode

Untuk mengaktifkan eksekusi kode, konfigurasi alat eksekusi kode pada model. Hal ini
memungkinkan model membuat dan menjalankan kode.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
}'
```

Outputnya mungkin akan terlihat seperti berikut, yang telah diformat agar mudah dibaca:

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

Output ini menggabungkan beberapa bagian konten yang ditampilkan model saat menggunakan eksekusi kode:

- `text`: Teks inline yang dihasilkan oleh model
- `executableCode`: Kode yang dibuat oleh model yang dimaksudkan untuk dieksekusi
- `codeExecutionResult`: Hasil kode yang dapat dieksekusi

Konvensi penamaan untuk bagian ini bervariasi menurut bahasa pemrograman.

## Eksekusi Kode dengan gambar (Gemini 3)

Model Gemini 3 Flash kini dapat menulis dan mengeksekusi kode Python untuk memanipulasi dan memeriksa gambar secara aktif.

**Kasus penggunaan**

- **Zoom dan periksa**: Model secara implisit mendeteksi saat detail terlalu kecil
  (misalnya, membaca pengukur dari jarak jauh) dan menulis kode untuk memangkas dan memeriksa ulang area
  pada resolusi yang lebih tinggi.
- **Matematika visual**: Model dapat menjalankan penghitungan multi-langkah menggunakan kode (misalnya, menjumlahkan item baris pada tanda terima).
- **Anotasi gambar**: Model dapat menganotasi gambar untuk menjawab pertanyaan, seperti menggambar panah untuk menunjukkan hubungan.

### Mengaktifkan Eksekusi Kode dengan gambar

Eksekusi Kode dengan gambar secara resmi didukung di Gemini 3 Flash. Anda dapat
mengaktifkan perilaku ini dengan mengaktifkan Eksekusi Kode sebagai alat dan Pemikiran.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
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
    "io"
    "log"
    "net/http"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.5-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## Menggunakan eksekusi kode dalam percakapan

Anda juga dapat menggunakan eksekusi kode sebagai bagian dari percakapan.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3.5-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3.5-flash",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## Input/output (I/O)

Eksekusi kode mendukung input file dan output grafik. Dengan kemampuan input dan output ini, Anda dapat mengupload file CSV dan teks, mengajukan pertanyaan tentang file, dan membuat grafik [Matplotlib](https://matplotlib.org/) sebagai bagian dari respons. File output ditampilkan sebagai gambar inline dalam respons.

### Harga I/O

Saat menggunakan I/O eksekusi kode, Anda akan ditagih untuk token input dan token output:

**Token input:**

- Perintah pengguna

**Token output:**

- Kode yang dihasilkan oleh model
- Output eksekusi kode di lingkungan kode
- Token pemikiran
- Ringkasan yang dibuat oleh model

### Detail I/O

Saat Anda menangani I/O eksekusi kode, perhatikan detail teknis berikut:

- Runtime maksimum lingkungan kode adalah 30 detik.
- Jika lingkungan kode menghasilkan error, model dapat memutuskan untuk
  membuat ulang output kode. Hal ini dapat terjadi hingga 5 kali.
- Ukuran input file maksimum dibatasi oleh jendela token model. Di AI Studio, ukuran file input maksimum adalah 1 juta token (kira-kira 2 MB untuk file teks dari jenis input yang didukung). Jika Anda
  mengupload file yang terlalu besar, AI Studio tidak akan mengizinkan Anda mengirimkannya.
- Eksekusi kode berfungsi paling baik dengan file teks dan CSV.
- File input dapat diteruskan dalam `part.inlineData` atau `part.fileData` (diupload
  melalui [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id)), dan file output selalu
  ditampilkan sebagai `part.inlineData`.

## Penagihan

Tidak ada biaya tambahan untuk mengaktifkan eksekusi kode dari Gemini API.
Anda akan ditagih dengan tarif token input dan output saat ini berdasarkan model Gemini yang Anda gunakan.

Berikut beberapa hal lain yang perlu diketahui tentang penagihan untuk eksekusi kode:

- Anda hanya ditagih satu kali untuk token input yang Anda teruskan ke model, dan Anda ditagih untuk token output akhir yang dikembalikan kepada Anda oleh model.
- Token yang merepresentasikan kode yang dihasilkan dihitung sebagai token output. Kode yang dihasilkan dapat mencakup teks dan output multimodal seperti gambar.
- Hasil eksekusi kode juga dihitung sebagai token output.

Model penagihan ditampilkan dalam diagram berikut:

![model penagihan eksekusi kode](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=id)

- Anda akan ditagih dengan tarif token input dan output saat ini berdasarkan
  model Gemini yang Anda gunakan.
- Jika Gemini menggunakan eksekusi kode saat membuat respons Anda, perintah asli, kode yang dihasilkan, dan hasil kode yang dieksekusi akan diberi label *token perantara* dan ditagih sebagai *token input*.
- Kemudian, Gemini membuat ringkasan dan menampilkan kode yang dihasilkan, hasil dari
  kode yang dieksekusi, dan ringkasan akhir. Token ini ditagih sebagai *token output*.
- Gemini API menyertakan jumlah token perantara dalam respons API, sehingga Anda tahu alasan Anda mendapatkan token input tambahan di luar perintah awal Anda.

## Batasan

- Model hanya dapat membuat dan mengeksekusi kode. Metode ini tidak dapat menampilkan artefak lain seperti file media.
- Dalam beberapa kasus, mengaktifkan eksekusi kode dapat menyebabkan regresi di area output model lainnya (misalnya, menulis cerita).
- Ada beberapa variasi dalam kemampuan berbagai model untuk berhasil menggunakan eksekusi kode.

## Kombinasi alat yang didukung

Alat eksekusi kode dapat digabungkan dengan
[Perujukan dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) untuk
mendukung kasus penggunaan yang lebih kompleks.

Model Gemini 3 mendukung penggabungan alat bawaan (seperti Eksekusi Kode) dengan alat kustom (panggilan fungsi). Anda harus meneruskan kembali kolom `id` dan
`thought_signature` agar kombinasi alat berfungsi. Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

## Library yang didukung

Lingkungan eksekusi kode mencakup library berikut:

- attrs
- catur
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- paket
- pandas
- bantal
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- enam
- striprtf
- sympy
- tabulasi
- tensorflow
- toolz
- xlrd

Anda tidak dapat menginstal library Anda sendiri.

## Langkah berikutnya

- Coba
  [Colab eksekusi kode](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=id).
- Pelajari alat Gemini API lainnya:
  - [Panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
  - [Melakukan grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/grounding?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
