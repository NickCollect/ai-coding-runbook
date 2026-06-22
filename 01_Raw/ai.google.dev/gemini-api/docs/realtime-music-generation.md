---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=hi
fetched_at: 2026-06-22T06:32:49.145695+00:00
title: "Lyria RealTime \u0915\u093e \u0907\u0938\u094d\u0924\u0947\u092e\u093e\u0932 \u0915\u0930\u0915\u0947, \u0930\u0940\u092f\u0932-\u091f\u093e\u0907\u092e \u092e\u0947\u0902 \u0938\u0902\u0917\u0940\u0924 \u091c\u0928\u0930\u0947\u091f \u0915\u0930\u0928\u093e \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini की Deep Research की सुविधा](https://ai.google.dev/gemini-api/docs/deep-research?hl=hi) अब झलक के तौर पर उपलब्ध है. इसमें साथ मिलकर प्लान बनाने, विज़ुअलाइज़ेशन, एमसीपी के साथ काम करने की सुविधा वगैरह शामिल है.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Lyria RealTime का इस्तेमाल करके, रीयल-टाइम में संगीत जनरेट करना

Gemini API,
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=hi) का इस्तेमाल करके, रीयल-टाइम में स्ट्रीमिंग के ज़रिए संगीत
जनरेट करने वाले सबसे नए मॉडल का ऐक्सेस देता है. इससे डेवलपर ऐसे ऐप्लिकेशन बना सकते हैं जिनमें उपयोगकर्ता इंटरैक्टिव तरीके से, लगातार इंस्ट्रुमेंटल म्यूज़िक बना सकते हैं और उसे कंट्रोल कर सकते हैं.

Lyria RealTime की मदद से संगीत जनरेट करने के लिए, लगातार, दोनों दिशाओं में,
कम-लेटेंसी वाला स्ट्रीमिंग कनेक्शन इस्तेमाल किया जाता है. इसके लिए,
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) का इस्तेमाल किया जाता है.

Lyria RealTime का इस्तेमाल करके क्या बनाया जा सकता है, यह जानने के लिए, AI Studio
पर इसे आज़माएं. इसके लिए, [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=hi) या
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=hi) ऐप्लिकेशन का इस्तेमाल करें.

## संगीत जनरेट करना और उसे कंट्रोल करना

