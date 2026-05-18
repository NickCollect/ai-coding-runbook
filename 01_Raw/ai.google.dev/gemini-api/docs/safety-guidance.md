---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=it
fetched_at: 2026-05-18T05:05:29.898716+00:00
title: "Linee guida su sicurezza e accuratezza \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Linee guida su sicurezza e accuratezza

I modelli di intelligenza artificiale generativa sono strumenti potenti, ma non
sono privi di limiti. La loro versatilità e applicabilità a volte possono
portare a output imprevisti, come output imprecisi, distorti o
offensivi. Il post-processing e una rigorosa valutazione manuale sono essenziali per
limitare il rischio di danni derivanti da questi output.

I modelli forniti dall'API Gemini possono essere utilizzati per un'ampia gamma di applicazioni di AI generativa e di elaborazione del linguaggio naturale (NLP). L'utilizzo di queste
funzioni è disponibile solo tramite l'API Gemini o l'app web Google AI Studio. L'utilizzo dell'API Gemini è inoltre soggetto alle [Norme relative all'uso vietato dell'AI generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it) e ai [Termini di servizio dell'API Gemini](https://ai.google.dev/terms?hl=it).

Ciò che rende i modelli linguistici di grandi dimensioni (LLM) così utili è che sono
strumenti creativi che possono affrontare molte attività linguistiche diverse. Purtroppo,
questo significa anche che i modelli linguistici di grandi dimensioni possono generare output inaspettati,
inclusi testi offensivi, insensibili o oggettivamente errati.
Inoltre, l'incredibile versatilità di questi modelli rende difficile
prevedere esattamente quali tipi di output indesiderati potrebbero produrre. Sebbene l'API Gemini sia stata progettata tenendo conto dei [principi di Google in materia di AI](https://ai.google/principles/?hl=it), spetta agli sviluppatori applicare questi modelli in modo responsabile. Per aiutare gli sviluppatori a creare applicazioni sicure e responsabili, l'API Gemini dispone di un filtro dei contenuti integrato e di impostazioni di sicurezza regolabili in quattro dimensioni di rischio. Per saperne di più, consulta la guida alle
[impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it). Offre anche la funzionalità Grounding
con la Ricerca Google abilitata per migliorare l'oggettività, anche se questa funzionalità può essere disattivata
per gli sviluppatori i cui casi d'uso sono più creativi e non di ricerca di informazioni.

Questo documento ha lo scopo di presentarti alcuni rischi per la sicurezza che possono sorgere quando
utilizzi i modelli LLM e consigliare le raccomandazioni emergenti per la progettazione e lo sviluppo
della sicurezza. Tieni presente che anche leggi e normative possono imporre limitazioni,
ma queste considerazioni non rientrano nell'ambito di questa guida.

Quando crei applicazioni con LLM, ti consigliamo di seguire questi passaggi:

- Comprendere i rischi per la sicurezza della tua applicazione
- Valutazione di aggiustamenti per mitigare i rischi per la sicurezza
- Eseguire test di sicurezza appropriati al tuo caso d'uso
- Richiesta di feedback agli utenti e monitoraggio dell'utilizzo

Le fasi di aggiustamento e test devono essere iterative finché non raggiungi
le prestazioni appropriate per la tua applicazione.

![Ciclo di implementazione del modello](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=it)

## Comprendere i rischi per la sicurezza della tua applicazione

In questo contesto, la sicurezza è definita come la capacità di un LLM di evitare
di causare danni ai suoi utenti, ad esempio generando un linguaggio o contenuti tossici
che promuovono stereotipi. I modelli disponibili tramite l'API Gemini sono stati
progettati tenendo presenti i [principi dell'AI di Google](https://ai.google/principles/?hl=it)
e il loro utilizzo è soggetto alle [Norme relative all'uso vietato dell'AI
generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it). L'API
fornisce filtri di sicurezza integrati per contribuire a risolvere alcuni problemi comuni dei modelli linguistici
come linguaggio tossico e incitamento all'odio, e si impegna per l'inclusività
e l'evitare gli stereotipi. Tuttavia, ogni applicazione può comportare una serie diversa
di rischi per i suoi utenti. Pertanto, in qualità di proprietario dell'applicazione, sei responsabile di
conoscere i tuoi utenti e i potenziali danni che la tua applicazione potrebbe causare e
garantire che la tua applicazione utilizzi gli LLM in modo sicuro e responsabile.

Nell'ambito di questa valutazione, devi considerare la probabilità che si verifichi un danno e determinare la sua gravità e le misure di mitigazione. Ad esempio, un'app che genera saggi basati su eventi reali deve prestare maggiore attenzione a evitare la disinformazione rispetto a un'app che genera storie di fantasia per l'intrattenimento. Un buon modo per iniziare a esplorare i potenziali rischi per la sicurezza
è fare ricerche sugli utenti finali e su altre persone che potrebbero essere interessate dai
risultati della tua applicazione. Ciò può assumere molte forme, tra cui la ricerca di studi all'avanguardia nel tuo dominio di app, l'osservazione di come le persone utilizzano app simili o l'esecuzione di uno studio sugli utenti, un sondaggio o la conduzione di interviste informali con potenziali utenti.

#### Suggerimenti avanzati

- Parla con un mix diversificato di potenziali utenti all'interno della tua popolazione target della tua applicazione e del suo scopo previsto per ottenere una prospettiva più ampia sui potenziali rischi e per adeguare i criteri di diversità in base alle esigenze.
- Il [framework per la gestione del rischio dell'AI](https://www.nist.gov/itl/ai-risk-management-framework)
  pubblicato dal National Institute of Standards and Technology (NIST)
  del governo degli Stati Uniti fornisce indicazioni più dettagliate e risorse di apprendimento aggiuntive per la gestione del rischio dell'AI.
- La pubblicazione di DeepMind sui
  [rischi etici e sociali di danni causati dai modelli linguistici](https://arxiv.org/abs/2112.04359)
  descrive in dettaglio i modi in cui le applicazioni
  dei modelli linguistici possono causare danni.

## Valuta modifiche per mitigare i rischi per la sicurezza e l'accuratezza dei fatti

Ora che hai compreso i rischi, puoi decidere come mitigarli. Determinare a quali rischi dare la priorità e cosa fare per cercare di
prevenirli è una decisione fondamentale, simile alla valutazione dei bug in un progetto
software. Una volta stabilite le priorità, puoi iniziare a pensare ai tipi di misure di mitigazione più appropriati. Spesso semplici modifiche possono
fare la differenza e ridurre i rischi.

Ad esempio, quando progetti un'applicazione, considera:

- **Ottimizzazione dell'output del modello** per riflettere meglio ciò che è accettabile nel contesto della tua applicazione. La messa a punto può rendere l'output del modello più prevedibile e coerente e quindi può contribuire a mitigare alcuni rischi.
- **Fornire un metodo di input che faciliti output più sicuri.** L'input esatto
  che fornisci a un LLM può fare la differenza nella qualità dell'output.
  Sperimentare con i prompt di input per trovare la soluzione più sicura nel tuo caso d'uso vale la pena, in quanto puoi fornire un'esperienza utente che lo faciliti. Ad esempio, potresti limitare gli utenti alla scelta solo da un
  elenco a discesa di prompt di input oppure offrire suggerimenti popup con
  frasi
  descrittive che hai riscontrato essere sicure nel contesto della tua applicazione.
- **Blocco degli input non sicuri e filtraggio dell'output prima che venga mostrato all'utente.** In situazioni semplici, le liste bloccate possono essere utilizzate per identificare e bloccare
  parole o frasi non sicure nei prompt o nelle risposte oppure richiedere a revisori umani
  di modificare o bloccare manualmente questi contenuti.
- **Utilizzo di classificatori addestrati per etichettare ogni prompt con potenziali danni o
  segnali contraddittori.** È poi possibile applicare varie strategie per gestire la richiesta in base al tipo di danno rilevato. Ad esempio, se l'input è apertamente contraddittorio o di natura illecita, potrebbe essere bloccato e fornire una risposta preimpostata.

  #### Suggerimento avanzato

  - Se gli indicatori determinano che l'output è dannoso,
    l'applicazione può utilizzare le seguenti opzioni:
    - Fornire un messaggio di errore o un output preimpostato.
    - Prova di nuovo il prompt, nel caso in cui venga generato un output alternativo sicuro, poiché a volte lo stesso prompt genera output diversi.
- **Implementazione di misure di salvaguardia contro l'uso improprio intenzionale**, ad esempio assegnando a ogni utente un ID univoco e imponendo un limite al volume di query utente che possono essere inviate in un determinato periodo. Un'altra misura di salvaguardia è quella di cercare di
  proteggere da possibili prompt injection. La prompt injection, proprio come l'SQL injection, è un modo per gli utenti malintenzionati di progettare un prompt di input che manipola l'output del modello, ad esempio inviando un prompt di input che indica al modello di ignorare tutti gli esempi precedenti. Per informazioni dettagliate sull'uso improprio intenzionale, consulta le
  [Norme relative all'uso vietato dell'IA generativa](https://policies.google.com/terms/generative-ai/use-policy?hl=it).
- **Modifica della funzionalità in modo che presenti un rischio intrinsecamente inferiore.**
  Le attività con un ambito più ristretto (ad es. l'estrazione di parole chiave da passaggi di testo) o che prevedono una maggiore supervisione umana (ad es. la generazione di contenuti in formato breve che verranno esaminati da una persona) spesso comportano un rischio inferiore. Ad esempio, invece di creare un'applicazione per scrivere una risposta email da zero, potresti limitarla a espandere una bozza o suggerire formulazioni alternative.
- **Regolazione delle impostazioni di sicurezza dei contenuti dannosi per ridurre la probabilità di
  visualizzare risposte potenzialmente dannose.** L'API Gemini fornisce impostazioni di sicurezza
  che puoi regolare durante la fase di prototipazione per determinare se la tua
  applicazione richiede una configurazione di sicurezza più o meno restrittiva. Puoi
  modificare queste impostazioni in cinque categorie di filtri per limitare o consentire
  determinati tipi di contenuti. Consulta la [guida alle impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it) per scoprire di più
  sulle impostazioni di sicurezza regolabili disponibili tramite l'API Gemini.
- **Riduci le potenziali imprecisioni fattuali o allucinazioni attivando
  Grounding con la Ricerca Google**. Tieni presente che molti modelli di AI sono sperimentali
  e potrebbero presentare informazioni imprecise, avere allucinazioni o produrre
  output problematici. La funzionalità Grounding con la Ricerca Google collega
  il modello Gemini a contenuti web in tempo reale e funziona con tutte le lingue
  disponibili. In questo modo, Gemini può fornire risposte più accurate e citare fonti verificabili oltre il knowledge cutoff dei modelli.

## Esegui test di sicurezza appropriati al tuo caso d'uso

I test sono una parte fondamentale della creazione di applicazioni robuste e sicure, ma l'entità,
l'ambito e le strategie di test variano. Ad esempio, un generatore di haiku
per divertimento probabilmente comporta rischi meno gravi rispetto, ad esempio, a un'applicazione progettata
per l'utilizzo da parte di studi legali per riassumere documenti legali e contribuire alla stesura di contratti. Tuttavia, il generatore di haiku può essere utilizzato da una gamma più ampia di utenti, il che significa che il potenziale di tentativi ostili o anche di input dannosi non intenzionali può essere maggiore. Anche il contesto di implementazione è importante. Ad esempio, un'applicazione
con output esaminati da esperti umani prima di intraprendere qualsiasi azione
potrebbe essere ritenuta meno propensa a produrre output dannosi rispetto all'applicazione
identica senza tale supervisione.

Non è raro dover apportare modifiche e testare diverse iterazioni prima di ritenere di essere pronti per il lancio, anche per le applicazioni a rischio relativamente basso. Due tipi di test sono particolarmente utili per le applicazioni di AI:

- Il **benchmarking della sicurezza** prevede la progettazione di metriche di sicurezza che riflettano i modi in cui la tua applicazione potrebbe essere pericolosa nel contesto del suo probabile utilizzo, quindi il test delle prestazioni dell'applicazione in base alle metriche utilizzando set di dati di valutazione. È buona norma pensare ai livelli minimi accettabili delle metriche di sicurezza prima del test, in modo da 1) valutare i risultati del test in base a queste aspettative e 2) raccogliere il set di dati di valutazione in base ai test che valutano le metriche che ti interessano di più.

  #### Suggerimenti avanzati

  - Fai attenzione a non fare eccessivo affidamento su approcci "pronti all'uso", in quanto è probabile
    che dovrai creare i tuoi set di dati di test utilizzando valutatori umani per
    adattarli completamente al contesto della tua applicazione.
  - Se hai più di una metrica, dovrai decidere come
    compensare se una modifica comporta miglioramenti per una metrica a
    detrimento di un'altra. Come per altre tecniche di ingegneria del rendimento, potresti
    voler concentrarti sul rendimento nel caso peggiore nel set di valutazione
    anziché sul rendimento medio.
- I **test contraddittori** consistono nel tentativo proattivo di interrompere il funzionamento dell'applicazione. L'obiettivo è identificare i punti deboli in modo da poter adottare
  le misure correttive più appropriate. I test avversariali possono richiedere
  tempo/sforzi significativi da parte di valutatori esperti nella tua applicazione, ma più ne esegui, maggiori sono le possibilità di individuare problemi,
  soprattutto quelli che si verificano raramente o solo dopo ripetute esecuzioni dell'applicazione.

  - un metodo per valutare sistematicamente un modello di ML con l'intento di apprendere come si comporta quando gli viene fornito un input dannoso, intenzionalmente o inavvertitamente:
    - Un input può essere intenzionalmente dannoso quando è chiaramente progettato per produrre un output non sicuro o pericoloso, ad esempio quando si chiede a un modello di generazione di testo di generare un discorso di incitamento all'odio nei confronti di una particolare religione.
    - Un input è inavvertitamente dannoso quando l'input stesso può essere
      innocuo, ma produce un output dannoso. Ad esempio, se si chiede a un modello di
      generazione di testo di descrivere una persona di una particolare etnia e
      si riceve un output razzista.
  - Ciò che distingue un test contraddittorio da una valutazione standard è la
    composizione dei dati utilizzati per il test. Per i test contraddittori, seleziona
    dati di test che hanno maggiori probabilità di generare output problematici
    dal modello. Ciò significa analizzare il comportamento del modello per tutti i tipi di
    danni possibili, inclusi esempi rari o insoliti e
    casi limite pertinenti alle norme di sicurezza. Deve inoltre includere
    la diversità nelle diverse dimensioni di una frase, come struttura,
    significato e lunghezza. Per ulteriori dettagli su cosa considerare quando crei un set di dati di test, consulta le [best practice di Google per l'AI responsabile in materia di equità](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=it).

    #### Suggerimenti avanzati

    - Utilizza
      [test automatici](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=it)
      anziché il metodo tradizionale di arruolare persone in "red team"
      per cercare di compromettere la tua applicazione. Nei test automatizzati, il
      "red team" è un altro modello linguistico che trova un testo di input che
      genera output dannosi dal modello in fase di test.

## Monitorare eventuali problemi

Non importa quanto tu testi e mitighi, non potrai mai garantire la perfezione, quindi pianifica in anticipo come individuare e affrontare i problemi che si presentano. Gli approcci comuni includono la configurazione di un canale monitorato in cui gli utenti possono condividere feedback (ad es. valutazione Mi piace/Non mi piace) e l'esecuzione di uno studio sugli utenti per sollecitare in modo proattivo feedback da un mix diversificato di utenti, il che è particolarmente utile se i modelli di utilizzo sono diversi dalle aspettative.

#### Suggerimenti avanzati

- Quando gli utenti forniscono feedback sui prodotti AI, nel tempo le prestazioni dell'AI e l'esperienza utente possono migliorare notevolmente, ad esempio, aiutandoti a scegliere esempi migliori per l'ottimizzazione dei prompt. Il
  [capitolo Feedback e controllo](https://pair.withgoogle.com/chapter/feedback-controls/)
  della [guida di Google Persone e AI](https://pair.withgoogle.com/guidebook/chapters)
  mette in evidenza le considerazioni chiave da tenere presenti durante la progettazione
  dei meccanismi di feedback.

## Passaggi successivi

- Consulta la guida alle [impostazioni di sicurezza](https://ai.google.dev/gemini-api/docs/safety-settings?hl=it) per scoprire di più sulle impostazioni di sicurezza regolabili disponibili tramite l'API Gemini.
- Consulta l'[introduzione ai prompt](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=it) per iniziare a scrivere i tuoi primi prompt.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-04-29 UTC."],[],[]]
