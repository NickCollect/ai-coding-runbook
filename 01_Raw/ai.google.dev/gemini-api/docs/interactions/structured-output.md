---
source_url: https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=vi
fetched_at: 2026-05-11T04:57:21.191275+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Kết quả có cấu trúc

Bạn có thể định cấu hình các mô hình Gemini để tạo câu trả lời tuân thủ một JSON Schema được cung cấp. Điều này đảm bảo kết quả có thể dự đoán và an toàn về kiểu, đồng thời đơn giản hoá việc trích xuất dữ liệu có cấu trúc từ văn bản không có cấu trúc.

Sử dụng đầu ra có cấu trúc là lựa chọn lý tưởng cho:

- **Trích xuất dữ liệu:** Lấy thông tin cụ thể như tên và ngày tháng từ văn bản.
- **Phân loại có cấu trúc:** Phân loại văn bản thành các danh mục được xác định trước.
- **Quy trình công việc dựa trên tác nhân:** Tạo thông tin đầu vào có cấu trúc cho các công cụ hoặc API.

Ngoài việc hỗ trợ JSON Schema trong API REST, Google GenAI SDK còn cho phép xác định giản đồ bằng [Pydantic](https://docs.pydantic.dev/latest/) (Python) và [Zod](https://zod.dev/) (JavaScript).

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.steps[-1].content[0].text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: {
      type: "string",
      description: "The name of the recipe."
    },
    prep_time_minutes: {
        type: "integer",
        description: "Optional time in minutes to prepare the recipe."
    },
    ingredients: {
      type: "array",
      items: {
        type: "object",
        properties: {
          name: { type: "string", description: "Name of the ingredient."},
          quantity: { type: "string", description: "Quantity of the ingredient, including units."}
        },
        required: ["name", "quantity"]
      }
    },
    instructions: {
      type: "array",
      items: { type: "string" }
    }
  },
  required: ["recipe_name", "ingredients", "instructions"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const client = new GoogleGenAI({});

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

const interaction = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: prompt,
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(recipe);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3-flash-preview",
      "input": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes.",
      "response_format": {
        "type": "text",
        "mime_type": "application/json",
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
      }
    }'
```

**Ví dụ về câu trả lời:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    { "name": "all-purpose flour", "quantity": "2 and 1/4 cups" },
    { "name": "baking soda", "quantity": "1 teaspoon" },
    { "name": "salt", "quantity": "1 teaspoon" },
    { "name": "unsalted butter (softened)", "quantity": "1 cup" },
    { "name": "granulated sugar", "quantity": "3/4 cup" },
    { "name": "packed brown sugar", "quantity": "3/4 cup" },
    { "name": "vanilla extract", "quantity": "1 teaspoon" },
    { "name": "large eggs", "quantity": "2" },
    { "name": "semisweet chocolate chips", "quantity": "2 cups" }
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

## Kết quả phát trực tuyến

Bạn có thể truyền trực tuyến các đầu ra có cấu trúc, cho phép bạn bắt đầu xử lý phản hồi khi phản hồi đang được tạo. Các khối được truyền trực tuyến là các chuỗi JSON hợp lệ một phần có thể được nối để tạo thành đối tượng JSON cuối cùng.

### Python

```
from google import genai
from pydantic import BaseModel
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive. Add a very long summary to test streaming!"

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input=prompt,
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Feedback.model_json_schema()
    },
    stream=True
)
for event in stream:
    if event.event_type == "step.delta" and event.delta.text:
        print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const feedbackJsonSchema = {
  type: "object",
  properties: {
    sentiment: { type: "string", enum: ["positive", "neutral", "negative"] },
    summary: { type: "string" }
  },
  required: ["sentiment", "summary"]
};

const feedbackSchema = z.fromJSONSchema(feedbackJsonSchema);

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
  model: "gemini-3-flash-preview",
  input: "The new UI is incredibly intuitive. Add a very long summary!",
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: feedbackJsonSchema
  },
  stream: true,
});

