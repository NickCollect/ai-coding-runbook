---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=it
fetched_at: 2026-07-06T05:20:41.234709+00:00
title: "Risolvere i problemi relativi a Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Risolvere i problemi relativi a Google AI Studio

Questa pagina fornisce suggerimenti per la risoluzione dei problemi di Google AI Studio in caso di
problemi.

## Informazioni sugli errori 403 Accesso limitato

Se visualizzi l'errore 403 Accesso limitato, stai utilizzando Google AI Studio in un modo che non rispetta i [Termini di servizio](https://ai.google.dev/terms?hl=it). Un motivo comune è che
non ti trovi in una [regione supportata](https://ai.google.dev/available_regions?hl=it).

## Risolvere le risposte Nessun contenuto su Google AI Studio

In Google AI Studio viene visualizzato il messaggio warning **Nessun contenuto** se i contenuti vengono bloccati per qualsiasi motivo. Per visualizzare ulteriori dettagli,
passa il puntatore sopra **Nessun contenuto** e fai clic su
warning **Sicurezza**.

Se la risposta è stata bloccata a causa delle [impostazioni di sicurezza](https://ai.google.dev/docs/safety_setting?hl=it) e
hai preso in considerazione i [rischi per la sicurezza](https://ai.google.dev/docs/safety_guidance?hl=it) per il tuo caso d'uso, puoi
modificare le
[impostazioni di sicurezza](https://ai.google.dev/docs/safety_setting?hl=it#safety_settings_in_makersuite)
per influire sulla risposta restituita.

Se la risposta è stata bloccata, ma non a causa delle impostazioni di sicurezza, la query o la risposta potrebbe violare i [Termini di servizio](https://ai.google.dev/terms?hl=it) o non essere supportata.

## Controllare l'utilizzo e i limiti dei token

Quando hai un prompt aperto, il pulsante **Anteprima testo** nella parte inferiore dello schermo mostra i token correnti utilizzati per i contenuti del prompt e il numero massimo di token per il modello in uso.

## Autorizzazioni Google Cloud IAM per AI Studio

I membri di un progetto Google Cloud hanno bisogno di autorizzazioni Identity and Access Management (IAM) specifiche per eseguire azioni in Google AI Studio. Per saperne di più su queste identità, consulta la [panoramica delle entità IAM](https://cloud.google.com/iam/docs/principals?hl=it).

Gli utenti con i ruoli **Editor** o **Proprietario** nel progetto Google Cloud associato dispongono delle autorizzazioni complete per visualizzare i dashboard e gestire le chiavi API Gemini. Gli utenti con il ruolo **Visualizzatore** possono visualizzare i dashboard e le chiavi API, ma non possono crearli, aggiornarli o eliminarli.

Per un controllo più granulare, consulta la seguente tabella per le autorizzazioni specifiche richieste per ciascuna funzionalità di AI Studio. Per istruzioni su come concedere queste autorizzazioni, consulta [Concessione, modifica e revoca dell'accesso alle risorse](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=it) nella documentazione di Google Cloud.

| Funzionalità di AI Studio | Autorizzazioni IAM obbligatorie | Requisiti aggiuntivi |
| --- | --- | --- |
| **Cerca progetto** (importa progetti) | `resourcemanager.projects.get` |  |
| **Rinomina progetto** | `resourcemanager.projects.update` |  |
| **Visualizzare il livello di quota** | N/D |  |
| **Crea chiave API** | Disporre delle autorizzazioni **Cerca progetto** e:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Elenco chiavi API** | Disporre delle autorizzazioni **Cerca progetto** e:  `apikeys.keys.list` `serviceusage.services.get` | Il progetto Google Cloud deve avere l'[API Generative Language](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=it) abilitata. |
| **Rinomina le chiavi API** | `apikeys.keys.update` |  |
| **Elimina chiavi API** | `apikeys.keys.delete` |  |
| **Dashboard Utilizzo** | Disporre delle autorizzazioni **Cerca progetto** e:  `monitoring.timeSeries.list` |  |
| **Dashboard per la limitazione di frequenza** | Disporre delle autorizzazioni per la **dashboard di utilizzo** e:  `cloudquotas.quotas.get` |  |
| **Spesa (limite di fatturazione)** | `billing.resourceCosts.get` (per visualizzare la spesa) `billing.resourcebudgets.read` (per visualizzare il limite) `billing.resourcebudgets.write` (per impostare il limite) |  |
| **Dashboard di fatturazione** | `billing.accounts.get` |  |

### Altri controlli di accesso

Oltre alle autorizzazioni Cloud IAM di Google Cloud, AI Studio esegue anche controlli di sicurezza e conformità. Potresti riscontrare un errore `PERMISSION_DENIED` o di limitazione dell'accesso nell'interfaccia di AI Studio o nelle risposte API se non soddisfi i seguenti requisiti:

- **Controlli di sicurezza**:la tua richiesta deve superare i controlli di sicurezza automatici.
- **Termini di servizio**:devi accettare i Termini di servizio di Google e i Termini di servizio aggiuntivi per l'IA generativa.
- **Regione supportata**:devi risiedere in una [regione supportata](https://ai.google.dev/gemini-api/docs/available-regions?hl=it).
- **Affidabilità e sicurezza**:il progetto cloud di Google non deve essere segnalato per abuso.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-29 UTC."],[],[]]
