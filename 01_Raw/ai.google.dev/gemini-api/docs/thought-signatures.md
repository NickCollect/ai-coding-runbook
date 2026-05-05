---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr
fetched_at: 2026-05-05T13:14:11.965264+00:00
title: "D\u00fc\u015f\u00fcnce \u0130mzalar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

- [Ana Sayfa](https://ai.google.dev/gemini-api/docs/Ana Sayfa)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/Dokümanlar)

Geri bildirim gönderin

# Düşünce İmzaları

Düşünce imzaları, modelin dahili düşünce sürecinin şifrelenmiş temsilleridir ve çok adımlı etkileşimlerde akıl yürütme bağlamını korumak için kullanılır.
Düşünme modelleri (ör.Gemini 3 ve 2.5 serisi) kullanılırken API, yanıtın [content parts](https://ai.google.dev/gemini-api/docs/content parts) (içerik bölümleri) içinde bir `thoughtSignature` alanı döndürebilir (ör. `text` veya `functionCall` bölümleri).

Genel bir kural olarak, model yanıtında düşünce imzası alırsanız konuşma geçmişini bir sonraki turda gönderirken bu imzayı olduğu gibi geri iletmeniz gerekir.
**Gemini 3 modellerini kullanırken işlev çağrısı sırasında düşünce imzalarını geri iletmeniz gerekir. Aksi takdirde doğrulama hatası alırsınız** (4xx durum kodu).
Bu, Gemini 3 Flash için `minimal`
[düşünme düzeyi](https://ai.google.dev/gemini-api/docs/düşünme düzeyi) ayarı kullanılırken de geçerlidir.

## İşleyiş şekli

Aşağıdaki grafik, Gemini API'deki [işlev çağrısı](https://ai.google.dev/gemini-api/docs/işlev çağrısı) ile ilgili olarak "dönüş" ve "adım"ın anlamını görselleştirir. "Dönüş", kullanıcı ile model arasındaki sohbetteki tek ve eksiksiz bir etkileşimdir. "Adım", model tarafından gerçekleştirilen daha ayrıntılı bir işlem veya operasyondur. Genellikle bir dönüşü tamamlamak için daha büyük bir sürecin parçası olarak gerçekleştirilir.

![İşlev çağırma dönüşleri ve adımları diyagramı](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=tr)

*Bu belgede, Gemini 3 modellerinde işlev çağrılarının işlenmesi ele alınmaktadır. 2.5 ile ilgili tutarsızlıklar için [model davranışı](https://ai.google.dev/gemini-api/docs/model davranışı) bölümüne bakın.*

Gemini 3, işlev çağrısı içeren tüm model yanıtları (API'den gelen yanıtlar) için düşünce imzaları döndürür. Düşünce imzaları aşağıdaki durumlarda gösterilir:

- [Paralel işlev](https://ai.google.dev/gemini-api/docs/Paralel işlev) çağrıları olduğunda, model yanıtı tarafından döndürülen ilk işlev çağrısı bölümünde bir düşünce imzası bulunur.
- Sıralı işlev çağrıları (çok adımlı) olduğunda her işlev çağrısının bir imzası olur ve tüm imzaları geri iletmeniz gerekir.
- İşlev çağrısı içermeyen model yanıtları, modelin döndürdüğü son kısımda düşünce imzası döndürür.

Aşağıdaki tabloda, yukarıda bahsedilen imzalar kavramıyla birlikte dönüş ve adım tanımlarını birleştiren çok adımlı işlev çağrıları için bir görselleştirme sunulmaktadır:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Dönüş** | **Step** | **Kullanıcı İsteği** | **Model Yanıtı** (Model Response) | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Yok |

## İşlev çağrısı bölümlerindeki imzalar

Gemini, `functionCall` oluştururken aracın çıktısını bir sonraki adımda doğru şekilde işlemek için `thought_signature` kullanır.

- **Davranış**:
  - **Tek İşlev Çağrısı**: `functionCall` bölümü `thought_signature` içerecek.
  - **Paralel İşlev Çağrıları**: Model, yanıtta paralel işlev çağrıları oluşturursa `thought_signature` **yalnızca ilk**
    `functionCall` bölüme eklenir. Aynı yanıttaki sonraki `functionCall` bölümleri imza **içermez**.
- **Şart: Görüşme geçmişini geri gönderirken bu imzayı, alındığı **tam** kısımda iade etmeniz gerekir**.
- **Doğrulama**: Geçerli dönüşteki tüm işlev çağrıları için katı doğrulama uygulanır . (Yalnızca mevcut dönüş gereklidir; önceki dönüşler doğrulanmaz)
  - API, standart içerik (ör. `text`) içeren en son **Kullanıcı** mesajını (mevcut dönüşün başlangıcı) bulmak için geçmişte geriye doğru (en yeni mesajdan en eski mesaja) gider. Bu işlem **be** `functionResponse` olarak değerlendirilmez.
  - Bu belirli kullanım mesajından sonraki **tüm** model `functionCall` dönüşleri, dönüşün bir parçası olarak kabul edilir.
  - **Mevcut dönüşteki **her adımda** yer alan **ilk** `functionCall` bölümü, `thought_signature` içermelidir.**
  - Mevcut dönüşün herhangi bir adımında ilk `functionCall` bölümü için `thought_signature` karakterini atlarsanız istek 400 hatasıyla başarısız olur.
- **Uygun imzalar döndürülmezse nasıl hata alacağınız aşağıda açıklanmıştır**
  - Gemini 3 modelleri: İmzaların eklenmemesi 400 hatasına neden olur. Metin şu biçimde olacaktır:
    - `<index of contents array>` içerik bloğundaki `<Function Call>` işlev çağrısında `thought_signature` eksik. Örneğin, *Function
      call `FC1` in the `1.` content block is missing a `thought_signature`.* ("`1.` içerik bloğundaki Function
      call `FC1` işlevinde `thought_signature` eksik.")

### Sıralı işlev çağrısı örneği

Bu bölümde, kullanıcının birden fazla görev gerektiren karmaşık bir soru sorduğu birden fazla işlev çağrısı örneği gösterilmektedir.

Kullanıcının birden fazla görev gerektiren karmaşık bir soru sorduğu çok turlu bir işlev çağrısı örneğini inceleyelim: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Dönüş** | **Step** | **Kullanıcı İsteği** | **Model Yanıtı** (Model Response) | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Aşağıdaki kod, yukarıdaki tablodaki sırayı gösterir.

**1. tur, 1. adım (Kullanıcı isteği)**

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

**1. Tur, 1. Adım (Model yanıt)**

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

**1. tur, 2. adım (Kullanıcı yanıtı - Araç çıktılarını gönderme)** Bu kullanıcı turu yalnızca `functionResponse` içerdiğinden (yeni metin yok) 1. turdayız. `<Signature_A>` korunmalıdır.

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

**1. Tur, 2. Adım (Model)** Model, önceki araç çıktısına göre taksi rezervasyonu yapmaya karar veriyor.

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

**1. tur, 3. adım (Kullanıcı - Araç çıktısı gönderme)** Taksi rezervasyonu onayını göndermek için bu döngüdeki **TÜM** işlev çağrılarına imza eklememiz gerekir (`<Signature A>` + `<Signature B>`).

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

### Paralel işlev çağrısı örneği

Kullanıcının modele doğrulama yaptığı yeri görmeyi istediği paralel işlev çağrısı örneğini inceleyelim.`"Check weather in Paris and London"`

| **Dönüş** | **Step** | **Kullanıcı İsteği** | **Model Yanıtı** (Model Response) | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | request1="Paris ve Londra'daki hava durumunu kontrol et" | FC1 ("Paris") + imza  FC2 ("London") | FR1 |
| 1 | 2 | istek 2 **=** istek1 **+** FC1 ("Paris") + imza + FC2 ("London") | text\_output  (FC yok) | Yok |

Aşağıdaki kod, yukarıdaki tablodaki sırayı gösterir.

**1. tur, 1. adım (Kullanıcı isteği)**

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

**1. Tur, 1. Adım (Model yanıtı)**

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

**1. Tur, 2. Adım (Kullanıcı yanıtı - Araç çıktılarını gönderme)** İlk bölümdeki
`<Signature_A>`, alındığı gibi korunmalıdır.

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

## `functionCall` dışındaki bölümlerdeki imzalar

Gemini, işlev çağrısı içermeyen bölümlerde yanıtın son kısmında `thought_signatures` da döndürebilir.

- **Davranış**: Model tarafından döndürülen son içerik bölümü (`text, inlineData…`) `thought_signature` içerebilir.
- **Öneri**: Bu imzaların döndürülmesi, modelin özellikle karmaşık talimatları takip etme veya simüle edilmiş aracı iş akışları için yüksek kaliteli muhakeme yeteneğini korumasını sağlamak açısından **önerilir**.
- **Doğrulama**: API, doğrulamayı katı bir şekilde **zorunlu kılmaz**. Bunları atladığınızda engelleyici bir hata almazsınız ancak performans düşebilir.

### Metin/Bağlam içi akıl yürütme (Doğrulama yok)

**1. Tur, 1. Adım (Model yanıtı)**

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

**2. Tur, 1. Adım (Kullanıcı)**

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

## OpenAI uyumluluğu için imzalar

Aşağıdaki örneklerde, [OpenAI uyumluluğu](https://ai.google.dev/gemini-api/docs/OpenAI uyumluluğu) kullanılarak sohbet tamamlama API'si için düşünce imzalarının nasıl işleneceği gösterilmektedir.

### Sıralı işlev çağrısı örneği

Bu, kullanıcının birden fazla görev gerektiren karmaşık bir soru sorduğu çoklu işlev çağrısı örneğidir.

Kullanıcının `Check flight status for AA100 and book a taxi if delayed` diye sorduğu çok turlu bir işlev çağrısı örneğini inceleyelim. Kullanıcı, birden fazla görev gerektiren karmaşık bir soru sorduğunda ne olduğunu görebilirsiniz.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Dönüş** | **Step** | **Kullanıcı İsteği** | **Model Yanıtı** (Model Response) | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Aşağıdaki kod, verilen sırayı adım adım açıklar.

**1. Tur, 1. Adım (Kullanıcı İsteği)**

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

**1. Tur, 1. Adım (Model Yanıt)**

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

**1. Tur, 2. Adım (Kullanıcı Yanıtı - Araç Çıkışlarını Gönderme)**

Bu kullanıcı dönüşü yalnızca `functionResponse` içerdiğinden (yeni metin yok) hâlâ 1. dönüşteyiz ve `<Signature_A>` korunmalıdır.

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

**1. Tur, 2. Adım (Model)**

Model, önceki araç çıkışına göre taksi rezervasyonu yapmaya karar veriyor.

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

**1. Tur, 3. Adım (Kullanıcı - Araç Çıktısı Gönderme)**

Taksi rezervasyonu onayını göndermek için bu döngüdeki TÜM işlev çağrıları (`<Signature A>` + `<Signature B>`) için imzalar eklememiz gerekir.

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

### Paralel işlev çağrısı örneği

Kullanıcının `"Check weather in Paris and London"` diye sorduğu paralel işlev çağırma örneğini inceleyelim. Bu örnekte, modelin nerede doğrulama yaptığını görebilirsiniz.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Dönüş** | **Step** | **Kullanıcı İsteği** | **Model Yanıtı** (Model Response) | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Belirtilen sırayı izlemek için gereken kod aşağıda verilmiştir.

**1. Tur, 1. Adım (Kullanıcı İsteği)**

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

**1. Tur, 1. Adım (Model Yanıt)**

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

**1. Tur, 2. Adım (Kullanıcı Yanıtı - Araç Çıkışlarını Gönderme)**

İlk bölümdeki `<Signature_A>` işaretini tam olarak aldığınız şekilde korumalısınız.

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

## SSS

1. **Geçerli dönüş ve adımda işlev çağrısı bölümü olan farklı bir modeldeki geçmişi Gemini 3'e nasıl aktarabilirim? API tarafından oluşturulmayan ve bu nedenle ilişkili bir düşünce imzası olmayan işlev çağrısı bölümleri sağlamam gerekiyor mu?**

   İsteğe özel işlev çağrısı bloklarının isteğe eklenmesi kesinlikle önerilmez.Ancak bu durumun kaçınılmaz olduğu durumlarda (ör. istemci tarafından deterministik olarak yürütülen işlev çağrıları ve yanıtları hakkında modele bilgi sağlama veya düşünce imzaları içermeyen farklı bir modelden izleme aktarma) doğrulamanın atlanması için düşünce imzası alanında `"context_engineering_is_the_way_to_go"` veya `"skip_thought_signature_validator"` değerlerinden birinin aşağıdaki sahte imzalarını ayarlayabilirsiniz.
2. **İç içe geçmiş paralel işlev çağrıları ve yanıtları geri gönderiyorum ve API 400 döndürüyor. Neden?**

   API, paralel işlev çağrıları "FC1 + imza, FC2" döndürdüğünde, beklenen kullanıcı yanıtı "FC1+ imza, FC2, FR1, FR2" olur. Bunları "FC1 + imza, FR1, FC2, FR2" şeklinde iç içe yerleştirirseniz API 400 hatası döndürür.
3. **Yayın sırasında model, bulamadığım bir işlev çağrısı döndürmediğinde düşünce imzasını bulamıyorum**

   Akış isteğiyle birlikte FC içermeyen bir model yanıtı sırasında model, düşünce imzasını boş metin içerikli bir bölümde döndürebilir. Model tarafından `finish_reason` döndürülene kadar isteğin tamamını ayrıştırmanız önerilir.

## Farklı modeller için düşünce imzaları

[Gemini 3 modelleri](https://ai.google.dev/gemini-api/docs/Gemini 3 modelleri) ve Gemini 2.5 modelleri
işlev çağrılarında düşünce imzalarıyla farklı şekilde davranır:

- Yanıtta işlev çağrıları varsa,
  - Gemini 3, her zaman ilk işlev çağrısı bölümünde imzaya sahip olur.
    Bu parçanın iade edilmesi **zorunludur**.
  - Gemini 2.5, ilk bölümde imzayı içerir (türden bağımsız olarak). Bu parçayı iade etmek **isteğe bağlıdır**.
- Yanıt içinde işlev çağrısı yoksa,
  - Model bir düşünce ürettiğinde Gemini 3, son kısımda imzayı gösterir.
  - Gemini 2.5'in hiçbir bölümünde imza bulunmaz.

Daha fazla karşılaştırma bilgisi için [Düşünme](https://ai.google.dev/gemini-api/docs/Düşünme) sayfasına bakın.
Gemini 3 Image modelleri için [Görüntü oluşturma](https://ai.google.dev/gemini-api/docs/Görüntü oluşturma) kılavuzunun düşünme süreci bölümüne bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://ai.google.dev/gemini-api/docs/Creative Commons Atıf 4.0 Lisansı) altında ve kod örnekleri [Apache 2.0 Lisansı](https://ai.google.dev/gemini-api/docs/Apache 2.0 Lisansı) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://ai.google.dev/gemini-api/docs/Google Developers Site Politikaları)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?
