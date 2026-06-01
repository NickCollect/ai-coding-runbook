---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi
fetched_at: 2026-06-01T05:59:35.749125+00:00
title: "Chi\u1ebfn l\u01b0\u1ee3c thi\u1ebft k\u1ebf c\u00e2u l\u1ec7nh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Chiến lược thiết kế câu lệnh

*Thiết kế câu lệnh* là quá trình tạo câu lệnh hoặc yêu cầu bằng ngôn ngữ tự nhiên để thu thập câu trả lời chính xác, chất lượng cao từ một mô hình ngôn ngữ.

Trang này giới thiệu các khái niệm, chiến lược và phương pháp hay nhất cơ bản để giúp bạn bắt đầu thiết kế câu lệnh nhằm khai thác tối đa các mô hình AI của Gemini.

## Hướng dẫn về câu lệnh theo chủ đề

Bạn đang tìm kiếm các chiến lược tạo câu lệnh cụ thể hơn? Hãy xem các hướng dẫn viết câu lệnh khác của chúng tôi về:

- [Đưa ra câu lệnh bằng tệp đa phương tiện](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide)
- Đưa ra câu lệnh để tạo hình ảnh bằng [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=vi#imagen-prompt-guide) và [Gemini Native Image Generation](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#prompt-guide)
- [Đưa ra câu lệnh để tạo video](https://ai.google.dev/gemini-api/docs/video?hl=vi#prompt-guide)

Bạn có thể tìm thấy các câu lệnh mẫu khác trong [thư viện câu lệnh](https://ai.google.dev/gemini-api/prompts?hl=vi). Thư viện này được thiết kế để minh hoạ một cách tương tác nhiều khái niệm được chia sẻ trong hướng dẫn này.

## Hướng dẫn rõ ràng và cụ thể

Một cách hiệu quả và năng suất để tuỳ chỉnh hành vi của mô hình là cung cấp cho mô hình các chỉ dẫn rõ ràng và cụ thể. Hướng dẫn có thể ở dạng câu hỏi, các bước thực hiện từng nhiệm vụ hoặc phức tạp như lập bản đồ trải nghiệm và tư duy của người dùng.

### Đầu vào

Đầu vào là văn bản bắt buộc trong câu lệnh mà bạn muốn mô hình đưa ra phản hồi. Thông tin đầu vào có thể là một câu hỏi mà mô hình trả lời (thông tin đầu vào câu hỏi), một việc mà mô hình thực hiện (thông tin đầu vào việc), một thực thể mà mô hình hoạt động (thông tin đầu vào thực thể) hoặc thông tin đầu vào một phần mà mô hình hoàn thành hoặc tiếp tục (thông tin đầu vào hoàn thành).

| **Loại nội dung nhập** | **Câu lệnh** | **Nội dung tạo sinh** |
| --- | --- | --- |
| Câu hỏi | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Việc cần làm | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Thực thể | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Hoàn tất một phần dữ liệu đầu vào

Mô hình ngôn ngữ tạo sinh hoạt động như một công cụ tự động hoàn thành nâng cao. Khi bạn cung cấp nội dung một phần, mô hình có thể cung cấp phần còn lại của nội dung hoặc nội dung mà mô hình cho là phần tiếp theo của nội dung đó dưới dạng câu trả lời. Khi bạn làm như vậy, nếu bạn đưa ra ví dụ hoặc bối cảnh, mô hình có thể xem xét những ví dụ hoặc bối cảnh đó.

Ví dụ sau đây cung cấp một câu lệnh có hướng dẫn và dữ liệu đầu vào là thực thể:

|  |
| --- |
| **Câu lệnh:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Phản hồi:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Mặc dù mô hình đã thực hiện theo yêu cầu, nhưng đôi khi việc viết hướng dẫn bằng ngôn ngữ tự nhiên có thể gặp khó khăn và mô hình sẽ phải tự diễn giải rất nhiều.
Ví dụ: thực đơn của nhà hàng có thể chứa nhiều món. Để giảm kích thước của phản hồi JSON, có lẽ bạn nên bỏ qua những mặt hàng chưa được đặt hàng. Trong trường hợp này, bạn có thể đưa ra một ví dụ và tiền tố phản hồi, sau đó để mô hình hoàn thành:

|  |
| --- |
| **Câu lệnh:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Phản hồi:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Lưu ý cách "cheeseburger" bị loại trừ khỏi đầu ra vì không phải là một phần của đơn đặt hàng.

Mặc dù bạn có thể chỉ định định dạng của các đối tượng phản hồi JSON đơn giản bằng cách sử dụng câu lệnh, nhưng bạn nên sử dụng tính năng [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) của Gemini API khi chỉ định một giản đồ JSON phức tạp hơn cho phản hồi.

### Giới hạn

Nêu rõ mọi hạn chế đối với việc đọc câu lệnh hoặc tạo câu trả lời. Bạn có thể cho mô hình biết những việc cần làm và không cần làm. Ví dụ: bạn có thể chỉ định một ràng buộc trong câu lệnh về độ dài mà bạn muốn bản tóm tắt có:

|  |
| --- |
| **Câu lệnh:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Câu trả lời:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Định dạng của phản hồi

Bạn có thể đưa ra chỉ dẫn để chỉ định định dạng của câu trả lời. Ví dụ: bạn có thể yêu cầu định dạng câu trả lời dưới dạng bảng, danh sách có dấu đầu dòng, lời chào bán hàng ngắn gọn, từ khoá, câu hoặc đoạn văn. Chỉ dẫn hệ thống sau đây yêu cầu mô hình phản hồi theo cách trò chuyện hơn:

|  |
| --- |
| **Hướng dẫn của hệ thống**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Câu lệnh**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Phản hồi:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Định dạng câu trả lời bằng chiến lược hoàn tất

[Chiến lược hoàn thành](#completion) cũng có thể giúp định dạng câu trả lời.
Ví dụ sau đây yêu cầu mô hình tạo một dàn ý cho bài luận:

|  |
| --- |
| **Câu lệnh:**    ``` Create an outline for an essay about hummingbirds. ```  **Phản hồi:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

Câu lệnh không chỉ định định dạng cho dàn ý và mô hình đã chọn một định dạng cho bạn. Để mô hình trả về dàn ý ở một định dạng cụ thể, bạn có thể thêm văn bản đại diện cho phần đầu của dàn ý và để mô hình hoàn tất dàn ý đó dựa trên mẫu mà bạn đã bắt đầu.

|  |
| --- |
| **Câu lệnh:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Phản hồi:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Câu lệnh không có ví dụ so với câu lệnh có một vài ví dụ

Bạn có thể đưa ra các ví dụ trong câu lệnh để cho mô hình biết thế nào là câu trả lời đúng. Mô hình này cố gắng xác định các mẫu và mối quan hệ từ các ví dụ, đồng thời áp dụng chúng khi tạo câu trả lời. Những câu lệnh có chứa một vài ví dụ được gọi là câu lệnh *dựa trên một vài ví dụ*, trong khi những câu lệnh không cung cấp ví dụ nào được gọi là câu lệnh *dựa trên không có ví dụ*. Câu lệnh có ít ví dụ thường được dùng để điều chỉnh định dạng, cách diễn đạt, phạm vi hoặc mẫu chung của câu trả lời do mô hình tạo. Sử dụng các ví dụ cụ thể và đa dạng để giúp mô hình thu hẹp phạm vi và tạo ra kết quả chính xác hơn.

Bạn nên luôn thêm một vài ví dụ về few-shot vào câu lệnh. Câu lệnh không có ví dụ ít lần có thể sẽ kém hiệu quả hơn. Trên thực tế, bạn có thể xoá hướng dẫn khỏi câu lệnh nếu các ví dụ của bạn đủ rõ ràng để cho thấy nhiệm vụ cần thực hiện.

Lời nhắc không cần ví dụ sau đây yêu cầu mô hình chọn lời giải thích phù hợp nhất.

|  |
| --- |
| **Câu lệnh:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Phản hồi:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Nếu trường hợp sử dụng của bạn yêu cầu mô hình tạo ra các câu trả lời ngắn gọn, bạn có thể đưa các ví dụ vào câu lệnh ưu tiên câu trả lời ngắn gọn.

Câu lệnh sau đây cung cấp 2 ví dụ cho thấy sự ưu tiên đối với lời giải thích ngắn gọn hơn. Trong câu trả lời, bạn có thể thấy rằng các ví dụ đã hướng dẫn mô hình chọn lời giải thích ngắn hơn (`Explanation2`) thay vì lời giải thích dài hơn (`Explanation1`) như trước đây.

|  |
| --- |
| **Câu lệnh:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Phản hồi:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Số lượng ví dụ tối ưu

Các mô hình như Gemini thường có thể nhận ra các mẫu bằng một vài ví dụ, mặc dù bạn có thể cần thử nghiệm với số lượng ví dụ cần cung cấp trong câu lệnh để đạt được kết quả tốt nhất. Đồng thời, nếu bạn đưa vào quá nhiều ví dụ, mô hình có thể bắt đầu [khớp quá mức](https://developers.google.com/machine-learning/glossary?hl=vi#overfitting) phản hồi với các ví dụ.

### Định dạng nhất quán

Đảm bảo rằng cấu trúc và định dạng của các ví dụ ít lượt tương tác đều giống nhau để tránh các phản hồi có định dạng không mong muốn. Một trong những mục tiêu chính của việc thêm ví dụ ít lần vào câu lệnh là cho mô hình thấy định dạng phản hồi. Do đó, bạn cần đảm bảo định dạng nhất quán trên tất cả các ví dụ, đặc biệt là chú ý đến thẻ XML, khoảng trắng, dòng mới và dấu phân cách ví dụ.

## Thêm ngữ cảnh

Bạn có thể đưa ra hướng dẫn và thông tin trong một câu lệnh mà mô hình cần để giải quyết vấn đề, thay vì giả định rằng mô hình có tất cả thông tin cần thiết. Thông tin theo bối cảnh này giúp mô hình hiểu được các ràng buộc và chi tiết về những việc bạn yêu cầu mô hình thực hiện.

Ví dụ sau đây yêu cầu mô hình đưa ra hướng dẫn khắc phục sự cố cho một bộ định tuyến:

|  |
| --- |
| **Câu lệnh:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Phản hồi:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

Câu trả lời có vẻ là thông tin khắc phục sự cố chung chung, không cụ thể cho bộ định tuyến hoặc trạng thái của đèn chỉ báo LED.

Để tuỳ chỉnh câu trả lời cho bộ định tuyến cụ thể, bạn có thể thêm hướng dẫn khắc phục sự cố của bộ định tuyến vào câu lệnh dưới dạng ngữ cảnh để bộ định tuyến tham khảo khi đưa ra câu trả lời.

|  |
| --- |
| **Câu lệnh:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Phản hồi:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Chia câu lệnh thành các thành phần

Đối với những trường hợp sử dụng đòi hỏi câu lệnh phức tạp, bạn có thể giúp mô hình quản lý độ phức tạp này bằng cách chia nhỏ mọi thứ thành các thành phần đơn giản hơn.

1. **Chia nhỏ hướng dẫn:** Thay vì đưa ra nhiều hướng dẫn trong một câu lệnh, hãy tạo một câu lệnh cho mỗi hướng dẫn. Bạn có thể chọn câu lệnh cần xử lý dựa trên thông tin đầu vào của người dùng.
2. **Kết hợp các câu lệnh:** Đối với những tác vụ phức tạp liên quan đến nhiều bước tuần tự, hãy tạo một câu lệnh cho mỗi bước và kết hợp các câu lệnh với nhau theo một trình tự. Trong chuỗi lời nhắc tuần tự này, đầu ra của một lời nhắc trong chuỗi sẽ trở thành đầu vào của lời nhắc tiếp theo. Kết quả đầu ra của câu lệnh cuối cùng trong chuỗi là kết quả đầu ra cuối cùng.
3. **Tổng hợp phản hồi:** Tổng hợp là khi bạn muốn thực hiện nhiều tác vụ song song trên nhiều phần dữ liệu và tổng hợp kết quả để tạo ra đầu ra cuối cùng. Ví dụ: bạn có thể yêu cầu mô hình thực hiện một thao tác trên phần đầu tiên của dữ liệu, thực hiện một thao tác khác trên phần còn lại của dữ liệu và tổng hợp kết quả.

## Thử nghiệm với các tham số mô hình

Mỗi lệnh gọi mà bạn gửi đến một mô hình đều bao gồm các giá trị tham số kiểm soát cách mô hình tạo ra phản hồi. Mô hình có thể tạo ra các kết quả khác nhau cho các giá trị tham số khác nhau. Thử nghiệm với nhiều giá trị tham số để nhận được các giá trị tốt nhất cho tác vụ. Các tham số có sẵn cho các mô hình khác nhau có thể khác nhau. Sau đây là các tham số phổ biến nhất:

1. **Số lượng mã thông báo đầu ra tối đa:** Chỉ định số lượng mã thông báo tối đa có thể được tạo trong câu trả lời. Một mã thông báo có khoảng 4 ký tự. 100 mã thông báo tương ứng với khoảng 60 đến 80 từ.
2. **Nhiệt độ:** Nhiệt độ kiểm soát mức độ ngẫu nhiên trong việc chọn mã thông báo. Nhiệt độ được dùng để lấy mẫu trong quá trình tạo phản hồi, xảy ra khi áp dụng `topP` và `topK`. Nhiệt độ thấp phù hợp với những câu lệnh yêu cầu câu trả lời mang tính xác định hơn hoặc ít mang tính mở hơn, trong khi nhiệt độ cao có thể dẫn đến kết quả đa dạng hoặc sáng tạo hơn. Nhiệt độ 0 là xác định, tức là phản hồi có xác suất cao nhất luôn được chọn.
3. **`topK`:** Tham số `topK` thay đổi cách mô hình chọn mã thông báo cho đầu ra. `topK` bằng 1 có nghĩa là mã thông báo được chọn có khả năng xuất hiện cao nhất trong số tất cả các mã thông báo trong từ vựng của mô hình (còn gọi là giải mã tham lam), trong khi `topK` bằng 3 có nghĩa là mã thông báo tiếp theo được chọn trong số 3 mã thông báo có khả năng xuất hiện cao nhất bằng cách sử dụng nhiệt độ. Đối với mỗi bước chọn mã thông báo, các mã thông báo `topK` có xác suất cao nhất sẽ được lấy mẫu. Sau đó, các mã thông báo sẽ được lọc thêm dựa trên `topP`, mã thông báo cuối cùng được chọn bằng cách sử dụng phương pháp lấy mẫu nhiệt độ.
4. **`topP`:** Tham số `topP` thay đổi cách mô hình chọn mã thông báo cho đầu ra. Các mã thông báo được chọn từ mã thông báo có khả năng cao nhất đến thấp nhất cho đến khi tổng xác suất của chúng bằng với giá trị `topP`. Ví dụ: nếu các mã thông báo A, B và C có xác suất lần lượt là 0,3, 0,2 và 0,1, đồng thời giá trị `topP` là 0,5, thì mô hình sẽ chọn A hoặc B làm mã thông báo tiếp theo bằng cách sử dụng nhiệt độ và loại trừ C làm ứng cử viên. Giá trị `topP` mặc định là 0,95.
5. **`stop_sequences`:** Đặt một chuỗi dừng để yêu cầu mô hình dừng tạo nội dung. Một chuỗi dừng có thể là bất kỳ chuỗi ký tự nào. Cố gắng tránh sử dụng một chuỗi ký tự có thể xuất hiện trong nội dung được tạo.

## Chiến lược ra lệnh nối tiếp

Đôi khi, bạn cần thiết kế câu lệnh nhiều lần trước khi nhận được câu trả lời mà bạn mong muốn một cách nhất quán. Phần này cung cấp hướng dẫn về một số việc bạn có thể thử khi lặp lại các câu lệnh:

1. **Sử dụng cách diễn đạt khác:** Việc sử dụng các từ hoặc cách diễn đạt khác nhau trong câu lệnh thường mang lại các câu trả lời khác nhau từ mô hình, mặc dù tất cả đều có nghĩa giống nhau. Nếu bạn không nhận được kết quả như mong đợi từ câu lệnh, hãy thử diễn đạt lại câu lệnh đó.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Chuyển sang một việc tương tự:** Nếu bạn không thể khiến mô hình làm theo chỉ dẫn của bạn cho một việc nào đó, hãy thử đưa ra chỉ dẫn cho một việc tương tự để đạt được kết quả tương tự.

   Câu lệnh này yêu cầu mô hình phân loại một cuốn sách bằng cách sử dụng các danh mục được xác định trước:

   |  |
   | --- |
   | **Câu lệnh:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Phản hồi:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   Câu trả lời là chính xác, nhưng mô hình không nằm trong phạm vi của các lựa chọn. Bạn cũng muốn mô hình chỉ phản hồi bằng một trong các lựa chọn thay vì một câu đầy đủ. Trong trường hợp này, bạn có thể diễn đạt lại hướng dẫn dưới dạng câu hỏi trắc nghiệm và yêu cầu mô hình chọn một phương án.

   |  |
   | --- |
   | **Câu lệnh:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Câu trả lời:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Thay đổi thứ tự nội dung trong câu lệnh:** Đôi khi, thứ tự của nội dung trong câu lệnh có thể ảnh hưởng đến câu trả lời. Hãy thử thay đổi thứ tự nội dung và xem điều đó ảnh hưởng đến câu trả lời như thế nào.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Phản hồi dự phòng

Phản hồi dự phòng là phản hồi do mô hình trả về khi câu lệnh hoặc câu trả lời kích hoạt bộ lọc an toàn. Ví dụ về câu trả lời dự phòng là "Tôi không thể giúp bạn về vấn đề đó vì tôi chỉ là một mô hình ngôn ngữ".

Nếu mô hình phản hồi bằng một câu trả lời dự phòng, hãy thử tăng nhiệt độ.

## Liên kết thực tế và thực thi mã

Gemini có thể sử dụng các công cụ để tránh đưa ra thông tin sai lệch trong những trường hợp mà Gemini có thể đưa ra câu trả lời không chính xác.

[Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) kết nối mô hình Gemini với nội dung trên web theo thời gian thực và cần được bật bất cứ khi nào mô hình có thể cần biết những thông tin thực tế không rõ ràng hoặc gần đây.

[Công cụ thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) của Gemini cho phép mô hình tạo và chạy mã Python, đồng thời phải được bật bất cứ khi nào mô hình cần thực hiện bất kỳ loại phép tính số học, đếm hoặc tính toán nào.

## Gemini 3

[Các mô hình Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-3) được thiết kế để lập luận nâng cao và làm theo hướng dẫn.
Các mô hình này phản hồi tốt nhất với những câu lệnh trực tiếp, có cấu trúc rõ ràng, xác định rõ nhiệm vụ và mọi ràng buộc. Bạn nên áp dụng các phương pháp sau đây để đạt được kết quả tối ưu với Gemini 3:

### Nguyên tắc cốt lõi về câu lệnh

- **Chính xác và trực tiếp:** Nêu rõ mục tiêu của bạn một cách rõ ràng và ngắn gọn. Tránh sử dụng ngôn từ không cần thiết hoặc quá thuyết phục.
- **Sử dụng cấu trúc nhất quán:** Sử dụng dấu phân cách rõ ràng để phân tách các phần khác nhau trong câu lệnh. Các thẻ theo kiểu XML (ví dụ: `<context>`, `<task>`) hoặc tiêu đề Markdown đều có hiệu quả. Chọn một định dạng và sử dụng nhất quán trong một câu lệnh.
- **Xác định các tham số:** Giải thích rõ ràng mọi thuật ngữ hoặc tham số mơ hồ.
- **Kiểm soát mức độ chi tiết của câu trả lời:** Theo mặc định, các mô hình Gemini 3 cung cấp câu trả lời trực tiếp và hiệu quả. Nếu cần câu trả lời chi tiết hơn hoặc mang tính trò chuyện hơn, bạn phải yêu cầu rõ ràng trong chỉ dẫn.
- **Xử lý nhất quán các thông tin đầu vào đa phương thức:** Khi sử dụng văn bản, hình ảnh, âm thanh hoặc video, hãy coi chúng là các thông tin đầu vào thuộc cùng một loại. Đảm bảo hướng dẫn của bạn tham chiếu rõ ràng đến từng phương thức khi cần.
- **Ưu tiên các chỉ dẫn quan trọng:** Đặt các ràng buộc hành vi thiết yếu, định nghĩa vai trò (persona) và yêu cầu về định dạng đầu ra trong Chỉ dẫn hệ thống hoặc ngay từ đầu lời nhắc của người dùng.
- **Cấu trúc cho bối cảnh dài:** Khi cung cấp một lượng lớn bối cảnh (ví dụ: tài liệu, mã), trước tiên hãy cung cấp tất cả bối cảnh. Đặt chỉ dẫn hoặc câu hỏi cụ thể của bạn ở *cuối* câu lệnh.
- **Ngữ cảnh liên kết:** Sau một khối dữ liệu lớn, hãy sử dụng một cụm từ chuyển đổi rõ ràng để kết nối ngữ cảnh và câu hỏi của bạn, chẳng hạn như "Dựa trên thông tin ở trên..."

### Chiến lược Gemini 3 Flash

- **Độ chính xác của ngày hiện tại:** Thêm mệnh đề sau vào hướng dẫn hệ thống để giúp mô hình chú ý đến ngày hiện tại là năm 2026:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Độ chính xác của điểm cắt kiến thức:** Thêm mệnh đề sau vào chỉ dẫn hệ thống để mô hình biết về điểm cắt kiến thức của mình:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Hiệu quả liên kết thực tế:** Thêm mệnh đề sau vào chỉ dẫn hệ thống (chỉnh sửa nếu thích hợp) để cải thiện khả năng liên kết thực tế của mô hình trong ngữ cảnh được cung cấp:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Nâng cao khả năng suy luận và lập kế hoạch

Các mô hình Gemini 2.5 và 3 tự động tạo văn bản "suy nghĩ" nội bộ để cải thiện hiệu suất suy luận. Do đó, bạn thường không cần phải có dàn ý, kế hoạch hoặc các bước suy luận chi tiết của mô hình trong chính phản hồi được trả về. Đối với những vấn đề đòi hỏi khả năng suy luận cao, các yêu cầu đơn giản như "Hãy suy nghĩ thật kỹ trước khi trả lời" có thể cải thiện hiệu suất, mặc dù phải trả giá bằng các mã thông báo suy nghĩ bổ sung.

Hãy xem tài liệu về [Cách Gemini suy nghĩ](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) để biết thêm thông tin chi tiết.

### Ví dụ về câu lệnh có cấu trúc

Việc sử dụng thẻ hoặc Markdown giúp mô hình phân biệt giữa hướng dẫn, bối cảnh và nhiệm vụ.

**Ví dụ về XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Ví dụ về cách đánh dấu:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Ví dụ về mẫu kết hợp các phương pháp hay nhất

Mẫu này ghi lại các nguyên tắc cốt lõi để đưa ra câu lệnh cho Gemini 3. Luôn đảm bảo lặp lại và sửa đổi cho trường hợp sử dụng cụ thể của bạn.

**Hướng dẫn của hệ thống:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Câu lệnh của người dùng:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Quy trình làm việc dựa trên trợ lý AI

Đối với quy trình làm việc sâu của tác nhân, bạn thường cần có hướng dẫn cụ thể để kiểm soát cách mô hình suy luận, lập kế hoạch và thực hiện các tác vụ. Mặc dù Gemini mang lại hiệu suất chung mạnh mẽ, nhưng các tác nhân phức tạp thường yêu cầu bạn định cấu hình sự đánh đổi giữa chi phí tính toán (độ trễ và token) và độ chính xác của tác vụ.

Khi thiết kế câu lệnh cho các tác nhân, hãy cân nhắc những khía cạnh sau đây về hành vi mà bạn có thể điều hướng trong tác nhân:

### Suy luận và chiến lược

Cấu hình cho cách mô hình suy nghĩ và lập kế hoạch trước khi hành động.

- **Phân tích logic:** Xác định mức độ kỹ lưỡng mà mô hình phải phân tích các quy tắc ràng buộc, điều kiện tiên quyết và thứ tự hoạt động.
- **Chẩn đoán vấn đề**: Kiểm soát mức độ phân tích khi xác định nguyên nhân và việc sử dụng suy luận bắt cầu của mô hình. Xác định xem mô hình có nên chấp nhận câu trả lời rõ ràng nhất hay khám phá những lời giải thích phức tạp, ít có khả năng hơn.
- **Tính đầy đủ của thông tin:** Sự đánh đổi giữa việc phân tích mọi chính sách và tài liệu có sẵn so với việc ưu tiên hiệu quả và tốc độ.

### Thực thi và độ tin cậy

Cấu hình về cách tác nhân hoạt động độc lập và xử lý các trở ngại.

- **Khả năng thích ứng:** Cách mô hình phản ứng với dữ liệu mới. Xác định xem có nên tuân thủ nghiêm ngặt kế hoạch ban đầu hay chuyển hướng ngay lập tức khi các quan sát mâu thuẫn với các giả định.
- **Tính kiên trì và khả năng phục hồi:** Mức độ mà mô hình cố gắng tự sửa lỗi. Độ duy trì cao sẽ làm tăng tỷ lệ thành công nhưng có nguy cơ tăng chi phí mã thông báo hoặc vòng lặp.
- **Đánh giá rủi ro:** Logic để đánh giá hậu quả. Phân biệt rõ ràng giữa các thao tác khám phá có rủi ro thấp (đọc) và các thay đổi trạng thái có rủi ro cao (ghi).

### Tương tác và đầu ra

Cấu hình về cách nhân viên hỗ trợ giao tiếp với người dùng và định dạng kết quả.

- **Tính mơ hồ và cách xử lý quyền:** Xác định thời điểm mô hình được phép đưa ra giả định so với thời điểm mô hình phải tạm dừng thực thi để yêu cầu người dùng làm rõ hoặc cấp quyền.
- **Độ chi tiết:** Kiểm soát lượng văn bản được tạo cùng với các lệnh gọi công cụ. Điều này xác định xem mô hình có giải thích hành động của mình cho người dùng hay không, hoặc vẫn im lặng trong quá trình thực thi.
- **Độ chính xác và tính đầy đủ:** Độ trung thực bắt buộc của đầu ra. Xác định xem mô hình có phải giải quyết mọi trường hợp đặc biệt và cung cấp số liệu chính xác hay không, hoặc có chấp nhận ước tính sơ bộ hay không.

### Mẫu hướng dẫn hệ thống

Sau đây là ví dụ về chỉ dẫn hệ thống đã được các nhà nghiên cứu đánh giá để cải thiện hiệu suất trên các điểm chuẩn dựa trên tác nhân, trong đó mô hình phải tuân thủ một bộ quy tắc phức tạp và tương tác với người dùng. Điều này khuyến khích tác nhân đóng vai trò là một người lập luận và lập kế hoạch hiệu quả, thực thi các hành vi cụ thể trên các phương diện nêu trên và yêu cầu mô hình chủ động lập kế hoạch trước khi thực hiện bất kỳ hành động nào.

Bạn có thể điều chỉnh mẫu này cho phù hợp với các ràng buộc trong trường hợp sử dụng cụ thể của mình.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Các bước tiếp theo

- Giờ đây, khi đã hiểu rõ hơn về cách thiết kế câu lệnh, hãy thử viết câu lệnh của riêng bạn bằng [Google AI Studio](http://aistudio.google.com?hl=vi).
- Để tìm hiểu về tính năng tạo câu lệnh đa phương thức, hãy xem bài viết [Tạo câu lệnh bằng tệp đa phương tiện](https://ai.google.dev/gemini-api/docs/files?hl=vi#prompt-guide).
- Để tìm hiểu về cách đặt câu lệnh cho hình ảnh, hãy xem hướng dẫn đặt câu lệnh cho [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#prompt-guide) và [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=vi#imagen-prompt-guide).
- Để tìm hiểu về câu lệnh cho video, hãy xem [hướng dẫn về câu lệnh cho Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi#prompt-guide).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
