---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=fr
fetched_at: 2026-07-06T05:13:46.368630+00:00
title: "Signatures de pens\u00e9e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Signatures de pensée

Les signatures de pensée sont des représentations chiffrées du processus de réflexion interne du modèle. Elles sont utilisées pour préserver le contexte de raisonnement lors d'interactions en plusieurs étapes.
Lorsque vous utilisez des modèles de réflexion (tels que les séries Gemini 3 et 2.5), l'API peut renvoyer un champ `thoughtSignature` dans les [parties de contenu](https://ai.google.dev/api/caching?hl=fr#Part) de la réponse (par exemple, les parties `text` ou `functionCall`).

En règle générale, si vous recevez une signature de pensée dans la réponse d'un modèle, vous devez la renvoyer exactement telle qu'elle a été reçue lorsque vous envoyez l'historique des conversations au tour suivant.
**Lorsque vous utilisez les modèles Gemini 3, vous devez renvoyer les signatures de pensée lors de l'appel de fonction, sinon vous recevrez une erreur de validation** (code d'état 4xx).
Cela inclut l'utilisation du paramètre `minimal`
[Niveau de raisonnement](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#thinking-levels) pour Gemini 3 Flash.

## Fonctionnement

Le graphique ci-dessous illustre la signification des termes "tour" et "étape" en ce qui concerne l'[appel de fonction](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr) dans l'API Gemini. Un "tour" correspond à un échange complet dans une conversation entre un utilisateur et un modèle. Une "étape" est une action ou une opération plus précise effectuée par le modèle, souvent dans le cadre d'un processus plus vaste pour terminer un tour.

![Diagramme des tours et des étapes d&#39;appel de fonction](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=fr)

*Ce document se concentre sur la gestion de l'appel de fonction pour les modèles Gemini 3. Consultez la section [Comportement du modèle](#model-behavior) pour connaître les différences avec la version 2.5.*

Gemini 3 renvoie des signatures de pensée pour toutes les réponses du modèle (réponses de l'API) avec un appel de fonction. Les signatures de pensée s'affichent dans les cas suivants :

- Lorsqu'il y a des appels de [fonction parallèle](https://ai.google.dev/gemini-api/docs/function-calling?hl=fr#parallel_function_calling), la première partie d'appel de fonction renvoyée par la réponse du modèle aura une signature de pensée.
- Lorsqu'il existe des appels de fonction séquentiels (multietapes), chaque appel de fonction aura une signature et vous devrez renvoyer toutes les signatures.
- Les réponses du modèle sans appel de fonction renvoient une signature de réflexion dans la dernière partie renvoyée par le modèle.

Le tableau suivant fournit une visualisation des appels de fonction en plusieurs étapes, en combinant les définitions des tours et des étapes avec le concept de signatures présenté ci-dessus :

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tourner** | **Step** | **Demande de l'utilisateur** | **Réponse du modèle** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Aucun |

## Signatures dans les parties d'appel de fonction

Lorsque Gemini génère un `functionCall`, il s'appuie sur `thought_signature` pour traiter correctement la sortie de l'outil au tour suivant.

- **Comportement** :
  - **Appel de fonction unique** : la partie `functionCall` contiendra un `thought_signature`.
  - **Appels de fonction parallèles** : si le modèle génère des appels de fonction parallèles dans une réponse, le `thought_signature` n'est associé **qu'à la première** partie `functionCall`. Les parties `functionCall` suivantes de la même réponse **ne contiendront pas** de signature.
- **Exigence** : Vous **devez** renvoyer cette signature exactement à l'endroit où elle a été reçue lorsque vous renvoyez l'historique des conversations.
- **Validation** : une validation stricte est appliquée à tous les appels de fonction au cours du tour actuel . (Seul le tour actuel est requis. Nous ne validons pas les tours précédents.)
  - L'API remonte dans l'historique (du plus récent au plus ancien) pour trouver le message **User** le plus récent contenant du contenu standard (par exemple, `text`), qui correspond au début du tour actuel. Il ne **be** d'un `functionResponse`.
  - Les tours `functionCall` du modèle **Tous** qui se produisent après ce message d'utilisation spécifique sont considérés comme faisant partie du tour.
  - La **première** partie `functionCall` de **chaque étape** du tour actuel **doit** inclure son `thought_signature`.
  - Si vous omettez un `thought_signature` pour la première partie `functionCall` d'une étape du tour actuel, la requête échouera et renverra une erreur 400.
- **Si les signatures appropriées ne sont pas renvoyées, voici comment l'erreur s'affichera :**
  - Modèles Gemini 3 : si vous n'incluez pas de signatures, une erreur 400 se produira. Le libellé se présentera sous la forme suivante :
    - Il manque un `thought_signature` à l'appel de fonction `<Function Call>` dans le bloc de contenu `<index of contents array>`. Par exemple, *l'appel de fonction `FC1` dans le bloc de contenu `1.` est manquant `thought_signature`*.

### Exemple d'appel de fonction séquentiel

Cette section présente un exemple d'appels de fonction multiples dans lequel l'utilisateur pose une question complexe nécessitant plusieurs tâches.

Prenons l'exemple d'un appel de fonction multitours où l'utilisateur pose une question complexe nécessitant plusieurs tâches : `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tourner** | **Step** | **Demande de l'utilisateur** | **Réponse du modèle** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Le code suivant illustre la séquence du tableau ci-dessus.

**Tour 1, étape 1 (demande de l'utilisateur)**

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

**Tour 1, étape 1 (réponse du modèle)**

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

**Tour 1, étape 2 (réponse de l'utilisateur : envoi des résultats de l'outil)** : comme ce tour d'utilisateur ne contient qu'un `functionResponse` (aucun nouveau texte), nous sommes toujours au tour 1. Nous devons préserver `<Signature_A>`.

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

**Tour 1, étape 2 (modèle)** : le modèle décide maintenant de réserver un taxi en fonction du résultat de l'outil précédent.

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

**Tour 1, Étape 3 (Utilisateur : envoi du résultat de l'outil)** Pour envoyer la confirmation de la réservation de taxi, nous devons inclure des signatures pour **TOUS** les appels de fonction dans cette boucle (`<Signature A>` + `<Signature B>`).

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

### Exemple d'appel de fonction parallèle

Passons à un exemple d'appel de fonction parallèle où l'utilisateur demande `"Check weather in Paris and London"` pour voir où le modèle effectue la validation.

| **Tourner** | **Step** | **Demande de l'utilisateur** | **Réponse du modèle** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("Londres") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (sans FC) | Aucun |

Le code suivant illustre la séquence du tableau ci-dessus.

**Tour 1, étape 1 (demande de l'utilisateur)**

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

**Tour 1, étape 1 (réponse du modèle)**

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

**Étape 2 du tour 1 (réponse de l'utilisateur : envoi des résultats de l'outil)** Nous devons conserver `<Signature_A>` dans la première partie exactement tel qu'il a été reçu.

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

## Signatures dans les parties non `functionCall`

Gemini peut également renvoyer `thought_signatures` dans la dernière partie de la réponse, dans les parties qui ne sont pas des appels de fonction.

- **Comportement** : la dernière partie du contenu (`text, inlineData…`) renvoyée par le modèle peut contenir un `thought_signature`.
- **Recommandation** : il est **recommandé** de renvoyer ces signatures pour s'assurer que le modèle conserve un raisonnement de haute qualité, en particulier pour les workflows agentifs simulés ou le suivi d'instructions complexes.
- **Validation** : l'API **n'applique pas** strictement la validation. Vous ne recevrez pas d'erreur bloquante si vous les omettez, mais les performances peuvent se dégrader.

### Texte/Raisonnement en contexte (aucune validation)

**Tour 1, étape 1 (réponse du modèle)**

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

**Tour 2, étape 1 (utilisateur)**

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

## Signatures pour la compatibilité avec OpenAI

L'exemple suivant montre comment gérer les signatures de pensée pour une API Chat Completions à l'aide de la [compatibilité OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr).

### Exemple d'appel de fonction séquentiel

Voici un exemple d'appel de fonction multiple où l'utilisateur pose une question complexe nécessitant plusieurs tâches.

Examinons un exemple d'appel de fonction multitours où l'utilisateur demande `Check flight status for AA100 and book a taxi if delayed`. Vous pouvez voir ce qui se passe lorsque l'utilisateur pose une question complexe nécessitant plusieurs tâches.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tourner** | **Step** | **Demande de l'utilisateur** | **Réponse du modèle** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Le code suivant parcourt la séquence donnée.

**Tour 1, étape 1 (demande de l'utilisateur)**

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

**Tour 1, étape 1 (réponse du modèle)**

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

**Tour 1, étape 2 (réponse de l'utilisateur : envoi des résultats de l'outil)**

Étant donné que ce tour d'utilisateur ne contient qu'un `functionResponse` (pas de nouveau texte), nous sommes toujours au tour 1 et devons conserver `<Signature_A>`.

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

**Tour 1, étape 2 (modèle)**

Le modèle décide maintenant de réserver un taxi en fonction du résultat de l'outil précédent.

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

**Tour 1, Étape 3 (Utilisateur : envoi du résultat de l'outil)**

Pour envoyer la confirmation de réservation de taxi, nous devons inclure des signatures pour TOUS les appels de fonction dans cette boucle (`<Signature A>` + `<Signature B>`).

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

### Exemple d'appel de fonction parallèle

Prenons l'exemple d'un appel de fonction parallèle où l'utilisateur demande `"Check weather in Paris and London"`. Vous pouvez voir où le modèle effectue la validation.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tourner** | **Step** | **Demande de l'utilisateur** | **Réponse du modèle** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Voici le code permettant de parcourir la séquence donnée.

**Tour 1, étape 1 (demande de l'utilisateur)**

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

**Tour 1, étape 1 (réponse du modèle)**

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

**Tour 1, étape 2 (réponse de l'utilisateur : envoi des résultats de l'outil)**

Vous devez conserver `<Signature_A>` dans la première partie exactement tel que vous l'avez reçu.

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

## Questions fréquentes

1. **Comment transférer l'historique d'un autre modèle vers Gemini 3 avec une partie d'appel de fonction dans le tour et l'étape actuels ? Je dois fournir des parties d'appel de fonction qui n'ont pas été générées par l'API et qui n'ont donc pas de signature de pensée associée.**

   Bien qu'il soit fortement déconseillé d'injecter des blocs d'appels de fonction personnalisés dans la requête, vous pouvez définir les signatures fictives suivantes (`"context_engineering_is_the_way_to_go"` ou `"skip_thought_signature_validator"`) dans le champ de signature de pensée pour ignorer la validation dans les cas où cela ne peut pas être évité (par exemple, pour fournir au modèle des informations sur les appels de fonction et les réponses qui ont été exécutés de manière déterministe par le client, ou pour transférer une trace à partir d'un autre modèle qui n'inclut pas de signatures de pensée).
2. **J'envoie des appels et des réponses de fonctions parallèles entrelacés, et l'API renvoie un code 400. Pourquoi ?**

   Lorsque l'API renvoie des appels de fonction parallèles "FC1 + signature, FC2", la réponse attendue de l'utilisateur est "FC1+ signature, FC2, FR1, FR2". Si vous les avez entrelacés comme "FC1 + signature, FR1, FC2, FR2", l'API renverra une erreur 400.
3. **Lorsque le modèle ne renvoie pas d'appel de fonction lors du streaming, je ne trouve pas la signature de la pensée.**

   Lorsqu'une réponse de modèle ne contient pas de FC avec une demande de streaming, le modèle peut renvoyer la signature de pensée dans une partie avec une partie de contenu textuel vide. Il est conseillé d'analyser l'intégralité de la requête jusqu'à ce que le modèle renvoie `finish_reason`.

## Signatures de réflexion pour différents modèles

Les [modèles Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-3) et Gemini 2.5 se comportent différemment avec les signatures de pensée dans les appels de fonction :

- Si une réponse contient des appels de fonction,
  - Gemini 3 aura toujours la signature dans la première partie de l'appel de fonction.
    Il est **obligatoire** de renvoyer cette partie.
  - Dans Gemini 2.5, la signature figurera dans la première partie (quel que soit le type). Le renvoi de cette partie est **facultatif**.
- S'il n'y a pas d'appels de fonction dans une réponse,
  - Gemini 3 ajoutera la signature à la dernière partie si le modèle génère une réflexion.
  - Gemini 2.5 ne comporte aucune signature.

Pour en savoir plus sur les comparaisons, consultez la page [Réflexion](https://ai.google.dev/gemini-api/docs/thinking?hl=fr#signatures).
Pour les modèles Gemini 3 Image, consultez la section sur le processus de réflexion du guide [Génération d'images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#thinking-process).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/22 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/22 (UTC)."],[],[]]
