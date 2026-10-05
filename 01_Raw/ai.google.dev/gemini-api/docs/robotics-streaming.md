---
source_url: https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fr
fetched_at: 2026-10-05T06:43:27.327929+00:00
title: "Robotique avec streaming \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Robotique avec streaming

Le point de terminaison du modèle `gemini-robotics-er-2-streaming-preview` expose un point de terminaison de streaming dédié qui s'intègre à l'[API Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=fr), ce qui permet une interaction bidirectionnelle en temps réel entre votre application et le robot. Elle convient donc aux agents qui ont besoin de boucles de rétroaction rapides et de réponses réactives à l'environnement.

[Essayer dans Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=fr)
[Cloner des exemples d'applications depuis GitHub](https://github.com/google-gemini/robotics-samples/tree/main/live-api)

## Cas d'utilisation

- **Coordination de plusieurs robots** : plusieurs robots communiquent l'état des tâches et délèguent des sous-tâches par le biais d'une session partagée.
- **Surveillance continue** : robots qui observent une scène et déclenchent des actions lorsque des événements spécifiques se produisent, par exemple lorsqu'un conteneur atteint un certain niveau de remplissage.
- **Entrepôt et logistique** : agents de préparation et d'emballage qui vérifient visuellement les articles, suivent la progression de l'emballage et corrigent les erreurs.

## Spécifications techniques

Le tableau suivant présente les spécifications techniques de l'API Live :

| Catégorie | Détails |
| --- | --- |
| Modes d'entrée | Audio (audio PCM 16 bits brut, 16 kHz, little-endian), images (JPEG <= 1 FPS), texte |
| Modes de sortie | Texte |
| Protocole | Connexion WebSocket avec état (WSS) |

## Créer une configuration agentique

Chaque agent robotique basé sur l'API Live suit trois étapes :

1. **Déclarez les capacités du robot en tant qu'outils.** Chaque action que le robot peut effectuer (naviguer, saisir, parler, etc.) devient une déclaration de fonction avec un nom, une description et un schéma de paramètres. Les actions physiques doivent utiliser `"behavior": "BLOCKING"` pour que le modèle attende que le robot ait terminé avant de choisir l'étape suivante.
2. **Transmettre des entrées multimodales dans une session persistante** Ouvrez une session `live.connect` et laissez-la ouverte pendant toute la durée de la tâche. Envoyez des images vidéo, de l'audio ou du texte à mesure qu'ils arrivent des capteurs de votre robot.
3. **Gérer les appels d'outils dans une boucle de réception** Chaque fois que le modèle sélectionne une action, il envoie un message `tool_call`. Votre boucle de réception exécute la fonction par rapport à votre SDK de robot et renvoie un `tool_response`. La session reste ouverte et le modèle choisit la prochaine action en fonction du résultat.

Les sections suivantes montrent comment appliquer ces étapes à trois modèles courants : une boucle d'agent de référence, la surveillance proactive de scènes avec un signal de présence et le routage de la parole via TTS en tant qu'outil.

## Orchestrer un robot à l'aide de l'appel de fonction

L'exemple suivant montre les trois étapes connectées dans un seul script Python.

L'étape 1 (définitions d'outils) déclare les capacités du robot sous forme de déclarations de fonctions. La fonction `navigate` utilise `"behavior": "BLOCKING"`. Le modèle attend donc que le robot atteigne le point de cheminement avant d'appeler un autre outil.
Ajoutez d'autres déclarations de fonction dans la même liste pour exposer des capacités de robot supplémentaires.

L'étape 2 (assistants d'entrée) présente trois fonctions qui transmettent en flux continu différentes entrées de modalités dans la session : `send_text` pour les commandes, `send_image` pour les images de caméra avec un prompt textuel facultatif et `send_audio` pour l'audio PCM brut provenant d'un micro.

