---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=pt-BR
fetched_at: 2026-08-24T02:26:58.279443+00:00
title: "Assinaturas de racioc\u00ednio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

A [API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pt-br) já está disponível para todos os usuários. Recomendamos usar essa API para acessar todos os recursos e modelos mais recentes.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

O Google usa tecnologia de IA na tradução de conteúdos para seu idioma de preferência. As traduções com IA podem ter erros.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Assinaturas de raciocínio

As assinaturas de pensamento são representações criptografadas do processo de pensamento interno do modelo e são usadas para preservar o contexto de raciocínio em interações de várias etapas.
Ao usar modelos de pensamento (como as séries Gemini 3 e 2.5), a API pode
retornar um campo `thoughtSignature` nas [partes de conteúdo](https://ai.google.dev/api/caching?hl=pt-br#Part)
da resposta (por exemplo, partes `text` ou `functionCall`).

Como regra geral, se você receber uma assinatura de pensamento em uma resposta do modelo, transmita-a exatamente como recebida ao enviar o histórico da conversa na próxima interação.
**Ao usar modelos do Gemini 3, é necessário transmitir assinaturas de pensamento durante a chamada de função. Caso contrário, você receberá um erro de validação** (código de status 4xx).
Isso inclui o uso da configuração de `minimal`
[nível de pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#thinking-levels) para o Gemini 3
Flash.

## Como funciona

O gráfico abaixo mostra o significado de "interação" e "etapa" em relação a
[chamada de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br) na API Gemini. Uma "interação" é uma troca única e completa em uma conversa entre um usuário e um modelo. Uma "etapa" é uma ação ou operação mais detalhada realizada pelo modelo, geralmente como parte de um processo maior para concluir uma interação.

![Diagrama de turnos e etapas de chamada de função](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=pt-br)

*Este documento se concentra no processamento de chamadas de função para modelos do Gemini 3. Consulte
a seção sobre o [comportamento do modelo](#model-behavior) para conferir discrepâncias com a versão 2.5.*

O Gemini 3 retorna assinaturas de pensamento para todas as respostas do modelo (respostas da API) com uma chamada de função. As assinaturas de pensamento aparecem nos seguintes casos:

- Quando há [chamadas de função](https://ai.google.dev/gemini-api/docs/function-calling?hl=pt-br#parallel_function_calling)
  paralelas, a primeira parte da chamada de função retornada pela resposta do modelo terá uma
  assinatura de pensamento.
- Quando há chamadas de função sequenciais (várias etapas), cada chamada de função terá uma assinatura, e você precisará transmitir todas as assinaturas.
- As respostas do modelo sem uma chamada de função vão retornar uma assinatura de pensamento na última parte retornada pelo modelo.

A tabela a seguir oferece uma visualização para chamadas de função de várias etapas, combinando as definições de interações e etapas com o conceito de assinaturas apresentado acima:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Interação** | **Etapa** | **Solicitação do usuário** | **Resposta do modelo** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Nenhum |

## Assinaturas em partes de chamada de função

Quando o Gemini gera um `functionCall`, ele depende da `thought_signature` para processar a saída da ferramenta corretamente na próxima interação.

- **Comportamento**:
  - **Chamada de função única**: a parte `functionCall` vai conter uma `thought_signature`.
  - **Chamadas de função paralelas**: se o modelo gerar chamadas de função paralelas
    em uma resposta, a `thought_signature` será anexada **apenas à primeira**
    `functionCall` parte. As partes `functionCall` subsequentes na mesma resposta **não** vão conter uma assinatura.
- **Requisito**: você **precisa** retornar essa assinatura na parte exata em que ela
  foi recebida ao enviar o histórico da conversa de volta.
- **Validação**: a validação estrita é aplicada a todas as chamadas de função na
  interação atual . Apenas a interação atual é necessária. Não validamos as interações anteriores.
  - A API volta no histórico (do mais recente ao mais antigo) para encontrar a mensagem **do usuário** mais recente que contém conteúdo padrão (por exemplo, `text`) ( que seria o início da interação atual). Essa mensagem **be** será uma `functionResponse`.
  - **Todas** as interações `functionCall` do modelo que ocorrem após essa mensagem de uso específica são consideradas parte da interação.
  - A **primeira** parte `functionCall` em **cada etapa** da interação atual **precisa** incluir a `thought_signature`.
  - Se você omitir uma `thought_signature` para a primeira parte `functionCall` em qualquer etapa da interação atual, a solicitação vai falhar com um erro 400.
- **Se as assinaturas adequadas não forem retornadas, veja como você vai receber um erro**
  - Modelos do Gemini 3: a falha ao incluir assinaturas vai resultar em um erro 400. A redação será do formulário:
    - A chamada de função `<Function Call>` no bloco de conteúdo `<index of contents array>`
      está sem um `thought_signature`. Por exemplo, *a chamada de função `FC1` no bloco de conteúdo `1.` está sem um `thought_signature`.*

### Exemplo de chamada de função sequencial

Esta seção mostra um exemplo de várias chamadas de função em que o usuário faz uma pergunta complexa que exige várias tarefas.

Vamos analisar um exemplo de chamada de função de várias interações em que o usuário faz
uma pergunta complexa que exige várias tarefas: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Interação** | **Etapa** | **Solicitação do usuário** | **Resposta do modelo** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

O código a seguir ilustra a sequência na tabela acima.

**Interação 1, etapa 1 (solicitação do usuário)**

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

**Interação 1, etapa 1 (resposta do modelo)**

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

**Interação 1, etapa 2 (resposta do usuário: envio de saídas de ferramentas)** Como essa interação do usuário contém apenas uma `functionResponse` (sem texto novo), ainda estamos na interação 1. Precisamos
preservar `<Signature_A>`.

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

**Interação 1, etapa 2 (modelo)** O modelo agora decide reservar um táxi com base na saída da ferramenta anterior.

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

**Interação 1, etapa 3 (usuário: envio da saída da ferramenta)** Para enviar a confirmação da reserva de táxi, precisamos incluir assinaturas para **TODAS** as chamadas de função neste loop
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

### Exemplo de chamada de função paralela

Vamos analisar um exemplo de chamada de função paralela em que o usuário pergunta
`"Check weather in Paris and London"` para ver onde o modelo faz a validação.

| **Interação** | **Etapa** | **Solicitação do usuário** | **Resposta do modelo** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (no FCs) | Nenhum |

O código a seguir ilustra a sequência na tabela acima.

**Interação 1, etapa 1 (solicitação do usuário)**

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

**Interação 1, etapa 1 (resposta do modelo)**

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

**Interação 1, etapa 2 (resposta do usuário: envio de saídas de ferramentas)** Precisamos preservar
`<Signature_A>` na primeira parte exatamente como recebida.

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

## Assinaturas em partes não `functionCall`

O Gemini também pode retornar `thought_signatures` na parte final da resposta em partes que não são de chamada de função.

- **Comportamento**: a parte de conteúdo final (`text, inlineData…`) retornada pelo
  modelo pode conter um `thought_signature`.
- **Recomendação**: o retorno dessas assinaturas é **recomendado** para garantir que
  o modelo mantenha um raciocínio de alta qualidade, especialmente para instruções complexas
  seguindo ou fluxos de trabalho de agente simulados.
- **Validação**: a API **não** aplica a validação de forma estrita. Você não vai receber um erro de bloqueio se omiti-las, embora a performance possa ser reduzida.

### Raciocínio de texto/no contexto (sem validação)

**Interação 1, etapa 1 (resposta do modelo)**

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

**Interação 2, etapa 1 (usuário)**

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

## Assinaturas para compatibilidade com OpenAI

Os exemplos a seguir mostram como processar assinaturas de pensamento para uma API de conclusão de chat
usando [compatibilidade com OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=pt-br).

### Exemplo de chamada de função sequencial

Este é um exemplo de várias chamadas de função em que o usuário faz uma pergunta complexa que exige várias tarefas.

Vamos analisar um exemplo de chamada de função de várias interações em que o usuário pergunta `Check flight status for AA100 and book a taxi if delayed` e você pode ver o que acontece quando o usuário faz uma pergunta complexa que exige várias tarefas.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Interação** | **Etapa** | **Solicitação do usuário** | **Resposta do modelo** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

O código a seguir mostra a sequência fornecida.

**Interação 1, etapa 1 (solicitação do usuário)**

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

**Interação 1, etapa 1 (resposta do modelo)**

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

**Interação 1, etapa 2 (resposta do usuário: envio de saídas de ferramentas)**

Como essa interação do usuário contém apenas um `functionResponse` (sem texto novo), ainda estamos
na interação 1 e precisamos preservar `<Signature_A>`.

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

**Interação 1, etapa 2 (modelo)**

O modelo agora decide reservar um táxi com base na saída da ferramenta anterior.

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

**Interação 1, etapa 3 (usuário: envio da saída da ferramenta)**

Para enviar a confirmação da reserva de táxi, precisamos incluir assinaturas para TODAS as
chamadas de função neste loop (`<Signature A>` + `<Signature B>`).

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

### Exemplo de chamada de função paralela

Vamos analisar um exemplo de chamada de função paralela em que o usuário pergunta
`"Check weather in Paris and London"` e você pode ver onde o modelo faz
validação.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Interação** | **Etapa** | **Solicitação do usuário** | **Resposta do modelo** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Confira o código para analisar a sequência fornecida.

**Interação 1, etapa 1 (solicitação do usuário)**

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

**Interação 1, etapa 1 (resposta do modelo)**

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

**Interação 1, etapa 2 (resposta do usuário: envio de saídas de ferramentas)**

É necessário preservar `<Signature_A>` na primeira parte exatamente como recebida.

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

## Perguntas frequentes

1. **Como faço para transferir o histórico de um modelo diferente para o Gemini 3 com uma parte de chamada de função na interação e etapa atuais? Preciso fornecer partes de chamada de função
   que não foram geradas pela API e, portanto, não têm uma assinatura de pensamento associada
   ?**

   Embora a injeção de blocos de chamada de função personalizados na solicitação seja fortemente
   desencorajada, em casos em que não é possível evitá-la, por exemplo, fornecer informações
   ao modelo sobre chamadas de função e respostas que foram executadas
   de forma determinística pelo cliente ou transferir um rastreamento de um modelo diferente
   que não inclui assinaturas de pensamento, é possível definir as seguintes
   assinaturas fictícias de `"context_engineering_is_the_way_to_go"` ou
   `"skip_thought_signature_validator"` no campo de assinatura de pensamento para ignorar a
   validação.
2. **Estou enviando chamadas e respostas de função paralelas intercaladas, e a API está retornando um erro 400. Por quê?**

   Quando a API retorna chamadas de função paralelas "FC1 + assinatura, FC2", a resposta do usuário esperada é "FC1 + assinatura, FC2, FR1, FR2". Se você as tiver intercaladas como "FC1 + assinatura, FR1, FC2, FR2", a API vai retornar um erro 400.
3. **Ao fazer streaming, e o modelo não retornar uma chamada de função, não consigo encontrar
   a assinatura de pensamento**

   Durante uma resposta do modelo que não contém uma FC com uma solicitação de streaming, o modelo pode retornar a assinatura de pensamento em uma parte com uma parte de conteúdo de texto vazia. É recomendável analisar toda a solicitação até que o `finish_reason` seja retornado pelo modelo.

## Assinaturas de pensamento para diferentes modelos

[Os modelos do Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pt-br#gemini-3) e do Gemini 2.5
se comportam de maneira diferente com assinaturas de pensamento em chamadas de função:

- Se houver chamadas de função em uma resposta,
  - O Gemini 3 sempre terá a assinatura na primeira parte da chamada de função.
    É **obrigatório** retornar essa parte.
  - O Gemini 2.5 terá a assinatura na primeira parte (independente do tipo). É **opcional** retornar essa parte.
- Se não houver chamadas de função em uma resposta,
  - O Gemini 3 terá a assinatura na última parte se o modelo gerar um pensamento.
  - O Gemini 2.5 não terá uma assinatura em nenhuma parte.

Consulte a página [Pensamento](https://ai.google.dev/gemini-api/docs/thinking?hl=pt-br#signatures) para mais
detalhes sobre a comparação.
Para modelos de imagem do Gemini 3, consulte a seção processo de pensamento do
[guia de geração de imagens](https://ai.google.dev/gemini-api/docs/image-generation?hl=pt-br#thinking-process).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-08-19 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-08-19 UTC."],[],[]]
