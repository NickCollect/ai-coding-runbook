---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=pl
fetched_at: 2026-09-28T06:33:50.547815+00:00
title: "podpisy w\u00a0my\u015blach \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs/generate-content?hl=pl)

Prześlij opinię

# podpisy w myślach

Podpisy myśli to zaszyfrowane reprezentacje wewnętrznego procesu myślowego modelu. Służą one do zachowania kontekstu rozumowania w interakcjach wieloetapowych.
Gdy używasz modeli myślących (takich jak Gemini 3 i 2.5), interfejs API może
zwracać pole `thoughtSignature` w [częściach odpowiedzi dotyczących treści](https://ai.google.dev/api/caching?hl=pl#Part) (np. `text` lub `functionCall`).

Ogólnie rzecz biorąc, jeśli otrzymasz podpis myśli w odpowiedzi modelu, w następnym etapie musisz go przekazać dokładnie tak, jak został otrzymany, podczas wysyłania historii rozmowy.
**Gdy używasz modeli Gemini 3, musisz przekazywać podpisy myśli podczas wywoływania funkcji. W przeciwnym razie otrzymasz błąd weryfikacji** (kod stanu 4xx).
Dotyczy to również sytuacji, gdy używasz ustawienia `minimal`
[poziomu myślenia](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#thinking-levels) w przypadku Gemini 3
Flash.

## Jak to działa

Poniższy diagram ilustruje znaczenie słów „etap” i „krok” w kontekście
[wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) w interfejsie Gemini API. „Etap” to pojedyncza, pełna wymiana informacji w rozmowie między użytkownikiem a modelem. „Krok” to bardziej szczegółowe działanie lub operacja wykonywana przez model, często w ramach większego procesu mającego na celu ukończenie etapu.

![Diagram przedstawiający tury i kroki wywoływania funkcji](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=pl)

*Ten dokument koncentruje się na obsłudze wywoływania funkcji w przypadku modeli Gemini 3. Więcej informacji o różnicach w przypadku modelu 2.5 znajdziesz w sekcji [Zachowanie modelu](#model-behavior).*

Gemini 3 zwraca podpisy myśli we wszystkich odpowiedziach modelu (odpowiedziach z interfejsu API) z wywołaniem funkcji. Podpisy myśli pojawiają się w tych przypadkach:

- Gdy występują [równoległe wywołania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#parallel_function_calling), pierwsza część wywołania funkcji zwrócona przez odpowiedź modelu będzie zawierać
  podpis myśli.
- Gdy występują sekwencyjne wywołania funkcji (wieloetapowe), każde wywołanie funkcji będzie miało podpis i musisz przekazać wszystkie podpisy.
- Odpowiedzi modelu bez wywołania funkcji będą zawierać podpis myśli w ostatniej części zwróconej przez model.

W tabeli poniżej przedstawiono wizualizację wieloetapowych wywołań funkcji, łącząc definicje etapów i kroków z koncepcją podpisów wprowadzoną powyżej:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Etap** | **Krok** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Brak |

## Podpisy w częściach wywoływania funkcji

Gdy Gemini generuje `functionCall`, korzysta z `thought_signature`, aby prawidłowo przetworzyć dane wyjściowe narzędzia w następnym etapie.

- **Zachowanie**:
  - **Pojedyncze wywołanie funkcji**: część `functionCall` będzie zawierać `thought_signature`.
  - **Równoległe wywołania funkcji**: jeśli model wygeneruje równoległe wywołania funkcji
    w odpowiedzi, `thought_signature` zostanie dołączony **tylko do pierwszej**
    `functionCall` części. Kolejne części `functionCall` w tej samej odpowiedzi **nie** będą zawierać podpisu.
- **Wymaganie**: podczas wysyłania historii rozmowy **musisz** zwrócić ten podpis w dokładnie tej części, w której został otrzymany.
- **Weryfikacja**: w przypadku wszystkich wywołań funkcji w ramach
  bieżącego etapu obowiązuje ścisła weryfikacja . (Wymagany jest tylko bieżący etap. Nie weryfikujemy poprzednich etapów).
  - Interfejs API cofa się w historii (od najnowszej do najstarszej), aby znaleźć najnowszą wiadomość **użytkownika** zawierającą standardową treść (np. `text`) ( która będzie początkiem bieżącego etapu). Nie **be** to `functionResponse`.
  - **Wszystkie** etapy `functionCall` modelu występujące po tej konkretnej wiadomości użytkownika są uważane za część etapu.
  - **Pierwsza** część `functionCall` w **każdym kroku** bieżącego etapu **musi** zawierać swój `thought_signature`.
  - Jeśli pominiesz `thought_signature` w pierwszej części `functionCall` w dowolnym kroku bieżącego etapu, żądanie zakończy się niepowodzeniem z błędem 400.
- **Jeśli nie zostaną zwrócone prawidłowe podpisy, wystąpi błąd:**
  - Modele Gemini 3: brak podpisów spowoduje błąd 400. Komunikat będzie miał postać:
    - Wywołanie funkcji `<Function Call>` w bloku treści `<index of contents array>`
      nie zawiera `thought_signature`. Na przykład *Wywołanie
      funkcji `FC1` w bloku treści `1.` nie zawiera `thought_signature`.*

### Przykład sekwencyjnego wywoływania funkcji

W tej sekcji znajdziesz przykład wielu wywołań funkcji, w których użytkownik zadaje złożone pytanie wymagające wykonania kilku zadań.

Przyjrzyjmy się przykładowi wywoływania funkcji w wielu etapach, w którym użytkownik zadaje
złożone pytanie wymagające wykonania kilku zadań: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Etap** | **Krok** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Poniższy kod ilustruje sekwencję w tabeli powyżej.

**Etap 1, krok 1 (prośba użytkownika)**

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

**Etap 1, krok 1 (odpowiedź modelu)**

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

**Etap 1, krok 2 (odpowiedź użytkownika – wysyłanie danych wyjściowych narzędzia)** Ponieważ ten etap użytkownika zawiera tylko `functionResponse` (bez nowego tekstu), nadal jesteśmy w etapie 1. Musimy
zachować `<Signature_A>`.

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

**Etap 1, krok 2 (model)** Model decyduje teraz o zamówieniu taksówki na podstawie poprzednich danych wyjściowych narzędzia.

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

**Etap 1, krok 3 (użytkownik – wysyłanie danych wyjściowych narzędzia)** Aby wysłać potwierdzenie
rezerwacji taksówki, musimy uwzględnić podpisy **wszystkich** wywołań funkcji w tej pętli
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

### Przykład równoległego wywoływania funkcji

Przyjrzyjmy się przykładowi równoległego wywoływania funkcji, w którym użytkownik pyta
`"Check weather in Paris and London"` aby zobaczyć, gdzie model przeprowadza weryfikację.

| **Etap** | **Krok** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paryż") + podpis  FC2 ("Londyn") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (brak FC) | Brak |

Poniższy kod ilustruje sekwencję w tabeli powyżej.

**Etap 1, krok 1 (prośba użytkownika)**

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

**Etap 1, krok 1 (odpowiedź modelu)**

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

**Etap 1, krok 2 (odpowiedź użytkownika – wysyłanie danych wyjściowych narzędzia)** Musimy zachować
`<Signature_A>` w pierwszej części dokładnie tak, jak została otrzymana.

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

## Podpisy w częściach innych niż `functionCall`

Gemini może też zwracać `thought_signatures` w ostatniej części odpowiedzi w częściach innych niż wywołanie funkcji.

- **Zachowanie**: ostatnia część treści (`text, inlineData…`) zwrócona przez
  model może zawierać `thought_signature`.
- **Zalecenie**: zwracanie tych podpisów jest **zalecane** , aby zapewnić
  wysoką jakość rozumowania modelu, zwłaszcza w przypadku złożonych instrukcji
  lub symulowanych przepływów pracy agenta.
- **Weryfikacja**: interfejs API **nie** wymusza ścisłej weryfikacji. Jeśli je pominiesz, nie otrzymasz błędu blokującego, ale wydajność może się pogorszyć.

### Tekst/rozumowanie w kontekście (bez weryfikacji)

**Etap 1, krok 1 (odpowiedź modelu)**

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

**Etap 2, krok 1 (użytkownik)**

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

## Podpisy dotyczące zgodności z OpenAI

W przykładach poniżej pokazujemy, jak obsługiwać podpisy myśli w interfejsie Chat
Completion API przy użyciu [zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

### Przykład sekwencyjnego wywoływania funkcji

To jest przykład wielu wywołań funkcji, w których użytkownik zadaje złożone pytanie wymagające wykonania kilku zadań.

Przyjrzyjmy się przykładowi wywoływania funkcji w wielu etapach, w którym użytkownik pyta
`Check flight status for AA100 and book a taxi if delayed` i zobaczysz, co
się stanie, gdy użytkownik zada złożone pytanie wymagające wykonania kilku zadań.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Etap** | **Krok** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Poniższy kod ilustruje podaną sekwencję.

**Etap 1, krok 1 (prośba użytkownika)**

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

**Etap 1, krok 1 (odpowiedź modelu)**

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

**Etap 1, krok 2 (odpowiedź użytkownika – wysyłanie danych wyjściowych narzędzia)**

Ponieważ ten etap użytkownika zawiera tylko `functionResponse` (bez nowego tekstu), nadal jesteśmy
w etapie 1 i musimy zachować `<Signature_A>`.

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

**Etap 1, krok 2 (model)**

Model decyduje teraz o zamówieniu taksówki na podstawie poprzednich danych wyjściowych narzędzia.

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

**Etap 1, krok 3 (użytkownik – wysyłanie danych wyjściowych narzędzia)**

Aby wysłać potwierdzenie rezerwacji taksówki, musimy uwzględnić podpisy wszystkich
wywołań funkcji w tej pętli (`<Signature A>` + `<Signature B>`).

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

### Przykład równoległego wywoływania funkcji

Przyjrzyjmy się przykładowi równoległego wywoływania funkcji, w którym użytkownik pyta
`"Check weather in Paris and London"`, aby zobaczyć, gdzie model przeprowadza
weryfikację.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Etap** | **Krok** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Oto kod, który ilustruje podaną sekwencję.

**Etap 1, krok 1 (prośba użytkownika)**

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

**Etap 1, krok 1 (odpowiedź modelu)**

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

**Etap 1, krok 2 (odpowiedź użytkownika – wysyłanie danych wyjściowych narzędzia)**

Musisz zachować `<Signature_A>` w pierwszej części dokładnie tak, jak została otrzymana.

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

## Najczęstsze pytania

1. **Jak przenieść historię z innego modelu do Gemini 3 z częścią wywołania funkcji w bieżącym etapie i kroku? Muszę podać części wywołania funkcji
   , które nie zostały wygenerowane przez interfejs API, a więc nie mają powiązanego
   podpisu myśli?**

   Wstrzykiwanie niestandardowych bloków wywołań funkcji do żądania jest zdecydowanie
   odradzane.W przypadkach, gdy nie można tego uniknąć, np. gdy trzeba przekazać informacje
   modelowi o wywołaniach funkcji i odpowiedziach, które zostały wykonane
   deterministycznie przez klienta, lub gdy trzeba przenieść ślad z innego
   modelu, który nie zawiera podpisów myśli, możesz ustawić w polu podpisu myśli te
   podpisy zastępcze: `"context_engineering_is_the_way_to_go"` lub
   `"skip_thought_signature_validator"`, aby pominąć
   weryfikację.
2. **Wysyłam przeplatane równoległe wywołania funkcji i odpowiedzi, a interfejs API zwraca błąd 400. Dlaczego?**

   Gdy interfejs API zwraca równoległe wywołania funkcji „FC1 + podpis, FC2”, oczekiwana odpowiedź użytkownika to „FC1 + podpis, FC2, FR1, FR2”. Jeśli przeplatasz je jako „FC1 + podpis, FR1, FC2, FR2”, interfejs API zwróci błąd 400.
3. **Podczas przesyłania strumieniowego model nie zwraca wywołania funkcji. Nie mogę znaleźć
   podpisu myśli**

   Podczas odpowiedzi modelu, która nie zawiera FC z żądaniem przesyłania strumieniowego, model może zwrócić podpis myśli w części z pustą częścią treści tekstowej. Zalecamy analizowanie całego żądania, dopóki model nie zwróci `finish_reason`.

## Podpisy myśli w przypadku różnych modeli

[Modele Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-3) i modele Gemini 2.5
różnie zachowują się w przypadku podpisów myśli w wywołaniach funkcji:

- Jeśli w odpowiedzi znajdują się wywołania funkcji:
  - Gemini 3 zawsze będzie mieć podpis w pierwszej części wywołania funkcji.
    Zwrócenie tej części jest **obowiązkowe**.
  - Gemini 2.5 będzie mieć podpis w pierwszej części (niezależnie od typu). Zwrócenie tej części jest **opcjonalne**.
- Jeśli w odpowiedzi nie ma wywołań funkcji:
  - Gemini 3 będzie mieć podpis w ostatniej części, jeśli model wygeneruje myśl.
  - Gemini 2.5 nie będzie mieć podpisu w żadnej części.

Więcej informacji o
porównaniu znajdziesz na stronie [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#signatures).
W przypadku modeli Gemini 3 Image zapoznaj się z sekcją Proces myślowy w przewodniku po
[generowaniu obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#thinking-process).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-08 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-08 UTC."],[],[]]
