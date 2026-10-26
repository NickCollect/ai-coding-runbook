---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=vi
fetched_at: 2026-10-26T05:55:29.499201+00:00
title: "Ch\u1eef k\u00fd suy ngh\u0129 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Chữ ký suy nghĩ

Chữ ký suy nghĩ là các bản trình bày được mã hoá về quy trình suy nghĩ nội bộ của mô hình và được dùng để duy trì bối cảnh suy luận trong các hoạt động tương tác nhiều bước.
Khi sử dụng các mô hình tư duy (chẳng hạn như dòng Gemini 4, 3 và 2.5), API có thể trả về trường `thoughtSignature` trong [các phần nội dung](https://ai.google.dev/api/caching?hl=vi#Part) của câu trả lời (ví dụ: các phần `text` hoặc `functionCall`).

Theo nguyên tắc chung, nếu nhận được chữ ký suy nghĩ trong câu trả lời của mô hình, bạn nên truyền lại chính xác chữ ký đó như khi nhận được khi gửi nhật ký trò chuyện ở lượt tiếp theo.
**Khi sử dụng các mô hình Gemini 4 và Gemini 3, bạn phải truyền lại chữ ký ý tưởng trong quá trình gọi hàm, nếu không bạn sẽ gặp lỗi xác thực** (mã trạng thái 4xx).
Điều này bao gồm cả khi bạn sử dụng chế độ cài đặt `minimal`
[mức độ tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#thinking-levels) cho Gemini 3
Flash.

## Cách hoạt động

Hình ảnh bên dưới minh hoạ ý nghĩa của "lượt" và "bước" liên quan đến [gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) trong Gemini API. Một "lượt" là một lần trao đổi hoàn chỉnh trong cuộc trò chuyện giữa người dùng và mô hình. "Bước" là một hành động hoặc thao tác chi tiết hơn do mô hình thực hiện, thường là một phần của quy trình lớn hơn để hoàn tất một lượt.

![Sơ đồ các bước và lượt gọi hàm](https://ai.google.dev/static/gemini-api/docs/images/fc-turns.png?hl=vi)

*Tài liệu này tập trung vào việc xử lý tính năng gọi hàm cho các mô hình Gemini 4 và Gemini 3. Hãy tham khảo
phần [hành vi của mô hình](#model-behavior) để biết những điểm khác biệt so với phiên bản 2.5.*

Gemini 4 và Gemini 3 trả về chữ ký suy nghĩ cho tất cả phản hồi của mô hình (phản hồi từ
API) bằng một lệnh gọi hàm. Chữ ký của suy nghĩ xuất hiện trong những trường hợp sau:

- Khi có các lệnh gọi [hàm song song](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#parallel_function_calling), phần lệnh gọi hàm đầu tiên do phản hồi của mô hình trả về sẽ có chữ ký suy nghĩ.
- Khi có các lệnh gọi hàm tuần tự (nhiều bước), mỗi lệnh gọi hàm sẽ có một chữ ký và bạn phải truyền tất cả chữ ký trở lại.
- Câu trả lời của mô hình không có lệnh gọi hàm sẽ trả về chữ ký suy nghĩ bên trong phần cuối cùng mà mô hình trả về.

Bảng sau đây minh hoạ các lệnh gọi hàm nhiều bước, kết hợp định nghĩa về lượt và bước với khái niệm về chữ ký được giới thiệu ở trên:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Lượt** | **Bước** | **Yêu cầu của người dùng** | **Câu trả lời của mô hình** | **FunctionResponse** |
| 1 | 1 | `request1 = user_prompt` | `FC1 + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + (FC1 + signature) + FR1` | `FC2 + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + (FC2 + signature) + FR2` | `text_output`  `(no FCs)` | Không có |

## Chữ ký trong các phần gọi hàm

Khi tạo `functionCall`, Gemini dựa vào `thought_signature` để xử lý chính xác kết quả của công cụ trong lượt tiếp theo.

- **Hành vi**:
  - **Single Function Call** (Lệnh gọi hàm đơn lẻ): Phần `functionCall` sẽ chứa một `thought_signature`.
  - **Lệnh gọi hàm song song**: Nếu mô hình tạo lệnh gọi hàm song song
    trong một phản hồi, thì `thought_signature` **chỉ được đính kèm vào**
    `functionCall` phần đầu tiên. Các phần `functionCall` tiếp theo trong cùng một phản hồi sẽ **không** chứa chữ ký.
- **Yêu cầu**: Bạn **phải** trả về chữ ký này ở đúng phần mà bạn nhận được chữ ký khi gửi lại nhật ký trò chuyện.
- **Xác thực**: Quy trình xác thực nghiêm ngặt được thực thi cho tất cả lệnh gọi hàm trong lượt hiện tại . (Chỉ cần lượt hiện tại; chúng tôi không xác thực các lượt trước)
  - API này sẽ quay lại nhật ký (từ mới nhất đến cũ nhất) để tìm thông báo **Người dùng** gần đây nhất có chứa nội dung tiêu chuẩn (ví dụ: `text`) ( đây sẽ là điểm bắt đầu của lượt hiện tại). Đây sẽ không **be** là `functionResponse`.
  - Mọi lượt **Tất cả** mô hình `functionCall` diễn ra sau thông báo sử dụng cụ thể đó đều được coi là một phần của lượt.
  - Phần **đầu tiên** của `functionCall` trong **mỗi bước** của lượt hiện tại **phải** bao gồm `thought_signature`.
  - Nếu bạn bỏ qua `thought_signature` cho phần `functionCall` đầu tiên trong bất kỳ bước nào của lượt hiện tại, thì yêu cầu sẽ không thành công và trả về lỗi 400.
- **Nếu không trả về chữ ký thích hợp, bạn sẽ gặp lỗi theo cách sau**
  - Các mô hình Gemini 3: Nếu không có chữ ký, bạn sẽ gặp lỗi 400. Nội dung sẽ có dạng như sau:
    - Lệnh gọi hàm `<Function Call>` trong khối nội dung `<index of contents array>` bị thiếu `thought_signature`. Ví dụ: *Lệnh gọi hàm `FC1` trong khối nội dung `1.` bị thiếu `thought_signature`.*

### Ví dụ về gọi hàm tuần tự

Phần này trình bày ví dụ về nhiều lệnh gọi hàm, trong đó người dùng đặt một câu hỏi phức tạp cần nhiều tác vụ.

Hãy cùng xem một ví dụ về lệnh gọi hàm nhiều lượt, trong đó người dùng đặt một câu hỏi phức tạp cần nhiều tác vụ: `"Check flight status for AA100 and
book a taxi if delayed"`.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Bật** | **Bước** | **Yêu cầu của người dùng** | **Câu trả lời của mô hình** | **FunctionResponse** |
| 1 | 1 | `request1="Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Đoạn mã sau đây minh hoạ trình tự trong bảng trên.

**Lượt 1, Bước 1 (Yêu cầu của người dùng)**

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

**Lượt 1, Bước 1 (Câu trả lời của mô hình)**

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

**Lượt 1, Bước 2 (Phản hồi của người dùng – Gửi kết quả của công cụ)** Vì lượt này của người dùng chỉ chứa một `functionResponse` (không có văn bản mới), nên chúng ta vẫn đang ở Lượt 1. Chúng ta phải bảo tồn `<Signature_A>`.

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

**Lượt 1, Bước 2 (Mô hình)** Mô hình hiện quyết định đặt taxi dựa trên kết quả đầu ra của công cụ trước đó.

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

**Lượt 1, Bước 3 (Người dùng – Gửi kết quả của công cụ)** Để gửi thông tin xác nhận đặt taxi, chúng ta phải thêm chữ ký cho **TẤT CẢ** lệnh gọi hàm trong vòng lặp này (`<Signature A>` + `<Signature B>`).

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

### Ví dụ về lệnh gọi hàm song song

Hãy cùng xem một ví dụ về lệnh gọi hàm song song, trong đó người dùng yêu cầu
`"Check weather in Paris and London"` để xem mô hình thực hiện quy trình xác thực ở đâu.

| **Lượt** | **Bước** | **Yêu cầu của người dùng** | **Câu trả lời của mô hình** | **FunctionResponse** |
| --- | --- | --- | --- | --- |
| 1 | 1 | `request1="Check the weather in Paris and London"` | FC1 ("Paris") + chữ ký  FC2 ("London") | FR1 |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | text\_output  (không có FC) | Không có |

Đoạn mã sau đây minh hoạ trình tự trong bảng trên.

**Lượt 1, Bước 1 (Yêu cầu của người dùng)**

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

**Lượt 1, Bước 1 (Câu trả lời của mô hình)**

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

**Lượt 1, Bước 2 (Phản hồi của người dùng – Gửi đầu ra của công cụ)** Chúng ta phải giữ nguyên `<Signature_A>` ở phần đầu tiên đúng như đã nhận.

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

## Chữ ký trong các phần không phải `functionCall`

Gemini cũng có thể trả về `thought_signatures` trong phần cuối của câu trả lời
trong các phần không phải lệnh gọi hàm.

- **Hành vi**: Phần nội dung cuối cùng (`text, inlineData…`) do mô hình trả về có thể chứa `thought_signature`.
- **Đề xuất**: Bạn **nên** trả về các chữ ký này để đảm bảo mô hình duy trì khả năng suy luận chất lượng cao, đặc biệt là đối với các quy trình làm việc phức tạp theo hướng dẫn hoặc quy trình làm việc mô phỏng của tác nhân.
- **Xác thực**: API **không** thực thi nghiêm ngặt quy trình xác thực. Bạn sẽ không nhận được lỗi chặn nếu bỏ qua các chỉ số này, mặc dù hiệu suất có thể giảm.

### Văn bản/Lý luận theo ngữ cảnh (Không xác thực)

**Lượt 1, Bước 1 (Câu trả lời của mô hình)**

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

**Lượt 2, Bước 1 (Người dùng)**

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

## Chữ ký cho khả năng tương thích với OpenAI

Các ví dụ sau đây cho thấy cách xử lý chữ ký suy nghĩ cho một API hoàn thành cuộc trò chuyện bằng cách sử dụng [khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi).

### Ví dụ về việc gọi hàm tuần tự

Đây là ví dụ về việc gọi nhiều hàm khi người dùng đặt một câu hỏi phức tạp, đòi hỏi phải thực hiện nhiều nhiệm vụ.

Hãy cùng xem một ví dụ về lệnh gọi hàm nhiều lượt, trong đó người dùng hỏi
`Check flight status for AA100 and book a taxi if delayed` và bạn có thể thấy điều gì
xảy ra khi người dùng đặt một câu hỏi phức tạp cần nhiều tác vụ.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Turn** | **Bước** | **Yêu cầu của người dùng** | **Câu trả lời của mô hình** | **FunctionResponse** |
| 1 | 1 | `request1 = "Check flight status for AA100 and book a taxi 2 hours before if delayed."` | `FC1 ("check_flight") + signature` | `FR1` |
| 1 | 2 | `request2 = request1 + FC1 ("check_flight") + signature + FR1` | `FC2("book_taxi") + signature` | `FR2` |
| 1 | 3 | `request3 = request2 + FC2 ("book_taxi") + signature + FR2` | `text_output`  `(no FCs)` | `None` |

Đoạn mã sau đây sẽ thực hiện trình tự đã cho.

**Lượt 1, Bước 1 (Yêu cầu của người dùng)**

```
{
  "model": "google/gemini-4-argon",
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

**Lượt 1, Bước 1 (Câu trả lời của mô hình)**

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

**Lượt 1, Bước 2 (Phản hồi của người dùng – Gửi kết quả của công cụ)**

Vì lượt này của người dùng chỉ chứa `functionResponse` (không có văn bản mới), nên chúng ta vẫn đang ở Lượt 1 và phải giữ nguyên `<Signature_A>`.

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

**Lượt 1, Bước 2 (Mô hình)**

Giờ đây, mô hình quyết định đặt taxi dựa trên kết quả đầu ra trước đó của công cụ.

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

**Lượt 1, Bước 3 (Người dùng – Gửi kết quả của công cụ)**

Để gửi thông báo xác nhận đặt xe taxi, chúng ta phải thêm chữ ký cho TẤT CẢ các lệnh gọi hàm trong vòng lặp này (`<Signature A>` + `<Signature B>`).

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

### Ví dụ về lệnh gọi hàm song song

Hãy cùng xem một ví dụ về lệnh gọi hàm song song, trong đó người dùng hỏi `"Check weather in Paris and London"` và bạn có thể thấy mô hình thực hiện quy trình xác thực ở đâu.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Bật** | **Bước** | **Yêu cầu của người dùng** | **Câu trả lời của mô hình** | **FunctionResponse** |
| 1 | 1 | `request1="Check the weather in Paris and London"` | `FC1 ("Paris") + signature`  `FC2 ("London")` | `FR1` |
| 1 | 2 | `request 2 = request1 + FC1 ("Paris") + signature + FC2 ("London")` | `text_output`  `(no FCs)` | `None` |

Sau đây là mã để duyệt qua chuỗi đã cho.

**Lượt 1, Bước 1 (Yêu cầu của người dùng)**

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

**Lượt 1, Bước 1 (Câu trả lời của mô hình)**

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

**Lượt 1, Bước 2 (Phản hồi của người dùng – Gửi kết quả của công cụ)**

Bạn phải giữ nguyên `<Signature_A>` ở phần đầu tiên đúng như khi nhận được.

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

## Câu hỏi thường gặp

1. **Làm cách nào để chuyển nhật ký từ một mô hình khác sang Gemini 4 hoặc Gemini 3 bằng một
   phần gọi hàm trong lượt và bước hiện tại? Tôi cần cung cấp các phần gọi hàm không phải do API tạo ra và do đó không có chữ ký suy nghĩ liên kết?**

   Mặc dù bạn không nên chèn các khối lệnh gọi hàm tuỳ chỉnh vào yêu cầu, nhưng trong trường hợp không thể tránh khỏi, chẳng hạn như cung cấp thông tin cho mô hình về các lệnh gọi hàm và phản hồi được ứng dụng thực thi một cách tất định, hoặc chuyển dấu vết từ một mô hình khác không bao gồm chữ ký suy nghĩ, bạn có thể đặt các chữ ký giả sau đây là `"context_engineering_is_the_way_to_go"` hoặc `"skip_thought_signature_validator"` trong trường chữ ký suy nghĩ để bỏ qua bước xác thực.
2. **Tôi đang gửi lại các lệnh gọi hàm song song và phản hồi xen kẽ và API đang trả về mã lỗi 400. Vì sao lại như vậy?**

   Khi API trả về các lệnh gọi hàm song song "FC1 + chữ ký, FC2", phản hồi dự kiến của người dùng là "FC1 + chữ ký, FC2, FR1, FR2". Nếu bạn có các khoá này xen kẽ với nhau dưới dạng "FC1 + chữ ký, FR1, FC2, FR2", thì API sẽ trả về lỗi 400.
3. **Khi truyền trực tuyến và mô hình không trả về lệnh gọi hàm, tôi không tìm thấy chữ ký suy nghĩ**

   Trong một phản hồi của mô hình không chứa lệnh gọi hàm có yêu cầu truyền trực tuyến, mô hình có thể trả về chữ ký suy nghĩ trong một phần có nội dung văn bản trống. Bạn nên phân tích cú pháp toàn bộ yêu cầu cho đến khi mô hình trả về `finish_reason`.

## Chữ ký suy nghĩ cho các mô hình khác nhau

Các mô hình [Gemini 4](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=vi), [Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-3) và Gemini 2.5 có hành vi khác nhau đối với chữ ký tư duy trong các lệnh gọi hàm:

- Nếu có lệnh gọi hàm trong một phản hồi,
  - Gemini 4 và Gemini 3 sẽ luôn có chữ ký trong phần gọi hàm đầu tiên.
    Bạn **bắt buộc** phải trả lại bộ phận đó.
  - Gemini 2.5 sẽ có chữ ký ở phần đầu tiên (bất kể loại). Bạn **không bắt buộc** phải trả lại phần đó.
- Nếu không có lệnh gọi hàm nào trong phản hồi, hãy làm như sau:
  - Gemini 4 và Gemini 3 sẽ có chữ ký ở phần cuối nếu mô hình tạo ra một suy nghĩ.
  - Gemini 2.5 sẽ không có chữ ký ở bất kỳ phần nào.

Hãy tham khảo trang [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#signatures) để biết thêm thông tin chi tiết về việc so sánh.
Đối với các mô hình Gemini 3 Image, hãy xem phần quy trình tư duy trong hướng dẫn về tính năng [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#thinking-process).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
