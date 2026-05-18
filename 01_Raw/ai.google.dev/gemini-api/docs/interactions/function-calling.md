---
source_url: https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi
fetched_at: 2026-05-18T05:17:49.421622+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tính năng gọi hàm bằng Gemini API

Tính năng gọi hàm cho phép bạn kết nối các mô hình với các công cụ và API bên ngoài.
Thay vì tạo phản hồi bằng văn bản, mô hình sẽ xác định thời điểm gọi các hàm cụ thể và cung cấp các tham số cần thiết để thực thi các hành động trong thế giới thực.
Điều này cho phép mô hình đóng vai trò là cầu nối giữa ngôn ngữ tự nhiên và các hành động cũng như dữ liệu trong thế giới thực. Tính năng gọi hàm có 3 trường hợp sử dụng chính:

- **Tăng cường kiến thức:** Truy cập thông tin từ các nguồn bên ngoài như cơ sở dữ liệu, API và cơ sở kiến thức.
- **Mở rộng khả năng:** Sử dụng các công cụ bên ngoài để thực hiện phép tính và mở rộng các giới hạn của mô hình, chẳng hạn như sử dụng máy tính hoặc tạo biểu đồ.
- **Thực hiện hành động:** Tương tác với các hệ thống bên ngoài bằng API, chẳng hạn như lên lịch hẹn, tạo hoá đơn, gửi email hoặc điều khiển các thiết bị nhà thông minh.

Xem thời tiết
Lên lịch họp
Tạo biểu đồ

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

