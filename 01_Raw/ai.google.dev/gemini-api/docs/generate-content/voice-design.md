---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=fr
fetched_at: 2026-10-05T06:38:49.892044+00:00
title: "Conception de la voix \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Conception de la voix

La conception de voix vous permet de créer une toute nouvelle personnalité vocale persistante à partir d'une description en langage naturel à l'aide du point de terminaison Voices de l'API Gemini (`POST /v1beta/voices`). Au lieu d'être limité aux voix prédéfinies ou à l'enregistrement d'un audio de référence, vous pouvez décrire l'âge, le timbre de voix, l'accent et le ton de base d'un personnage, et recevoir un ID `voice_...` réutilisable enregistré dans votre projet.

Le moyen le plus rapide de concevoir, d'essayer et d'itérer des voix personnalisées est d'utiliser le studio interactif **Voice Design** dans [Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr). Vous pouvez générer des personas personnalisés à partir de requêtes textuelles, les tester avec des exemples de scripts et copier l'ID `voice_...` obtenu directement dans le code de votre application.

[Essayer dans Google AI Studio](https://aistudio.google.com/generate-speech?hl=fr)

[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=fr) (`gemini-3.8-flash-tts`) et [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=fr) (`gemini-3.8-flash-lite-tts`) sont compatibles avec la conception de voix.

## Créer une voix conçue

Utilisez le SDK Google GenAI (`google-genai` 2.25.0 ou version ultérieure / `@google/genai` 2.24.0 ou version ultérieure) ou l'API REST pour créer une voix personnalisée à partir d'une description textuelle. Pour les voix `"prompted"`, `voices.create` (`CreateVoice`) et `voices.get` (`GetVoice`) renvoient un champ `sample_audio` en sortie uniquement (`mime_type: "audio/wav"`, `data` encodé en base64) pour que vous puissiez écouter immédiatement la voix générée :

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Fonctionnement de la conception vocale

1. **Créer une voix guidée** : appelez `voices.create` (`POST /v1beta/voices`) avec `type="prompted"` et `store=True`.
2. **Recevoir un aperçu permanent `voice_id` et `sample_audio`** : l'API génère l'identité vocale, la stocke dans votre projet et renvoie un ID permanent (par exemple, `voice_abc123...`) avec `sample_audio` (`mime_type: "audio/wav"`, `data` encodé en base64) contenant l'aperçu audio généré pour la voix.
3. **Synthétiser la parole** : transmettez `voice_id` dans `speechConfig.voiceConfig.voice` lorsque vous appelez `generateContent`.

## Synthétiser la voix avec la voix que vous avez conçue

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
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
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
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
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
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Gérer vos voix

Vous pouvez lister, filtrer, inspecter et supprimer vos voix stockées à tout moment à l'aide de l'API Voices (consultez [Bibliothèque de voix étendue et filtrage](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr#voice-library) pour tous les paramètres de filtre).

- **Limites de stockage et valeur TTL** : les voix avec état (`store=True`, partagées entre les voix incitées et répliquées) sont limitées à **200 voix par projet** et ont une **valeur TTL (Time To Live) d'un an**.
- **Disponibilité de `sample_audio`** : `voices.create()` (`CreateVoice`) et `voices.get()` (`GetVoice`) renseignent `sample_audio` (`mime_type:
  "audio/wav"`, `data` encodé en base64) pour les voix `"prompted"`. Pour que la fiche reste légère, `voices.list()` (`ListVoices`) omet `sample_audio` (et `sample_audio` n'est pas défini pour les voix `"replicated"` et `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Bonnes pratiques concernant les requêtes pour la conception vocale

- **Définissez les caractéristiques vocales permanentes dans la conception de la voix, et non dans `style`** : définissez les caractéristiques immuables (âge, genre, timbre, texture vocale et accent régional, par exemple) lorsque vous créez la voix dans `voices.create`.
- **Réservez `speech_metadata.style` pour les émotions situationnelles** : une fois votre voix personnalisée créée, utilisez de courtes requêtes `style` (par exemple, `"whispered urgently"` ou `"cheerful and energetic"`) pour orienter le jeu d'acteur tour par tour sans modifier l'identité principale du locuteur.
- **Soyez précis et concis** : une description claire en une ou deux phrases (par exemple, *une commentatrice sportive énergique et dynamique d'une trentaine d'années avec un léger accent du Midwest*) produit des résultats plus clairs et plus cohérents que des paragraphes contradictoires ou trop longs.

## Étape suivante

- Découvrez comment répliquer la voix d'un locuteur existant dans [Réplication de la voix](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=fr).
- Découvrez la mise en forme au niveau du tour, les balises intégrées et les dialogues à plusieurs locuteurs dans le [guide Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/24 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/24 (UTC)."],[],[]]
