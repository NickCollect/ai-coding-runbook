---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr
fetched_at: 2026-09-28T06:29:37.537931+00:00
title: "R\u00e9plication de la voix \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Réplication de la voix

La réplication de voix vous permet de répliquer les caractéristiques vocales d'un locuteur à partir d'un court extrait audio à l'aide du point de terminaison Voices de l'API Gemini (`POST /v1beta/voices`). La réplication de voix est compatible avec [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`).

Le moyen le plus rapide de répliquer une voix, de vérifier le consentement et d'écouter une voix répliquée est l'expérience interactive **Réplication de voix** dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr). Vous pouvez enregistrer ou importer des extraits de référence et de consentement directement dans le navigateur, prévisualiser la voix et copier l'ID `voice_...` obtenu directement dans le code de votre application.

[Essayer dans Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr)

![Workflow de réplication vocale](https://ai.google.dev/static/gemini-api/docs/images/voice-replication-overview.svg?hl=fr)

## Modes de stockage avec état et sans état

La réplication vocale est compatible avec deux modes de stockage lors de l'appel de `voices.create` (`POST /v1beta/voices`), avec le stockage avec état activé par défaut :

- **Stockage avec état (`store=True`, valeur par défaut recommandée)** : Google stocke votre profil vocal validé dans votre projet et renvoie un `voice_id` léger et persistant (`replicated_voice.id`, tel que `voice_abc123...`). Vous pouvez transmettre ce `voice_id` dans les requêtes et le gérer avec `voices.list()`, `voices.get()` et `voices.delete()`.
- **Clés gérées par le client sans état (`store=False`, facultatif)** : pour les charges de travail nécessitant une persistance côté serveur nulle des profils vocaux biométriques, définissez `store=False`. L'API renvoie un `voice_key` chiffré et autonome (`replicated_voice.key`, commençant par `voicekey_...`) que votre application stocke en local et transmet directement dans les requêtes de synthèse.

| Mode de stockage | Identifiant | Limite de projets | Rétention (TTL) |
| --- | --- | --- | --- |
| **Voix avec état** (`store=True`) | `voice_...` | **200 voix par projet** (partagées entre les voix suggérées et répliquées) | **1 an** |
| **Clés vocales sans état** (`store=False`) | `voicekey_...` | Géré par le client | **7 jours** |

## Exigences concernant le contenu audio et le consentement

Chaque demande de réplication `CreateVoice` nécessite deux enregistrements audio de vraies personnes **du même locuteur adulte** (format WAV mono 16 bits à 24 kHz recommandé) :

1. **Audio de référence (`source_audio`)** : extrait de 10 à 30 secondes de parole claire et naturelle de la personne dont vous souhaitez répliquer la voix.
2. **Enregistrement audio du consentement (`consent_audio`)** : enregistrement de la même personne récitant clairement la déclaration de consentement obligatoire dans l'une des [langues acceptées](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr#consent-phrases-by-language) (par exemple, en français) :
   > *"Je suis le propriétaire de cette voix et j'autorise Google à l'utiliser pour créer un modèle de voix synthétique."*

## Créer une voix répliquée (état par défaut)

Utilisez le SDK GenAI de Google (`google-genai` 2.25.0 ou version ultérieure / `@google/genai` 2.24.0 ou version ultérieure) ou l'API REST avec `store=True` pour créer et enregistrer un profil vocal répliqué dans votre projet :

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

## Synthétiser la voix avec votre voix répliquée

Transmettez le `id` renvoyé (`voice_...`) dans `voiceConfig.voice` lorsque vous appelez `generateContent` :

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

## Gérer les voix répliquées stockées

Lorsque vous créez des voix répliquées avec `store=True`, vous pouvez les lister, les filtrer, les inspecter et les supprimer à l'aide de l'API Voices (consultez [Bibliothèque vocale étendue et filtrage](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#voice-library) pour connaître tous les paramètres de filtrage) :

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

## Option : Clés vocales sans état gérées par le client (`store=False`)

Si votre application ne nécessite aucune persistance côté serveur des profils vocaux, définissez `store=False` lors de la création de la voix répliquée. L'API renvoie un `voice_key` chiffré (`replicated_voice.key`, commençant par `voicekey_...`) que vous stockez côté client et transmettez directement dans `voiceConfig.voice` :

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

## Expressions de consentement acceptées par langue

L'enregistrement audio du consentement doit énoncer clairement la déclaration exacte dans l'une des 30 langues disponibles :

| Langue | Paramètres régionaux (`lang_id`) | Déclaration de consentement mot à mot |
| --- | --- | --- |
| **Arabe** | `ar-XA` | أنا مالك هذا الصوت وأوافق على أن تستخدم Google هذا الصوت لإنشاء نموذج صوتي اصطناعي. |
| **Bengali** | `bn-IN` | আমি এই ভয়েসের মালিক এবং আমি একটি সিন্থেটিক ভয়েস মডেল তৈরি করতে এই ভয়েস ব্যবহার করে Google-এর সাথে সম্মতি দিচ্ছি। |
| **Chinois (simplifié)** | `zh-CN` | 我是此声音的拥有者并授权谷歌使用此声音创建语音合成模型 |
| **Néerlandais** | `nl-NL` | Ik ben de eigenaar van deze stem en ik geef Google toestemming om deze stem te gebruiken om een synthetisch stemmodel te maken. |
| **Français (France)** | `en-US` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **English (UK)** | `en-GB` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **Anglais (Inde)** | `en-IN` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **Anglais (Australie)** | `en-AU` | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model. |
| **French (France)** | `fr-FR` | Je suis le propriétaire de cette voix et j'autorise Google à l'utiliser pour créer un modèle de voix synthétique. |
| **Français (Canada)** | `fr-CA` | Je suis le propriétaire de cette voix et j'autorise Google à l'utiliser pour créer un modèle de voix synthétique. |
| **Allemand** | `de-DE` | Ich bin der Eigentümer dieser Stimme und bin damit einverstanden, dass Google diese Stimme zur Erstellung eines synthetischen Stimmmodells verwendet. |
| **Gujarati** | `gu-IN` | હું આ વોઈસનો માલિક છું અને સિન્થેટિક વોઈસ મોડલ બનાવવા માટે આ વોઈસનો ઉપયોગ કરીને google ને હું સંમતિ આપું છું |
| **Hindi** | `hi-IN` | मैं इस आवाज का मालिक हूं और मैं सिंथेटिक आवाज मॉडल बनाने के लिए Google को इस आवाज का उपयोग करने की सहमति देता हूं |
| **Indonésien** | `id-ID` | Saya pemilik suara ini dan saya menyetujui Google menggunakan suara ini untuk membuat model suara sintetis. |
| **Italien** | `it-IT` | Sono il proprietario di questa voce e acconsento che Google la utilizzi per creare un modello di voce sintetica. |
| **Japonais** | `ja-JP` | 私はこの音声の所有者であり、Googleがこの音声を使用して音声合成モデルを作成することを承認します。 |
| **Kannada** | `kn-IN` | ನಾನು ಈ ಧ್ವನಿಯ ಮಾಲಿಕ ಮತ್ತು ಸಂಶ್ಲೇಷಿತ ಧ್ವನಿ ಮಾದರಿಯನ್ನು ರಚಿಸಲು ಈ ಧ್ವನಿಯನ್ನು ಬಳಸಿಕೊಂಡುಗೂಗಲ್ ಗೆ ನಾನು ಸಮ್ಮತಿಸುತ್ತೇನೆ. |
| **Coréen** | `ko-KR` | 나는 이 음성의 소유자이며 구글이 이 음성을 사용하여 음성 합성 모델을 생성할 것을 허용합니다. |
| **Malayalam** | `ml-IN` | ഈ ശബ്ദത്തിന്റെ ഉടമ ഞാനാണ്, ഒരു സിന്തറ്റിക് വോയ്സ് മോഡൽ സൃഷ്ടിക്കാൻ ഈ ശബ്ദം ഉപയോഗിക്കുന്നതിന് ഞാൻ Google-ന് സമ്മതം നൽകുന്നു. |
| **Marathi** | `mr-IN` | मी या आवाजाचा मालक आहे आणि सिंथेटिक व्हॉइस मॉडेल तयार करण्यासाठी हा आवाज वापरण्यासाठी मी Google ला संमती देतो |
| **Polonais** | `pl-PL` | Jestem właścicielem tego głosu i wyrażam zgodę na wykorzystanie go przez Google w celu utworzenia syntetycznego modelu głosu. |
| **Portugais (Brésil)** | `pt-BR` | Eu sou o proprietário desta voz e autorizo o Google a usá-la para criar um modelo de voz sintética. |
| **Russe** | `ru-RU` | Я являюсь владельцем этого голоса и даю согласие Google на использование этого голоса для создания модели синтетического голоса. |
| **Spanish (Spain)** | `es-ES` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **Spanish (US)** | `es-US` | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética. |
| **Tamoul** | `ta-IN` | நான் இந்த குரலின் உரிமையாளர் மற்றும் செயற்கை குரல் மாதிரியை உருவாக்க இந்த குரலை பயன்படுத்த குகல்க்கு நான் ஒப்புக்கொள்கிறேன். |
| **Télougou** | `te-IN` | నేను ఈ వాయిస్ యజమానిని మరియు సింతటిక్ వాయిస్ మోడల్ ని రూపొందించడానికి ఈ వాయిస్ ని ఉపయోగించడానికి googleకి నేను సమ్మతిస్తున్నాను. |
| **Thaï** | `th-TH` | ฉันเป็นเจ้าของเสียงนี้ และฉันยินยอมให้ Google ใช้เสียงนี้เพื่อสร้างแบบจำลองเสียงสังเคราะห์ |
| **Turc** | `tr-TR` | Bu sesin sahibi benim ve Google'ın bu sesi kullanarak sentetik bir ses modeli oluşturmasına izin veriyorum. |
| **Vietnamien** | `vi-VN` | Tôi là chủ sở hữu giọng nói này và tôi đồng ý cho Google sử dụng giọng nói này để tạo mô hình giọng nói tổng hợp. |

## Bonnes pratiques pour enregistrer l'audio de référence

- **Enregistrez-vous dans un environnement calme** : limitez l'écho de la pièce, le bruit de fond, la musique et les voix qui se chevauchent.
- **Respectez les conditions d'enregistrement** : enregistrez `source_audio` et `consent_audio` avec le même micro et dans le même environnement acoustique pour que la vérification du locuteur réussisse à chaque fois.
- **Convertir au format WAV mono 24 kHz** : pour de meilleurs résultats, rééchantillonnez l'audio d'entrée au format WAV PCM mono 16 bits 24 kHz avant l'encodage.

## Étape suivante

- Découvrez comment créer des personas personnalisés à partir de descriptions textuelles dans [Conception vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr).
- Découvrez la mise en forme au niveau du tour, les balises intégrées et les dialogues à plusieurs locuteurs dans le [guide Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
