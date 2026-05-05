---
source_url: https://ai.google.dev/gemini-api/docs/computer-use?hl=vi
fetched_at: 2026-05-05T19:46:31.838766+00:00
title: "S\u1eed d\u1ee5ng m\u00e1y t\u00ednh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Sử dụng máy tính

Tính năng Sử dụng máy tính cho phép bạn tạo các tác nhân kiểm soát trình duyệt tương tác và tự động hoá các tác vụ. Bằng cách sử dụng ảnh chụp màn hình, mô hình này có thể "nhìn thấy" màn hình máy tính và "hành động" bằng cách tạo các thao tác cụ thể trên giao diện người dùng, chẳng hạn như thao tác nhấp chuột và thao tác nhập bằng bàn phím. Tương tự như lệnh gọi hàm, bạn cần viết mã xử lý ứng dụng phía máy khách để nhận và thực thi các thao tác Sử dụng máy tính.

Với tính năng Sử dụng máy tính, bạn có thể tạo các tác nhân có khả năng:

- Tự động hoá việc nhập dữ liệu hoặc điền biểu mẫu lặp đi lặp lại trên các trang web.
- Thực hiện kiểm thử tự động các ứng dụng web và quy trình của người dùng
- Nghiên cứu trên nhiều trang web (ví dụ: thu thập thông tin sản phẩm, giá cả và bài đánh giá từ các trang web thương mại điện tử để đưa ra quyết định mua hàng)

