---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=vi
fetched_at: 2026-06-22T06:29:21.609684+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) is now available in preview with collaborative planning, visualization, MCP support, and more.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tính năng gọi hàm bằng Gemini API

Tính năng gọi hàm cho phép bạn kết nối các mô hình với các công cụ và API bên ngoài.
Thay vì tạo phản hồi bằng văn bản, mô hình sẽ xác định thời điểm gọi các hàm cụ thể và cung cấp các tham số cần thiết để thực thi các hành động trong thế giới thực.
Điều này cho phép mô hình đóng vai trò là cầu nối giữa ngôn ngữ tự nhiên và các hành động cũng như dữ liệu trong thế giới thực. Tính năng gọi hàm có 3 trường hợp sử dụng chính:

- [**Thực hiện hành động:**](#meeting) Tương tác với các hệ thống bên ngoài bằng API, chẳng hạn như lên lịch hẹn, tạo hoá đơn, gửi email hoặc điều khiển các thiết bị nhà thông minh.
- [**Tăng cường kiến thức:**](#weather) Truy cập thông tin từ các nguồn bên ngoài như cơ sở dữ liệu, API và cơ sở kiến thức.
- [**Mở rộng khả năng:**](#chart) Sử dụng các công cụ bên ngoài để thực hiện phép tính và mở rộng các giới hạn của mô hình, chẳng hạn như sử dụng máy tính hoặc tạo biểu đồ.

Bạn có thể duyệt xem ví dụ về các trường hợp sử dụng này bên dưới:

### Lên lịch cuộc họp

Ví dụ này cho thấy cách xác định một hàm lên lịch cuộc họp với người tham dự vào một thời điểm cụ thể, cho phép mô hình phân tích cú pháp các yêu cầu của người dùng và trả về các đối số có cấu trúc để kích hoạt các hành động trong hệ thống bên ngoài.

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{
      functionDeclarations: [scheduleMeetingFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "schedule_meeting",
            "description": "Schedules a meeting with specified attendees at a given time and date.",
            "parameters": {
              "type": "object",
              "properties": {
                "attendees": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of people attending the meeting."
                },
                "date": {
                  "type": "string",
                  "description": "Date of the meeting (e.g., '2024-07-29')"
                },
                "time": {
                  "type": "string",
                  "description": "Time of the meeting (e.g., '15:00')"
                },
                "topic": {
                  "type": "string",
                  "description": "The subject or topic of the meeting."
                }
              },
              "required": ["attendees", "date", "time", "topic"]
            }
          }
        ]
      }
    ]
  }'
```

### Nhận thông tin thời tiết

Ví dụ này cho thấy cách xác định một hàm truy xuất dữ liệu nhiệt độ cho một vị trí, cho phép mô hình gọi các API bên ngoài để trả lời những truy vấn yêu cầu thông tin theo thời gian thực hoặc thông tin bên ngoài.

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What's the temperature in London?",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = get_current_temperature(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const weatherFunctionDeclaration = {
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      location: {
        type: Type.STRING,
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: "What's the temperature in London?",
  config: {
    tools: [{
      functionDeclarations: [weatherFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await getCurrentTemperature(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "What'\''s the temperature in London?"
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

### Tạo biểu đồ

Ví dụ này cho thấy cách xác định một hàm tạo biểu đồ thanh từ dữ liệu có cấu trúc, minh hoạ cách mô hình có thể sử dụng các công cụ bên ngoài để thực hiện các phép tính hoặc tạo tài sản trực quan:

### Python

```
import os
from google import genai
from google.genai import types

# Define the function declaration for the model
create_chart_function = {
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and corresponding values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title for the chart.",
            },
            "labels": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of labels for the data points (e.g., ['Q1', 'Q2', 'Q3']).",
            },
            "values": {
                "type": "array",
                "items": {"type": "number"},
                "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).",
            },
        },
        "required": ["title", "labels", "values"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[create_chart_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here using a charting library:
    #  result = create_bar_chart(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const createChartFunctionDeclaration = {
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and corresponding values.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      title: {
        type: Type.STRING,
        description: 'The title for the chart.',
      },
      labels: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of labels for the data points (e.g., ["Q1", "Q2", "Q3"]).',
      },
      values: {
        type: Type.ARRAY,
        items: { type: Type.NUMBER },
        description: 'List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000]).',
      },
    },
    required: ['title', 'labels', 'values'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: "Create a bar chart titled 'Quarterly Sales' with data: Q1: 50000, Q2: 75000, Q3: 60000.",
  config: {
    tools: [{
      functionDeclarations: [createChartFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await createBarChart(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Create a bar chart titled ''Quarterly Sales'' with data: Q1: 50000, Q2: 75000, Q3: 60000."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "create_bar_chart",
            "description": "Creates a bar chart given a title, labels, and corresponding values.",
            "parameters": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string",
                  "description": "The title for the chart."
                },
                "labels": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of labels for the data points (e.g., [''Q1'', ''Q2'', ''Q3''])."
                },
                "values": {
                  "type": "array",
                  "items": {"type": "number"},
                  "description": "List of numerical values corresponding to the labels (e.g., [50000, 75000, 60000])."
                }
              },
              "required": ["title", "labels", "values"]
            }
          }
        ]
      }
    ]
  }'
