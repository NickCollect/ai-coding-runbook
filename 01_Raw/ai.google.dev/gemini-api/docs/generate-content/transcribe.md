---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/transcribe?hl=fr
fetched_at: 2026-10-05T06:32:37.977253+00:00
title: "Transcription audio \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=fr)

Envoyer des commentaires

# Transcription audio

L'API Gemini convertit la parole contenue dans les fichiers audio en texte à l'aide du modèle Gemini 3.5 Transcribe (`gemini-3.5-transcribe`). Grâce aux capacités de compréhension audio de Gemini, elle fournit une transcription précise avec identification automatique de la langue, attribution des locuteurs, codes temporels au niveau des mots et suggestions de vocabulaire personnalisé. Il propose également un mode de [transcription intelligente](#transcription-modes) qui supprime les hésitations et met en forme le texte de manière intelligente.

Pour transcrire un fichier audio, importez-le et transmettez-le à `gemini-3.5-transcribe` :

### Python

```
from google import genai

client = genai.Client()

audio_file = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const audioFile = await ai.files.upload({
  file: "path/to/sample.mp3",
  mimeType: "audio/mp3",
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
});

console.log(response.text);
```

### REST

```
# First upload the file via the Files API, then pass its URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ]
  }'
```

## Présentation

Gemini 3.5 Transcribe est optimisé pour les tâches de reconnaissance vocale. Il gère les différents accents, les bruits de fond et les conversations multilingues.

Voici les principales fonctionnalités de cette solution :

- **Reconnaissance vocale automatique** : détecte automatiquement les langues dans [plus de 85 paramètres régionaux](#supported-languages). Gère le code-switching intra-phrase et inter-phrase sans configuration manuelle.
- **Vocabulaire personnalisé** : oriente la reconnaissance vers les termes, acronymes et noms propres spécifiques à un domaine en transmettant jusqu'à 1 000 expressions.
- **Diarisation des locuteurs** : permet de distinguer plusieurs locuteurs et d'attribuer des segments parlés à des libellés distincts.
- **Codes temporels au niveau du mot** : génèrent des décalages temporels de début et de fin précis pour chaque mot reconnu.
- **Transcription intelligente** : supprime les hésitations, les mots de remplissage et les répétitions, et applique une mise en forme structurée.
- **Mise en forme et normalisation** : applique la mise en majuscules, la ponctuation et la normalisation inverse du texte (par exemple, en convertissant "vingt-six millions de dollars" en "26 M$").

Pour le raisonnement audio général ou les systèmes de questions-réponses sur le contenu audio, utilisez [Compréhension audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=fr). Pour la synthèse audio de texte en voix, utilisez [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr).

## Détection de la langue et suggestions

Par défaut, le modèle détecte automatiquement la langue parlée. Il passe d'une langue à l'autre de manière dynamique lorsque les locuteurs alternent les langues.

Pour utiliser la détection automatique, omettez `language_codes` ou fournissez une liste vide :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            language_codes=[],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      languageCodes: [],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "languageCodes": []
      }
    }
  }'
```

Si vous connaissez la langue à l'avance, spécifiez les codes de langue BCP-47 dans `language_codes` pour améliorer la précision de la transcription (voir [Langues acceptées](#supported-languages)) :

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    languageCodes: ["es-ES"],
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "languageCodes": ["es-ES"]
    }
  }
}
```

## Vocabulaire personnalisé

Vous pouvez orienter le modèle vocal vers des mots inhabituels, du jargon technique, des noms de marques ou des noms propres. Fournissez jusqu'à 1 000 termes dans le tableau `custom_vocabulary` (les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes) :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      customVocabulary: ["Gemini", "Kubernetes", "BigQuery"],
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "customVocabulary": ["Gemini", "Kubernetes", "BigQuery"]
      }
    }
  }'
```

## Identification du locuteur

L'identification des locuteurs permet d'identifier les différentes voix dans l'enregistrement et d'attribuer un identifiant à chaque segment, comme `spk_1` ou `spk_2`. Jusqu'à huit locuteurs sont pris en charge (l'attribution pour trois locuteurs ou plus est expérimentale).

Activez l'identification des locuteurs en définissant `diarization` sur `True` :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            diarization=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      diarization: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "diarization": true
      }
    }
  }'
```

## Codes temporels au niveau du mot

Les codes temporels au niveau du mot fournissent des décalages de début et de fin exacts pour chaque mot reconnu dans le flux audio.

Activez les codes temporels en définissant `word_timestamp` sur `True` :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            word_timestamp=True,
        )
    ),
)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      wordTimestamp: true,
    },
  },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "wordTimestamp": true
      }
    }
  }'
