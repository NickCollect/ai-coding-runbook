---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=vi
fetched_at: 2026-05-05T20:02:47.403910+00:00
title: "Live API best practices \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Live API best practices

Hướng dẫn này trình bày các phương pháp hay nhất mà bạn có thể làm theo để tối ưu hoá việc sử dụng Live API.
Hãy xem trang [Bắt đầu sử dụng Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) để biết thông tin tổng quan và mã mẫu cho các trường hợp sử dụng phổ biến.

## Thiết kế hướng dẫn rõ ràng cho hệ thống

Để khai thác tối đa hiệu suất của Live API, chúng tôi khuyên bạn nên có một bộ hướng dẫn hệ thống (SI) được xác định rõ ràng để xác định vai trò của tác nhân, các quy tắc đàm thoại và các biện pháp bảo vệ, theo thứ tự này.

Để có kết quả tốt nhất, hãy tách từng tác nhân thành một SI riêng biệt.

1. **Chỉ định tính cách của nhân viên hỗ trợ:** Cung cấp thông tin chi tiết về tên, vai trò và mọi đặc điểm ưu tiên của nhân viên hỗ trợ. Nếu bạn muốn chỉ định giọng, hãy nhớ chỉ định cả ngôn ngữ đầu ra ưu tiên (chẳng hạn như giọng Anh cho người nói tiếng Anh).
2. **Chỉ định các quy tắc trò chuyện:** Đặt các quy tắc này theo thứ tự mà bạn muốn mô hình tuân theo. Phân biệt giữa các yếu tố chỉ xuất hiện một lần trong cuộc trò chuyện và các vòng lặp trò chuyện. Ví dụ:

   - **Phần tử dùng một lần:** Thu thập thông tin chi tiết của khách hàng một lần (chẳng hạn như tên, vị trí, số thẻ khách hàng thân thiết).
   - **Vòng lặp trò chuyện:** Người dùng có thể thảo luận về đề xuất, giá cả, việc trả lại hàng và giao hàng, đồng thời có thể muốn chuyển từ chủ đề này sang chủ đề khác. Cho mô hình biết rằng mô hình có thể tham gia vào vòng lặp trò chuyện này miễn là người dùng muốn.
3. **Chỉ định các lệnh gọi công cụ trong một quy trình bằng các câu riêng biệt:** Ví dụ: nếu một bước duy nhất để thu thập thông tin chi tiết của khách hàng yêu cầu bạn phải gọi một hàm `get_user_info`, bạn có thể nói: *Bước đầu tiên là thu thập thông tin người dùng. Trước tiên, hãy yêu cầu người dùng cung cấp tên, vị trí và số thẻ khách hàng thân thiết của họ. Sau đó, hãy gọi `get_user_info` kèm theo những thông tin chi tiết này.*
4. **Thêm mọi biện pháp bảo vệ cần thiết:** Cung cấp mọi biện pháp bảo vệ chung trong cuộc trò chuyện mà bạn không muốn mô hình thực hiện. Bạn có thể cung cấp các ví dụ cụ thể về trường hợp nếu *x* xảy ra, bạn muốn mô hình thực hiện *y*. Nếu bạn vẫn chưa nhận được mức độ chính xác như mong muốn, hãy dùng từ *rõ ràng* để hướng dẫn mô hình đưa ra kết quả chính xác.

## Xác định chính xác các công cụ

