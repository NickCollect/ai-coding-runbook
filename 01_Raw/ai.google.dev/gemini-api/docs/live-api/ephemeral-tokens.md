---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=vi
fetched_at: 2026-05-11T04:58:55.206250+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ephemeral tokens

Mã thông báo tạm thời là mã thông báo xác thực có thời gian tồn tại ngắn để truy cập vào Gemini
API thông qua [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Mã thông báo này được thiết kế để tăng cường bảo mật khi
bạn kết nối trực tiếp từ thiết bị của người dùng đến API (triển khai
[từ ứng dụng đến máy chủ](https://ai.google.dev/gemini-api/docs/live?hl=vi#implementation-approach)
). Giống như khoá API tiêu chuẩn, bạn có thể trích xuất mã thông báo tạm thời từ các ứng dụng phía máy khách, chẳng hạn như trình duyệt web hoặc ứng dụng di động. Tuy nhiên, vì mã thông báo tạm thời hết hạn nhanh chóng và có thể bị hạn chế, nên mã thông báo này giúp giảm đáng kể các rủi ro bảo mật trong môi trường phát hành chính thức. Bạn nên sử dụng mã thông báo này khi truy cập trực tiếp vào Live API từ các ứng dụng phía máy khách để tăng cường bảo mật khoá API.

 

## Cách hoạt động của mã thông báo tạm thời

Sau đây là cách hoạt động của mã thông báo tạm thời ở cấp độ cao:

1. Ứng dụng của bạn (ví dụ: ứng dụng web) xác thực với phần phụ trợ.
2. Phần phụ trợ của bạn yêu cầu mã thông báo tạm thời từ dịch vụ cung cấp của Gemini API.
3. Gemini API phát hành mã thông báo có thời gian tồn tại ngắn.
4. Phần phụ trợ của bạn gửi mã thông báo đến ứng dụng để kết nối WebSocket với Live API. Bạn có thể thực hiện việc này bằng cách đổi khoá API của mình thành mã thông báo tạm thời.
5. Sau đó, ứng dụng sẽ sử dụng mã thông báo này như thể đó là khoá API.

![Tổng quan về mã thông báo tạm thời](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=vi)

Điều này giúp tăng cường bảo mật vì ngay cả khi được trích xuất, mã thông báo này cũng có thời gian tồn tại ngắn, không giống như khoá API có thời gian tồn tại dài được triển khai ở phía máy khách. Vì ứng dụng gửi dữ liệu trực tiếp đến Gemini, nên điều này cũng giúp cải thiện độ trễ và tránh việc phần phụ trợ của bạn cần phải làm trung gian cho dữ liệu theo thời gian thực.

## Tạo mã thông báo tạm thời

Sau đây là ví dụ đơn giản về cách nhận mã thông báo tạm thời từ Gemini.
Theo mặc định, bạn sẽ có 1 phút để bắt đầu các phiên Live API mới bằng mã thông báo từ yêu cầu này (`newSessionExpireTime`) và 30 phút để gửi thông báo qua kết nối đó (`expireTime`).

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Để biết các ràng buộc về giá trị `expireTime`, giá trị mặc định và các thông số kỹ thuật khác của trường, hãy xem tài liệu tham khảo về API
.
Trong khung thời gian `expireTime`, bạn sẽ cần
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=vi#session-resumption) để
kết nối lại lệnh gọi sau mỗi 10 phút (bạn có thể thực hiện việc này bằng cùng một mã thông báo ngay cả
khi `uses: 1`).

Bạn cũng có thể khoá mã thông báo tạm thời đối với một nhóm cấu hình. Điều này có thể hữu ích để cải thiện thêm tính bảo mật của ứng dụng và giữ các hướng dẫn của hệ thống ở phía máy chủ.

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

Bạn cũng có thể khoá một nhóm nhỏ các trường. Hãy xem [tài liệu về SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
để biết thêm thông tin.

## Kết nối với Live API bằng mã thông báo tạm thời

Sau khi có mã thông báo tạm thời, bạn sẽ sử dụng mã thông báo này như thể đó là khoá API (nhưng hãy nhớ rằng mã thông báo này chỉ hoạt động đối với Live API và chỉ với phiên bản `v1alpha` của API).

Việc sử dụng mã thông báo tạm thời chỉ mang lại giá trị khi triển khai các ứng dụng
tuân theo [phương pháp triển khai từ ứng dụng đến máy chủ](https://ai.google.dev/gemini-api/docs/live?hl=vi#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Hãy xem bài viết [Bắt đầu sử dụng Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) để biết thêm ví dụ.

## Các phương pháp hay nhất

- Đặt thời gian hết hạn ngắn bằng tham số `expire_time`.
- Mã thông báo sẽ hết hạn, yêu cầu bạn phải khởi động lại quy trình cung cấp.
- Xác minh quá trình xác thực an toàn cho phần phụ trợ của riêng bạn. Mã thông báo tạm thời sẽ chỉ an toàn như phương thức xác thực phần phụ trợ của bạn.
- Nói chung, hãy tránh sử dụng mã thông báo tạm thời cho các kết nối từ phần phụ trợ đến Gemini, vì đường dẫn này thường được coi là an toàn.

## Các điểm hạn chế

Hiện tại, mã thông báo tạm thời chỉ tương thích với [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi).

## Bước tiếp theo

- Đọc tài liệu tham khảo API Live [trên mã thông báo tạm thời](https://ai.google.dev/api/live?hl=vi#ephemeral-auth-tokens) để biết thêm thông tin.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