```

## Cách hoạt động của tính năng gọi hàm

![tổng quan về tính năng gọi hàm](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=vi)

Gọi hàm là một hoạt động tương tác có cấu trúc giữa ứng dụng, mô hình và các hàm bên ngoài. Sau đây là thông tin chi tiết về quy trình này:

1. **Xác định khai báo hàm:** Xác định khai báo hàm trong mã xử lý ứng dụng của bạn. Khai báo hàm mô tả tên, tham số và mục đích của hàm cho mô hình.
2. **Gọi API bằng khai báo hàm:** Gửi câu lệnh của người dùng cùng với(các) khai báo hàm đến mô hình. Mô hình sẽ phân tích yêu cầu và xác định xem liệu lệnh gọi hàm có hữu ích hay không. Nếu có, mô hình sẽ phản hồi bằng một đối tượng JSON có cấu trúc chứa tên hàm, các đối số và một `id` duy nhất (API cho các mô hình Gemini 3 hiện luôn trả về `id` này\*).
3. **Thực thi mã hàm (trách nhiệm của bạn):** Mô hình *không* tự thực thi hàm. Ứng dụng của bạn có trách nhiệm xử lý phản hồi và kiểm tra lệnh gọi hàm. Nếu
   - **Có**: Trích xuất tên, đối số và `id` của hàm rồi thực thi hàm tương ứng trong ứng dụng của bạn.
   - **Không:** Mô hình đã cung cấp một câu trả lời bằng văn bản trực tiếp cho câu lệnh (luồng này ít được nhấn mạnh trong ví dụ nhưng là một kết quả có thể xảy ra).
4. **Tạo phản hồi thân thiện với người dùng:** Nếu một hàm đã được thực thi, hãy thu thập kết quả và gửi lại cho mô hình, đảm bảo bạn đưa `id` phù hợp vào lượt tiếp theo của cuộc trò chuyện. Công cụ này sẽ sử dụng kết quả để tạo ra một phản hồi cuối cùng, thân thiện với người dùng, kết hợp thông tin từ lệnh gọi hàm.

Quá trình này có thể được lặp lại nhiều lần, cho phép các quy trình và hoạt động tương tác phức tạp. Mô hình này cũng hỗ trợ gọi nhiều hàm trong một lượt ([gọi hàm song song](#parallel_function_calling)), theo trình tự ([gọi hàm thành phần](#compositional_function_calling)) và bằng các công cụ Gemini tích hợp ([sử dụng nhiều công cụ](#native-tools)).

\* **Luôn ánh xạ mã nhận dạng hàm:** Giờ đây, Gemini 3 luôn trả về một `id` duy nhất với mọi `functionCall`. Hãy đưa chính xác `id` này vào `functionResponse` để mô hình có thể ánh xạ chính xác kết quả của bạn trở lại yêu cầu ban đầu.

### Bước 1: Xác định một khai báo hàm

Xác định một hàm và khai báo của hàm đó trong mã xử lý ứng dụng để cho phép người dùng đặt giá trị ánh sáng và đưa ra yêu cầu API. Hàm này có thể gọi các dịch vụ hoặc API bên ngoài.

### Python

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}
```

### Bước 2: Gọi mô hình bằng các khai báo hàm

Sau khi xác định nội dung khai báo hàm, bạn có thể ra lệnh cho mô hình sử dụng nội dung khai báo đó. Mô hình sẽ phân tích câu lệnh và nội dung khai báo hàm, đồng thời quyết định có nên phản hồi trực tiếp hay gọi một hàm. Nếu một hàm được gọi, đối tượng phản hồi sẽ chứa một đề xuất lệnh gọi hàm.

