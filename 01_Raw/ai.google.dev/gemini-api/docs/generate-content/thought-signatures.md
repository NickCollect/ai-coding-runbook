---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=ja
fetched_at: 2026-06-29T05:36:37.208709+00:00
title: "Thought Signatures \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Thought Signatures

思考シグネチャは、モデルの内部的な思考プロセスを暗号化したもので、マルチステップのやり取りで推論コンテキストを維持するために使用されます。
思考モデル（Gemini 3 シリーズや 2.5 シリーズなど）を使用する場合、API は
`thoughtSignature` フィールドをレスポンスの[コンテンツ部分](https://ai.google.dev/api/caching?hl=ja#Part)
（`text` 部分や `functionCall` 部分など）に返すことがあります。

原則として、モデル レスポンスで思考シグネチャを受け取った場合は、次のターンで会話履歴を送信するときに、受け取ったとおりに返します。
**Gemini 3 モデルを使用する場合は、関数呼び出し中に思考シグネチャを返す必要があります。そうしないと、検証エラー** （4xx ステータス コード）が発生します。
これには、Gemini 3
Flash で `minimal`
[思考レベル](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#thinking-levels)の設定を使用する場合も含まれます。

## 仕組み

下の図は、Gemini API での
[関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)に関連する「ターン」と「ステップ」の意味を視覚化したものです。「ターン」とは、ユーザーとモデルの間の会話における 1 回の完全なやり取りのことです。「ステップ」とは、モデルが実行するより細かいアクションまたはオペレーションのことで、多くの場合、ターンを完了するための大きなプロセスの一部として実行されます。

![関数呼び出しのターンとステップの図](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=ja)

このドキュメントでは、Gemini 3 モデルの関数呼び出しの処理に焦点を当てています。 *2.5 との違いについては、[モデルの動作](#model-behavior)セクションをご覧ください。*

Gemini 3 は、関数呼び出しを含むすべてのモデル レスポンス（API からのレスポンス）に対して思考シグネチャを返します。思考シグネチャは、次の場合に表示されます。

- [並列関数呼び出しがある場合、モデル レスポンスから返される最初の関数呼び出し部分には思考シグネチャが含まれます。](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#parallel_function_calling)
- 関数呼び出しが連続している場合（マルチステップ）、各関数呼び出しにシグネチャがあり、すべてのシグネチャを返す必要があります。
- 関数呼び出しのないモデル レスポンスでは、モデルによって返される最後の部分に思考シグネチャを返します。

次の表は、マルチステップ関数呼び出しの視覚化を示しています。ターンとステップの定義と、前述のシグネチャの概念を組み合わせています。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ターン** | **ステップ** | **ユーザー リクエスト** | **モデルのレスポンス** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | なし |

## 関数呼び出し部分のシグネチャ

Gemini は `functionCall` を生成するときに、`thought_signature` を使用して次のターンでツールの出力を正しく処理します。

- **動作**:
  - **単一の関数呼び出し**: `functionCall` 部分に `thought_signature` が含まれます。
  - **並列関数呼び出し**: モデルがレスポンスで並列関数呼び出しを生成する場合、`thought_signature` は**最初の**
    `functionCall` 部分にのみ付加されます。同じレスポンス内の後続の `functionCall` 部分にはシグネチャは**含まれません** 。
- **要件**: 会話履歴を返す際は、このシグネチャを受け取った部分に正確に返す**必要があります**。
- **検証**: 現在のターン内のすべての関数呼び出しに対して厳格な検証が適用されます。（現在のターンのみが必要です。以前のターンでは検証されません）
  - API は履歴を遡って（最新から最古まで）、標準コンテンツ（`text` など）を含む最新の**ユーザー** メッセージ（現在のターンの開始）を検索します。これは `functionResponse` **be** 。
  - 特定のユーザー メッセージの後に発生する**すべての** モデル `functionCall` ターンは、ターンの一部と見なされます。
  - 現在のターンの**各ステップ** の**最初の** `functionCall` 部分には、その `thought_signature` を含める**必要があります** 。
  - 現在のターンの任意のステップの最初の `functionCall` 部分の `thought_signature` を省略すると、リクエストは 400 エラーで失敗します。
- **適切なシグネチャが返されない場合、エラーは次のように発生します**
  - Gemini 3 モデル: シグネチャを含めないと、400 エラーが発生します。文言は次の形式になります。
    - `<index of contents array>`
      コンテンツ ブロックの関数呼び出し `<Function Call>` に `thought_signature` がありません。例: *関数
      呼び出し `FC1` コンテンツ ブロックに `1.` がありません。*`thought_signature`

### 順次関数呼び出しの例

このセクションでは、ユーザーが複数のタスクを必要とする複雑な質問をした場合の、複数の関数呼び出しの例を示します。

ユーザーが複数のタスクを必要とする複雑な質問（`"Check flight status for AA100 and
book a taxi if delayed"`）をした場合の、マルチターン関数呼び出しの例を見てみましょう。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ターン** | **ステップ** | **ユーザー リクエスト** | **モデルのレスポンス** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

次のコードは、上の表のシーケンスを示しています。

**ターン 1、ステップ 1（ユーザー リクエスト）**

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

**ターン 1、ステップ 1（モデルのレスポンス）**

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

**ターン 1、ステップ 2（ユーザーのレスポンス - ツールの出力を送信）** このユーザーのターンには `functionResponse` のみ（新しいテキストなし）が含まれているため、まだターン 1 です。
は保持する必要があります。`<Signature_A>`

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

**ターン 1、ステップ 2（モデル）** モデルは、前のツールの出力に基づいてタクシーを予約することにしました。

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

**ターン 1、ステップ 3（ユーザー - ツールの出力を送信）** タクシーの予約確認を送信するには、このループ内の**すべての** 関数呼び出し（`<Signature A>` + `<Signature B>`）の署名を含める必要があります。

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

### 並列関数呼び出しの例

ユーザーが
`"Check weather in Paris and London"`と尋ねた場合の並列関数呼び出しの例を見て、モデルが検証を行う場所を確認しましょう。

| **ターン** | **ステップ** | **ユーザー リクエスト** | **モデルのレスポンス** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + signature  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  （FC なし） | なし |

次のコードは、上の表のシーケンスを示しています。

**ターン 1、ステップ 1（ユーザー リクエスト）**

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

**ターン 1、ステップ 1（モデルのレスポンス）**

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

**ターン 1、ステップ 2（ユーザーのレスポンス - ツールの出力を送信）** 最初の部分の
`<Signature_A>` は、受け取ったとおりに保持する必要があります。

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

## `functionCall` 以外のパーツのシグネチャ

関数呼び出し以外の部分のレスポンスの最後の部分に、`thought_signatures` が返されることもあります。

- **動作**: モデルから返される最終的なコンテンツ部分（`text, inlineData…`）に
  `thought_signature`が含まれることがあります。
- **推奨事項**: このシグネチャを返すことは、特に複雑な指示の実行やエージェント ワークフローのシミュレーションで、モデルが高品質の推論を維持するために**推奨** されます。
- **検証**: API は検証を厳密に適用**しません** 。省略してもブロッキング エラーは発生しませんが、パフォーマンスが低下する可能性があります。

### テキスト/インコンテキスト推論（検証なし）

**ターン 1、ステップ 1（モデルのレスポンス）**

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

**ターン 2、ステップ 1（ユーザー）**

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

## OpenAI の互換性のためのシグネチャ

次の例は、[OpenAI の互換性](https://ai.google.dev/gemini-api/docs/openai?hl=ja)を使用してチャット
補完 API の思考シグネチャを処理する方法を示しています。

### 順次関数呼び出しの例

これは、ユーザーが複数のタスクを必要とする複雑な質問をした場合の、複数の関数呼び出しの例です。

ユーザーが `Check flight status for AA100 and book a taxi if delayed` と尋ねた場合の、マルチターン関数呼び出しの例を見てみましょう。ユーザーが複数のタスクを必要とする複雑な質問をした場合に何が起こるかを確認できます。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ターン** | **ステップ** | **ユーザー リクエスト** | **モデルのレスポンス** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

次のコードは、指定されたシーケンスを示しています。

**ターン 1、ステップ 1（ユーザー リクエスト）**

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

**ターン 1、ステップ 1（モデルのレスポンス）**

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

**ターン 1、ステップ 2（ユーザーのレスポンス - ツールの出力を送信）**

このユーザーのターンには `functionResponse` のみ（新しいテキストなし）が含まれているため、まだターン 1 です。`<Signature_A>` は保持する必要があります。

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

**ターン 1、ステップ 2（モデル）**

モデルは、前のツールの出力に基づいてタクシーを予約することにしました。

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

**ターン 1、ステップ 3（ユーザー - ツールの出力を送信）**

タクシーの予約確認を送信するには、このループ内のすべての
関数呼び出し（`<Signature A>` + `<Signature B>`）の署名を含める必要があります。

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

### 並列関数呼び出しの例

ユーザーが
`"Check weather in Paris and London"`と尋ねた場合の並列関数呼び出しの例を見て、モデルが
検証を行う場所を確認しましょう。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ターン** | **ステップ** | **ユーザー リクエスト** | **モデルのレスポンス** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

指定されたシーケンスを示すコードは次のとおりです。

**ターン 1、ステップ 1（ユーザー リクエスト）**

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

**ターン 1、ステップ 1（モデルのレスポンス）**

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

**ターン 1、ステップ 2（ユーザーのレスポンス - ツールの出力を送信）**

最初の部分の `<Signature_A>` は、受け取ったとおりに保持する必要があります。

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

## よくある質問

1. **現在のターンとステップに関数呼び出し部分がある場合、別のモデルから Gemini 3 に履歴を転送するにはどうすればよいですか？API によって生成されなかったため、関連する
   思考シグネチャがない関数呼び出し
   部分を提供する必要があります。**

   カスタム関数呼び出しブロックをリクエストに挿入することは強く
   推奨されませんが、回避できない場合（クライアントによって決定的に実行された関数呼び出しとレスポンスに関する情報をモデルに提供する場合や、思考シグネチャを含まない別のモデルからトレースを転送する場合など）は、思考シグネチャ フィールドに `"context_engineering_is_the_way_to_go"` または
   `"skip_thought_signature_validator"` のダミー シグネチャを設定して、検証をスキップできます。
2. **並列関数呼び出しとレスポンスをインターリーブして返していますが、API から 400 が返されます。なぜでしょうか？**

   API が並列関数呼び出し「FC1 + signature, FC2」を返す場合、想定されるユーザー レスポンスは「FC1+ signature, FC2, FR1, FR2」です。「FC1 + signature, FR1, FC2, FR2」のようにインターリーブすると、API は 400 エラーを返します。
3. **ストリーミング中にモデルが関数呼び出しを返さない場合、
   思考シグネチャが見つかりません**

   ストリーミング リクエストで FC を含まないモデル レスポンスの場合、モデルはテキスト コンテンツ部分が空の部分に思考シグネチャを返すことがあります。モデルから `finish_reason` が返されるまで、リクエスト全体を解析することをおすすめします。

## モデルごとの思考シグネチャ

[Gemini 3 モデル](https://ai.google.dev/gemini-api/docs/models?hl=ja#gemini-3)と Gemini 2.5 モデル
では、関数呼び出しの思考シグネチャの動作が異なります。

- レスポンスに関数呼び出しがある場合、
  - Gemini 3 では、最初の関数呼び出し部分に常にシグネチャが含まれます。
    その部分を返すことは**必須** です。
  - Gemini 2.5 では、最初の部分にシグネチャが含まれます（タイプに関係なく）。その部分を返すことは**省略可能** です。
- レスポンスに関数呼び出しがない場合、
  - Gemini 3 では、モデルが思考を生成した場合、最後の部分にシグネチャが含まれます。
  - Gemini 2.5 では、どの部分にもシグネチャが含まれません。

比較の詳細については、[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#signatures)のページをご覧ください。Gemini 3 Image モデルについては、
[画像生成](https://ai.google.dev/gemini-api/docs/image-generation?hl=ja#thinking-process)ガイドの思考プロセス セクションをご覧ください。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-22 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-22 UTC。"],[],[]]