Cách dễ nhất để kiểm thử tính năng Sử dụng máy tính là thông qua [triển khai tham chiếu](https://github.com/google/computer-use-preview/) hoặc [môi trường minh hoạ Browserbase](http://gemini.browserbase.com).

## Cách hoạt động của tính năng Sử dụng máy tính

Để tạo một tác nhân kiểm soát trình duyệt bằng mô hình Sử dụng máy tính, hãy triển khai một vòng lặp tác nhân thực hiện những việc sau:

1. [**Gửi yêu cầu đến mô hình**](#send-request)

   - Thêm công cụ Sử dụng máy tính và tuỳ ý thêm mọi hàm do người dùng xác định tuỳ chỉnh hoặc hàm bị loại trừ vào yêu cầu API của bạn.
   - Nhắc mô hình Sử dụng máy tính bằng yêu cầu của người dùng.
2. [**Nhận câu trả lời của mô hình**](#model-response)

   - Mô hình Sử dụng máy tính phân tích yêu cầu và ảnh chụp màn hình của người dùng, đồng thời tạo ra một phản hồi bao gồm `function_call` được đề xuất, đại diện cho một thao tác trên giao diện người dùng (ví dụ: "nhấp vào toạ độ (x,y)" hoặc "nhập "văn bản""). Để biết nội dung mô tả về tất cả các thao tác trên giao diện người dùng mà mô hình Sử dụng máy tính hỗ trợ, hãy xem phần [Các thao tác được hỗ trợ](#supported-actions).
   - Phản hồi của API cũng có thể bao gồm một `safety_decision` từ hệ thống an toàn nội bộ, hệ thống này sẽ kiểm tra hành động được đề xuất của mô hình. `safety_decision` này phân loại hành động như sau:
     - **Thông thường / được phép:** Hành động này được coi là an toàn. Điều này cũng có thể được biểu thị bằng việc không có `safety_decision`.
     - **Yêu cầu xác nhận (`require_confirmation`):** Mô hình sắp thực hiện một hành động có thể gây rủi ro (ví dụ: nhấp vào "biểu ngữ về cookie").
3. [**Thực hiện hành động đã nhận được**](#execute-actions)

   - Mã phía máy khách của bạn sẽ nhận được `function_call` và mọi `safety_decision` đi kèm.
     - **Thông thường / được phép:** Nếu `safety_decision` cho biết thông thường/được phép (hoặc nếu không có `safety_decision`), mã phía máy khách của bạn có thể thực thi `function_call` đã chỉ định trong môi trường mục tiêu (ví dụ: trình duyệt web).
     - **Yêu cầu xác nhận:** Nếu `safety_decision` cho biết yêu cầu xác nhận, thì ứng dụng của bạn phải nhắc người dùng cuối xác nhận trước khi thực thi `function_call`. Nếu người dùng xác nhận, hãy tiến hành thực hiện hành động. Nếu người dùng từ chối, đừng thực hiện hành động.
4. [**Ghi lại trạng thái môi trường mới**](#capture-state)

   - Nếu hành động đã được thực hiện, ứng dụng sẽ chụp một ảnh chụp màn hình mới của GUI và URL hiện tại để gửi lại cho mô hình Sử dụng máy tính trong `function_response`.
   - Nếu một hành động bị hệ thống an toàn chặn hoặc người dùng từ chối xác nhận, thì ứng dụng của bạn có thể gửi một dạng thông tin phản hồi khác cho mô hình hoặc kết thúc hoạt động tương tác.

Quy trình này lặp lại từ bước 2 với mô hình sử dụng ảnh chụp màn hình mới và mục tiêu đang diễn ra để đề xuất hành động tiếp theo. Vòng lặp tiếp tục cho đến khi tác vụ hoàn tất, xảy ra lỗi hoặc quy trình bị chấm dứt (ví dụ: do phản hồi an toàn "chặn" hoặc quyết định của người dùng).

![Tổng quan về việc sử dụng máy tính](https://ai.google.dev/static/gemini-api/docs/images/computer_use.png?hl=vi)

## Cách triển khai tính năng Sử dụng máy tính

Trước khi tạo bằng công cụ Sử dụng máy tính, bạn cần thiết lập những nội dung sau:

- **Môi trường thực thi an toàn:** Vì lý do an toàn, bạn nên chạy tác nhân Sử dụng máy tính trong một môi trường an toàn và có kiểm soát (ví dụ: máy ảo hộp cát, một vùng chứa hoặc một hồ sơ trình duyệt chuyên dụng có quyền hạn hạn chế).
- **Trình xử lý thao tác phía máy khách:** Bạn sẽ cần triển khai logic phía máy khách để thực thi các thao tác do mô hình tạo và chụp ảnh màn hình của môi trường sau mỗi thao tác.

Các ví dụ trong phần này sử dụng trình duyệt làm môi trường thực thi và [Playwright](https://playwright.dev/) làm trình xử lý hành động phía máy khách. Để chạy các mẫu này, bạn phải cài đặt các phần phụ thuộc cần thiết và khởi tạo một phiên bản trình duyệt Playwright.

#### Cài đặt Playwright

```
    pip install google-genai playwright
    playwright install chromium
```

#### Khởi chạy phiên bản trình duyệt Playwright

```
    from playwright.sync_api import sync_playwright

    # 1. Configure screen dimensions for the target environment
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 900

    # 2. Start the Playwright browser
    # In production, utilize a sandboxed environment.
    playwright = sync_playwright().start()
    # Set headless=False to see the actions performed on your screen
    browser = playwright.chromium.launch(headless=False)

    # 3. Create a context and page with the specified dimensions
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT}
    )
    page = context.new_page()

    # 4. Navigate to an initial page to start the task
    page.goto("https://www.google.com")

    # The 'page', 'SCREEN_WIDTH', and 'SCREEN_HEIGHT' variables
    # will be used in the steps below.
```

Mã mẫu để mở rộng sang môi trường Android có trong phần [Sử dụng các hàm tuỳ chỉnh do người dùng xác định](#custom-functions).

### 1. Gửi yêu cầu đến mô hình

Thêm công cụ Sử dụng máy tính vào yêu cầu API và gửi một câu lệnh cho mô hình có chứa mục tiêu của người dùng. Bạn phải sử dụng một trong các mẫu được hỗ trợ cho mục đích Sử dụng máy tính, nếu không bạn sẽ gặp lỗi:

- `gemini-2.5-computer-use-preview-10-2025`
- `gemini-3-flash-preview`

Bạn cũng có thể thêm các tham số sau (không bắt buộc):

- **Các thao tác bị loại trừ:** Nếu có bất kỳ thao tác nào trong danh sách [Các thao tác được hỗ trợ trên giao diện người dùng](#supported-actions) mà bạn không muốn mô hình thực hiện, hãy chỉ định các thao tác này là `excluded_predefined_functions`.
- **Hàm do người dùng xác định:** Ngoài công cụ Sử dụng máy tính, bạn có thể muốn thêm các hàm tuỳ chỉnh do người dùng xác định.

Xin lưu ý rằng bạn không cần chỉ định kích thước hiển thị khi đưa ra yêu cầu; mô hình dự đoán toạ độ pixel được điều chỉnh theo chiều cao và chiều rộng của màn hình.

### Python

```
from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

# Specify predefined functions to exclude (optional)
excluded_functions = ["drag_and_drop"]

generate_content_config = genai.types.GenerateContentConfig(
    tools=[
        # 1. Computer Use tool with browser environment
        types.Tool(
            computer_use=types.ComputerUse(
                environment=types.Environment.ENVIRONMENT_BROWSER,
                # Optional: Exclude specific predefined functions
                excluded_predefined_functions=excluded_functions
                )
              ),
        # 2. Optional: Custom user-defined functions
        #types.Tool(
          # function_declarations=custom_functions
          #   )
          ],
  )

# Create the content with user message
contents=[
    Content(
        role="user",
        parts=[
            Part(text="Search for highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping. Create a bulleted list of the 3 cheapest options in the format of name, description, price in an easy-to-read layout."),
        ],
    )
]

# Generate content with the configured settings
response = client.models.generate_content(
    model='gemini-2.5-computer-use-preview-10-2025',
    contents=contents,
    config=generate_content_config,
)

# Print the response output
print(response)
```

Để xem ví dụ về các hàm tuỳ chỉnh, hãy xem phần [Sử dụng các hàm do người dùng xác định tuỳ chỉnh](#custom-functions).

### 2. Nhận câu trả lời của mô hình

Khi bạn bật công cụ Sử dụng máy tính, mô hình sẽ phản hồi bằng một hoặc nhiều `FunctionCalls` nếu xác định rằng cần có hành động trên giao diện người dùng để hoàn tất tác vụ.
Tính năng Sử dụng máy tính hỗ trợ gọi hàm song song, tức là mô hình có thể trả về nhiều thao tác trong một lượt.

Sau đây là một ví dụ về câu trả lời của mô hình.

```
{
  "content": {
    "parts": [
      {
        "text": "I will type the search query into the search bar. The search bar is in the center of the page."
      },
      {
        "function_call": {
          "name": "type_text_at",
          "args": {
            "x": 371,
            "y": 470,
            "text": "highly rated smart fridges with touchscreen, 2 doors, around 25 cu ft, priced below 4000 dollars on Google Shopping",
            "press_enter": true
          }
        }
      }
    ]
  }
}
```

### 3. Thực thi các thao tác đã nhận

Mã xử lý ứng dụng của bạn cần phân tích cú pháp phản hồi của mô hình, thực thi các hành động và thu thập kết quả.

Đoạn mã ví dụ bên dưới trích xuất các lệnh gọi hàm từ phản hồi của mô hình Sử dụng máy tính và dịch chúng thành các thao tác có thể thực thi bằng Playwright.
Mô hình này xuất ra các toạ độ được chuẩn hoá (0-999) bất kể kích thước hình ảnh đầu vào, vì vậy, một phần của bước dịch là chuyển đổi các toạ độ được chuẩn hoá này trở lại các giá trị điểm ảnh thực tế.

Kích thước màn hình được đề xuất để sử dụng với mô hình Sử dụng máy tính là (1440, 900). Mô hình này sẽ hoạt động với mọi độ phân giải, mặc dù chất lượng của kết quả có thể bị ảnh hưởng.

Xin lưu ý rằng ví dụ này chỉ bao gồm việc triển khai cho 3 thao tác phổ biến nhất trên giao diện người dùng: `open_web_browser`, `click_at` và `type_text_at`. Đối với các trường hợp sử dụng trong thực tế, bạn sẽ cần triển khai tất cả các thao tác khác trên giao diện người dùng trong danh sách [Các thao tác được hỗ trợ](#supported-actions), trừ phi bạn thêm các thao tác đó một cách rõ ràng dưới dạng `excluded_predefined_functions`.

### Python

```
from typing import Any, List, Tuple
import time

def denormalize_x(x: int, screen_width: int) -> int:
    """Convert normalized x coordinate (0-1000) to actual pixel coordinate."""
    return int(x / 1000 * screen_width)

def denormalize_y(y: int, screen_height: int) -> int:
    """Convert normalized y coordinate (0-1000) to actual pixel coordinate."""
    return int(y / 1000 * screen_height)

def execute_function_calls(candidate, page, screen_width, screen_height):
    results = []
    function_calls = []
    for part in candidate.content.parts:
        if part.function_call:
            function_calls.append(part.function_call)

    for function_call in function_calls:
        action_result = {}
        fname = function_call.name
        args = function_call.args
        print(f"  -> Executing: {fname}")

        try:
            if fname == "open_web_browser":
                pass # Already open
            elif fname == "click_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                page.mouse.click(actual_x, actual_y)
            elif fname == "type_text_at":
                actual_x = denormalize_x(args["x"], screen_width)
                actual_y = denormalize_y(args["y"], screen_height)
                text = args["text"]
                press_enter = args.get("press_enter", False)

                page.mouse.click(actual_x, actual_y)
                # Simple clear (Command+A, Backspace for Mac)
                page.keyboard.press("Meta+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(text)
                if press_enter:
                    page.keyboard.press("Enter")
            else:
                print(f"Warning: Unimplemented or custom function {fname}")

            # Wait for potential navigations/renders
            page.wait_for_load_state(timeout=5000)
            time.sleep(1)

        except Exception as e:
            print(f"Error executing {fname}: {e}")
            action_result = {"error": str(e)}

        results.append((fname, action_result))

    return results
```

### 4. Ghi lại trạng thái môi trường mới

Sau khi thực hiện các hành động, hãy gửi kết quả thực thi hàm trở lại mô hình để mô hình có thể sử dụng thông tin này để tạo hành động tiếp theo. Nếu thực hiện nhiều thao tác (cuộc gọi song song), bạn phải gửi một `FunctionResponse` cho từng thao tác trong lượt tương tác tiếp theo của người dùng.

### Python

```
def get_function_responses(page, results):
    screenshot_bytes = page.screenshot(type="png")
    current_url = page.url
    function_responses = []
    for name, result in results:
        response_data = {"url": current_url}
        response_data.update(result)
        function_responses.append(
            types.FunctionResponse(
                name=name,
                response=response_data,
                parts=[types.FunctionResponsePart(
                        inline_data=types.FunctionResponseBlob(
                            mime_type="image/png",
                            data=screenshot_bytes))
                ]
            )
        )
    return function_responses
```

## Tạo vòng lặp tác nhân

Để bật các lượt tương tác nhiều bước, hãy kết hợp 4 bước trong phần [Cách triển khai việc sử dụng máy tính](#implement-computer-use) thành một vòng lặp.
Hãy nhớ quản lý nhật ký trò chuyện một cách chính xác bằng cách thêm cả câu trả lời của mô hình và câu trả lời của hàm.

Để chạy mã mẫu này, bạn cần:

- Cài đặt [các phần phụ thuộc cần thiết của Playwright](#expandable-1).
- Xác định các hàm trợ giúp từ các bước [(3) Thực thi các thao tác đã nhận](#execute-actions) và [(4) Ghi lại trạng thái môi trường mới](#capture-state).

### Python

```
import time
from typing import Any, List, Tuple
from playwright.sync_api import sync_playwright

from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

# Constants for screen dimensions
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900

# Setup Playwright
print("Initializing browser...")
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT})
page = context.new_page()

# Define helper functions. Copy/paste from steps 3 and 4
# def denormalize_x(...)
# def denormalize_y(...)
# def execute_function_calls(...)
# def get_function_responses(...)

try:
    # Go to initial page
    page.goto("https://ai.google.dev/gemini-api/docs")

    # Configure the model (From Step 1)
    config = types.GenerateContentConfig(
        tools=[types.Tool(computer_use=types.ComputerUse(
            environment=types.Environment.ENVIRONMENT_BROWSER
        ))],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    )

    # Initialize history
    initial_screenshot = page.screenshot(type="png")
    USER_PROMPT = "Go to ai.google.dev/gemini-api/docs and search for pricing."
    print(f"Goal: {USER_PROMPT}")

    contents = [
        Content(role="user", parts=[
            Part(text=USER_PROMPT),
            Part.from_bytes(data=initial_screenshot, mime_type='image/png')
        ])
    ]

    # Agent Loop
    turn_limit = 5
    for i in range(turn_limit):
        print(f"\n--- Turn {i+1} ---")
        print("Thinking...")
        response = client.models.generate_content(
            model='gemini-2.5-computer-use-preview-10-2025',
            contents=contents,
            config=config,
        )

        candidate = response.candidates[0]
        contents.append(candidate.content)

        has_function_calls = any(part.function_call for part in candidate.content.parts)
        if not has_function_calls:
            text_response = " ".join([part.text for part in candidate.content.parts if part.text])
            print("Agent finished:", text_response)
            break

        print("Executing actions...")
        results = execute_function_calls(candidate, page, SCREEN_WIDTH, SCREEN_HEIGHT)

        print("Capturing state...")
        function_responses = get_function_responses(page, results)

        contents.append(
            Content(role="user", parts=[Part(function_response=fr) for fr in function_responses])
        )

finally:
    # Cleanup
    print("\nClosing browser...")
    browser.close()
    playwright.stop()
```

## Sử dụng hàm tuỳ chỉnh do người dùng xác định

Bạn có thể tuỳ ý thêm các hàm do người dùng xác định tuỳ chỉnh vào yêu cầu để mở rộng chức năng của mô hình. Ví dụ dưới đây điều chỉnh mô hình và công cụ Sử dụng máy tính cho các trường hợp sử dụng trên thiết bị di động bằng cách thêm các thao tác tuỳ chỉnh do người dùng xác định như `open_app`, `long_press_at` và `go_home`, đồng thời loại trừ các thao tác dành riêng cho trình duyệt. Mô hình này có thể gọi một cách thông minh các hàm tuỳ chỉnh này cùng với các thao tác chuẩn trên giao diện người dùng để hoàn thành các tác vụ trong môi trường không phải trình duyệt.

### Python

```
from typing import Optional, Dict, Any

from google import genai
from google.genai import types
from google.genai.types import Content, Part

client = genai.Client()

SYSTEM_PROMPT = """You are operating an Android phone. Today's date is October 15, 2023, so ignore any other date provided.
* To provide an answer to the user, *do not use any tools* and output your answer on a separate line. IMPORTANT: Do not add any formatting or additional punctuation/text, just output the answer by itself after two empty lines.
* Make sure you scroll down to see everything before deciding something isn't available.
* You can open an app from anywhere. The icon doesn't have to currently be on screen.
* Unless explicitly told otherwise, make sure to save any changes you make.
* If text is cut off or incomplete, scroll or click into the element to get the full text before providing an answer.
* IMPORTANT: Complete the given task EXACTLY as stated. DO NOT make any assumptions that completing a similar task is correct.  If you can't find what you're looking for, SCROLL to find it.
* If you want to edit some text, ONLY USE THE `type` tool. Do not use the onscreen keyboard.
* Quick settings shouldn't be used to change settings. Use the Settings app instead.
* The given task may already be completed. If so, there is no need to do anything.
"""

def open_app(app_name: str, intent: Optional[str] = None) -> Dict[str, Any]:
    """Opens an app by name.

    Args:
        app_name: Name of the app to open (any string).
        intent: Optional deep-link or action to pass when launching, if the app supports it.

    Returns:
        JSON payload acknowledging the request (app name and optional intent).
    """
    return {"status": "requested_open", "app_name": app_name, "intent": intent}

def long_press_at(x: int, y: int) -> Dict[str, int]:
    """Long-press at a specific screen coordinate.

    Args:
        x: X coordinate (absolute), scaled to the device screen width (pixels).
        y: Y coordinate (absolute), scaled to the device screen height (pixels).

    Returns:
        Object with the coordinates pressed and the duration used.
    """
    return {"x": x, "y": y}

def go_home() -> Dict[str, str]:
    """Navigates to the device home screen.

    Returns:
        A small acknowledgment payload.
    """
    return {"status": "home_requested"}

#  Build function declarations
CUSTOM_FUNCTION_DECLARATIONS = [
    types.FunctionDeclaration.from_callable(client=client, callable=open_app),
    types.FunctionDeclaration.from_callable(client=client, callable=long_press_at),
    types.FunctionDeclaration.from_callable(client=client, callable=go_home),
]

#Exclude browser functions
EXCLUDED_PREDEFINED_FUNCTIONS = [
    "open_web_browser",
    "search",
    "navigate",
    "hover_at",
    "scroll_document",
    "go_forward",
    "key_combination",
    "drag_and_drop",
]

#Utility function to construct a GenerateContentConfig
def make_generate_content_config() -> genai.types.GenerateContentConfig:
    """Return a fixed GenerateContentConfig with Computer Use + custom functions."""
    return genai.types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[
            types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                    excluded_predefined_functions=EXCLUDED_PREDEFINED_FUNCTIONS,
                )
            ),
            types.Tool(function_declarations=CUSTOM_FUNCTION_DECLARATIONS),
        ],
    )

# Create the content with user message
contents: list[Content] = [
    Content(
        role="user",
        parts=[
            # text instruction
            Part(text="Open Chrome, then long-press at 200,400."),
        ],
    )
]

# Build your fixed config (from helper)
config = make_generate_content_config()

# Generate content with the configured settings
response = client.models.generate_content(
        model='gemini-2.5-computer-use-preview-10-2025',
        contents=contents,
        config=config,
    )

print(response)
```

## Các thao tác được hỗ trợ trên giao diện người dùng

Mô hình có thể yêu cầu các thao tác sau trên giao diện người dùng thông qua `FunctionCall`. Mã phía máy khách của bạn phải triển khai logic thực thi cho các thao tác này. Hãy xem [triển khai tham chiếu](https://github.com/google/computer-use-preview) để biết các ví dụ.

| Tên lệnh | Mô tả | Đối số (trong Lệnh gọi hàm) | Ví dụ về lệnh gọi hàm |
| --- | --- | --- | --- |
| **open\_web\_browser** | Mở trình duyệt web. | Không có | `{"name": "open_web_browser", "args": {}}` |
| **wait\_5\_seconds** | Tạm dừng thực thi trong 5 giây để cho phép nội dung động tải hoặc hoạt ảnh hoàn tất. | Không có | `{"name": "wait_5_seconds", "args": {}}` |
| **go\_back** | Chuyển đến trang trước trong nhật ký của trình duyệt. | Không có | `{"name": "go_back", "args": {}}` |
| **go\_forward** | Chuyển đến trang tiếp theo trong nhật ký của trình duyệt. | Không có | `{"name": "go_forward", "args": {}}` |
| **search** | Chuyển đến trang chủ của công cụ tìm kiếm mặc định (ví dụ: Google). Hữu ích khi bắt đầu một nhiệm vụ tìm kiếm mới. | Không có | `{"name": "search", "args": {}}` |
| **navigate** | Điều hướng trình duyệt trực tiếp đến URL đã chỉ định. | `url`: str | `{"name": "navigate", "args": {"url": "https://www.wikipedia.org"}}` |
| **click\_at** | Nhấp vào một toạ độ cụ thể trên trang web. Các giá trị x và y dựa trên lưới 1000x1000 và được điều chỉnh theo kích thước màn hình. | `y`: int (0-999), `x`: int (0-999) | `{"name": "click_at", "args": {"y": 300, "x": 500}}` |
| **hover\_at** | Di chuột đến một toạ độ cụ thể trên trang web. Hữu ích khi hiển thị các trình đơn con. x và y dựa trên lưới 1000x1000. | `y`: int (0-999) `x`: int (0-999) | `{"name": "hover_at", "args": {"y": 150, "x": 250}}` |
| **type\_text\_at** | Nhập văn bản tại một toạ độ cụ thể, theo mặc định, trước tiên sẽ xoá trường và nhấn ENTER sau khi nhập, nhưng bạn có thể tắt các thao tác này. x và y dựa trên lưới 1000x1000. | `y`: int (0-999), `x`: int (0-999), `text`: str, `press_enter`: bool (Không bắt buộc, mặc định là True), `clear_before_typing`: bool (Không bắt buộc, mặc định là True) | `{"name": "type_text_at", "args": {"y": 250, "x": 400, "text": "search query", "press_enter": false}}` |
| **key\_combination** | Nhấn các phím hoặc tổ hợp phím trên bàn phím, chẳng hạn như "Control+C" hoặc "Enter". Hữu ích cho việc kích hoạt các hành động (chẳng hạn như gửi biểu mẫu bằng phím "Enter") hoặc các thao tác trên bảng nhớ tạm. | `keys`: str (ví dụ: "enter", "control+c"). | `{"name": "key_combination", "args": {"keys": "Control+A"}}` |
| **scroll\_document** | Cuộn toàn bộ trang web "lên", "xuống", "trái" hoặc "phải". | `direction`: str ("up", "down", "left" hoặc "right") | `{"name": "scroll_document", "args": {"direction": "down"}}` |
| **scroll\_at** | Di chuyển một phần tử hoặc khu vực cụ thể tại toạ độ (x, y) theo hướng đã chỉ định với một độ lớn nhất định. Toạ độ và độ lớn (mặc định là 800) dựa trên lưới 1000x1000. | `y`: int (0-999), `x`: int (0-999), `direction`: str ("up", "down", "left", "right"), `magnitude`: int (0-999, Không bắt buộc, mặc định là 800) | `{"name": "scroll_at", "args": {"y": 500, "x": 500, "direction": "down", "magnitude": 400}}` |
| **drag\_and\_drop** | Kéo một phần tử từ toạ độ bắt đầu (x, y) và thả phần tử đó tại toạ độ đích (destination\_x, destination\_y). Tất cả toạ độ đều dựa trên lưới 1000x1000. | `y`: int (0-999), `x`: int (0-999), `destination_y`: int (0-999), `destination_x`: int (0-999) | `{"name": "drag_and_drop", "args": {"y": 100, "x": 100, "destination_y": 500, "destination_x": 500}}` |

## An toàn và bảo mật

### Xác nhận quyết định về sự an toàn

Tuỳ thuộc vào hành động, phản hồi của mô hình cũng có thể bao gồm một `safety_decision` từ hệ thống an toàn nội bộ để kiểm tra hành động được đề xuất của mô hình.

```
{
  "content": {
    "parts": [
      {
        "text": "I have evaluated step 2. It seems Google detected unusual traffic and is asking me to verify I'm not a robot. I need to click the 'I'm not a robot' checkbox located near the top left (y=98, x=95).",
      },
      {
        "function_call": {
          "name": "click_at",
          "args": {
            "x": 60,
            "y": 100,
            "safety_decision": {
              "explanation": "I have encountered a CAPTCHA challenge that requires interaction. I need you to complete the challenge by clicking the 'I'm not a robot' checkbox and any subsequent verification steps.",
              "decision": "require_confirmation"
            }
          }
        }
      }
    ]
  }
}
```

Nếu `safety_decision` là `require_confirmation`, bạn phải yêu cầu người dùng cuối xác nhận trước khi tiến hành thực hiện hành động. Theo [điều khoản dịch vụ](https://ai.google.dev/gemini-api/terms?hl=vi), bạn không được phép bỏ qua yêu cầu xác nhận của người dùng.

Mã mẫu này nhắc người dùng cuối xác nhận trước khi thực thi hành động. Nếu người dùng không xác nhận hành động, thì vòng lặp sẽ kết thúc. Nếu người dùng xác nhận hành động, hành động sẽ được thực thi và trường `safety_acknowledgement` sẽ được đánh dấu là `True`.

### Python

```
import termcolor

def get_safety_confirmation(safety_decision):
    """Prompt user for confirmation when safety check is triggered."""
    termcolor.cprint("Safety service requires explicit confirmation!", color="red")
    print(safety_decision["explanation"])

    decision = ""
    while decision.lower() not in ("y", "n", "ye", "yes", "no"):
        decision = input("Do you wish to proceed? [Y]es/[N]o\n")

    if decision.lower() in ("n", "no"):
        return "TERMINATE"
    return "CONTINUE"

def execute_function_calls(candidate, page, screen_width, screen_height):

    # ... Extract function calls from response ...

    for function_call in function_calls:
        extra_fr_fields = {}

        # Check for safety decision
        if 'safety_decision' in function_call.args:
            decision = get_safety_confirmation(function_call.args['safety_decision'])
            if decision == "TERMINATE":
                print("Terminating agent loop")
                break
            extra_fr_fields["safety_acknowledgement"] = "true" # Safety acknowledgement

        # ... Execute function call and append to results ...
```

Nếu người dùng xác nhận, bạn phải đưa thông báo xác nhận an toàn vào `FunctionResponse`.

### Python

```
function_response_parts.append(
    FunctionResponse(
        name=name,
        response={"url": current_url,
                  **extra_fr_fields},  # Include safety acknowledgement
        parts=[
            types.FunctionResponsePart(
                inline_data=types.FunctionResponseBlob(
                    mime_type="image/png", data=screenshot
                )
             )
           ]
         )
       )
```

### Các phương pháp hay nhất về an toàn

Việc sử dụng máy tính là một công cụ mới mang đến những rủi ro mới mà nhà phát triển cần lưu ý:

- **Nội dung không đáng tin cậy và thủ đoạn lừa đảo:** Khi cố gắng đạt được mục tiêu của người dùng, mô hình có thể dựa vào các nguồn thông tin và hướng dẫn không đáng tin cậy trên màn hình. Ví dụ: nếu mục tiêu của người dùng là mua điện thoại Pixel và mô hình gặp phải một trò lừa đảo "Tặng miễn phí Pixel nếu bạn hoàn thành một bản khảo sát", thì có khả năng mô hình sẽ hoàn thành bản khảo sát.
- **Thỉnh thoảng thực hiện hành động không mong muốn:** Mô hình có thể hiểu sai mục tiêu của người dùng hoặc nội dung trang web, khiến mô hình thực hiện các hành động không chính xác như nhấp vào nút sai hoặc điền vào biểu mẫu sai. Điều này có thể dẫn đến các tác vụ không thành công hoặc việc đánh cắp dữ liệu.
- **Vi phạm chính sách:** Các chức năng của API có thể được hướng đến (dù vô tình hay cố ý) những hoạt động vi phạm các chính sách của Google ([Chính sách về các hành vi bị cấm khi sử dụng AI tạo sinh](https://policies.google.com/terms/generative-ai/use-policy?hl=vi) và [Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi)). Điều này bao gồm những hành động có thể gây ảnh hưởng đến tính toàn vẹn của hệ thống, gây nguy hại cho tính bảo mật, bỏ qua các biện pháp bảo mật, kiểm soát thiết bị y tế, v.v.

Để giải quyết những rủi ro này, bạn có thể triển khai các biện pháp an toàn và phương pháp hay nhất sau đây:

1. **Human-in-the-Loop (HITL):**

   - **Triển khai bước xác nhận của người dùng:** Khi phản hồi về sự an toàn cho biết `require_confirmation`, bạn phải triển khai bước xác nhận của người dùng trước khi thực thi. Hãy xem phần [Xác nhận quyết định về sự an toàn](#safety-decisions) để biết mã mẫu.
   - **Cung cấp hướng dẫn an toàn tuỳ chỉnh:** Ngoài các bước kiểm tra xác nhận người dùng tích hợp sẵn, nhà phát triển có thể tuỳ ý thêm một [hướng dẫn tuỳ chỉnh cho hệ thống](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions) để thực thi chính sách an toàn của riêng họ, nhằm chặn một số hành động nhất định của mô hình hoặc yêu cầu người dùng xác nhận trước khi mô hình thực hiện một số hành động không thể đảo ngược có mức độ rủi ro cao. Sau đây là ví dụ về một chỉ dẫn tuỳ chỉnh cho hệ thống an toàn mà bạn có thể đưa vào khi tương tác với mô hình.

     #### Ví dụ về hướng dẫn an toàn

     Đặt các quy tắc an toàn tuỳ chỉnh làm chỉ dẫn hệ thống:

     ```
         ## **RULE 1: Seek User Confirmation (USER_CONFIRMATION)**

         This is your first and most important check. If the next required action falls
         into any of the following categories, you MUST stop immediately, and seek the
         user's explicit permission.

         **Procedure for Seeking Confirmation:**  * **For Consequential Actions:**
         Perform all preparatory steps (e.g., navigating, filling out forms, typing a
         message). You will ask for confirmation **AFTER** all necessary information is
         entered on the screen, but **BEFORE** you perform the final, irreversible action
         (e.g., before clicking "Send", "Submit", "Confirm Purchase", "Share").  * **For
         Prohibited Actions:** If the action is strictly forbidden (e.g., accepting legal
         terms, solving a CAPTCHA), you must first inform the user about the required
         action and ask for their confirmation to proceed.

         **USER_CONFIRMATION Categories:**

         *   **Consent and Agreements:** You are FORBIDDEN from accepting, selecting, or
             agreeing to any of the following on the user's behalf. You must ask the
             user to confirm before performing these actions.
             *   Terms of Service
             *   Privacy Policies
             *   Cookie consent banners
             *   End User License Agreements (EULAs)
             *   Any other legally significant contracts or agreements.
         *   **Robot Detection:** You MUST NEVER attempt to solve or bypass the
             following. You must ask the user to confirm before performing these actions.
         *   CAPTCHAs (of any kind)
             *   Any other anti-robot or human-verification mechanisms, even if you are
                 capable.
         *   **Financial Transactions:**
             *   Completing any purchase.
             *   Managing or moving money (e.g., transfers, payments).
             *   Purchasing regulated goods or participating in gambling.
         *   **Sending Communications:**
             *   Sending emails.
             *   Sending messages on any platform (e.g., social media, chat apps).
             *   Posting content on social media or forums.
         *   **Accessing or Modifying Sensitive Information:**
             *   Health, financial, or government records (e.g., medical history, tax
                 forms, passport status).
             *   Revealing or modifying sensitive personal identifiers (e.g., SSN, bank
                 account number, credit card number).
         *   **User Data Management:**
             *   Accessing, downloading, or saving files from the web.
             *   Sharing or sending files/data to any third party.
             *   Transferring user data between systems.
         *   **Browser Data Usage:**
             *   Accessing or managing Chrome browsing history, bookmarks, autofill data,
                 or saved passwords.
         *   **Security and Identity:**
             *   Logging into any user account.
             *   Any action that involves misrepresentation or impersonation (e.g.,
                 creating a fan account, posting as someone else).
         *   **Insurmountable Obstacles:** If you are technically unable to interact with
             a user interface element or are stuck in a loop you cannot resolve, ask the
             user to take over.
         ---

         ## **RULE 2: Default Behavior (ACTUATE)**

         If an action does **NOT** fall under the conditions for `USER_CONFIRMATION`,
         your default behavior is to **Actuate**.

         **Actuation Means:**  You MUST proactively perform all necessary steps to move
         the user's request forward. Continue to actuate until you either complete the
         non-consequential task or encounter a condition defined in Rule 1.

         *   **Example 1:** If asked to send money, you will navigate to the payment
             portal, enter the recipient's details, and enter the amount. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Send" button.
         *   **Example 2:** If asked to post a message, you will navigate to the site,
             open the post composition window, and write the full message. You will then
             **STOP** as per Rule 1 and ask for confirmation before clicking the final
             "Post" button.

             After the user has confirmed, remember to get the user's latest screen
             before continuing to perform actions.

         # Final Response Guidelines:
         Write final response to the user in the following cases:
         - User confirmation
         - When the task is complete or you have enough information to respond to the user
     ```
2. **Môi trường thực thi an toàn:** Chạy tác nhân của bạn trong một môi trường hộp cát an toàn để hạn chế tác động tiềm ẩn của tác nhân (ví dụ: Máy ảo (VM) hộp cát, một vùng chứa (ví dụ: Docker) hoặc một hồ sơ trình duyệt chuyên dụng có các quyền hạn chế).
3. **Làm sạch dữ liệu đầu vào:** Làm sạch tất cả văn bản do người dùng tạo trong câu lệnh để giảm thiểu nguy cơ vô tình đưa ra chỉ dẫn hoặc tiêm câu lệnh (prompt injection). Đây là một lớp bảo mật hữu ích, nhưng không thay thế được môi trường thực thi an toàn.
4. **Quy định hạn chế về nội dung:** Sử dụng quy định hạn chế và [API an toàn nội dung](https://ai.google.dev/gemma/docs/shieldgemma?hl=vi) để đánh giá thông tin đầu vào của người dùng, thông tin đầu vào và đầu ra của công cụ, phản hồi của một đặc vụ về tính phù hợp, việc chèn câu lệnh và phát hiện hành vi vượt rào.
5. **Danh sách cho phép và danh sách chặn:** Triển khai các cơ chế lọc để kiểm soát nơi mô hình có thể điều hướng và những việc mô hình có thể làm. Danh sách chặn các trang web bị cấm là một điểm khởi đầu tốt, trong khi danh sách cho phép hạn chế hơn sẽ an toàn hơn nữa.
6. **Khả năng quan sát và ghi nhật ký:** Duy trì nhật ký chi tiết để gỡ lỗi, kiểm tra và xử lý sự cố. Ứng dụng của bạn nên ghi lại các câu lệnh, ảnh chụp màn hình, hành động do mô hình đề xuất (function\_call), câu trả lời an toàn và tất cả các hành động mà ứng dụng thực hiện.
7. **Quản lý môi trường:** Đảm bảo môi trường GUI nhất quán.
   Cửa sổ bật lên, thông báo hoặc thay đổi bố cục không mong muốn có thể khiến mô hình bị nhầm lẫn. Bắt đầu từ một trạng thái sạch, đã biết cho mỗi tác vụ mới nếu có thể.

## Phiên bản mô hình

Xin lưu ý rằng `gemini-3-flash-preview` có hỗ trợ sẵn cho tính năng Sử dụng máy tính; bạn không cần một mô hình riêng để truy cập vào công cụ này.

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `gemini-2.5-computer-use-preview-10-2025` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Hình ảnh, văn bản  **Đầu ra**  Văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  128.000  **Giới hạn mã thông báo đầu ra**  64.000 |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Xem trước: `gemini-2.5-computer-use-preview-10-2025` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 10 năm 2025 |

## Bước tiếp theo

- Thử nghiệm với việc sử dụng máy tính trong [môi trường trình diễn Browserbase](http://gemini.browserbase.com).
- Hãy xem [Triển khai tham chiếu](https://github.com/google/computer-use-preview) để biết mã ví dụ.
- Tìm hiểu về các công cụ khác của Gemini API:
  - [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
  - [Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