schedule_meeting_function = {
    "type": "function",
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string", "description": "Date (e.g., '2024-07-29')"},
            "time": {"type": "string", "description": "Time (e.g., '15:00')"},
            "topic": {"type": "string", "description": "The meeting topic."},
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about Q3 planning.",
    tools=[{"type": "function", **schedule_meeting_function}],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const scheduleMeetingFunction = {
  type: 'function',
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: 'object',
    properties: {
      attendees: { type: 'array', items: { type: 'string' } },
      date: { type: 'string', description: 'Date (e.g., "2024-07-29")' },
      time: { type: 'string', description: 'Time (e.g., "15:00")' },
      topic: { type: 'string', description: 'The meeting topic.' },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.',
  tools: [scheduleMeetingFunction],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

Bạn có thể truyền trực tuyến các lượt tương tác lệnh gọi hàm để nhận các bước gọi công cụ theo gia số khi chúng diễn ra. Để biết thông tin chi tiết về cách truyền phát bằng các công cụ, bao gồm cả cách tích luỹ các mức chênh lệch `arguments` và xử lý các bước `function_call`, hãy xem hướng dẫn [Tương tác truyền phát trực tiếp](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=vi#streaming-with-tools).

## Cách hoạt động của tính năng gọi hàm

![tổng quan về tính năng gọi hàm](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=vi)

Tính năng gọi hàm liên quan đến một hoạt động tương tác có cấu trúc giữa ứng dụng, mô hình và các hàm bên ngoài:

1. **Xác định khai báo hàm:** Xác định tên, tham số và mục đích của hàm cho mô hình.
2. **Gọi LLM bằng các khai báo hàm:** Gửi câu lệnh của người dùng cùng với(các) khai báo hàm đến mô hình.
3. **Thực thi mã hàm (Trách nhiệm của bạn):** Mô hình *không* tự thực thi hàm. Trích xuất tên và đối số rồi thực thi trong ứng dụng của bạn.
4. **Tạo câu trả lời thân thiện với người dùng:** Gửi kết quả trở lại mô hình để có câu trả lời cuối cùng, thân thiện với người dùng.

Quá trình này có thể được lặp lại nhiều lần. Mô hình này hỗ trợ việc gọi nhiều hàm trong một lượt ([gọi hàm song song](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi#parallel_function_calling)) và theo trình tự ([gọi hàm thành phần](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi#compositional_function_calling)).

### Bước 1: Xác định một khai báo hàm

### Python

```
# This will only work for SDK newer than 2.0.0
set_light_values_declaration = {
    "type": "function",
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) -> dict:
    """Set the brightness and color temperature of a room light."""
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const setLightValuesTool = {
  type: 'function',
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: 'object',
    properties: {
      brightness: { type: 'number', description: 'Light level from 0 to 100' },
      color_temp: { type: 'string', enum: ['daylight', 'cool', 'warm'] },
    },
    required: ['brightness', 'color_temp'],
  },
};

function setLightValues(brightness, color_temp) {
  return { brightness: brightness, colorTemperature: color_temp };
}
```

### Bước 2: Gọi mô hình bằng các khai báo hàm

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

# Find the function call step
fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

// Find the function call step
const fcStep = interaction.steps.find(s => s.type === 'function_call');
console.log(fcStep);
```

Mô hình này trả về một bước `function_call` với `type`, `name` và `arguments`:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': 'warm', 'brightness': 25}
```

### Bước 3: Thực thi hàm

### Python

```
# This will only work for SDK newer than 2.0.0
fc_step = next(s for s in interaction.steps if s.type == "function_call")

if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const fcStep = interaction.steps.find(s => s.type === 'function_call');

let result;
if (fcStep.name === 'set_light_values') {
  result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### Bước 4: Gửi kết quả về mô hình

### Python

```
# This will only work for SDK newer than 2.0.0
final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {
            "type": "function_result",
            "name": fc_step.name,
            "call_id": fc_step.id,
            "result": [{"type": "text", "text": json.dumps(result)}],
        }
    ],
    tools=[set_light_values_declaration],
    previous_interaction_id=interaction.id,
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const finalInteraction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

### Gọi hàm không trạng thái

Bạn cũng có thể sử dụng tính năng gọi hàm ở chế độ không trạng thái bằng cách quản lý nhật ký trò chuyện ở phía máy khách và đặt `store=false`.

Ở chế độ không trạng thái, bạn phải truyền toàn bộ nhật ký cuộc trò chuyện trong trường `input` của mỗi yêu cầu tiếp theo. Nhật ký này phải bao gồm:
1. Bước `user_input` ban đầu.
2. Tất cả các bước do mô hình tạo được trả về trong Lượt 1 (bao gồm cả các bước `thought` và `function_call`) chính xác như đã nhận.
3. Bước `function_result` chứa kết quả của hàm mà bạn đã thực thi.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import json

client = genai.Client()

# Initialize history with Turn 1 input
history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
    }
]

# Turn 1: Call model with tools and store=False
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

# Append all model-generated steps (including thoughts and function_calls)
for step in interaction.steps:
    history.append(step.model_dump())

# Find the function call step to execute it
fc_step = next(s for s in interaction.steps if s.type == "function_call")
if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)

# Append the function result as a step
history.append({
    "type": "function_result",
    "name": fc_step.name,
    "call_id": fc_step.id,
    "result": [{"type": "text", "text": json.dumps(result)}],
})

# Turn 2: Send the full history to get the final response
final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  // Initialize history with Turn 1 input
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "Turn the lights down to a romantic level" }]
    }
  ];

  // Turn 1: Call model with tools and store: false
  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  // Append all model-generated steps
  history.push(...interaction.steps);

  // Find and execute function
  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  let result;
  if (fcStep.name === 'set_light_values') {
    result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  }

  // Append function result step
  history.push({
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  });

  // Turn 2: Send full history
  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  console.log(finalInteraction.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with tools and store: false
# Specifies the API revision to avoid breaking changes when they become default
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
      }
    ],
    "tools": [{
      "type": "function",
      "name": "set_light_values",
      "description": "Sets the brightness and color temperature of a light.",
      "parameters": {
        "type": "object",
        "properties": {
          "brightness": {"type": "integer", "description": "Light level from 0 to 100"},
          "color_temp": {"type": "string", "enum": ["daylight", "cool", "warm"]}
        },
        "required": ["brightness", "color_temp"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Extract function call details to execute
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')

# Assume local execution returns: {"brightness": 25, "colorTemperature": "warm"}
RESULT="{\"brightness\": 25, \"colorTemperature\": \"warm\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"set_light_values\",
      \"description\": \"Sets the brightness and color temperature of a light.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"brightness\": {\"type\": \"integer\"},
          \"color_temp\": {\"type\": \"string\"}
        },
        \"required\": [\"brightness\", \"color_temp\"]
      }
    }]
  }"
