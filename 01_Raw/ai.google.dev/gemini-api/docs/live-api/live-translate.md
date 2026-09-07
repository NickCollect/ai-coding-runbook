---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=fr
fetched_at: 2026-09-07T05:39:35.925367+00:00
title: "Traduction instantan\u00e9e avec l'API Gemini\u00a0Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Traduction instantanée avec l'API Gemini Live

L'API Gemini Live est compatible avec la traduction vocale en temps réel et à faible latence entre plus de 70 langues à l'aide du [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=fr) modèle. En configurant l'API Live avec des paramètres de traduction, vous pouvez diffuser de l'audio dans une langue et recevoir une sortie audio traduite dans une autre langue, ce qui permet une traduction vocale en temps réel fluide.

[Essayer la traduction instantanée dans Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=fr)
[Cloner l'exemple d'application depuis GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Utiliser les compétences de l'agent de codageterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr#gemini-live-api-dev)

## Agent en direct ou traduction instantanée

Bien que les deux utilisent l'API Live, le modèle mental de la traduction instantanée est différent des interactions conversationnelles en temps réel avec un agent.

| Agent en direct | Traduction instantanée |
| --- | --- |
| **Le modèle agit comme un assistant.** Il écoute, raisonne et effectue des actions en votre nom. | **Le modèle agit comme un interprète.** Il se comporte comme un pipeline de traduction en temps réel. |
| **Utilise des interactions basées sur les tours de parole.** S'appuie sur les pauses, la détection d'intention et gère les interruptions. | **Utilise le traitement continu des flux.** Traduit pendant que l'orateur parle sans attendre son tour. |
| **Compatible avec les outils et les agents.** Compatibilité native avec les appels de fonction, la recherche Google et les instructions. | **Compatible uniquement avec la traduction.** Traduction pure à faible latence, sans compatibilité avec les outils ni les instructions. |
| **Entièrement multimodal.** Compatible avec les entrées de texte, audio, vidéo et image. | **Audio limité.** L'entrée est limitée à l'audio pour garantir des seuils de latence en temps réel stricts. |
| **Configuration précise.** Utilise la génération, la parole, les outils et les instructions système. | **Configuration simplifiée.** Définissez `target_language_code` et des boutons à bascule comme `echo_target_language`. |

## Premiers pas

Les exemples suivants montrent comment initialiser un client et se connecter à l'API Live avec une configuration de traduction.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Envoyer l'audio

Pour diffuser des entrées vocales à traduire, envoyez de l'audio PCM 16 bits brut, little-endian.

- **Format audio d'entrée** : PCM 16 bits brut à 16 kHz (mono, little-endian).
- **Format audio de sortie** : PCM 16 bits brut à 24 kHz (mono, little-endian).
- **Taille des blocs et latence** : envoyez l'audio par blocs de 100 ms.

Les exemples suivants montrent comment envoyer des blocs audio à la session.

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

### WebSockets

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
  }
}
```

## Configuration

Pour activer la traduction, vous devez spécifier `translationConfig` dans `generationConfig` lors de la configuration de la session.

### Configurer les messages de configuration

`generationConfig` accepte les champs suivants pour activer les transcriptions :

- **`inputAudioTranscription`**: objet qui, lorsqu'il est présent, permet au modèle d'envoyer des transcriptions textuelles de l'audio d'entrée.
- **`outputAudioTranscription`**: objet qui, lorsqu'il est présent, permet au modèle d'envoyer des transcriptions textuelles de l'audio de sortie (traduit).

`translationConfig` accepte les champs suivants :

- **`targetLanguageCode`** : le [code de langue BCP-47](#supported-languages) de la langue dans laquelle vous souhaitez que le modèle traduise (par exemple, `"pl"` pour le polonais, `"es"` pour l'espagnol). La valeur par défaut est `"en"`.
- **`echoTargetLanguage`**: valeur booléenne indiquant comment gérer l'audio d'entrée qui est déjà dans la langue cible. Si la valeur est `true`, le modèle répète l'audio d'entrée qui est déjà dans la langue cible. Si la valeur est `false`, le modèle reste silencieux lorsque la parole d'entrée est déjà dans la langue cible. La valeur par défaut est `false`.

Voici un exemple de structure de message de configuration :

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## Utiliser des jetons éphémères dans les applications côté client

Pour les applications client-serveur, vous pouvez utiliser [des jetons éphémères](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr) (actuellement en `v1beta`) pour éviter d'exposer votre clé API.

Lorsque vous utilisez des jetons éphémères avec la traduction instantanée :

1. Vous devez utiliser le point de terminaison `v1beta`.
2. **Verrouillage de la configuration** : par défaut, vous devez spécifier `translationConfig` dans les contraintes de création de jeton sur votre serveur. Cela garantit que la configuration de traduction est verrouillée et ne peut pas être falsifiée par le client.
3. **Déverrouillage de la configuration** : si vous souhaitez pouvoir définir `translationConfig` côté client (par exemple, pour permettre à un utilisateur de choisir sa propre langue cible), vous devez l'omettre de la requête de création de jeton et définir `"lock_additional_fields": []` à la place. Cela déverrouillera `translationConfig` pour qu'il soit défini côté client.

### Créer un jeton éphémère contraint

Les exemples suivants montrent comment créer un jeton éphémère avec des contraintes de traduction.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## Limites

- **Modalités d'entrée** : seule l'entrée audio est acceptée pour la traduction. L'entrée de texte n'est pas acceptée.
- **Réplication vocale** : la réplication vocale peut être incohérente. Les voix peuvent changer après de longues pauses, attribuer le mauvais genre en fonction du début de la parole ou rester bloquées sur une seule voix lors de conversations rapides entre plusieurs personnes.
- **Détection de la langue** : la détection de la langue a du mal avec les accents prononcés, les langues similaires (par exemple, l'espagnol et le portugolais) ou les changements de langue rapides. **Remarque** : Cela ne devrait avoir d'impact que sur la transcription d'entrée. Les codes de langue et la traduction finale doivent toujours être précis.
- **Audio de fond** : le modèle est conçu pour filtrer le bruit et la musique afin de produire une parole claire, mais il est possible que l'audio de fond ne soit pas entièrement ignoré.
- **Écho de la langue cible** : lorsque `echoTargetLanguage: true`, le bruit de fond ou la musique peuvent introduire des artefacts dans l'audio traduit lorsque l'audio d'entrée est déjà dans la langue cible.

## Langues disponibles

Les langues suivantes sont disponibles pour la traduction instantanée.

| Langue | Code BCP-47 | Langue | Code BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | af | Kazakh | kk |
| Akan | ak | Khmer | km |
| Albanais | sq | Kinyarwanda | rw |
| Amharique | am | Coréen | ko |
| Arabe | ar | Laotien | lo |
| Arménien | hy | Letton | lv |
| Azéri | az | Lituanien | lt |
| Basque | eu | Macédonien | mk |
| Biélorusse | be | Malaisien | ms |
| Bengali | bn | Malayalam | ml |
| Bulgare | bg | Marathi | mr |
| Birman (Myanmar) | my | Mongol | mn |
| Catalan | ca | Népalais | ne |
| Chinois (simplifié) | zh-Hans | Norvégien | no, nb |
| Chinois (traditionnel) | zh-Hant | Persan | fa |
| Croate | hr | Polonais | pl |
| Tchèque | cs | Portugais (Brésil) | pt-BR |
| Danois | da | Portugais (Portugal) | pt-PT |
| Néerlandais | nl | Panjabi | pa |
| Anglais | en | Roumain | ro |
| Estonien | et | Russe | ru |
| Tagalog | fil | Serbe | sr |
| Finnois | fi | Sindhî | sd |
| Français | fr | Cingalais | si |
| Galicien | gl | Slovaque | sk |
| Géorgien | ka | Slovène | sl |
| Allemand | de | Espagnol | es |
| Grec | el | Soundanais | su |
| Gujarati | gu | Swahili | sw |
| Haoussa | ha | Suédois | sv |
| Hébreu | he | Tamoul | ta |
| Hindi | hi | Telugu | te |
| Hongrois | hu | Thaï | th |
| Islandais | is | Turc | tr |
| Indonésien | id | Ukrainien | uk |
| Italien | it | Urdu | ur |
| Japonais | ja | Ouzbek | uz |
| Javanais | jv | Vietnamien | vi |
| Kannada | kn | Zoulou | zu |

## Étape suivante

- Consultez le guide complet sur les fonctionnalités de l'API Live [Capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=fr).
- Consultez le guide [Premiers pas avec le SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=fr).
- Consultez le guide [Premiers pas avec WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=fr).
- Consultez le guide [Jetons éphémères](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr) pour une authentification sécurisée dans les applications client-serveur.
- Clonez les [exemples d'API Live](https://github.com/google-gemini/gemini-live-api-examples) depuis GitHub.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/23 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/23 (UTC)."],[],[]]