L'étape 3 (boucle de réception) s'exécute simultanément et gère deux types de messages : les messages `server_content` (sortie de texte du modèle) et les messages `tool_call` (le modèle demandant une action du robot). Lorsqu'un appel d'outil arrive, la boucle appelle `execute_tool` (un stub que vous remplacez par votre véritable SDK de robot), puis renvoie un `tool_response` afin que le modèle puisse sélectionner la prochaine action.

```
import asyncio
from google import genai
from google.genai import types

MODEL = "gemini-robotics-er-2-streaming-preview"

# ── Tool definitions ─────────────────────────────────────────────────────────
tools = [
   {
       "function_declarations": [
           {
               "name": "navigate",
               "description": "Navigate the robot to a named waypoint.",
               "behavior": "BLOCKING",
               "parameters": {
                   "type": "OBJECT",
                   "properties": {"name": {"type": "STRING"}},
                   "required": ["name"],
               },
           },
           # Add more function definitions here
       ]
   }
]

# ── Stub tool executor (replace with real robot SDK calls) ───────────────────
def execute_tool(name: str, args: dict) -> dict:
   print(f"  [Tool] {name}({args})")
   return {"status": "success"}

# ── Input helpers ────────────────────────────────────────────────────────────
def send_text(session, text: str):
   """Send a text turn."""
   return session.send_client_content(
       turns=types.Content(role="user", parts=[types.Part(text=text)]),
       turn_complete=True,
   )

def send_image(session, image_bytes: bytes, prompt: str = ""):
   """Send a JPEG image with an optional text prompt."""
   parts = [
       types.Part(
           inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
       )
   ]
   if prompt:
       parts.append(types.Part(text=prompt))
   return session.send_client_content(
       turns=types.Content(role="user", parts=parts),
       turn_complete=True,
   )

def send_audio(session, audio_chunk: bytes):
   """Stream a chunk of raw PCM audio (16-bit, 16 kHz, mono)."""
   return session.send_realtime_input(
       media=types.Blob(data=audio_chunk, mime_type="audio/pcm;rate=16000")
   )

# ── Receive loop ─────────────────────────────────────────────────────────────
async def receive_loop(session):
   """Print model text and handle tool calls until the session ends."""
   async for message in session.receive():
       if message.server_content:
           sc = message.server_content
           if sc.model_turn and sc.model_turn.parts:
               for part in sc.model_turn.parts:
                   if part.text:
                       print(f"Model: {part.text}", end="", flush=True)
           if sc.turn_complete:
               print("\n[Turn Complete]")
       elif message.tool_call:
           responses = []
           for call in message.tool_call.function_calls:
               print(f"\n[Tool Call] {call.name}({call.args})")
               result = execute_tool(call.name, call.args)
               responses.append(
                   types.FunctionResponse(
                       name=call.name,
                       response=result,
                       id=call.id,
                   )
               )
           await session.send_tool_response(function_responses=responses)

# ── Main ─────────────────────────────────────────────────────────────────────
async def main():
   client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
   config = types.LiveConnectConfig(
       response_modalities=["TEXT"],
       tools=tools,
       system_instruction=types.Content(
           parts=[types.Part(text="You are a robot controller. Use tools to execute commands.")]
       ),
   )
   async with client.aio.live.connect(model=MODEL, config=config) as session:
       recv_task = asyncio.create_task(receive_loop(session))
       # Connect robot perception callbacks and user inputs to the helpers above.
       recv_task.cancel()

asyncio.run(main())
```

La boucle de réception reste active après chaque réponse de l'outil. Le modèle construit et révise un plan à long terme sans que vous ayez à encoder toute la séquence d'actions à l'avance.

## Raisonnement spatio-temporel proactif

