---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=it
fetched_at: 2026-07-06T05:22:00.567974+00:00
title: "Limiti di frequenza \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Limiti di frequenza

I limiti di frequenza regolano il numero di richieste che puoi effettuare all'API Gemini
in un determinato periodo di tempo. Questi limiti contribuiscono a mantenere un utilizzo equo, proteggere dagli abusi e mantenere le prestazioni del sistema per tutti gli utenti.

[Visualizzare i limiti di frequenza attivi in AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=it)

## Come funzionano i limiti di frequenza

I limiti di frequenza vengono in genere misurati in tre dimensioni:

- Richieste al minuto (**RPM**)
- Token al minuto (input) (**TPM**)
- Richieste al giorno (**RPD**)

Il tuo utilizzo viene valutato in base a ciascun limite e il superamento di uno qualsiasi di questi limiti
attiva un errore di limite di frequenza. Ad esempio, se il limite RPM è 20, l'invio di 21
richieste in un minuto genererà un errore, anche se non hai superato
il limite TPM o altri limiti.

I limiti di frequenza vengono applicati per progetto, non per chiave API. Le quote di richieste al giorno (**RPD**) vengono reimpostate alla mezzanotte del fuso orario del Pacifico.

I limiti variano a seconda del modello specifico utilizzato e alcuni limiti si applicano solo a modelli specifici. Ad esempio, le immagini al minuto (IPM) vengono calcolate solo per i modelli in grado di generare immagini (Nano Banana), ma sono concettualmente simili ai token al minuto (TPM). Altri modelli potrebbero avere un limite di token al giorno (TPD).

I limiti di frequenza sono più restrittivi per i modelli sperimentali e di anteprima.

### Limiti di frequenza basati sulla spesa

