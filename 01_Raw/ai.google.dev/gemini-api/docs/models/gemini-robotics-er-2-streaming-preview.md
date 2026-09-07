---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-2-streaming-preview?hl=it
fetched_at: 2026-09-07T05:34:56.647756+00:00
title: "Streaming di Gemini Robotics ER 2 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'API [Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=it) è ora disponibile a livello generale. Ti consigliamo di utilizzare questa API per accedere a tutti i modelli e a tutte le funzionalità più recenti.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Streaming di Gemini Robotics ER 2

Gemini Robotics ER 2 Streaming è un modello vision-language (VLM) per la robotica
ottimizzato per lo streaming di testo in tempo reale tramite l'API Live. Accetta input di testo,
immagini, video e audio e supporta lo streaming bidirezionale con
chiamata di funzioni.

[Prova in Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-streaming-preview&hl=it)

## Documentazione

Visita la pagina dell'[API Live per la robotica](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=it) per
una copertura completa di funzionalità e capacità.

## gemini-robotics-er-2-streaming-preview

### Gemini Robotics ER 2 (anteprima)

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | `gemini-robotics-er-2-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Fondatezza della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| Versioni 123 | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions) per maggiori dettagli.  - Anteprima: `gemini-robotics-er-2-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |

### Gemini Robotics ER 2 Streaming Preview

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | `gemini-robotics-er-2-streaming-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Non supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Non supportato  **[Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Non supportato  **[Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Non supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Non supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Supportato  **[Fondatezza della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Non supportato  **[Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Non supportato |
| speedOpzioni di consumo | **[API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Non supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| Versioni 123 | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions) per maggiori dettagli.  - Anteprima: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthUltimo aggiornamento | Luglio 2026 |
| id\_cardScheda del modello | [Scheda del modello](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=it) |

### Gemini Robotics ER 1.6 (anteprima)

| Proprietà | Descrizione |
| --- | --- |
| Codice modello id\_card | `gemini-robotics-er-1.6-preview` |
| saveTipi di dati supportati | **Input**  Testo, immagini, video, audio  **Output**  Testo |
| token\_autoLimiti dei token[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=it) | **Limite di token di input**  131.072  **Limite di token di output**  65.536 |
| handymanFunzionalità | **[Generazione di audio](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it)**  Non supportato  **[Memorizzazione nella cache](https://ai.google.dev/gemini-api/docs/caching?hl=it)**  Supportato  **[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/code-execution?hl=it)**  Supportato  **[Utilizzo del computer](https://ai.google.dev/gemini-api/docs/computer-use?hl=it)**  Supportato  **[Ricerca file](https://ai.google.dev/gemini-api/docs/file-search?hl=it)**  Supportato  **[Chiamata di funzione](https://ai.google.dev/gemini-api/docs/function-calling?hl=it)**  Supportato  **[Grounding con Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=it)**  Supportato  **[Generazione di immagini](https://ai.google.dev/gemini-api/docs/image-generation?hl=it)**  Non supportato  **[API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it)**  Non supportato  **[Fondatezza della Ricerca](https://ai.google.dev/gemini-api/docs/google-search?hl=it)**  Supportato  **[Output strutturati](https://ai.google.dev/gemini-api/docs/structured-output?hl=it)**  Supportato  **[Pensiero](https://ai.google.dev/gemini-api/docs/thinking?hl=it)**  Supportato  **[Contesto URL](https://ai.google.dev/gemini-api/docs/url-context?hl=it)**  Supportato |
| speedOpzioni di consumo | **[API batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=it)**  Supportato  **[Inferenza Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=it)**  Non supportato  **[Inferenza prioritaria](https://ai.google.dev/gemini-api/docs/priority-inference?hl=it)**  Non supportato |
| Versioni 123 | Leggi i [pattern delle versioni del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=it#model-versions) per maggiori dettagli.  - Anteprima: `gemini-robotics-er-1.6-preview` |
| calendar\_monthUltimo aggiornamento | Dicembre 2025 |
| cognition\_2Knowledge cutoff | Gennaio 2025 |

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-08-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-08-19 UTC."],[],[]]
