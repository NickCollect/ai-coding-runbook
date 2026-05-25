---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=ar
fetched_at: 2026-05-25T05:24:54.762044+00:00
title: "Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Get started with Gemini Live API using WebSockets

تتيح واجهة برمجة التطبيقات Gemini Live التفاعل الثنائي في الوقت الفعلي مع نماذج Gemini، وتدعم إدخالات الصوت والفيديو والنص ومخرجات الصوت الأصلية. يوضّح هذا الدليل كيفية التكامل مباشرةً مع واجهة برمجة التطبيقات باستخدام بروتوكولات WebSocket الأولية.

[تجربة واجهة برمجة التطبيقات Live في Google AI Studiomic](https://aistudio.google.com/live?hl=ar)
[استنساخ التطبيق النموذجي من GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[استخدام مهارات وكيل الترميزterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar)

## نظرة عامة

تستخدم واجهة برمجة التطبيقات Gemini Live بروتوكولات WebSocket للاتصال في الوقت الفعلي. على عكس استخدام حزمة تطوير برامج (SDK)، يتضمّن هذا النهج إدارة اتصال WebSocket مباشرةً وإرسال الرسائل وتلقّيها بتنسيق JSON محدّد من خلال واجهة برمجة التطبيقات.

المفاهيم الرئيسيّة:

- **نقطة نهاية WebSocket**: عنوان URL محدّد للاتصال به.
- **تنسيق الرسالة**: يتم إجراء جميع الاتصالات من خلال رسائل JSON تتوافق مع بُنيتَي [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentclientmessage) و[`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentservermessage).
- **إدارة الجلسة**: أنت مسؤول عن الحفاظ على اتصال WebSocket.

## المصادقة

تتم عملية المصادقة من خلال تضمين مفتاح واجهة برمجة التطبيقات كمعلَمة طلب بحث في عنوان URL لبروتوكول WebSocket.

تنسيق نقطة النهاية هو:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

استبدِل `YOUR_API_KEY` بمفتاح واجهة برمجة التطبيقات الفعلي.

## المصادقة باستخدام الرموز المميّزة المؤقتة

في حال استخدام [الرموز المميّزة المؤقتة](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ar)، عليك الاتصال بنقطة النهاية `v1alpha`.
يجب تمرير الرمز المميّز المؤقت كمعلَمة طلب بحث `access_token`.

تنسيق نقطة النهاية للمفاتيح المؤقتة هو:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

استبدِل `{short-lived-token}` بالرمز المميّز المؤقت الفعلي.

## الاتصال بواجهة برمجة التطبيقات Live

لبدء جلسة مباشرة، أنشئ اتصال WebSocket بنقطة النهاية التي تمّت المصادقة عليها.
يجب أن تكون الرسالة الأولى التي يتم إرسالها عبر WebSocket هي [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentsetup) التي تحتوي على `config`.
للاطّلاع على خيارات الإعداد الكاملة، يُرجى الرجوع إلى الدليل المرجعي لواجهة برمجة التطبيقات [Live - بروتوكولات WebSocket](https://ai.google.dev/api/live?hl=ar).

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        config_message = {
            "config": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(config_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const configMessage = {
    config: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(configMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## جارٍ إرسال الرسالة النصية

لإرسال إدخال نصي، أنشئ رسالة [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentrealtimeinput) باستخدام الحقل `text`.

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## إرسال ملف الصوت

يجب إرسال الصوت كبيانات PCM أولية (صوت PCM أولي 16 بت، 16 كيلوهرتز، little-endian). أنشئ رسالة [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentrealtimeinput) باستخدام البيانات الصوتية. يُعدّ `mimeType` أمرًا بالغ الأهمية.

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

للاطّلاع على مثال حول كيفية الحصول على الصوت من جهاز العميل (مثل المتصفّح)،
يُرجى الرجوع إلى المثال الشامل على [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## إرسال الفيديو

يتم إرسال إطارات الفيديو كصور فردية (مثل JPEG أو PNG). على غرار الصوت، استخدِم `realtimeInput` مع `Blob`، مع تحديد `mimeType` الصحيح.

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

للاطّلاع على مثال حول كيفية الحصول على الفيديو من جهاز العميل (مثل المتصفّح)،
يُرجى الرجوع إلى المثال الشامل على [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## تلقّي الردود

سيرسل WebSocket رسائل [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentservermessage). عليك تحليل رسائل JSON هذه ومعالجة أنواع مختلفة من المحتوى.

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

للاطّلاع على مثال حول كيفية معالجة الرد، يُرجى الرجوع إلى المثال الشامل على [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## معالجة طلبات استخدام الأدوات

عندما يطلب النموذج استخدام أداة، ستحتوي [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontentservermessage) على حقل `toolCall`. عليك تنفيذ الدالة محليًا وإرسال النتيجة مرة أخرى إلى WebSocket باستخدام رسالة [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=ar#bidigeneratecontenttoolresponse).

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## الخطوات التالية

- [يُرجى قراءة دليل إمكانات واجهة برمجة التطبيقات Live الكامل للاطّلاع على الإمكانات والإعدادات الرئيسية، بما في ذلك ميزة "رصد النشاط الصوتي" وميزات الصوت الأصلية.](https://ai.google.dev/gemini-api/docs/live-guide?hl=ar)
- يُرجى قراءة دليل [استخدام الأدوات](https://ai.google.dev/gemini-api/docs/live-tools?hl=ar) للتعرّف على كيفية دمج واجهة برمجة التطبيقات Live مع الأدوات واستدعاء الدوال.
- يُرجى قراءة دليل [إدارة الجلسات](https://ai.google.dev/gemini-api/docs/live-session?hl=ar) لإدارة المحادثات الطويلة.
- يُرجى قراءة دليل [الرموز المميّزة المؤقتة](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=ar) للمصادقة الآمنة في تطبيقات [من جهة العميل إلى جهة الخادم](#implementation-approach).
- لمزيد من المعلومات عن واجهة برمجة التطبيقات الأساسية لبروتوكولات WebSocket، يُرجى الرجوع إلى [الدليل المرجعي لواجهة برمجة التطبيقات لبروتوكولات WebSocket](https://ai.google.dev/api/live?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
