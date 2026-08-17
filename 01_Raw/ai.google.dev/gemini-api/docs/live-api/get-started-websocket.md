---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=hi
fetched_at: 2026-08-17T02:35:44.988544+00:00
title: "WebSockets \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0915\u0947, Gemini Live API \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0936\u0941\u0930\u0942 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# WebSockets का इस्तेमाल करके, Gemini Live API का इस्तेमाल शुरू करना

Gemini Live API की मदद से, Gemini के मॉडल के साथ रीयल-टाइम में दोनों तरफ़ से बातचीत की जा सकती है. यह ऑडियो, वीडियो, और टेक्स्ट इनपुट के साथ-साथ नेटिव ऑडियो आउटपुट के साथ काम करता है. इस गाइड में, रॉ वेबसॉकेट का इस्तेमाल करके, सीधे तौर पर एपीआई के साथ इंटिग्रेट करने का तरीका बताया गया है.

[Google AI Studio में Live API आज़माएंmic](https://aistudio.google.com/live?hl=hi)
[GitHub से उदाहरण ऐप्लिकेशन क्लोन करेंcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[कोडिंग एजेंट की क्षमताओं का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi)

## खास जानकारी

Gemini Live API, रीयल-टाइम में कम्यूनिकेशन के लिए WebSockets का इस्तेमाल करता है. एसडीके टूल का इस्तेमाल करने के बजाय, इस तरीके में WebSocket कनेक्शन को सीधे तौर पर मैनेज किया जाता है. साथ ही, एपीआई के तय किए गए JSON फ़ॉर्मैट में मैसेज भेजे और पाए जाते हैं.

मुख्य कॉन्सेप्ट:

- **WebSocket एंडपॉइंट**: कनेक्ट करने के लिए खास यूआरएल.
- **मैसेज का फ़ॉर्मैट**: सभी कम्यूनिकेशन, JSON मैसेज के ज़रिए किए जाते हैं. ये मैसेज, [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentclientmessage) और [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentservermessage) स्ट्रक्चर के मुताबिक होते हैं.
- **सेशन मैनेजमेंट**: WebSocket कनेक्शन को बनाए रखने की ज़िम्मेदारी आपकी होती है.

## पुष्टि करना

पुष्टि करने की प्रोसेस को मैनेज करने के लिए, WebSocket यूआरएल में अपनी एपीआई कुंजी को क्वेरी पैरामीटर के तौर पर शामिल करें.

एंडपॉइंट का फ़ॉर्मैट यह है:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

`YOUR_API_KEY` की जगह अपनी एपीआई कुंजी डालें.

## कुछ समय के लिए मान्य टोकन की मदद से पुष्टि करना

अगर [कुछ समय के लिए मान्य टोकन](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=hi) का इस्तेमाल किया जा रहा है, तो आपको `v1beta` एंडपॉइंट से कनेक्ट करना होगा.
अस्थायी टोकन को `access_token` क्वेरी पैरामीटर के तौर पर पास करना ज़रूरी है.

अस्थायी कुंजियों के लिए एंडपॉइंट का फ़ॉर्मैट यह है:

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

`{short-lived-token}` की जगह असल इफ़ेमरल टोकन डालें.

## Live API से कनेक्ट करना

लाइव सेशन शुरू करने के लिए, पुष्टि किए गए एंडपॉइंट से WebSocket कनेक्शन बनाएं.
WebSocket पर भेजा गया पहला मैसेज, [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentsetup) होना चाहिए. इसमें `config` शामिल होना चाहिए.
कॉन्फ़िगरेशन के सभी विकल्पों के बारे में जानने के लिए, [लाइव एपीआई - WebSockets API के बारे में जानकारी](https://ai.google.dev/api/live?hl=hi) देखें.

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
const MODEL_NAME = "gemini-3.1-flash-live-preview";
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

## टेक्स्ट भेजें

टेक्स्ट इनपुट भेजने के लिए, `text` फ़ील्ड के साथ [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentrealtimeinput) मैसेज बनाएं.

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

## ऑडियो भेजें

ऑडियो को रॉ पीसीएम डेटा (रॉ 16-बिट पीसीएम ऑडियो, 16kHz, लिटिल-एंडियन) के तौर पर भेजा जाना चाहिए. ऑडियो डेटा की मदद से, [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentrealtimeinput) मैसेज बनाएं. `mimeType` बहुत ज़रूरी है.

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

क्लाइंट डिवाइस (जैसे कि ब्राउज़र) से ऑडियो पाने का उदाहरण देखने के लिए, [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74) पर एंड-टू-एंड उदाहरण देखें.

## वीडियो भेजें

वीडियो फ़्रेम को अलग-अलग इमेज (जैसे, JPEG या PNG) के तौर पर भेजा जाता है. ऑडियो की तरह ही, `realtimeInput` का इस्तेमाल `Blob` के साथ करें. साथ ही, सही `mimeType` की जानकारी दें.

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

क्लाइंट डिवाइस (जैसे कि ब्राउज़र) से वीडियो पाने का उदाहरण देखने के लिए, [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222) पर दिया गया पूरा उदाहरण देखें.

## जवाब पाना

WebSocket, [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentservermessage) मैसेज वापस भेजेगा. आपको इन JSON मैसेज को पार्स करना होगा और अलग-अलग तरह के कॉन्टेंट को मैनेज करना होगा.

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

रिस्पॉन्स को मैनेज करने का उदाहरण देखने के लिए, [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75) पर दिया गया पूरा उदाहरण देखें.

## टूल कॉल मैनेज करना

जब मॉडल, टूल कॉल का अनुरोध करता है, तब [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontentservermessage) में `toolCall` फ़ील्ड शामिल होता है. आपको फ़ंक्शन को स्थानीय तौर पर लागू करना होगा. साथ ही, [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=hi#bidigeneratecontenttoolresponse) मैसेज का इस्तेमाल करके, नतीजे को WebSocket पर वापस भेजना होगा.

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

## आगे क्या करना है

- मुख्य सुविधाओं और कॉन्फ़िगरेशन के लिए, Live API की [सुविधाओं](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi) से जुड़ी पूरी गाइड पढ़ें. इसमें आवाज़ की गतिविधि का पता लगाने और नेटिव ऑडियो सुविधाओं के बारे में जानकारी शामिल है.
- टूल और फ़ंक्शन कॉलिंग के साथ Live API को इंटिग्रेट करने का तरीका जानने के लिए, [टूल इस्तेमाल करने](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi) से जुड़ी गाइड पढ़ें.
- लंबे समय तक चलने वाली बातचीत को मैनेज करने के लिए, [सेशन मैनेजमेंट](https://ai.google.dev/gemini-api/docs/live-session?hl=hi) गाइड पढ़ें.
- [क्लाइंट-टू-सर्वर](#implementation-approach) ऐप्लिकेशन में सुरक्षित तरीके से पुष्टि करने के लिए, [एफ़ेमरल टोकन](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=hi) गाइड पढ़ें.
- WebSockets API के बारे में ज़्यादा जानकारी के लिए, [WebSockets API के बारे में जानकारी](https://ai.google.dev/api/live?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-07-23 (UTC) को अपडेट किया गया."],[],[]]
