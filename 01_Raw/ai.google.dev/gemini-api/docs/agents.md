---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=it
fetched_at: 2026-06-22T06:27:17.085089+00:00
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

Gli agenti gestiti sull'API Gemini ti offrono un'interfaccia di agente
configurabile. Una singola chiamata API esegue il provisioning di un sandbox Linux in cui l'agente ragiona,
esegue il codice, gestisce i file e naviga sul web in modo autonomo.

[rocket\_launch

Guida rapida

Effettua la tua prima chiamata con un agente, trasmetti in streaming le risposte e crea un agente personalizzato.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=it)
[smart\_toy

Agente Antigravity

Funzionalità, strumenti, input multimodale e prezzi per l'agente predefinito.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it)
[experiment

Agent in AI Studio

Playground visivo per la prototipazione di agenti senza scrivere codice.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it)

## Agenti gestiti disponibili

- **[Agente antigravità](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it)**: agente gestito per uso generico basato su Gemini 3.5 Flash. Esegue il codice, gestisce i file e
  cerca sul web all'interno di una sandbox Linux sicura ospitata da Google. Puoi
  estenderlo con istruzioni, competenze e dati personalizzati per
  [creare un agente personalizzato](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it)**: agente di ricerca autonomo
  che pianifica, esegue e sintetizza attività di ricerca in più fasi per casi d'uso
  come analisi di mercato, due diligence e revisioni della letteratura.

## Sicurezza e best practice

Ogni agente viene eseguito in un ambiente sandbox isolato a livello di sistema operativo.
Per impostazione predefinita, la sandbox ha accesso alla rete in uscita senza restrizioni. Puoi
limitare o disattivare l'accesso alla rete utilizzando una lista consentita.

### Accesso alla rete

Per impostazione predefinita, gli ambienti hanno accesso alla rete in uscita senza limitazioni. Utilizza una
`network` lista consentita per limitare il traffico in uscita a domini specifici o
pattern jolly. Per i dettagli della configurazione, vedi
[Lista consentita di rete](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=it#network_allow_list) (AI
Studio) o [Regole di rete](https://ai.google.dev/gemini-api/docs/custom-agents?hl=it#with_network_rules)
(API).

### API e strumenti esterni

Puoi collegare strumenti e API esterni per estendere l'agente. Utilizza solo strumenti
provenienti da fonti attendibili e limita le autorizzazioni al minimo necessario. Le credenziali
possono essere inserite in modo sicuro tramite le trasformazioni delle intestazioni del proxy in uscita e non vengono mai
esposte all'interno della sandbox. L'agente può utilizzare qualsiasi credenziale a cui ha accesso,
quindi fornisci solo le credenziali di cui vuoi concedere l'ambito completo.

- Utilizza service account o chiavi API con privilegi minimi.
- Preferisci i token di breve durata alle chiavi di lunga durata.
- Fornisci solo le credenziali di cui vuoi concedere l'ambito completo.
- Ruota le credenziali in base a una pianificazione regolare.

Per informazioni dettagliate sulla configurazione delle trasformazioni delle intestazioni, vedi
[Credenziali](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#credentials).

### Supervisione umana

Verifica sempre gli output (codice generato, trasformazioni dei dati, modifiche alla configurazione) prima di eseguirne il deployment, soprattutto per le attività che modificano i dati o interagiscono con sistemi esterni.

## Prezzi

Gli agenti gestiti utilizzano un [modello a pagamento a consumo](https://ai.google.dev/gemini-api/docs/pricing?hl=it#pricing-for-agents) basato sui token del modello Gemini e sull'utilizzo degli strumenti. Una singola interazione può attivare più cicli di ragionamento, in genere consumando da 100.000 a 3 milioni di token. Il calcolo dell'ambiente **non viene fatturato** durante l'anteprima. Consulta i [costi stimati](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=it#availability-and-pricing) per le suddivisioni per attività.

## Limiti

| Limite | Descrizione |
| --- | --- |
| **Durata dell'ambiente** | Gli ambienti vengono eliminati definitivamente dopo 7 giorni di inattività. |
| **VM Spin-down** | Le VM vengono arrestate dopo un breve periodo di inattività per risparmiare risorse. La richiesta successiva ripristina lo stato (con un avvio a freddo). |
| **Software preinstallato** | Ambiente basato su Ubuntu con Python 3.12 e Node.js 22. Per maggiori informazioni sull'immagine di base dell'ambiente, consulta [Software preinstallato](https://ai.google.dev/gemini-api/docs/agent-environment?hl=it#pre-installed-software). |
| **Max agents** | Puoi avere fino a 1000 agenti gestiti. |

## Framework degli agenti

Puoi anche creare agenti con Gemini utilizzando questi framework e SDK:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=it): crea
  flussi di applicazioni complessi e con stato e sistemi multi-agente utilizzando strutture
  di grafici.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=it): collega gli agenti Gemini ai tuoi dati privati per flussi di lavoro migliorati con RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=it): orchestra agenti AI autonomi collaborativi
  che interpretano ruoli.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=it): crea
  interfacce utente e agenti basati sull'AI in JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): un framework
  open source per creare e orchestrare agenti di IA interoperabili.
- [**SDK Antigravity**](https://antigravity.google/product/antigravity-sdk?hl=it): crea
  agenti AI autonomi utilizzando gli stessi strumenti, lo stesso ciclo di agenti e la stessa gestione del contesto
  che alimentano Google Antigravity, programmabile in Python.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-20 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-20 UTC."],[],[]]
