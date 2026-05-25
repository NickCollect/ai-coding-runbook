---
source_url: https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=fr
fetched_at: 2026-05-25T05:23:56.095924+00:00
title: "Ephemeral tokens \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Ephemeral tokens

Les jetons éphémères sont des jetons d'authentification de courte durée permettant d'accéder à l'API Gemini
via [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Ils sont conçus pour améliorer la sécurité lorsque
vous vous connectez directement à l'API depuis l'appareil d'un utilisateur (une
[implémentation client-serveur](https://ai.google.dev/gemini-api/docs/live?hl=fr#implementation-approach)
). Comme les clés API standards, les jetons éphémères peuvent être extraits d'applications côté client telles que des navigateurs Web ou des applications mobiles. Toutefois, comme ils expirent rapidement et peuvent être limités, ils réduisent considérablement les risques de sécurité dans un environnement de production. Vous devez les utiliser lorsque vous accédez directement à l'API Live à partir d'applications côté client pour améliorer la sécurité des clés API.

 

## Fonctionnement des jetons éphémères

Voici comment fonctionnent les jetons éphémères de manière générale :

1. Votre client (par exemple, une application Web) s'authentifie auprès de votre backend.
2. Votre backend demande un jeton éphémère au service de provisionnement de l'API Gemini.
3. L'API Gemini émet un jeton de courte durée.
4. Votre backend envoie le jeton au client pour les connexions WebSocket à l'API Live. Pour ce faire, vous pouvez remplacer votre clé API par un jeton éphémère.
5. Le client utilise ensuite le jeton comme s'il s'agissait d'une clé API.

![Présentation des jetons éphémères](https://ai.google.dev/static/gemini-api/docs/images/Live_API_01.png?hl=fr)

Cela améliore la sécurité, car même s'il est extrait, le jeton est de courte durée, contrairement à une clé API de longue durée déployée côté client. Comme le client envoie des données directement à Gemini, cela améliore également la latence et évite que vos backends n'aient à proxyfier les données en temps réel.

## Créer un jeton éphémère

Voici un exemple simplifié de la façon d'obtenir un jeton éphémère de Gemini.
Par défaut, vous disposez d'une minute pour démarrer de nouvelles sessions de l'API Live à l'aide du jeton de cette requête (`newSessionExpireTime`) et de 30 minutes pour envoyer des messages via cette connexion (`expireTime`).

### Python

```
import datetime

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1, # The ephemeral token can only be used to start a single session
    'expire_time': now + datetime.timedelta(minutes=30), # Default is 30 minutes in the future
    # 'expire_time': '2025-05-17T00:00:00Z',   # Accepts isoformat.
    'new_session_expire_time': now + datetime.timedelta(minutes=1), # Default 1 minute in the future
    'http_options': {'api_version': 'v1alpha'},
  }
)

# You'll need to pass the value under token.name back to your client to use it
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

  const token: AuthToken = await client.authTokens.create({
    config: {
      uses: 1, // The default
      expireTime: expireTime, // Default is 30 mins
      newSessionExpireTime: new Date(Date.now() + (1 * 60 * 1000)), // Default 1 minute in the future
      httpOptions: {apiVersion: 'v1alpha'},
    },
  });
```

Pour connaître les contraintes de valeur, les valeurs par défaut et les autres spécifications de champ de `expireTime`, consultez la
[documentation de référence de l'API](https://ai.google.dev/api/live?hl=fr#ephemeral-auth-tokens).
Dans le délai `expireTime`, vous aurez besoin
[`sessionResumption`](https://ai.google.dev/gemini-api/docs/live-session?hl=fr#session-resumption) pour
reconnecter l'appel toutes les 10 minutes (cela peut être fait avec le même jeton même
si `uses: 1`).

Il est également possible de verrouiller un jeton éphémère sur un ensemble de configurations. Cela peut être utile pour améliorer davantage la sécurité de votre application et conserver les instructions de votre système côté serveur.

### Python

```
client = genai.Client(
    http_options={'api_version': 'v1alpha',}
)

token = client.auth_tokens.create(
    config = {
    'uses': 1,
    'live_connect_constraints': {
        'model': 'gemini-3.1-flash-live-preview',
        'config': {
            'session_resumption':{},
            'temperature':0.7,
            'response_modalities':['AUDIO']
        }
    },
    'http_options': {'api_version': 'v1alpha'},
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
            model: 'gemini-3.1-flash-live-preview',
            config: {
                sessionResumption: {},
                temperature: 0.7,
                responseModalities: ['AUDIO']
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    }
});

// You'll need to pass the value under token.name back to your client to use it
```

Vous pouvez également verrouiller un sous-ensemble de champs. Pour en savoir plus, consultez la [documentation du SDK](https://googleapis.github.io/python-genai/genai.html#genai.types.CreateAuthTokenConfig.lock_additional_fields)
.

## Se connecter à l'API Live avec un jeton éphémère

Une fois que vous disposez d'un jeton éphémère, vous l'utilisez comme s'il s'agissait d'une clé API (mais n'oubliez pas qu'il ne fonctionne que pour l'API Live et uniquement avec la version `v1alpha` de l'API).

L'utilisation de jetons éphémères n'est utile que lors du déploiement d'applications
qui suivent une approche d'implémentation [client-serveur](https://ai.google.dev/gemini-api/docs/live?hl=fr#implementation-approach).

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

// Use the token generated in the "Create an ephemeral token" section here
const ai = new GoogleGenAI({
  apiKey: token.name
});
const model = 'gemini-3.1-flash-live-preview';
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
- Vérifiez l'authentification sécurisée de votre propre backend. Les jetons éphémères ne seront sécurisés que si votre méthode d'authentification backend l'est également.
- En règle générale, évitez d'utiliser des jetons éphémères pour les connexions backend-Gemini, car ce chemin est généralement considéré comme sécurisé.

## Limites

Pour le moment, les jetons éphémères ne sont compatibles qu'avec l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=fr).

## Étape suivante

- Pour en savoir plus, consultez la documentation de référence de l'API Live [reference](https://ai.google.dev/api/live?hl=fr#ephemeral-auth-tokens)
  sur les jetons éphémères.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/13 (UTC)."],[],[]]
