---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=id
fetched_at: 2026-08-31T06:42:02.059236+00:00
title: "Tanda tangan penalaran \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Tanda tangan penalaran

resmi dan menambahkan objek respons model lengkap langsung ke histori. **Anda
hanya perlu menggunakan tanda tangan pemikiran secara langsung saat menggunakan REST API**, atau
jika Anda *mengekstraksi dan menampilkan histori bagian secara manual dalam percakapan multi-giliran
percapan*.

Tanda tangan pemikiran adalah representasi terenkripsi dari proses pemikiran internal model dan digunakan untuk mempertahankan konteks penalaran di seluruh interaksi multi-langkah.
Saat menggunakan model penalaran (seperti seri Gemini 3 dan 2.5), API dapat
menampilkan kolom `thoughtSignature` dalam [bagian konten](https://ai.google.dev/api/caching?hl=id#Part)
respons (misalnya, bagian `text` atau `functionCall`).

Sebagai aturan umum, jika Anda menerima tanda tangan pemikiran dalam respons model, Anda harus meneruskannya kembali persis seperti yang diterima saat mengirim histori percakapan pada giliran berikutnya.
**Saat menggunakan model Gemini 3, Anda harus meneruskan kembali tanda tangan pemikiran selama panggilan fungsi, jika tidak, Anda akan mendapatkan error validasi** (kode status 4xx).
Hal ini mencakup saat menggunakan setelan tingkat `minimal`
[penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#thinking-levels) untuk Gemini 3
Flash.

## Cara kerjanya

Grafik di bawah memvisualisasikan arti "giliran" dan "langkah" sebagaimana terkait dengan
[panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id) di Gemini API. "Giliran" adalah satu pertukaran lengkap dalam percakapan antara pengguna dan model. "Langkah" adalah tindakan atau operasi yang lebih mendetail yang dilakukan oleh model, sering kali sebagai bagian dari proses yang lebih besar untuk menyelesaikan giliran.

![Diagram langkah dan giliran pemanggilan fungsi](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=id)

*Dokumen ini berfokus pada penanganan panggilan fungsi untuk model Gemini 3. Lihat
bagian [perilaku model](#model-behavior) untuk mengetahui perbedaan dengan 2.5.*

Gemini 3 menampilkan tanda tangan pemikiran untuk semua respons model (respons dari API) dengan panggilan fungsi. Tanda tangan pemikiran muncul dalam kasus berikut:

- Jika ada [panggilan fungsi paralel](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#parallel_function_calling), bagian panggilan fungsi pertama yang ditampilkan oleh respons model akan memiliki
  tanda tangan pemikiran.
- Jika ada panggilan fungsi berurutan (multi-langkah), setiap panggilan fungsi akan memiliki tanda tangan dan Anda harus meneruskan kembali semua tanda tangan.
- Respons model tanpa panggilan fungsi akan menampilkan tanda tangan pemikiran di dalam bagian terakhir yang ditampilkan oleh model.

Tabel berikut memberikan visualisasi untuk panggilan fungsi multi-langkah, menggabungkan definisi giliran dan langkah dengan konsep tanda tangan yang diperkenalkan di atas:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Giliran** | **Langkah** | **Permintaan Pengguna** | **Respons Model** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Tidak ada |

## Tanda tangan di bagian panggilan fungsi

Saat Gemini membuat `functionCall`, Gemini mengandalkan `thought_signature` untuk memproses output alat dengan benar pada giliran berikutnya.

- **Perilaku**:
  - **Panggilan Fungsi Tunggal**: Bagian `functionCall` akan berisi `thought_signature`.
  - **Panggilan Fungsi Paralel**: Jika model membuat panggilan fungsi paralel
    dalam respons, `thought_signature` akan dilampirkan **hanya ke bagian**
    `functionCall` pertama. Bagian `functionCall` berikutnya dalam respons yang sama **tidak** akan berisi tanda tangan.
- **Persyaratan**: Anda **harus** menampilkan tanda tangan ini di bagian yang sama persis dengan tempat tanda tangan
  diterima saat mengirim kembali histori percakapan.
- **Validasi**: Validasi ketat diterapkan untuk semua panggilan fungsi dalam
  giliran saat ini . (Hanya giliran saat ini yang diperlukan; kami tidak memvalidasi giliran sebelumnya)
  - API akan kembali ke histori (terbaru hingga terlama) untuk menemukan pesan **Pengguna** terbaru yang berisi konten standar (misalnya, `text`) ( yang akan menjadi awal giliran saat ini). Ini tidak akan **be** `functionResponse`.
  - **Semua** giliran `functionCall` model yang terjadi setelah pesan penggunaan tertentu tersebut dianggap sebagai bagian dari giliran.
  - Bagian `functionCall` **pertama** di **setiap langkah** giliran saat ini **harus** menyertakan `thought_signature`.
  - Jika Anda menghapus `thought_signature` untuk bagian `functionCall` pertama di langkah mana pun pada giliran saat ini, permintaan akan gagal dengan error 400.
- **Jika tanda tangan yang tepat tidak ditampilkan, berikut cara Anda akan mengalami error**
  - Model Gemini 3: Kegagalan menyertakan tanda tangan akan menghasilkan error 400. Kata-katanya akan berbentuk:
    - Panggilan fungsi `<Function Call>` di blok konten `<index of contents array>`
      tidak memiliki `thought_signature`. Misalnya, *Panggilan
      fungsi `FC1` di blok konten `1.` tidak memiliki `thought_signature`.*

### Contoh panggilan fungsi berurutan

Bagian ini menunjukkan contoh beberapa panggilan fungsi saat pengguna mengajukan pertanyaan kompleks yang memerlukan beberapa tugas.

Mari kita lihat contoh panggilan fungsi multi-giliran saat pengguna mengajukan
pertanyaan kompleks yang memerlukan beberapa tugas: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Giliran** | **Langkah** | **Permintaan Pengguna** | **Respons Model** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Kode berikut mengilustrasikan urutan dalam tabel di atas.

**Giliran 1, Langkah 1 (Permintaan pengguna)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "check_flight",
          "description": "Gets the current status of a flight",
          "parameters": {
            "type": "object",
            "properties": {
              "flight": {
                "type": "string",
                "description": "The flight number to check"
              }
            },
            "required": [
              "flight"
            ]
          }
        },
        {
          "name": "book_taxi",
          "description": "Book a taxi",
          "parameters": {
            "type": "object",
            "properties": {
              "time": {
                "type": "string",
                "description": "time to book the taxi"
              }
            },
            "required": [
              "time"
            ]
          }
        }
      ]
    }
  ]
}
```

**Giliran 1, Langkah 1 (Respons model)**

```
{
"content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>"
          }
        ]
  }
}
```

**Giliran 1, Langkah 2 (Respons pengguna - Mengirim output alat)** Karena giliran pengguna ini hanya berisi `functionResponse` (tidak ada teks baru), kita masih berada di Giliran 1. Kita
harus mempertahankan `<Signature_A>`.

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
                }
              }
            }
        ]
}
```

