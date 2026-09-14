---
source_url: https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr
fetched_at: 2026-09-14T05:47:00.290600+00:00
title: "Gestion des sessions avec l'API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Gestion des sessions avec l'API Live

Dans l'API Live, une session fait référence à une connexion persistante
dans laquelle les entrées et les sorties sont diffusées en continu sur la même
connexion (en savoir plus sur [son fonctionnement](https://ai.google.dev/gemini-api/docs/live?hl=fr)).
Cette conception de session unique permet une faible latence et prend en charge des fonctionnalités uniques, mais peut également poser des problèmes, tels que des limites de temps de session et une résiliation anticipée.
Ce guide présente des stratégies pour surmonter les problèmes de gestion de session qui peuvent survenir lors de l'utilisation de l'API Live.

## Durée de vie de la session

Sans compression, les sessions audio uniquement sont limitées à 15 minutes, et les sessions audio-vidéo à 2 minutes. Si vous dépassez ces limites, la session (et donc la connexion) sera interrompue. Toutefois, vous pouvez utiliser
[la compression de la fenêtre de contexte](#context-window-compression) pour étendre les sessions à
une durée illimitée.

La durée de vie d'une connexion est également limitée à environ 10 minutes. Lorsque la connexion est interrompue, la session l'est également. Dans ce cas, vous pouvez
configurer une seule session pour qu'elle reste active sur plusieurs connexions à l'aide de
[la reprise de session](#session-resumption).
Vous recevrez également un [message GoAway](#goaway-message) avant la
fin de la connexion, ce qui vous permettra de prendre d'autres mesures.

## Compression de la fenêtre de contexte

Pour activer des sessions plus longues et éviter l'interruption brutale de la connexion, vous pouvez
activer la compression de la fenêtre de contexte en définissant le champ [contextWindowCompression](https://ai.google.dev/api/live?hl=fr#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
dans la configuration de la session.

Dans [ContextWindowCompressionConfig](https://ai.google.dev/api/live?hl=fr#contextwindowcompressionconfig), vous pouvez configurer un
[mécanisme de fenêtre glissante](https://ai.google.dev/api/live?hl=fr#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
et le [nombre de jetons](https://ai.google.dev/api/live?hl=fr#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
qui déclenchent la compression.

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

## Reprise de session

Pour éviter l'interruption de la session lorsque le serveur réinitialise périodiquement la connexion WebSocket, configurez le champ [sessionResumption](https://ai.google.dev/api/live?hl=fr#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
dans la [configuration](https://ai.google.dev/api/live?hl=fr#BidiGenerateContentSetup).

Lorsque vous transmettez cette configuration, le
serveur envoie des messages [SessionResumptionUpdate](https://ai.google.dev/api/live?hl=fr#SessionResumptionUpdate)
, qui peuvent être utilisés pour reprendre la session en transmettant le dernier jeton de reprise
en tant que [`SessionResumptionConfig.handle`](https://ai.google.dev/api/live?hl=fr#SessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)
de la connexion suivante.

Les jetons de reprise sont valides pendant deux heures après la fin des dernières sessions.

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

## Recevoir un message avant la déconnexion de la session

Le serveur envoie un message [GoAway](https://ai.google.dev/api/live?hl=fr#GoAway) qui signale que la connexion actuelle
sera bientôt interrompue. Ce message inclut le [timeLeft](https://ai.google.dev/api/live?hl=fr#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left),
qui indique le temps restant et vous permet de prendre d'autres mesures avant que la
connexion ne soit interrompue (considérée comme ABORTED).

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

## Recevoir un message lorsque la génération est terminée

Le serveur envoie un [generationComplete](https://ai.google.dev/api/live?hl=fr#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
message qui signale que le modèle a terminé de générer la réponse.

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

## Étape suivante

Découvrez d'autres façons d'utiliser l'API Live dans le guide complet des
[fonctionnalités](https://ai.google.dev/gemini-api/docs/live?hl=fr),
la page [Utilisation des outils](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr) ou le
[livre de recettes de l'API Live](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.ipynb?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/08 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/08 (UTC)."],[],[]]