L'API Live diffuse des vidéos, mais les images vidéo seules ne déclenchent pas de nouveau tour de raisonnement. Les images vidéo doivent être accompagnées d'une requête textuelle ou audio pour déclencher une réponse du modèle. Pour en savoir plus, consultez [Fonctionnalités de l'API Live](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=fr).

Pour activer le raisonnement proactif, implémentez un **signal de présence** : envoyez régulièrement la dernière image de la caméra, suivie d'un court prompt textuel qui force le modèle à inspecter la scène et à prendre une décision explicite. L'entrée vidéo est limitée à une image par seconde.

### Implémenter le signal de pulsation

La coroutine heartbeat s'exécute en tant que tâche `asyncio` distincte dans la même session.
Il cible de manière opportuniste une cadence de 1 Hz (correspondant à la limite de fréquence d'entrée vidéo) en attendant la fin de chaque tour (`er_turn_done`) pour éviter d'interrompre le raisonnement en cours :

```
async def heartbeat(session, camera, er_turn_done: asyncio.Event):
    TARGET_INTERVAL_SEC = 1.0

    while True:
        start_time = asyncio.get_running_loop().time()

        frame = await camera.latest_jpeg()
        await session.send_realtime_input(
            video=types.Blob(data=frame, mime_type="image/jpeg")
        )
        await session.send_realtime_input(
            text=(
                "[HEARTBEAT] If no task is active, call 'ack' and wait for user"
                " input. If a task is active: observe the scene. If the current"
                " step is progressing correctly, call 'ack'. If the current step"
                " is complete, call 'run_instruction' with the next step. If the"
                " overall goal is achieved, call 'reset' and inform the user."
            )
        )

        # Wait for the model to finish responding before sending the next heartbeat
        await er_turn_done.wait()
        er_turn_done.clear()

        # Sleep only the remaining time to maintain ~1 Hz cadence
        elapsed = asyncio.get_running_loop().time() - start_time
        remaining = TARGET_INTERVAL_SEC - elapsed
        if remaining > 0:
            await asyncio.sleep(remaining)
```

### Mettre à jour la boucle de réception

Pour indiquer que le modèle a terminé son tour, mettez à jour votre `receive_loop` pour définir `er_turn_done` :

```
# In receive_loop: signal when the model finishes its turn
if sc.turn_complete:
    er_turn_done.set()
```

## Sortie audio via un système TTS externe

Gemini Robotics ER 2 renvoie du texte. Votre application achemine les réponses complètes vers un fournisseur de synthèse vocale distinct (tel que [Gemini TTS](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fr)) via un rappel injecté.
Cela vous permet de contrôler la latence vocale, la sélection de la voix et le comportement d'interruption, et d'échanger les backends de synthèse vocale sans modifier la logique de l'agent.

Vous pouvez également déclarer la synthèse vocale comme un outil afin que le modèle traite "dis quelque chose" de la même manière que "bouge le bras". Ajoutez la déclaration de fonction suivante à votre liste `tools` de la première section :

```
TOOLS = [
    {
        "name": "send_message",
        "description": (
            "Speak a message aloud via TTS, then deliver it to the"
            " specified target. Use target='user' to speak directly"
            " to the user, or a peer agent name (e.g., 'duo') to"
            " communicate with another robot."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Recipient: 'user' or a peer agent name.",
                },
                "message": {
                    "type": "string",
                    "description": "The message to speak and deliver.",
                },
            },
            "required": ["target", "message"],
        },
    },
]
```

En encapsulant la synthèse vocale dans une déclaration de fonction, le modèle gère la parole via le même chemin d'appel d'outil que toute autre action du robot. Votre application traite l'appel avec un rappel injecté.

## Exemples sur GitHub

Pour obtenir des exemples fonctionnels complets, y compris la démonstration de récupération de snacks par le robot Spot et le bonjour du Tinybot avec panoramique et inclinaison, consultez les [exemples d'API Robotics Live](https://github.com/google-gemini/robotics-samples/tree/main/live-api).

## Étape suivante

- [Compréhension des vidéos](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fr) : recherche de moments et classification de la progression.
- [Orchestration des tâches](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=fr) : tâches à long terme sans streaming.
- [Présentation de l'API Live](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=fr) : documentation complète de l'API Live.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/16 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/16 (UTC)."],[],[]]
