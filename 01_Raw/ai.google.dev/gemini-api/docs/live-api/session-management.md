---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=hi
fetched_at: 2026-07-06T05:17:56.172495+00:00
title: "Live API \u0915\u0940 \u092e\u0926\u0926 \u0938\u0947 \u0938\u0947\u0936\u0928 \u092e\u0948\u0928\u0947\u091c \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Live API की मदद से सेशन मैनेज करना

लाइव एपीआई में, सेशन का मतलब है ऐसा कनेक्शन जो लगातार बना रहता है. इसमें, एक ही कनेक्शन पर इनपुट और आउटपुट की स्ट्रीमिंग लगातार होती रहती है. इस बारे में ज़्यादा जानें कि [यह कैसे काम करता है](https://ai.google.dev/gemini-api/docs/live?hl=hi).
सेशन के इस यूनीक डिज़ाइन की वजह से, कम समय में डेटा ट्रांसफ़र किया जा सकता है. साथ ही, इसमें यूनीक सुविधाएं भी मिलती हैं. हालांकि, इससे कुछ समस्याएं भी आ सकती हैं. जैसे, सेशन की समयसीमा तय होना और सेशन का समय से पहले खत्म हो जाना.
इस गाइड में, सेशन के मैनेजमेंट से जुड़ी उन समस्याओं को हल करने की रणनीतियों के बारे में बताया गया है जो Live API का इस्तेमाल करते समय आ सकती हैं.

## सेशन की समयसीमा

कंप्रेशन के बिना, सिर्फ़ ऑडियो वाले सेशन 15 मिनट तक और ऑडियो-वीडियो वाले सेशन दो मिनट तक ही चल सकते हैं. इन सीमाओं से ज़्यादा समय तक सेशन चलाने पर
सेशन खत्म हो जाएगा. साथ ही, कनेक्शन भी खत्म हो जाएगा. हालांकि,
[कॉन्टेक्स्ट विंडो कंप्रेशन](#context-window-compression) का इस्तेमाल करके,
सेशन को अनलिमिटेड समय तक चलाया जा सकता है.

कनेक्शन की समयसीमा भी सीमित होती है. यह करीब 10 मिनट तक ही चल सकता है. कनेक्शन खत्म होने पर, सेशन भी खत्म हो जाता है. [ऐसे में, सेशन को फिर से शुरू करने की सुविधा का इस्तेमाल करके, एक सेशन को कई कनेक्शन पर चालू रखा जा सकता है.](#session-resumption)
कनेक्शन खत्म होने से पहले, आपको [GoAway मैसेज](#goaway-message) भी मिलेगा.
इससे आपको आगे की कार्रवाई करने में मदद मिलेगी.

## कॉन्टेक्स्ट विंडो कंप्रेशन

सेशन को ज़्यादा समय तक चलाने और कनेक्शन के अचानक खत्म होने से बचने के लिए, सेशन के कॉन्फ़िगरेशन के हिस्से के तौर पर,
[contextWindowCompression](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
फ़ील्ड सेट करके, कॉन्टेक्स्ट विंडो कंप्रेशन की सुविधा चालू की जा सकती है.

[ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=hi#contextwindowcompressionconfig) में, [स्लाइडिंग-विंडो मैकेनिज़्म](https://ai.google.dev/api/live?hl=hi#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
और [टोकन की संख्या](https://ai.google.dev/api/live?hl=hi#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
को कॉन्फ़िगर किया जा सकता है. इससे कंप्रेशन ट्रिगर होता है.

### Python

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.
        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.AUDIO],
  contextWindowCompression: { slidingWindow: {} }
};
```

## सेशन को फिर से शुरू करना

सर्वर के समय-समय पर WebSocket
कनेक्शन रीसेट करने पर, सेशन को खत्म होने से रोकने के लिए, [sessionResumption](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
फ़ील्ड को [सेटअप कॉन्फ़िगरेशन](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentSetup) में कॉन्फ़िगर करें.

इस कॉन्फ़िगरेशन को पास करने पर,
सर्वर [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=hi#SessionResumptionUpdate)
मैसेज भेजता है. इसका इस्तेमाल, अगले कनेक्शन के [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=hi#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)
के तौर पर, पिछले रेज़्युमशन
टोकन को पास करके, सेशन को फिर से शुरू करने के लिए किया जा सकता है.

रेज़्युमशन टोकन, पिछले सेशन के खत्म होने के दो घंटे बाद तक मान्य होते हैं.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.1-flash-live-preview"

async def main():
    print(f"Connecting to the service with handle {previous_session_handle}...")
    async with client.aio.live.connect(
        model=model,
        config=types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            session_resumption=types.SessionResumptionConfig(
                # The handle of the session to resume is passed here,
                # or else None to start a new session.
                handle=previous_session_handle
            ),
        ),
    ) as session:
        while True:
            await session.send_client_content(
                turns=types.Content(
                    role="user", parts=[types.Part(text="Hello world!")]
                )
            )
            async for message in session.receive():
                # Periodically, the server will send update messages that may
                # contain a handle for the current state of the session.
                if message.session_resumption_update:
                    update = message.session_resumption_update
                    if update.resumable and update.new_handle:
                        # The handle should be retained and linked to the session.
                        return update.new_handle

                # For the purposes of this example, placeholder input is continually fed
                # to the model. In non-sample code, the model inputs would come from
                # the user.
                if message.server_content and message.server_content.turn_complete:
                    break

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.1-flash-live-preview';

async function live() {
  const responseQueue = [];

  async function waitMessage() {
    let done = false;
    let message = undefined;
    while (!done) {
      message = responseQueue.shift();
      if (message) {
        done = true;
      } else {
        await new Promise((resolve) => setTimeout(resolve, 100));
      }
    }
    return message;
  }

  async function handleTurn() {
    const turns = [];
    let done = false;
    while (!done) {
      const message = await waitMessage();
      turns.push(message);
      if (message.serverContent && message.serverContent.turnComplete) {
        done = true;
      }
    }
    return turns;
  }

console.debug('Connecting to the service with handle %s...', previousSessionHandle)
const session = await ai.live.connect({
  model: model,
  callbacks: {
    onopen: function () {
      console.debug('Opened');
    },
    onmessage: function (message) {
      responseQueue.push(message);
    },
    onerror: function (e) {
      console.debug('Error:', e.message);
    },
    onclose: function (e) {
      console.debug('Close:', e.reason);
    },
  },
  config: {
    responseModalities: [Modality.AUDIO],
    sessionResumption: { handle: previousSessionHandle }
    // The handle of the session to resume is passed here, or else null to start a new session.
  }
});

const inputTurns = 'Hello how are you?';
session.sendClientContent({ turns: inputTurns });

const turns = await handleTurn();
for (const turn of turns) {
  if (turn.sessionResumptionUpdate) {
    if (turn.sessionResumptionUpdate.resumable && turn.sessionResumptionUpdate.newHandle) {
      let newHandle = turn.sessionResumptionUpdate.newHandle
      // ...Store newHandle and start new session with this handle here
    }
  }
}

  session.close();
}

async function main() {
  await live().catch((e) => console.error('got error', e));
}

main();
```

## सेशन डिसकनेक्ट होने से पहले मैसेज पाना

सर्वर एक [GoAway](https://ai.google.dev/api/live?hl=hi#GoAway) मैसेज भेजता है. इससे पता चलता है कि मौजूदा
कनेक्शन जल्द ही खत्म हो जाएगा. इस मैसेज में [timeLeft](https://ai.google.dev/api/live?hl=hi#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left) शामिल होता है. इससे पता चलता है कि कनेक्शन खत्म होने में कितना समय बचा है. साथ ही, इससे आपको कनेक्शन के ABORTED के तौर पर खत्म होने से पहले, आगे की कार्रवाई करने में मदद मिलती है.

### Python

```
async for response in session.receive():
    if response.go_away is not None:
        # The connection will soon be terminated
        print(response.go_away.time_left)
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.goAway) {
    console.debug('Time left: %s\n', turn.goAway.timeLeft);
  }
}
```

## जनरेशन पूरा होने पर मैसेज पाना

सर्वर एक [generationComplete](https://ai.google.dev/api/live?hl=hi#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
मैसेज भेजता है. इससे पता चलता है कि मॉडल ने जवाब जनरेट कर लिया है.

### Python

```
async for response in session.receive():
    if response.server_content.generation_complete is True:
        # The generation is complete
```

### JavaScript

```
const turns = await handleTurn();

for (const turn of turns) {
  if (turn.serverContent && turn.serverContent.generationComplete) {
    // The generation is complete
  }
}
```

## आगे क्या करना है

लाइव एपीआई के साथ काम करने के अन्य तरीकों के बारे में जानने के लिए, सुविधाओं की पूरी
[गाइड](https://ai.google.dev/gemini-api/docs/live?hl=hi), टूल के [इस्तेमाल वाला](https://ai.google.dev/gemini-api/docs/live-tools?hl=hi) पेज या
[Live API कुकबुक](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=hi) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-01 (UTC) को अपडेट किया गया."],[],[]]
