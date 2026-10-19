---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=he
fetched_at: 2026-10-19T05:37:54.954491+00:00
title: "\u05e9\u05db\u05e4\u05d5\u05dc \u05e7\u05d5\u05dc\u05d9 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon זמין עכשיו. [רוצים לנסות?](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=he)

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=he)

שליחת משוב

# שכפול קולי

רפליקציה של קולות מאפשרת לשכפל את המאפיינים הקוליים של דובר מדגימת אודיו קצרה באמצעות נקודת הקצה Voices של Gemini API ‏ (`POST /v1beta/voices`). רפליקציה של קולות נתמכת גם ב-[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=he) ‏(`gemini-3.8-flash-tts`) וגם ב-[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=he) ‏(`gemini-3.8-flash-lite-tts`).

הדרך הכי מהירה לשכפל קול, לאמת את ההסכמה ולבדוק את הקול המשוכפל היא באמצעות חוויית **שכפול הקול** האינטראקטיבית ב-[Google AI Studio](https://aistudio.google.com/generate-speech?hl=he). אתם יכולים להקליט או להעלות קטעי אודיו של הפניה והסכמה ישירות בדפדפן, לראות תצוגה מקדימה של הקול ולהעתיק את מזהה הקול שנוצר `voice_...` ישירות לקוד האפליקציה.

[לניסיון ב-Google AI Studio](https://aistudio.google.com/generate-speech?hl=he)

![תהליך העבודה של רפליקציה של קולות](https://ai.google.dev/static/gemini-api/docs/images/voice-replication-overview.svg?hl=he)

## מצבי אחסון עם שמירת מצב לעומת מצבי אחסון ללא שמירת מצב

רפליקציה של קולות תומכת בשני מצבי אחסון כשמתקשרים אל `voices.create` (`POST /v1beta/voices`), ואחסון עם שמירת מצב מופעל כברירת מחדל:

- **אחסון עם שמירת מצב (`store=True`, מומלץ כברירת מחדל):** Google מאחסנת את פרופיל הקול המאומת בפרויקט ומחזירה `voice_id` קל משקל ומתמשך (`replicated_voice.id`, כמו `voice_abc123...`). אפשר להעביר את ה`voice_id` הזה בין בקשות ולנהל אותו באמצעות `voices.list()`,‏ `voices.get()` ו-`voices.delete()`.
- **מפתחות ללא שמירת מצב שמנוהלים על ידי הלקוח (`store=False`, אופציונלי):** כדי להגדיר עומסי עבודה שבהם לא נדרשת התמדה בצד השרת של פרופילים ביומטריים של קול, מגדירים את `store=False`. ה-API מחזיר `voice_key`מוצפן (`replicated_voice.key`, החל מ-`voicekey_...`) שהאפליקציה שלכם מאחסנת באופן מקומי ומעבירה ישירות בבקשות סינתזה.

| מצב אחסון | מזהה | מגבלת הפרויקטים | שמירה (TTL) |
| --- | --- | --- | --- |
| **קולות עם מצב** (`store=True`) | `voice_...` | **200 קולות לכל פרויקט** (משותפים בין קולות שנוצרו מהנחיות וקולות ששוכפלו) | **שנה אחת** |
| **מקשי קול ללא מצב** (`store=False`) | `voicekey_...` | בניהול של לקוח | **7 ימים** |

## דרישות לגבי אודיו והדרישות לקבלת הסכמה

כל בקשת שכפול`CreateVoice` צריכה לכלול שתי הקלטות אודיו של בני אדם אמיתיים
מ**אותו דובר בוגר** (מומלץ להשתמש ב-WAV במונו 24kHz 16-bit):

1. **אודיו להשוואה (`source_audio`):** קליפ באורך 10-30 שניות של דיבור טבעי ונקי של הדובר שאת הקול שלו רוצים לשכפל.
2. **אודיו להסכמה (`consent_audio`):** הקלטה של אותו דובר שאומר בבירור את הצהרת ההסכמה הנדרשת באחת מ[השפות הנתמכות](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=he#consent-phrases-by-language) (לדוגמה, בעברית):
   > *"אני הבעלים של הקול הזה ואני מסכים ש-Google תשתמש בקול הזה כדי ליצור מודל קול סינתטי".*

## יצירת קול משוכפל (ברירת מחדל עם שמירת מצב)

משתמשים ב-Google GenAI SDK ‏ (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) או ב-API בארכיטקטורת REST עם `store=True` כדי ליצור ולשמור פרופיל קולי משוכפל בפרויקט:

### Python

```
import base64
from google import genai

client = genai.Client()

with open("reference_speaker.wav", "rb") as f:
    source_b64 = base64.b64encode(f.read()).decode("utf-8")

with open("speaker_consent.wav", "rb") as f:
    consent_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create a persistent replicated voice (store=True)
replicated_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "replicated",
        "display_name": "Custom Replicated Speaker",
        "replicated": {
            "source_audio": {
                "mime_type": "audio/wav",
                "data": source_b64,
            },
            "consent_audio": {
                "mime_type": "audio/wav",
                "data": consent_b64,
            },
        },
    },
)

print(f"Created voice ID: {replicated_voice.id}")
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const sourceB64 = fs.readFileSync("reference_speaker.wav").toString("base64");
const consentB64 = fs.readFileSync("speaker_consent.wav").toString("base64");

// Create a persistent replicated voice (store: true)
const replicatedVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "replicated",
    display_name: "Custom Replicated Speaker",
    replicated: {
      source_audio: {
        mime_type: "audio/wav",
        data: sourceB64,
      },
      consent_audio: {
        mime_type: "audio/wav",
        data: consentB64,
      },
    },
  },
});

console.log(`Created voice ID: ${replicatedVoice.id}`);
```

### REST

```
SOURCE_B64=$(base64 -w 0 reference_speaker.wav)
CONSENT_B64=$(base64 -w 0 speaker_consent.wav)

curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{
    \"store\": true,
    \"voice\": {
      \"model\": \"gemini-3.8-flash-tts\",
      \"type\": \"replicated\",
      \"display_name\": \"Custom Replicated Speaker\",
      \"replicated\": {
        \"source_audio\": {
          \"mime_type\": \"audio/wav\",
          \"data\": \"$SOURCE_B64\"
        },
        \"consent_audio\": {
          \"mime_type\": \"audio/wav\",
          \"data\": \"$CONSENT_B64\"
        }
      }
    }
  }"
```

## סינתזת דיבור באמצעות העתק של הקול שלכם

מעבירים את הערך `id` (`voice_...`) שמוחזר ב-`voiceConfig.voice` כשמתקשרים אל `generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Hello! This audio was synthesized using a replicated"
                " speaker voice."
            ),
            "speech_metadata": {"style": "warm and conversational"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": replicated_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("replicated_speech.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Hello! This audio was synthesized using a replicated speaker voice.",
      speechMetadata: { style: "warm and conversational" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: replicatedVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("replicated_speech.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Hello! This audio was synthesized using a replicated speaker voice.",
        "speech_metadata": {
          "style": "warm and conversational"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_REPLICATED_VOICE_ID"
        }
      }
    }
  }'
```

## ניהול קולות משוכפלים מאוחסנים

כשיוצרים קולות משוכפלים באמצעות `store=True`, אפשר לראות אותם, לסנן אותם, לבדוק אותם ולמחוק אותם דרך Voices API (למידע על כל פרמטרי הסינון, אפשר לעיין במאמר [Extended Voice Library and filtering](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=he#voice-library)).

### Python

```
from google import genai

client = genai.Client()

# List stored replicated voices in your project
response = client.voices.list(type_=["replicated"])
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=replicated_voice.id)

# Delete a stored replicated voice
client.voices.delete(id=replicated_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored replicated voices in your project
const response = await ai.voices.list({ type: ["replicated"] });
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(replicatedVoice.id);

// Delete a stored replicated voice
await ai.voices.delete(replicatedVoice.id);
```

### REST

```
# List stored replicated voices in your project
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=replicated"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_REPLICATED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored replicated voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_REPLICATED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## אפשרות: מפתחות קוליים בניהול הלקוח ללא שמירת מצב (`store=False`)

אם האפליקציה שלכם לא יכולה לשמור פרופילים קוליים בצד השרת, צריך להגדיר את הערך `store=False` כשיוצרים את הקול המשוכפל. ה-API מחזיר מחרוזת מוצפנת של `voice_key` (`replicated_voice.key`, שמתחילה ב-`voicekey_...`) שאתם מאחסנים בצד הלקוח ומעבירים ישירות ב-`voiceConfig.voice`:

### Python

```
import base64
from google import genai

client = genai.Client()

with open("reference_speaker.wav", "rb") as f:
    source_b64 = base64.b64encode(f.read()).decode("utf-8")

with open("speaker_consent.wav", "rb") as f:
    consent_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create a stateless client-managed voice key (store=False)
replicated_voice = client.voices.create(
    store=False,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "replicated",
        "replicated": {
            "source_audio": {"mime_type": "audio/wav", "data": source_b64},
            "consent_audio": {"mime_type": "audio/wav", "data": consent_b64},
        },
    },
)

# Pass replicated_voice.key ("voicekey_...") directly in voice_config
response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Hello! This audio uses a stateless client-managed voice key.",
            "speech_metadata": {"style": "warm and conversational"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": replicated_voice.key}
        },
    },
)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const sourceB64 = fs.readFileSync("reference_speaker.wav").toString("base64");
const consentB64 = fs.readFileSync("speaker_consent.wav").toString("base64");

// Create a stateless client-managed voice key (store: false)
const replicatedVoice = await ai.voices.create({
  store: false,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "replicated",
    replicated: {
      source_audio: { mime_type: "audio/wav", data: sourceB64 },
      consent_audio: { mime_type: "audio/wav", data: consentB64 },
    },
  },
});

// Pass replicatedVoice.key ("voicekey_...") directly in voiceConfig
const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Hello! This audio uses a stateless client-managed voice key.",
      speechMetadata: { style: "warm and conversational" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: replicatedVoice.key },
    },
  },
});
```

### REST

```
SOURCE_B64=$(base64 -w 0 reference_speaker.wav)
CONSENT_B64=$(base64 -w 0 speaker_consent.wav)

curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{
    \"store\": false,
    \"voice\": {
      \"model\": \"gemini-3.8-flash-tts\",
      \"type\": \"replicated\",
      \"replicated\": {
        \"source_audio\": {\"mime_type\": \"audio/wav\", \"data\": \"$SOURCE_B64\"},
        \"consent_audio\": {\"mime_type\": \"audio/wav\", \"data\": \"$CONSENT_B64\"}
      }
    }
  }"
```

## ביטויי הסכמה נתמכים לפי שפה

האודיו להבעת הסכמה צריך לכלול הקראה ברורה של ההצהרה המדויקת באחד מ-30 הלוקאלים של השפות הנתמכות:

| שפה | לוקאל (`lang_id`) | הצהרת הסכמה מילולית |
| --- | --- | --- |
| **ערבית** | `ar-XA` | أنا مالك هذا الصوت وأوافق على أن تستخدم Google هذا الصوت لإنشاء نموذج صوتي اصطناعي. |
| **בנגאלית** | `bn-IN` | আমি এই ভয়েসের মালিক এবং আমি একটি সিন্থেটিক ভয়েস মডেল তৈরি করতে এই ভয়েস ব্যবহার করে Google-এর সাথে সম্মতি দিচ্ছি। |
| **סינית (פשוטה)** | `zh-CN` | 我拥有此声音并授权谷歌使用此声音创建语音合成模型 |
| **הולנדית** | `nl-NL` | Ik ben de eigenaar van deze stem en ik geef Google toestemming om deze stem te gebruiken om een synthetisch stemmodel te maken. |
| **אנגלית (ארה"ב)** | `en-US` | אני הבעלים של הקול הזה ואני מסכים/ה ש-Google תשתמש בקול הזה כדי ליצור מודל קול סינתטי. |
| **אנגלית (בריטניה)** | `en-GB` | אני הבעלים של הקול הזה ואני מסכים/ה ש-Google תשתמש בקול הזה כדי ליצור מודל קול סינתטי. |
| **אנגלית (הודו)** | `en-IN` | אני הבעלים של הקול הזה ואני מסכים/ה ש-Google תשתמש בקול הזה כדי ליצור מודל קול סינתטי. |
| **אנגלית (אוסטרליה)** | `en-AU` | אני הבעלים של הקול הזה ואני מסכים/ה ש-Google תשתמש בקול הזה כדי ליצור מודל קול סינתטי. |
| **צרפתית (צרפת)** | `fr-FR` | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique. |
| **צרפתית (קנדה)** | `fr-CA` | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique. |
| **גרמנית** | `de-DE` | Ich bin der Eigentümer dieser Stimme und bin damit einverstanden, dass Google diese Stimme zur Erstellung eines synthetischen Stimmmodells verwendet. |
| **גוג'ארטי** | `gu-IN` | હું આ વોઈસનો માલિક છું અને સિન્થેટિક વોઈસ મોડલ બનાવવા માટે આ વોઈસનો ઉપયોગ કરીને google ને હું સંમતિ આપું છું |
| **הינדית** | `hi-IN` | मैं इस आवाज का मालिक हूं और मैं सिंथेटिक आवाज मॉडल बनाने के लिए Google को इस आवाज का उपयोग करने की सहमति देता हूं |
| **אינדונזית** | `id-ID` | Saya pemilik suara ini dan saya menyetujui Google menggunakan suara ini untuk membuat model suara sintetis. |
| **איטלקית** | `it-IT` | Sono il proprietario di questa voce e acconsento che Google la utilizzi per creare un modello di voce sintetica. |
| **יפנית** | `ja-JP` | 私はこの音声の所有者であり、Googleがこの音声を使用して音声合成モデルを作成することを承認します。 |
| **קנאדה** | `kn-IN` | ನಾನು ಈ ಧ್ವನಿಯ ಮಾಲಿಕ ಮತ್ತು ಸಂಶ್ಲೇಷಿತ ಧ್ವನಿ ಮಾದರಿಯನ್ನು ರಚಿಸಲು ಈ ಧ್ವನಿಯನ್ನು ಬಳಸಿಕೊಂಡುಗೂಗಲ್ ಗೆ ನಾನು ಸಮ್ಮತಿಸುತ್ತೇನೆ. |
| **קוריאנית** | `ko-KR` | 나는 이 음성의 소유자이며 구글이 이 음성을 사용하여 음성 합성 모델을 생성할 것을 허용합니다. |
| **מלאיאלאם** | `ml-IN` | ഈ ശബ്ദത്തിന്റെ ഉടമ ഞാനാണ്, ഒരു സിന്തറ്റിക് വോയ്സ് മോഡൽ സൃഷ്ടിക്കാൻ ഈ ശബ്ദം ഉപയോഗിക്കുന്നതിന് ഞാൻ Google-ന് സമ്മതം നൽകുന്നു. |
| **מראטהית** | `mr-IN` | मी या आवाजाचा मालक आहे आणि सिंथेटिक व्हॉइस मॉडेल तयार करण्यासाठी हा आवाज वापरण्यासाठी मी Google ला संमती देतो |
| **פולנית** | `pl-PL` | Jestem właścicielem tego głosu i wyrażam zgodę na wykorzystanie go przez Google w celu utworzenia syntetycznego modelu głosu. |
| **פורטוגזית (ברזיל)** | `pt-BR` | Eu sou o proprietário desta voz e autorizo o Google a usá-la para criar um modelo de voz sintética. |
| **רוסית** | `ru-RU` | Я являюсь владельцем этого голоса и даю согласие Google на использование этого голоса для создания модели синтетического голоса. |
| **ספרדית (ספרד)** | `es-ES` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **ספרדית (ארה"ב)** | `es-US` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **טמילית** | `ta-IN` | நான் இந்த குரலின் உரிமையாளர் மற்றும் செயற்கை குரல் மாதிரியை உருவாக்க இந்த குரலை பயன்படுத்த குகல்க்கு நான் ஒப்புக்கொள்கிறேன். |
| **טלוגו** | `te-IN` | ‫I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **תאית** | `th-TH` | אני הבעלים של הקול הזה ואני מסכים ש-Google תשתמש בו כדי ליצור מודל של קול סינתטי. |
| **טורקית** | `tr-TR` | Bu sesin sahibi benim ve Google'ın bu sesi kullanarak sentetik bir ses modeli oluşturmasına izin veriyorum. |
| **וייטנאמית** | `vi-VN` | Tôi là chủ sở hữu giọng nói này và tôi đồng ý cho Google sử dụng giọng nói này để tạo mô hình giọng nói tổng hợp. |

## שיטות מומלצות להקלטת אודיו להשוואה

- **הקלטה בסביבה שקטה:** חשוב להפחית את ההד בחדר, רעשי הרקע, המוזיקה והקולות החופפים.
- **התאמה של תנאי ההקלטה:** מקליטים את `source_audio` ואת `consent_audio` באותו מיקרופון ובאותה סביבה אקוסטית, כדי שאימות הדובר יצליח באופן מהימן.
- **המרת קובץ ל-WAV מונו 24kHz:** כדי לקבל את התוצאות הטובות ביותר, מומלץ לבצע דגימה מחדש של קובץ האודיו לקובץ WAV מונו 24kHz PCM 16-bit לפני הקידוד.

## המאמרים הבאים

- [כך יוצרים פרסונות בהתאמה אישית מתיאורי טקסט](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=he).
- ב[מדריך להמרת טקסט לדיבור](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=he) אפשר לקרוא על עיצוב ברמת הפנייה, תגים מוטבעים ודיאלוג עם כמה דוברים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-24 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-24 (שעון UTC)."],[],[]]
