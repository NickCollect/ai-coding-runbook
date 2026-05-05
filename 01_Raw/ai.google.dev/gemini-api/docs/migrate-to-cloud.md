---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=vi
fetched_at: 2026-05-05T20:50:16.427748+00:00
title: "Gemini Developer API so v\u1edbi N\u1ec1n t\u1ea3ng t\u00e1c nh\u00e2n Gemini Enterprise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Gemini Developer API so với Nền tảng tác nhân Gemini Enterprise

Khi phát triển các giải pháp AI tạo sinh bằng Gemini, Google cung cấp 2 sản phẩm API: [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=vi) và [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=vi).

Gemini Developer API cung cấp cách nhanh nhất để tạo, phát hành công khai và mở rộng quy mô các ứng dụng dựa trên Gemini. Hầu hết nhà phát triển nên sử dụng Gemini Developer API, trừ phi cần có các chế độ kiểm soát cụ thể cho doanh nghiệp.

Nền tảng tác nhân Gemini Enterprise cung cấp một hệ sinh thái toàn diện gồm các tính năng và dịch vụ sẵn sàng cho doanh nghiệp để xây dựng và triển khai các ứng dụng AI tạo sinh được hỗ trợ bởi Google Cloud Platform.

Gần đây, chúng tôi đã đơn giản hoá quy trình di chuyển giữa các dịch vụ này. Giờ đây, bạn có thể truy cập cả Gemini Developer API và Gemini Enterprise Agent Platform API thông qua [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) hợp nhất.

## So sánh mã

Trang này có các đoạn mã so sánh song song giữa Gemini Developer API và hướng dẫn nhanh về Nền tảng tác nhân Gemini Enterprise để tạo văn bản.

### Python

Bạn có thể truy cập cả Gemini Developer API và các dịch vụ của Nền tảng tác nhân Gemini Enterprise thông qua thư viện `google-genai`. Hãy xem trang [thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) để biết hướng dẫn về cách cài đặt `google-genai`.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript và TypeScript

Bạn có thể truy cập cả Gemini Developer API và các dịch vụ của Nền tảng tác nhân Gemini Enterprise thông qua thư viện `@google/genai`. Hãy xem trang [thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) để biết hướng dẫn về cách cài đặt `@google/genai`.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

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

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

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

Bạn có thể truy cập cả Gemini Developer API và các dịch vụ của Nền tảng tác nhân Gemini Enterprise thông qua thư viện `google.golang.org/genai`. Hãy xem trang [thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) để biết hướng dẫn về cách cài đặt `google.golang.org/genai`.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Các trường hợp sử dụng và nền tảng khác

Hãy tham khảo hướng dẫn dành riêng cho từng trường hợp sử dụng trên [Tài liệu về Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=vi) và [Tài liệu về Nền tảng tác nhân Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=vi) cho các nền tảng và trường hợp sử dụng khác.

## Những điều cần cân nhắc khi di chuyển

Khi bạn di chuyển:

- Bạn cần sử dụng tài khoản dịch vụ Google Cloud để xác thực. Hãy xem [tài liệu về Nền tảng tác nhân Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=vi) để biết thêm thông tin.
- Bạn có thể sử dụng dự án Google Cloud hiện có (dự án mà bạn đã dùng để tạo khoá API) hoặc bạn có thể [tạo một dự án Google Cloud mới](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=vi).
- Các khu vực được hỗ trợ có thể khác nhau giữa Gemini Developer API và Gemini Enterprise Agent Platform API. Xem danh sách [các khu vực được hỗ trợ cho AI tạo sinh trên Google Cloud](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=vi).
- Bạn cần phải huấn luyện lại mọi mô hình mà bạn đã tạo trong Google AI Studio trong Nền tảng tác nhân Gemini Enterprise.

Nếu không cần dùng khoá Gemini API cho Gemini Developer API nữa, hãy làm theo các phương pháp bảo mật hay nhất và xoá khoá đó.

Cách xoá khoá API:

1. Mở trang [Thông tin đăng nhập API Google Cloud](https://console.cloud.google.com/apis/credentials?hl=vi).
2. Tìm khoá API mà bạn muốn xoá rồi nhấp vào biểu tượng **Thao tác**.
3. Chọn **Xoá khoá API**.
4. Trong cửa sổ **Xoá thông tin đăng nhập**, hãy chọn **Xoá**.

   Quá trình xoá khoá API sẽ mất vài phút để có hiệu lực. Sau khi quá trình truyền dữ liệu hoàn tất, mọi lưu lượng truy cập sử dụng khoá API đã xoá đều bị từ chối.

## Các bước tiếp theo

- Xem [Tổng quan về AI tạo sinh trên Nền tảng tác nhân Gemini Enterprise](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=vi) để tìm hiểu thêm về các giải pháp AI tạo sinh trên Nền tảng tác nhân Gemini Enterprise.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
