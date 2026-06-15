---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=fr
fetched_at: 2026-06-15T06:33:19.994819+00:00
title: "G\u00e9n\u00e9ration de musique en temps r\u00e9el avec Lyria RealTime \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Génération de musique en temps réel avec Lyria RealTime

L'API Gemini, qui utilise
[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=fr),
donne accès à un modèle de génération de musique en streaming, en temps réel et de pointe. Elle permet aux développeurs de créer des applications dans lesquelles les utilisateurs peuvent créer, diriger et interpréter de la musique instrumentale de manière interactive et continue.

La génération de musique Lyria RealTime utilise une connexion de streaming persistante, bidirectionnelle,
à faible latence via
[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).

Pour découvrir ce qu'il est possible de créer avec Lyria RealTime, essayez-le dans AI Studio
à l'aide des applications [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=fr) ou
[MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=fr).

## Générer et contrôler de la musique

Lyria RealTime fonctionne de la même manière que l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr)
en ce sens qu'elle utilise des WebSockets pour maintenir une communication en temps réel avec le modèle.

Le code suivant montre comment générer de la musique :

### Python

Cet exemple initialise la session Lyria RealTime à l'aide de `client.aio.live.music.connect()`, puis envoie une requête initiale avec `session.set_weighted_prompts()` ainsi qu'une configuration initiale à l'aide de `session.set_music_generation_config`, démarre la génération de musique à l'aide de `session.play()` et configure `receive_audio()` pour traiter les blocs audio qu'il reçoit.

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

Cet exemple initialise la session Lyria RealTime à l'aide de `client.live.music.connect()`, puis envoie une requête initiale avec `session.setWeightedPrompts()` ainsi qu'une configuration initiale à l'aide de `session.setMusicGenerationConfig`, démarre la génération de musique à l'aide de `session.play()` et configure un rappel `onMessage` pour traiter les blocs audio qu'il reçoit.

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

Vous pouvez ensuite utiliser `session.play()`, `session.pause()`, `session.stop()` et `session.reset_context()` pour démarrer, mettre en pause, arrêter ou réinitialiser la session.

## Diriger la musique en temps réel

Vous pouvez diriger la génération de musique en temps réel en envoyant des requêtes et en mettant à jour les paramètres de génération en temps réel.

### Requête Lyria RealTime

Lorsque le flux est actif, vous pouvez envoyer de nouveaux messages `WeightedPrompt` à tout moment pour modifier la musique générée. Le modèle effectue une transition en douceur en fonction de la nouvelle entrée.

Les requêtes doivent respecter le bon format avec un `text` (la requête proprement dite) et un `weight`. Le `weight` peut prendre n'importe quelle valeur, sauf `0`. `1.0`
est généralement un bon point de départ.

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

Notez que les transitions de modèle peuvent être un peu abruptes lorsque vous modifiez radicalement les requêtes. Il est donc recommandé d'implémenter une sorte de fondu enchaîné en envoyant des valeurs de pondération intermédiaires au modèle.

### Mettre à jour la configuration

Vous pouvez diriger la génération de musique en mettant à jour les paramètres de génération de musique en temps réel. Vous ne pouvez pas simplement mettre à jour un paramètre. Vous devez définir l'ensemble de la configuration, sinon les autres champs seront réinitialisés à leurs valeurs par défaut.

Étant donné que la modification du BPM ou de la gamme constitue un changement radical pour le modèle, vous devez également lui demander de réinitialiser son contexte à l'aide de `reset_context()` pour prendre en compte la nouvelle configuration. Le flux ne s'arrête pas, mais la transition sera difficile. Vous n'avez pas besoin de le faire pour les autres paramètres.

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

## Guide sur les prompts pour Lyria RealTime

Voici une liste non exhaustive de requêtes que vous pouvez utiliser pour interroger Lyria RealTime :

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
- Genre musical : `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
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
- Ambiance/Description : `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Ce ne sont là que quelques exemples. Lyria RealTime peut faire bien plus. Essayez vos propres requêtes.

## Bonnes pratiques

- Les applications clientes doivent implémenter une mise en mémoire tampon audio robuste pour garantir une lecture fluide. Cela permet de tenir compte de la gigue du réseau et des légères variations de la latence de génération.
- Requêtes efficaces :
  - Utilisez des mots clés descriptifs. Utilisez des adjectifs décrivant l'ambiance, le genre et l'instrumentation.
  - Itérez et dirigez progressivement. Plutôt que de modifier complètement la requête, essayez d'ajouter ou de modifier des éléments pour transformer la musique plus en douceur.
  - Testez la pondération sur `WeightedPrompt` pour influencer la force avec laquelle une nouvelle requête affecte la génération en cours.

## Détails techniques

Cette section décrit les spécificités de l'utilisation de la génération de musique Lyria RealTime.

### Spécifications

- Format de sortie : audio PCM 16 bits brut
- Taux d'échantillonnage : 48 kHz
- Chaînes : 2 (stéréo)

### Commandes

La génération de musique peut être influencée en temps réel en envoyant des messages contenant les éléments suivants :

