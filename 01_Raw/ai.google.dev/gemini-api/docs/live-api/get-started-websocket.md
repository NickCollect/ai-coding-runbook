---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=fr
fetched_at: 2026-06-22T06:31:28.893979+00:00
title: "Premiers pas avec l'API Gemini\u00a0Live \u00e0 l'aide de WebSockets \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Premiers pas avec l'API Gemini Live à l'aide de WebSockets

L'API Gemini Live permet une interaction bidirectionnelle en temps réel avec les modèles Gemini, et accepte les entrées audio, vidéo et texte, ainsi que les sorties audio natives. Ce guide explique comment intégrer directement l'API à l'aide de WebSockets bruts.

[Essayez l'API Live dans Google AI Studiomic](https://aistudio.google.com/live?hl=fr)
[Cloner l'exemple d'application depuis GitHubcode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-ephemeral-tokens-websocket)
[Utiliser les compétences de l'agent de codageterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=fr)

## Présentation

L'API Gemini Live utilise WebSockets pour la communication en temps réel. Contrairement à l'utilisation d'un SDK, cette approche implique de gérer directement la connexion WebSocket et d'envoyer/recevoir des messages dans un format JSON spécifique défini par l'API.

Concepts clés :

- **Point de terminaison WebSocket** : URL spécifique à laquelle se connecter.
- **Format des messages** : toutes les communications sont effectuées via des messages JSON conformes aux structures [`BidiGenerateContentClientMessage`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentclientmessage) et [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentservermessage).
- **Gestion des sessions** : vous êtes responsable de la maintenance de la connexion WebSocket.

## Authentification

L'authentification est gérée en incluant votre clé API en tant que paramètre de requête dans l'URL WebSocket.

Le format du point de terminaison est le suivant :

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY
```

Remplacez `YOUR_API_KEY` par votre clé API réelle.

## Authentification avec des jetons éphémères

Si vous utilisez des [jetons éphémères](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=fr), vous devez vous connecter au point de terminaison `v1alpha`.
Le jeton éphémère doit être transmis en tant que paramètre de requête `access_token`.

Le format du point de terminaison pour les clés éphémères est le suivant :

```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContentConstrained?access_token={short-lived-token}
```

Remplacez `{short-lived-token}` par le jeton éphémère réel.

## Se connecter à l'API Live

Pour démarrer une session en direct, établissez une connexion WebSocket au point de terminaison authentifié.
Le premier message envoyé via WebSocket doit être un [`BidiGenerateContentSetup`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentsetup) contenant la `config`.
Pour obtenir la liste complète des options de configuration, consultez la documentation de référence de l'API [Live - WebSockets](https://ai.google.dev/api/live?hl=fr).

### Python

```
import asyncio
import websockets
import json

API_KEY = "YOUR_API_KEY"
MODEL_NAME = "gemini-3.1-flash-live-preview"
WS_URL = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key={API_KEY}"

async def connect_and_configure():
    async with websockets.connect(WS_URL) as websocket:
        print("WebSocket Connected")

        # 1. Send the initial configuration
        setup_message = {
            "setup": {
                "model": f"models/{MODEL_NAME}",
                "responseModalities": ["AUDIO"],
                "systemInstruction": {
                    "parts": [{"text": "You are a helpful assistant."}]
                }
            }
        }
        await websocket.send(json.dumps(setup_message))
        print("Configuration sent")

        # Keep the session alive for further interactions
        await asyncio.sleep(3600) # Example: keep open for an hour

async def main():
    await connect_and_configure()

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.1-flash-live-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  // 1. Send the initial configuration
  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      responseModalities: ['AUDIO'],
      systemInstruction: {
        parts: [{ text: 'You are a helpful assistant.' }]
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
  console.log('Configuration sent');
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);
  // Handle different types of responses here
};

websocket.onerror = (error) => {
  console.error('WebSocket Error:', error);
};

websocket.onclose = () => {
  console.log('WebSocket Closed');
};
```

## Envoi d'un SMS…

Pour envoyer une entrée de texte, créez un [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentrealtimeinput) message avec le `text` champ.

### Python

```
# Inside the websocket context
async def send_text(websocket, text):
    text_message = {
        "realtimeInput": {
            "text": text
        }
    }
    await websocket.send(json.dumps(text_message))
    print(f"Sent text: {text}")

# Example usage: await send_text(websocket, "Hello, how are you?")
```

### JavaScript

```
function sendTextMessage(text) {
  if (websocket.readyState === WebSocket.OPEN) {
    const textMessage = {
      realtimeInput: {
        text: text
      }
    };
    websocket.send(JSON.stringify(textMessage));
    console.log('Text message sent:', text);
  } else {
    console.warn('WebSocket not open.');
  }
}

// Example usage:
sendTextMessage("Hello, how are you?");
```

## Envoi de l'audio

L'audio doit être envoyé sous forme de données PCM brutes (audio PCM 16 bits brut, 16 kHz, little-endian). Créez un [`BidiGenerateContentRealtimeInput`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentrealtimeinput) message avec les données audio. Le `mimeType` est essentiel.

### Python

```
# Inside the websocket context
async def send_audio_chunk(websocket, chunk_bytes):
    import base64
    encoded_data = base64.b64encode(chunk_bytes).decode('utf-8')
    audio_message = {
        "realtimeInput": {
            "audio": {
                "data": encoded_data,
                "mimeType": "audio/pcm;rate=16000"
            }
        }
    }
    await websocket.send(json.dumps(audio_message))
    # print("Sent audio chunk") # Avoid excessive logging

# Assuming 'chunk' is your raw PCM audio bytes
# await send_audio_chunk(websocket, chunk)
```

### JavaScript

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
    // console.log('Sent audio chunk');
  }
}
// Example usage: sendAudioChunk(audioBuffer);
```

Pour obtenir un exemple de récupération de l'audio à partir de l'appareil client (par exemple, le navigateur),
consultez l'exemple de bout en bout sur [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L38-L74).

## Envoi de la vidéo…

Les images vidéo sont envoyées sous forme d'images individuelles (par exemple, JPEG ou PNG). Comme pour l'audio, utilisez `realtimeInput` avec un `Blob`, en spécifiant le `mimeType` approprié.

### Python

```
# Inside the websocket context
async def send_video_frame(websocket, frame_bytes, mime_type="image/jpeg"):
    import base64
    encoded_data = base64.b64encode(frame_bytes).decode('utf-8')
    video_message = {
        "realtimeInput": {
            "video": {
                "data": encoded_data,
                "mimeType": mime_type
            }
        }
    }
    await websocket.send(json.dumps(video_message))
    # print("Sent video frame")

# Assuming 'frame' is your JPEG-encoded image bytes
# await send_video_frame(websocket, frame)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
function sendVideoFrame(frame, mimeType = 'image/jpeg') {
  if (websocket.readyState === WebSocket.OPEN) {
    const videoMessage = {
      realtimeInput: {
        video: {
          data: frame.toString('base64'),
          mimeType: mimeType
        }
      }
    };
    websocket.send(JSON.stringify(videoMessage));
    // console.log('Sent video frame');
  }
}
// Example usage: sendVideoFrame(jpegBuffer);
```

Pour obtenir un exemple de récupération de la vidéo à partir de l'appareil client (par exemple, le navigateur),
consultez l'exemple de bout en bout sur [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/mediaUtils.js#L185-L222).

## Recevoir les réponses

WebSocket renverra des [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentservermessage) messages. Vous devez analyser ces messages JSON et gérer différents types de contenu.

### Python

```
# Inside the websocket context, in a receive loop
async def receive_loop(websocket):
    async for message in websocket:
        response = json.loads(message)
        print("Received:", response)

        if "serverContent" in response:
            server_content = response["serverContent"]
            # Receiving Audio
            if "modelTurn" in server_content and "parts" in server_content["modelTurn"]:
                for part in server_content["modelTurn"]["parts"]:
                    if "inlineData" in part:
                        audio_data_b64 = part["inlineData"]["data"]
                        # Process or play the base64 encoded audio data
                        # audio_data = base64.b64decode(audio_data_b64)
                        print(f"Received audio data (base64 len: {len(audio_data_b64)})")

            # Receiving Text Transcriptions
            if "inputTranscription" in server_content:
                print(f"User: {server_content['inputTranscription']['text']}")
            if "outputTranscription" in server_content:
                print(f"Gemini: {server_content['outputTranscription']['text']}")

        # Handling Tool Calls
        if "toolCall" in response:
            await handle_tool_call(websocket, response["toolCall"])

# Example usage: await receive_loop(websocket)
```

### JavaScript

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  console.log('Received:', response);

  if (response.serverContent) {
    const serverContent = response.serverContent;
    // Receiving Audio
    if (serverContent.modelTurn?.parts) {
      for (const part of serverContent.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data; // Base64 encoded string
          // Process or play audioData
          console.log(`Received audio data (base64 len: ${audioData.length})`);
        }
      }
    }

    // Receiving Text Transcriptions
    if (serverContent.inputTranscription) {
      console.log('User:', serverContent.inputTranscription.text);
    }
    if (serverContent.outputTranscription) {
      console.log('Gemini:', serverContent.outputTranscription.text);
    }
  }

  // Handling Tool Calls
  if (response.toolCall) {
    handleToolCall(response.toolCall);
  }
};
```

Pour obtenir un exemple de gestion de la réponse, consultez l'exemple de bout en bout sur [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-ephemeral-tokens-websocket/frontend/geminilive.js#L22-L75).

## Gérer les appels d'outils

Lorsque le modèle demande un appel d'outil, le [`BidiGenerateContentServerMessage`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontentservermessage) contient un champ `toolCall`. Vous devez exécuter la fonction localement et renvoyer le résultat à WebSocket à l'aide d'un [`BidiGenerateContentToolResponse`](https://ai.google.dev/api/live?hl=fr#bidigeneratecontenttoolresponse) message.

### Python

```
# Placeholder for your tool function
def my_tool_function(args):
    print(f"Executing tool with args: {args}")
    # Implement your tool logic here
    return {"status": "success", "data": "some result"}