**Giliran 1, Langkah 2 (Model)** Model kini memutuskan untuk memesan taksi berdasarkan output alat sebelumnya.

```
{
      "content": {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>"
          }
        ]
      }
}
```

**Giliran 1, Langkah 3 (Pengguna - Mengirim output alat)** Untuk mengirim konfirmasi pemesanan taksi, kita harus menyertakan tanda tangan untuk **SEMUA** panggilan fungsi dalam loop ini
(`<Signature A>` + `<Signature B>`).

```
{
      "role": "user",
      "parts": [
        {
          "text": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
        }
      ]
    },
    {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "check_flight",
              "args": {
                "flight": "AA100"
              }
            },
            "thoughtSignature": "<Signature A>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "check_flight",
              "response": {
                "status": "delayed",
                "departure_time": "12 PM"
              }
              }
            }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "functionCall": {
              "name": "book_taxi",
              "args": {
                "time": "10 AM"
              }
            },
            "thoughtSignature": "<Signature B>" //Required and Validated
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "functionResponse": {
              "name": "book_taxi",
              "response": {
                "booking_status": "success"
              }
              }
            }
        ]
    }
}
```

### Contoh panggilan fungsi paralel

Mari kita lihat contoh panggilan fungsi paralel saat pengguna bertanya
`"Check weather in Paris and London"` untuk melihat tempat model melakukan validasi.

