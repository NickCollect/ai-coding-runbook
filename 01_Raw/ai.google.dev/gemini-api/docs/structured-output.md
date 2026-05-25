---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=vi
fetched_at: 2026-05-25T05:17:49.484159+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Kết quả có cấu trúc

Bạn có thể định cấu hình các mô hình Gemini để tạo câu trả lời tuân thủ một JSON Schema được cung cấp. Điều này đảm bảo kết quả có thể dự đoán và an toàn về kiểu, đồng thời đơn giản hoá việc trích xuất dữ liệu có cấu trúc từ văn bản không có cấu trúc.

Sử dụng đầu ra có cấu trúc là lựa chọn lý tưởng cho:

- **Trích xuất dữ liệu:** Lấy thông tin cụ thể như tên và ngày tháng từ văn bản.
- **Phân loại có cấu trúc:** Phân loại văn bản thành các danh mục được xác định trước.
- **Quy trình công việc dựa trên tác nhân:** Tạo thông tin đầu vào có cấu trúc cho các công cụ hoặc API.

Ngoài việc hỗ trợ Giản đồ JSON trong API REST, Google GenAI SDK còn giúp bạn dễ dàng xác định giản đồ bằng [Pydantic](https://docs.pydantic.dev/latest/) (Python) và [Zod](https://zod.dev/) (JavaScript).

Recipe Extractor
Content Moderation
Recursive Structures

Ví dụ này minh hoạ cách trích xuất dữ liệu có cấu trúc từ văn bản bằng các loại Giản đồ JSON cơ bản như `object`, `array`, `string` và `integer`.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Recipe.model_json_schema()}},
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(recipeSchema) } },
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please extract the recipe from the following text.
  The user wants to make delicious chocolate chip cookies.
  They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
  1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
  3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
  For the best part, they'll need 2 cups of semisweet chocolate chips.
  First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
  baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
  until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
  ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
  onto ungreased baking sheets and bake for 9 to 11 minutes.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "recipe_name": map[string]any{
                    "type":        "string",
                    "description": "The name of the recipe.",
                },
                "prep_time_minutes": map[string]any{
                    "type":        "integer",
                    "description": "Optional time in minutes to prepare the recipe.",
                },
                "ingredients": map[string]any{
                    "type": "array",
                    "items": map[string]any{
                        "type": "object",
                        "properties": map[string]any{
                            "name": map[string]any{
                                "type":        "string",
                                "description": "Name of the ingredient.",
                            },
                            "quantity": map[string]any{
                                "type":        "string",
                                "description": "Quantity of the ingredient, including units.",
                            },
                        },
                        "required": []string{"name", "quantity"},
                    },
                },
                "instructions": map[string]any{
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
        ]
      }],
      "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
          }
        }
      },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
    }'
```

**Ví dụ về câu trả lời:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    {
      "name": "all-purpose flour",
      "quantity": "2 and 1/4 cups"
    },
    {
      "name": "baking soda",
      "quantity": "1 teaspoon"
    },
    {
      "name": "salt",
      "quantity": "1 teaspoon"
    },
    {
      "name": "unsalted butter (softened)",
      "quantity": "1 cup"
    },
    {
      "name": "granulated sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "packed brown sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "vanilla extract",
      "quantity": "1 teaspoon"
    },
    {
      "name": "large eggs",
      "quantity": "2"
    },
    {
      "name": "semisweet chocolate chips",
      "quantity": "2 cups"
    }
  ],
  "instructions": [
    "Preheat the oven to 375°F (190°C).",
    "In a small bowl, whisk together the flour, baking soda, and salt.",
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
    "Beat in the vanilla and eggs, one at a time.",
    "Gradually beat in the dry ingredients until just combined.",
    "Stir in the chocolate chips.",
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
  ]
}
```

## Phát trực tiếp

Bạn có thể truyền trực tuyến các đầu ra có cấu trúc, cho phép bạn bắt đầu xử lý phản hồi khi phản hồi đang được tạo mà không cần phải đợi toàn bộ đầu ra hoàn tất. Điều này có thể cải thiện hiệu suất cảm nhận của ứng dụng.

