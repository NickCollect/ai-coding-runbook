---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=he
fetched_at: 2026-10-26T05:55:33.355927+00:00
title: "\u05d0\u05d9\u05da \u05de\u05ea\u05d7\u05d9\u05dc\u05d9\u05dd \u05dc\u05d4\u05e9\u05ea\u05de\u05e9 \u05d1-Gemini Live API \u05d1\u05d0\u05de\u05e6\u05e2\u05d5\u05ea WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# איך מתחילים להשתמש ב-Gemini Live API באמצעות WebSockets

‫Gemini Live API מאפשר אינטראקציה דו-כיוונית עם מודלים של Gemini בזמן אמת, ותומך בקלט של אודיו, וידאו וטקסט, וגם בפלט אודיו מקורי. במדריך הזה מוסבר איך לבצע שילוב ישירות עם ה-API באמצעות WebSockets גולמיים.

[אפשר לנסות את Live API ב-Google AI Studiomic](https://aistudio.google.com/live?hl=he)
[שיבוט של אפליקציית הדוגמה מ-GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[שימוש במיומנויות של סוכן תכנותterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=he)

## סקירה כללית

‫Gemini Live API משתמש ב-WebSockets לתקשורת בזמן אמת. בגישה הזו, בניגוד לשימוש ב-SDK, צריך לנהל ישירות את חיבור ה-WebSocket ולשלוח ולקבל הודעות בפורמט JSON ספציפי שמוגדר על ידי ה-API.

מושגים מרכזיים:

- **נקודת קצה של WebSocket**: כתובת ה-URL הספציפית להתחברות.
- **פורמט ההודעה**: כל התקשורת מתבצעת באמצעות הודעות JSON שתואמות למבנים של [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentclientmessage) ושל [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentservermessage).
- **ניהול סשנים**: אתם אחראים לתחזוקת חיבור ה-WebSocket.

## אימות

האימות מתבצע על ידי הוספת מפתח ה-API כפרמטר של שאילתה בכתובת ה-URL של WebSocket.

הפורמט של נקודת הקצה הוא:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

מחליפים את הערך `YOUR_API_KEY` במפתח ה-API שלכם.

## אימות באמצעות טוקנים זמניים

אם אתם משתמשים ב[טוקנים זמניים](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=he), אתם צריכים להתחבר לנקודת הקצה `v1beta`.
צריך להעביר את הטוקן הזמני כפרמטר שאילתה `access_token`.

פורמט נקודת הקצה של מפתחות זמניים הוא:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

מחליפים את `{short-lived-token}` באסימון האפמרי בפועל.

## חיבור ל-API של נתונים בזמן אמת

כדי להתחיל סשן בזמן אמת, צריך ליצור חיבור WebSocket לנקודת הקצה המאומתת.
ההודעה הראשונה ששולחים באמצעות WebSocket חייבת להיות [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentsetup) שמכילה את `config`.
אפשרויות ההגדרה המלאות מפורטות במאמרי העזרה של ה-API [Live API - WebSockets API reference](https://ai.google.dev/api/live?hl=he).

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.8-live"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
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
const MODEL_NAME = "gemini-3.8-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
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

## שליחת הודעת טקסט

כדי לשלוח קלט טקסט, יוצרים הודעה מסוג [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentrealtimeinput) עם השדה `text`.

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

## שלח אודיו

צריך לשלוח את האודיו כנתוני PCM גולמיים (אודיו PCM גולמי של 16 ביט, 16kHz, little-endian). יוצרים הודעה [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentrealtimeinput) עם נתוני האודיו. ה-`mimeType` הוא קריטי.

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

דוגמה לאופן שבו מקבלים את האודיו ממכשיר הלקוח (למשל, הדפדפן) מופיעה בדוגמה המפורטת ב-[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## שלח סרטון

מסגרות של סרטונים נשלחות כתמונות נפרדות (למשל, JPEG או PNG). בדומה לאודיו, משתמשים ב-`realtimeInput` עם `Blob` ומציינים את `mimeType` הנכון.

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

דוגמה לאופן קבלת הסרטון ממכשיר הלקוח (למשל, הדפדפן) מופיעה בדוגמה המפורטת ב-[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## קבלת תשובות

ה-WebSocket ישלח בחזרה הודעות [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentservermessage). צריך לנתח את הודעות ה-JSON האלה ולטפל בסוגים שונים של תוכן.

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

דוגמה לאופן הטיפול בתגובה מופיעה בדוגמה מקצה לקצה ב-[GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## טיפול בקריאות לכלי

כשהמודל מבקש הפעלת כלי, השדה [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=he#bidigeneratecontentservermessage) יכיל את השדה `toolCall`. צריך להריץ את הפונקציה באופן מקומי ולשלוח את התוצאה בחזרה ל-WebSocket באמצעות הודעה מסוג [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=he#bidigeneratecontenttoolresponse).

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

## המאמרים הבאים

- במדריך המלא בנושא [יכולות](https://ai.google.dev/gemini-api/docs/live-guide?hl=he) של Live API מוסבר על היכולות וההגדרות העיקריות, כולל זיהוי פעילות קולית ותכונות אודיו מקוריות.
- במדריך [שימוש בכלי](https://ai.google.dev/gemini-api/docs/live-tools?hl=he) מוסבר איך לשלב את Live API עם כלים ובקשות להפעלת פונקציות.
- כדי לנהל שיחות ארוכות, כדאי לקרוא את המדריך בנושא [ניהול סשנים](https://ai.google.dev/gemini-api/docs/live-session?hl=he).
- קוראים את המדריך בנושא [טוקנים זמניים](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=he) לאימות מאובטח באפליקציות [client-to-server](#implementation-approach).
- מידע נוסף על WebSockets API מופיע ב[מאמרי העזרה של ה-API של WebSockets](https://ai.google.dev/api/live?hl=he).

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-17 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-17 (שעון UTC)."],[],[]]
