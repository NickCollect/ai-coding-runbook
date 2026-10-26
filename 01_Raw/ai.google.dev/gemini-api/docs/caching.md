---
source_url: https://ai.google.dev/gemini-api/docs/caching?hl=it
fetched_at: 2026-10-26T05:40:26.015202+00:00
title: "Memorizzazione nella cache del contesto \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Memorizzazione nella cache del contesto

In un tipico workflow di AI, potresti passare ripetutamente gli stessi token di input a un modello. L'API Gemini offre la memorizzazione nella cache implicita per ottimizzare le prestazioni e i costi.

## Memorizzazione nella cache implicita

La memorizzazione nella cache implicita è abilitata per impostazione predefinita per tutti i modelli Gemini 2.5 e versioni successive. È supportato sia per le modalità conversazionali [stateful](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#multi-turn-conversations) (utilizzando `previous_interaction_id`) sia per quelle [stateless](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#stateless-conversations).
Se la tua richiesta raggiunge le cache, ti trasferiamo automaticamente i risparmi sui costi. Non è necessario configurare nulla per attivarlo. La tabella seguente elenca il numero minimo di token di input per ogni modello:

| Modello | Limite minimo di token |
| --- | --- |
| Gemini 4 Argon | 4096 |
| Gemini 3.8 Flash | 4096 |
| Gemini 3.6 Flash | 4096 |
| Gemini 3.1 Pro (anteprima) | 4096 |
| Gemini 2.5 Flash | 2048 |
| Gemini 2.5 Pro | 2048 |

Per aumentare le probabilità di un successo della cache implicito:

- Prova a inserire contenuti di grandi dimensioni e comuni all'inizio del prompt
- Prova a inviare richieste con un prefisso simile in un breve periodo di tempo

Puoi visualizzare il numero di token che hanno generato successi della cache nel campo `usage.total_cached_tokens` (Python e JavaScript) dell'oggetto di risposta.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-23 UTC."],[],[]]