Các khối được truyền trực tuyến sẽ là các chuỗi JSON hợp lệ một phần, có thể được nối để tạo thành đối tượng JSON hoàn chỉnh cuối cùng.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents=prompt,
    config={
        "response_format": {"text": {"mime_type": "application/json", "schema": Feedback.model_json_schema()}},
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
  sentiment: z.enum(["positive", "neutral", "negative"]),
  summary: z.string(),
});

const stream = await ai.models.generateContentStream({
  model: "gemini-3.5-flash",
  contents: prompt,
  config: {
    responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(feedbackSchema) } },
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## Đầu ra có cấu trúc bằng các công cụ

Gemini 3 cho phép bạn kết hợp Đầu ra có cấu trúc với các công cụ tích hợp, bao gồm [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi), [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi), [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi), [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi#structured-output) và [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_format": {"text": {"mime_type": "application/json", "schema": MatchResult.model_json_schema()}},
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseFormat: { text: { mimeType: "application/json", schema: zodToJsonSchema(matchSchema) } },
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseFormat": {
          "text": {
            "mimeType": "application/json",
            "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
          }
        }
      },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

## Hỗ trợ giản đồ JSON

Để tạo một đối tượng JSON, hãy đặt `response_format` trong cấu hình tạo. Giản đồ phải là một [Giản đồ JSON](https://json-schema.org/) hợp lệ mô tả định dạng đầu ra mong muốn.

Sau đó, mô hình sẽ tạo một phản hồi là chuỗi JSON hợp lệ về mặt cú pháp, khớp với giản đồ được cung cấp. Khi sử dụng dữ liệu đầu ra có cấu trúc, mô hình sẽ tạo ra dữ liệu đầu ra theo cùng thứ tự với các khoá trong giản đồ.

Chế độ đầu ra có cấu trúc của Gemini hỗ trợ một phần của quy cách [Giản đồ JSON](https://json-schema.org).

Sau đây là các giá trị được hỗ trợ của `type`:

- **`string`**: Đối với văn bản.
- **`number`**: Đối với số dấu phẩy động.
- **`integer`**: Đối với số nguyên.
- **`boolean`**: Đối với giá trị đúng/sai.
- **`object`**: Đối với dữ liệu có cấu trúc có các cặp khoá-giá trị.
- **`array`**: Đối với danh sách các mục.
- **`null`**: Để cho phép một thuộc tính có giá trị rỗng, hãy thêm `"null"` vào mảng loại (ví dụ: `{"type": ["string", "null"]}`).

Những thuộc tính mô tả này giúp hướng dẫn mô hình:

- **`title`**: Nội dung mô tả ngắn về một tài sản.
- **`description`**: Nội dung mô tả dài hơn và chi tiết hơn về một cơ sở lưu trú.

### Thuộc tính cụ thể theo loại

**Đối với các giá trị `object`:**

- **`properties`**: Một đối tượng trong đó mỗi khoá là tên thuộc tính và mỗi giá trị là một giản đồ cho thuộc tính đó.
- **`required`**: Một mảng gồm các chuỗi, liệt kê những thuộc tính bắt buộc.
- **`additionalProperties`**: Kiểm soát việc có cho phép các thuộc tính không có trong `properties` hay không. Có thể là một boolean hoặc một giản đồ.

**Đối với các giá trị `string`:**

- **`enum`**: Liệt kê một tập hợp cụ thể gồm các chuỗi có thể có cho các tác vụ phân loại.
- **`format`**: Chỉ định cú pháp cho chuỗi, chẳng hạn như `date-time`, `date`, `time`.

**Đối với các giá trị `number` và `integer`:**

- **`enum`**: Liệt kê một tập hợp cụ thể gồm các giá trị bằng số có thể có.
- **`minimum`**: Giá trị tối thiểu bao gồm.
- **`maximum`**: Giá trị tối đa (bao gồm).

**Đối với các giá trị `array`:**

- **`items`**: Xác định giản đồ cho tất cả các mục trong mảng.
- **`prefixItems`**: Xác định danh sách giản đồ cho N mục đầu tiên, cho phép các cấu trúc giống như bộ giá trị.
- **`minItems`**: Số lượng tối thiểu của các mục trong mảng.
- **`maxItems`**: Số lượng tối đa của các mục trong mảng.

## Hỗ trợ mô hình

Các mô hình sau đây hỗ trợ đầu ra có cấu trúc:

| Mô hình | Đầu ra có cấu trúc |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Bản xem trước Gemini 3.1 Pro | ✔️ |
| Gemini 3.5 Flash | ✔️ |
| Bản xem trước Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* Xin lưu ý rằng Gemini 2.0 yêu cầu danh sách `propertyOrdering` rõ ràng trong dữ liệu đầu vào JSON để xác định cấu trúc ưu tiên. Bạn có thể xem ví dụ trong [sổ tay này](https://github.com/google-gemini/cookbook/blob/main/examples/Pdf_structured_outputs_on_invoices_and_forms.ipynb).*

## Đầu ra có cấu trúc so với gọi hàm

Cả đầu ra có cấu trúc và lệnh gọi hàm đều sử dụng giản đồ JSON, nhưng chúng phục vụ các mục đích khác nhau:

| Tính năng | Trường hợp sử dụng chính |
| --- | --- |
| **Đầu ra có cấu trúc** | **Định dạng phản hồi cuối cùng cho người dùng.** Hãy sử dụng tham số này khi bạn muốn *câu trả lời* của mô hình ở một định dạng cụ thể (ví dụ: trích xuất dữ liệu từ một tài liệu để lưu vào cơ sở dữ liệu). |
| **Lệnh gọi hàm** | **Thực hiện hành động trong cuộc trò chuyện.** Hãy sử dụng chức năng này khi mô hình cần *hỏi bạn* thực hiện một việc (ví dụ: "xem thời tiết hiện tại") trước khi có thể đưa ra câu trả lời cuối cùng. |

## Các phương pháp hay nhất

- **Nội dung mô tả rõ ràng:** Sử dụng trường `description` trong giản đồ để cung cấp hướng dẫn rõ ràng cho mô hình về ý nghĩa của từng thuộc tính. Điều này rất quan trọng để hướng dẫn đầu ra của mô hình.
- **Nhập mạnh:** Sử dụng các loại cụ thể (`integer`, `string`, `enum`) bất cứ khi nào có thể. Nếu một tham số có một tập hợp giới hạn các giá trị hợp lệ, hãy sử dụng `enum`.
- **Thiết kế câu lệnh:** Nêu rõ trong câu lệnh những gì bạn muốn mô hình thực hiện. Ví dụ: "Trích xuất thông tin sau đây từ văn bản..." hoặc "Phân loại ý kiến phản hồi này theo giản đồ được cung cấp...".
- **Xác thực:** Mặc dù đầu ra có cấu trúc đảm bảo JSON chính xác về mặt cú pháp, nhưng không đảm bảo các giá trị chính xác về mặt ngữ nghĩa. Luôn xác thực đầu ra cuối cùng trong mã xử lý ứng dụng trước khi sử dụng.
- **Xử lý lỗi:** Triển khai quy trình xử lý lỗi mạnh mẽ trong ứng dụng của bạn để quản lý một cách thích hợp các trường hợp mà đầu ra của mô hình, mặc dù tuân thủ giản đồ, nhưng có thể không đáp ứng các yêu cầu về logic nghiệp vụ của bạn.

## Các điểm hạn chế

- **Tập hợp con của giản đồ:** Không phải tất cả các tính năng của quy cách Giản đồ JSON đều được hỗ trợ. Mô hình này bỏ qua các thuộc tính không được hỗ trợ.
- **Độ phức tạp của giản đồ:** API có thể từ chối các giản đồ quá lớn hoặc được lồng sâu. Nếu bạn gặp lỗi, hãy thử đơn giản hoá giản đồ bằng cách rút ngắn tên thuộc tính, giảm số lượng lớp lồng nhau hoặc giới hạn số lượng ràng buộc.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
