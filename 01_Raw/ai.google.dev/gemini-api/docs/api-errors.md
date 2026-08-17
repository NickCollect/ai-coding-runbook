---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=it
fetched_at: 2026-08-17T02:35:15.725537+00:00
title: "Errori API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Errori API

Questa pagina fornisce un riferimento per tutti i codici di errore dell'API Interactions, descrive il formato della risposta di errore e spiega come l'API restituisce gli errori per i diversi tipi di richiesta.

## Codici di errore API standard

Questi codici di errore generali a livello di richiesta corrispondono ai codici di stato HTTP standard.
Utilizza il campo `code` nella logica dell'applicazione per gestire gli errori a livello di programmazione.

| Codice | Stato HTTP | Descrizione | Comportamento consigliato |
| --- | --- | --- | --- |
| `invalid_request` | 400 Richiesta non valida | La richiesta non è valida o contiene parametri non validi. | Controlla gli input rispetto al [riferimento API](https://ai.google.dev/api/interactions-api?hl=it). |
| `parameter_unknown` | 400 Richiesta non valida | La richiesta contiene un parametro sconosciuto. | Rimuovi il parametro non riconosciuto e riprova. |
| `authentication` | 401 Non autorizzato | La chiave API non è presente o non è valida. | Verifica la [chiave API](https://ai.google.dev/gemini-api/docs/api-key?hl=it). |
| `permission_denied` | 403 Non consentito | La chiave API non dispone dell'autorizzazione per questa risorsa. | Controlla le autorizzazioni della chiave API e l'accesso al progetto. |
| `not_found` | 404: non trovato | La risorsa richiesta non è stata trovata. | Verifica il percorso e i parametri della risorsa. |
| `model_not_found` | 404: non trovato | Il modello specificato non è stato trovato. | Verifica il nome del modello o utilizza un modello diverso. |
| `rate_limit_exceeded` | 429 Troppe richieste | Hai superato il limite di richieste o token al minuto o al secondo. | Attendi e riprova con un backoff esponenziale. |
| `quota_exceeded` | 429 Troppe richieste | Hai superato la quota giornaliera. | Attendi il ripristino della quota o richiedi un aumento della quota. |
| `cancelled` | 499 Richiesta chiusa dal client | Il client ha annullato la richiesta prima del completamento. | Nessuna azione richiesta. In genere, questo significa che il client si è disconnesso. |
| `api_error` | 500 Errore interno del server | Si è verificato un errore imprevisto sul server. | Riprova a inviare la richiesta. Se il problema persiste, contatta l'assistenza. |
| `service_unavailable` | 503 Servizio non disponibile | Il servizio è temporaneamente sovraccarico o non è disponibile. | Attendi e riprova con un backoff esponenziale. |

## Codici di generazione bloccati

Questi codici di errore indicano che le norme, la sicurezza o le limitazioni dei contenuti hanno bloccato l'output del modello. Quando ricevi uno di questi codici, modifica l'input e riprova.

| Codice | Descrizione |
| --- | --- |
| `safety` | Le violazioni della sicurezza (contenuti dannosi) hanno bloccato la richiesta. |
| `recitation` | Le limitazioni relative al copyright o alla recitazione hanno bloccato la richiesta. |
| `language` | Una lingua non supportata ha bloccato la richiesta. |
| `prohibited_content` | Le linee guida per i contenuti vietati hanno bloccato la richiesta. |
| `spii` | Le limitazioni relative alle informazioni sensibili che consentono l'identificazione personale hanno bloccato la richiesta. |
| `blocklist` | I termini vietati in una lista di blocco hanno bloccato la richiesta. |
| `image_safety` | Le violazioni della sicurezza hanno bloccato la generazione di immagini. |
| `image_prohibited_content` | Le linee guida per i contenuti vietati hanno bloccato la generazione di immagini. |
| `image_recitation` | Le limitazioni relative al copyright o alla recitazione hanno bloccato la generazione di immagini. |
| `image_other` | Motivi non specificati hanno bloccato la generazione di immagini. |
| `content_blocked` | Un motivo di norme non specificato ha bloccato la richiesta. |

## Codici di errore di generazione

Questi codici di errore indicano un problema strutturale con l'output generato dal modello (ad esempio una chiamata di funzione non valida o una chiamata di strumento non dichiarata).

| Codice | Descrizione |
| --- | --- |
| `malformed_function_call` | Il modello ha prodotto una chiamata di funzione che non è stato possibile analizzare. |
| `malformed_tool_call` | Il modello ha prodotto una chiamata di strumento che non è stato possibile analizzare. |
| `unexpected_tool_call` | Il modello ha chiamato uno strumento non dichiarato nella richiesta. |
| `no_image` | Il modello non è riuscito a generare un'immagine. |
| `too_many_tool_calls` | Il modello ha generato più chiamate di strumenti di quelle consentite. |
| `missing_thought_signature` | Nella risposta manca una firma di pensiero obbligatoria. |

## Formato della risposta di errore

Tutti gli errori dell'API Interactions restituiscono un `error` oggetto contenente un `code` e `message`. Ad esempio, il passaggio di un tipo di strumento non supportato restituisce:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Campo | Tipo | Descrizione |
| --- | --- | --- |
| `code` | stringa | Un codice di errore leggibile dalla macchina in `snake_case`. |
| `message` | stringa | Una descrizione leggibile di ciò che è andato storto. |

## Come vengono restituiti gli errori

L'API restituisce gli errori in modo diverso a seconda che tu effettui una richiesta HTTP standard o una richiesta di streaming (SSE).

### Richieste HTTP standard

Per le richieste standard (non di streaming), l'API imposta il codice di stato della risposta HTTP (ad esempio `400 Bad Request`, `401 Unauthorized`, o `429 Too Many Requests`) e restituisce un oggetto `error` nel corpo della risposta JSON:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Richieste di streaming (SSE)

Per le richieste di streaming (`stream: true`), l'API invia eventi di errore tramite il flusso di eventi inviati dal server (SSE) con `event_type` impostato su `"error"`. Il campo `error` contiene la stessa struttura `code` e `message`:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Per lo schema completo degli eventi SSE, consulta il [riferimento dell'API Interactions](https://ai.google.dev/api/interactions-api?hl=it).

## Passaggi successivi

- [Risoluzione dei problemi dell'API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=it): risolvi i problemi comuni e gli scenari di errore.
- [Limiti di frequenza](https://ai.google.dev/gemini-api/docs/rate-limits?hl=it): scopri di più sui limiti di richiesta e sulla gestione delle quote.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-30 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-30 UTC."],[],[]]
