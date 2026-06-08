---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=vi
fetched_at: 2026-06-08T05:37:00.142862+00:00
title: "S\u1eed d\u1ee5ng kho\u00e1 API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Sử dụng khoá API Gemini

Để sử dụng Gemini API, bạn cần có khoá API. Trang này trình bày cách tạo và quản lý khoá trong Google AI Studio, cũng như cách thiết lập môi trường để sử dụng các khoá đó trong mã của bạn.

[Tạo hoặc xem khoá Gemini API](https://aistudio.google.com/app/apikey?hl=vi)

## Khoá API

Bạn có thể tạo và quản lý tất cả khoá Gemini API trên trang [Khoá API của **Google AI Studio**](https://aistudio.google.com/app/apikey?hl=vi).

Sau khi có khoá API, bạn có thể kết nối với Gemini API theo những cách sau:

- [Đặt khoá API làm biến môi trường](#set-api-env-var)
- [Cung cấp khoá API một cách rõ ràng](#provide-api-key-explicitly)

Đối với hoạt động kiểm thử ban đầu, bạn có thể mã hoá cứng một khoá API, nhưng đây chỉ là giải pháp tạm thời vì không an toàn. Bạn có thể tìm thấy các ví dụ về việc mã hoá cứng khoá API trong phần [Cung cấp khoá API một cách rõ ràng](#provide-api-key-explicitly).

## Dự án trên Google Cloud

[Dự án Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=vi) là yếu tố cơ bản để sử dụng các dịch vụ của Google Cloud (chẳng hạn như Gemini API), quản lý việc thanh toán và kiểm soát cộng tác viên cũng như quyền. Google AI Studio cung cấp một giao diện đơn giản cho các dự án của bạn trên Google Cloud.

Nếu chưa tạo dự án nào, bạn phải tạo một dự án mới hoặc nhập một dự án từ Google Cloud vào Google AI Studio. Trang **Dự án** trong Google AI Studio sẽ hiển thị tất cả các khoá có đủ quyền sử dụng Gemini API. Hãy tham khảo phần [nhập dự án](#import-projects) để biết hướng dẫn.

### Dự án mặc định

Đối với người dùng mới, sau khi chấp nhận Điều khoản dịch vụ, Google AI Studio sẽ tạo một Dự án Google Cloud và Khoá API mặc định để người dùng dễ dàng sử dụng. Bạn có thể đổi tên dự án này trong Google AI Studio bằng cách chuyển đến chế độ xem **Projects** (Dự án) trong **Dashboard** (Trang tổng quan), nhấp vào nút cài đặt có biểu tượng 3 dấu chấm bên cạnh một dự án rồi chọn **Rename project** (Đổi tên dự án). Người dùng hiện tại hoặc người dùng đã có Tài khoản Google Cloud sẽ không có dự án mặc định được tạo.

## Nhập dự án

Mỗi khoá API Gemini đều được liên kết với một dự án trên Google Cloud. Theo mặc định, Google AI Studio không hiển thị tất cả Dự án trên đám mây của bạn. Bạn phải nhập các dự án mình muốn bằng cách tìm tên hoặc mã dự án trong hộp thoại **Nhập dự án**. Để xem danh sách đầy đủ các dự án mà bạn có quyền truy cập, hãy truy cập vào Cloud Console.

Nếu bạn chưa nhập dự án nào, hãy làm theo các bước sau để nhập một dự án trên Google Cloud và tạo khoá:

1. Truy cập vào [Google AI Studio](https://aistudio.google.com?hl=vi).
2. Mở **Trang tổng quan** trong bảng điều khiển bên trái.
3. Chọn **Dự án**.
4. Chọn nút **Nhập dự án** trên trang **Dự án**.
5. Tìm và chọn dự án trên đám mây của Google Cloud mà bạn muốn nhập, rồi chọn nút **Nhập**.

Sau khi nhập một dự án, hãy chuyển đến trang **API Keys** (Khoá API) trong trình đơn **Dashboard** (Trang tổng quan) rồi tạo một khoá API trong dự án mà bạn vừa nhập.

## Các điểm hạn chế

Sau đây là những hạn chế khi quản lý khoá API và dự án Google Cloud trong Google AI Studio.

- Bạn có thể tạo tối đa 10 dự án cùng một lúc trên trang **Dự án** của Google AI Studio.
- Bạn có thể đặt tên và đổi tên dự án cũng như khoá.
- Trang **Khoá API** và **Dự án** hiển thị tối đa 100 khoá và 50 dự án.
- Chỉ những khoá API không có quy tắc hạn chế hoặc bị hạn chế đối với Generative Language API mới xuất hiện.

Để có thêm quyền quản lý đối với các dự án của bạn, bao gồm cả việc sửa đổi và hạn chế khoá API, hãy truy cập vào [trang thông tin xác thực của Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).
Trong Cloud Console, bạn có thể chọn dự án của mình, nhấp vào một khoá API hiện có, rồi hạn chế khoá đó đối với **Generative Language API**.

## Đặt khoá API làm biến môi trường

Nếu bạn đặt biến môi trường `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`, khoá API sẽ tự động được ứng dụng chọn khi sử dụng một trong các [thư viện Gemini API](https://ai.google.dev/gemini-api/docs/libraries?hl=vi). Bạn chỉ nên đặt một trong các biến đó, nhưng nếu đặt cả hai, thì `GOOGLE_API_KEY` sẽ được ưu tiên.

Nếu đang sử dụng API REST hoặc JavaScript trên trình duyệt, bạn sẽ cần cung cấp khoá API một cách rõ ràng.

Sau đây là cách bạn có thể đặt khoá API cục bộ làm biến môi trường `GEMINI_API_KEY` bằng các hệ điều hành khác nhau.

### Linux/macOS – Bash

Bash là một cấu hình thiết bị đầu cuối phổ biến trên Linux và macOS. Bạn có thể kiểm tra xem mình có tệp cấu hình cho ứng dụng đó hay không bằng cách chạy lệnh sau:

```
~/.bashrc
```

Nếu phản hồi là "No such file or directory" (Không có tệp hoặc thư mục như vậy), bạn sẽ cần tạo tệp này và mở tệp bằng cách chạy các lệnh sau hoặc sử dụng `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Tiếp theo, bạn cần đặt khoá API bằng cách thêm lệnh xuất sau:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Sau khi lưu tệp, hãy áp dụng các thay đổi bằng cách chạy:

```
source ~/.bashrc
```

### macOS – Zsh

Zsh là một cấu hình phổ biến của thiết bị đầu cuối Linux và macOS. Bạn có thể kiểm tra xem mình có tệp cấu hình cho ứng dụng đó hay không bằng cách chạy lệnh sau:

```
~/.zshrc
```

Nếu phản hồi là "No such file or directory" (Không có tệp hoặc thư mục như vậy), bạn sẽ cần tạo tệp này và mở tệp bằng cách chạy các lệnh sau hoặc sử dụng `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Tiếp theo, bạn cần đặt khoá API bằng cách thêm lệnh xuất sau:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Sau khi lưu tệp, hãy áp dụng các thay đổi bằng cách chạy:

```
source ~/.zshrc
```

### Windows

1. Tìm "Environment Variables" (Biến môi trường) trong thanh tìm kiếm.
2. Chọn sửa đổi **Cài đặt hệ thống**. Bạn có thể phải xác nhận rằng bạn muốn thực hiện việc này.
3. Trong hộp thoại cài đặt hệ thống, hãy nhấp vào nút có nhãn **Environment Variables** (Biến môi trường).
4. Trong mục **User variables** (Biến người dùng) (dành cho người dùng hiện tại) hoặc **System variables** (Biến hệ thống) (áp dụng cho tất cả người dùng sử dụng máy), hãy nhấp vào **New...** (Mới...)
5. Chỉ định tên biến là `GEMINI_API_KEY`. Chỉ định Khoá Gemini API làm giá trị biến.
6. Nhấp vào **OK** để áp dụng các thay đổi.
7. Mở một phiên thiết bị đầu cuối mới (cmd hoặc Powershell) để lấy biến mới.

## Cung cấp khoá API một cách rõ ràng

Trong một số trường hợp, bạn có thể muốn cung cấp khoá API một cách rõ ràng. Ví dụ:

- Bạn đang thực hiện một lệnh gọi API đơn giản và muốn mã hoá khoá API.
- Bạn muốn kiểm soát rõ ràng mà không cần dựa vào tính năng tự động phát hiện các biến môi trường của thư viện Gemini API
- Bạn đang sử dụng một môi trường không hỗ trợ các biến môi trường (ví dụ: web) hoặc bạn đang thực hiện các lệnh gọi REST.

Dưới đây là ví dụ về cách bạn có thể cung cấp khoá API một cách rõ ràng:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.5-flash", contents="Explain how AI works in a few words"
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
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

## Bảo mật khoá API

Hãy coi khoá Gemini API như một mật khẩu. Nếu bị xâm nhập, những người khác có thể sử dụng hạn mức của dự án, phát sinh phí (nếu bạn bật tính năng thanh toán) và truy cập vào dữ liệu riêng tư của bạn, chẳng hạn như tệp.

### Quy tắc bảo mật quan trọng

- **Giữ bí mật các khoá**: Khoá API cho Gemini có thể truy cập vào dữ liệu nhạy cảm mà ứng dụng của bạn phụ thuộc vào.

  - **Tuyệt đối không chuyển khoá API vào tính năng kiểm soát nguồn.** Đừng kiểm tra khoá API của bạn trong các hệ thống kiểm soát phiên bản như Git.
  - **Tuyệt đối không để lộ khoá API ở phía máy khách.** Không sử dụng trực tiếp khoá API trong các ứng dụng web hoặc di động đang hoạt động. Các khoá trong mã phía máy khách (bao gồm cả thư viện JavaScript/TypeScript và lệnh gọi REST) có thể được trích xuất.
- **Hạn chế quyền truy cập**: Hạn chế việc sử dụng khoá API ở các địa chỉ IP, HTTP referrer hoặc ứng dụng Android/iOS cụ thể (nếu có thể).
- **Hạn chế việc sử dụng**: Chỉ bật những API cần thiết cho mỗi khoá.
- **Thực hiện kiểm tra thường xuyên**: Thường xuyên kiểm tra và định kỳ xoay vòng các khoá API.

### Các phương pháp hay nhất

- **Sử dụng các lệnh gọi phía máy chủ bằng khoá API** Cách an toàn nhất để sử dụng khoá API là gọi Gemini API từ một ứng dụng phía máy chủ, nơi khoá có thể được giữ bí mật.
- **Sử dụng mã thông báo tạm thời để truy cập phía máy khách (chỉ Live API):** Để truy cập trực tiếp vào Live API phía máy khách, bạn có thể sử dụng mã thông báo tạm thời. Chúng có rủi ro bảo mật thấp hơn và có thể phù hợp để sử dụng trong bản phát hành chính thức. Hãy xem hướng dẫn về [mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=vi) để biết thêm thông tin.
- **Cân nhắc việc thêm các quy tắc hạn chế đối với khoá:** Bạn có thể giới hạn các quyền của khoá bằng cách thêm [các quy tắc hạn chế đối với khoá API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=vi#add-api-restrictions).
  Điều này giúp giảm thiểu thiệt hại tiềm ẩn nếu khoá bị rò rỉ.

Để biết một số phương pháp hay nhất chung, bạn cũng có thể xem [bài viết hỗ trợ](https://support.google.com/googleapi/answer/6310037?hl=vi) này.

## Bảo mật khoá API không bị hạn chế

Khoá API không bị hạn chế rất dễ bị kẻ xấu lợi dụng và sử dụng trái phép. Kể từ ngày 19 tháng 6 năm 2026, để cải thiện tính bảo mật, Gemini API sẽ ngừng hỗ trợ các khoá lưu lượng truy cập không hạn chế.

**Điều này có nghĩa là các yêu cầu của bạn đối với Gemini API sẽ không thành công nếu bạn không thực hiện hành động.**

Để tiếp tục sử dụng Gemini API mà không bị gián đoạn, hãy bảo mật các khoá lưu lượng truy cập bằng cách thêm các quy tắc hạn chế trong [AI Studio](https://aistudio.google.com/api-keys?hl=vi).

Trong [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=vi), bạn sẽ thấy một biểu ngữ thông báo cho bạn khi khoá API không bị hạn chế. Bạn có thể xem những khoá không bị hạn chế và mức sử dụng dịch vụ trong 90 ngày qua.

Đối với các khoá không hạn chế, bạn cần chọn một trong những lựa chọn sau:

- Chỉ sử dụng khoá cho Gemini API.
- Sử dụng khoá này cho mục đích không phải là Gemini API.

### Hạn chế để chỉ sử dụng khoá cho Gemini API

Nếu chỉ muốn hạn chế khoá cho Gemini API, hãy bảo mật khoá trong [AI Studio](https://aistudio.google.com/api-keys?hl=vi) bằng cách nhấp vào nút **Hạn chế cho Gemini API**.

### Hạn chế khoá để sử dụng cho các API không phải Gemini

Nếu bạn muốn hạn chế việc sử dụng khoá cho các API không phải Gemini:

1. Truy cập vào [trang thông tin đăng nhập của Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).
2. Đảm bảo bạn đã chọn đúng dự án.
3. Chọn một khoá API.
4. Mở rộng trình đơn thả xuống **API restrictions** (Hạn chế cho API) rồi áp dụng các quy tắc hạn chế về dịch vụ cho khoá API.

Nếu bạn muốn sửa đổi các khoá có hạn chế hiện tại hoặc mới thêm, hãy truy cập vào [Google Cloud Console](https://console.cloud.google.com/apis/credentials?hl=vi).

## Khoá bị chặn

Kể từ ngày 7 tháng 5 năm 2026, Gemini API sẽ chặn các khoá API không bị hạn chế và không hoạt động trong một thời gian dài. Những người dùng này sẽ thấy thẻ **Bị chặn** cho khoá của họ trên [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys?hl=vi) và cần tạo khoá mới hoặc sử dụng khoá bị hạn chế thay thế để tiếp tục dùng Gemini API.

## Khắc phục sự cố khi tạo khoá API

Trong Google AI Studio, nút **Tạo khoá API** có thể không hoạt động và xuất hiện thông báo: "*Bạn không có quyền tạo khoá trong dự án này*".

Lỗi này xảy ra khi bạn không có các quyền cần thiết trong dự án để tạo khoá mới:

- **`resourcemanager.projects.get`**: Cho phép AI Studio xác minh sự tồn tại của dự án.
- **`apikeys.keys.create`**: Cho phép tạo chính khoá API.
- **`serviceusage.services.enable`**: Bắt buộc để đảm bảo Gemini API đang hoạt động trên dự án.
- **`iam.serviceAccounts.create`**: Mỗi khoá API mới hiện đều yêu cầu một [tài khoản dịch vụ](https://docs.cloud.google.com/docs/authentication/api-keys?hl=vi#api-keys-bound-sa) được liên kết, được tạo khi tạo khoá API.
- **`iam.serviceAccountApiKeyBindings.create`**: Bắt buộc để liên kết tài khoản dịch vụ mới tạo với khoá API.

Để sửa quyền, hãy yêu cầu quản trị viên dự án hoặc quản trị viên của tổ chức (nếu dự án thuộc về một [tổ chức](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=vi)) cấp cho bạn một vai trò có các quyền nêu trên (chẳng hạn như vai trò Người chỉnh sửa dự án hoặc vai trò tùy chỉnh).

Nếu không có quyền quản trị đối với một dự án, bạn có thể tạo một dự án mới không liên kết với tổ chức để tạo khoá.

Để xem danh sách đầy đủ các quyền IAM cần thiết cho tất cả tính năng của Google AI Studio (chẳng hạn như xem mức sử dụng, hạn mức hoặc thông tin thanh toán), hãy xem [hướng dẫn khắc phục sự cố của AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=vi#iam-permissions).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-29 UTC."],[],[]]