| **Giliran** | **Langkah** | **Permintaan Pengguna** | **Respons Model** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (no FCs) | Tidak ada |

Kode berikut mengilustrasikan urutan dalam tabel di atas.

**Giliran 1, Langkah 1 (Permintaan pengguna)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**Giliran 1, Langkah 1 (Respons model)**

```
{
  "content": {
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "Paris"
          }
        },
        "thoughtSignature": "<Signature_A>"// INCLUDED on First FC
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "location": "London"
          }// NO signature on subsequent parallel FCs
        }
      }
    ]
  }
}
```

**Giliran 1, Langkah 2 (Respons pengguna - Mengirim output alat)** Kita harus mempertahankan
`<Signature_A>` di bagian pertama persis seperti yang diterima.

```
[
  {
    "role": "user",
    "parts": [
      {
        "text": "Check the weather in Paris and London."
      }
    ]
  },
  {
    "role": "model",
    "parts": [
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "Paris"
          }
        },
        "thought_signature": "<Signature_A>" // MUST BE INCLUDED
      },
      {
        "functionCall": {
          "name": "get_current_temperature",
          "args": {
            "city": "London"
          }
        }
      } // NO SIGNATURE FIELD
    ]
  },
  {
    "role": "user",
    "parts": [
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "15C"
          }
        }
      },
      {
        "functionResponse": {
          "name": "get_current_temperature",
          "response": {
            "temp": "12C"
          }
        }
      }
    ]
  }
]
```

## Tanda tangan di bagian non `functionCall`

Gemini juga dapat menampilkan `thought_signatures` di bagian akhir respons di bagian non-panggilan fungsi.

- **Perilaku**: Bagian konten akhir (`text, inlineData…`) yang ditampilkan oleh
  model dapat berisi `thought_signature`.
- **Rekomendasi**: Menampilkan tanda tangan ini **direkomendasikan** untuk memastikan
  model mempertahankan penalaran berkualitas tinggi, terutama untuk mengikuti instruksi
  yang kompleks atau alur kerja agen yang disimulasikan.
- **Validasi**: API **tidak** menerapkan validasi secara ketat. Anda tidak akan menerima error pemblokiran jika menghapusnya, meskipun performa dapat menurun.

### Penalaran teks/dalam konteks (Tidak ada validasi)

**Giliran 1, Langkah 1 (Respons model)**

```
{
  "role": "model",
  "parts": [
    {
      "text": "I need to calculate the risk. Let me think step-by-step...",
      "thought_signature": "<Signature_C>" // OPTIONAL (Recommended)
    }
  ]
}
```

**Giliran 2, Langkah 1 (Pengguna)**

```
[
  { "role": "user", "parts": [{ "text": "What is the risk?" }] },
  {
    "role": "model", 
    "parts": [
      {
        "text": "I need to calculate the risk. Let me think step-by-step...",
        // If you omit <Signature_C> here, no error will occur.
      }
    ]
  },
  { "role": "user", "parts": [{ "text": "Summarize it." }] }
]
```

## Tanda tangan untuk kompatibilitas OpenAI

Contoh berikut menunjukkan cara menangani tanda tangan pemikiran untuk API penyelesaian chat
menggunakan [kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id).

### Contoh panggilan fungsi berurutan

Ini adalah contoh beberapa panggilan fungsi saat pengguna mengajukan pertanyaan kompleks yang memerlukan beberapa tugas.