### Python

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [
    types.Content(
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]
    )
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{
    functionDeclarations: [setLightValuesFunctionDeclaration]
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [
  {
    role: 'user',
    parts: [{ text: 'Turn the lights down to a romantic level' }]
  }
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

Sau đó, mô hình sẽ trả về một đối tượng `functionCall` trong một giản đồ tương thích với OpenAPI, chỉ định cách gọi một hoặc nhiều hàm đã khai báo để trả lời câu hỏi của người dùng.

### Python

```
id='8f2b1a3c' args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

### JavaScript

```
{
  id: '8f2b1a3c',
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}
```

### Bước 3: Thực thi mã hàm set\_light\_values

Trích xuất thông tin chi tiết về lệnh gọi hàm từ phản hồi của mô hình, phân tích cú pháp các đối số và thực thi hàm `set_light_values`.

### Python

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### Bước 4: Tạo phản hồi thân thiện với người dùng bằng kết quả của hàm và gọi lại mô hình

Cuối cùng, hãy gửi kết quả thực thi hàm trở lại mô hình để mô hình có thể kết hợp thông tin này vào phản hồi cuối cùng cho người dùng.

### Python

```
from google import genai
from google.genai import types

# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
    id=tool_call.id,
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

client = genai.Client()
final_response = client.models.generate_content(
    model="gemini-3.5-flash",
    config=config,
    contents=contents,
)

print(final_response.text)
```

### JavaScript

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result },
  id: tool_call.id
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

Thao tác này sẽ hoàn tất quy trình gọi hàm. Mô hình đã sử dụng thành công hàm `set_light_values` để thực hiện hành động theo yêu cầu của người dùng.

## Khai báo hàm

Khi triển khai tính năng gọi hàm trong một câu lệnh, bạn sẽ tạo một đối tượng `tools`, trong đó có chứa một hoặc nhiều `function declarations`. Bạn xác định các hàm bằng JSON, cụ thể là bằng một [tập hợp con chọn lọc](https://ai.google.dev/api/caching?hl=vi#Schema) của định dạng [sơ đồ OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Một khai báo hàm duy nhất có thể bao gồm các tham số sau:

- `name` (chuỗi): Tên duy nhất cho hàm (`get_weather_forecast`, `send_email`). Sử dụng tên mô tả không có dấu cách hoặc ký tự đặc biệt (sử dụng dấu gạch dưới hoặc kiểu lạc đà).
- `description` (chuỗi): Nội dung giải thích rõ ràng và chi tiết về mục đích và khả năng của hàm. Điều này rất quan trọng để mô hình hiểu được thời điểm sử dụng hàm. Hãy nêu cụ thể và đưa ra ví dụ nếu hữu ích ("Tìm rạp chiếu phim dựa trên vị trí và tiêu đề phim (không bắt buộc) hiện đang chiếu tại rạp.").
- `parameters` (đối tượng): Xác định các tham số đầu vào mà hàm mong đợi.
  - `type` (chuỗi): Chỉ định loại dữ liệu tổng thể, chẳng hạn như `object`.
  - `properties` (đối tượng): Liệt kê các thông số riêng lẻ, mỗi thông số có:
    - `type` (chuỗi): Loại dữ liệu của tham số, chẳng hạn như `string`, `integer`, `boolean, array`.
    - `description` (chuỗi): Nội dung mô tả về mục đích và định dạng của tham số. Đưa ra ví dụ và các ràng buộc ("Thành phố và tiểu bang, ví dụ: "San Francisco, CA" hoặc mã zip, ví dụ: "95616").
    - `enum` (mảng, không bắt buộc): Nếu các giá trị tham số thuộc một tập hợp cố định, hãy sử dụng "enum" để liệt kê các giá trị được phép thay vì chỉ mô tả các giá trị đó trong phần mô tả. Điều này giúp cải thiện độ chính xác ("enum":["daylight", "cool", "warm"]).
  - `required` (mảng): Một mảng gồm các chuỗi liệt kê tên tham số bắt buộc để hàm hoạt động.

Bạn cũng có thể tạo `FunctionDeclarations` trực tiếp từ các hàm Python bằng cách sử dụng `types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Gọi hàm bằng mô hình tư duy

Các mô hình Gemini 3 và 2.5 sử dụng quy trình ["tư duy"](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) nội bộ để suy luận về các yêu cầu. Điều này giúp cải thiện đáng kể hiệu suất gọi hàm, cho phép mô hình xác định chính xác hơn thời điểm gọi hàm và tham số cần sử dụng. Vì Gemini API không lưu giữ trạng thái, nên các mô hình sử dụng [chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=vi) để duy trì ngữ cảnh trong các cuộc trò chuyện nhiều lượt.

Phần này đề cập đến việc quản lý nâng cao chữ ký tư duy và chỉ cần thiết nếu bạn đang tạo yêu cầu API theo cách thủ công (ví dụ: thông qua REST) hoặc thao tác với nhật ký cuộc trò chuyện.

**Nếu đang sử dụng [SDK AI tạo sinh của Google](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) (các thư viện chính thức của chúng tôi), bạn không cần quản lý quy trình này**. Các SDK sẽ tự động xử lý các bước cần thiết, như minh hoạ trong [ví dụ](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-4) trước đó.

### Quản lý cuộc trò chuyện theo cách thủ công

Nếu sửa đổi nhật ký trò chuyện theo cách thủ công, thay vì gửi [phản hồi hoàn chỉnh trước đó](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#step-4), bạn phải xử lý chính xác `thought_signature` có trong lượt của mô hình.

Hãy tuân thủ các quy tắc sau để đảm bảo ngữ cảnh của mô hình được giữ nguyên:

- Luôn gửi `thought_signature` trở lại mô hình bên trong [`Part`](https://ai.google.dev/api?hl=vi#request-body-structure) ban đầu của mô hình.
- **Luôn thêm chính xác `id` từ `function_call` vào `function_response` để API có thể ánh xạ kết quả đến yêu cầu chính xác.**
- Đừng hợp nhất một `Part` chứa chữ ký với một `Part` không chứa chữ ký. Điều này phá vỡ ngữ cảnh vị trí của suy nghĩ.
- Đừng kết hợp hai `Parts` đều chứa chữ ký, vì bạn không thể hợp nhất các chuỗi chữ ký.

#### Chữ ký tư duy của Gemini 3

Trong Gemini 3, mọi [`Part`](https://ai.google.dev/api?hl=vi#request-body-structure) của một phản hồi của mô hình đều có thể chứa chữ ký suy nghĩ. Mặc dù thường thì bạn nên trả về chữ ký từ tất cả các loại `Part`, nhưng việc truyền lại chữ ký suy nghĩ là bắt buộc đối với tính năng gọi hàm. Trừ phi bạn thao tác thủ công với nhật ký cuộc trò chuyện, còn không thì Google GenAI SDK sẽ tự động xử lý chữ ký suy nghĩ.

Nếu bạn đang thao tác nhật ký cuộc trò chuyện theo cách thủ công, hãy tham khảo trang [Chữ ký suy nghĩ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=vi) để biết hướng dẫn và thông tin chi tiết đầy đủ về cách xử lý chữ ký suy nghĩ cho Gemini 3.

##### Kiểm tra chữ ký của suy nghĩ

Mặc dù không cần thiết cho việc triển khai, nhưng bạn có thể kiểm tra phản hồi để xem `thought_signature` cho mục đích gỡ lỗi hoặc giáo dục.

### Python

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))
```

### JavaScript

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}
```

Tìm hiểu thêm về các hạn chế và cách sử dụng chữ ký tư duy, cũng như về các mô hình tư duy nói chung, trên trang [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#signatures).

## Gọi hàm song song

Ngoài việc gọi hàm một lần, bạn cũng có thể gọi nhiều hàm cùng một lúc. Tính năng gọi hàm song song cho phép bạn thực thi nhiều hàm cùng một lúc và được dùng khi các hàm không phụ thuộc vào nhau. Tính năng này hữu ích trong các trường hợp như thu thập dữ liệu từ nhiều nguồn độc lập, chẳng hạn như truy xuất thông tin chi tiết về khách hàng từ các cơ sở dữ liệu khác nhau hoặc kiểm tra mức tồn kho ở nhiều nhà kho hoặc thực hiện nhiều hành động như biến căn hộ của bạn thành một vũ trường.

Khi mô hình bắt đầu nhiều lệnh gọi hàm trong một lượt, bạn không cần trả về các đối tượng `function_result` theo cùng thứ tự mà các đối tượng `function_call` đã nhận được. Gemini API liên kết từng kết quả với lệnh gọi tương ứng bằng cách sử dụng `id` từ đầu ra của mô hình. Nhờ đó, bạn có thể thực thi các hàm một cách không đồng bộ và thêm kết quả vào danh sách khi các hàm hoàn tất.

### Python

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}
```

### JavaScript

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
  }
};
```

Định cấu hình chế độ gọi hàm để cho phép sử dụng tất cả các công cụ được chỉ định.
Để tìm hiểu thêm, bạn có thể đọc về [cách định cấu hình tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#function_calling_modes).

### Python

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-3.5-flash", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args}) - ID: {fn.id}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{
        functionDeclarations: houseFns
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-3.5-flash',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args}) - ID: ${fn.id}`);
}
```

Mỗi kết quả được in phản ánh một lệnh gọi hàm duy nhất mà mô hình đã yêu cầu. Để gửi kết quả trở lại, hãy đưa các phản hồi theo cùng thứ tự như khi chúng được yêu cầu.

Python SDK hỗ trợ [tự động gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#automatic_function_calling_python_only), tự động chuyển đổi các hàm Python thành khai báo, xử lý quá trình thực thi lệnh gọi hàm và chu kỳ phản hồi cho bạn. Sau đây là một ví dụ về trường hợp sử dụng disco.

### Python

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Gọi hàm thành phần

Việc gọi hàm theo thành phần hoặc tuần tự cho phép Gemini liên kết nhiều lệnh gọi hàm với nhau để thực hiện một yêu cầu phức tạp. Ví dụ: để trả lời câu hỏi "Nhiệt độ ở vị trí hiện tại của tôi là bao nhiêu", trước tiên, Gemini API có thể gọi một hàm `get_current_location()`, sau đó gọi một hàm `get_weather()` lấy vị trí làm tham số.

Ví dụ sau đây minh hoạ cách triển khai lệnh gọi hàm kết hợp bằng cách sử dụng Python SDK và lệnh gọi hàm tự động.

### Python

Ví dụ này sử dụng tính năng gọi hàm tự động của SDK Python `google-genai`. SDK tự động chuyển đổi các hàm Python thành giản đồ bắt buộc, thực thi các lệnh gọi hàm khi được mô hình yêu cầu và gửi kết quả trở lại mô hình để hoàn tất tác vụ.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Kết quả đầu ra dự kiến**

Khi chạy mã, bạn sẽ thấy SDK điều phối các lệnh gọi hàm. Trước tiên, mô hình gọi `get_weather_forecast`, nhận nhiệt độ, sau đó gọi `set_thermostat_temperature` với giá trị chính xác dựa trên logic trong câu lệnh.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

Ví dụ này cho thấy cách sử dụng JavaScript/TypeScript SDK để thực hiện lệnh gọi hàm kết hợp bằng cách sử dụng vòng lặp thực thi thủ công.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [
  {
    functionDeclarations: [
      {
        name: "get_weather_forecast",
        description:
          "Gets the current weather temperature for a given location.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            location: {
              type: Type.STRING,
            },
          },
          required: ["location"],
        },
      },
      {
        name: "set_thermostat_temperature",
        description: "Sets the thermostat to a desired temperature.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            temperature: {
              type: Type.NUMBER,
            },
          },
          required: ["temperature"],
        },
      },
    ],
  },
];

// Prompt for the model
let contents = [
  {
    role: "user",
    parts: [
      {
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
      },
    ],
  },
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
      id: functionCall.id,
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [
        {
          functionCall: functionCall,
        },
      ],
    });
    contents.push({
      role: "user",
      parts: [
        {
          functionResponse: functionResponsePart,
        },
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}
```

**Kết quả đầu ra dự kiến**

Khi chạy mã, bạn sẽ thấy SDK điều phối các lệnh gọi hàm. Trước tiên, mô hình gọi `get_weather_forecast`, nhận nhiệt độ, sau đó gọi `set_thermostat_temperature` với giá trị chính xác dựa trên logic trong câu lệnh.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

Gọi hàm thành phần là một tính năng gốc của [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi). Điều này có nghĩa là Live API có thể xử lý việc gọi hàm tương tự như Python SDK.

### Python

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [
    {'code_execution': {}},
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}
]

await run(prompt, tools=tools, modality="AUDIO")
```

### JavaScript

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [
  { codeExecution: {} },
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }
];

await run(prompt, tools=tools, modality="AUDIO")
```

## Chế độ gọi hàm

Gemini API cho phép bạn kiểm soát cách mô hình sử dụng các công cụ được cung cấp (khai báo hàm). Cụ thể, bạn có thể đặt chế độ trong `function_calling_config`.

- `VALIDATED`: Chế độ mặc định để kết hợp các công cụ (khi các công cụ tích hợp hoặc đầu ra có cấu trúc cũng được bật). Mô hình bị hạn chế dự đoán các lệnh gọi hàm hoặc ngôn ngữ tự nhiên và đảm bảo tuân thủ giản đồ hàm. Nếu không có `allowed_function_names`, mô hình sẽ chọn trong số tất cả các khai báo hàm có sẵn. Nếu có `allowed_function_names`, mô hình sẽ chọn trong số các hàm được phép. Chế độ này giúp giảm các lệnh gọi hàm bị lỗi (so với chế độ `AUTO`).
- `AUTO`: Chế độ mặc định khi chỉ bật công cụ function\_declarations.
  Mô hình sẽ quyết định có tạo câu trả lời bằng ngôn ngữ tự nhiên hay đề xuất một lệnh gọi hàm dựa trên câu lệnh và bối cảnh.
- `ANY`: Mô hình bị hạn chế để luôn dự đoán một lệnh gọi hàm và đảm bảo tuân thủ giản đồ hàm. Nếu bạn không chỉ định `allowed_function_names`, mô hình có thể chọn trong số bất kỳ khai báo hàm nào được cung cấp.
  Nếu `allowed_function_names` được cung cấp dưới dạng một danh sách, thì mô hình chỉ có thể chọn trong số các hàm trong danh sách đó. Sử dụng chế độ này khi bạn yêu cầu phản hồi lệnh gọi hàm cho mọi câu lệnh (nếu có).
- `NONE`: Mô hình *bị cấm* thực hiện lệnh gọi hàm. Điều này tương đương với việc gửi một yêu cầu mà không có bất kỳ khai báo hàm nào. Sử dụng tuỳ chọn này để tạm thời vô hiệu hoá tính năng gọi hàm mà không cần xoá định nghĩa công cụ.

### Python

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)
```

### JavaScript

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};
```

## Gọi hàm tự động (chỉ dành cho Python)

Khi sử dụng Python SDK, bạn có thể cung cấp trực tiếp các hàm Python dưới dạng công cụ.
SDK chuyển đổi các hàm này thành các khai báo, quản lý việc thực thi lệnh gọi hàm và xử lý chu kỳ phản hồi cho bạn. Xác định hàm bằng các gợi ý về kiểu và chuỗi tài liệu. Để có kết quả tối ưu, bạn nên sử dụng [chuỗi tài liệu theo kiểu của Google](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).
Sau đó, SDK sẽ tự động:

1. Phát hiện các phản hồi gọi hàm từ mô hình.
2. Gọi hàm Python tương ứng trong mã của bạn.
3. Gửi phản hồi của hàm trở lại mô hình.
4. Trả về phản hồi văn bản cuối cùng của mô hình.

SDK hiện không phân tích cú pháp nội dung mô tả đối số thành các vị trí nội dung mô tả thuộc tính của khai báo hàm được tạo. Thay vào đó, nó sẽ gửi toàn bộ chuỗi tài liệu dưới dạng nội dung mô tả hàm cấp cao nhất.

### Python

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

Bạn có thể tắt tính năng tự động gọi hàm bằng cách dùng:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Khai báo giản đồ hàm tự động

API này có thể mô tả bất kỳ loại nào sau đây. cho phép các loại `Pydantic`, miễn là các trường được xác định trên các loại này cũng bao gồm các loại được phép. Các loại Dict (như `dict[str: int]`) không được hỗ trợ tốt ở đây, đừng sử dụng chúng.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Để xem giản đồ suy luận trông như thế nào, bạn có thể chuyển đổi giản đồ đó bằng cách sử dụng [`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

### Python

```
from google import genai
from google.genai import types

def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

client = genai.Client()
fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())
```

## Sử dụng nhiều công cụ: Kết hợp các công cụ tích hợp với tính năng gọi hàm

Bạn có thể bật nhiều công cụ, kết hợp các công cụ tích hợp sẵn với tính năng gọi hàm trong cùng một yêu cầu.

Các mô hình Gemini 3 có thể kết hợp các công cụ tích hợp với tính năng gọi hàm ngay lập tức, nhờ tính năng truyền ngữ cảnh công cụ. Hãy đọc trang về [Kết hợp các công cụ tích hợp và tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi) để tìm hiểu thêm.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3.5-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

Đối với các mô hình trước dòng Gemini 3, hãy sử dụng [Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=vi).

## Phản hồi của hàm đa phương thức

Đối với các mô hình thuộc dòng Gemini 3, bạn có thể đưa nội dung đa phương thức vào các phần phản hồi của hàm mà bạn gửi đến mô hình. Mô hình có thể xử lý nội dung đa phương thức này trong lượt tiếp theo để tạo ra câu trả lời có nhiều thông tin hơn. Các loại MIME sau đây được hỗ trợ cho nội dung đa phương thức trong phản hồi của hàm:

- **Hình ảnh**: `image/png`, `image/jpeg`, `image/webp`
- **Tài liệu**: `application/pdf`, `text/plain`

Để đưa dữ liệu đa phương thức vào phản hồi của hàm, hãy đưa dữ liệu đó vào dưới dạng một hoặc nhiều phần được lồng trong phần `functionResponse`. Mỗi phần đa phương thức phải chứa `inlineData`. Nếu bạn tham chiếu một phần đa phương thức từ trong trường `response` có cấu trúc, thì phần đó phải chứa một `displayName` duy nhất.

Bạn cũng có thể tham chiếu một phần đa phương thức từ trong trường `response` có cấu trúc của phần `functionResponse` bằng cách sử dụng định dạng tham chiếu JSON `{"$ref": "<displayName>"}`. Mô hình sẽ thay thế thông tin tham khảo bằng nội dung đa phương thức khi xử lý phản hồi. Bạn chỉ có thể tham chiếu mỗi `displayName` một lần trong trường `response` có cấu trúc.

Ví dụ sau đây cho thấy một thông báo chứa `functionResponse` cho một hàm có tên `get_image` và một phần lồng nhau chứa dữ liệu hình ảnh có `displayName: "instrument.jpg"`. Trường `functionResponse` của `response` tham chiếu đến phần hình ảnh này:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          id=function_call.id,
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'user',
    parts: [
      {
        functionResponse: {
          id: functionCall.id,
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData]
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3.5-flash',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "id": "UNIQUE_CALL_ID_HERE",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

## Gọi hàm bằng đầu ra có cấu trúc

Đối với các mô hình thuộc dòng Gemini 3, bạn có thể sử dụng tính năng gọi hàm với [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi). Nhờ đó, mô hình có thể dự đoán các lệnh gọi hàm hoặc đầu ra tuân thủ một lược đồ cụ thể. Do đó, bạn sẽ nhận được các câu trả lời có định dạng nhất quán khi mô hình không tạo ra các lệnh gọi hàm.

## Giao thức ngữ cảnh mô hình (MCP)

[Giao thức ngữ cảnh mô hình (MCP)](https://modelcontextprotocol.io/introduction) là một tiêu chuẩn mở để kết nối các ứng dụng AI với các công cụ và dữ liệu bên ngoài.
MCP cung cấp một giao thức chung để các mô hình truy cập vào bối cảnh, chẳng hạn như các hàm (công cụ), nguồn dữ liệu (tài nguyên) hoặc câu lệnh được xác định trước.

Các Gemini SDK có hỗ trợ tích hợp cho MCP, giúp giảm mã nguyên mẫu và cung cấp [tính năng gọi công cụ tự động](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#automatic_function_calling_python_only) cho các công cụ MCP. Khi mô hình tạo một lệnh gọi công cụ MCP, SDK ứng dụng Python và JavaScript có thể tự động thực thi công cụ MCP và gửi phản hồi trở lại mô hình trong một yêu cầu tiếp theo, tiếp tục vòng lặp này cho đến khi mô hình không thực hiện thêm lệnh gọi công cụ nào.

Tại đây, bạn có thể xem ví dụ về cách sử dụng máy chủ MCP cục bộ với Gemini và SDK `mcp`.

### Python

Đảm bảo bạn đã cài đặt phiên bản mới nhất của [`mcp` SDK](https://modelcontextprotocol.io/introduction) trên nền tảng mà bạn chọn.

```
pip install mcp
```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```

### JavaScript

Đảm bảo bạn đã cài đặt phiên bản mới nhất của SDK `mcp` trên nền tảng mà bạn chọn.

```
npm install @modelcontextprotocol/sdk
```

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();
```

### Hạn chế đối với tính năng hỗ trợ MCP tích hợp

Hỗ trợ MCP tích hợp là một tính năng [thử nghiệm](https://ai.google.dev/gemini-api/docs/models?hl=vi#preview) trong SDK của chúng tôi và có những hạn chế sau:

- Chỉ hỗ trợ các công cụ, không hỗ trợ tài nguyên hay câu lệnh
- Tính năng này có trong SDK Python và JavaScript/TypeScript.
- Các thay đổi có thể gây lỗi có thể xảy ra trong các bản phát hành sau này.

Tích hợp thủ công các máy chủ MCP luôn là một lựa chọn nếu những máy chủ này giới hạn những gì bạn đang xây dựng.

## Mô hình được hỗ trợ

Phần này liệt kê các mô hình và khả năng gọi hàm của chúng. Không bao gồm các mô hình thử nghiệm. Bạn có thể xem thông tin tổng quan toàn diện về các chức năng trên trang [tổng quan về mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi).

| Mô hình | Gọi hàm | Gọi hàm song song | Gọi hàm thành phần |
| --- | --- | --- | --- |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ | ✔️ | ✔️ |

## Các phương pháp hay nhất

- **Nội dung mô tả về hàm và tham số:** Nội dung mô tả phải cực kỳ rõ ràng và cụ thể. Mô hình dựa vào những thông tin này để chọn đúng hàm và cung cấp các đối số phù hợp.
- **Đặt tên:** Sử dụng tên hàm mô tả (không có dấu cách, dấu chấm hoặc dấu gạch ngang).
- **Nhập mạnh:** Sử dụng các loại cụ thể (số nguyên, chuỗi, enum) cho các tham số để giảm lỗi. Nếu một tham số có một tập hợp giới hạn các giá trị hợp lệ, hãy sử dụng một enum.
- **Lựa chọn công cụ:** Mặc dù mô hình có thể sử dụng một số lượng tuỳ ý công cụ, nhưng việc cung cấp quá nhiều công cụ có thể làm tăng nguy cơ chọn một công cụ không chính xác hoặc không tối ưu. Để đạt được kết quả tốt nhất, hãy chỉ cung cấp các công cụ phù hợp cho bối cảnh hoặc nhiệm vụ, lý tưởng nhất là giữ cho tập hợp đang hoạt động ở mức tối đa là 10-20. Hãy cân nhắc việc chọn công cụ động dựa trên ngữ cảnh cuộc trò chuyện nếu bạn có tổng số lượng lớn công cụ.
- **Kỹ thuật tạo câu lệnh:**
  - Cung cấp bối cảnh: Cho mô hình biết vai trò của mô hình (ví dụ: "Bạn là một trợ lý thời tiết hữu ích").
  - Đưa ra hướng dẫn: Chỉ định cách thức và thời điểm sử dụng các hàm (ví dụ: "Đừng đoán ngày; luôn sử dụng ngày trong tương lai cho các dự báo").
  - Khuyến khích làm rõ: Hướng dẫn mô hình đặt câu hỏi làm rõ nếu cần.
  - Hãy xem [Quy trình làm việc dựa trên tác nhân](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi#agentic-workflows) để biết thêm các chiến lược về cách thiết kế những câu lệnh này. Dưới đây là ví dụ về một [chỉ dẫn hệ thống](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi#agentic-si-template) đã được kiểm thử.
- **Nhiệt độ:** Sử dụng nhiệt độ thấp (ví dụ: 0) để có các lệnh gọi hàm đáng tin cậy và mang tính xác định hơn.
- **Xác thực:** Nếu một lệnh gọi hàm có hậu quả đáng kể (ví dụ: đặt hàng), hãy xác thực lệnh gọi đó với người dùng trước khi thực thi.
- **Kiểm tra lý do hoàn thành:** Luôn kiểm tra [`finishReason`](https://ai.google.dev/api/generate-content?hl=vi#FinishReason) trong câu trả lời của mô hình để xử lý các trường hợp mô hình không tạo được một lệnh gọi hàm hợp lệ.
- **Xử lý lỗi**: Triển khai quy trình xử lý lỗi mạnh mẽ trong các hàm để xử lý một cách thích hợp các dữ liệu đầu vào không mong muốn hoặc lỗi API. Trả về các thông báo lỗi mang tính thông tin mà mô hình có thể dùng để tạo câu trả lời hữu ích cho người dùng.
- **Bảo mật:** Lưu ý đến vấn đề bảo mật khi gọi các API bên ngoài. Sử dụng cơ chế xác thực và uỷ quyền thích hợp. Tránh để lộ dữ liệu nhạy cảm trong các lệnh gọi hàm.
- **Giới hạn mã thông báo:** Nội dung mô tả và tham số của hàm được tính vào giới hạn mã thông báo đầu vào. Nếu bạn đang gặp phải giới hạn mã thông báo, hãy cân nhắc việc giới hạn số lượng hàm hoặc độ dài của nội dung mô tả, chia các tác vụ phức tạp thành các tập hợp hàm nhỏ hơn và tập trung hơn.
- **Kết hợp bash và các công cụ tuỳ chỉnh** Đối với những người tạo bằng cách kết hợp bash và các công cụ tuỳ chỉnh, Gemini 3.1 Pro Preview có một điểm cuối riêng biệt có sẵn thông qua API có tên là [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi#gemini-31-pro-preview-customtools).

## Lưu ý và hạn chế

- Vị trí của các phần trong lệnh gọi hàm: Khi sử dụng các khai báo hàm tuỳ chỉnh [cùng với các công cụ tích hợp sẵn](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi) (như Google Tìm kiếm), mô hình có thể trả về hỗn hợp các phần `functionCall`, `toolCall` và `toolResponse` trong một lượt. Do đó, đừng giả định rằng `functionCall` sẽ luôn là mục cuối cùng trong mảng parts. Nếu bạn đang phân tích cú pháp phản hồi JSON theo cách thủ công, hãy luôn lặp lại mảng parts thay vì dựa vào vị trí.
- Chỉ hỗ trợ [một phần của giản đồ OpenAPI](https://ai.google.dev/api/caching?hl=vi#FunctionDeclaration).
- Đối với chế độ `ANY`, API có thể từ chối các giản đồ rất lớn hoặc được lồng sâu. Nếu bạn gặp lỗi, hãy thử đơn giản hoá tham số hàm và lược đồ phản hồi bằng cách rút ngắn tên thuộc tính, giảm số lượng lồng ghép hoặc giới hạn số lượng khai báo hàm.
- Các loại tham số được hỗ trợ trong Python bị hạn chế.
- Tính năng tự động gọi hàm chỉ có trong Python SDK.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-19 UTC."],[],[]]