```

Vous pouvez combiner `diarization` et `word_timestamp` dans une même requête pour recevoir à la fois les identifiants des intervenants et les codes temporels des mots :

### Python

```
config = types.GenerateContentConfig(
    audio_transcription_config=types.AudioTranscriptionConfig(
        diarization=True,
        word_timestamp=True,
    )
)
```

### JavaScript

```
const config = {
  audioTranscriptionConfig: {
    diarization: true,
    wordTimestamp: true,
  },
};
```

### REST

```
{
  "generationConfig": {
    "audioTranscriptionConfig": {
      "diarization": true,
      "wordTimestamp": true
    }
  }
}
```

## Modes de transcription

Gemini 3.5 Transcribe est compatible avec deux modes de transcription via le paramètre `mode` :

- **`VERBATIM` (par défaut)** : renvoie une transcription exacte de tout ce qui a été dit, en conservant les mots de remplissage bruts ("euh", "enfin", "genre", "tu vois"), les répétitions, les pauses et les faux départs. Obligatoire lorsque vous utilisez des codes temporels ou la segmentation des locuteurs.
- **`SMART` (Transcription intelligente)** : optimise la transcription pour la lecture en appliquant un post-traitement intelligent :
  - **Suppression des hésitations** : élimine les mots de remplissage, les bégaiements et les faux départs.
  - **Corrections spontanées** : les corrections orales sont résolues directement (par exemple, *"Rendez-vous mardi, non, mercredi à 14h"* devient *"Rendez-vous mercredi à 14h"*).
  - **Mise en forme structurée automatique** : structure automatiquement les pensées exprimées en paragraphes, listes numérotées, listes à puces, dates, devises et nombres mis en forme.
  - **Nettoyage grammatical** : applique une ponctuation, une mise en forme des phrases et un flux naturels.

| Audio parlé | Résultat de la fonction `VERBATIM` | Résultat de la fonction `SMART` (transcription intelligente) |
| --- | --- | --- |
| "Euh, pour la réunion, je pense qu'on devrait inviter Alice et, non, Bob et Carol." | "Euh, pour la réunion, je pense qu'on devrait inviter Alice, non, Bob et Carol." | "Pour la réunion, je pense que nous devrions inviter Bob et Carol." |
| "First item review budget second item finalize timeline third item send recap" (Premier élément : examiner le budget. Deuxième élément : finaliser le calendrier. Troisième élément : envoyer le récapitulatif.) | "examine le premier élément, vérifie le budget du deuxième élément, finalise le calendrier du troisième élément, envoie le récapitulatif" | "1. Vérifiez le budget. 2. Finalisez la timeline 3. Envoyer le récapitulatif" |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-transcribe",
    contents=[audio_file],
    config=types.GenerateContentConfig(
        audio_transcription_config=types.AudioTranscriptionConfig(
            mode="SMART",
        )
    ),
)
print(response.text)
```

### JavaScript

```
const response = await ai.models.generateContent({
  model: "gemini-3.5-transcribe",
  contents: [audioFile],
  config: {
    audioTranscriptionConfig: {
      mode: "SMART",
    },
  },
});
console.log(response.text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "fileData": {
              "fileUri": "YOUR_FILE_URI",
              "mimeType": "audio/mp3"
            }
          }
        ]
      }
    ],
    "generationConfig": {
      "audioTranscriptionConfig": {
        "mode": "SMART"
      }
    }
  }'
```

## Analyser la transcription

Le texte complet de la transcription est renvoyé dans `response.text`.

Lorsque `word_timestamp` ou `diarization` sont activés, l'API renvoie également des annotations détaillées au niveau des mots et des identifiants des intervenants associés aux parties candidates.

Voici comment extraire et parcourir les codes temporels des mots et les tours de parole :

### Python

```
def extract_word_transcriptions(response):
    words = []
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", []) or []:
            transcription = getattr(part, "audio_transcription", None)
            if transcription:
                speaker = getattr(transcription, "speaker_label", "")
                for word_info in getattr(transcription, "words", []) or []:
                    word = getattr(word_info, "word", "")
                    start = getattr(word_info, "start_offset", "")
                    end = getattr(word_info, "end_offset", "")
                    words.append({
                        "word": word,
                        "speaker": speaker,
                        "start_offset": start,
                        "end_offset": end,
                    })
    return words

words = extract_word_transcriptions(response)

for w in words:
    speaker = f"[{w['speaker']}] " if w["speaker"] else ""
    timing = f"({w['start_offset']} -> {w['end_offset']}) " if w["start_offset"] and w["end_offset"] else ""
    print(f"{speaker}{timing}{w['word']}")
```