async def handle_tool_call(websocket, tool_call):
    function_responses = []
    for fc in tool_call["functionCalls"]:
        # 1. Execute the function locally
        try:
            result = my_tool_function(fc.get("args", {}))
            response_data = {"result": result}
        except Exception as e:
            print(f"Error executing tool {fc['name']}: {e}")
            response_data = {"error": str(e)}

        # 2. Prepare the response
        function_responses.append({
            "name": fc["name"],
            "id": fc["id"],
            "response": response_data
        })

    # 3. Send the tool response back to the session
    tool_response_message = {
        "toolResponse": {
            "functionResponses": function_responses
        }
    }
    await websocket.send(json.dumps(tool_response_message))
    print("Sent tool response")

# This function is called within the receive_loop when a toolCall is detected.
```

### JavaScript

```
// Placeholder for your tool function
function myToolFunction(args) {
  console.log(`Executing tool with args:`, args);
  // Implement your tool logic here
  return { status: 'success', data: 'some result' };
}

function handleToolCall(toolCall) {
  const functionResponses = [];
  for (const fc of toolCall.functionCalls) {
    // 1. Execute the function locally
    let result;
    try {
      result = myToolFunction(fc.args || {});
    } catch (e) {
      console.error(`Error executing tool ${fc.name}:`, e);
      result = { error: e.message };
    }

    // 2. Prepare the response
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }

  // 3. Send the tool response back to the session
  if (websocket.readyState === WebSocket.OPEN) {
    const toolResponseMessage = {
      toolResponse: {
        functionResponses: functionResponses
      }
    };
    websocket.send(JSON.stringify(toolResponseMessage));
    console.log('Sent tool response');
  } else {
    console.warn('WebSocket not open to send tool response.');
  }
}
// This function is called within websocket.onmessage when a toolCall is detected.
```

## Étape suivante

- Consultez le guide complet sur les fonctionnalités de l'API Live [Fonctionnalités](https://ai.google.dev/gemini-api/docs/live-guide?hl=fr) pour découvrir les principales fonctionnalités et configurations, y compris la détection d'activité vocale et les fonctionnalités audio natives.
- Consultez le [guide sur l'utilisation des outils](https://ai.google.dev/gemini-api/docs/live-tools?hl=fr) pour découvrir comment intégrer l'API Live aux outils et aux appels de fonction.
- Consultez le [guide sur la gestion des sessions](https://ai.google.dev/gemini-api/docs/live-session?hl=fr) pour gérer les conversations de longue durée.
- Consultez le guide sur les [jetons éphémères](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=fr) pour une authentification sécurisée dans les applications [client-serveur](#implementation-approach).
- Pour en savoir plus sur l'API WebSockets sous-jacente, consultez la [documentation de référence de l'API WebSockets](https://ai.google.dev/api/live?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/09 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/09 (UTC)."],[],[]]