```

## Khai báo hàm

Một nội dung khai báo hàm được truyền dưới dạng một công cụ và bao gồm:

- `type` (chuỗi): Phải là `"function"` đối với các hàm tuỳ chỉnh.
- `name` (chuỗi): Tên hàm riêng biệt (sử dụng dấu gạch dưới hoặc quy tắc viết hoa chữ cái đầu của từ thứ hai).
- `description` (chuỗi): Giải thích rõ ràng về mục đích của hàm.
- `parameters` (đối tượng): Các tham số đầu vào mà hàm này yêu cầu.
  - `type` (chuỗi): Loại dữ liệu tổng thể, chẳng hạn như `object`.
  - `properties` (đối tượng): Các tham số riêng lẻ có loại và nội dung mô tả.
  - `required` (mảng): Tên tham số bắt buộc.

## Gọi hàm bằng các mô hình tư duy

Các mô hình Gemini 3 và 2.5 sử dụng quy trình ["tư duy"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=vi) nội bộ giúp cải thiện tính năng gọi hàm.
Các SDK sẽ tự động xử lý [chữ ký ý tưởng](https://ai.google.dev/gemini-api/docs/interactions/thought-signatures?hl=vi) cho bạn.

## Gọi hàm song song

Gọi nhiều hàm cùng lúc khi chúng độc lập:

### Python

```
# This will only work for SDK newer than 2.0.0
power_disco_ball = {"type": "function", "name": "power_disco_ball", "description": "Powers the disco ball.",
    "parameters": {"type": "object", "properties": {"power": {"type": "boolean"}}, "required": ["power"]}}
start_music = {"type": "function", "name": "start_music", "description": "Play music.",
    "parameters": {"type": "object", "properties": {"energetic": {"type": "boolean"}, "loud": {"type": "boolean"}}, "required": ["energetic", "loud"]}}
dim_lights = {"type": "function", "name": "dim_lights", "description": "Dim the lights.",
    "parameters": {"type": "object", "properties": {"brightness": {"type": "number"}}, "required": ["brightness"]}}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Turn this place into a party!",
    tools=[power_disco_ball, start_music, dim_lights],
    generation_config={"tool_choice": "any"},
)

for step in interaction.steps:
    if step.type == "function_call":
        args = ", ".join(f"{key}={val}" for key, val in step.arguments.items())
        print(f"{step.name}({args})")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const powerDiscoBall = { type: 'function', name: 'power_disco_ball', description: 'Powers the disco ball.',
  parameters: { type: 'object', properties: { power: { type: 'boolean' } }, required: ['power'] } };
const startMusic = { type: 'function', name: 'start_music', description: 'Play music.',
  parameters: { type: 'object', properties: { energetic: { type: 'boolean' }, loud: { type: 'boolean' } }, required: ['energetic', 'loud'] } };
const dimLights = { type: 'function', name: 'dim_lights', description: 'Dim the lights.',
  parameters: { type: 'object', properties: { brightness: { type: 'number' } }, required: ['brightness'] } };

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: 'Turn this place into a party!',
  tools: [powerDiscoBall, startMusic, dimLights],
  generation_config: { tool_choice: 'any' },
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

## Gọi hàm kết hợp

Nối nhiều lệnh gọi hàm với nhau cho các yêu cầu phức tạp (ví dụ: trước tiên, hãy lấy vị trí, sau đó lấy thông tin thời tiết cho vị trí đó).

### Python

```
# This will only work for SDK newer than 2.0.0
get_weather_forecast_declaration = {
    "type": "function",
    "name": "get_weather_forecast",
    "description": "Gets the current weather temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The location"},
        },
        "required": ["location"],
    },
}

set_thermostat_temperature_declaration = {
    "type": "function",
    "name": "set_thermostat_temperature",
    "description": "Sets the thermostat to a desired temperature.",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "integer",
                "description": "The temperature in Celsius",
            },
        },
        "required": ["temperature"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    tools=[
        get_weather_forecast_declaration,
        set_thermostat_temperature_declaration,
    ],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
    elif hasattr(step, "content") and step.content:
         for part in step.content:
             if hasattr(part, "text"):
                 print(part.text)
```

