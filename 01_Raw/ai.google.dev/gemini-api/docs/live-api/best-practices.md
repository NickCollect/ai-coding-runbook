---
source_url: https://ai.google.dev/gemini-api/docs/live-api/best-practices?hl=fr
fetched_at: 2026-08-10T03:18:51.398701+00:00
title: "Bonnes pratiques concernant l'API Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Bonnes pratiques concernant l'API Live

Ce guide présente les bonnes pratiques à suivre pour optimiser votre utilisation de l'API Live.
Consultez la page [Premiers pas avec l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr) pour obtenir une présentation et des exemples de code pour les cas d'utilisation courants.

## Concevoir des instructions système claires

Pour obtenir les meilleures performances de l'API Live, nous vous recommandons de définir clairement un ensemble d'instructions système (IS) qui définissent la personnalité de l'agent, les règles de conversation et les garde-fous, dans cet ordre.

Pour de meilleurs résultats, séparez chaque agent dans un SI distinct.

1. **Spécifiez le persona de l'agent** : fournissez des informations sur le nom, le rôle et les caractéristiques préférées de l'agent. Si vous souhaitez spécifier l'accent, veillez également à indiquer la langue de sortie souhaitée (par exemple, un accent britannique pour un locuteur anglophone).
2. **Spécifiez les règles de conversation** : placez ces règles dans l'ordre dans lequel vous souhaitez que le modèle les suive. Faites la distinction entre les éléments ponctuels de la conversation et les boucles conversationnelles. Exemple :

   - **Élément ponctuel** : collectez les informations d'un client une seule fois (nom, localisation, numéro de carte de fidélité, etc.).
   - **Boucle conversationnelle** : l'utilisateur peut discuter des recommandations, des prix, des retours et de la livraison, et peut vouloir passer d'un sujet à l'autre. Indiquez au modèle qu'il peut s'engager dans cette boucle de conversation aussi longtemps que l'utilisateur le souhaite.
3. **Spécifiez les appels d'outil dans un flux dans des phrases distinctes** : par exemple, si une étape ponctuelle pour recueillir les informations d'un client nécessite d'appeler une fonction `get_user_info`, vous pouvez dire : *Votre première étape consiste à recueillir les informations de l'utilisateur. Tout d'abord, demandez à l'utilisateur de fournir son nom, sa position et son numéro de carte de fidélité. Ensuite, appelez `get_user_info` avec ces informations.*
4. ***Ajoutez les garde-fous nécessaires** : fournissez tous les garde-fous conversationnels généraux que vous ne souhaitez pas que le modèle applique. N'hésitez pas à fournir des exemples spécifiques de ce que vous souhaitez que le modèle fasse si *x* se produit.* Si vous n'obtenez toujours pas le niveau de précision souhaité, utilisez le mot *incontestablement* pour guider le modèle vers la précision.

## Définir précisément les outils

Lorsque vous utilisez des outils avec l'API Live, soyez précis dans vos définitions d'outils.
Veillez à indiquer à Gemini dans quelles conditions un appel d'outil doit être invoqué. Pour en savoir plus, consultez [Définitions des outils](#tool-definitions-example) dans la section des exemples.

## Rédiger des requêtes efficaces

- **Utilisez des requêtes claires** : fournissez des exemples de ce que les modèles doivent et ne doivent pas faire dans les requêtes, et essayez de limiter les requêtes à une par persona ou rôle à la fois. Au lieu d'utiliser des requêtes longues et multipages, pensez plutôt à utiliser l'enchaînement de requêtes. Le modèle est plus performant pour les tâches avec des appels de fonction uniques.
- **Fournissez des commandes et des informations de départ** : l'API Live attend une entrée utilisateur avant de répondre. Pour que l'API Live lance la conversation, incluez une requête lui demandant de saluer l'utilisateur ou de commencer la conversation. Incluez des informations sur l'utilisateur pour que l'API Live puisse personnaliser le message d'accueil.

## Spécifier la langue

Pour des performances optimales sur les `gemini-live-2.5-flash` en cascade de l'API Live, assurez-vous que le `language_code` de l'API correspond à la langue parlée par l'utilisateur.

Si vous attendez du modèle qu'il réponde dans une langue autre que l'anglais, incluez les éléments suivants dans vos instructions système :

```
RESPOND IN {OUTPUT_LANGUAGE}. YOU MUST RESPOND UNMISTAKABLY IN {OUTPUT_LANGUAGE}.
```

## Streaming

Lorsque vous implémentez l'audio en temps réel, suivez ces bonnes pratiques :

- **Taille des fragments et latence** : envoyez l'audio par fragments de 20 à 40 ms.
- **Gestion des interruptions** : lorsque l'utilisateur parle pendant que le modèle répond, le serveur envoie un message `server_content` avec `"interrupted": true`. Vous devez immédiatement supprimer votre tampon audio côté client pour empêcher l'agent de continuer à parler par-dessus l'utilisateur.

## Gestion du contexte

Utilisez `ContextWindowCompressionConfig` pour les longues sessions, car les jetons audio natifs s'accumulent rapidement (environ 25 jetons par seconde d'audio).