for await (const event of stream) {
  if (event.type === "step.delta" && event.delta?.text) {
    process.stdout.write(event.delta.text);
  }
}
```

## Đầu ra có cấu trúc bằng các công cụ

Gemini 3 cho phép bạn kết hợp Đầu ra có cấu trúc với các công cụ tích hợp, bao gồm [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=vi), [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=vi), [Thực thi mã](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=vi), [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=vi#structured-output) và [Gọi hàm](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi).

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

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[{"type": "google_search"}, {"type": "url_context"}],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.steps[-1].content[0].text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string" },
    final_match_score: { type: "string" },
    scorers: { type: "array", items: { type: "string" } }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: "gemini-3.1-pro-preview",
  input: "Search for all details for the latest Euro.",
  tools: [{type: "google_search"}, {type: "url_context"}],
  response_format: {
    type: 'text',
    mime_type: 'application/json',
    schema: matchJsonSchema
  },
});

const match = matchSchema.parse(JSON.parse(interaction.steps.at(-1).content[0].text));
console.log(match);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [{"type": "google_search"}, {"type": "url_context"}],
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
            "winner": {"type": "string"},
            "final_match_score": {"type": "string"},
            "scorers": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["winner", "final_match_score", "scorers"]
      }
    }
  }'
```

## Hỗ trợ giản đồ JSON

Để tạo một đối tượng JSON, hãy định cấu hình `response_format` bằng một đối tượng (hoặc một mảng chứa một đối tượng) thuộc loại `text` và đặt `mime_type` của đối tượng đó thành `application/json`. Bạn nên cung cấp giản đồ trong trường `schema`.

Chế độ đầu ra có cấu trúc của Gemini hỗ trợ một phần của quy cách [Giản đồ JSON](https://json-schema.org/).

Sau đây là các giá trị được hỗ trợ của `type`:

- **`string`**: Đối với văn bản.
- **`number`**: Đối với số dấu phẩy động.
- **`integer`**: Đối với số nguyên.
- **`boolean`**: Đối với giá trị đúng hoặc sai.
- **`object`**: Đối với dữ liệu có cấu trúc có các cặp khoá-giá trị.
- **`array`**: Đối với danh sách các mục.
- **`null`**: Để cho phép một thuộc tính có giá trị rỗng, hãy thêm `"null"` vào mảng loại (ví dụ: `{"type": ["string", "null"]}`).

Những thuộc tính mô tả này giúp hướng dẫn mô hình:

- **`title`**: Nội dung mô tả ngắn về một tài sản.
- **`description`**: Nội dung mô tả dài và chi tiết hơn về một cơ sở lưu trú.

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

| Mô hình | Đầu ra có cấu trúc |
| --- | --- |
| Bản xem trước Gemini 3.1 Pro | ✔️ |
| Bản xem trước Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* Gemini 2.0 yêu cầu danh sách `propertyOrdering` rõ ràng.*

## Đầu ra có cấu trúc so với gọi hàm

| Tính năng | Trường hợp sử dụng chính |
| --- | --- |
| **Đầu ra có cấu trúc** | **Định dạng câu trả lời cuối cùng.** Sử dụng khi bạn muốn *câu trả lời* của mô hình ở một định dạng cụ thể. |
| **Lệnh gọi hàm** | **Thực hiện hành động trong cuộc trò chuyện.** Sử dụng khi mô hình cần *hỏi bạn* thực hiện một việc trước khi đưa ra câu trả lời cuối cùng. |

## Các phương pháp hay nhất

- **Nội dung mô tả rõ ràng:** Sử dụng trường `description` để hướng dẫn mô hình.
- **Nhập mạnh:** Sử dụng các loại cụ thể (`integer`, `string`, `enum`).
- **Thiết kế câu lệnh:** Nêu rõ bạn muốn mô hình làm gì.
- **Xác thực:** Mặc dù đầu ra là JSON có cú pháp chính xác, nhưng bạn luôn phải xác thực các giá trị trong ứng dụng của mình.
- **Xử lý lỗi:** Triển khai biện pháp xử lý lỗi hữu ích cho các đầu ra tuân thủ giản đồ nhưng không chính xác về mặt ngữ nghĩa.

## Các điểm hạn chế

- **Tập hợp con giản đồ:** Không phải tính năng nào của Giản đồ JSON cũng được hỗ trợ.
- **Độ phức tạp của giản đồ:** Những giản đồ quá lớn hoặc có cấu trúc lồng ghép sâu có thể bị từ chối.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-09 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-09 UTC."],[],[]]