## Chế độ gọi hàm

Kiểm soát cách mô hình sử dụng các công cụ bằng cách sử dụng `tool_choice` trong `generation_config`:

- `auto` (Mặc định): Mô hình quyết định có gọi một hàm hay phản hồi trực tiếp.
- `any`: Mô hình bị hạn chế để luôn dự đoán một lệnh gọi hàm.
- `none`: Mô hình không được phép thực hiện lệnh gọi hàm.
- `validated` (Xem trước): Mô hình đảm bảo tuân thủ giản đồ hàm.

### Python

```
# This will only work for SDK newer than 2.0.0
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools": ["get_current_temperature"]
        }
    }
}
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const generation_config = {
  tool_choice: {
    allowed_tools: {
      mode: 'any',
      tools: ['get_current_temperature']
    }
  }
};
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the temperature in Boston?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string"}
        },
        "required": ["location"]
      }
    }],
    "generation_config": {
      "tool_choice": {
        "allowed_tools": {
          "mode": "any",
          "tools": ["get_current_temperature"]
        }
      }
    }
  }'
```

## Sử dụng dụng cụ đa năng

Bạn có thể bật nhiều công cụ, kết hợp các công cụ tích hợp sẵn với tính năng gọi hàm trong cùng một yêu cầu. Các mô hình Gemini 3 có thể kết hợp các công cụ tích hợp với tính năng gọi hàm ngay lập tức trong phần Tương tác. Việc truyền `previous_interaction_id` sẽ tự động lưu hành ngữ cảnh công cụ tích hợp.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "get_weather",
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

tools = [
    {"type": "google_search"},  # Built-in tool
    get_weather                 # Custom tool
]

# Turn 1: Initial request with both tools enabled
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        # Execute your custom function locally
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        # Turn 2: Provide the function result back to the model.
        # Passing `previous_interaction_id` automatically circulates the
        # built-in Google Search context from Turn 1
        interaction_2 = client.interactions.create(
            model="gemini-3-flash-preview",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool              // Custom tool
];

// Turn 1: Initial request with both tools enabled
let interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        // Execute your custom function locally
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        // Turn 2: Provide the function result back to the model.
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3-flash-preview',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.steps.at(-1).content[0].text);
    }
}
```

## Phản hồi của hàm đa phương thức

Đối với các mô hình Gemini 3, bạn có thể đưa nội dung đa phương thức vào các phần phản hồi của hàm mà bạn gửi đến mô hình. Mô hình có thể xử lý nội dung đa phương thức này trong lượt tiếp theo để đưa ra câu trả lời có nhiều thông tin hơn.

Để đưa dữ liệu đa phương thức vào phản hồi của hàm, hãy thêm dữ liệu đó dưới dạng một hoặc nhiều khối nội dung trong trường `result` của bước `function_result`. Mỗi khối nội dung phải chỉ định `type` (ví dụ: `"text"`, `"image"`).

Ví dụ sau đây cho thấy cách gửi một phản hồi hàm chứa dữ liệu hình ảnh trở lại mô hình trong một lượt tương tác:

### Python

```
# This will only work for SDK newer than 2.0.0
import base64
from google import genai
import requests

client = genai.Client()

# Find the function call step
tool_call = next(s for s in interaction.steps if s.type == "function_call")

# Execute your tool to get image bytes
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction.id,
    input=[
        {
            "type": "function_result",
            "name": tool_call.name,
            "call_id": tool_call.id,
            "result": [
                {"type": "text", "text": "instrument.jpg"},
                {
                    "type": "image",
                    "mime_type": "image/jpeg",
                    "data": base64_image_data,
                },
            ],
        }
    ],
)

print(final_interaction.steps[-1].content[0].text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Find the function call step
const toolCall = interaction.steps.find(s => s.type === 'function_call');

// Execute your tool to get image bytes and convert to base64
// (Implementation depends on your environment)
const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction.id,
    input: [{
        type: 'function_result',
        name: toolCall.name,
        call_id: toolCall.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }]
});

