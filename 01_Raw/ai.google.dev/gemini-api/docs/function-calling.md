---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=ja
fetched_at: 2026-06-15T06:26:14.131217+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Gemini API を使用した関数呼び出し

関数呼び出しを使用すると、モデルを外部ツールや API に接続できます。モデルは、テキスト レスポンスを生成する代わりに、特定の関数を呼び出すタイミングを判断し、現実世界のアクションを実行するために必要なパラメータを提供します。これにより、モデルは自然言語と現実世界のアクションやデータの間のブリッジとして機能できます。関数呼び出しには、主に次の 3 つのユースケースがあります。

- [**アクションを実行する:**](#meeting) API を使用して外部システムとやり取りします。たとえば、予定のスケジュール設定、請求書の作成、メールの送信、スマートホーム デバイスの制御などです。
- [**知識の補強:**](#weather) データベース、API、ナレッジベースなどの外部ソースから情報にアクセスします。
- [**機能の拡張:**](#chart) 外部ツールを使用して計算を実行し、モデルの制限を拡張します（電卓の使用やグラフの作成など）。

これらのユースケースの例については、以下をご覧ください。

### 会議のスケジュール

この例では、特定の時間に会議をスケジュールする関数を定義する方法を示します。これにより、モデルはユーザー リクエストを解析し、構造化された引数を返して外部システムでアクションをトリガーできます。

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

### 天気情報を取得する

この例では、ある場所の気温データを取得する関数を定義する方法を示します。これにより、モデルはリアルタイムまたは外部情報を必要とするクエリに回答するために外部 API を呼び出すことができます。

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

### グラフを作成

次の例は、構造化データから棒グラフを生成する関数を定義する方法を示しています。この例では、モデルが外部ツールを使用して計算を実行したり、ビジュアル アセットを作成したりする方法を示しています。

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

## 関数呼び出しの仕組み

![関数呼び出しの概要](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=ja)

関数呼び出しでは、アプリケーション、モデル、外部関数間の構造化されたやり取りが行われます。プロセスの詳細は次のとおりです。

1. **関数宣言を定義する:** アプリケーション コードで関数宣言を定義します。関数宣言は、関数の名前、パラメータ、目的をモデルに記述します。
2. **関数宣言を使用して API を呼び出す:** ユーザーのプロンプトと関数宣言をモデルに送信します。リクエストを分析し、関数呼び出しが役立つかどうかを判断します。その場合、関数名、引数、一意の `id` を含む構造化 JSON オブジェクトで応答します（この `id` は、Gemini 3 モデルの API で常に返されるようになりました\*）。
3. ***関数コードの実行（お客様の責任）:** モデルは関数自体を実行しません。レスポンスを処理して関数呼び出しを確認するのは、アプリケーションの責任です。*- **はい**: 関数の名前、引数、`id` を抽出し、アプリケーション内の対応する関数を実行します。
   - **いいえ:** モデルがプロンプトに直接テキスト レスポンスを提供しました（このフローは例ではあまり強調されていませんが、考えられる結果です）。
4. **ユーザー フレンドリーなレスポンスを作成する:** 関数が実行された場合は、結果を取得してモデルに送り返します。その際、会話の次のターンで一致する `id` を含めます。モデルはこの結果を使用して、関数呼び出しからの情報を取り込んだ、ユーザー フレンドリーな最終的なレスポンスを生成します。

このプロセスは複数回繰り返すことができ、複雑なインタラクションとワークフローが可能になります。このモデルは、1 回のターンで複数の関数を呼び出す（[並列関数呼び出し](#parallel_function_calling)）、順番に呼び出す（[構成関数呼び出し](#compositional_function_calling)）、組み込みの Gemini ツールを使用して呼び出す（[マルチツール使用](#native-tools)）こともサポートしています。

\* **関数 ID を常にマッピングする:** Gemini 3 は、すべての `functionCall` で一意の `id` を返すようになりました。モデルが結果を元のリクエストに正確にマッピングできるように、この `id` を `functionResponse` に含めます。

### ステップ 1: 関数宣言を定義する

ユーザーが照明の値を設定して API リクエストを行うことができる関数とその宣言を、アプリケーション コード内で定義します。この関数は、外部サービスまたは API を呼び出すことができます。

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

### ステップ 2: 関数宣言を使用してモデルを呼び出す

関数宣言を定義したら、モデルにそれらを使用するように指示できます。プロンプトと関数宣言を分析し、直接応答するか関数を呼び出すかを決定します。関数が呼び出されると、レスポンス オブジェクトに関数呼び出しの候補が含まれます。

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

次に、モデルは、ユーザーの質問に回答するために宣言された 1 つ以上の関数を呼び出す方法を指定する OpenAPI 互換スキーマの `functionCall` オブジェクトを返します。

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

### ステップ 3: set\_light\_values 関数コードを実行する

モデルのレスポンスから関数呼び出しの詳細を抽出し、引数を解析して、`set_light_values` 関数を実行します。

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

### ステップ 4: 関数結果を含むユーザー フレンドリーなレスポンスを作成し、モデルを再度呼び出す

最後に、関数実行の結果をモデルに送り返します。モデルはこの情報をユーザーへの最終的なレスポンスに組み込みます。

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

これで関数呼び出しフローは完了です。モデルは `set_light_values` 関数を使用して、ユーザーのリクエスト アクションを正常に実行しました。

## 関数宣言

プロンプトで関数呼び出しを実装する場合は、1 つ以上の `function declarations` を含む `tools` オブジェクトを作成します。関数は JSON を使用して定義します。具体的には、[OpenAPI スキーマ](https://spec.openapis.org/oas/v3.0.3#schemaw)形式の[サブセットを選択](https://ai.google.dev/api/caching?hl=ja#Schema)します。1 つの関数宣言に含めることができるパラメータは、次のとおりです。

- `name`（文字列）: 関数の固有の名前（`get_weather_forecast`、`send_email`）。スペースや特殊文字を含まない説明的な名前を使用します（アンダースコアまたは camelCase を使用します）。
- `description`（文字列）: 関数の目的と機能についての明確で詳細な説明。これは、モデルが関数を使用するタイミングを理解するために重要です。具体的で、必要に応じて例を挙げてください（「現在映画館で上映中の映画のタイトルと、必要に応じて位置情報に基づいて映画館を検索します。」）。
- `parameters`（オブジェクト）: 関数が想定する入力パラメータを定義します。
  - `type`（文字列）: 全体的なデータ型（`object` など）を指定します。
  - `properties`（オブジェクト）: 個々のパラメータを一覧表示します。各パラメータには次の情報が含まれます。
    - `type`（文字列）: パラメータのデータ型（`string`、`integer`、`boolean, array` など）。
    - `description`（文字列）: パラメータの目的と形式の説明。例と制約を指定します（「市区町村と都道府県（例: 「カリフォルニア州サンフランシスコ」）または郵便番号（例: 「95616」）を指定します。」）。
    - `enum`（配列、省略可）: パラメータ値が固定セットの場合、説明で説明するだけでなく、「enum」を使用して許容値を一覧表示します。これにより、精度が向上します（「enum」: ["daylight", "cool", "warm"]）。
  - `required`（配列）: 関数の動作に必須のパラメータ名を列挙した文字列の配列。

`types.FunctionDeclaration.from_callable(client=client, callable=your_function)` を使用して、Python 関数から `FunctionDeclarations` を直接構築することもできます。

## 思考モデルを使用した関数呼び出し

Gemini 3 シリーズと Gemini 2.5 シリーズのモデルは、リクエストを推論するために内部の「思考」プロセスを使用します。これにより、関数呼び出しのパフォーマンスが大幅に向上し、モデルが関数を呼び出すタイミングと使用するパラメータをより適切に判断できるようになります。Gemini API はステートレスであるため、モデルは[思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja)を使用して、マルチターンの会話でコンテキストを維持します。

このセクションでは、思考シグネチャの詳細管理について説明します。このセクションは、API リクエストを手動で作成する場合（REST 経由など）や、会話履歴を操作する場合にのみ必要です。

**[Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=ja)（Google の公式ライブラリ）を使用している場合は、このプロセスを管理する必要はありません**。SDK は、前述の[例](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-4)に示すように、必要な手順を自動的に処理します。

### 会話履歴を手動で管理する

会話履歴を手動で変更する場合は、[以前の完全なレスポンス](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#step-4)を送信する代わりに、モデルのターンに含まれる `thought_signature` を正しく処理する必要があります。

モデルのコンテキストが保持されるように、次のルールに従ってください。

- 常に、元の [`Part`](https://ai.google.dev/api?hl=ja#request-body-structure) 内のモデルに `thought_signature` を送り返します。
- **API が結果を正しいリクエストにマッピングできるように、`function_call` の正確な `id` を常に `function_response` に含めてください。**
- シグネチャを含む `Part` と含まないものを結合しないでください。これにより、思考の位置コンテキストが損なわれます。
- 署名文字列はマージできないため、両方に署名が含まれている 2 つの `Parts` を結合しないでください。

#### Gemini 3 の思考シグネチャ

Gemini 3 では、モデル レスポンスの任意の [`Part`](https://ai.google.dev/api?hl=ja#request-body-structure) に思考シグネチャを含めることができます。一般的に、すべての `Part` タイプからシグネチャを返すことをおすすめしますが、関数呼び出しでは思考シグネチャを渡す必要があります。会話履歴を手動で操作しない限り、Google GenAI SDK が思考シグネチャを自動的に処理します。

会話履歴を手動で操作する場合は、[思考シグネチャ](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ja)のページで、Gemini 3 の思考シグネチャの処理に関する完全なガイダンスと詳細を参照してください。

##### 思考シグネチャの検査

実装には必要ありませんが、デバッグや学習のためにレスポンスを調べて `thought_signature` を確認できます。

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

思考シグネチャの制限事項と使用方法、および思考モデル全般については、[思考](https://ai.google.dev/gemini-api/docs/thinking?hl=ja#signatures)のページをご覧ください。

## 並列関数呼び出し

単一ターンの関数呼び出しに加えて、複数の関数を一度に呼び出すこともできます。並列関数呼び出しを使用すると、複数の関数を同時に実行できます。これは、関数が相互に依存していない場合に使用されます。これは、複数の独立したソースからデータを収集するシナリオ（異なるデータベースから顧客の詳細を取得する、さまざまな倉庫の在庫レベルを確認する、アパートをディスコに改造するなど複数のアクションを実行する）で役立ちます。

モデルが 1 ターンで複数の関数呼び出しを開始する場合、`function_call` オブジェクトが受信された順序と同じ順序で `function_result` オブジェクトを返す必要はありません。Gemini API は、モデルの出力の `id` を使用して、各結果を対応する呼び出しにマッピングします。これにより、関数を非同期で実行し、完了した結果をリストに追加できます。

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

指定されたすべてのツールを使用できるように関数呼び出しモードを構成します。詳細については、[関数呼び出しの構成](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#function_calling_modes)をご覧ください。

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

出力された結果はそれぞれ、モデルがリクエストした単一の関数呼び出しを反映しています。結果を返すには、リクエストされた順序と同じ順序でレスポンスを含めます。

Python SDK は、Python 関数を宣言に自動的に変換し、関数呼び出しの実行とレスポンスのサイクルを処理する[自動関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#automatic_function_calling_python_only)をサポートしています。以下は、ディスコのユースケースの例です。

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

## コンポジション関数呼び出し

構成関数呼び出しまたは順次関数呼び出しを使用すると、Gemini は複数の関数呼び出しを連結して、複雑なリクエストを満たすことができます。たとえば、「現在地の気温を教えて」という質問に答えるために、Gemini API は最初に `get_current_location()` 関数を呼び出し、次に位置情報をパラメータとして受け取る `get_weather()` 関数を呼び出すことがあります。

次の例は、Python SDK と自動関数呼び出しを使用して、構成関数呼び出しを実装する方法を示しています。

### Python

この例では、`google-genai` Python SDK の自動関数呼び出し機能を使用します。SDK は、Python 関数を必要なスキーマに自動的に変換し、モデルからリクエストされたときに関数呼び出しを実行して、結果をモデルに送り返してタスクを完了します。

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

**想定される出力**

コードを実行すると、SDK が関数呼び出しをオーケストレートしていることがわかります。モデルは最初に `get_weather_forecast` を呼び出し、Temperature を受け取ってから、プロンプトのロジックに基づいて正しい値で `set_thermostat_temperature` を呼び出します。

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

この例では、JavaScript/TypeScript SDK を使用して、手動実行ループで合成関数呼び出しを行う方法を示します。

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

**想定される出力**

コードを実行すると、SDK が関数呼び出しをオーケストレートしていることがわかります。モデルは最初に `get_weather_forecast` を呼び出し、Temperature を受け取ってから、プロンプトのロジックに基づいて正しい値で `set_thermostat_temperature` を呼び出します。

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

構成関数呼び出しは、ネイティブの [Live API](https://ai.google.dev/gemini-api/docs/live?hl=ja) 機能です。つまり、Live API は Python SDK と同様に関数呼び出しを処理できます。

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

## 関数呼び出しモード

Gemini API を使用すると、モデルが提供されたツール（関数宣言）を使用する方法を制御できます。具体的には、`function_calling_config` 内でモードを設定できます。

- `VALIDATED`: ツール組み合わせのデフォルト モード（組み込みツールまたは構造化出力も有効になっている場合）。モデルは、関数呼び出しまたは自然言語のいずれかを予測するように制約され、関数スキーマの準拠が保証されます。`allowed_function_names` が指定されていない場合、モデルは使用可能なすべての関数宣言から選択します。`allowed_function_names` が指定されている場合、モデルは許可された関数のセットから選択します。このモードでは、不正な形式の関数呼び出しが減少します（`AUTO` モードと比較して）。
- `AUTO`: function\_declarations ツールのみが有効になっている場合のデフォルト モード。モデルは、プロンプトとコンテキストに基づいて、自然言語によるレスポンスを生成するか、関数呼び出しを提案するかを決定します。
- `ANY`: モデルは常に関数呼び出しを予測するように制約され、関数スキーマの準拠が保証されます。`allowed_function_names` が指定されていない場合、モデルは指定された関数宣言のいずれかを選択できます。`allowed_function_names` がリストとして指定されている場合、モデルはそのリスト内の関数からのみ選択できます。すべてのプロンプトに関数呼び出しのレスポンスが必要な場合は、このモードを使用します（該当する場合）。
- `NONE`: モデルは関数呼び出しを行うことが*禁止*されています。これは、関数宣言なしでリクエストを送信するのと同じです。これを使用すると、ツール定義を削除せずに関数呼び出しを一時的に無効にできます。

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

## 自動関数呼び出し（Python のみ）

Python SDK を使用する場合は、Python 関数をツールとして直接指定できます。SDK はこれらの関数を宣言に変換し、関数呼び出しの実行を管理し、レスポンス サイクルを処理します。型ヒントと docstring を使用して関数を定義します。最適な結果を得るには、[Google スタイルの docstring](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) を使用することをおすすめします。SDK は次の処理を自動的に行います。

1. モデルからの関数呼び出しレスポンスを検出します。
2. コードで対応する Python 関数を呼び出します。
3. 関数のレスポンスをモデルに送り返します。
4. モデルの最終的なテキスト レスポンスを返します。

現在、SDK は引数の説明を解析して、生成された関数宣言のプロパティの説明スロットに格納しません。代わりに、docstring 全体を最上位の関数説明として送信します。

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

自動関数呼び出しは、次のコマンドで無効にできます。

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### 関数スキーマの自動宣言

API は次のいずれかの型を記述できます。`Pydantic` 型は、定義されたフィールドも許可された型で構成されている限り許可されます。ここでは辞書型（`dict[str: int]` など）は十分にサポートされていないため、使用しないでください。

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

推定スキーマを確認するには、[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable) を使用して変換します。

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

## マルチツールの使用: 組み込みツールと関数呼び出しを組み合わせる

複数のツールを有効にして、同じリクエストで組み込みツールと関数呼び出しを組み合わせることができます。

Gemini 3 モデルは、ツール コンテキスト循環機能により、組み込みツールと関数呼び出しをすぐに組み合わせることができます。詳しくは、[組み込みツールと関数呼び出しの組み合わせ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)をご覧ください。

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

Gemini 3 シリーズより前のモデルでは、[Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=ja) を使用します。

## マルチモーダル関数レスポンス

Gemini 3 シリーズのモデルでは、モデルに送信する関数レスポンス部分にマルチモーダル コンテンツを含めることができます。モデルは、次のターンでこのマルチモーダル コンテンツを処理して、より多くの情報に基づいたレスポンスを生成できます。関数レスポンスのマルチモーダル コンテンツでは、次の MIME タイプがサポートされています。

- **画像**: `image/png`、`image/jpeg`、`image/webp`
- **ドキュメント**: `application/pdf`、`text/plain`

関数レスポンスにマルチモーダル データを含めるには、`functionResponse` 部分内にネストされた 1 つ以上の部分としてデータを含めます。各マルチモーダル部分には、`inlineData` を含める必要があります。構造化された `response` フィールド内からマルチモーダル パートを参照する場合は、一意の `displayName` を含める必要があります。

JSON 参照形式 `{"$ref": "<displayName>"}` を使用して、`functionResponse` 部分の構造化された `response` フィールド内からマルチモーダル部分を参照することもできます。モデルは、レスポンスの処理時に参照をマルチモーダル コンテンツに置き換えます。各 `displayName` は、構造化された `response` フィールドで 1 回だけ参照できます。

次の例は、`get_image` という名前の関数の `functionResponse` と、`displayName: "instrument.jpg"` を含む画像データを含むネストされた部分を含むメッセージを示しています。`functionResponse` の `response` フィールドは、この画像部分を参照します。

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

## 構造化出力を使用した関数呼び出し

Gemini 3 シリーズのモデルでは、[構造化出力](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja)で関数呼び出しを使用できます。これにより、モデルは特定のスキーマに準拠する関数呼び出しまたは出力を予測できます。その結果、モデルが関数呼び出しを生成しない場合でも、一貫した形式のレスポンスを受信できます。

## モデル コンテキスト プロトコル（MCP）

[Model Context Protocol（MCP）](https://modelcontextprotocol.io/introduction)は、AI アプリケーションを外部のツールやデータに接続するためのオープン スタンダードです。MCP は、モデルが関数（ツール）、データソース（リソース）、事前定義されたプロンプトなどのコンテキストにアクセスするための共通プロトコルを提供します。

Gemini SDK には MCP のサポートが組み込まれているため、ボイラープレート コードが削減され、MCP ツール用の[自動ツール呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja#automatic_function_calling_python_only)が提供されます。モデルが MCP ツール呼び出しを生成すると、Python と JavaScript のクライアント SDK は MCP ツールを自動的に実行し、後続のリクエストでレスポンスをモデルに送り返します。このループは、モデルがツール呼び出しを行わなくなるまで続きます。

Gemini と `mcp` SDK でローカル MCP サーバーを使用する方法の例については、こちらをご覧ください。

### Python

選択したプラットフォームに最新バージョンの [`mcp` SDK](https://modelcontextprotocol.io/introduction) がインストールされていることを確認します。

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

選択したプラットフォームに最新バージョンの `mcp` SDK がインストールされていることを確認します。

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

### 組み込みの MCP サポートの制限事項

組み込みの MCP サポートは SDK の[試験運用版](https://ai.google.dev/gemini-api/docs/models?hl=ja#preview)の機能であり、次の制限があります。

- ツールのみがサポートされ、リソースやプロンプトはサポートされません
- これは、Python と JavaScript/TypeScript の SDK で使用できます。
- 今後のリリースで破壊的変更が発生する可能性があります。

これらの制限によって構築するものが制限される場合は、MCP サーバーの手動統合をいつでも選択できます。

## サポートされているモデル

このセクションでは、モデルとその関数呼び出し機能の一覧を示します。試験運用版モデルは含まれていません。機能の包括的な概要については、[モデルの概要](https://ai.google.dev/gemini-api/docs/models?hl=ja)ページをご覧ください。

| モデル | 関数呼び出し | 並列関数呼び出し | コンポジション関数呼び出し |
| --- | --- | --- | --- |
| [Gemini 3.1 Pro プレビュー版](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ja) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ja) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ja) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ja) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ja) | ✔️ | ✔️ | ✔️ |

## ベスト プラクティス

- **関数とパラメータの説明:** 説明は、非常に明確かつ具体的に記述します。モデルは、この説明に基づいて正しい関数を選択し、適切な引数を指定します。
- **命名:** 説明的な関数名を使用します（スペース、ピリオド、ダッシュは使用しません）。
- **強い型指定:** パラメータに特定の型（整数、文字列、列挙型）を使用して、エラーを減らします。パラメータの有効な値のセットが限られている場合は、列挙型を使用します。
- **ツールの選択:** モデルでは任意の数のツールを使用できますが、ツールが多すぎると、誤ったツールや最適でないツールが選択されるリスクが高まる可能性があります。最良の結果を得るには、コンテキストやタスクに関連するツールのみを提供することを目指します。理想的には、アクティブなセットを最大 10 ～ 20 個に保ちます。ツールの合計数が多い場合は、会話のコンテキストに基づく動的なツール選択を検討してください。
- **プロンプト エンジニアリング:**
  - コンテキストを提供する: モデルに役割を伝えます（例: 「あなたは有能な天気アシスタントです。」）。
  - 指示を出す: 関数をいつ、どのように使用するかを指定します（例: 「日付を推測しないでください。予測には常に将来の日付を使用してください。」）。
  - 明確化を促す: 必要に応じて、明確化を求める質問をするようモデルに指示します。
  - これらのプロンプトの設計に関する戦略については、[エージェント ワークフロー](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja#agentic-workflows)をご覧ください。テスト済みの[システム指示](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ja#agentic-si-template)の例を次に示します。
- **Temperature:** より確定的で信頼性の高い関数呼び出しには、低い Temperature（0 など）を使用します。
- **検証:** 関数呼び出しが重大な結果をもたらす場合（注文など）、それを実行する前にユーザーにその呼び出しの妥当性を確認してください。
- **終了理由を確認する:** モデルのレスポンスで [`finishReason`](https://ai.google.dev/api/generate-content?hl=ja#FinishReason) を常に確認し、モデルが有効な関数呼び出しを生成できなかったケースを処理します。
- **エラー処理**: 関数で堅牢なエラー処理を実装して、予期しない入力や API の障害を適切に処理します。モデルがユーザーに役立つ回答を生成するために使用できる、有益なエラー メッセージを返します。
- **セキュリティ:** 外部 API を呼び出す際は、セキュリティに注意してください。適切な認証と認可のメカニズムを使用します。関数呼び出しでセンシティブ データを公開しないようにします。
- **トークンの上限:** 関数の説明とパラメータは、入力トークンの上限にカウントされます。トークンの上限に達した場合は、関数の数や説明の長さを制限するか、複雑なタスクをより小さな、より集約された関数セットに分割することを検討してください。
- **bash とカスタムツールの組み合わせ**: bash とカスタムツールの組み合わせで構築している場合、Gemini 3.1 Pro プレビューには、[`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ja#gemini-31-pro-preview-customtools) という API を介して利用できる個別のエンドポイントが付属しています。

## 注意と制限事項

- 関数呼び出し部分の配置: カスタム関数宣言を[組み込みツール](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ja)（Google 検索など）とともに使用する場合、モデルは 1 回のターンで `functionCall`、`toolCall`、`toolResponse` の部分を混在させて返すことがあります。そのため、`functionCall` が常に parts 配列の最後の項目であるとは限りません。JSON レスポンスを手動で解析する場合は、位置に依存するのではなく、常に parts 配列を反復処理してください。
- [OpenAPI スキーマのサブセット](https://ai.google.dev/api/caching?hl=ja#FunctionDeclaration)のみがサポートされています。
- `ANY` モードの場合、API は非常に大きなスキーマやネストが深いスキーマを拒否することがあります。エラーが発生した場合は、プロパティ名を短くしたり、ネストを減らしたり、関数宣言の数を制限したりして、関数パラメータとレスポンス スキーマを簡素化してみてください。
- Python でサポートされているパラメータの型は限られています。
- 自動関数呼び出しは Python SDK の機能です。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-06-10 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-06-10 UTC。"],[],[]]