Mari kita lihat contoh panggilan fungsi multi-giliran saat pengguna bertanya `Check flight status for AA100 and book a taxi if delayed` dan Anda dapat melihat apa yang terjadi saat pengguna mengajukan pertanyaan kompleks yang memerlukan beberapa tugas.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Giliran** | **Langkah** | **Permintaan Pengguna** | **Respons Model** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Kode berikut menjelaskan urutan yang diberikan.

**Giliran 1, Langkah 1 (Permintaan Pengguna)**

```
{
  "model": "google/gemini-3.1-pro-preview",
  "messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "check_flight",
        "description": "Gets the current status of a flight",
        "parameters": {
          "type": "object",
          "properties": {
            "flight": {
              "type": "string",
              "description": "The flight number to check."
            }
          },
          "required": [
            "flight"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "book_taxi",
        "description": "Book a taxi",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "time to book the taxi"
            }
          },
          "required": [
            "time"
          ]
        }
      }
    }
  ]
}
```

**Giliran 1, Langkah 1 (Respons Model)**

```
{
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>"
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    }
```

**Giliran 1, Langkah 2 (Respons Pengguna - Mengirim Output Alat)**

Karena giliran pengguna ini hanya berisi `functionResponse` (tidak ada teks baru), kita masih berada di Giliran 1 dan harus mempertahankan `<Signature_A>`.

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    }
  ]
```

**Giliran 1, Langkah 2 (Model)**

Model kini memutuskan untuk memesan taksi berdasarkan output alat sebelumnya.

```
{
"role": "model",
"tool_calls": [
{
"extra_content": {
"google": {
"thought_signature": "<Signature B>"
}
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-2",
            "type": "function"
          }
       ]
}
```

**Giliran 1, Langkah 3 (Pengguna - Mengirim Output Alat)**

Untuk mengirim konfirmasi pemesanan taksi, kita harus menyertakan tanda tangan untuk SEMUA
panggilan fungsi dalam loop ini (`<Signature A>` + `<Signature B>`).

```
"messages": [
    {
      "role": "user",
      "content": "Check flight status for AA100 and book a taxi 2 hours before if delayed."
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"flight\":\"AA100\"}",
              "name": "check_flight"
            },
            "id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "check_flight",
      "tool_call_id": "function-call-1d6a1a61-6f4f-4029-80ce-61586bd86da5",
      "content": "{\"status\":\"delayed\",\"departure_time\":\"12 PM\"}"                 
    },
    {
      "role": "model",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature B>" //Required and Validated
              }
            },
            "function": {
              "arguments": "{\"time\":\"10 AM\"}",
              "name": "book_taxi"
            },
            "id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
            "type": "function"
          }
        ]
    },
    {
      "role": "tool",
      "name": "book_taxi",
      "tool_call_id": "function-call-65b325ba-9b40-4003-9535-8c7137b35634",
      "content": "{\"booking_status\":\"success\"}"
    }
  ]
```

### Contoh panggilan fungsi paralel

Mari kita lihat contoh panggilan fungsi paralel saat pengguna bertanya
`"Check weather in Paris and London"` dan Anda dapat melihat tempat model melakukan
validasi.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Giliran** | **Langkah** | **Permintaan Pengguna** | **Respons Model** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Berikut kode untuk menjelaskan urutan yang diberikan.

**Giliran 1, Langkah 1 (Permintaan Pengguna)**

```
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "Check the weather in Paris and London."
        }
      ]
    }
  ],
  "tools": [
    {
      "functionDeclarations": [
        {
          "name": "get_current_temperature",
          "description": "Gets the current temperature for a given location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco"
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ]
    }
  ]
}
```

**Giliran 1, Langkah 1 (Respons Model)**

```
{
"role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Signature returned
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": {
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function" // No signature on Parallel FC
          }
        ]
}
```

**Giliran 1, Langkah 2 (Respons Pengguna - Mengirim Output Alat)**

Anda harus mempertahankan `<Signature_A>` di bagian pertama persis seperti yang diterima.

```
"messages": [
    {
      "role": "user",
      "content": "Check the weather in Paris and London."
    },
    {
      "role": "assistant",
        "tool_calls": [
          {
            "extra_content": {
              "google": {
                "thought_signature": "<Signature A>" //Required
              }
            },
            "function": {
              "arguments": "{\"location\":\"Paris\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
            "type": "function"
          },
          {
            "function": { //No Signature
              "arguments": "{\"location\":\"London\"}",
              "name": "get_current_temperature"
            },
            "id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
            "type": "function"
          }
        ]
    },
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-f3b9ecb3-d55f-4076-98c8-b13e9d1c0e01",
      "content": "{\"temp\":\"15C\"}"
    },    
    {
      "role":"tool",
      "name": "get_current_temperature",
      "tool_call_id": "function-call-335673ad-913e-42d1-bbf5-387c8ab80f44",
      "content": "{\"temp\":\"12C\"}"
    }
  ]
