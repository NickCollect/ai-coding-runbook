---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=hi
fetched_at: 2026-10-12T06:56:46.605301+00:00
title: "Google GenAI SDK \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0915\u0947, Gemini Live API \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0936\u0941\u0930\u0942 \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Google GenAI SDK का इस्तेमाल करके, Gemini Live API का इस्तेमाल शुरू करना

Gemini Live API की मदद से, Gemini मॉडल के साथ रीयल-टाइम में दोनों तरफ़ से बातचीत की जा सकती है. इसमें ऑडियो, वीडियो, और टेक्स्ट इनपुट के साथ-साथ नेटिव ऑडियो आउटपुट की सुविधा भी मिलती है. इस गाइड में, अपने सर्वर पर Google GenAI SDK का इस्तेमाल करके, एपीआई के साथ इंटिग्रेट करने का तरीका बताया गया है.

[Google AI Studio में Live API आज़माएंmic](https://aistudio.google.com/live?hl=hi)
[GitHub से उदाहरण ऐप्लिकेशन क्लोन करेंcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[कोडिंग एजेंट की क्षमताओं का इस्तेमाल करेंterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=hi)

## खास जानकारी

Gemini Live API, रीयल-टाइम में बातचीत करने के लिए WebSockets का इस्तेमाल करता है. `google-genai` एसडीके, इन कनेक्शन को मैनेज करने के लिए एसिंक्रोनस इंटरफ़ेस उपलब्ध कराता है.

मुख्य कॉन्सेप्ट:

- **सेशन**: मॉडल से लगातार कनेक्ट किया जाता है.
- **कॉन्फ़िगरेशन**: इसमें ऑडियो/टेक्स्ट, आवाज़, और सिस्टम के निर्देशों को सेट अप किया जाता है.
- **रीयल-टाइम इनपुट**: ऑडियो और वीडियो फ़्रेम को ब्लोब के तौर पर भेजना.

## Live API से कनेक्ट करना

एपीआई पासकोड की मदद से, Live API सेशन शुरू करने के लिए:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.8-live"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## टेक्स्ट भेजा जा रहा है

टेक्स्ट को `send_realtime_input` (Python) या `sendRealtimeInput` (JavaScript) का इस्तेमाल करके भेजा जा सकता है.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## ऑडियो भेजना

ऑडियो को रॉ पीसीएम डेटा (रॉ 16-बिट पीसीएम ऑडियो, 16kHz, लिटिल-एंडियन) के तौर पर भेजा जाना चाहिए.

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

क्लाइंट डिवाइस (जैसे कि ब्राउज़र) से ऑडियो पाने का उदाहरण देखने के लिए, [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70) पर एंड-टू-एंड उदाहरण देखें.

## वीडियो भेजा जा रहा है

वीडियो फ़्रेम को अलग-अलग इमेज (जैसे, JPEG या PNG) के तौर पर, किसी खास फ़्रेम रेट (ज़्यादा से ज़्यादा एक फ़्रेम प्रति सेकंड) पर भेजा जाता है.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

क्लाइंट डिवाइस (जैसे कि ब्राउज़र) से वीडियो पाने का उदाहरण देखने के लिए, [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120) पर दिया गया पूरा उदाहरण देखें.

## ऑडियो पाना

मॉडल से मिलने वाले ऑडियो जवाब, डेटा के हिस्सों के तौर पर मिलते हैं.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

[अपने सर्वर पर ऑडियो पाने](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) और [उसे ब्राउज़र में चलाने](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174) का तरीका जानने के लिए, GitHub पर उदाहरण ऐप्लिकेशन देखें.

## टेक्स्ट आ रहा है

उपयोगकर्ता के इनपुट और मॉडल के आउटपुट, दोनों के लिए ट्रांसक्रिप्ट, सर्वर के कॉन्टेंट में उपलब्ध होती हैं.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## टूल कॉल मैनेज करना

यह एपीआई, टूल कॉलिंग (फ़ंक्शन कॉलिंग) की सुविधा के साथ काम करता है. जब मॉडल, टूल कॉल का अनुरोध करता है, तब आपको फ़ंक्शन को लागू करना होगा और जवाब वापस भेजना होगा.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## आगे क्या करना है

- मुख्य सुविधाओं और कॉन्फ़िगरेशन के लिए, Live API की [सुविधाओं](https://ai.google.dev/gemini-api/docs/live-guide?hl=hi) से जुड़ी पूरी गाइड पढ़ें. इसमें आवाज़ की गतिविधि का पता लगाने और नेटिव ऑडियो सुविधाओं के बारे में जानकारी शामिल है.
- टूल और फ़ंक्शन कॉलिंग के साथ Live API को इंटिग्रेट करने का तरीका जानने के लिए, [टूल इस्तेमाल करने](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi) से जुड़ी गाइड पढ़ें.
- लंबे समय तक चलने वाली बातचीत को मैनेज करने के लिए, [सेशन मैनेजमेंट](https://ai.google.dev/gemini-api/docs/live-session?hl=hi) गाइड पढ़ें.
- [क्लाइंट-टू-सर्वर](https://ai.google.dev/gemini-api/docs/live-api?hl=hi#implementation-approach) ऐप्लिकेशन में सुरक्षित तरीके से पुष्टि करने के लिए, [एफ़ेमरल टोकन](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=hi) गाइड पढ़ें.
- WebSockets API के बारे में ज़्यादा जानने के लिए, [WebSockets API का रेफ़रंस](https://ai.google.dev/api/live?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-17 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-17 (UTC) को अपडेट किया गया."],[],[]]