### JavaScript

```
function extractWordTranscriptions(response) {
  const words = [];
  for (const candidate of response.candidates ?? []) {
    for (const part of candidate.content?.parts ?? []) {
      const transcription = part.audioTranscription;
      if (transcription) {
        const speaker = transcription.speakerLabel ?? "";
        for (const wordInfo of transcription.words ?? []) {
          words.push({
            word: wordInfo.word ?? "",
            speaker: speaker,
            startOffset: wordInfo.startOffset ?? "",
            endOffset: wordInfo.endOffset ?? "",
          });
        }
      }
    }
  }
  return words;
}

const words = extractWordTranscriptions(response);

for (const w of words) {
  const speaker = w.speaker ? `[${w.speaker}] ` : "";
  const timing = (w.startOffset && w.endOffset) ? `(${w.startOffset} -> ${w.endOffset}) ` : "";
  console.log(`${speaker}${timing}${w.word}`);
}
```

### REST

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "audioTranscription": {
              "speakerLabel": "spk_1",
              "words": [
                {
                  "word": "Hello",
                  "startOffset": "0.100s",
                  "endOffset": "0.450s"
                },
                {
                  "word": "world",
                  "startOffset": "0.500s",
                  "endOffset": "0.850s"
                }
              ]
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

## Langues disponibles

Les langues et les codes de langue BCP-47 suivants sont compatibles avec Gemini 3.5 Transcribe :

| Langue | Code BCP-47 | Langue | Code BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japonais | `ja-JP` |
| Amharique | `am-ET` | Javanais | `jv-ID` |
| Arabe (Égypte) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Arménien | `hy-AM` | Kannada | `kn-IN` |
| Assamais | `as-IN` | Kazakh | `kk-KZ` |
| Azéri | `az-AZ` | Coréen | `ko-KR` |
| Biélorusse | `be-BY` | Kirghiz | `ky-KG` |
| Bengali (Bangladesh) | `bn-BD` | Letton | `lv-LV` |
| Bengali (Inde) | `bn-IN` | Lingala | `ln-CD` |
| Bosniaque | `bs-BA` | Lituanien | `lt-LT` |
| Bulgare | `bg-BG` | Macédonien | `mk-MK` |
| Bulgare (aroumain) | `rup-BG` | Malaisien | `ms-MY` |
| Birman | `my-MM` | Malayalam | `ml-IN` |
| Cantonais (traditionnel) | `yue-Hant-HK` | Maltais | `mt-MT` |
| Catalan | `ca-ES` | Chinois mandarin (simplifié) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer central | `km-KH` | Mongol | `mn-MN` |
| Croate | `hr-HR` | Népalais | `ne-NP` |
| Tchèque | `cs-CZ` | Norvégien | `nb-NO` |
| Danois | `da-DK` | Oriya | `or-IN` |
| Néerlandais | `nl-NL` | Polonais | `pl-PL` |
| Anglais (Grande-Bretagne) | `en-GB` | Portugais (Brésil) | `pt-BR` |
| Anglais (Inde) | `en-IN` | Portugais (Portugal) | `pt-PT` |
| Anglais (États-Unis) | `en-US` | Panjabi | `pa-IN` |
| Estonien | `et-EE` | Panjabi (écriture gurmukhī) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Roumain | `ro-RO` |
| Tagalog | `fil-PH` | Russe | `ru-RU` |
| Finnois | `fi-FI` | Serbe | `sr-RS` |
| Français | `fr-FR` | Sindhi (écriture arabe) | `sd-Arab-IN` |
| Galicien | `gl-ES` | Slovaque | `sk-SK` |
| Géorgien | `ka-GE` | Slovène | `sl-SI` |
| Allemand | `de-DE` | Espagnol (Amérique latine) | `es-419` |
| Grec | `el-GR` | Espagnol (États-Unis) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Haoussa | `ha-NG` | Suédois | `sv-SE` |
| Hébreu | `he-IL` | Tadjik | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Hongrois | `hu-HU` | Thaï | `th-TH` |
| Islandais | `is-IS` | Turc | `tr-TR` |
| Anglais (Inde) | `en-IN` | Ukrainien | `uk-UA` |
| Indonésien | `id-ID` | Ouzbek | `uz-UZ` |
| Italien | `it-IT` | Vietnamien | `vi-VN` |

## Formats audio acceptés

Gemini 3.5 Transcribe est compatible avec les types MIME de format audio suivants :

- WAV - `audio/wav`
- MP3 - `audio/mp3`
- AIFF – `audio/aiff`
- AAC - `audio/aac`
- OGG - `audio/ogg`
- FLAC - `audio/flac`
- MPEG - `audio/mpeg`
- M4A - `audio/m4a`
- L16 – `audio/l16`
- Opus – `audio/opus`
- ALAW - `audio/alaw`
- MULAW - `audio/mulaw`
- WebM - `audio/webm`

Pour obtenir la liste complète des types MIME et des schémas de paramètres acceptés, consultez la [documentation de référence de l'API Interactions](https://ai.google.dev/api/interactions-api?hl=fr#Resource:Content).

## Référence de paramètre

Configurez la transcription en définissant les champs de l'objet `audio_transcription_config` dans `GenerateContentConfig` :

| Champ | Type | Description |
| --- | --- | --- |
| `language_codes` | Tableau de chaînes | Codes de langue BCP-47 (par exemple, `["en-US"]`). S'ils sont omis ou vides (`[]`), le modèle détecte automatiquement la langue et gère le changement de code. |
| `custom_vocabulary` | Tableau de chaînes | Jusqu'à 1 000 termes, acronymes ou noms propres personnalisés pour orienter la reconnaissance vocale. Incompatible avec l'identification du locuteur et les codes temporels au niveau du mot. |
| `word_timestamp` | Booléen | Définissez sur `True` pour inclure les décalages de début et de fin des mots. Si cette option est omise ou définie sur `False`, aucun code temporel de mot n'est renvoyé. Incompatible avec le vocabulaire personnalisé. |
| `diarization` | Booléen | Définissez la valeur sur `True` pour identifier les différents intervenants et leur attribuer un identifiant. Incompatible avec le vocabulaire personnalisé. |
| `mode` | Chaîne | Mode Transcription. Valeurs acceptées : `"VERBATIM"` (par défaut) et `"SMART"`. Incompatible avec les codes temporels et l'identification des locuteurs. |

## Bonnes pratiques

- **Fournissez un son clair** : assurez-vous que les enregistrements audio ont une séparation vocale claire et évitez les découpages importants.
- **Fournissez des indications de langue si vous les connaissez** : si vous connaissez la langue de l'audio à l'avance, spécifiez `language_codes` pour maximiser la précision.
- **Cibler un vocabulaire personnalisé** : n'incluez que des termes de domaine distincts, des noms de marques ou des noms propres dans `custom_vocabulary`, plutôt que des mots courants.
- **Utilisez l'API Files pour les enregistrements volumineux** : pour les fichiers de plus de quelques secondes, importez le fichier à l'aide de `client.files.upload` et transmettez le fichier renvoyé au contenu du modèle.

## Limites

- **Durée de l'audio** : les requêtes unitaires standards sont compatibles avec les fichiers audio d'une durée maximale d'une heure. Le traitement audio est limité à 30 minutes lorsque des fonctionnalités telles que la segmentation des locuteurs ou les codes temporels au niveau des mots sont activées.
- **Codes temporels au niveau du mot** : l'activation des codes temporels au niveau du mot peut dégrader la précision globale de la transcription.
- **Identification des locuteurs** : l'identification des locuteurs est compatible avec un maximum de huit locuteurs. L'attribution des locuteurs pour trois locuteurs ou plus est une fonctionnalité expérimentale.
- **Vocabulaire personnalisé** : vous pouvez fournir jusqu'à 1 000 termes dans `custom_vocabulary`, mais les meilleurs résultats sont généralement obtenus avec un maximum de 100 termes. Vous ne pouvez pas combiner `custom_vocabulary` avec la segmentation des locuteurs ou les codes temporels au niveau des mots. L'API rejette les requêtes qui spécifient `custom_vocabulary` avec l'une ou l'autre de ces fonctionnalités.
- **Compatibilité des modes** : la transcription intelligente (`mode: "SMART"`) ne peut pas être combinée avec `word_timestamp` ni `diarization`.

## Étape suivante

- Diffusez de l'audio en temps réel avec le [guide de transcription en direct](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=fr) à l'aide de l'API Live.
- Explorez la [compréhension audio](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=fr) pour analyser, résumer ou interroger des contenus audio.
- Découvrez comment synthétiser des contenus audio à partir de texte à l'aide de [Text-to-Speech](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=fr).
- Consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#gemini-3.5-transcribe) pour connaître les tarifs des modèles et les limites de jetons.
- Consultez le guide de l'[API Files](https://ai.google.dev/gemini-api/docs/files?hl=fr) pour savoir comment importer et gérer des fichiers multimédias.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/08 (UTC)."],[],[]]