```

## FAQ

1. **Bagaimana cara mentransfer histori dari model lain ke Gemini 3 dengan bagian panggilan fungsi di giliran dan langkah saat ini? Saya perlu menyediakan bagian panggilan fungsi
   yang tidak dibuat oleh API dan oleh karena itu tidak memiliki tanda tangan pemikiran terkait
   ?**

   Meskipun sangat tidak disarankan untuk menyisipkan blok panggilan fungsi kustom ke dalam permintaan, dalam kasus yang tidak dapat dihindari, misalnya memberikan informasi
   kepada model tentang panggilan fungsi dan respons yang dieksekusi
   secara deterministik oleh klien, atau mentransfer pelacakan dari model lain yang tidak menyertakan tanda tangan pemikiran, Anda dapat menetapkan tanda tangan dummy berikut `"context_engineering_is_the_way_to_go"` atau
   `"skip_thought_signature_validator"` di kolom tanda tangan pemikiran untuk melewati
   validasi.
2. **Saya mengirim kembali panggilan dan respons fungsi paralel yang disisipkan dan API menampilkan 400. Mengapa?**

   Saat API menampilkan panggilan fungsi paralel "FC1 + signature, FC2", respons pengguna yang diharapkan adalah "FC1+ signature, FC2, FR1, FR2". Jika Anda menyisipkannya sebagai "FC1 + signature, FR1, FC2, FR2", API akan menampilkan error 400.
3. **Saat melakukan streaming dan model tidak menampilkan panggilan fungsi, saya tidak dapat menemukan
   tanda tangan pemikiran**

   Selama respons model yang tidak berisi FC dengan permintaan streaming, model dapat menampilkan tanda tangan pemikiran di bagian dengan bagian konten teks kosong. Sebaiknya analisis seluruh permintaan hingga `finish_reason` ditampilkan oleh model.

## Tanda tangan pemikiran untuk model yang berbeda

[Model Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=id#gemini-3) dan model Gemini 2.5
berperilaku berbeda dengan tanda tangan pemikiran dalam panggilan fungsi:

- Jika ada panggilan fungsi dalam respons,
  - Gemini 3 akan selalu memiliki tanda tangan di bagian panggilan fungsi pertama.
    **Wajib** untuk menampilkan bagian tersebut.
  - Gemini 2.5 akan memiliki tanda tangan di bagian pertama (terlepas dari jenisnya). **Opsional** untuk menampilkan bagian tersebut.
- Jika tidak ada panggilan fungsi dalam respons,
  - Gemini 3 akan memiliki tanda tangan di bagian terakhir jika model membuat pemikiran.
  - Gemini 2.5 tidak akan memiliki tanda tangan di bagian mana pun.

Lihat halaman [Penalaran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#signatures) untuk mengetahui detail perbandingan selengkapnya.
Untuk model Gambar Gemini 3, lihat bagian proses penalaran di
[panduan Pembuatan gambar](https://ai.google.dev/gemini-api/docs/image-generation?hl=id#thinking-process).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-08-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-08-19 UTC."],[],[]]
