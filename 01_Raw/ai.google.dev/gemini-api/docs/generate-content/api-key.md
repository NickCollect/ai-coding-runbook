---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=vi
fetched_at: 2026-07-20T04:43:13.207244+00:00
title: "S\u1eed d\u1ee5ng kho\u00e1 API Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Sử dụng khoá API Gemini

Để sử dụng Gemini API, bạn phải xác thực các yêu cầu của mình. Bạn có thể xác thực bằng khoá API tiêu chuẩn hoặc khoá API uỷ quyền.

[Tạo hoặc xem khoá Gemini API](https://aistudio.google.com/apikey?hl=vi)

## Các loại khoá API: tiêu chuẩn so với uỷ quyền

Khoá API cung cấp quyền truy cập vào Gemini API, nhưng đặc điểm bảo mật của các khoá này khác nhau. Gemini API đang chuyển từ khoá API tiêu chuẩn sang khoá uỷ quyền để cải thiện tính bảo mật:

- **Khoá API tiêu chuẩn**: Liên kết các yêu cầu với một dự án trên đám mây của Google Cloud cho mục đích lập hoá đơn và hạn mức. Các khoá tiêu chuẩn không xác định người gọi, điều này hạn chế mức độ chi tiết của các quyền và quyền kiểm soát truy cập mà chúng có thể hỗ trợ.
- **Khoá uỷ quyền (auth)**: Liên kết trực tiếp với một tài khoản dịch vụ của Google Cloud. Khi bạn sử dụng khoá uỷ quyền, các yêu cầu của bạn sẽ được xử lý theo danh tính của tài khoản dịch vụ được liên kết đó, cho phép kiểm soát quyền truy cập chi tiết. Theo mặc định, các khoá uỷ quyền bị hạn chế đối với Generative Language API (Gemini API) và cung cấp chế độ thực thi khoá bị lộ có hiệu lực nhanh chóng, giúp nhanh chóng ngăn chặn việc sử dụng các khoá bị lộ mà hệ thống của chúng tôi phát hiện được.

Để đảm bảo sử dụng an toàn, Gemini API sẽ chuyển từ khoá Chuẩn sang khoá Xác thực:

- **Khoá uỷ quyền mặc định**: Tất cả khoá API mới được tạo trong Google AI Studio đều tự động được tạo dưới dạng khoá uỷ quyền.
- **Khoá không hạn chế bị từ chối**: Gemini API từ chối các yêu cầu từ **khoá chuẩn không hạn chế**. Các khoá API tiêu chuẩn có quy tắc hạn chế rõ ràng được áp dụng vẫn sẽ hoạt động. Quy định hạn chế này ngăn chặn việc sử dụng trái phép các khoá có thể được chia sẻ công khai hoặc liên kết với các dịch vụ khác.
- **Vào tháng 9 năm 2026**: Gemini API sẽ từ chối các yêu cầu từ **khoá chuẩn**. Bạn phải [di chuyển sang khoá uỷ quyền](#migrate-to-auth-key) trước ngày này để tránh bị gián đoạn dịch vụ. Đừng quên di chuyển sang khoá uỷ quyền trước tháng 9 năm 2026.

## Quản lý khoá API trong Google AI Studio

Bạn có thể quản lý dự án và khoá ngay trong [Google AI Studio](https://aistudio.google.com/apikey?hl=vi).

### Dự án trên Google Cloud

Mỗi khoá Gemini API đều được liên kết với một [dự án trên Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=vi).
Các dự án trên Google Cloud quản lý hoạt động thanh toán, cộng tác viên và quyền. Google AI Studio cung cấp một giao diện đơn giản để truy cập vào các dự án này.

- **Dự án mặc định**: Nếu bạn là người dùng mới, Google AI Studio sẽ tự động tạo một dự án trên đám mây của Google Cloud và khoá API mặc định sau khi bạn chấp nhận Điều khoản dịch vụ. Bạn có thể đổi tên dự án này bằng cách chuyển đến chế độ xem **Dự án** trong trang tổng quan.
- **Dự án hiện có**: Nếu bạn đã có một tài khoản Google Cloud, AI Studio sẽ không tạo dự án mặc định. Thay vào đó, bạn phải nhập các dự án hiện có.

### Nhập dự án

Theo mặc định, Google AI Studio không hiển thị tất cả các dự án của bạn trên Google Cloud. Bạn phải nhập các dự án mà bạn muốn sử dụng:

1. Truy cập vào [Google AI Studio](https://aistudio.google.com?hl=vi).
2. Mở **Trang tổng quan** trên bảng điều khiển bên trái rồi chọn **Dự án**.
3. Nhấp vào nút **Nhập dự án**.
4. Tìm và chọn dự án trên đám mây của Google Cloud mà bạn muốn nhập, sau đó nhấp vào **Nhập**.
5. Sau khi nhập, hãy chuyển đến trang **Khoá API** trong trang tổng quan để tạo khoá trong dự án đó.

### Khắc phục sự cố về quyền tạo khoá

Nếu nút **Tạo khoá API** không hoạt động và hiển thị thông báo:
*"Bạn không có quyền tạo khoá trong dự án này"*, tức là bạn thiếu các quyền IAM bắt buộc.

Yêu cầu quản trị viên dự án hoặc tổ chức trên Google Cloud cấp cho bạn một vai trò có các quyền sau (chẳng hạn như Người chỉnh sửa dự án):

- `resourcemanager.projects.get`: Cho phép AI Studio xác minh dự án.
- `apikeys.keys.create`: Cho phép tạo khoá.
- `serviceusage.services.enable`: Đảm bảo Generative Language API được bật.
- `iam.serviceAccounts.create`: Bắt buộc để tạo tài khoản dịch vụ được liên kết.
- `iam.serviceAccountApiKeyBindings.create`: Liên kết tài khoản dịch vụ với khoá API.

Nếu không có quyền truy cập quản trị, bạn có thể tạo một dự án Google Cloud mới không liên kết với tổ chức để tạo khoá.

## Thiết lập môi trường

Sau khi có khoá, hãy định cấu hình môi trường để sử dụng khoá đó một cách an toàn trong các ứng dụng của bạn.

### Sử dụng các biến môi trường (nên dùng)

Đặt biến môi trường `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`. Các thư viện ứng dụng Gemini API sẽ tự động phát hiện và sử dụng các biến này. Nếu bạn đặt cả hai, thì `GOOGLE_API_KEY` sẽ được ưu tiên.

Chọn hệ điều hành để đặt biến:

### Linux/macOS – Bash

Xác minh xem bạn có tệp cấu hình bash hay không:

```
~/.bashrc
```

Nếu chưa có, hãy tạo một dự án rồi mở dự án đó:

```
touch ~/.bashrc && open ~/.bashrc
```

Thêm lệnh xuất vào cuối tệp:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Lưu tệp, sau đó áp dụng các thay đổi:

```
source ~/.bashrc
```

### macOS – Zsh

Xác minh xem bạn có tệp cấu hình zsh hay không:

```
~/.zshrc
```

Nếu chưa có, hãy tạo một dự án rồi mở dự án đó:

```
touch ~/.zshrc && open ~/.zshrc
```

Thêm lệnh xuất:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Lưu tệp, sau đó áp dụng các thay đổi:

```
source ~/.zshrc
```

### Windows

1. Tìm "Environment Variables" (Biến môi trường) trong thanh tìm kiếm của Windows.
2. Nhấp vào **Environment Variables** (Biến môi trường) trong hộp thoại System Properties (Thuộc tính hệ thống).
3. Trong mục **Biến người dùng** hoặc **Biến hệ thống**, hãy nhấp vào **Mới...**.
4. Đặt tên biến thành `GEMINI_API_KEY` và giá trị thành khoá API của bạn.
5. Nhấp vào **OK** để lưu. Mở một phiên thiết bị đầu cuối mới để tải biến.

### Cung cấp khoá API một cách rõ ràng trong mã

Bạn có thể truyền khoá API một cách rõ ràng khi khởi tạo ứng dụng. Chỉ thực hiện việc này nếu bạn không thể sử dụng các biến môi trường.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
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
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
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
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3.5-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
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

## Quản lý bảo mật và bí mật

Hãy coi khoá Gemini API như một mật khẩu. Nếu bị xâm nhập, những người khác có thể sử dụng hết hạn mức của dự án, phát sinh các khoản phí thanh toán không mong muốn và truy cập vào các tài nguyên riêng tư.

### Quy tắc bảo mật quan trọng

- **Giữ bí mật khoá**: Tuyệt đối không kiểm tra khoá API trong các hệ thống kiểm soát nguồn như Git.
- **Không bao giờ để lộ khoá phía máy khách trong quá trình sản xuất**: Đừng mã hoá cứng khoá API trực tiếp trong các ứng dụng web hoặc di động. Người dùng có thể trích xuất các khoá được biên dịch trong mã phía máy khách. Để bảo mật các ứng dụng phía máy khách, hãy chạy một máy chủ proxy phụ trợ để thực hiện các lệnh gọi API thực tế.

### Các phương pháp hay nhất về quản lý bí mật

- **Biến môi trường**: Đọc khoá từ các biến môi trường thay vì các tệp cấu hình.
- **Secret Manager**: Đối với quá trình sản xuất, hãy lưu trữ các khoá của bạn trong một kho bí mật an toàn, chẳng hạn như [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=vi).
- **Cảnh báo thanh toán**: Thiết lập cảnh báo thanh toán trong Google Cloud Console để thông báo cho bạn nếu mức sử dụng hoặc chi phí tăng đột biến.

### Danh sách kiểm tra phản ứng rò rỉ

Nếu bạn nghi ngờ khoá API của mình bị lộ:

1. **Tạo khoá mới**: Tạo khoá thay thế trong Google AI Studio hoặc Cloud Console.
2. **Cập nhật ứng dụng**: Triển khai mã bằng khoá mới.
3. **Tắt hoặc xoá khoá bị xâm phạm**: Tắt khoá bị rò rỉ trong Cloud Console sau khi khoá mới được xác minh. Đừng xoá khoá cũ cho đến khi khoá mới hoàn toàn hoạt động để tránh thời gian ngừng hoạt động của ứng dụng.
4. **Kiểm tra mức sử dụng**: Kiểm tra nhật ký thanh toán và mức sử dụng API trong Google Cloud Console để xác định hoạt động trái phép.

## Hạn chế và bảo mật khoá

Việc thêm các quy tắc hạn chế cho khoá API sẽ giảm thiểu thiệt hại tiềm ẩn nếu một khoá bị xâm phạm.

### Áp dụng các quy tắc hạn chế về nguồn gốc của yêu cầu

Các hạn chế về nguồn gốc giới hạn những địa chỉ IP, trang web hoặc ứng dụng có thể sử dụng khoá của bạn.

1. Chuyển đến [trang Thông tin đăng nhập của Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).
2. Chọn dự án của bạn, rồi nhấp vào tên của khoá API mà bạn muốn hạn chế.
3. Trong mục **Application restrictions** (Hạn chế cho ứng dụng), hãy chọn **IP addresses** (Địa chỉ IP) (hoặc loại hạn chế phù hợp cho môi trường của bạn).
4. Chỉ định địa chỉ hoặc dải IP được phép, rồi nhấp vào **Lưu**.

### Bảo mật khoá API thông thường không bị hạn chế

Để tiếp tục sử dụng Gemini API, bạn phải bảo mật mọi khoá không bị hạn chế.

#### Hạn chế để chỉ sử dụng khoá cho Gemini API thông qua AI Studio

Nếu bạn chỉ dùng khoá cho Gemini API, hãy bảo mật khoá đó ngay trong AI Studio:

1. Trên trang **Khoá API** trong [Google AI Studio](https://aistudio.google.com/api-keys?hl=vi), hãy tìm những khoá được đánh dấu bằng nhãn **Không hạn chế**.
2. Di chuột lên nhãn rồi nhấp vào **Thêm quy định hạn chế** trong hộp thoại.
3. Chọn **Chỉ hạn chế đối với Gemini API**.
4. Nhấp vào **Hạn chế khoá** để xác nhận.

#### Hạn chế khoá cho các dịch vụ khác thông qua Bảng điều khiển Google Cloud

Nếu khoá được chia sẻ với các API khác của Google (không nên dùng), hãy hạn chế khoá đó trong Cloud Console. **Lưu ý: Các yêu cầu Gemini API sử dụng khoá này sẽ không thành công sau khi các quy định hạn chế này được áp dụng.**

1. Truy cập vào [trang Thông tin đăng nhập của Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).
2. Chọn dự án và khoá API.
3. Trong mục **API restrictions** (Hạn chế cho API), chọn **Restrict key** (Hạn chế cho khoá).
4. Trong trình đơn thả xuống, hãy chọn những API mà bạn muốn khoá này truy cập. Không chọn **Generative Language API**.
5. Nhấp vào **Lưu**. Tạo một khoá riêng biệt, có hạn chế trong AI Studio để tiếp tục sử dụng Gemini API.

### Chặn các khoá không hoạt động

Kể từ ngày 7 tháng 5 năm 2026, Gemini API sẽ chặn các khoá API không bị hạn chế và không hoạt động trong một thời gian dài. Các khoá này sẽ có thẻ **Bị chặn** trong AI Studio. Bạn phải tạo một khoá mới hoặc sử dụng một khoá bị hạn chế hiện có để tiếp tục.

## Di chuyển sang khoá uỷ quyền

Hãy làm theo các bước sau để tạo khoá API uỷ quyền mới và cập nhật các ứng dụng của bạn:

1. Chuyển đến [trang Khoá API của AI Studio](https://aistudio.google.com/api-keys?hl=vi).
2. Kiểm tra cột **Loại khoá** để xác định mọi khoá được liệt kê là **Chuẩn**.
3. Nhấp vào **Tạo khoá API** để tạo một khoá mới. Tất cả khoá mới được tạo trong AI Studio đều tự động được tạo dưới dạng khoá uỷ quyền.
4. Sao chép khoá API xác thực mới.
5. Cập nhật mã ứng dụng, biến môi trường và mọi cấu hình triển khai để sử dụng khoá API xác thực mới.
6. Kiểm thử ứng dụng để xác nhận rằng ứng dụng hoạt động đúng cách với khoá mới.
7. Sau khi xác minh, hãy xoá hoặc thu hồi khoá lưu lượng truy cập cũ để tránh bị sử dụng sai mục đích.

## Các điểm hạn chế

Google AI Studio áp dụng các hạn chế sau đây đối với việc quản lý dự án và khoá:

- Bạn có thể tạo tối đa 10 dự án cùng lúc trên trang **Dự án** của Google AI Studio.
- Trang **Khoá API** và **Dự án** hiển thị tối đa 100 khoá và 50 dự án.
- Chỉ những khoá API không bị hạn chế hoặc bị hạn chế cụ thể đối với Generative Language API (Gemini API) mới xuất hiện.

Để quản lý dự án nâng cao hoặc sửa đổi khoá theo các quy định hạn chế khác, hãy sử dụng [trang thông tin đăng nhập của Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-16 UTC."],[],[]]