## Mise en mémoire tampon côté client

N'effectuez pas de mise en mémoire tampon importante de l'audio d'entrée (par exemple, une seconde) avant de l'envoyer. Envoyez de petits blocs (20 à 100 ms) pour minimiser la latence.

## Rééchantillonnage

Assurez-vous que votre application cliente rééchantillonne l'entrée du micro (souvent 44,1 kHz ou 48 kHz) à 16 kHz avant la transmission.

## Gestion de la session

Suivez ces consignes pour gérer le cycle de vie des sessions et garantir une expérience utilisateur fiable :

- **Activez la compression de la fenêtre de contexte** : les jetons audio s'accumulent à environ 25 jetons par seconde. Sans compression, les sessions audio uniquement sont limitées à 15 minutes et les sessions audio-vidéo à 2 minutes. Activez la [compression de la fenêtre de contexte](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr#context-window-compression) pour étendre les sessions à une durée illimitée.
- **Implémentez la reprise de session** : le serveur peut réinitialiser périodiquement la connexion WebSocket. Utilisez la [reprise de session](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr#session-resumption) pour vous reconnecter facilement sans perdre le contexte. Conservez le dernier jeton de reprise des messages `SessionResumptionUpdate` et transmettez-le en tant que handle lors de la reconnexion. Les jetons de reprise sont valides pendant deux heures après la fin de la dernière session.
- **Gérer les messages GoAway** : le serveur envoie un message [GoAway](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr#goaway-message) avant de mettre fin à une connexion. Écoutez ce message et utilisez le champ `timeLeft` pour terminer ou rétablir la connexion en douceur avant qu'elle ne se ferme.
- **Gérez les signaux generationComplete** : utilisez le message [`generationComplete`](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr#generation-complete-message) pour savoir quand le modèle a fini de générer une réponse, afin que votre application puisse mettre à jour son UI ou passer à l'action suivante.

Pour en savoir plus sur l'implémentation, consultez [Gestion des sessions](https://ai.google.dev/gemini-api/docs/live-api/session-management?hl=fr).

## Exemples

Cet exemple combine les bonnes pratiques et les [consignes pour la conception d'instructions système](#system-instruction-guidelines) afin de guider les performances du modèle en tant que coach de carrière.

```
**Persona:**
You are Laura, a career coach from Brooklyn, NY. You specialize in providing
data driven advice to give your clients a fresh perspective on the career
questions they're navigating. Your special sauce is providing quantitative,
data-driven insights to help clients think about their issues in a different
way. You leverage statistics, research, and psychology as much as possible.
You only speak to your clients in English, no matter what language they speak
to you in.

**Conversational Rules:**

1. **Introduce yourself:** Warmly greet the client.

2. **Intake:** Ask for your client's full name, date of birth, and state they're
calling in from. Call `create_client_profile` to create a new patient profile.

3. **Discuss the client's issue:** Get a sense of what the client wants to
cover in the session. DO NOT repeat what the client is saying back to them in
your response. Don't ask more than a few questions here.

4. **Reframe the client's issue with real data:** NO PLATITUDES. Start providing
data-driven insights for the client, but embed these as general facts within
conversation. This is what they're coming to you for: your unique thinking on
the subjects that are stressing them out. Show them a new way of thinking about
something. Let this step go on for as long as the client wants. As part of this,
if the client mentions wanting to take any actions, update
`add_action_items_to_profile` to remind the client later.

5. **Next appointment:** Call `get_next_appointment` to see if another
appointment has already been scheduled for the client. If so, then share the
date and time with the client and confirm if they'll be able to attend. If
there is no appointment, then call `get_available_appointments` to see openings.
Share the list of openings with the client and ask what they would prefer. Save
their preference with `schedule_appointment`. If the client prefers to schedule
offline, then let them know that's perfectly fine and to use the patient portal.

**General Guidelines:** You're meant to be a witty, snappy conversational
partner. Keep your responses short and progressively disclose more information
if the client requests it. Don't repeat back what the client says back to them.
Each response you give should be a net new addition to the conversation, not a
recap of what the client said. Be relatable by bringing in your own background 
growing up professionally in Brooklyn, NY. If a client tries to get you off
track, gently bring them back to the workflow articulated above.

**Guardrails:** If the client is being hard on themselves, never encourage that.
Remember that your ultimate goal is to create a supportive environment for your
clients to thrive.
```

### Définitions d'outils

Ce JSON définit les fonctions pertinentes appelées dans l'exemple de conseiller professionnel.
Pour obtenir les meilleurs résultats lorsque vous définissez des fonctions, incluez leur nom, leur description, leurs paramètres et leurs conditions d'appel.

```
[
 {
   "name": "create_client_profile",
   "description": "Creates a new client profile with their personal details. Returns a unique client ID. \n**Invocation Condition:** Invoke this tool *only after* the client has provided their full name, date of birth, AND state. This should only be called once at the beginning of the 'Intake' step.",
   "parameters": {
     "type": "object",
     "properties": {
       "full_name": {
         "type": "string",
         "description": "The client's full name."
       },
       "date_of_birth": {
         "type": "string",
         "description": "The client's date of birth in YYYY-MM-DD format."
       },
       "state": {
         "type": "string",
         "description": "The 2-letter postal abbreviation for the client's state (e.g., 'NY', 'CA')."
       }
     },
     "required": ["full_name", "date_of_birth", "state"]
   }
 },
 {
   "name": "add_action_items_to_profile",
   "description": "Adds a list of actionable next steps to a client's profile using their client ID. \n**Invocation Condition:** Invoke this tool *only after* a list of actionable next steps has been discussed and agreed upon with the client during the 'Actions' step. Requires the `client_id` obtained from the start of the session.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client, obtained from create_client_profile."
       },
       "action_items": {
         "type": "array",
         "items": {
           "type": "string"
         },
         "description": "A list of action items for the client (e.g., ['Update resume', 'Research three companies'])."
       }
     },
     "required": ["client_id", "action_items"]
   }
 },
 {
   "name": "get_next_appointment",
   "description": "Checks if a client has a future appointment already scheduled using their client ID. Returns the appointment details or null. \n**Invocation Condition:** Invoke this tool at the *start* of the 'Next Appointment' workflow step, immediately after the 'Actions' step is complete. This is used to check if an appointment *already exists*.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       }
     },
     "required": ["client_id"]
   }
 },
 {
   "name": "get_available_appointments",
   "description": "Fetches a list of the next available appointment slots. \n**Invocation Condition:** Invoke this tool *only if* the `get_next_appointment` tool was called and it returned `null` (or an empty response), indicating no future appointment is scheduled.",
   "parameters": {
     "type": "object",
     "properties": {}
   }
 },
 {
   "name": "schedule_appointment",
   "description": "Books a new appointment for a client at a specific date and time. \n**Invocation Condition:** Invoke this tool *only after* `get_available_appointments` has been called, a list of openings has been presented to the client, and the client has *explicitly confirmed* which specific date and time they want to book.",
   "parameters": {
     "type": "object",
     "properties": {
       "client_id": {
         "type": "string",
         "description": "The unique ID of the client."
       },
       "appointment_datetime": {
         "type": "string",
         "description": "The chosen appointment slot in ISO 8601 format (e.g., '2025-10-30T14:30:00')."
       }
     },
     "required": ["client_id", "appointment_datetime"]
   }
 }
]
```

## Tarification et facturation

L'API Gemini Live est facturée strictement en fonction de l'utilisation de jetons. Étant donné que l'API Live maintient une session WebSocket persistante, la facturation suit un modèle composé basé sur la fenêtre de contexte active.

### Fenêtre de contexte de session (coûts cumulés)

L'API vous facture chaque tour pour tous les jetons présents dans la fenêtre de contexte de la session. Un "tour" est défini comme une entrée utilisateur et la réponse correspondante du modèle.

- **Accumulation** : la fenêtre de contexte inclut les nouveaux jetons du tour actuel, ainsi que tous les jetons accumulés des tours précédents.
- **Refacturation** : les jetons précédents sont retraités et pris en compte à chaque nouveau tour, jusqu'à la taille de la fenêtre de contexte que vous avez configurée. À mesure qu'une session s'allonge, le coût par tour augmente, car l'historique des conversations est retraité.

### Jetons audio et transcriptions

L'API Live est nativement multimodale. Il conserve l'historique des conversations sous forme de jetons audio bruts pour préserver les nuances et le ton acoustiques.

- **Facturation audio** : l'API vous facture les jetons audio natifs cumulés au tarif standard des entrées audio à chaque tour.
- **Frais supplémentaires de transcription** : lorsque la transcription audio en texte est activée (`inputAudioTranscription` ou `outputAudioTranscription`), l'API facture tous les jetons de texte générés pour la transcription au tarif des jetons de texte de sortie, en plus des coûts standard des jetons audio.

### Gérer les coûts avec les limites de contexte

Pour éviter une croissance illimitée des coûts lors de longues sessions, configurez la taille de votre fenêtre de contexte à l'aide de `contextWindowCompression`.

En définissant un déclencheur de compression (par exemple, 25 000 jetons) et une fenêtre glissante (par exemple, 8 000 jetons), l'API supprime automatiquement les jetons les plus anciens une fois le seuil atteint. L'API facture ensuite les tours suivants uniquement pour l'historique conservé et les nouveaux jetons.

### Mode audio proactif

Lorsque le mode audio proactif est activé, les jetons d'entrée sont facturés pendant toute la durée d'écoute de l'API Live, tandis que les jetons de sortie ne sont facturés que lorsque l'API répond.

- **Remarque concernant Gemini 3.1** : Le mode audio proactif n'est pas compatible avec `gemini-3.1-flash-live-preview`. Pour ce modèle, vous n'êtes facturé pour l'audio que lorsque vous diffusez activement des entrées.

Pour en savoir plus sur les tarifs, consultez la [page des tarifs de l'API Gemini](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/01 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/01 (UTC)."],[],[]]
