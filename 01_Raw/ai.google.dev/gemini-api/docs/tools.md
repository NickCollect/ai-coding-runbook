---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=it
fetched_at: 2026-09-28T06:31:04.235236+00:00
title: "Utilizzo degli strumenti con l'API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Utilizzo degli strumenti con l'API Gemini

Gli strumenti estendono le funzionalità dei modelli Gemini, consentendo loro di agire nel mondo, accedere a informazioni in tempo reale ed eseguire attività di calcolo complesse. I modelli possono utilizzare gli strumenti sia nelle interazioni standard di richiesta-risposta sia nelle
sessioni di streaming in tempo reale utilizzando l'[API Live](https://ai.google.dev/gemini-api/docs/live-tools?hl=it).

Gli strumenti sono funzionalità specifiche (come la Ricerca Google o l'esecuzione di codice) che un modello può utilizzare per rispondere alle query. L'API Gemini fornisce una suite di strumenti integrati completamente
gestiti oppure puoi definire strumenti personalizzati utilizzando [la chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).

Per creare sistemi multi-step orientati agli obiettivi, consulta la [Panoramica
sugli agenti](https://ai.google.dev/gemini-api/docs/agents?hl=it).

## Strumenti integrati disponibili

| Strumento | Descrizione | Casi d'uso |
| --- | --- | --- |
| [la Ricerca Google](https://ai.google.dev/gemini-api/docs/google-search?hl=it) | Basare le risposte su eventi e fatti attuali del web per ridurre le allucinazioni. | Rispondere a domande su eventi recenti, verificare i fatti con diverse fonti. |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it) | Crea assistenti basati sulla posizione in grado di trovare luoghi, ottenere indicazioni stradali e fornire un contesto locale ricco. | Pianificare itinerari di viaggio con più tappe, trovare attività locali in base ai criteri dell'utente. |
| [Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) | Consenti al modello di scrivere ed eseguire codice Python per risolvere problemi matematici o elaborare i dati con precisione. | Risolvere equazioni matematiche complesse, elaborare e analizzare con precisione i dati di testo. |
| [Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it) | Indica al modello di leggere e analizzare i contenuti di pagine web o documenti specifici. | Rispondere a domande basate su URL o documenti specifici, recuperare informazioni su diverse pagine web. |
| [Utilizzo del computer (anteprima)](https://ai.google.dev/gemini-api/docs/computer-use?hl=it) | Consenti a Gemini di visualizzare uno schermo e generare azioni per interagire con le UI del browser web (esecuzione lato client). | Automatizzare i flussi di lavoro ripetitivi basati sul web, testare le interfacce utente delle applicazioni web. |
| [Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it) | Indicizza e cerca i tuoi documenti per abilitare la Retrieval-Augmented Generation (RAG). | Cercare manuali tecnici, rispondere a domande su dati proprietari. |

Per informazioni dettagliate
sui costi associati a strumenti specifici, consulta la pagina dei [prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing_for_tools).

## Come funziona l'esecuzione degli strumenti

Gli strumenti consentono al modello di richiedere azioni durante una conversazione. Il flusso varia a seconda che lo strumento sia integrato (gestito da Google) o personalizzato (gestito da te).

### Flusso degli strumenti integrati

Per gli strumenti integrati (Ricerca Google, Google Maps, Contesto URL, Ricerca file, Esecuzione di codice), l'intero processo avviene all'interno di una chiamata API:

1. **Tu** invii un prompt: "Qual è la radice quadrata dell'ultimo prezzo delle azioni di GOOG?".
2. **Gemini** decide di aver bisogno di strumenti e li esegue sui server di Google (ad es. cerca il prezzo delle azioni, quindi esegue codice Python per calcolare la radice quadrata).
3. **Gemini** invia la risposta finale basata sui risultati dello strumento.

### Flusso degli strumenti personalizzati (chiamata di funzione)

Per gli strumenti personalizzati e l'utilizzo del computer, l'applicazione gestisce l'esecuzione:

1. **Tu** invii un prompt insieme alle dichiarazioni delle funzioni (strumenti).
2. **Gemini** potrebbe restituire JSON strutturato per chiamare una funzione specifica
   (ad esempio, `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   sempre con un `id` univoco.
3. **Tu** esegui la funzione nella tua applicazione o nel tuo ambiente.
4. **Tu** invii i risultati della funzione a Gemini, con lo stesso `id` della chiamata di funzione.
5. **Gemini** utilizza i risultati per generare una risposta finale o un'altra chiamata di strumento.

Scopri di più nella [guida alla chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it).

### Combinazione del flusso di strumenti integrati e personalizzati

Per le richieste che combinano strumenti integrati e strumenti personalizzati (chiamate di funzione), il
modello utilizza [la circolazione del contesto dello strumento](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it) per
coordinare l'esecuzione in ambienti diversi:

1. **Tu** invii un prompt e dichiari gli strumenti integrati e le funzioni personalizzate che vuoi abilitare, impostando un flag per attivare il supporto della combinazione.
2. **Gemini** esegue gli strumenti integrati e cede il controllo all'utente se vengono generate chiamate di funzione lato client (l'esecuzione dipende dal prompt e da ciò che decide il modello). Restituisce una risposta con:
   - Conferma della chiamata di strumento
   - Risultati della risposta dello strumento (potrebbe essere visualizzata dopo il JSON se il modello ha generato due chiamate di funzione parallele)
   - JSON strutturato per chiamare la funzione
   - Firme di pensiero criptate per preservare il contesto
3. **Tu** esegui la funzione nella tua applicazione o nel tuo ambiente.
4. **Tu** restituisci tutte le parti della risposta di Gemini, oltre ai risultati della chiamata di funzione.
5. **Gemini** genera la risposta finale utilizzando tutto il contesto combinato.

Leggi la [guida alla combinazione di strumenti](https://ai.google.dev/gemini-api/docs/tool-combination?hl=it) per scoprire
come attivare il supporto per la combinazione di strumenti integrati e personalizzati ed esempi di
circolazione del contesto.

## Output strutturati e chiamata di funzione

Gemini offre due metodi per generare output strutturati. Utilizza la [chiamata di
funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it) quando il modello deve eseguire un
passaggio intermedio collegandosi ai tuoi strumenti o sistemi di dati. Utilizza
[gli output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) quando hai bisogno che
la risposta finale del modello rispetti uno schema specifico, ad esempio per il rendering
di un'UI personalizzata.

## Output strutturati con strumenti

Puoi combinare gli [output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it) con
gli strumenti integrati per assicurarti che le risposte del modello basate su dati o
calcoli esterni rispettino comunque uno schema rigoroso.

Per esempi di codice, consulta [Output strutturati con strumenti](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=it#structured_outputs_with_tools).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-11 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-11 UTC."],[],[]]
