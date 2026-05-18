---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=vi
fetched_at: 2026-05-18T05:13:30.472577+00:00
title: "B\u1eaft \u0111\u1ea7u nhanh API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bắt đầu nhanh API Gemini

Hướng dẫn bắt đầu nhanh này cho bạn biết cách cài đặt [các thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) của chúng tôi và thực hiện yêu cầu API đầu tiên đối với Gemini API.

## Trước khi bắt đầu

Để sử dụng Gemini API, bạn cần có một khoá API để xác thực các yêu cầu, thực thi giới hạn bảo mật và theo dõi mức sử dụng cho tài khoản của bạn.

Tạo một dự án trên AI Studio miễn phí để bắt đầu:

[Tạo khoá Gemini API](https://aistudio.google.com/app/apikey?hl=vi)

## Cài đặt Google GenAI SDK

### Python

Khi dùng [Python 3.9 trở lên](https://www.python.org/downloads/), hãy cài đặt gói [`google-genai`](https://pypi.org/project/google-genai/) bằng [lệnh pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) sau:

```
pip install -q -U google-genai
```

### JavaScript

Sử dụng [Node.js phiên bản 18 trở lên](https://nodejs.org/en/download/package-manager), hãy cài đặt [Google Gen AI SDK cho TypeScript và JavaScript](https://www.npmjs.com/package/@google/genai) bằng [lệnh npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) sau:

```
npm install @google/genai
```

### Go

Cài đặt [google.golang.org/genai](https://pkg.go.dev/google.golang.org/genai) trong thư mục mô-đun bằng [lệnh go get](https://go.dev/doc/code):

```
go get google.golang.org/genai
```

### Java

Nếu đang sử dụng Maven, bạn có thể cài đặt [google-genai](https://github.com/googleapis/java-genai) bằng cách thêm nội dung sau vào các phần phụ thuộc:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

Cài đặt [googleapis/go-genai](https://googleapis.github.io/dotnet-genai/) trong thư mục mô-đun bằng [lệnh dotnet add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add)

```
dotnet add package Google.GenAI
```

### Apps Script

1. Để tạo một dự án Apps Script mới, hãy truy cập vào [script.new](https://script.google.com/u/0/home/projects/create?hl=vi).
2. Nhấp vào **Dự án chưa có tiêu đề**.
3. Đổi tên dự án Apps Script thành **AI Studio** rồi nhấp vào **Rename** (Đổi tên).
4. Đặt [khoá API](https://developers.google.com/apps-script/guides/properties?hl=vi#manage_script_properties_manually)
   1. Ở bên trái, hãy nhấp vào **Cài đặt dự án** ![Biểu tượng cho chế độ cài đặt dự án](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg).
   2. Trong phần **Script Properties** (Thuộc tính tập lệnh), hãy nhấp vào **Add script property** (Thêm thuộc tính tập lệnh).
   3. Đối với **Thuộc tính**, hãy nhập tên khoá: `GEMINI_API_KEY`.
   4. Đối với **Giá trị**, hãy nhập giá trị cho khoá API.
   5. Nhấp vào **Lưu thuộc tính của tập lệnh**.
5. Thay thế nội dung tệp `Code.gs` bằng đoạn mã sau:

## Tạo yêu cầu đầu tiên

Bạn có thể dùng 2 cách để gửi yêu cầu đến Gemini API:

- ***(Nên dùng)*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=vi) là một nguyên tắc cơ bản mới có hỗ trợ gốc cho việc sử dụng công cụ nhiều bước, điều phối và các luồng suy luận phức tạp thông qua các bước thực thi được nhập. Trong tương lai, các mô hình mới ngoài dòng sản phẩm cốt lõi, cùng với các công cụ và khả năng của tác nhân AI mới, sẽ chỉ ra mắt trên Interactions API.
- [`generateContent`](https://ai.google.dev/api/generate-content?hl=vi#method:-models.generatecontent) cung cấp một cách để tạo câu trả lời đơn giản, không có trạng thái từ một mô hình. Mặc dù bạn nên sử dụng Interactions API, nhưng `generateContent` vẫn được hỗ trợ đầy đủ.

Ví dụ này sử dụng phương thức [`generateContent`](https://ai.google.dev/api/generate-content?hl=vi#method:-models.generatecontent) để gửi yêu cầu đến Gemini API bằng mô hình Gemini 2.5 Flash.

Nếu bạn [đặt khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#set-api-env-var) làm biến môi trường `GEMINI_API_KEY`, thì ứng dụng sẽ tự động chọn khoá này khi sử dụng [Thư viện Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=vi).
Nếu không, bạn sẽ cần [truyền khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#provide-api-key-explicitly) làm đối số khi khởi chạy ứng dụng.

Xin lưu ý rằng tất cả các mẫu mã trong tài liệu về Gemini API đều giả định rằng bạn đã đặt biến môi trường `GEMINI_API_KEY`.

### Python

```
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The client gets the API key from the environment variable `GEMINI_API_KEY`.
const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
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
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    // The client gets the API key from the environment variable `GEMINI_API_KEY`.
    Client client = new Client();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### C#

```
using System.Threading.Tasks;
using Google.GenAI;
using Google.GenAI.Types;

public class GenerateContentSimpleText {
  public static async Task main() {
    // The client gets the API key from the environment variable `GOOGLE_API_KEY`.
    var client = new Client();
    var response = await client.Models.GenerateContentAsync(
      model: "gemini-3-flash-preview", contents: "Explain how AI works in a few words"
    );
    Console.WriteLine(response.Candidates[0].Content.Parts[0].Text);
  }
}
```

### Apps Script

```
// See https://developers.google.com/apps-script/guides/properties
// for instructions on how to set the API key.
const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
function main() {
  const payload = {
    contents: [
      {
        parts: [
          { text: 'Explain how AI works in a few words' },
        ],
      },
    ],
  };

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent';
  const options = {
    method: 'POST',
    contentType: 'application/json',
    headers: {
      'x-goog-api-key': apiKey,
    },
    payload: JSON.stringify(payload)
  };

  const response = UrlFetchApp.fetch(url, options);
  const data = JSON.parse(response);
  const content = data['candidates'][0]['content']['parts'][0]['text'];
  console.log(content);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Bước tiếp theo

Giờ đây, khi đã thực hiện yêu cầu API đầu tiên, bạn có thể muốn khám phá các hướng dẫn sau đây cho thấy Gemini đang hoạt động:

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi)
- [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)
- [Hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi)
- [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
- [Ngữ cảnh dài](https://ai.google.dev/gemini-api/docs/long-context?hl=vi)
- [Vectơ nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-11 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-11 UTC."],[],[]]