Oltre ai limiti di richieste al minuto (RPM) e token al minuto (TPM), l'API Gemini applica limiti di frequenza basati sulla spesa per proteggersi da addebiti imprevisti. L'applicazione di questi limiti al tuo account dipende dalla cronologia
della fatturazione e dal [livello di utilizzo](#usage-tiers).

La tabella seguente mostra i limiti di frequenza basati sulla spesa per ogni [livello di utilizzo](#usage-tiers). Questi limiti vengono valutati in una finestra mobile di 10 minuti. L'applicazione di questi limiti al tuo account dipende dalla cronologia della fatturazione e dallo stato dell'account.

| Livello di utilizzo | Limite di spesa (ogni 10 minuti) |
| --- | --- |
| **Nessun costo** | N/D |
| **Livello 1** | 10 $ |
| **Livello 2** | 200 $ |
| **Livello 3** | 200 $ |

Se raggiungi un limite di frequenza basato sulla spesa, l'API restituisce un errore `429 RESOURCE_EXHAUSTED`. Per risolvere questo problema:

- **Attendi e riprova** dopo un breve periodo di tempo.
- **Riduci la frequenza delle richieste costose**, ad esempio utilizzando finestre contestuali più piccole o output più brevi.
- Se raggiungi costantemente questo limite durante l'utilizzo normale,
  [richiedi un aumento del limite di frequenza](#request-rate-limit-increase).

## Livelli di utilizzo

I limiti di frequenza sono legati al livello di utilizzo del progetto. Man mano che l'utilizzo e la spesa per l'API aumentano, verrà eseguito automaticamente l'upgrade a un livello superiore con limiti di frequenza più elevati.

I requisiti per i livelli 2 e 3 si basano sulla spesa cumulativa totale
per i servizi Google Cloud (inclusa, a titolo esemplificativo, l'API Gemini) per l'account di fatturazione collegato al tuo progetto.

| Livello di utilizzo | Qualificazione | [Limite del livello di fatturazione](https://ai.google.dev/gemini-api/docs/billing?hl=it#tier-spend-caps) |
| --- | --- | --- |
| **Nessun costo** | [Progetto attivo](https://ai.google.dev/gemini-api/docs/api-key?hl=it#google-cloud-projects) o prova senza costi | N/D |
| **Livello 1** | [Configura e collega un account di fatturazione attivo](https://ai.google.dev/gemini-api/docs/billing?hl=it#setup-billing) | 250 $ |
| **Livello 2** | Pagamento di 100 $+ 3 giorni dal primo pagamento riuscito | $ 2000 |
| **Livello 3** | Pagamento di 1000 $+ 30 giorni dal primo pagamento riuscito | 20.000 $-100.000+ $ |

Sebbene il rispetto dei criteri di qualificazione indicati sia generalmente
sufficiente per l'approvazione, in rari casi una richiesta di upgrade può essere rifiutata in base
ad altri fattori identificati durante la procedura di revisione.

Questo sistema contribuisce a mantenere la sicurezza e l'integrità della piattaforma API Gemini
per tutti gli utenti.

## Limiti di frequenza dell'API Gemini

I limiti di frequenza dipendono da una serie di fattori (ad esempio il tuo livello di utilizzo) e possono essere
visualizzati in Google AI Studio. Man mano che il tuo livello e lo stato dell'account cambiano nel tempo,
i limiti di frequenza verranno aggiornati automaticamente.

[Visualizzare i limiti di frequenza attivi in AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=it)

I limiti di frequenza specificati non sono garantiti e la capacità effettiva potrebbe variare.

## Limiti di frequenza dell'inferenza della priorità

Il consumo [prioritario](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it) mantiene i propri limiti di frequenza
anche se il consumo viene conteggiato ai fini dei limiti di frequenza
complessivi del traffico interattivo. **I limiti di frequenza predefiniti sono: 0,3 volte il [limite di frequenza standard](https://aistudio.google.com/rate-limit?hl=it) per ogni modello e livello**

## Limiti di frequenza delle richieste API Batch

Le richieste [API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it) sono soggette a limiti di frequenza propri, separati dalle chiamate API non batch.

- **Richieste batch simultanee:** 100
- **Limite di dimensione del file di input:** 2 GB
- **Limite di spazio di archiviazione dei file:** 20 GB
- **Token in coda per modello**:la tabella **Token batch in coda** elenca il numero massimo di token che possono essere messi in coda per l'elaborazione batch in tutti i job batch attivi per un determinato modello.

### Livello 1

| Modello | Token batch in coda |
| --- | --- |
| Modelli di testo | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (anteprima) | 5.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.1 Flash Lite (anteprima) | 10.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Gemini 2.5 Flash (anteprima) | 3.000.000 |
| Anteprima di Gemini 2.5 Flash Image | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash-Lite | 10.000.000 |
| Gemini 2.5 Flash Lite (anteprima) | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Gemini 2.0 Flash Image | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Modelli di generazione multimodali | | | | |
| Anteprima dell'immagine flash di Gemini 3.1 🍌 | 1.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 2.000.000 |
| Anteprima di Gemini 3 Pro Image 🍌 | 2.000.000 |
| Modelli di embedding | | | | |
| Incorporamento di Gemini | 500.000 |

### Livello 2

| Modello | Token batch in coda |
| --- | --- |
| Modelli di testo | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (anteprima) | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.1 Flash Lite (anteprima) | 500.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Gemini 2.5 Flash (anteprima) | 400.000.000 |
| Anteprima di Gemini 2.5 Flash Image | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash-Lite | 500.000.000 |
| Gemini 2.5 Flash Lite (anteprima) | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Image | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Modelli di generazione multimodali | | | | |
| Anteprima dell'immagine flash di Gemini 3.1 🍌 | 250.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 270.000.000 |
| Anteprima di Gemini 3 Pro Image 🍌 | 270.000.000 |
| Modelli di embedding | | | | |
| Incorporamento di Gemini | 5.000.000 |

### Livello 3

| Modello | Token batch in coda |
| --- | --- |
| Modelli di testo | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (anteprima) | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.1 Flash Lite (anteprima) | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Gemini 2.5 Flash (anteprima) | 1.000.000.000 |
| Anteprima di Gemini 2.5 Flash Image | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash-Lite | 1.000.000.000 |
| Gemini 2.5 Flash Lite (anteprima) | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Gemini 2.0 Flash Image | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Modelli di generazione multimodali | | | | |
| Anteprima dell'immagine flash di Gemini 3.1 🍌 | 750.000.000 |
| Gemini 3.1 Flash Lite Image 🍌 | 1.000.000.000 |
| Anteprima di Gemini 3 Pro Image 🍌 | 1.000.000.000 |
| Modelli di embedding | | | | |
| Incorporamento di Gemini | 10.000.000 |

## Come eseguire l'upgrade al livello successivo

Per eseguire la transizione dal livello senza costi a un livello a pagamento, devi prima
[configurare la fatturazione in AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=it).

Una volta che il tuo progetto soddisfa i [criteri specificati](#usage-tiers), verrà
eseguito automaticamente l'upgrade al livello successivo. Gli upgrade dal Livello senza costi al Livello 1
in genere hanno effetto immediatamente, mentre gli upgrade successivi
hanno effetto entro 10 minuti. Vai alla [pagina Progetti](https://aistudio.google.com/projects?hl=it) in AI Studio per controllare i tuoi livelli.

## Richiedi un aumento del limite di frequenza

Ogni variante del modello ha un limite di frequenza associato (richieste al minuto, RPM).
Per informazioni dettagliate su questi limiti di frequenza, consulta la pagina
[Limite di frequenza di AI Studio](https://aistudio.google.com/rate-limit?hl=it).

[Richiedere un aumento del limite di frequenza per il livello a pagamento](https://forms.gle/ETzX94k8jf7iSotH9)

Non offriamo garanzie in merito all'aumento del limite di frequenza, ma faremo del nostro meglio
per esaminare la tua richiesta.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-03 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-03 UTC."],[],[]]
