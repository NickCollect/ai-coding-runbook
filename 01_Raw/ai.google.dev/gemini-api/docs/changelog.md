---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=de
fetched_at: 2026-09-14T05:52:52.922471+00:00
title: "Versionshinweise \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Versionshinweise

Auf dieser Seite werden Aktualisierungen der Gemini API dokumentiert.

## 21. Juli 2026

- **Allgemeine Verfügbarkeit von Gemini 3.6 Flash und Gemini 3.5 Flash-Lite**: Wir haben stabile, produktionsreife Versionen unserer neuesten 3.x-Flash-Modelle veröffentlicht:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): Bietet eine verbesserte Token-Effizienz und Funktionen für die Code-/Agentenplanung zu einem niedrigeren Preis als 3.5 Flash. Damit wird das Entwickler-Feedback zur Ausführlichkeit der Ausgabe berücksichtigt.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): Bietet eine kostengünstige Subagent-Option mit niedriger Latenz, die für die Automatisierung großer Mengen entwickelt wurde.

  Weitere Informationen finden Sie im Leitfaden [Aktuelles Gemini-Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de).
- **Eingestellte Parameter**: Die Sampling-Parameter `temperature`, `top_p` und `top_k` werden jetzt nicht mehr unterstützt. Weitere Informationen finden Sie unter [Neuestes Gemini-Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de#sampling-parameter-deprecation).

## 6. Juli 2026

- [Entwicklerlogs](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) für die Interactions API: Logs für unterstützte Interactions API-Aufrufe sind jetzt im [AI Studio-Dashboard](https://aistudio.google.com/logs?hl=de) verfügbar.

## 30. Juni 2026

- **Gemini Omni Flash in der öffentlichen Vorabversion**: Veröffentlicht am `gemini-omni-flash-preview`. Ein leistungsstarkes multimodales Modell, das für die schnelle Videogenerierung und die konversationelle Videobearbeitung entwickelt wurde. Mit der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) können Sie aus Textbeschreibungen 3–10 Sekunden lange Videos in 720p generieren oder Standbilder animieren und die Ergebnisse dann im Dialog bearbeiten und optimieren. Weitere Informationen finden Sie im [Leitfaden zu Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=de) und in der [Modellkarte zu Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=de).
- Wir haben `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) allgemein verfügbar gemacht. Das integrierte multimodale Modell ist für extrem niedrige Latenz und kostengünstige Bildgenerierung und ‑bearbeitung optimiert. Weitere Informationen finden Sie in der [Modellkarte für Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=de) und im Leitfaden zur [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

## 24. Juni 2026

- **Computer Use**: Wir haben die öffentliche Vorabversion des Tools [Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) in Gemini 3.5 Flash eingeführt. Diese Version umfasst vereinfachte Aktionen mit Intents, integrierte Unterstützung für Browser-, Mobilgeräte- und Computerumgebungen, konfigurierbare Sicherheitsrichtlinien und eine erweiterte Erkennung von Prompt-Injection.

## 17. Juni 2026

- **Streaming-Unterstützung für die Sprachgenerierung**: Streaming über `streamGenerateContent` (und `stream: true` in der Interactions API) wird jetzt für das Modell `gemini-3.1-flash-tts-preview` unterstützt. Weitere Informationen finden Sie im Leitfaden [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#streaming).

## 15. Juni 2026

- **Ankündigung der Einstellung**: Die folgenden Modelle für die Bildgenerierung werden eingestellt und am **17. August 2026** [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - **Imagen 4- und Gemini 3-Bildmodelle**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    Informationen zum Migrieren Ihres Codes zu neueren stabilen oder Preview-Endpunkten finden Sie auf der Seite [Gemini-Einstellung](https://ai.google.dev/gemini-api/docs/deprecations?hl=de#imagen-models).
- **Ankündigung der Einstellung**: Die folgenden Modelle zur Videogenerierung werden eingestellt und am **30. Juni 2026** [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - **Veo-Modelle**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    Aktualisieren Sie Ihre Integration, um entweder die Preview-Modell-IDs von Veo 3.1 (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) oder die GA-Modelle von Veo 3.1 zu verwenden, die über die [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=de) verfügbar sind, um Dienstunterbrechungen zu vermeiden.
- **Ankündigung der Einstellung**: Das experimentelle GMP Contextual View-Tool (eine feste Schnittstelle für Grounding mit Google Maps-Ausgaben) wird am **15. Juni 2026** [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

## 1. Juni 2026

- Die folgenden Gemini 2.0-Modelle wurden [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Verwenden Sie stattdessen [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) oder [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de).

## 28. Mai 2026

- Wir haben `gemini-3.1-flash-image` (Nano Banana 2) und `gemini-3-pro-image` (Nano Banana Pro) veröffentlicht, die allgemein verfügbaren (GA) Versionen unserer nativen visuellen Modelle [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=de) und [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=de).
- **Unterstützung der Videobildgenerierung**: Sie können jetzt eine Videodatei (per Direktupload oder als öffentliche YouTube-URL) zusammen mit einem Text-Prompt als multimodalen Kontext übergeben, um hochwertige Thumbnails, filmreife Filmposter oder zusammenfassende Infografiken zu generieren. Diese Funktion wird ausschließlich auf dem Modell `gemini-3.1-flash-image` unterstützt. Weitere Informationen finden Sie im Leitfaden zur [Videobildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de#video-to-image).
- Ankündigung der Einstellung: Die Modelle `gemini-3.1-flash-image-preview` und `gemini-3-pro-image-preview` sind veraltet und werden am 25. Juni 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 25. Mai 2026

- Das Modell `gemini-3.1-flash-lite-preview` wurde [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). Verwenden Sie stattdessen [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de).

## 19. Mai 2026

- Wir haben `gemini-3.5-flash` die allgemein verfügbare (GA) Version von [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) veröffentlicht, unserem bisher intelligentesten Modell für dauerhafte Spitzenleistung bei agentischen und Coding-Aufgaben. Dieses Modell ist jetzt die Grundlage für `gemini-flash-latest`.
- Die **Verwalteten KI-Agenten in der Gemini API** sind jetzt in der öffentlichen Vorschau verfügbar. So können Entwickler autonome, zustandsbehaftete Agents erstellen und bereitstellen, die in sicheren, isolierten, von Google gehosteten Linux-Sandbox-Umgebungen ausgeführt werden. Weitere Informationen finden Sie auf der Seite [Agents – Übersicht](https://ai.google.dev/gemini-api/docs/agents?hl=de) und in der [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de).
- Der verwaltete Agent **Antigravity Agent** für allgemeine Zwecke [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=de) ist jetzt in der öffentlichen Vorschau verfügbar.
  Der Antigravity-Agent kann autonom Code planen, schreiben und ausführen, Dateien verwalten und im Web surfen – alles innerhalb seines Sandbox-Containers. [Weitere Informationen](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)

## 7. Mai 2026

- Die allgemein verfügbare (GA) Version von [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) wurde am `gemini-3.1-flash-lite` veröffentlicht. Das Modell ist für Geschwindigkeit, Skalierbarkeit und Kosteneffizienz optimiert.
- Mitteilung zur Einstellung: Das Modell `gemini-3.1-flash-lite-preview` wird am 11.05.2026 eingestellt und am 25.05.2026 [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 6. Mai 2026

- **Anstehende schwerwiegende Änderung**: Das Anfrage- und Antwortschema (`outputs` → `steps`) und die Konfiguration des Ausgabeformats (`response_format`) der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) werden geändert. Das neue Schema wird am **26. Mai** zum Standardschema und das alte Schema wird am **8. Juni** entfernt.
  [Weitere Informationen finden Sie in der Migrationsanleitung](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=de).

## 5. Mai 2026

- Die **Dateisuche** wurde aktualisiert und unterstützt jetzt die multimodale Suche. Sie können jetzt Bilder mithilfe des `gemini-embedding-2`-Modells nativ einbetten und durchsuchen.
  Die Metadaten für die Fundierung enthalten jetzt `media_id` für visuelle Quellenangaben und `page_numbers`, die angeben, wo Informationen gefunden werden. Weitere Informationen finden Sie im Leitfaden [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de).

## 4. Mai 2026

- Wir haben die Unterstützung für ereignisgesteuerte [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=de) in der Gemini API eingeführt, um Polling-Workflows für die Batch API und Vorgänge mit langer Ausführungszeit zu ersetzen.

## 30. April 2026

- Das Modell `gemini-robotics-er-1.5-preview` wurde [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). Verwenden Sie stattdessen [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=de).

## 22. April 2026

- `gemini-embedding-2` ist jetzt allgemein verfügbar (GA). Weitere Informationen finden Sie auf der Seite [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de).

## 21. April 2026

- Wir haben neue Versionen des [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de)-Agents mit Funktionen für die kollaborative Planung, Visualisierung, MCP-Serverintegration und Dateisuche veröffentlicht:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=de): Dieses Modell ist auf Geschwindigkeit und Effizienz ausgelegt und eignet sich ideal für das Streaming zurück an eine Client-Benutzeroberfläche.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=de): Maximale Vollständigkeit für die automatische Kontexterfassung und ‑synthese.

## 15. April 2026

- Wir haben [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=de) eingeführt, unser kostengünstiges, ausdrucksstarkes und steuerbares Modell für die Sprachsynthese. Weitere Informationen finden Sie in der [Dokumentation zu Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de).

## 14. April 2026

- Wir haben `gemini-robotics-er-1.6-preview` veröffentlicht, unser aktualisiertes Robotikmodell.
  Das Modell hat jetzt neue Funktionen wie das Lesen von Instrumenten und verbesserte räumliche und physische Denkfähigkeiten. Weitere Informationen finden Sie auf der Seite [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de) und im [Blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=de).
- Mitteilung zur Einstellung: Das Modell `gemini-robotics-er-1.5-preview` wird am 30. April 2026 um 9:00 Uhr PST [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 2. April 2026

- `gemma-4-26b-a4b-it` und `gemma-4-31b-it` wurden im Rahmen der Einführung von [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=de) veröffentlicht und sind in [AI Studio](https://aistudio.google.com?hl=de) und über die Gemini API verfügbar.

## 1. April 2026

- Die neuen Inferenzebenen [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) und [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) bieten mehr Optionen zur Optimierung von Kosten oder Latenz.

## 31. März 2026

- Wir haben die Veo 3.1 Lite-Vorschau [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=de) eingeführt, unser kostengünstigstes Modell für die [Videogenerierung](https://ai.google.dev/gemini-api/docs/video?hl=de), das für schnelle Iterationen und die Entwicklung von Anwendungen mit hohem Volumen entwickelt wurde.
- Das Modell `gemini-2.5-flash-lite-preview-09-2025` wurde heruntergefahren. Verwenden Sie stattdessen [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de).

## 26. März 2026

- Das neueste Audio-zu-Audio-Modell (A2A) wurde am [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=de) veröffentlicht und ist für Echtzeitdialoge und KI-Anwendungen konzipiert, bei denen die Sprachsteuerung im Vordergrund steht. [Dokumentation zur Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)

## 25. März 2026

- Einführung der [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=de)-Modelle für die Musikgenerierung: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=de) (30-Sekunden-Clips) und [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=de) (Songs in voller Länge). Beide Modelle akzeptieren Text- und Bildeingaben und generieren hochwertiges Stereo-Audio mit 48 kHz. Weitere Informationen und Codebeispiele finden Sie im [Leitfaden zur Musikgenerierung](https://ai.google.dev/gemini-api/docs/music-generation?hl=de).

## 23. März 2026

- Die [Abrechnungsmodelle „Vorauszahlung“ und „Nachträgliche Zahlung“](https://ai.google.dev/gemini-api/docs/billing?hl=de) wurden in AI Studio eingeführt. Bestehende Konten können betroffen sein. Weitere Informationen finden Sie in der [Dokumentation zur Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de).

## 18. März 2026

- Die neue Funktion [Kombination aus integrierten Tools und Funktionsaufrufen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de) wurde eingeführt. Damit ist es möglich, die integrierten Tools von Gemini zusammen mit benutzerdefinierten Tools für Funktionsaufrufe in einem einzigen API-Aufruf zu verwenden.
- Die [Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de#supported_models) wird jetzt für Gemini 3-Modelle unterstützt.

## 16. März 2026

- Wir haben die [Nutzungsstufen](https://ai.google.dev/gemini-api/docs/billing?hl=de#about-billing) und [Ausgabenlimits für Rechnungskonten](https://ai.google.dev/gemini-api/docs/billing?hl=de#tier-spend-caps) überarbeitet, um die Abrechnung für Nutzer zu verbessern.

## 12. März 2026

- In der Abrechnung in AI Studio wurden [Ausgabenobergrenzen auf Projektebene](https://ai.google.dev/gemini-api/docs/billing?hl=de#project-spend-caps) eingeführt.

## 10. März 2026

- Wir haben `gemini-embedding-2-preview` veröffentlicht, unser erstes multimodales Einbettungsmodell.
  Das Modell unterstützt Text-, Bild-, Video-, Audio- und PDF-Eingaben und ordnet alle Modalitäten einem einheitlichen Einbettungsbereich zu. Weitere Informationen finden Sie unter [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de).
- Mitteilung zur Einstellung: Das Modell `gemini-2.5-flash-lite-preview-09-2025` wird am 31. März 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 9. März 2026

- Das Gemini 3 Pro-Vorschaumodell wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). Die `gemini-3-pro-preview` verweist jetzt auf [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de).

## 3. März 2026

- Wir haben Gemini 3.1 Flash-Lite (Vorabversion) eingeführt, das erste Flash-Lite-Modell der Gemini 3-Serie. Auf der [Modellseite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de) finden Sie Spezifikationen, spezifische Updates und Entwickleranleitungen.

## 26. Februar 2026

- Wir haben Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=de), eingeführt. Dieses hocheffiziente Modell ist für Geschwindigkeit und Anwendungsfälle mit hohem Volumen optimiert.
- Ankündigung der Einstellung: Die Vorabversion von Gemini 3 Pro (`gemini-3-pro-preview`) wird am [9. März 2026 eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 19. Februar 2026

- Wir haben [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) veröffentlicht, die neueste Version der neuen Gemini 3-Serie.
- Wir haben einen separaten Endpunkt `gemini-3.1-pro-preview-customtools` eingeführt, der benutzerdefinierte Tools besser priorisiert. Er ist für Nutzer gedacht, die eine Mischung aus Bash und Tools verwenden.

## 18. Februar 2026

- Ankündigung der Einstellung: Die folgenden Modelle werden am 1. Juni 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17. Februar 2026

- Die folgenden Modelle wurden [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29. Januar 2026

- Unterstützung für das Tool „Computer Use“ in `gemini-3-pro-preview` und `gemini-3-flash-preview` eingeführt.

## 21. Januar 2026

- Die `latest`-Aliasse wurden geändert:

  - `gemini-pro-latest` wurde auf `gemini-3-pro-preview` umgestellt
  - `gemini-flash-latest` wurde auf `gemini-3-flash-preview` umgestellt

## 15. Januar 2026

- Ankündigung der Einstellung: Die folgenden Modelle werden am 17. Februar 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Das Modell `gemini-2.5-flash-image-preview` wurde heruntergefahren.

## 14. Januar 2026

- Das Modell `text-embedding-004` wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 13. Januar 2026

- Für [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de) wurden 4K-Ausgabeauflösungen hinzugefügt. Außerdem werden jetzt Hochkantvideos in allen Auflösungen unterstützt.

## 12. Januar 2026

- Die Funktion zum Modelllebenszyklus wurde eingeführt. Bei einigen Modellen werden jetzt die Lebenszyklusphase und der Zeitplan für die Einstellung angegeben. Weitere Informationen finden Sie in der folgenden Dokumentation:

  - [Modellphasen](https://ai.google.dev/api/generate-content?hl=de#ModelStatus)

## 8. Januar 2026

- Unterstützung für Cloud Storage-Buckets und alle öffentlichen und privaten vorab signierten DB-URLs als Daten-Eingangsquelle für die Gemini API eingeführt. Das Dateigrößenlimit wurde ebenfalls von 20 MB auf 100 MB erhöht. Weitere Informationen finden Sie im [Leitfaden zu Dateieingabemethoden](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

## 19. Dezember 2025

- In v1beta wurde eine nicht abwärtskompatible Änderung an der Interactions API eingeführt. Das Feld `total_reasoning_tokens` wurde in `total_thought_tokens` umbenannt, um besser mit dem Konzept von „Gedanken“ in Denkmodellen übereinzustimmen.

## 17. Dezember 2025

- Wir haben Gemini 3 Flash (Vorabversion) eingeführt, `gemini-3-flash-preview`, das eine schnelle Leistung der Frontier-Klasse bietet, die mit größeren Modellen mithalten kann, aber nur einen Bruchteil der Kosten verursacht. Mit verbesserter visueller und räumlicher Argumentation sowie agentischen Programmierfunktionen. Hier finden Sie die Dokumentation zu einigen neuen Funktionen:

  - [Multimodale Funktionsantworten](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#multimodal)
  - [Code-Ausführung mit Bildern](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#images)

## 12. Dezember 2025

- Wir haben `gemini-2.5-flash-native-audio-preview-12-2025` veröffentlicht, ein neues natives Audiomodell für die Live API. Durch diese Aktualisierung wird die Fähigkeit des Modells verbessert, komplexe Workflows zu verarbeiten. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) und unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=de).

## 11. Dezember 2025

- Die Interactions API wurde eingeführt. Diese API bietet eine einheitliche Schnittstelle für die Interaktion mit Gemini-Modellen und ‑Agents. Weitere Informationen finden Sie im [Leitfaden zur Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de).
- Der Gemini Deep Research-Agent wurde in der Vorabversion eingeführt. Die Funktion kann mehrstufige Rechercheaufgaben selbstständig planen, ausführen und die Ergebnisse zusammenfassen. Weitere Informationen finden Sie im [Deep Research-Leitfaden](https://ai.google.dev/gemini-api/docs/deep-research?hl=de).

## 10. Dezember 2025

- Wir haben Verbesserungen an unseren [Text-zu-Sprache-Modellen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) eingeführt, darunter die Gemini 2.5 Flash TTS-Vorabversion (optimiert für niedrige Latenz) und die Gemini 2.5 Pro TTS-Vorabversion (optimiert für Qualität). Diese Modelle bieten eine verbesserte Ausdruckskraft, präzise Rhythmisierung und nahtlose Dialoge.

## 9. Dezember 2025

- Die folgenden Gemini Live API-Modelle werden jetzt eingestellt:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5. Dezember 2025

- Die Abrechnung für Gemini 3 für die [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) beginnt am 5. Januar 2026.

## 4. Dezember 2025

- Einstellung: Das Modell `gemini-2.5-flash-image-preview` wird am 15. Januar 2026 eingestellt.

## 3. Dezember 2025

- Ankündigung der Einstellung: Das Modell `text-embedding-004` wird am 14. Januar 2026 eingestellt.

## 20. November 2025

- Wir haben die Vorabversion von Gemini 3 Pro Image, `gemini-3-pro-image-preview`, veröffentlicht. Das ist die nächste Generation des Nano Banana-Modells. Weitere Informationen finden Sie auf der Seite [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

## 18. November 2025

- Wir haben das erste Modell der Gemini 3-Reihe, `gemini-3-pro-preview`, eingeführt. Es ist unser hochmodernes Modell für Schlussfolgerungen und multimodales Verstehen mit leistungsstarken Agent- und Programmierfunktionen.

  Neben Verbesserungen bei Intelligenz und Leistung bietet die Vorabversion von Gemini 3 Pro neue Verhaltensweisen in Bezug auf:

  - [Media-Auflösung](https://ai.google.dev/gemini-api/docs/media-resolution?hl=de)
  - [Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de)
  - [Denkaufwand](https://ai.google.dev/gemini-api/docs/thinking?hl=de#thinking-levels)

  Weitere Informationen zur Migration, zu neuen Funktionen und zu den Spezifikationen finden Sie im [Gemini 3-Entwicklerleitfaden](https://ai.google.dev/gemini-api/docs/gemini-3?hl=de).

## 11. November 2025

- Ankündigung der Einstellung: Die folgenden Modelle werden deaktiviert:

  - 12. November:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14. November:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10. November 2025

- Das folgende Modell wird heruntergefahren:

  - `imagen-3.0-generate-002`

  Verwenden Sie stattdessen [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=de#imagen-4). Weitere Informationen finden Sie in der [Tabelle zu verworfenen Gemini-Komponenten](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 6. November 2025

- Die File Search API wurde als öffentliche Vorschau eingeführt. Entwickler können damit Antworten auf ihre eigenen Daten stützen. Weitere Informationen finden Sie auf der neuen Seite [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de).

## November 4, 2025

- Bei [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) wurde die Anzahl der Eingabetokens für Bilder von 1.290 auf 258 reduziert, wodurch die Kosten für die Bildbearbeitung sinken.
- Ankündigung der Einstellung: Die folgenden Modelle werden deaktiviert:

  - 18. November:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2. Dezember:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9. Dezember:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29. Oktober 2025

- Das neue Tool [Logging und Datasets](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) für die Gemini API wurde eingeführt.

## 20. Oktober 2025

- Die folgenden Gemini Live API-Modelle werden jetzt eingestellt:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Verwenden Sie stattdessen `gemini-2.5-flash-native-audio-preview-09-2025`.
- Mitteilung zur Einstellung: `gemini-2.0-flash-live-001` und `gemini-live-2.5-flash-preview` werden am 9. Dezember 2025 eingestellt.

## 17. Oktober 2025

- Die **Fundierung mit Google Maps** ist jetzt allgemein verfügbar. Weitere Informationen finden Sie in der Dokumentation [Fundierung mit Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=de).

## 15. Oktober 2025

- Die Modelle [Veo 3.1 und 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=de#veo-3.1) wurden in der öffentlichen Vorschau veröffentlicht. Sie bieten unter anderem folgende neue Funktionen:

  - Mit Veo erstellte Videos verlängern
  - Es werden bis zu drei Bilder als Referenz für die Videoerstellung verwendet.
  - Bereitstellung von Bildern für den ersten und letzten Frame, um Videos zu generieren

  Mit der Einführung wurden auch weitere Optionen für die Videolänge der Veo 3-Ausgabe hinzugefügt: 4, 6 und 8 Sekunden.
- Mitteilung zur Einstellung: `veo-3.0-generate-preview` und `veo-3.0-fast-generate-preview` werden am 12. November 2025 eingestellt.

## 7. Oktober 2025

- [Vorabversion von Gemini 2.5 Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=de)

## 2. Oktober 2025

- Gemini 2.5 Flash Image ist jetzt allgemein verfügbar: [Bildgenerierung mit Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=de)

## 29. September 2025

- Die folgenden Gemini 1.5-Modelle wurden eingestellt:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25. September 2025

- Das Gemini Robotics-ER 1.5-Modell wurde in der Vorabversion veröffentlicht. [Übersicht über Robotik](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de)
- Die folgenden Modelle in der Vorabversion wurden eingeführt:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Weitere Informationen finden Sie auf der Seite [Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de).

## 23. September 2025

- `gemini-2.5-flash-native-audio-preview-09-2025` wurde veröffentlicht, ein neues natives Audiomodell für die Live API mit verbesserter Funktionsaufruf- und Sprachunterbrechungsbehandlung. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) und unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-native-audio).

## 16. September 2025

- Einstellung: Die folgenden Modelle werden im Oktober 2025 eingestellt:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Weitere Informationen zum neuesten Einbettungsmodell finden Sie auf der Seite [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de).

## 10. September 2025

- Wir haben die Unterstützung für das [Embeddings-Modell in der Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de#batch-embedding) eingeführt und die Batch API der [OpenAI-Kompatibilitätsbibliothek](https://ai.google.dev/gemini-api/docs/openai?hl=de#batch) hinzugefügt, um den Einstieg in Batch-Anfragen noch einfacher zu gestalten.

## 9. September 2025

- Veo 3 und Veo 3 Fast sind jetzt allgemein verfügbar. Sie bieten niedrigere Preise und neue Optionen für Seitenverhältnis, Auflösung und Seeding. Weitere Informationen finden Sie in der [Veo-Dokumentation](https://ai.google.dev/gemini-api/docs/video?hl=de#model-features).

## 26. August 2025

- Wir haben [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-image-preview) eingeführt, unser neuestes natives Modell zur Bildgenerierung.

## 18. August 2025

- Das [Tool für URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) ist jetzt allgemein verfügbar. Mit diesem Tool können Sie URLs als zusätzlichen Kontext für Prompts angeben. Die Unterstützung für die Verwendung von URL-Kontext mit dem Modell `gemini-2.0-flash` (verfügbar während der experimentellen Veröffentlichung) wird in einer Woche eingestellt.

## 14. August 2025

- Die Modelle Imagen 4 Ultra, Standard und Fast sind jetzt allgemein verfügbar. Weitere Informationen finden Sie auf der Seite [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=de).

## 7. August 2025

- Die `allow_adult`-Einstellung für die Funktion „Bild zu Video“ ist jetzt auch in eingeschränkten Regionen verfügbar. Weitere Informationen finden Sie auf der Seite [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=de#veo-model-parameters).

## 31. Juli 2025

- Die Bild-zu-Video-Generierung für das Veo 3-Vorschaumodell wurde eingeführt.
- Das Modell „Veo 3 Fast Preview“ wurde veröffentlicht.
- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de)

## 22. Juli 2025

- Wir haben `gemini-2.5-flash-lite` veröffentlicht, unser schnelles, kostengünstiges und leistungsstarkes Gemini 2.5-Modell. [Weitere Informationen zu Gemini 2.5 Flash Lite](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-lite)

## Juli 17, 2025

- Wir haben `veo-3.0-generate-preview` eingeführt, das neueste Update für Veo, mit dem Videos mit Audio generiert werden können. [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de)
- Höhere Ratenbegrenzungen für Imagen 4 Standard und Ultra. Weitere Informationen finden Sie auf der Seite [Ratenbeschränkungen](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de).

## 14. Juli 2025

- Wir haben `gemini-embedding-001` veröffentlicht, die stabile Version unseres Modelle für Texteinbettungen. Weitere Informationen finden Sie unter [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de). Das `gemini-embedding-exp-03-07`-Modell wird am 14. August 2025 eingestellt.

## 7. Juli 2025

- Der Batch-Modus für die Gemini API wurde eingeführt. Fassen Sie Anfragen in Batches zusammen und senden Sie sie asynchron an „process“. Weitere Informationen finden Sie unter [Batchmodus](https://ai.google.dev/gemini-api/docs/batch-mode?hl=de).

## 26. Juni 2025

- Die Vorschauversionen der Modelle `gemini-2.5-pro-preview-05-06` und `gemini-2.5-pro-preview-03-25` werden jetzt zur aktuellen stabilen Version `gemini-2.5-pro` weitergeleitet.
- `gemini-2.5-pro-exp-03-25` wurde heruntergefahren.

## 24. Juni 2025

- Imagen 4 Ultra- und Standard-Vorschaumodelle wurden veröffentlicht. Weitere Informationen finden Sie auf der Seite [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

## 17. Juni 2025

- Wir haben `gemini-2.5-pro` veröffentlicht, die stabile Version unseres leistungsstärksten Modells, das jetzt adaptives Denken unterstützt. Weitere Informationen finden Sie unter [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de). `gemini-2.5-pro-preview-05-06`
  wird am 26. Juni 2025 zu `gemini-2.5-pro` weitergeleitet.
- Wir haben `gemini-2.5-flash` veröffentlicht, unser erstes stabiles 2.5 Flash-Modell. [Weitere Informationen zu Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash)
  `gemini-2.5-flash-preview-04-17` wird am 15. Juli 2025 eingestellt.
- `gemini-2.5-flash-lite-preview-06-17` wurde veröffentlicht, ein kostengünstiges, leistungsstarkes Gemini 2.5-Modell. Weitere Informationen finden Sie unter [Gemini 2.5 Flash-Lite
  Vorabversion](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-lite).

## 5. Juni 2025

- Wir haben `gemini-2.5-pro-preview-06-05` veröffentlicht, eine neue Version unseres leistungsstärksten Modells, das jetzt adaptives Denken unterstützt. Weitere Informationen finden Sie unter [Gemini 2.5 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro-preview-06-05) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).
  `gemini-2.5-pro-preview-05-06` wird am 26. Juni 2025 zu `gemini-2.5-pro` weitergeleitet.

## 27. Mai 2025

- Das letzte verfügbare Tuning-Modell, Gemini 1.5 Flash 001, wurde eingestellt.
  Das Feinabstimmen wird für kein Modell mehr unterstützt.
  Weitere Informationen finden Sie unter [Gemini API für das Fine-Tuning](https://ai.google.dev/gemini-api/docs/model-tuning?hl=de).

## 20. Mai 2025

**API-Updates:**

- Unterstützung für die [benutzerdefinierte Videovorverarbeitung](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#customize-video-processing) mit Clipping-Intervallen und konfigurierbarer Framerate-Erfassung wurde eingeführt.
- Die Verwendung mehrerer Tools wurde eingeführt. Damit können Sie die [Codeausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und die [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/grounding?hl=de) für dieselbe `generateContent`-Anfrage konfigurieren.
- Unterstützung für [asynchrone Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/live-tools?hl=de#async-function-calling) in der Live API wurde eingeführt.
- Wir haben ein experimentelles [Tool für URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) eingeführt, mit dem Sie URLs als zusätzlichen Kontext für Prompts angeben können.

**Modell-Updates**:

- `gemini-2.5-flash-preview-05-20` wurde veröffentlicht, ein Gemini-[Vorschaumodell](https://ai.google.dev/gemini-api/docs/models?hl=de#model-versions), das für Preis-Leistungs-Verhältnis und adaptives Denken optimiert ist. Weitere Informationen finden Sie unter [Gemini 2.5 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).
- Die Modelle [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro-preview-tts) und [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview-tts) wurden veröffentlicht. Sie können [Sprache mit einem oder zwei Sprechern generieren](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de).
- Wir haben das `lyria-realtime-exp`-Modell veröffentlicht, das [Musik in Echtzeit generiert](https://ai.google.dev/gemini-api/docs/music-generation?hl=de).
- `gemini-2.5-flash-preview-native-audio-dialog` und `gemini-2.5-flash-exp-native-audio-thinking-dialog` wurden veröffentlicht, neue Gemini-Modelle für die Live API mit nativer Audioausgabe. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#native-audio-output) und unter [Natives Audiomodell Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-native-audio).
- Die `gemma-3n-e4b-it`-Vorabversion wurde veröffentlicht und ist im Rahmen der Einführung von [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=de) in [AI Studio](https://aistudio.google.com?hl=de) und über die Gemini API verfügbar.

## 7. Mai 2025

- Wir haben `gemini-2.0-flash-preview-image-generation` veröffentlicht, ein Vorschau-Modell zum Generieren und Bearbeiten von Bildern. Weitere Informationen finden Sie unter [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) und [Gemini 2.0 Flash Preview Image Generation](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.0-flash-preview-image-generation).

## 6. Mai 2025

- Wir haben `gemini-2.5-pro-preview-05-06` veröffentlicht, eine neue Version unseres leistungsstärksten Modells, mit Verbesserungen bei Code und Funktionsaufrufen. `gemini-2.5-pro-preview-03-25` verweist automatisch auf die neue Version des Modells.

## 17. April 2025

- `gemini-2.5-flash-preview-04-17` wurde veröffentlicht, ein Gemini-[Vorschaumodell](https://ai.google.dev/gemini-api/docs/models?hl=de#model-versions), das für Preis-Leistungs-Verhältnis und adaptives Denken optimiert ist. Weitere Informationen finden Sie unter [Gemini 2.5 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).

## 16. April 2025

- Kontext-Caching für [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.0-flash) eingeführt.

## 9. April 2025

**Modell-Updates**:

- `veo-2.0-generate-001` wurde veröffentlicht, ein allgemein verfügbares (GA) Modell, das auf Text und Bildern basiert und detaillierte und künstlerisch anspruchsvolle Videos generieren kann. Weitere Informationen finden Sie in der [Veo-Dokumentation](https://ai.google.dev/gemini-api/docs/video?hl=de).
- Am `gemini-2.0-flash-live-001` wurde eine öffentliche Vorschauversion des [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de)-Modells mit aktivierter Abrechnung veröffentlicht.

  - **Verbesserte Sitzungsverwaltung und Zuverlässigkeit**

    - **Sitzungswiederaufnahme**:Sitzungen werden auch bei vorübergehenden Netzwerkunterbrechungen aufrechterhalten. Die API unterstützt jetzt die serverseitige Speicherung des Sitzungsstatus (bis zu 24 Stunden) und bietet Handles (session\_resumption) zum erneuten Verbinden und Fortsetzen der Sitzung.
    - **Längere Sitzungen durch Kontextkomprimierung**:Ermöglicht längere Interaktionen als bisher. Konfigurieren Sie die Komprimierung des Kontextfensters mit einem gleitenden Fenster, um die Kontextlänge automatisch zu verwalten und abrupte Beendigungen aufgrund von Kontextlimits zu verhindern.
    - **Benachrichtigung über das ordnungsgemäße Trennen der Verbindung**:Sie erhalten eine `GoAway`-Servermeldung, die angibt, wann eine Verbindung geschlossen wird. So können Sie die Verbindung vor dem Beenden ordnungsgemäß trennen.
  - **Mehr Kontrolle über die Interaktionsdynamik**
  - **Konfigurierbare Spracherkennung (Voice Activity Detection, VAD)**: Sie können die Empfindlichkeitsstufen auswählen oder die automatische VAD vollständig deaktivieren und neue Clientereignisse (`activityStart`, `activityEnd`) für die manuelle Zugriffssteuerung verwenden.
  - **Konfigurierbare Unterbrechungsbehandlung**:Sie können festlegen, ob die Antwort des Modells durch Nutzereingaben unterbrochen werden soll.
  - **Konfigurierbare Abdeckung von Äußerungen**:Wählen Sie aus, ob die API alle Audio- und Videoeingaben kontinuierlich verarbeitet oder nur dann erfasst, wenn der Endnutzer spricht.
  - **Konfigurierbare Media-Auflösung**:Sie können die Auflösung für Eingabemedien auswählen, um die Qualität oder die Token-Nutzung zu optimieren.
  - **Umfangreichere Ausgabe und Funktionen**
  - **Erweiterte Sprach- und Sprachausgabeoptionen**:Sie können jetzt aus zwei neuen Stimmen und 30 neuen Sprachen für die Audioausgabe auswählen. Die Ausgabesprache kann jetzt in `speechConfig` konfiguriert werden.
  - **Text-Streaming**:Sie erhalten Textantworten inkrementell, während sie generiert werden, sodass sie dem Nutzer schneller angezeigt werden können.
  - **Berichte zur Tokennutzung**:Sie erhalten detaillierte Tokenanzahlen im Feld `usageMetadata` von Servernachrichten, aufgeschlüsselt nach Modalität und Prompt- oder Antwortphasen.

## 4. April 2025

- Wir haben `gemini-2.5-pro-preview-03-25` veröffentlicht, eine öffentliche Vorabversion von Gemini 2.5 Pro mit aktivierter Abrechnung. Sie können `gemini-2.5-pro-exp-03-25` weiterhin im kostenlosen Kontingent verwenden.

## 25. März 2025

- `gemini-2.5-pro-exp-03-25` wurde veröffentlicht, ein öffentliches experimentelles Gemini-Modell, bei dem der Denkmodus standardmäßig immer aktiviert ist.
  Weitere Informationen finden Sie unter
  [Gemini 2.5 Pro (experimentell)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro-preview-03-25).

## 12. März 2025

**Modell-Updates**:

- Wir haben das experimentelle Modell [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=de#gemini) eingeführt, das Bilder generieren und bearbeiten kann.
- Veröffentlicht am `gemma-3-27b-it`, verfügbar in [AI Studio](https://aistudio.google.com?hl=de) und über die Gemini API im Rahmen der Einführung von [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=de).

**API-Updates:**

- Unterstützung für [YouTube-URLs](https://ai.google.dev/gemini-api/docs/vision?hl=de#youtube) als Media-Quelle hinzugefügt.
- Es ist jetzt möglich, ein [Inline-Video](https://ai.google.dev/gemini-api/docs/vision?hl=de#inline-video) mit einer Größe von weniger als 20 MB einzufügen.

## 11. März 2025

**SDK-Updates:**

- Das [Google Gen AI SDK für TypeScript und JavaScript](https://googleapis.github.io/js-genai) ist jetzt in der öffentlichen Vorschau verfügbar.

## 7. März 2025

**Modell-Updates**:

- `gemini-embedding-exp-03-07` wurde ein [experimentelles](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=de) auf Gemini basierendes Einbettungsmodell in der öffentlichen Vorschau veröffentlicht.

## 28. Februar 2025

**API-Updates:**

- Unterstützung für [Suche als Tool](https://ai.google.dev/gemini-api/docs/grounding?hl=de) wurde `gemini-2.0-pro-exp-02-05` hinzugefügt, einem experimentellen Modell, das auf Gemini 2.0 Pro basiert.

## 25. Februar 2025

**Modell-Updates**:

- Wir haben `gemini-2.0-flash-lite` veröffentlicht, eine allgemein verfügbare Version von [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash-lite), die für Geschwindigkeit, Skalierbarkeit und Kosteneffizienz optimiert ist.

## 19. Februar 2025

**Updates zu AI Studio**:

- Unterstützung für [zusätzliche Regionen](https://ai.google.dev/gemini-api/docs/available-regions?hl=de) (Kosovo, Grönland und Färöer).

**API-Updates:**

- Unterstützung für [zusätzliche Regionen](https://ai.google.dev/gemini-api/docs/available-regions?hl=de) (Kosovo, Grönland und Färöer).

## 18. Februar 2025

**Modell-Updates**:

- Gemini 1.0 Pro wird nicht mehr unterstützt. Eine Liste der unterstützten Modelle finden Sie unter [Gemini-Modelle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

## 11. Februar 2025

**API-Updates:**

- Aktualisierungen der [Kompatibilität der OpenAI-Bibliotheken](https://ai.google.dev/gemini-api/docs/openai?hl=de).

## 6. Februar 2025

**Modell-Updates**:

- Wir haben `imagen-3.0-generate-002` veröffentlicht, eine allgemein verfügbare (GA) Version von [Imagen 3 in der Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=de).

**SDK-Updates:**

- Das [Google Gen AI SDK für Java](https://github.com/googleapis/java-genai) wurde für die öffentliche Vorschau veröffentlicht.

## 5. Februar 2025

**Modell-Updates**:

- Wir haben `gemini-2.0-flash-001` veröffentlicht, eine allgemein verfügbare (GA) Version von [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash), die nur Textausgabe unterstützt.
- Veröffentlicht am `gemini-2.0-pro-exp-02-05`,
  eine [experimentelle](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=de) öffentliche Vorabversion von Gemini 2.0 Pro.
- `gemini-2.0-flash-lite-preview-02-05` wurde veröffentlicht, eine experimentelle öffentliche [Modell](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash-lite)-Vorabversion, die für Kosteneffizienz optimiert ist.

**API-Updates:**

- Die Unterstützung von [Dateieingabe und Grafikausgabe](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#input-output) wurde der Codeausführung hinzugefügt.

**SDK-Updates:**

- Das [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/) ist jetzt allgemein verfügbar.

## 21. Januar 2025

**Modell-Updates**:

- Wir haben `gemini-2.0-flash-thinking-exp-01-21` veröffentlicht, die aktuelle Vorabversion des Modells, das dem [Gemini 2.0 Flash Thinking-Modell](https://ai.google.dev/gemini-api/docs/thinking?hl=de) zugrunde liegt.

## 19. Dezember 2024

**Modell-Updates**:

- Der Gemini 2.0 Flash Thinking-Modus ist jetzt in der öffentlichen Vorschau verfügbar. Der Denkmodus ist ein Berechnungsmodell für die Testzeit, mit dem Sie den Denkprozess des Modells sehen können, während es eine Antwort generiert. Außerdem werden Antworten mit besseren Argumentationsfähigkeiten erstellt.

  Weitere Informationen zum Gemini 2.0 Flash Thinking-Modus finden Sie auf unserer [Übersichtsseite](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=de).

## 11. Dezember 2024

**Modell-Updates**:

- [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash) für die öffentliche Vorschau veröffentlicht. Hier eine unvollständige Liste der Funktionen von Gemini 2.0 Flash Experimental:
  - Doppelt so schnell wie Gemini 1.5 Pro
  - Bidirektionales Streaming mit unserer Live API
  - Multimodale Antwortgenerierung in Form von Text, Bildern und Sprache
  - Verwendung integrierter Tools mit Mehrfachdialog-Argumentation, um Funktionen wie Codeausführung, Suche und Funktionsaufrufe zu nutzen

[Weitere Informationen zu Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=de)

## 21. November 2024

**Modell-Updates**:

- Wir haben `gemini-exp-1121` veröffentlicht, ein noch leistungsstärkeres experimentelles Gemini API-Modell.

**Modell-Updates**:

- Die Modellaliase `gemini-1.5-flash-latest` und `gemini-1.5-flash` wurden aktualisiert, sodass `gemini-1.5-flash-002` verwendet wird.
  - Änderung des Parameters `top_k`: Das Modell `gemini-1.5-flash-002` unterstützt `top_k`-Werte zwischen 1 und 41 (ausschließlich).
    Werte über 40 werden in 40 geändert.

## 14. November 2024

**Modell-Updates**:

- Wir haben `gemini-exp-1114` veröffentlicht, ein leistungsstarkes experimentelles Gemini API-Modell.

## 8. November 2024

**API-Updates:**

- [Unterstützung für Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=de) in den OpenAI-Bibliotheken / der REST API hinzugefügt.

## 31. Oktober 2024

**API-Updates:**

- [Unterstützung für die Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/grounding?hl=de) hinzugefügt.

## 3. Oktober 2024

**Modell-Updates**:

- Wir haben `gemini-1.5-flash-8b-001` veröffentlicht, eine stabile Version unseres kleinsten Gemini API-Modells.

## 24. September 2024

**Modell-Updates**:

- Wir haben `gemini-1.5-pro-002` und `gemini-1.5-flash-002` veröffentlicht, zwei neue stabile Versionen von Gemini 1.5 Pro und 1.5 Flash, die allgemein verfügbar sind.
- Der `gemini-1.5-pro-latest`-Modellcode wurde aktualisiert, sodass `gemini-1.5-pro-002` verwendet wird, und der `gemini-1.5-flash-latest`-Modellcode wurde aktualisiert, sodass `gemini-1.5-flash-002` verwendet wird.
- `gemini-1.5-flash-8b-exp-0924` wurde veröffentlicht, um `gemini-1.5-flash-8b-exp-0827` zu ersetzen.
- Der [Sicherheitsfilter für die Integrität öffentlicher Aussagen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de#safety-filters) für die Gemini API und AI Studio wurde veröffentlicht.
- Unterstützung für zwei neue Parameter für Gemini 1.5 Pro und 1.5 Flash in Python und NodeJS wurde eingeführt: [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=de#FIELDS.frequency_penalty) und [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=de#FIELDS.presence_penalty).

## 19. September 2024

**Updates zu AI Studio**:

- Den Modellantworten wurden „Gefällt mir“- und „Gefällt mir nicht“-Buttons hinzugefügt, damit Nutzer Feedback zur Qualität einer Antwort geben können.

**API-Updates:**

- Unterstützung für Google Cloud-Guthaben hinzugefügt, das jetzt für die Nutzung der Gemini API verwendet werden kann.

## 17. September 2024

**Updates zu AI Studio**:

- Die Schaltfläche **In Colab öffnen** wurde hinzugefügt. Damit wird ein Prompt und der Code zum Ausführen des Prompts in ein Colab-Notebook exportiert. Die Funktion unterstützt noch keine Prompts mit Tools (JSON-Modus, Funktionsaufrufe oder Codeausführung).

## 13. September 2024

**Updates zu AI Studio**:

- Es wurde Unterstützung für den Vergleichsmodus hinzugefügt. Damit können Sie Antworten verschiedener Modelle und Prompts vergleichen, um die beste Lösung für Ihren Anwendungsfall zu finden.

## 30. August 2024

**Modell-Updates**:

- Gemini 1.5 Flash unterstützt [die Bereitstellung von JSON-Schemas über die Modellkonfiguration](https://ai.google.dev/gemini-api/docs/json-mode?hl=de#supply-schema-in-config).

## 27. August 2024

**Modell-Updates**:

- Die folgenden [experimentellen Modelle](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=de) wurden veröffentlicht:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9. August 2024

**API-Updates:**

- Unterstützung für die [PDF-Verarbeitung](https://ai.google.dev/gemini-api/docs/document-processing?hl=de) hinzugefügt.

## 5. August 2024

**Modell-Updates**:

- Unterstützung für die Feinabstimmung von Gemini 1.5 Flash wurde eingeführt.

## 1. August 2024

**Modell-Updates**:

- Wir haben `gemini-1.5-pro-exp-0801` eine neue experimentelle Version von [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-pro) veröffentlicht.

## 12. Juli 2024

**Modell-Updates**:

- Unterstützung für Gemini 1.0 Pro Vision aus Google AI-Diensten und ‑Tools entfernt.

## 27. Juni 2024

**Modell-Updates**:

- Release mit allgemeiner Verfügbarkeit für das Kontextfenster von 2 Millionen Tokens von Gemini 1.5 Pro.

**API-Updates:**

- Unterstützung für die [Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) hinzugefügt.

## 18. Juni 2024

**API-Updates:**

- Unterstützung für [Kontext-Caching](https://ai.google.dev/gemini-api/docs/caching?hl=de) hinzugefügt.

## 12. Juni 2024

**Modell-Updates**:

- Gemini 1.0 Pro Vision wurde eingestellt.

## 23. Mai 2024

**Modell-Updates**:

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-pro) (`gemini-1.5-pro-001`) ist allgemein verfügbar.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-flash) (`gemini-1.5-flash-001`) ist allgemein verfügbar.

## 14. Mai 2024

**API-Updates:**

- Ein Kontextfenster von 2 Millionen Tokens für Gemini 1.5 Pro wurde eingeführt (Warteliste).
- Das [Abrechnungsmodell „Pay as you go“](https://ai.google.dev/gemini-api/docs/billing?hl=de) für Gemini 1.0 Pro wurde eingeführt. Die Abrechnung für Gemini 1.5 Pro und Gemini 1.5 Flash folgt in Kürze.
- Die Ratenbegrenzungen für die kommende kostenpflichtige Version von Gemini 1.5 Pro wurden erhöht.
- Der [File API](https://ai.google.dev/api/rest/v1beta/files?hl=de) wurde integrierte Videounterstützung hinzugefügt.
- Unterstützung für Nur-Text in der [File API](https://ai.google.dev/api/rest/v1beta/files?hl=de) hinzugefügt.
- Es wurde Unterstützung für parallele Funktionsaufrufe hinzugefügt, bei denen jeweils mehr als ein Aufruf zurückgegeben wird.

## 10. Mai 2024

**Modell-Updates**:

- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-flash) (`gemini-1.5-flash-latest`) wurde in der Vorabversion veröffentlicht.

## 9. April 2024

**Modell-Updates**:

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-pro) (`gemini-1.5-pro-latest`) wurde als Vorschauversion veröffentlicht.
- Wir haben ein neues Texteinbettungsmodell, `text-embeddings-004`, veröffentlicht, das [flexible Einbettungsgrößen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de#elastic-embedding) unter 768 unterstützt.

**API-Updates:**

- Die [File API](https://ai.google.dev/api/rest/v1beta/files?hl=de) wurde veröffentlicht, um Mediendateien vorübergehend für die Verwendung in Prompts zu speichern.
- Es wurde Unterstützung für Prompts mit Text-, Bild- und Audiodaten hinzugefügt, auch bekannt als *multimodale* Prompts. Weitere Informationen finden Sie unter [Prompts mit Medien](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=de).
- [Systemanweisungen](https://ai.google.dev/gemini-api/docs/system-instructions?hl=de) in der Betaversion veröffentlicht.
- Der [Modus für Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#function_calling_mode) wurde hinzugefügt. Er definiert das Ausführungsverhalten für Funktionsaufrufe.
- Unterstützung für die Konfigurationsoption `response_mime_type` hinzugefügt, mit der Sie Antworten im [JSON-Format](https://ai.google.dev/gemini-api/docs/api-overview?hl=de#json) anfordern können.

## 19. März 2024

**Modell-Updates**:

- Unterstützung für das [Abstimmen von Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) in Google AI Studio oder mit der Gemini API hinzugefügt.

## 13. Dezember 2023

**Modell-Updates**:

- gemini-pro: Neues Textmodell für eine Vielzahl von Aufgaben. Gleicht Leistungsfähigkeit und Effizienz aus.
- gemini-pro-vision: Neues multimodales Modell für eine Vielzahl von Aufgaben.
  Gleicht Leistungsfähigkeit und Effizienz aus.
- embedding-001: Neues Einbettungsmodell.
- aqa: Ein neues, speziell abgestimmtes Modell, das darauf trainiert ist, Fragen zu beantworten und dabei Textpassagen zur Fundierung der generierten Antworten zu verwenden.

Weitere Informationen finden Sie unter [Gemini-Modelle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

**Updates der API-Version:**

- v1: Der stabile API-Channel.
- v1beta: Betaversion. Dieser Kanal hat Funktionen, die sich möglicherweise noch in der Entwicklung befinden.

Weitere Informationen finden Sie im [Thema zu API-Versionen](https://ai.google.dev/gemini-api/docs/api-versions?hl=de).

**API-Updates:**

- `GenerateContent` ist ein einzelner einheitlicher Endpunkt für Chat und Text.
- Streaming über die Methode `StreamGenerateContent` verfügbar.
- Multimodale Funktion: Bilder sind ein neuer unterstützter Modus
- Neue Betafunktionen:
  - [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=de)
  - Attributed Question Answering (AQA)
- Aktualisierte Anzahl der Kandidaten: Gemini-Modelle geben nur einen Kandidaten zurück.
- Unterschiedliche Sicherheitseinstellungen und Altersfreigabekategorien. Weitere Informationen finden Sie unter [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).
- Das Optimieren von Modellen wird für Gemini-Modelle noch nicht unterstützt (wird gerade entwickelt).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-12 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-12 (UTC)."],[],[]]
