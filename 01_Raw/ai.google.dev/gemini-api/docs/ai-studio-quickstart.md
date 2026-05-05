---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=it
fetched_at: 2026-05-05T20:49:05.077748+00:00
title: "Guida rapida di Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Guida rapida di Google AI Studio

[Google AI Studio](https://aistudio.google.com/?hl=it) ti consente di provare rapidamente modelli e sperimentare diversi prompt. Quando è tutto pronto, puoi selezionare "Ottieni codice " e il tuo linguaggio di programmazione preferito per utilizzare l'[API Gemini](https://ai.google.dev/gemini-api/docs/quickstart?hl=it).

## Prompt e impostazioni

Google AI Studio fornisce diverse interfacce per i prompt progettate per
diversi casi d'uso. Questa guida tratta i **prompt di chat**, utilizzati per creare
esperienze conversazionali. Questa tecnica di prompt consente più turni di input
e risposta per generare l'output. Scopri di più con il nostro
[esempio di prompt di chat di seguito](#chat_example).
Altre opzioni includono **Streaming in tempo reale**, **Generazione video** e
altro ancora.

AI Studio fornisce anche il riquadro **Impostazioni di esecuzione**, in cui puoi apportare modifiche ai [parametri del modello](https://ai.google.dev/docs/prompting-strategies?hl=it#model-parameters), alle [impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it) e attivare/disattivare strumenti come [output strutturato](https://ai.google.dev/gemini-api/docs/structured-output?hl=it), [chiamata di funzioni](https://ai.google.dev/gemini-api/docs/function-calling?hl=it), [esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it) e [grounding](https://ai.google.dev/gemini-api/docs/grounding?hl=it).

## Esempio di prompt di chat: crea un'applicazione di chat personalizzata

Se hai utilizzato un chatbot per uso generico come
[Gemini](https://gemini.google.com/?hl=it), hai sperimentato in prima persona la potenza
dei modelli di AI generativa per il dialogo aperto. Sebbene questi chatbot per uso generico siano utili, spesso devono essere adattati a casi d'uso particolari.

Ad esempio, potresti voler creare un chatbot di assistenza clienti che supporti solo le conversazioni che riguardano il prodotto di un'azienda. Potresti voler
creare un chatbot che parli con un tono o uno stile particolare: un bot che faccia
molte battute, rimi come un poeta o usi molte emoji nelle sue risposte.

Questo esempio mostra come utilizzare Google AI Studio per creare un chatbot amichevole
che comunica come se fosse un alieno che vive su una delle lune di Giove, Europa.

### Passaggio 1: crea un prompt di chat

Per creare un chatbot, devi fornire esempi di interazioni tra un utente e il chatbot per guidare il modello a fornire le risposte che stai cercando.

Per creare un prompt di chat:

1. Apri [Google AI Studio](https://aistudio.google.com/?hl=it). **Chat** verrà preselezionata nel menu opzioni a sinistra.
2. Fai clic sull'icona assignment nella parte superiore della finestra del prompt di Chat per espandere il campo di immissione [**Istruzioni di sistema**](https://ai.google.dev/gemini-api/docs/text-generation?hl=it#system-instructions). Incolla quanto segue nel campo di immissione del testo:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Dopo aver aggiunto le istruzioni di sistema, inizia a testare l'applicazione
interagendo con il modello:

1. Nella casella di input di testo con l'etichetta **Digita qualcosa…**, digita una domanda o
   un'osservazione che un utente potrebbe fare. Ad esempio:

   **Utente:**

   ```
   What's the weather like?
   ```
2. Fai clic sul pulsante **Esegui** per ricevere una risposta dal chatbot. Questa risposta
   potrebbe essere simile alla seguente:

   **Modello:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Passaggio 2: insegna al bot a chattare meglio

Fornendo una singola istruzione, sei riuscito a creare un chatbot di base per l'alieno Europa. Tuttavia, una singola istruzione potrebbe non essere sufficiente a garantire
coerenza e qualità nelle risposte del modello. Senza istruzioni più specifiche, la risposta del modello a una domanda sul meteo tende a essere molto lunga e può assumere un tono personale.

Personalizza il tono del chatbot aggiungendo alle istruzioni di sistema:

1. Avvia un nuovo prompt di chat o utilizza lo stesso. Le istruzioni di sistema sono
   modificabili dopo l'inizio della sessione di chat.
2. Nella sezione **Istruzioni di sistema**, modifica le istruzioni esistenti
   con le seguenti:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Inserisci di nuovo la domanda (`What's the weather like?`) e fai clic sul pulsante **Esegui**. Se non hai avviato una nuova chat, la risposta potrebbe essere simile a questa:

   **Modello:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Puoi utilizzare questo approccio per aggiungere ulteriore profondità al chatbot. Poni altre
domande, modifica le risposte e migliora la qualità del tuo chatbot. Continua
ad aggiungere o modificare le istruzioni e verifica come cambiano il comportamento
del chatbot.

### Passaggio 3: azioni successive

Come per gli altri tipi di prompt, una volta creato il prototipo del prompt in modo soddisfacente, puoi utilizzare il pulsante **Ottieni codice** per iniziare a programmare o salvare il prompt per lavorarci in un secondo momento e condividerlo con altri.

## Per approfondire

- Se vuoi passare al codice, consulta le [guide rapide
  alle API](https://ai.google.dev/gemini-api/docs/quickstart?hl=it).
- Per scoprire come creare prompt migliori, consulta le [linee guida per la progettazione dei prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