Lyria RealTime, [Live API](https://ai.google.dev/gemini-api/docs/live?hl=hi)
की तरह काम करता है. यह मॉडल के साथ रीयल-टाइम में कम्यूनिकेशन बनाए रखने के लिए, Websockets का इस्तेमाल करता है.

यहां दिए गए कोड से पता चलता है कि संगीत कैसे जनरेट किया जाता है:

### Python

इस उदाहरण में, `client.aio.live.music.connect()` का इस्तेमाल करके, Lyria RealTime सेशन शुरू किया जाता है. इसके बाद, `session.set_weighted_prompts()` की मदद से शुरुआती प्रॉम्प्ट भेजा जाता है. साथ ही, `session.set_music_generation_config` का इस्तेमाल करके, शुरुआती कॉन्फ़िगरेशन भेजा जाता है. इसके बाद, `session.play()` का इस्तेमाल करके, संगीत जनरेट करना शुरू किया जाता है. साथ ही, `receive_audio()` को सेट अप किया जाता है, ताकि यह मिलने वाले ऑडियो चंक को प्रोसेस कर सके.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

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

इस उदाहरण में, `client.live.music.connect()` का इस्तेमाल करके, Lyria RealTime सेशन शुरू किया जाता है. इसके बाद, `session.setWeightedPrompts()` की मदद से शुरुआती प्रॉम्प्ट भेजा जाता है. साथ ही, `session.setMusicGenerationConfig` का इस्तेमाल करके, शुरुआती कॉन्फ़िगरेशन भेजा जाता है. इसके बाद, `session.play()` का इस्तेमाल करके, संगीत जनरेट करना शुरू किया जाता है. साथ ही, `onMessage` कॉलबैक को सेट अप किया जाता है, ताकि यह मिलने वाले ऑडियो चंक को प्रोसेस कर सके.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
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

इसके बाद, सेशन शुरू करने, रोकने, बंद करने या रीसेट करने के लिए, `session.play()`, `session.pause()`, `session.stop()` और `session.reset_context()` का इस्तेमाल किया जा सकता है.

## रीयल-टाइम में संगीत को कंट्रोल करना

प्रॉम्प्ट भेजकर और जनरेशन पैरामीटर को रीयल-टाइम में अपडेट करके, रीयल-टाइम में संगीत जनरेट करने की सुविधा को कंट्रोल किया जा सकता है.

### Lyria RealTime के लिए प्रॉम्प्ट

स्ट्रीम चालू रहने के दौरान, जनरेट किए गए संगीत में बदलाव करने के लिए, किसी भी समय नए `WeightedPrompt` मैसेज भेजे जा सकते हैं. मॉडल, नए इनपुट के आधार पर आसानी से ट्रांज़िशन करेगा.

प्रॉम्प्ट, सही फ़ॉर्मैट में होने चाहिए. इनमें `text` (असल प्रॉम्प्ट) और `weight` शामिल होना चाहिए. `weight` के लिए, `0` के अलावा कोई भी वैल्यू इस्तेमाल की जा सकती है. आम तौर पर, `1.0` से शुरुआत करना बेहतर होता है.

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
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

ध्यान दें कि प्रॉम्प्ट में अचानक बदलाव करने पर, मॉडल के ट्रांज़िशन थोड़े अचानक हो सकते हैं. इसलिए, मॉडल को इंटरमीडिएट वेट वैल्यू भेजकर, किसी तरह का क्रॉस-फ़ेडिंग लागू करने का सुझाव दिया जाता है.

### कॉन्फ़िगरेशन अपडेट करना

रीयल-टाइम में संगीत जनरेट करने के पैरामीटर अपडेट करके, संगीत जनरेट करने की सुविधा को कंट्रोल किया जा सकता है. सिर्फ़ एक पैरामीटर अपडेट नहीं किया जा सकता. आपको पूरा कॉन्फ़िगरेशन सेट करना होगा. ऐसा न करने पर, अन्य फ़ील्ड अपनी डिफ़ॉल्ट वैल्यू पर रीसेट हो जाएंगे.

बीपीएम या स्केल अपडेट करने से, मॉडल में बड़ा बदलाव होता है. इसलिए, आपको इसे `reset_context()` का इस्तेमाल करके, अपना कॉन्टेक्स्ट रीसेट करने के लिए भी कहना होगा, ताकि यह नए कॉन्फ़िगरेशन को ध्यान में रख सके. इससे स्ट्रीम बंद नहीं होगी, लेकिन यह एक मुश्किल ट्रांज़िशन होगा. आपको अन्य पैरामीटर के लिए ऐसा करने की ज़रूरत नहीं है.

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

## Lyria RealTime के लिए प्रॉम्प्ट गाइड

यहां उन प्रॉम्प्ट की सूची दी गई है जिनका इस्तेमाल, Lyria RealTime के लिए प्रॉम्प्ट के तौर पर किया जा सकता है. यह सूची पूरी नहीं है:

- Instruments: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Music Genre: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Mood/Description: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

ये सिर्फ़ कुछ उदाहरण हैं. Lyria RealTime, इससे कहीं ज़्यादा काम कर सकता है. अपने प्रॉम्प्ट के साथ एक्सपेरिमेंट करें!

## सबसे सही तरीके

- क्लाइंट ऐप्लिकेशन में, ऑडियो बफ़रिंग की मज़बूत सुविधा लागू होनी चाहिए, ताकि प्लेबैक आसानी से हो सके. इससे नेटवर्क जिटर और जनरेशन लेटेंसी में होने वाले मामूली बदलावों को ध्यान में रखा जा सकता है.
- असरदार प्रॉम्प्ट:
  - ब्यौरा दें. मूड, शैली, और इंस्ट्रुमेंटेशन के बारे में बताने वाले विशेषणों का इस्तेमाल करें.
  - धीरे-धीरे बदलाव करें और धीरे-धीरे कंट्रोल करें. प्रॉम्प्ट को पूरी तरह से बदलने के बजाय, संगीत को ज़्यादा आसानी से बदलने के लिए, एलिमेंट जोड़ें या उनमें बदलाव करें.
  - नए प्रॉम्प्ट का, मौजूदा जनरेशन पर कितना असर पड़ता है, यह तय करने के लिए, `WeightedPrompt` पर वेट के साथ एक्सपेरिमेंट करें.

## तकनीकी जानकारी

इस सेक्शन में, Lyria RealTime की मदद से संगीत जनरेट करने की सुविधा का इस्तेमाल करने के बारे में जानकारी दी गई है.

### विशेषताएं

- आउटपुट फ़ॉर्मैट: Raw 16-bit PCM Audio
- सैंपल रेट: 48 किलोहर्ट्ज़
- चैनल: 2 (स्टीरियो)

### कंट्रोल

मैसेज भेजकर, रीयल-टाइम में संगीत जनरेट करने की सुविधा को कंट्रोल किया जा सकता है. इन मैसेज में ये शामिल हो सकते हैं:

- `WeightedPrompt`: यह एक टेक्स्ट स्ट्रिंग है, जिसमें संगीत के आइडिया, शैली, इंस्ट्रुमेंट, मूड या खासियत के बारे में बताया जाता है. एक से ज़्यादा प्रॉम्प्ट दिए जा सकते हैं, ताकि अलग-अलग तरह के संगीत को मिक्स किया जा सके. Lyria RealTime के लिए सबसे सही प्रॉम्प्ट देने के तरीके के बारे में ज़्यादा जानकारी के लिए, [ऊपर](https://ai.google.dev/gemini-api/docs/:?hl=hi#steer-music) देखें.
- `MusicGenerationConfig`: यह संगीत जनरेट करने की प्रोसेस का कॉन्फ़िगरेशन है. इससे आउटपुट ऑडियो की विशेषताओं पर असर पड़ता है.). पैरामीटर में ये शामिल हैं:
  - `guidance`: (फ़्लोट) रेंज: `[0.0, 6.0]`. डिफ़ॉल्ट: `4.0`.
    इससे यह कंट्रोल किया जाता है कि मॉडल, प्रॉम्प्ट को कितनी सख्ती से फ़ॉलो करता है. ज़्यादा गाइडेंस होने पर, प्रॉम्प्ट को बेहतर तरीके से फ़ॉलो किया जाता है. हालांकि, इससे ट्रांज़िशन ज़्यादा अचानक होते हैं.
  - `bpm`: (int) रेंज: `[60, 200]`.
    इससे जनरेट किए गए संगीत के लिए, बीट पर मिनट सेट किए जाते हैं. मॉडल को नए बीपीएम को ध्यान में रखने के लिए, आपको कॉन्टेक्स्ट को रोकना/चलाना या रीसेट करना होगा.
  - `density`: (फ़्लोट) रेंज: `[0.0, 1.0]`.
    इससे म्यूज़िकल नोट/साउंड की डेंसिटी कंट्रोल की जाती है. कम वैल्यू से, कम म्यूज़िक नोट वाला संगीत बनता है. वहीं, ज़्यादा वैल्यू से "ज़्यादा" म्यूज़िक नोट वाला संगीत बनता है.
  - `brightness`: (फ़्लोट) रेंज: `[0.0, 1.0]`.
    इससे टोनल क्वालिटी अडजस्ट की जाती है. ज़्यादा वैल्यू से "ब्राइटर" साउंड वाला ऑडियो बनता है. आम तौर पर, इससे ज़्यादा फ़्रीक्वेंसी पर ज़ोर दिया जाता है.
  - `scale`: (Enum) इससे जनरेशन के लिए म्यूज़िकल स्केल (की और मोड) सेट किया जाता है. एसडीके से मिली
    [`Scale` enum वैल्यू](#scale-enum) का इस्तेमाल करें. मॉडल को नए स्केल को ध्यान में रखने के लिए, आपको कॉन्टेक्स्ट को रोकना/चलाना या रीसेट करना होगा.
  - `mute_bass`: (bool) डिफ़ॉल्ट: `False`.
    इससे यह कंट्रोल किया जाता है कि मॉडल, आउटपुट के बास को कम करता है या नहीं.
  - `mute_drums`: (bool) डिफ़ॉल्ट: `False`.
    इससे यह कंट्रोल किया जाता है कि मॉडल, आउटपुट के ड्रम को कम करता है या नहीं.
  - `only_bass_and_drums`: (bool) डिफ़ॉल्ट: `False`.
    मॉडल को सिर्फ़ बास और ड्रम आउटपुट करने के लिए कंट्रोल करें.
  - `music_generation_mode`: (Enum) इससे मॉडल को यह पता चलता है कि उसे संगीत की `QUALITY` (डिफ़ॉल्ट वैल्यू) या `DIVERSITY` पर फ़ोकस करना चाहिए. इसे `VOCALIZATION` पर भी सेट किया जा सकता है, ताकि मॉडल, वोकलाइज़ेशन को दूसरे इंस्ट्रुमेंट के तौर पर जनरेट कर सके. इसके लिए, उन्हें नए प्रॉम्प्ट के तौर पर जोड़ा जा सकता है.
- `PlaybackControl`: यह प्लेबैक के पहलुओं को कंट्रोल करने के लिए कमांड है. जैसे, कॉन्टेक्स्ट को चलाना, रोकना, बंद करना या रीसेट करना.

`bpm`, `density`, `brightness` और `scale` के लिए, अगर कोई वैल्यू नहीं दी जाती है, तो मॉडल, आपके शुरुआती प्रॉम्प्ट के हिसाब से सबसे सही वैल्यू तय करेगा.

`MusicGenerationConfig` में, क्लासिकल पैरामीटर भी पसंद के मुताबिक बनाए जा सकते हैं. जैसे, `temperature` (0.0 से 3.0, डिफ़ॉल्ट 1.1), `top_k` (1 से 1000, डिफ़ॉल्ट 40) और `seed` (0 से 2,147,483,647, डिफ़ॉल्ट रूप से रैंडम तरीके से चुना जाता है).

#### स्केल enum वैल्यू

यहां स्केल की सभी वैल्यू दी गई हैं जिन्हें मॉडल स्वीकार कर सकता है:

| Enum वैल्यू | स्केल / की |
| --- | --- |
| `C_MAJOR_A_MINOR` | सी मेजर / ए माइनर |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | डी फ़्लैट मेजर / बी फ़्लैट माइनर |
| `D_MAJOR_B_MINOR` | डी मेजर / बी माइनर |
| `E_FLAT_MAJOR_C_MINOR` | ई फ़्लैट मेजर / सी माइनर |
| `E_MAJOR_D_FLAT_MINOR` | ई मेजर / सी शार्प/डी फ़्लैट माइनर |
| `F_MAJOR_D_MINOR` | एफ़ मेजर / डी माइनर |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | जी फ़्लैट मेजर / ई फ़्लैट माइनर |
| `G_MAJOR_E_MINOR` | जी मेजर / ई माइनर |
| `A_FLAT_MAJOR_F_MINOR` | ए फ़्लैट मेजर / एफ़ माइनर |
| `A_MAJOR_G_FLAT_MINOR` | ए मेजर / एफ़ शार्प/जी फ़्लैट माइनर |
| `B_FLAT_MAJOR_G_MINOR` | बी फ़्लैट मेजर / जी माइनर |
| `B_MAJOR_A_FLAT_MINOR` | बी मेजर / जी शार्प/ए फ़्लैट माइनर |
| `SCALE_UNSPECIFIED` | डिफ़ॉल्ट / मॉडल तय करता है |

मॉडल, बजाए जाने वाले नोट को गाइड कर सकता है. हालांकि, यह रिलेटिव की के बीच अंतर नहीं करता. इसलिए, हर enum, रिलेटिव मेजर और माइनर, दोनों से मेल खाता है. उदाहरण के लिए, `C_MAJOR_A_MINOR` पियानो की सभी सफ़ेद की से मेल खाएगा. वहीं, `F_MAJOR_D_MINOR`, बी फ़्लैट को छोड़कर सभी सफ़ेद की से मेल खाएगा.

### सीमाएं

- सिर्फ़ इंस्ट्रुमेंटल: मॉडल, सिर्फ़ इंस्ट्रुमेंटल म्यूज़िक जनरेट करता है.
- सुरक्षा: प्रॉम्प्ट की जांच, सुरक्षा फ़िल्टर से की जाती है. फ़िल्टर को ट्रिगर करने वाले प्रॉम्प्ट को अनदेखा कर दिया जाएगा. ऐसे में, आउटपुट के `filtered_prompt` फ़ील्ड में इसकी वजह लिखी जाएगी.
- [वॉटरमार्किंग: ज़िम्मेदार एआई के सिद्धांतों के मुताबिक, आउटपुट ऑडियो की पहचान के लिए, उसमें हमेशा वॉटरमार्क जोड़ा जाता है.](https://ai.google/responsibility/principles/?hl=hi)

## आगे क्या करना है

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=hi) की मदद से, पूरे गाने और वोकल ट्रैक जनरेट करना,
- [म्यूज़िक के बजाय,
  टीटीएस मॉडल](https://ai.google.dev/gemini-api/docs/speech-generation?hl=hi) का इस्तेमाल करके, एक से ज़्यादा लोगों की बातचीत जनरेट करने का तरीका जानना,
- [[इमेज या वीडियो जनरेट करने का तरीका जानना,](https://ai.google.dev/gemini-api/docs/image-generation?hl=hi)](https://ai.google.dev/gemini-api/docs/video?hl=hi)
- म्यूज़िक या ऑडियो जनरेट करने के बजाय, यह जानना कि Gemini,
  [ऑडियो फ़ाइलें कैसे समझ सकता है,](https://ai.google.dev/gemini-api/docs/audio?hl=hi)
- [Live API का इस्तेमाल करके, Gemini के साथ रीयल-टाइम में बातचीत करना.](https://ai.google.dev/gemini-api/docs/live?hl=hi)

ज़्यादा
कोड उदाहरणों और ट्यूटोरियल के लिए, [कुकबुक](https://github.com/google-gemini/cookbook) देखें.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-19 (UTC) को अपडेट किया गया."],[],[]]
