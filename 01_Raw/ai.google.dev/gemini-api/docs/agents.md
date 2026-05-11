---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=it
fetched_at: 2026-05-11T05:02:59.138755+00:00
title: "Panoramica degli agenti \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Panoramica degli agenti

Gli agenti sono sistemi che sfruttano i modelli Gemini, un insieme di strumenti e capacità di ragionamento per svolgere attività complesse in più passaggi e raggiungere obiettivi specifici. A differenza di una singola chiamata di modello, un agente può pianificare, eseguire una serie di azioni, interagire con sistemi esterni e sintetizzare le informazioni per soddisfare la richiesta di un utente.

Con l'API Gemini, puoi creare agenti potenti utilizzando funzionalità come:

- **[Modelli Gemini](https://ai.google.dev/gemini-api/docs/models?hl=it):** l'intelligenza di base,
  che fornisce ragionamento e comprensione del linguaggio.
- **[Strumenti](https://ai.google.dev/gemini-api/docs/tools?hl=it):** funzionalità che collegano il modello a
  informazioni e azioni del mondo reale. Questi possono essere strumenti integrati (come la Ricerca Google, Maps, Esecuzione di codice) o strumenti personalizzati.
- **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it):** il meccanismo per
  definire e connettere le tue API e i tuoi strumenti personalizzati al modello Gemini.
- **[Ragionamento](https://ai.google.dev/gemini-api/docs/thinking?hl=it):** funzionalità che migliorano la capacità del modello di ragionare e pianificare attività complesse.
- **[Contesto lungo](https://ai.google.dev/gemini-api/docs/long-context?hl=it):** consente agli agenti di
  mantenere lo stato e le informazioni durante interazioni prolungate.

## Agenti disponibili

- **[Agente Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it):** un agente autonomo
  che pianifica, esegue e sintetizza attività di ricerca in più fasi per
  casi d'uso come analisi di mercato, due diligence e revisioni della letteratura.

## Creare agenti

Gli agenti utilizzano modelli e strumenti per completare attività in più passaggi. Sebbene Gemini fornisca
le funzionalità di ragionamento (il "cervello") e gli strumenti essenziali (le "mani"),
spesso è necessario un framework di orchestrazione per gestire la memoria dell'agente, pianificare
i loop ed eseguire un concatenamento complesso di strumenti.

Per massimizzare l'affidabilità nei flussi di lavoro in più passaggi, devi creare istruzioni
che controllino esplicitamente il modo in cui il modello ragiona e pianifica. Anche se Gemini fornisce
un ragionamento generale solido, gli agenti complessi traggono vantaggio da prompt che impongono
comportamenti specifici come la persistenza di fronte ai problemi, la valutazione del rischio e
la pianificazione proattiva.

Consulta i [flussi di lavoro
agentici](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it#agentic-workflows) per
strategie sulla progettazione di questi prompt. Ecco un esempio di [istruzione
di sistema](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=it#agentic-si-template) che ha
migliorato le prestazioni in diversi benchmark agentici di circa il 5%.

## Framework degli agenti

Gemini si integra con i principali framework di agenti open source, ad esempio:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=it): crea flussi di applicazioni complessi e con stato e sistemi multi-agente utilizzando strutture grafiche.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=it): collega gli agenti Gemini ai tuoi dati privati per flussi di lavoro migliorati con RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=it): orchestra agenti AI autonomi collaborativi
  che interpretano ruoli.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=it): crea
  interfacce utente e agenti basati sull'AI in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): un framework
  open source per la creazione e l'orchestrazione di agenti di IA
  interoperabili.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