Khi sử dụng các công cụ có Live API, hãy xác định cụ thể trong định nghĩa công cụ của bạn.
Hãy nhớ cho Gemini biết những điều kiện mà bạn nên gọi một công cụ. Để biết thêm thông tin chi tiết, hãy xem phần [Định nghĩa công cụ](#tool-definitions-example) trong phần ví dụ.

## Tạo câu lệnh hiệu quả

- **Sử dụng câu lệnh rõ ràng:** Cung cấp ví dụ về những việc mà mô hình nên và không nên làm trong câu lệnh, đồng thời cố gắng giới hạn câu lệnh ở một câu lệnh cho mỗi nhân vật hoặc vai trò tại một thời điểm. Thay vì sử dụng các câu lệnh dài, nhiều trang, hãy cân nhắc sử dụng tính năng liên kết câu lệnh. Mô hình này hoạt động hiệu quả nhất đối với các tác vụ có một lệnh gọi hàm.
- **Cung cấp lệnh và thông tin bắt đầu:** Live API cần có hoạt động đầu vào của người dùng trước khi phản hồi. Để Live API bắt đầu cuộc trò chuyện, hãy thêm một câu lệnh yêu cầu API chào người dùng hoặc bắt đầu cuộc trò chuyện. Bao gồm thông tin về người dùng để Live API cá nhân hoá lời chào đó.

## Chỉ định ngôn ngữ

Để có hiệu suất tối ưu trên `gemini-live-2.5-flash` xếp tầng Live API, hãy đảm bảo rằng `language_code` của API này khớp với ngôn ngữ mà người dùng nói.

Nếu bạn muốn mô hình phản hồi bằng một ngôn ngữ không phải tiếng Anh, hãy thêm nội dung sau vào chỉ dẫn hệ thống:

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Phát trực tiếp

Khi triển khai âm thanh theo thời gian thực, hãy làm theo các phương pháp hay nhất sau đây:

- **Kích thước phân đoạn và độ trễ**: Gửi âm thanh theo phân đoạn từ 20 mili giây đến 40 mili giây.
- **Xử lý gián đoạn**: Khi người dùng nói trong lúc mô hình đang trả lời, máy chủ sẽ gửi thông báo `server_content` kèm theo `"interrupted": true`. Bạn phải huỷ ngay bộ đệm âm thanh phía máy khách để ngăn tác nhân tiếp tục nói chuyện với người dùng.

## Quản lý ngữ cảnh

Sử dụng `ContextWindowCompressionConfig` cho các phiên dài, vì mã thông báo âm thanh gốc tích luỹ nhanh chóng (khoảng 25 mã thông báo/giây âm thanh).

## Lưu vào bộ đệm phía máy khách

Không đệm đáng kể âm thanh đầu vào (chẳng hạn như 1 giây) trước khi gửi. Gửi các đoạn nhỏ (20 mili giây – 100 mili giây) để giảm thiểu độ trễ.

## Lấy mẫu lại

Đảm bảo ứng dụng khách của bạn lấy mẫu lại dữ liệu đầu vào từ micrô (thường là 44,1 kHz hoặc 48 kHz) thành 16 kHz trước khi truyền.

## Quản lý phiên

Hãy làm theo các nguyên tắc này để xử lý vòng đời phiên và đảm bảo mang lại trải nghiệm đáng tin cậy cho người dùng:

- **Bật tính năng nén cửa sổ ngữ cảnh:** Các mã thông báo âm thanh tích luỹ với tốc độ khoảng 25 mã thông báo mỗi giây. Nếu không nén, các phiên chỉ có âm thanh sẽ bị giới hạn ở 15 phút và các phiên có cả âm thanh và video sẽ bị giới hạn ở 2 phút. Bật tính năng [nén cửa sổ ngữ cảnh](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi#context-window-compression) để kéo dài phiên đến thời lượng không giới hạn.
- **Triển khai tính năng tiếp tục phiên:** Máy chủ có thể định kỳ đặt lại kết nối WebSocket. Sử dụng tính năng [tiếp tục phiên](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi#session-resumption) để kết nối lại một cách liền mạch mà không bị mất ngữ cảnh. Giữ lại mã thông báo tiếp tục mới nhất từ `SessionResumptionUpdate` tin nhắn và truyền mã thông báo đó dưới dạng mã nhận dạng khi kết nối lại. Mã thông báo tiếp tục có hiệu lực trong 2 giờ sau khi phiên gần nhất kết thúc.
- **Xử lý thông báo GoAway:** Máy chủ gửi thông báo [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi#goaway-message) trước khi chấm dứt kết nối. Lắng nghe thông báo này và sử dụng trường `timeLeft` để kết thúc hoặc kết nối lại một cách suôn sẻ trước khi kết nối đóng.
- **Xử lý tín hiệu generationComplete:** Sử dụng thông báo [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi#generation-complete-message) để biết thời điểm mô hình đã hoàn tất việc tạo câu trả lời, nhờ đó ứng dụng của bạn có thể cập nhật giao diện người dùng hoặc tiến hành hành động tiếp theo.

Để biết thông tin chi tiết về cách triển khai, hãy xem phần [Quản lý phiên](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=vi).

## Ví dụ

Ví dụ này kết hợp cả các phương pháp hay nhất và [hướng dẫn về thiết kế chỉ dẫn hệ thống](#system-instruction-guidelines) để hướng dẫn hiệu suất của mô hình với vai trò là huấn luyện viên nghề nghiệp.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Định nghĩa về công cụ

JSON này xác định các hàm có liên quan được gọi trong ví dụ về huấn luyện viên nghề nghiệp.
Để có kết quả tốt nhất khi xác định các hàm, hãy thêm tên, nội dung mô tả, tham số và điều kiện gọi của các hàm đó.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
