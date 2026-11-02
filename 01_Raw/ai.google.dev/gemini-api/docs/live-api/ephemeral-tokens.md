---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr
fetched_at: 2026-11-02T07:24:40.528372+00:00
title: "Jetons \u00e9ph\u00e9m\u00e8res \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon est désormais disponible. [À vous de jouer](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fr).

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Jetons éphémères

Les jetons éphémères sont des jetons d'authentification de courte durée permettant d'accéder à l'API Gemini via [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Elles sont conçues pour renforcer la sécurité lorsque vous vous connectez directement à l'API depuis l'appareil d'un utilisateur (une implémentation [client-serveur](https://ai.google.dev/gemini-api/docs/live?hl=fr#implementation-approach)). Comme les clés API standards, les jetons éphémères peuvent être extraits des applications côté client, telles que les navigateurs Web ou les applications mobiles. Toutefois, comme les jetons éphémères expirent rapidement et peuvent être limités, ils réduisent considérablement les risques de sécurité dans un environnement de production. Vous devez les utiliser lorsque vous accédez à l'API Live directement depuis des applications côté client pour renforcer la sécurité des clés API.

## Fonctionnement des jetons éphémères

Voici comment fonctionnent les jetons éphémères de manière générale :

1. Votre client (par exemple, une application Web) s'authentifie auprès de votre backend.
2. Votre backend demande un jeton éphémère au service de provisionnement de l'API Gemini.
3. L'API Gemini émet un jeton de courte durée.
4. Votre backend envoie le jeton au client pour les connexions WebSocket à l'API Live. Pour ce faire, remplacez votre clé API par un jeton éphémère.
5. Le client utilise ensuite le jeton comme s'il s'agissait d'une clé API.

![Présentation des jetons éphémères](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=fr)

Cela renforce la sécurité, car même s'il est extrait, le jeton est éphémère, contrairement à une clé API à longue durée de vie déployée côté client. Comme le client envoie les données directement à Gemini, cela améliore également la latence et évite à vos backends d'avoir à relayer les données en temps réel.

## Créer un jeton éphémère

Voici un exemple simplifié de la façon d'obtenir un jeton éphémère de Gemini.
Par défaut, vous disposez d'une minute pour démarrer de nouvelles sessions de l'API Live à l'aide du jeton de cette requête (`newSessionExpireTime`) et de 30 minutes pour envoyer des messages via cette connexion (`expireTime`).

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
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
    "newSessionExpireTime": "YYYY-MM-DDTHH:MM:SSZ"
  }'
```

Pour connaître les contraintes de valeur, les valeurs par défaut et les autres spécifications des champs `expireTime`, consultez la [documentation de référence de l'API](https://ai.google.dev/api/live?hl=fr#ephemeral-auth-tokens).
Dans le délai de `expireTime`, vous devrez [`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=fr#session-resumption) reconnecter l'appel toutes les 10 minutes (cela peut être fait avec le même jeton, même si `uses: 1`).

Il est également possible de verrouiller un jeton éphémère sur un ensemble de configurations. Cela peut être utile pour améliorer davantage la sécurité de votre application et conserver vos instructions système côté serveur.

### Python

```
from google import genai

client = genai.Client()

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.8-live',
        'config': {
            'session_resumption':{},
            'response_modalities':['AUDIO']
        }
    },
    }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1, // The default
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.8-live',
            config: {
                sessionResumption: {},
                responseModalities: ['AUDIO']
            }
        },
    }
});

// You'll need to pass the value under token.name back to your client to use it
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
      "model": "models/gemini-3.8-live",
      "config": {
        "sessionResumption": {},
        "responseModalities": ["AUDIO"]
      }
    }
  }'
```

Vous pouvez également verrouiller un sous-ensemble de champs. Pour en savoir plus, consultez la [documentation du SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields).

## Se connecter à l'API Live avec un jeton éphémère

Une fois que vous disposez d'un jeton éphémère, vous l'utilisez comme s'il s'agissait d'une clé API (mais n'oubliez pas qu'il ne fonctionne que pour l'API en direct et uniquement avec la version `v1beta` de l'API).

L'utilisation de jetons éphémères n'est utile que lors du déploiement d'applications qui suivent l'approche d'[implémentation client-serveur](https://ai.google.dev/gemini-api/docs/live?hl=fr#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.8-live';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: { ... },
  });

  // Send content...

  session.close();
}

main();
```

Pour obtenir d'autres exemples, consultez [Premiers pas avec l'API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

## Bonnes pratiques

- Définissez une courte durée d'expiration à l'aide du paramètre `expire_time`.
- Les jetons expirent, ce qui nécessite de relancer le processus de provisionnement.
- Validez l'authentification sécurisée pour votre propre backend. La sécurité des jetons éphémères dépendra uniquement de la sécurité de votre méthode d'authentification backend.
- En règle générale, évitez d'utiliser des jetons éphémères pour les connexions entre le backend et Gemini, car ce chemin est généralement considéré comme sécurisé.

## Limites

Les jetons éphémères ne sont compatibles qu'avec l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr) pour le moment.

## Étape suivante

- Pour en savoir plus, consultez la [documentation de référence](https://ai.google.dev/api/live?hl=fr#ephemeral-auth-tokens) de l'API Live sur les jetons éphémères.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/09/17 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/09/17 (UTC)."],[],[]]