- `WeightedPrompt`: chaîne de texte décrivant une idée musicale, un genre, un instrument, une ambiance ou une caractéristique. Plusieurs requêtes peuvent être fournies pour combiner les influences. Pour en savoir plus sur la meilleure façon d'interroger
  Lyria RealTime, consultez la section [ci-dessus](https://ai.google.dev/gemini-api/docs/:?hl=fr#steer-music).
- `MusicGenerationConfig`: configuration du processus de génération de musique, qui influence les caractéristiques de la sortie audio. Les paramètres incluent les éléments suivants :
  - `guidance` : (float) Plage : `[0.0, 6.0]`. Valeur par défaut : `4.0`.
    Contrôle la rigueur avec laquelle le modèle suit les requêtes. Une guidance plus élevée améliore le respect de la requête, mais rend les transitions plus abruptes.
  - `bpm` : (int) Plage : `[60, 200]`.
    Définit le nombre de battements par minute souhaité pour la musique générée. Vous devez arrêter/lire ou réinitialiser le contexte pour que le modèle prenne en compte le nouveau BPM.
  - `density` : (float) Plage : `[0.0, 1.0]`.
    Contrôle la densité des notes/sons musicaux. Les valeurs inférieures produisent une musique plus éparse, tandis que les valeurs supérieures produisent une musique plus "chargée".
  - `brightness` : (float) Plage : `[0.0, 1.0]`.
    Ajuste la qualité tonale. Les valeurs plus élevées produisent un son plus "brillant", en mettant généralement l'accent sur les fréquences plus élevées.
  - `scale`: (Enum) Définit la gamme musicale (clé et mode) pour la génération. Utilisez les
    [`Scale` valeurs enum](#scale-enum) fournies par le SDK. Vous devez arrêter/lire ou réinitialiser le contexte pour que le modèle prenne en compte la nouvelle gamme.
  - `mute_bass` : (bool) Valeur par défaut : `False`.
    Contrôle si le modèle réduit les basses des sorties.
  - `mute_drums` : (bool) Valeur par défaut : `False`.
    Contrôle si le modèle réduit les percussions des sorties.
  - `only_bass_and_drums` : (bool) Valeur par défaut : `False`.
    Dirige le modèle pour qu'il n'essaie de générer que des basses et des percussions.
  - `music_generation_mode`: (Enum) Indique au modèle s'il doit se concentrer sur la `QUALITY` (valeur par défaut) ou la `DIVERSITY` de la musique. Il peut également être défini sur `VOCALIZATION` pour permettre au modèle de générer des vocalises comme un autre instrument (ajoutez-les en tant que nouvelles requêtes).
- `PlaybackControl`: commandes permettant de contrôler les aspects de la lecture, tels que la lecture, la mise en pause, l'arrêt ou la réinitialisation du contexte.

Pour `bpm`, `density`, `brightness` et `scale`, si aucune valeur n'est fournie, le modèle décide de ce qui est le mieux en fonction de vos requêtes initiales.

Des paramètres plus classiques tels que `temperature` (0.0 à 3.0, valeur par défaut 1.1), `top_k` (1 à 1 000, valeur par défaut 40) et `seed` (0 à 2 147 483 647, sélectionnée de manière aléatoire par défaut) sont également personnalisables dans `MusicGenerationConfig`.

#### Valeurs enum de la gamme

Voici toutes les valeurs de gamme que le modèle peut accepter :

| Valeur enum | Gamme / Clé |
| --- | --- |
| `C_MAJOR_A_MINOR` | Do majeur / La mineur |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Ré bémol majeur / Si bémol mineur |
| `D_MAJOR_B_MINOR` | Ré majeur / Si mineur |
| `E_FLAT_MAJOR_C_MINOR` | Mi bémol majeur / Do mineur |
| `E_MAJOR_D_FLAT_MINOR` | Mi majeur / Do dièse/Ré bémol mineur |
| `F_MAJOR_D_MINOR` | Fa majeur / Ré mineur |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol bémol majeur / Mi bémol mineur |
| `G_MAJOR_E_MINOR` | Sol majeur / Mi mineur |
| `A_FLAT_MAJOR_F_MINOR` | La bémol majeur / Fa mineur |
| `A_MAJOR_G_FLAT_MINOR` | La majeur / Fa dièse/Sol bémol mineur |
| `B_FLAT_MAJOR_G_MINOR` | Si bémol majeur / Sol mineur |
| `B_MAJOR_A_FLAT_MINOR` | Si majeur / Sol dièse/La bémol mineur |
| `SCALE_UNSPECIFIED` | Par défaut / Le modèle décide |

Le modèle est capable de guider les notes jouées, mais ne fait pas la distinction entre les clés relatives. Ainsi, chaque enum correspond à la fois au majeur et au mineur relatifs. Par exemple, `C_MAJOR_A_MINOR` correspond à toutes les touches blanches d'un piano, et `F_MAJOR_D_MINOR` à toutes les touches blanches sauf le si bémol.

### Limites

- Instrumental uniquement : le modèle ne génère que de la musique instrumentale.
- Sécurité : les requêtes sont vérifiées par des filtres de sécurité. Les requêtes qui déclenchent les filtres seront ignorées. Dans ce cas, une explication sera écrite dans le champ `filtered_prompt` de la sortie.
- Filigrane : la sortie audio est toujours filigranée pour l'identification, conformément à
  nos [principes d'IA responsable](https://ai.google/responsibility/principles/?hl=fr).

## Étape suivante

- Générez des chansons complètes et des pistes vocales avec [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=fr).
- Au lieu de la musique, découvrez comment générer une conversation à plusieurs locuteurs à l'aide de
  les [modèles TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr).
- Découvrez comment générer des [images](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) ou des [vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr).
- Au lieu de générer de la musique ou de l'audio, découvrez comment Gemini peut
  [comprendre les fichiers audio](https://ai.google.dev/gemini-api/docs/audio?hl=fr).
- Discutez en temps réel avec Gemini à l'aide de l'
  [API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

Consultez le [livre de recettes](https://github.com/google-gemini/cookbook) pour obtenir d'autres
exemples de code et tutoriels.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/01 (UTC)."],[],[]]
