---
source_url: https://ai.google.dev/gemini-api/docs/thought-signatures?hl=pl
fetched_at: 2026-06-15T06:28:36.210016+00:00
title: "Podpisy my\u015bli \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Podpisy myśli

Podpisy myśli to zaszyfrowane reprezentacje wewnętrznego procesu myślowego modelu. Służą one do zachowania kontekstu rozumowania w interakcjach wieloetapowych.
W przypadku korzystania z modeli myślenia (takich jak Gemini 3 i 2.5) interfejs API może zwracać pole `thoughtSignature` w ramach [części treści](https://ai.google.dev/api/caching?hl=pl#Part) odpowiedzi (np. części `text` lub `functionCall`).

Ogólnie rzecz biorąc, jeśli w odpowiedzi modelu otrzymasz sygnaturę myśli, w kolejnej turze rozmowy prześlij ją z powrotem w niezmienionej postaci wraz z historią rozmowy.
**Podczas korzystania z modeli Gemini 3 musisz przekazywać sygnatury myśli podczas wywoływania funkcji, w przeciwnym razie otrzymasz błąd weryfikacji** (kod stanu 4xx).
Dotyczy to również korzystania z ustawienia `minimal`
[poziom myślenia](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#thinking-levels) w przypadku Gemini 3 Flash.

## Jak to działa

Grafika poniżej ilustruje znaczenie terminów „tura” i „krok” w kontekście [wywoływania funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl) w interfejsie Gemini API. „Tura” to pojedyncza, pełna wymiana informacji w rozmowie między użytkownikiem a modelem. „Krok” to bardziej szczegółowe działanie lub operacja wykonywana przez model, często w ramach większego procesu, który ma na celu ukończenie tury.

![Diagram przedstawiający tury i kroki wywoływania funkcji](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=pl)

*Ten dokument dotyczy obsługi wywoływania funkcji w przypadku modeli Gemini 3. Więcej informacji o różnicach w stosunku do wersji 2.5 znajdziesz w sekcji [Zachowanie modelu](#model-behavior).*

Gemini 3 zwraca sygnatury myśli dla wszystkich odpowiedzi modelu (odpowiedzi z interfejsu API) z wywołaniem funkcji. Podpisy myśli pojawiają się w tych przypadkach:

- W przypadku [równoległych wywołań funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl#parallel_function_calling) pierwsza część wywołania funkcji zwrócona przez odpowiedź modelu będzie zawierać sygnaturę myśli.
- W przypadku sekwencyjnych wywołań funkcji (wielokrotnych) każde wywołanie funkcji będzie miało sygnaturę i musisz przekazać wszystkie sygnatury z powrotem.
- Odpowiedzi modelu bez wywołania funkcji będą zawierać sygnaturę myśli w ostatniej części zwróconej przez model.

Poniższa tabela przedstawia wizualizację wieloetapowych wywołań funkcji, łącząc definicje tur i etapów z wprowadzonym powyżej pojęciem sygnatur:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Obróć** | **Step** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Brak |

## Podpisy w częściach wywołania funkcji

Gdy Gemini generuje `functionCall`, korzysta z `thought_signature`, aby w kolejnym kroku prawidłowo przetworzyć dane wyjściowe narzędzia.

- **Zachowanie**:
  - **Wywołanie pojedynczej funkcji:** część `functionCall` będzie zawierać `thought_signature`.
  - **Równoległe wywołania funkcji:**  jeśli model generuje w odpowiedzi równoległe wywołania funkcji, symbol `thought_signature` jest dołączany **tylko do pierwszej** części.`functionCall` Kolejne części `functionCall` w tej samej odpowiedzi **nie** będą zawierać podpisu.
- **Wymaganie:**  podczas odsyłania historii rozmowy **musisz** zwrócić ten podpis w dokładnie tym samym miejscu, w którym został otrzymany.
- **Weryfikacja:** w przypadku wszystkich wywołań funkcji w bieżącej turze obowiązuje ścisła weryfikacja . (Wymagana jest tylko bieżąca tura. Nie sprawdzamy poprzednich tur).
  - Interfejs API cofa się w historii (od najnowszej do najstarszej), aby znaleźć najnowszą wiadomość **użytkownika** zawierającą standardowe treści (np. `text`), która będzie początkiem bieżącej tury. Nie będzie to **be** `functionResponse`.
  - W przypadku modelu **wszystkie** `functionCall` wypowiedzi następujące po tym konkretnym komunikacie o użyciu są traktowane jako część wypowiedzi.
  - **Pierwsza** część `functionCall` w **każdym kroku** bieżącej tury **musi** zawierać `thought_signature`.
  - Jeśli w pierwszej części `thought_signature` w dowolnym kroku bieżącej tury pominiesz `functionCall`, żądanie zakończy się niepowodzeniem i zostanie zwrócony błąd 400.
- **Jeśli nie zostaną zwrócone prawidłowe podpisy, wystąpi błąd**
  - Modele Gemini 3: brak podpisów spowoduje błąd 400. Tekst będzie miał postać:
    - W wywołaniu funkcji `<Function Call>` w bloku treści `<index of contents array>` brakuje elementu `thought_signature`. Na przykład w bloku treści `1.` brakuje `thought_signature` w *wywołaniu funkcji`FC1`*.

### Przykład sekwencyjnego wywoływania funkcji

W tej sekcji znajdziesz przykład kilku wywołań funkcji, w których użytkownik zadaje złożone pytanie wymagające wykonania kilku zadań.

Przyjrzyjmy się przykładowi wywoływania funkcji w wielu turach, w którym użytkownik zadaje złożone pytanie wymagające wykonania kilku zadań: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Obróć** | **Step** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Poniższy kod ilustruje sekwencję z tabeli powyżej.

**Tura 1, krok 1 (prośba użytkownika)**

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

**Tura 1, krok 1 (odpowiedź modelu)**

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

**Tura 1, krok 2 (odpowiedź użytkownika – wysyłanie wyników narzędzia)** Ponieważ ta tura użytkownika zawiera tylko `functionResponse` (bez nowego tekstu), nadal jesteśmy w turze 1. Musimy zachować `<Signature_A>`.

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

**Tura 1, krok 2 (model)**: model decyduje teraz o zamówieniu taksówki na podstawie poprzedniego wyniku narzędzia.

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

**Tura 1, krok 3 (użytkownik – wysyłanie danych wyjściowych narzędzia)** Aby wysłać potwierdzenie rezerwacji taksówki, musimy uwzględnić podpisy **WSZYSTKICH** wywołań funkcji w tej pętli (`<Signature A>` + `<Signature B>`).

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

Przyjrzyjmy się przykładowi równoległego wywoływania funkcji, w którym użytkownik prosi`"Check weather in Paris and London"` o sprawdzenie, gdzie model przeprowadza weryfikację.

| **Obróć** | **Step** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 („Paryż”) + podpis  FC2 („Londyn”) | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (bez FC) | Brak |

Poniższy kod ilustruje sekwencję z tabeli powyżej.

**Tura 1, krok 1 (prośba użytkownika)**

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

**Tura 1, krok 1 (odpowiedź modelu)**

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

**Tura 1, krok 2 (odpowiedź użytkownika – wysyłanie wyników narzędzia)** Musimy zachować
`<Signature_A>` pierwszą część dokładnie tak, jak została otrzymana.

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

## Podpisy w częściach innych niż `functionCall`

Gemini może też zwracać znak `thought_signatures` w ostatniej części odpowiedzi w przypadku części niebędących wywołaniami funkcji.

- **Zachowanie:** ostatnia część treści (`text, inlineData…`) zwrócona przez model może zawierać `thought_signature`.
- **Rekomendacja:**  zwracanie tych sygnatur jest **zalecane**, aby zapewnić wysoką jakość rozumowania modelu, zwłaszcza w przypadku złożonych instrukcji lub symulowanych przepływów pracy agenta.
- **Weryfikacja:**  interfejs API **nie** wymusza weryfikacji. Jeśli je pominiesz, nie otrzymasz błędu blokującego, ale wydajność może się pogorszyć.

### Tekst/wnioskowanie w kontekście (bez weryfikacji)

**Tura 1, krok 1 (odpowiedź modelu)**

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

**Tura 2, krok 1 (użytkownik)**

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

## Zachowywanie myśli i wykorzystanie tokenów

**Od modelu Gemini 3.5 Flash** model używa kontekstu rozumowania ze wszystkich poprzednich tur, gdy w historii rozmów występują sygnatury myśli.

Aby włączyć zachowywanie myśli, **przekaż pełną, niezmodyfikowaną historię rozmowy** (w tym pola `thought_signature` zwrócone w poprzednich turach modelu) w tablicy `contents` w swoim żądaniu.

### Zarządzanie wykorzystaniem tokenów

Zachowywanie pośrednich przemyśleń w wielu turach zwiększa liczbę tokenów wejściowych w kolejnych turach, ponieważ model musi analizować sygnatury przemyśleń z poprzednich tur.

Jeśli Twoja aplikacja wykonuje proste zapytania lub chcesz zminimalizować koszty długich rozmów, możesz wyczyścić z historii rozmów poprzednie sygnatury myśli.

## Sygnatury zgodne z OpenAI

Poniższy przykład pokazuje, jak obsługiwać sygnatury myśli w przypadku interfejsu API do uzupełniania czatu za pomocą [zgodności z OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pl).

### Przykład sekwencyjnego wywoływania funkcji

To przykład wywoływania wielu funkcji, w którym użytkownik zadaje złożone pytanie wymagające wykonania kilku zadań.

Przyjrzyjmy się przykładowi wywoływania funkcji w wielu turach, w którym użytkownik zadaje pytanie
`Check flight status for AA100 and book a taxi if delayed`. Zobaczysz, co się stanie, gdy użytkownik zada złożone pytanie wymagające wykonania wielu zadań.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Obróć** | **Step** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Poniższy kod przedstawia podaną sekwencję.

**Tura 1, krok 1 (prośba użytkownika)**

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

**Tura 1, krok 1 (odpowiedź modelu)**

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

**Tura 1, krok 2 (odpowiedź użytkownika – wysyłanie wyników narzędzi)**

Ponieważ ta tura użytkownika zawiera tylko `functionResponse` (bez nowego tekstu), nadal jesteśmy w turze 1 i musimy zachować `<Signature_A>`.

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

**Tura 1, krok 2 (model)**

Model decyduje teraz o zamówieniu taksówki na podstawie poprzedniego wyniku narzędzia.

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

**Tura 1, krok 3 (użytkownik – wysyłanie danych wyjściowych narzędzia)**

Aby wysłać potwierdzenie rezerwacji taksówki, musimy uwzględnić podpisy wszystkich wywołań funkcji w tej pętli (`<Signature A>` + `<Signature B>`).

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

Przyjrzyjmy się przykładowi równoległego wywoływania funkcji, w którym użytkownik zadaje pytanie `"Check weather in Paris and London"`, a Ty możesz zobaczyć, gdzie model przeprowadza weryfikację.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Obróć** | **Step** | **Prośba użytkownika** | **Odpowiedź modelu** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Oto kod, który umożliwia przejście podanej sekwencji.

**Tura 1, krok 1 (prośba użytkownika)**

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

**Tura 1, krok 1 (odpowiedź modelu)**

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

**Tura 1, krok 2 (odpowiedź użytkownika – wysyłanie wyników narzędzi)**

W pierwszej części musisz zachować `<Signature_A>` w dokładnie takiej formie, w jakiej została otrzymana.

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

1. **Jak przenieść historię z innego modelu do Gemini 3 z wywołaniem funkcji w bieżącej turze i kroku? Muszę podać części wywołania funkcji, które nie zostały wygenerowane przez interfejs API, a więc nie mają powiązanego podpisu myśli?**

   Wstrzykiwanie niestandardowych bloków wywołań funkcji do żądania jest zdecydowanie odradzane.W przypadkach, w których nie można tego uniknąć, np. gdy trzeba przekazać modelowi informacje o wywołaniach funkcji i odpowiedziach, które zostały wykonane deterministycznie przez klienta, lub przenieść ślad z innego modelu, który nie zawiera sygnatur myśli, możesz ustawić w polu sygnatury myśli te sygnatury zastępcze: `"context_engineering_is_the_way_to_go"` lub `"skip_thought_signature_validator"`, aby pominąć weryfikację.
2. **Wysyłam przeplatane równoległe wywołania funkcji i odpowiedzi, a interfejs API zwraca kod 400. Dlaczego?**

   Gdy interfejs API zwraca równoległe wywołania funkcji „FC1 + podpis, FC2”, oczekiwana odpowiedź użytkownika to „FC1 + podpis, FC2, FR1, FR2”. Jeśli są one przeplatane w formacie „FC1 + podpis, FR1, FC2, FR2”, interfejs API zwróci błąd 400.
3. **Podczas przesyłania strumieniowego i gdy model nie zwraca wywołania funkcji, nie mogę znaleźć podpisu myśli**

   Podczas odpowiedzi modelu niezawierającej funkcji FC z żądaniem przesyłania strumieniowego model może zwrócić sygnaturę myśli w części z pustą treścią tekstową. Zalecamy przeanalizowanie całego żądania, dopóki model nie zwróci znaku `finish_reason`.

## Sygnatury myśli dla różnych modeli

[Modele Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-3) i Gemini 2.5 zachowują się inaczej w przypadku sygnatur myśli:

- **Zachowywanie myśli:**
  - **Od modelu Gemini 3.5 Flash** model korzysta z kontekstu rozumowania ze wszystkich poprzednich tur, gdy w historii rozmowy występują sygnatury myśli.
  - Starsze modele nie wykorzystują kontekstu rozumowania z poprzednich tur w ten sam sposób.
- **Jeśli w odpowiedzi znajdują się wywołania funkcji:**
  - Gemini 3 zawsze będzie zawierać sygnaturę w pierwszej części wywołania funkcji.
    Zwrot tej części jest **obowiązkowy**.
  - Gemini 2.5 będzie umieszczać podpis w pierwszej części (niezależnie od typu). Zwrot tej części jest **opcjonalny**.
- **Jeśli w odpowiedzi nie ma wywołań funkcji:**
  - Jeśli model wygeneruje myśl, Gemini 3 umieści podpis na końcu.
  - Gemini 2.5 nie będzie zawierać podpisu w żadnej części.

Więcej informacji o porównaniu znajdziesz na stronie [Myślenie](https://ai.google.dev/gemini-api/docs/thinking?hl=pl#signatures).
W przypadku modeli Gemini 3 Image zapoznaj się z sekcją dotyczącą procesu rozumowania w przewodniku [Generowanie obrazów](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#thinking-process).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-06-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-06-01 UTC."],[],[]]
