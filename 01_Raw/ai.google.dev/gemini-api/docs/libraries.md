---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=it
fetched_at: 2026-08-17T02:27:42.971229+00:00
title: "Librerie API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Librerie API Gemini

Quando crei con l'API Gemini, ti consigliamo di utilizzare l'**SDK Google GenAI**.
Si tratta delle librerie ufficiali e pronte per la produzione che sviluppiamo e gestiamo per i linguaggi più diffusi. Sono in [disponibilità generale](https://ai.google.dev/gemini-api/docs/libraries?hl=it#new-libraries) e vengono utilizzate in tutta la nostra documentazione ed esempi ufficiali.

Se non hai mai utilizzato l'API Gemini, consulta la nostra guida [Inizia](https://ai.google.dev/gemini-api/docs/get-started?hl=it) per iniziare.

## Supporto linguistico e installazione

L'SDK Google GenAI è disponibile per i linguaggi Python, JavaScript/TypeScript, Go e Java. Puoi installare la libreria di ogni linguaggio utilizzando i gestori di pacchetti o visitare i relativi repository GitHub per ulteriori informazioni:

### Python

- Libreria: [`google-genai`](https://pypi.org/project/google-genai)
- Repository GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Installazione: `pip install google-genai`

### JavaScript

- Libreria: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Repository GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Installazione: `npm install @google/genai`

### Vai

- Libreria: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Repository GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Installazione: `go get google.golang.org/genai`

### Java

- Libreria: `google-genai`
- Repository GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Installazione: se utilizzi Maven, aggiungi quanto segue alle dipendenze:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Libreria: `Google.GenAI`
- Repository GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Installazione: `dotnet add package Google.GenAI`

## Disponibilità generale

A partire da maggio 2025, l'SDK Google GenAI ha raggiunto la disponibilità generale (GA) su tutte le piattaforme supportate ed è la libreria consigliata per accedere all'API Gemini.
Sono stabili, completamente supportate per l'utilizzo in produzione e vengono gestite attivamente.
Forniscono l'accesso alle funzionalità più recenti e offrono le migliori prestazioni con Gemini.

Se utilizzi una delle nostre librerie precedenti, ti consigliamo vivamente di eseguire la migrazione per poter accedere alle funzionalità più recenti e ottenere le migliori prestazioni con Gemini. Per ulteriori informazioni, consulta la sezione [Librerie precedenti](https://ai.google.dev/gemini-api/docs/libraries?hl=it#previous-sdks).

## Librerie precedenti e migrazione

[Se utilizzi una delle nostre librerie precedenti, ti consigliamo di eseguire la migrazione alle nuove librerie.](https://ai.google.dev/gemini-api/docs/migrate?hl=it)

Le librerie precedenti non forniscono l'accesso alle funzionalità recenti (come
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=it) e [Veo](https://ai.google.dev/gemini-api/docs/video?hl=it)) e sono
ritirate a partire dal 30 novembre 2025.

Lo stato del supporto di ogni libreria precedente varia, come indicato nella tabella seguente:

| Lingua | Libreria precedente | Stato del supporto | Libreria consigliata |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Non gestita attivamente | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Non gestita attivamente | `@google/genai` |
| **Vai** | `google.golang.org/generative-ai` | Non gestita attivamente | `google.golang.org/genai` |
| **Dart e Flutter** | `google_generative_ai` | Non gestita attivamente | Utilizza [Genkit Dart](https://genkit.dev/docs/dart/get-started/) o [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Non gestita attivamente | Utilizza [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=it) |
| **Android** | `generative-ai-android` | Non gestita attivamente | Utilizza [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=it) |

**Nota per gli sviluppatori Java:** non esisteva un SDK Java fornito da Google per l'API Gemini, quindi non è necessaria la migrazione da una libreria Google precedente. Puoi iniziare direttamente con la nuova libreria nella
[sezione Supporto linguistico e installazione](#install).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-06-22 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-06-22 UTC."],[],[]]
