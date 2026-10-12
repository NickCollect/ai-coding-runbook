---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=id
fetched_at: 2026-10-12T07:01:02.264604+00:00
title: "Grounding with Google Search \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Grounding with Google Search

Grounding with Google Search menghubungkan model Gemini ke konten web real-time dan berfungsi dengan semua bahasa yang tersedia. Dengan fitur ini, Gemini dapat memberikan jawaban yang lebih akurat dan mengutip sumber yang dapat diverifikasi di luar batas informasinya.

Perujukan membantu Anda membangun aplikasi yang dapat:

- **Meningkatkan akurasi faktual:** Mengurangi halusinasi model dengan mendasarkan respons pada informasi dunia nyata.
- **Mengakses informasi real-time:** Menjawab pertanyaan tentang peristiwa dan topik terbaru.
- **Memberikan kutipan:** Bangun kepercayaan pengguna dengan menampilkan sumber klaim model.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(resp.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## Cara kerja perujukan dengan Google Penelusuran

Saat Anda mengaktifkan alat `google_search`, model akan menangani seluruh alur kerja
untuk menelusuri, memproses, dan mengutip informasi secara otomatis.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=id)

1. **Perintah Pengguna:** Aplikasi Anda mengirimkan perintah pengguna ke Gemini API
   dengan mengaktifkan alat `google_search`.
2. **Analisis Perintah:** Model menganalisis perintah dan menentukan apakah Google Penelusuran dapat meningkatkan kualitas jawaban.
3. **Google Penelusuran:** Jika diperlukan, model akan otomatis membuat satu atau beberapa kueri penelusuran dan menjalankannya.
4. **Pemrosesan Hasil Penelusuran:** Model memproses hasil penelusuran, menyintesis informasi, dan merumuskan respons.
5. **Respons yang Di-grounding:** API menampilkan respons akhir yang mudah digunakan dan
   didasarkan pada hasil penelusuran. Respons ini mencakup jawaban teks model dengan `annotations` inline yang berisi kutipan, serta langkah-langkah `google_search_call` dan `google_search_result` dengan kueri penelusuran dan saran penelusuran.

## Memahami respons perujukan

Jika respons berhasil dirujuk, output teks model akan menyertakan `annotations` inline langsung di blok konten teks. Anotasi ini
memberikan informasi kutipan yang menautkan bagian respons ke sumbernya.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

Kolom utama dalam respons:

