---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi
fetched_at: 2026-09-28T06:31:54.573236+00:00
title: "Lyria RealTime \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0915\u0947, \u0930\u0940\u092f\u0932-\u091f\u093e\u0907\u092e \u092e\u0947\u0902 \u0938\u0902\u0917\u0940\u0924 \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria RealTime का इस्तेमाल करके, रीयल-टाइम में संगीत जनरेट करना

Gemini API, [Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=hi) का इस्तेमाल करके, रीयल-टाइम में संगीत जनरेट करने वाले बेहतरीन मॉडल का ऐक्सेस देता है. इससे डेवलपर ऐसे ऐप्लिकेशन बना सकते हैं जिनमें उपयोगकर्ता, इंटरैक्टिव तरीके से संगीत बना सकते हैं, उसे लगातार चला सकते हैं, और वाद्य संगीत बना सकते हैं.

Lyria RealTime की मदद से रीयल-टाइम में संगीत जनरेट करने की सुविधा का इस्तेमाल करने के लिए, लगातार काम करने वाले, दोनों दिशाओं में डेटा ट्रांसफ़र करने वाले, और कम इंतज़ार के समय वाले स्ट्रीमिंग कनेक्शन का इस्तेमाल किया जाता है. इसके लिए, [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल किया जाता है.

Lyria RealTime का इस्तेमाल करके क्या-क्या बनाया जा सकता है, यह जानने के लिए इसे AI Studio पर आज़माएं. इसके लिए, [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=hi) या [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=hi) ऐप्लिकेशन का इस्तेमाल करें.

## संगीत जनरेट करना और उसे कंट्रोल करना

Lyria RealTime, [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi) की तरह ही काम करता है. यह मॉडल के साथ रीयल-टाइम कम्यूनिकेशन बनाए रखने के लिए, Websockets का इस्तेमाल करता है.

नीचे दिए गए कोड में, संगीत जनरेट करने का तरीका बताया गया है:

### Python

इस उदाहरण में, `client.aio.live.music.connect()` का इस्तेमाल करके Lyria RealTime सेशन को शुरू किया गया है. इसके बाद, `session.set_weighted_prompts()` का इस्तेमाल करके शुरुआती प्रॉम्प्ट भेजा गया है. साथ ही, `session.set_music_generation_config` का इस्तेमाल करके शुरुआती कॉन्फ़िगरेशन भेजा गया है. इसके बाद, `session.play()` का इस्तेमाल करके संगीत जनरेट करने की प्रोसेस शुरू की गई है. साथ ही, `receive_audio()` को सेट अप किया गया है, ताकि यह मिले हुए ऑडियो चंक को प्रोसेस कर सके.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1beta'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

इस उदाहरण में, `client.live.music.connect()` का इस्तेमाल करके Lyria RealTime सेशन शुरू किया गया है. इसके बाद, `session.setWeightedPrompts()` के साथ शुरुआती प्रॉम्प्ट भेजा गया है. साथ ही, `session.setMusicGenerationConfig` का इस्तेमाल करके शुरुआती कॉन्फ़िगरेशन सेट अप किया गया है. इसके बाद, `session.play()` का इस्तेमाल करके संगीत जनरेट करने की सुविधा शुरू की गई है. साथ ही, `onMessage` कॉलबैक सेट अप किया गया है, ताकि मिले हुए ऑडियो चंक को प्रोसेस किया जा सके.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1beta" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

इसके बाद, सेशन को शुरू करने, रोकने, बंद करने या रीसेट करने के लिए, `session.play()`, `session.pause()`, `session.stop()`, और `session.reset_context()` का इस्तेमाल किया जा सकता है.

## रीयल-टाइम में संगीत को कंट्रोल करना

रीयल-टाइम में संगीत जनरेट करने के लिए, प्रॉम्प्ट भेजे जा सकते हैं. साथ ही, जनरेशन पैरामीटर को रीयल टाइम में अपडेट किया जा सकता है.

### Lyria RealTime को प्रॉम्प्ट करना

स्ट्रीम चालू रहने के दौरान, जनरेट किए गए संगीत में बदलाव करने के लिए, किसी भी समय नए `WeightedPrompt` मैसेज भेजे जा सकते हैं. नया इनपुट मिलने पर, मॉडल आसानी से ट्रांज़िशन कर लेगा.

प्रॉम्प्ट सही फ़ॉर्मैट में होने चाहिए. इनमें `text` (असल प्रॉम्प्ट) और `weight` शामिल होना चाहिए. `weight` में `0` को छोड़कर कोई भी वैल्यू हो सकती है. `1.0`से शुरुआत करना आम तौर पर अच्छा होता है.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

ध्यान दें कि प्रॉम्प्ट में अचानक बदलाव करने पर, मॉडल ट्रांज़िशन में कुछ समय लग सकता है. इसलिए, हमारा सुझाव है कि मॉडल को इंटरमीडिएट वेट वैल्यू भेजकर, किसी तरह का क्रॉस-फ़ेडिंग लागू करें.

### कॉन्फ़िगरेशन अपडेट करना

रीयल टाइम में संगीत जनरेट करने की सुविधा के पैरामीटर अपडेट करके, संगीत जनरेट करने की प्रोसेस को कंट्रोल किया जा सकता है. सिर्फ़ किसी पैरामीटर को अपडेट नहीं किया जा सकता. आपको पूरा कॉन्फ़िगरेशन सेट करना होगा. ऐसा न करने पर, अन्य फ़ील्ड की वैल्यू वापस डिफ़ॉल्ट वैल्यू पर रीसेट हो जाएंगी.

बीपीएम या स्केल को अपडेट करने से, मॉडल में काफ़ी बदलाव होता है. इसलिए, आपको मॉडल को यह भी बताना होगा कि वह `reset_context()` का इस्तेमाल करके अपने कॉन्टेक्स्ट को रीसेट करे, ताकि वह नई कॉन्फ़िगरेशन को ध्यान में रख सके. इससे स्ट्रीम बंद नहीं होगी, लेकिन यह एक मुश्किल ट्रांज़िशन होगा. आपको अन्य पैरामीटर के लिए ऐसा करने की ज़रूरत नहीं है.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Lyria RealTime को प्रॉम्प्ट करना

Lyria RealTime, म्यूज़िकल जॉनर, इंस्ट्रूमेंट, और मूड को डाइनैमिक तरीके से मिक्स करने के लिए, वेटेज वाले प्रॉम्प्ट का इस्तेमाल करता है. प्रॉम्प्ट स्टीयरिंग की रणनीतियों, कीवर्ड टैग की शब्दावलियों, और प्रॉम्प्ट के पूरे उदाहरणों के बारे में जानने के लिए, [Lyria की प्रॉम्प्ट के लिए गाइड](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide?hl=hi#realtime-prompting) देखें.

## सबसे सही तरीके

- क्लाइंट ऐप्लिकेशन में, ऑडियो बफ़रिंग की मज़बूत सुविधा लागू होनी चाहिए, ताकि ऑडियो को बिना किसी रुकावट के चलाया जा सके. इससे नेटवर्क जिटर और जनरेशन में लगने वाले समय में मामूली अंतर का पता लगाने में मदद मिलती है.
- असरदार प्रॉम्प्ट लिखना:
  - ब्यौरा दें. मूड, शैली, और इंस्ट्रुमेंट के बारे में बताने वाले विशेषणों का इस्तेमाल करें.
  - धीरे-धीरे बदलाव करें और आगे बढ़ें. प्रॉम्प्ट को पूरी तरह से बदलने के बजाय, संगीत को ज़्यादा आसानी से बदलने के लिए, उसमें एलिमेंट जोड़ें या उनमें बदलाव करें.
  - `WeightedPrompt` पर वेट के साथ एक्सपेरिमेंट करें, ताकि यह तय किया जा सके कि नया प्रॉम्प्ट, मौजूदा जनरेशन पर कितना असर डालेगा.

## तकनीकी जानकारी

इस सेक्शन में, Lyria RealTime की संगीत जनरेट करने की सुविधा को इस्तेमाल करने के बारे में खास जानकारी दी गई है.

### विशेषताएं

- आउटपुट फ़ॉर्मैट: रॉ 16-बिट पीसीएम ऑडियो
- सैंपल रेट: 48 किलोहर्ट्ज़
- चैनल: 2 (स्टीरियो)

### कंट्रोल

संगीत जनरेट करने की सुविधा पर, रीयल टाइम में असर डाला जा सकता है. इसके लिए, ऐसे मैसेज भेजें जिनमें ये शामिल हों:

- `WeightedPrompt`: यह एक टेक्स्ट स्ट्रिंग होती है. इसमें संगीत के आइडिया, शैली, वाद्य यंत्र, मूड या विशेषता के बारे में बताया जाता है. अलग-अलग स्टाइल को मिक्स करने के लिए, एक से ज़्यादा प्रॉम्प्ट दिए जा सकते हैं. Lyria RealTime को बेहतर तरीके से प्रॉम्प्ट करने के बारे में ज़्यादा जानने के लिए, [ऊपर](#steer-music) देखें.
- `MusicGenerationConfig`: संगीत जनरेट करने की प्रोसेस के लिए कॉन्फ़िगरेशन. इससे आउटपुट ऑडियो की विशेषताओं पर असर पड़ता है. पैरामीटर
  include:
  - `guidance`: (फ़्लोट) रेंज: `[0.0, 6.0]`. डिफ़ॉल्ट: `4.0`.
    इससे यह कंट्रोल किया जाता है कि मॉडल, प्रॉम्प्ट का कितनी सख्ती से पालन करे. ज़्यादा गाइडेंस से, प्रॉम्प्ट के हिसाब से वीडियो बनाने में मदद मिलती है. हालांकि, इससे वीडियो के ट्रांज़िशन अचानक होते हैं.
  - `bpm`: (int) रेंज: `[60, 200]`.
    इससे जनरेट किए गए संगीत के लिए, बीट प्रति मिनट की संख्या सेट की जाती है. आपको मॉडल के कॉन्टेक्स्ट को रोकना/चलाना या रीसेट करना होगा, ताकि वह नए बीपीएम को ध्यान में रख सके.
  - `density`: (फ़्लोट) रेंज: `[0.0, 1.0]`.
    इससे म्यूज़िकल नोट/आवाज़ की डेंसिटी को कंट्रोल किया जाता है. कम वैल्यू से, कम म्यूज़िक जनरेट होता है. वहीं, ज़्यादा वैल्यू से "ज़्यादा" म्यूज़िक जनरेट होता है.
  - `brightness`: (फ़्लोट) रेंज: `[0.0, 1.0]`.
    इससे टोनल क्वालिटी को अडजस्ट किया जाता है. ज़्यादा वैल्यू से, ऑडियो "ज़्यादा चमकदार" लगता है. इससे आम तौर पर, ज़्यादा फ़्रीक्वेंसी पर ज़ोर दिया जाता है.
  - `scale`: (Enum)
    इससे जनरेट किए जाने वाले संगीत का स्केल (की और मोड) सेट किया जाता है. SDK टूल की ओर से दी गई [`Scale` enum वैल्यू](#scale-enum) का इस्तेमाल करें. आपको मॉडल के लिए कॉन्टेक्स्ट को रोकना/चलाना या रीसेट करना होगा, ताकि वह नए स्केल को ध्यान में रख सके.
  - `mute_bass`: (bool) डिफ़ॉल्ट: `False`.
    इससे यह कंट्रोल किया जाता है कि मॉडल, आउटपुट के बेस को कम करे या नहीं.
  - `mute_drums`: (bool) डिफ़ॉल्ट: `False`.
    इस विकल्प से यह कंट्रोल किया जाता है कि मॉडल के आउटपुट में ड्रम की आवाज़ कम हो.
  - `only_bass_and_drums`: (bool) डिफ़ॉल्ट: `False`.
    मॉडल को सिर्फ़ बास और ड्रम का आउटपुट देने के लिए निर्देश दें.
  - `music_generation_mode`: (Enum)
    इससे मॉडल को यह पता चलता है कि उसे संगीत के `QUALITY` (डिफ़ॉल्ट वैल्यू) या `DIVERSITY` पर फ़ोकस करना चाहिए. इसे `VOCALIZATION` पर भी सेट किया जा सकता है, ताकि मॉडल किसी दूसरे इंस्ट्रुमेंट के तौर पर आवाज़ें जनरेट कर सके. इसके लिए, उन्हें नए प्रॉम्प्ट के तौर पर जोड़ें.
- `PlaybackControl`: प्लेबैक को कंट्रोल करने के लिए निर्देश. जैसे, चलाना, रोकना, बंद करना या कॉन्टेक्स्ट रीसेट करना.

`bpm`, `density`, `brightness`, और `scale` के लिए, अगर कोई वैल्यू नहीं दी जाती है, तो मॉडल आपके शुरुआती प्रॉम्प्ट के हिसाब से सबसे सही वैल्यू तय करेगा.

`MusicGenerationConfig` में, ज़्यादा क्लासिकल पैरामीटर भी पसंद के मुताबिक बनाए जा सकते हैं. जैसे, `temperature` (0.0 से 3.0, डिफ़ॉल्ट 1.1), `top_k` (1 से 1000, डिफ़ॉल्ट 40), और `seed` (0 से 2,147,483,647, डिफ़ॉल्ट रूप से रैंडम तरीके से चुना जाता है).

#### स्केल Enum वैल्यू

यहां स्केल की वे सभी वैल्यू दी गई हैं जिन्हें मॉडल स्वीकार कर सकता है:

| Enum वैल्यू | स्केल / कुंजी |
| --- | --- |
| `C_MAJOR_A_MINOR` | सी मेजर / ए माइनर |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | D♭ मेजर / B♭ माइनर |
| `D_MAJOR_B_MINOR` | डी मेजर / बी माइनर |
| `E_FLAT_MAJOR_C_MINOR` | E♭ मेजर / C माइनर |
| `E_MAJOR_D_FLAT_MINOR` | E major / C♯/D♭ minor |
| `F_MAJOR_D_MINOR` | एफ़ मेजर / डी माइनर |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | G♭ मेजर / E♭ माइनर |
| `G_MAJOR_E_MINOR` | जी मेजर / ई माइनर |
| `A_FLAT_MAJOR_F_MINOR` | A♭ मेजर / F माइनर |
| `A_MAJOR_G_FLAT_MINOR` | ए मेजर / एफ़♯/जी♭ माइनर |
| `B_FLAT_MAJOR_G_MINOR` | B♭ मेजर / G माइनर |
| `B_MAJOR_A_FLAT_MINOR` | B मेजर / G♯/A♭ माइनर |
| `SCALE_UNSPECIFIED` | डिफ़ॉल्ट / मॉडल तय करता है |

यह मॉडल, बजाए जाने वाले नोट के बारे में जानकारी दे सकता है. हालांकि, यह रिलेटिव की के बीच अंतर नहीं कर सकता. इसलिए, हर enum, रिलेटिव मेजर और माइनर, दोनों से मेल खाता है. उदाहरण के लिए, `C_MAJOR_A_MINOR` पियानो की सभी सफ़ेद कुंजियों के बराबर होगा. वहीं, `F_MAJOR_D_MINOR` बी फ़्लैट को छोड़कर, सभी सफ़ेद कुंजियों के बराबर होगा.

### सीमाएं

- सिर्फ़ इंस्ट्रुमेंटल संगीत: मॉडल सिर्फ़ इंस्ट्रुमेंटल संगीत जनरेट करता है.
- सुरक्षा: प्रॉम्प्ट की जांच, सुरक्षा फ़िल्टर करते हैं. फ़िल्टर को ट्रिगर करने वाले प्रॉम्प्ट को अनदेखा कर दिया जाएगा. ऐसे मामले में, आउटपुट के `filtered_prompt` फ़ील्ड में इसकी वजह बताई जाएगी.
- वॉटरमार्किंग: आउटपुट ऑडियो में हमेशा वॉटरमार्क लगाया जाता है, ताकि उसकी पहचान की जा सके. ऐसा [ज़िम्मेदारी के साथ एआई का इस्तेमाल करने](https://ai.google/responsibility/principles/?hl=hi) से जुड़े हमारे सिद्धांतों के तहत किया जाता है.

## आगे क्या करना है

- [Lyria 3.5](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi) की मदद से पूरे गाने और वोकल ट्रैक जनरेट करें,
- संगीत के बजाय, [टीटीएस मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) का इस्तेमाल करके, एक से ज़्यादा स्पीकर की आवाज़ में बातचीत जनरेट करने का तरीका जानें,
- [इमेज](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi) या [वीडियो](https://ai.google.dev/gemini-api/docs/video?hl=hi) जनरेट करने का तरीका जानें,
- संगीत या ऑडियो जनरेट करने के बजाय, जानें कि Gemini [ऑडियो फ़ाइलों को कैसे समझ सकता है](https://ai.google.dev/gemini-api/docs/audio?hl=hi),
- [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=hi) का इस्तेमाल करके, Gemini के साथ रीयल-टाइम में बातचीत करें.

कोड के ज़्यादा उदाहरणों और ट्यूटोरियल के लिए, [कुकिंग बुक](https://github.com/google-gemini/cookbook) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-18 (UTC) को अपडेट किया गया."],[],[]]