console.log(finalInteraction.steps.at(-1).content[0].text);
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [
      {
        "type": "function_result",
        "name": "get_image",
        "call_id": "call_123",
        "result": [
          {"type": "text", "text": "instrument.jpg"},
          {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "BASE64_IMAGE_DATA"
          }
        ]
      }
    ]
  }'
```

## Gọi hàm bằng đầu ra có cấu trúc

Đối với các mô hình dòng Gemini 3, hãy kết hợp lệnh gọi hàm với [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=vi) để có các câu trả lời được định dạng nhất quán.

## MCP (Giao thức ngữ cảnh mô hình) từ xa

API Tương tác hỗ trợ việc kết nối với các máy chủ MCP từ xa để cấp cho mô hình quyền truy cập vào các công cụ và dịch vụ bên ngoài. Bạn cung cấp `name` và `url` của máy chủ trong cấu hình công cụ.

Khi sử dụng MCP từ xa, hãy lưu ý những giới hạn sau:

- **Các loại máy chủ**: MCP từ xa chỉ hoạt động với các máy chủ HTTP có thể truyền phát. Không được hỗ trợ máy chủ SSE (Sự kiện do máy chủ gửi).
- **Hỗ trợ mô hình**: MCP từ xa hiện không hoạt động với các mô hình Gemini 3. Chúng tôi sẽ sớm hỗ trợ Gemini 3.
- **Đặt tên**: Tên máy chủ MCP không được chứa ký tự `-`. Thay vào đó, hãy sử dụng tên máy chủ `snake_case`.

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `type` | `string` | Có | Phải là `"mcp_server"`. |
| `name` | `string` | Không | Tên hiển thị của máy chủ MCP. |
| `url` | `string` | Không | URL đầy đủ cho điểm cuối của máy chủ MCP. |
| `headers` | `object` | Không | Các cặp khoá-giá trị được gửi dưới dạng tiêu đề HTTP trong mỗi yêu cầu đến máy chủ (ví dụ: mã thông báo xác thực). |
| `allowed_tools` | `array` | Không | Hạn chế những công cụ mà tác nhân có thể gọi từ máy chủ. |

### Ví dụ:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="Check the status of my last server deployment.",
    tools=[
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"},
        }
    ]
)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-2.5-flash',
    input: 'Check the status of my last server deployment.',
    tools: [
        {
            type: 'mcp_server',
            name: 'Deployment Tracker',
            url: 'https://mcp.example.com/mcp',
            headers: { Authorization: 'Bearer my-token' }
        }
    ]
});
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
-d '{
    "model": "gemini-2.5-flash",
    "input": "Check the status of my last server deployment.",
    "tools": [
        {
            "type": "mcp_server",
            "name": "Deployment Tracker",
            "url": "https://mcp.example.com/mcp",
            "headers": {"Authorization": "Bearer my-token"}
        }
    ]
}'
```

## Các phương pháp hay nhất

- **Mô tả chức năng và tham số:** Rõ ràng và cụ thể.
- **Đặt tên:** Sử dụng tên mô tả không có dấu cách hoặc ký tự đặc biệt.
- **Nhập mạnh:** Sử dụng các loại cụ thể (số nguyên, chuỗi, enum).
- **Lựa chọn công cụ:** Giữ số lượng công cụ đang hoạt động ở mức tối đa là 10 đến 20.
- **Thiết kế câu lệnh:** Cung cấp bối cảnh và hướng dẫn.
- **Xác thực:** Xác thực các lệnh gọi hàm trước khi thực thi.
- **Xử lý lỗi:** Triển khai biện pháp xử lý lỗi hữu ích.
- **Bảo mật:** Sử dụng phương thức xác thực phù hợp cho các API bên ngoài.

## Lưu ý và giới hạn

- Chỉ hỗ trợ [một phần của giản đồ OpenAPI](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=vi#FunctionDeclaration).
- Đối với chế độ `any`, API có thể từ chối các giản đồ rất lớn hoặc được lồng sâu.
- Các loại tham số được hỗ trợ trong Python bị hạn chế.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-16 UTC."],[],[]]