- `google_search_call` : Berisi penelusuran `queries` yang dijalankan model.
- `google_search_result` : Berisi `search_suggestions`, cuplikan HTML
  untuk merender saran penelusuran di UI Anda. Persyaratan penggunaan lengkap dijelaskan dalam [Persyaratan Layanan](https://ai.google.dev/gemini-api/terms?hl=id#grounding-with-google-search).
- `text` dengan `annotations` : Jawaban yang disintesis model dengan kutipan inline. Setiap anotasi `url_citation` menautkan segmen teks (ditentukan
  oleh `start_index` dan `end_index`) ke URL sumber. Langkah ini adalah kunci untuk membuat kutipan sebaris.

Pen-groundingan dengan Google Penelusuran juga dapat digunakan bersama dengan [alat konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id) untuk men-grounding respons dalam
data web publik dan URL tertentu yang Anda berikan.

## Mengatribusikan sumber dengan kutipan di dalam teks

API menampilkan anotasi `url_citation` inline pada blok konten teks, sehingga Anda memiliki kontrol penuh atas cara menampilkan sumber di antarmuka pengguna.
Setiap anotasi menyertakan `start_index` dan `end_index` untuk mengidentifikasi bagian teks yang dikutipnya. Berikut cara mengekstrak dan menampilkannya.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(GoogleSearch.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            String text = textContent.text().orElse("");
            System.out.println(text);
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nCitations:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof URLCitation) {
                  URLCitation citation = (URLCitation) annotation;
                  int start = citation.startIndex().orElse(0);
                  int end = citation.endIndex().orElse(0);
                  String citedText =
                      (start >= 0 && end <= text.length() && start <= end)
                          ? text.substring(start, end)
                          : "";
                  System.out.printf(
                      "  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
                  System.out.printf("    Cited text: \"%s\"%n", citedText);
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    resp, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(
            interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput("Who won the euro 2024?"),
                Tools: []interactions.Tool{
                    interactions.NewTool(interactions.GoogleSearch{}),
                },
            },
        ),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range resp.Interaction.Steps {
        if step.ModelOutputStep != nil {
            for _, content := range step.ModelOutputStep.Content {
                if content.TextContent != nil {
                    text := content.TextContent.Text
                    fmt.Println(text)
                    if len(content.TextContent.Annotations) > 0 {
                        fmt.Println("\nCitations:")
                        for _, annotation := range content.TextContent.Annotations {
                            if annotation.URLCitation != nil {
                                c := annotation.URLCitation
                                start := 0
                                if c.StartIndex != nil {
                                    start = *c.StartIndex
                                }
                                end := 0
                                if c.EndIndex != nil {
                                    end = *c.EndIndex
                                }
                                citedText := ""
                                if start >= 0 && end <= len(text) && start <= end {
                                    citedText = text[start:end]
                                }
                                title := ""
                                if c.Title != nil {
                                    title = *c.Title
                                }
                                url := ""
                                if c.URL != nil {
                                    url = *c.URL
                                }
                                fmt.Printf("  [%s](%s)\n", title, url)
                                fmt.Printf("    Cited text: %q\n", citedText)
                            }
                        }
                    }
                }
            }
        }
    }
}
```

Output akan menampilkan teks yang diikuti dengan kutipannya:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## Harga

Saat Anda menggunakan Grounding with Google Search dengan Gemini 3 dan model yang lebih baru, project Anda akan ditagih untuk **setiap** kueri penelusuran yang diputuskan untuk dijalankan oleh model.
Model penagihan per kueri ini mencakup 5.000 permintaan penelusuran gratis per bulan yang dibagikan di semua model Gemini 3 dan yang lebih baru, lalu dikenai biaya **$14 per 1.000 permintaan penelusuran**.

Misalnya, jika model memutuskan untuk menjalankan beberapa kueri penelusuran untuk menjawab satu perintah (misalnya, menelusuri `"UEFA Euro 2024 winner"` dan `"Spain vs
England Euro 2024 final score"` dalam panggilan API yang sama), hal ini dihitung sebagai dua penggunaan alat yang dapat ditagih untuk permintaan tersebut. Untuk tujuan penagihan, kami mengabaikan
kueri penelusuran web kosong saat menghitung kueri unik.

Saat Anda menggunakan perujukan penelusuran dengan model Gemini 2.5 atau yang lebih lama, project Anda ditagih per perintah.

Untuk mengetahui informasi harga mendetail, lihat [halaman harga Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=id).

## Model yang didukung

Anda dapat menemukan kemampuan lengkap di halaman [ringkasan model](https://ai.google.dev/gemini-api/docs/models?hl=id).

| Model | Grounding dengan Google Penelusuran |
| --- | --- |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Pratinjau Gambar Gemini 3.1 Flash | ✔️ |
| Pratinjau Gemini 3.1 Pro | ✔️ |
| Pratinjau Gambar Gemini 3 Pro | ✔️ |
| Pratinjau Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Kombinasi alat yang didukung

Anda dapat menggunakan Grounding dengan Google Penelusuran bersama alat lain seperti
[eksekusi kode](https://ai.google.dev/gemini-api/docs/code-execution?hl=id),
[konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id), dan
[Grounding dengan Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=id) (didukung di
Gemini 3.5 Flash-Lite dan model yang lebih baru) untuk mendukung kasus penggunaan yang lebih kompleks.
Model Gemini 3 juga mendukung penggabungan alat bawaan ini dengan alat kustom (panggilan fungsi). Pelajari lebih lanjut di halaman
[kombinasi alat](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id).

## Langkah berikutnya

- Pelajari alat lain yang tersedia, seperti [Panggilan Fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id).
- Pelajari cara memperkaya perintah dengan URL tertentu menggunakan [alat konteks URL](https://ai.google.dev/gemini-api/docs/url-context?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
