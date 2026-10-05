---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=de
fetched_at: 2026-10-05T06:30:05.347842+00:00
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

## 22. September 2026

- **Gemini 3.8 Flash TTS und Gemini 3.8 Flash-Lite TTS allgemein verfügbar**: Wir haben unsere Audio-Modelle der nächsten Generation für die Text-to-Speech-Technologie (TTS) und den Gemini API-Endpunkt „Voices“ (`/v1beta/voices`) veröffentlicht:

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de)
    (`gemini-3.8-flash-tts`)**: Flagship-TTS-Modell für kreative Anwendungen, das für Sprachwiedergabe in Studioqualität, nuancierte Darstellung, regionale Dialekte und Stabilität bei langen Mehrfachdialogen entwickelt wurde.
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de)
    (`gemini-3.8-flash-lite-tts`)**: Schnelles, kostengünstiges TTS-Modell, das `gemini-3.1-flash-tts-preview` für die Produktion mit hohem Durchsatz und Echtzeit-Sprachagenten-Cascades ersetzen soll.
  - **[Stimmendesign](https://ai.google.dev/gemini-api/docs/voice-design?hl=de),
    [Stimmreplikation](https://ai.google.dev/gemini-api/docs/voice-replication?hl=de) und die
    [erweiterte Stimmenbibliothek](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#voice-library)**:
    Erstellen Sie dauerhafte benutzerdefinierte Stimmenidentitäten aus Text-Prompts, replizieren Sie Stimmen mit Einwilligung und fragen Sie mehr als 150 vordefinierte und benutzerdefinierte Stimmen ab.

  [Weitere Informationen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de)

## 18. September 2026

- **Aktualisierung des Zugriffs auf Gemini 2.5-Modelle**: Damit alle Nutzer zuverlässig auf die Modelle zugreifen können, beschränken wir den Zugriff auf die 2.5-Modelle auf Nutzer, die sie in der Vergangenheit aktiv verwendet haben. Diese Modelle sind nicht veraltet und werden bis auf Weiteres über die API bereitgestellt. Verwenden Sie für neue Projekte unsere neuesten Modelle: 3.5 Flash-Lite oder 3.8 Flash. So können wir sowohl für laufende Legacy-Workflows als auch für neue Anwendungen ausreichend Kapazität bereitstellen.

## 17. September 2026

- **Antigravity Agent 09-2026**: Veröffentlicht am `antigravity-preview-09-2026`. Er ersetzt und macht `antigravity-preview-05-2026` überflüssig.

  Wenn Sie eine Remote-Sandbox (`environment: "remote"`) verwenden und nur die Schritte `output_text` oder `model_output` lesen, wird nur der Agent-String aktualisiert.

  Wenn Sie Tools lokal ausführen (`local_environment`) oder `function_call`-Schritte parsen, haben sich die integrierten Tools geändert. Für Parameter wird PascalCase anstelle von snake\_case verwendet und für Dateibearbeitungen werden Zeilenbereichsersetzungen anstelle von vollständigen Überschreibungen verwendet.

  | Funktion | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | Dateierstellung | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | Dateibearbeitung | `write_file(path, content)`, vollständiges Umschreiben | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | Datei lesen | `read_file(path, offset, limit)`, Byte-Offsets | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | Verzeichniseintrag | `list_files(path)` | `list_dir(DirectoryPath)` |
  | Datei- und Codesuche | Keine, da Shell-Befehle verwendet wurden | `find_by_name(SearchDirectory, Pattern, MaxDepth)` und `grep_search(SearchPath, Query, IsRegex)` |
  | Shell-Ausführung | `code_execution(command, timeout_seconds)` | Nicht geändert |
  | Websuche | `google_search(queries)` | Nicht geändert |

  Weitere Informationen finden Sie im [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)-Leitfaden.
  `antigravity-preview-05-2026` wird am 5. Oktober 2026 eingestellt. Weitere Informationen finden Sie auf der Seite [Einstellung](https://ai.google.dev/gemini-api/docs/deprecations?hl=de#managed-agents).

## 15. September 2026

- **Gemini 3.8 Live und Gemini 3.8 Live Extended Thinking allgemein verfügbar**: Wir haben zwei neue Audio-zu-Audio-Modelle für Echtzeit-Sprachanwendungen mit der Live API veröffentlicht:

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=de)): Die Standardoption für die meisten Sprach-KI-Agenten mit geringer Latenz und Echtzeitdialoge ohne Verzögerungen bei der Schlussfolgerung. Sie bietet verschachtelte Argumentation, standardmäßige asynchrone Funktionsaufrufe und vollständige Aktualisierungen der Clientinhalte in der Sitzung.
  - **Gemini 3.8 Live Extended Thinking**
    ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=de)): Audio-zu-Audio-Modell mit hoher Schlussfolgerungsfähigkeit, das Hintergrundschlüsse während der Live-Audio-Interaktionen unterstützt. Empfohlen, wenn eine höhere Hintergrundschlüssigkeit erforderlich ist.

  Eine Einführung finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-api?hl=de), im [Leitfaden zu Funktionen](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de) und im [Leitfaden zum Denken](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=de).

## 3. September 2026

- **Lyria 3.5 allgemein verfügbar**: Wir haben die nächste Generation des Musikgenerierungsmodells von Google veröffentlicht:

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=de):
    Generierung von Songs in voller Länge mit verbesserter musikalischer Kohärenz, natürlichen Gesangsparts sowie detaillierter Steuerung von Dauer und Struktur.

  Das Modell unterstützt Text- und Bildeingaben und generiert hochwertiges Stereo-Audio mit 44,1 kHz. Weitere Informationen und Codebeispiele finden Sie im [Leitfaden zur Musikgenerierung](https://ai.google.dev/gemini-api/docs/music-generation?hl=de).

## 2. September 2026

- **Gemini 3.8 Flash allgemein verfügbar**: Veröffentlicht
  `gemini-3.8-flash`, unser intelligentestes Flash-Modell, das für langfristige Softwareentwicklung, autonome KI-Agenten und komplexe Unternehmensworkflows entwickelt wurde.

  Weitere Informationen finden Sie auf der Modellseite [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=de) und im [Leitfaden für das neueste Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de).

## 1. September 2026

- **Agentic Video Understanding**: Wir haben Agentic Video Understanding für Gemini 3.7 Flash, 3.6 Flash und 3.5 Flash-Lite in den APIs „Interactions“ und „GenerateContent“ eingeführt. Das Modell navigiert dynamisch durch Video-Zeitleisten und fordert Transkripte, Frames oder Audio-Tracks bei Bedarf an. Bei diesem Ansatz werden für Inhalte im Langformat bis zu 88% weniger Tokens verwendet als bei der statischen Verarbeitung.

  [Anleitung zum agentischen Videoverständnis](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#agentic-video-understanding)

## 27. August 2026

- **Gemini Omni Flash allgemein verfügbar (GA)**: Veröffentlicht
  `gemini-omni-1.1-flash`, die GA-Version unseres schnellen, konversationellen Modells für die Videogenerierung und ‑bearbeitung. Diese Version enthält wichtige neue Funktionen:

  - **Video verlängern**: Sie können vorhandene Videos ganz einfach verlängern, indem Sie mit dem `extend`-Vorgang oder direkt mit einem Prompt Fortsetzungen am Ende eines Clips generieren.
  - **Interpolation (erstes + letztes Frame)**: Mit dem Task `image_to_video` können Sie ein Video generieren, das zwischen zwei Bildern überblendet. Dabei können Sie bis zu zwei Bilder verwenden.
  - **Auflösungssteuerung**: Der neue `resolution`-Parameter in `video_config` unterstützt die Ausgaben `360p`, `720p` (Standard), `1080p` und `4k`.
    1080p- und 4K-Ausgaben werden durch Upscaling generiert.

  Der vorhandene `gemini-omni-flash-preview`-Endpunkt wird am 30. September 2026 eingestellt.

  Weitere Informationen finden Sie auf der Modellseite [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=de) und im [Omni-Leitfaden](https://ai.google.dev/gemini-api/docs/omni?hl=de).

## 26. August 2026

- **Gemini 3.5 Transcribe allgemein verfügbar**: Wir haben zwei spezielle Speech-to-Text-Modelle auf Grundlage der Audioanalyse von Gemini veröffentlicht:

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`): Hohe Genauigkeit, geringe Latenz, nicht gestreamte Sprache-zu-Text-Funktion mit auf Äußerungen basierender Spracherkennung in über 85 Sprachen, Sprecherzuordnung, Zeitstempel auf Wortebene und benutzerdefinierte Vokabeln (bis zu 1.000 Begriffe).
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`):
    Bidirektionale Streaming-Sprache-zu-Text-Funktion mit geringer Latenz über WebSockets mit der Live API, die Zwischen- und endgültige Transkriptionsereignisse, den Smart-Transkriptionsmodus und mehrere Strategien zur Erkennung von Sprachaktivitäten (Voice Activity Detection, VAD) unterstützt.

  Weitere Informationen finden Sie im [Leitfaden zur Audiotranskription](https://ai.google.dev/gemini-api/docs/transcribe?hl=de), im [Leitfaden zur Live-Transkription](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=de) und auf der [Modellseite für Gemini 3.5 Transcribe](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=de).

## 13. August 2026

- **Gemini 3.7 Flash allgemein verfügbar**: Wir haben unser bisher intelligentestes Workhorse-Modell für Coding und KI-Agenten veröffentlicht:

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`): Deutliche Verbesserungen in den Bereichen Softwareentwicklung, Webentwicklung und Agent-Workflows. Bis zum 31. Dezember 2026 zum Einführungspreis verfügbar.

  Weitere Informationen finden Sie auf der Modellseite [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=de) und im [Leitfaden für das neueste Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de).

## 30. Juli 2026

- **Gemini Robotics ER 2 in der öffentlichen Vorschau**: Es wurden zwei neue Endpunkte für Modelle für verkörperte Schlussfolgerungen für die Robotik veröffentlicht:

  - `gemini-robotics-er-2-preview`: Erweiterte räumliche Argumentation, agentische Code-Ausführung, mehrstufige Tool-Orchestrierung, Auffinden von Videomomenten, Fortschrittsklassifizierung und Koordination mehrerer Roboter.
  - `gemini-robotics-er-2-streaming-preview`: Optimiert für das Text-Streaming in Echtzeit über die Live API, wodurch Roboter-Agents mit geringer Latenz und bidirektionaler Audio- und Videoeingabe möglich sind.

  Beide Modellendpunkte akzeptieren Text-, Bild-, Video- und Audioeingaben und unterstützen Funktionsaufrufe mit blockierendem Verhalten für physische Roboteraktionen.
  Eine Einführung finden Sie in der [Übersicht über die Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de). Anwendungsfälle für Echtzeit-Streaming finden Sie unter [Robotik mit Streaming](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=de).
- **Mitteilung zur Einstellung**: Das Modell `gemini-robotics-er-1.6-preview` wird am 31. August 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 21. Juli 2026

- **Allgemeine Verfügbarkeit von Gemini 3.6 Flash und Gemini 3.5 Flash-Lite**:
  Wir haben stabile, produktionsreife Versionen unserer neuesten 3.x-Flash-Modelle veröffentlicht:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): Bietet eine verbesserte Token-Effizienz und Funktionen für die Code- und Agentenplanung zu einem niedrigeren Preis als 3.5 Flash. Damit wird auf das Entwickler-Feedback zur Ausführlichkeit der Ausgabe reagiert.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): Bietet eine kostengünstige Subagent-Option mit geringer Latenz, die für die Automatisierung großer Mengen entwickelt wurde.

  Weitere Informationen finden Sie im Leitfaden [Aktuelles Gemini-Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de).
- **Nicht mehr unterstützte Parameter**: Die Sampling-Parameter `temperature`, `top_p` und `top_k` werden nicht mehr unterstützt. Weitere Informationen finden Sie unter [Neuestes Gemini-Modell](https://ai.google.dev/gemini-api/docs/latest-model?hl=de#sampling-parameter-deprecation).

## 6. Juli 2026

- [Entwicklerlogs](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=de) für die Interactions API: Logs für unterstützte Interactions API-Aufrufe sind jetzt im [AI Studio-Dashboard](https://aistudio.google.com/logs?hl=de) verfügbar.

## 30. Juni 2026

- **Gemini Omni Flash in der öffentlichen Vorabversion**: Veröffentlicht am `gemini-omni-flash-preview`. Es handelt sich um ein leistungsstarkes multimodales Modell, das für die schnelle Videogenerierung und die konversationelle Videobearbeitung entwickelt wurde. Mit der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) können Sie aus Textbeschreibungen 3–10 Sekunden lange Videos in 720p generieren oder Standbilder animieren und die Ergebnisse dann im Dialog bearbeiten und optimieren. Weitere Informationen finden Sie im [Leitfaden zu Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=de) und in der [Modellkarte zu Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=de).
- Wir haben `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) allgemein verfügbar gemacht. Das integrierte multimodale Modell ist für extrem niedrige Latenz und kostengünstige Bildgenerierung und ‑bearbeitung optimiert. Weitere Informationen finden Sie in der [Modellkarte für Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=de) und im Leitfaden zur [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

## 24. Juni 2026

- **Computer Use**: Wir haben die öffentliche Vorabversion des Tools [Computer Use](https://ai.google.dev/gemini-api/docs/computer-use?hl=de) in Gemini 3.5 Flash eingeführt. Diese Version umfasst vereinfachte Aktionen mit Intents, integrierte Unterstützung für Browser-, Mobil- und Desktopumgebungen, konfigurierbare Sicherheitsrichtlinien und eine erweiterte Erkennung von Prompt-Injection.

## 17. Juni 2026

- **Streaming-Unterstützung für die Spracherzeugung**: Streaming über `streamGenerateContent` (und `stream: true` in der Interactions API) wird jetzt für das Modell `gemini-3.1-flash-tts-preview` unterstützt. Weitere Informationen finden Sie im [Leitfaden zu Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de#streaming).

## 15. Juni 2026

- **Ankündigung der Einstellung**: Die folgenden Modelle zur Bildgenerierung werden eingestellt und am **17. August 2026** [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - **Imagen 4- und Gemini 3-Bildmodelle**:
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  Informationen zur Migration Ihres Codes zu neueren stabilen oder Preview-Endpunkten finden Sie auf der Seite [Gemini-Einstellung](https://ai.google.dev/gemini-api/docs/deprecations?hl=de#imagen-models).
- **Ankündigung zur Einstellung**: Die folgenden Modelle zur Videogenerierung werden eingestellt und am **30. Juni 2026** [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

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
- **Unterstützung für die Generierung von Bildern aus Videos**: Sie können jetzt eine Videodatei (über einen direkten Upload oder als öffentliche YouTube-URL) als multimodalen Kontext zusammen mit einem Text-Prompt übergeben, um hochwertige Thumbnails, Kinoplakate oder zusammenfassende Infografiken zu generieren. Diese Funktion wird ausschließlich auf dem Modell `gemini-3.1-flash-image` unterstützt. Weitere Informationen finden Sie im Leitfaden zur [Videobildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de#video-to-image).
- Ankündigung der Einstellung: Die Modelle `gemini-3.1-flash-image-preview` und `gemini-3-pro-image-preview` werden nicht mehr unterstützt und am 25. Juni 2026 [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 25. Mai 2026

- Das Modell `gemini-3.1-flash-lite-preview` wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). Verwenden Sie stattdessen [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de).

## 19. Mai 2026

- Wir haben `gemini-3.5-flash` die allgemein verfügbare (GA) Version von [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) veröffentlicht, unserem bisher intelligentesten Modell für dauerhafte Spitzenleistung bei agentischen und Coding-Aufgaben. Dieses Modell ist jetzt die Grundlage für `gemini-flash-latest`.
- Die **Verwalteten KI-Agenten in der Gemini API** sind jetzt in der öffentlichen Vorschau verfügbar. So können Entwickler autonome, zustandsbehaftete Agenten erstellen und bereitstellen, die in sicheren, isolierten, von Google gehosteten Linux-Sandbox-Umgebungen ausgeführt werden. Weitere Informationen finden Sie auf der Seite [Übersicht über Agents](https://ai.google.dev/gemini-api/docs/agents?hl=de) und in der [Kurzanleitung](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de).
- Der verwaltete **Antigravity-Agent** für allgemeine Zwecke [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=de) wurde in der öffentlichen Vorschau veröffentlicht.
  Der Antigravity-Agent kann in seinem Sandbox-Container autonom Code planen, analysieren, schreiben und ausführen, Dateien verwalten und im Web suchen. [Weitere Informationen](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de)

## 7. Mai 2026

- Die allgemein verfügbare (GA) Version von [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) wurde am `gemini-3.1-flash-lite` veröffentlicht. Das Modell ist für Geschwindigkeit, Skalierbarkeit und Kosteneffizienz optimiert.
- Mitteilung zur Einstellung: Das Modell `gemini-3.1-flash-lite-preview` wird am 11.05.2026 eingestellt und am 25.05.2026 [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 6. Mai 2026

- **Anstehende Breaking Change**: Das Anfrage- und Antwortschema (`outputs` → `steps`) und die Konfiguration des Ausgabeformats (`response_format`) der [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) werden geändert. Das neue Schema wird am **26. Mai** zum Standard und das alte Schema wird am **8. Juni** entfernt.
  [Weitere Informationen finden Sie in der Migrationsanleitung](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=de).

## 5. Mai 2026

- Die **Dateisuche** wurde aktualisiert und unterstützt jetzt die multimodale Suche. Sie können jetzt Bilder mithilfe des `gemini-embedding-2`-Modells nativ einbetten und durchsuchen.
  Die Metadaten für die Fundierung enthalten jetzt `media_id` für visuelle Quellenangaben und `page_numbers`, die angeben, wo Informationen gefunden werden. Weitere Informationen finden Sie im Leitfaden [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de).

## 4. Mai 2026

- Wir haben die Unterstützung für ereignisgesteuerte [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=de) in der Gemini API eingeführt, um Polling-Workflows für die Batch API und Vorgänge mit langer Ausführungszeit zu ersetzen.

## 30. April 2026

- Das Modell `gemini-robotics-er-1.5-preview` wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). Verwenden Sie stattdessen [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=de).

## 22. April 2026

- `gemini-embedding-2` ist jetzt allgemein verfügbar (GA). Weitere Informationen finden Sie auf der Seite [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de).

## 21. April 2026

- Wir haben neue Versionen des [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de)-Agenten mit Funktionen für die kollaborative Planung, Visualisierung, MCP-Serverintegration und Dateisuche veröffentlicht:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=de): Dieses Modell ist auf Geschwindigkeit und Effizienz ausgelegt und eignet sich ideal für das Streaming zurück an eine Client-Benutzeroberfläche.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=de): Maximale Vollständigkeit für die automatische Kontextsammlung und ‑synthese.

## 15. April 2026

- Wir haben [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=de) eingeführt, unser kostengünstiges, ausdrucksstarkes und steuerbares Modell für die Sprachsynthese. Weitere Informationen finden Sie in der [Text-to-Speech-Dokumentation](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de).

## 14. April 2026

- Wir haben `gemini-robotics-er-1.6-preview` veröffentlicht, unser aktualisiertes Robotikmodell.
  Das Modell hat jetzt neue Funktionen wie das Lesen von Instrumenten und verbesserte räumliche und physische Denkfähigkeiten. Weitere Informationen finden Sie auf der Seite [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de) und im [Blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=de).
- Mitteilung zur Einstellung: Das Modell `gemini-robotics-er-1.5-preview` wird am 30. April 2026 um 9:00 Uhr PST [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 2. April 2026

- `gemma-4-26b-a4b-it` und `gemma-4-31b-it` wurden im Rahmen der Einführung von [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=de) veröffentlicht und sind in [AI Studio](https://aistudio.google.com?hl=de) und über die Gemini API verfügbar.

## 1. April 2026

- Die neuen Inferenzstufen [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=de) und [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=de) bieten mehr Optionen zur Optimierung von Kosten oder Latenz.

## 31. März 2026

- Wir haben die Veo 3.1 Lite-Vorschau[`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=de) eingeführt, unser kostengünstigstes Modell für die [Videogenerierung](https://ai.google.dev/gemini-api/docs/video?hl=de), das für schnelle Iterationen und die Entwicklung von Anwendungen mit hohem Volumen entwickelt wurde.
- Das Modell `gemini-2.5-flash-lite-preview-09-2025` wurde heruntergefahren. Verwenden Sie stattdessen [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de).

## 26. März 2026

- Veröffentlicht am [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=de). Das neueste Audio-zu-Audio-Modell (A2A) wurde für Echtzeitdialoge und KI-Anwendungen entwickelt, bei denen die Sprachsteuerung im Vordergrund steht. Lesen Sie die [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de)-Dokumentation, um loszulegen.

## 25. März 2026

- Einführung der [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=de)-Modelle für die Musikgenerierung: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=de) (30‑sekündige Clips) und [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=de) (Songs in voller Länge). Beide Modelle akzeptieren Text- und Bildeingaben und generieren hochwertiges Stereo-Audio mit 48 kHz. Weitere Informationen und Codebeispiele finden Sie im [Leitfaden zur Musikgenerierung](https://ai.google.dev/gemini-api/docs/music-generation?hl=de).

## 23. März 2026

- [Abrechnungsmodelle mit Vorauszahlung und nachträglicher Zahlung](https://ai.google.dev/gemini-api/docs/billing?hl=de) in AI Studio eingeführt. Vorhandene Konten können betroffen sein. Weitere Informationen finden Sie in der [Dokumentation zur Abrechnung](https://ai.google.dev/gemini-api/docs/billing?hl=de).

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

- Das Gemini 3 Pro-Vorschaumodell wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de). `gemini-3-pro-preview` verweist jetzt auf [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de).

## 3. März 2026

- Wir haben die Vorabversion von Gemini 3.1 Flash-Lite eingeführt, dem ersten Flash-Lite-Modell der Gemini 3-Serie. Auf der [Modellseite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=de) finden Sie Spezifikationen, spezifische Updates und Entwicklerinformationen.

## 26. Februar 2026

- Wir haben Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=de), eingeführt. Das ist ein hocheffizientes Modell, das für Geschwindigkeit und Anwendungsfälle mit hohem Volumen optimiert ist.
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

- Die folgenden Modelle werden [heruntergefahren](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

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

- Ankündigung der Einstellung: Die folgenden Modelle werden am 17. Februar 2026 [deaktiviert](https://ai.google.dev/gemini-api/docs/deprecations?hl=de):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Das Modell `gemini-2.5-flash-image-preview` wurde heruntergefahren.

## 14. Januar 2026

- Das Modell `text-embedding-004` wurde [eingestellt](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 13. Januar 2026

- Für [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de) wurden 4K-Ausgabeauflösungen hinzugefügt. Außerdem werden jetzt Hochformatvideos in allen Auflösungen unterstützt.

## 12. Januar 2026

- Die Funktion zum Modelllebenszyklus wurde eingeführt. Bei einigen Modellen werden jetzt die Lebenszyklusphase und der Zeitplan für die Einstellung angegeben. Weitere Informationen finden Sie in der folgenden Dokumentation:

  - [Modellphasen](https://ai.google.dev/api/generate-content?hl=de#ModelStatus)

## 8. Januar 2026

- Unterstützung für Cloud Storage-Buckets und alle öffentlichen und privaten vorab signierten DB-URLs als Daten-Eingangsquelle für die Gemini API eingeführt. Das Dateigrößenlimit wurde von 20 MB auf 100 MB erhöht. Weitere Informationen finden Sie im [Leitfaden zu Dateieingabemethoden](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=de).

## 19. Dezember 2025

- In v1beta wurde eine funktionsgefährdende Änderung an der Interactions API eingeführt. Das Feld `total_reasoning_tokens` wurde in `total_thought_tokens` umbenannt, um besser mit dem Konzept von „Gedanken“ in Denkmodellen übereinzustimmen.

## 17. Dezember 2025

- Wir haben Gemini 3 Flash (Vorabversion) eingeführt, `gemini-3-flash-preview`, das eine schnelle Leistung der Frontier-Klasse bietet, die mit größeren Modellen mithalten kann, aber nur einen Bruchteil der Kosten verursacht. Mit verbesserter visueller und räumlicher Argumentation sowie agentischen Programmierfunktionen. Hier finden Sie die Dokumentation zu einigen neuen Funktionen:

  - [Multimodale Funktionsantworten](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#multimodal)
  - [Code-Ausführung mit Bildern](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#images)

## 12. Dezember 2025

- Wir haben `gemini-2.5-flash-native-audio-preview-12-2025` veröffentlicht, ein neues natives Audiomodell für die Live API. Durch dieses Update wird die Fähigkeit des Modells verbessert, komplexe Workflows zu verarbeiten. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) und unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=de).

## 11. Dezember 2025

- Die Interactions API wurde eingeführt. Diese API bietet eine einheitliche Schnittstelle für die Interaktion mit Gemini-Modellen und ‑Agents. Weitere Informationen finden Sie im Leitfaden zur [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de).
- Der Gemini Deep Research-Agent wurde in der Vorabversion eingeführt. Die Funktion kann mehrstufige Rechercheaufgaben selbstständig planen, ausführen und die Ergebnisse zusammenfassen. Weitere Informationen finden Sie im [Leitfaden zu Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=de).

## 10. Dezember 2025

- Wir haben Verbesserungen an unseren [Modellen für die Sprachsynthese](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) eingeführt, darunter die Gemini 2.5 Flash TTS-Vorschau (optimiert für niedrige Latenz) und die Gemini 2.5 Pro TTS-Vorschau (optimiert für Qualität). Diese bieten eine verbesserte Ausdruckskraft, präzise Rhythmisierung und nahtlose Dialoge.

## 9. Dezember 2025

- Die folgenden Gemini Live API-Modelle werden jetzt eingestellt:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5. Dezember 2025

- Die Abrechnung für Gemini 3 für die [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/google-search?hl=de) beginnt am 5. Januar 2026.

## 4. Dezember 2025

- Einstellung: Das Modell `gemini-2.5-flash-image-preview` wird am 15. Januar 2026 eingestellt.

## 3. Dezember 2025

- Einstellung: Das Modell `text-embedding-004` wird am 14. Januar 2026 eingestellt.

## 20. November 2025

- Wir haben die Gemini 3 Pro Image Preview, `gemini-3-pro-image-preview`, veröffentlicht. Das ist die nächste Generation des Nano Banana-Modells. Weitere Informationen finden Sie auf der Seite [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de).

## 18. November 2025

- Wir haben das erste Modell der Gemini 3-Reihe, `gemini-3-pro-preview`, eingeführt. Es ist unser hochmodernes Modell für Schlussfolgerungen und multimodales Verstehen mit leistungsstarken Agent- und Coding-Funktionen.

  Neben Verbesserungen bei Intelligenz und Leistung bietet die Vorabversion von Gemini 3 Pro neue Verhaltensweisen in Bezug auf:

  - [Media-Auflösung](https://ai.google.dev/gemini-api/docs/media-resolution?hl=de)
  - [Gedankensignaturen](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=de)
  - [Denkaufwand](https://ai.google.dev/gemini-api/docs/thinking?hl=de#thinking-levels)

  Im [Gemini 3 Developer Guide](https://ai.google.dev/gemini-api/docs/gemini-3?hl=de) finden Sie Informationen zur Migration, zu neuen Funktionen und zu den Spezifikationen.

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

  Verwenden Sie stattdessen [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=de#imagen-4). Weitere Informationen finden Sie in der [Tabelle zu Gemini-Einstellung](https://ai.google.dev/gemini-api/docs/deprecations?hl=de).

## 6. November 2025

- Die File Search API wurde als öffentliche Vorschau eingeführt. Damit können Entwickler Antworten mit ihren eigenen Daten fundieren. Weitere Informationen finden Sie auf der neuen Seite [Dateisuche](https://ai.google.dev/gemini-api/docs/file-search?hl=de).

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

  Außerdem wurden mit dieser Einführung weitere Optionen für die Videolänge der Veo 3-Ausgabe hinzugefügt: 4, 6 und 8 Sekunden.
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

- Das Gemini Robotics ER 1.5-Modell wurde in der Vorabversion veröffentlicht. [Übersicht über Robotik](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=de)
- Die folgenden Modelle in der Vorabversion wurden eingeführt:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Weitere Informationen finden Sie auf der Seite [Modelle](https://ai.google.dev/gemini-api/docs/models?hl=de).

## 23. September 2025

- Wir haben `gemini-2.5-flash-native-audio-preview-09-2025` veröffentlicht, ein neues natives Audiomodell für die Live API mit verbessertem Funktionsaufruf und verbesserter Verarbeitung von abgeschnittenen Sprachbeiträgen. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de) und unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-native-audio).

## 16. September 2025

- Ankündigung der Einstellung: Die folgenden Modelle werden im Oktober 2025 eingestellt:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Weitere Informationen zum neuesten Einbettungsmodell finden Sie auf der Seite [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de).

## 10. September 2025

- Unterstützung für das [Embeddings-Modell in der Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=de#batch-embedding) wurde eingeführt und die Batch API wurde der [OpenAI-Kompatibilitätsbibliothek](https://ai.google.dev/gemini-api/docs/openai?hl=de#batch) hinzugefügt, um den Einstieg in Batch-Anfragen noch einfacher zu gestalten.

## 9. September 2025

- Veo 3 und Veo 3 Fast sind jetzt allgemein verfügbar. Die Preise sind niedriger und es gibt neue Optionen für Seitenverhältnis, Auflösung und Seeding. Weitere Informationen finden Sie in der [Veo-Dokumentation](https://ai.google.dev/gemini-api/docs/video?hl=de#model-features).

## 26. August 2025

- Wir haben [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-image-preview) eingeführt, unser neuestes natives Modell zur Bildgenerierung.

## 18. August 2025

- Das [Tool für URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) ist jetzt allgemein verfügbar. Mit diesem Tool können Sie URLs als zusätzlichen Kontext für Prompts angeben. Die Unterstützung für die Verwendung des URL-Kontexts mit dem `gemini-2.0-flash`-Modell (während der experimentellen Veröffentlichung verfügbar) wird in einer Woche eingestellt.

## 14. August 2025

- Die Modelle Imagen 4 Ultra, Standard und Fast sind jetzt allgemein verfügbar. Weitere Informationen finden Sie auf der Seite [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=de).

## 7. August 2025

- Die `allow_adult`-Einstellung für die Funktion „Bild zu Video“ ist jetzt auch in eingeschränkten Regionen verfügbar. Weitere Informationen finden Sie auf der Seite [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=de#veo-model-parameters).

## 31. Juli 2025

- Die Bild-zu-Video-Funktion für das Veo 3-Vorschaumodell wurde eingeführt.
- Das Vorabmodell Veo 3 Fast wurde veröffentlicht.
- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de)

## 22. Juli 2025

- Wir haben `gemini-2.5-flash-lite` veröffentlicht, unser schnelles, kostengünstiges und leistungsstarkes Gemini 2.5-Modell. [Weitere Informationen zu Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-lite)

## Juli 17, 2025

- Wir haben `veo-3.0-generate-preview` eingeführt, das neueste Update für Veo, mit dem Videos mit Audio generiert werden können. [Veo](https://ai.google.dev/gemini-api/docs/video?hl=de)
- Höhere Ratenbegrenzungen für Imagen 4 Standard und Ultra. Weitere Informationen finden Sie auf der Seite [Ratenbeschränkungen](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de).

## 14. Juli 2025

- Wir haben `gemini-embedding-001` veröffentlicht, die stabile Version unseres Modelle für Texteinbettungen. Weitere Informationen finden Sie unter [Einbettungen](https://ai.google.dev/gemini-api/docs/embeddings?hl=de). Das `gemini-embedding-exp-03-07`-Modell wird am 14. August 2025 eingestellt.

## 7. Juli 2025

- Der Batch-Modus für die Gemini API wurde eingeführt. Anfragen in Batches zusammenfassen und asynchron an „process“ senden. Weitere Informationen finden Sie unter [Batchmodus](https://ai.google.dev/gemini-api/docs/batch-mode?hl=de).

## 26. Juni 2025

- Die Vorschauversionen der Modelle `gemini-2.5-pro-preview-05-06` und `gemini-2.5-pro-preview-03-25` werden jetzt zur neuesten stabilen Version `gemini-2.5-pro` weitergeleitet.
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

- Wir haben `gemini-2.5-pro-preview-06-05` veröffentlicht, eine neue Version unseres leistungsstärksten Modells, die jetzt adaptives Denken nutzt. Weitere Informationen finden Sie unter [Gemini 2.5 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro-preview-06-05) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).
  `gemini-2.5-pro-preview-05-06` wird am 26. Juni 2025 zu `gemini-2.5-pro` weitergeleitet.

## 27. Mai 2025

- Das letzte verfügbare Tuning-Modell, Gemini 1.5 Flash 001, wurde eingestellt.
  Die Abstimmung wird für keine Modelle mehr unterstützt.
  Weitere Informationen finden Sie unter [Gemini API für das Fine-Tuning](https://ai.google.dev/gemini-api/docs/model-tuning?hl=de).

## 20. Mai 2025

**API-Updates:**

- Unterstützung für die [benutzerdefinierte Videovorverarbeitung](https://ai.google.dev/gemini-api/docs/video-understanding?hl=de#customize-video-processing) mit Clipping-Intervallen und konfigurierbarer Framerate-Erfassung wurde eingeführt.
- Die Verwendung mehrerer Tools wurde eingeführt. Damit können Sie [Code-Ausführung](https://ai.google.dev/gemini-api/docs/code-execution?hl=de) und [Fundierung mit der Google Suche](https://ai.google.dev/gemini-api/docs/grounding?hl=de) in derselben `generateContent`-Anfrage konfigurieren.
- Unterstützung für [asynchrone Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/live-tools?hl=de#async-function-calling) in der Live API wurde eingeführt.
- Wir haben ein experimentelles [Tool für den URL-Kontext](https://ai.google.dev/gemini-api/docs/url-context?hl=de) eingeführt, mit dem Sie URLs als zusätzlichen Kontext für Prompts angeben können.

**Modell-Updates**:

- `gemini-2.5-flash-preview-05-20` wurde veröffentlicht, ein [Vorschaumodell](https://ai.google.dev/gemini-api/docs/models?hl=de#model-versions) von Gemini, das für Preis-Leistungs-Verhältnis und adaptives Denken optimiert ist. Weitere Informationen finden Sie unter [Gemini 2.5 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).
- Die Modelle [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-pro-preview-tts) und [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview-tts) wurden veröffentlicht. Sie können [Sprache mit einem oder zwei Sprechern generieren](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de).
- Wir haben das Modell `lyria-realtime-exp` veröffentlicht, das [Musik in Echtzeit generiert](https://ai.google.dev/gemini-api/docs/music-generation?hl=de).
- `gemini-2.5-flash-preview-native-audio-dialog` und `gemini-2.5-flash-exp-native-audio-thinking-dialog` wurden veröffentlicht, neue Gemini-Modelle für die Live API mit nativer Audioausgabe. Weitere Informationen finden Sie im [Live API-Leitfaden](https://ai.google.dev/gemini-api/docs/live-guide?hl=de#native-audio-output) und unter [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-native-audio).
- Die `gemma-3n-e4b-it`-Vorabversion wurde veröffentlicht und ist in [AI Studio](https://aistudio.google.com?hl=de) und über die Gemini API im Rahmen der Einführung von [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=de) verfügbar.

## 7. Mai 2025

- Wir haben `gemini-2.0-flash-preview-image-generation` veröffentlicht, ein Vorschau-Modell zum Generieren und Bearbeiten von Bildern. Weitere Informationen finden Sie unter [Bildgenerierung](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) und [Gemini 2.0 Flash Preview Image Generation](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.0-flash-preview-image-generation).

## 6. Mai 2025

- Wir haben `gemini-2.5-pro-preview-05-06` veröffentlicht, eine neue Version unseres leistungsstärksten Modells, mit Verbesserungen bei Code und Funktionsaufrufen. `gemini-2.5-pro-preview-03-25` verweist automatisch auf die neue Version des Modells.

## 17. April 2025

- `gemini-2.5-flash-preview-04-17` wurde veröffentlicht, ein [Vorschaumodell](https://ai.google.dev/gemini-api/docs/models?hl=de#model-versions) von Gemini, das für Preis-Leistungs-Verhältnis und adaptives Denken optimiert ist. Weitere Informationen finden Sie unter [Gemini 2.5 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.5-flash-preview) und [Denken](https://ai.google.dev/gemini-api/docs/thinking?hl=de).

## 16. April 2025

- Kontext-Caching für [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=de#gemini-2.0-flash) eingeführt.

## 9. April 2025

**Modell-Updates**:

- `veo-2.0-generate-001` wurde veröffentlicht, ein allgemein verfügbares (GA) Modell, das auf Text und Bildern basiert und detaillierte und künstlerisch anspruchsvolle Videos generieren kann. Weitere Informationen finden Sie in der [Veo-Dokumentation](https://ai.google.dev/gemini-api/docs/video?hl=de).
- Am `gemini-2.0-flash-live-001` wurde eine öffentliche Vorschauversion des [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de)-Modells mit aktivierter Abrechnung veröffentlicht.

  - **Verbesserte Sitzungsverwaltung und Zuverlässigkeit**

    - **Sitzung fortsetzen**:Sitzungen werden auch bei vorübergehenden Netzwerkunterbrechungen aufrechterhalten. Die API unterstützt jetzt die serverseitige Speicherung des Sitzungsstatus (bis zu 24 Stunden) und bietet Handles (session\_resumption) zum erneuten Verbinden und Fortsetzen der Wiedergabe.
    - **Längere Sitzungen durch Kontextkomprimierung**:Ermöglichen Sie längere Interaktionen als bisher. Konfigurieren Sie die Komprimierung des Kontextfensters mit einem gleitenden Fenstermechanismus, um die Kontextlänge automatisch zu verwalten und abrupte Beendigungen aufgrund von Kontextlimits zu verhindern.
    - **Benachrichtigung über das ordnungsgemäße Trennen der Verbindung**:Sie erhalten eine `GoAway`-Servermeldung, die angibt, wann eine Verbindung geschlossen wird. So können Sie die Verbindung vor dem Beenden ordnungsgemäß trennen.
  - **Mehr Kontrolle über die Interaktionsdynamik**
  - **Konfigurierbare Spracherkennung (Voice Activity Detection, VAD)**: Sie können die Empfindlichkeitsstufen auswählen oder die automatische VAD vollständig deaktivieren und neue Clientereignisse (`activityStart`, `activityEnd`) für die manuelle Sprachsteuerung verwenden.
  - **Konfigurierbare Unterbrechungsbehandlung**:Sie können festlegen, ob die Antwort des Modells durch Nutzereingaben unterbrochen werden soll.
  - **Konfigurierbare Abdeckung von Drehungen**:Wählen Sie aus, ob die API alle Audio- und Videoeingaben kontinuierlich verarbeitet oder nur dann erfasst, wenn der Endnutzer spricht.
  - **Konfigurierbare Media-Auflösung**:Sie können die Auflösung für Eingabemedien auswählen, um die Qualität oder die Token-Nutzung zu optimieren.
  - **Umfangreichere Ausgabe und Funktionen**
  - **Erweiterte Sprach- und Sprachausgabeoptionen**:Sie können jetzt aus zwei neuen Stimmen und 30 neuen Sprachen für die Audioausgabe wählen. Die Ausgabesprache kann jetzt in `speechConfig` konfiguriert werden.
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

- Aktualisierungen der [Kompatibilität mit OpenAI-Bibliotheken](https://ai.google.dev/gemini-api/docs/openai?hl=de).

## 6. Februar 2025

**Modell-Updates**:

- Wir haben `imagen-3.0-generate-002` veröffentlicht, eine allgemein verfügbare (GA) Version von [Imagen 3 in der Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=de).

**SDK-Updates:**

- Das [Google Gen AI SDK für Java](https://github.com/googleapis/java-genai) wurde für die öffentliche Vorschau veröffentlicht.

## 5. Februar 2025

**Modell-Updates**:

- Wir haben `gemini-2.0-flash-001` veröffentlicht, eine allgemein verfügbare (GA) Version von [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash), die nur Textausgabe unterstützt.
- `gemini-2.0-pro-exp-02-05` wurde eine [experimentelle](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=de) öffentliche Vorabversion von Gemini 2.0 Pro veröffentlicht.
- Wir haben `gemini-2.0-flash-lite-preview-02-05` veröffentlicht, eine experimentelle öffentliche [Modell](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash-lite)-Vorabversion, die für Kosteneffizienz optimiert ist.

**API-Updates:**

- Die Codeausführung unterstützt jetzt [Dateieingabe und Grafikausgabe](https://ai.google.dev/gemini-api/docs/code-execution?hl=de#input-output).

**SDK-Updates:**

- Das [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/) ist jetzt allgemein verfügbar (GA).

## 21. Januar 2025

**Modell-Updates**:

- Wir haben `gemini-2.0-flash-thinking-exp-01-21` veröffentlicht, die aktuelle Vorabversion des Modells, das dem [Gemini 2.0 Flash Thinking-Modell](https://ai.google.dev/gemini-api/docs/thinking?hl=de) zugrunde liegt.

## 19. Dezember 2024

**Modell-Updates**:

- Der Gemini 2.0 Flash Thinking-Modus ist jetzt in der öffentlichen Vorschau verfügbar. Der Denkmodus ist ein Berechnungsmodell für die Testzeit, mit dem Sie den Denkprozess des Modells sehen können, während es eine Antwort generiert. Außerdem werden Antworten mit besseren Schlussfolgerungsfähigkeiten erzeugt.

  Weitere Informationen zum Gemini 2.0 Flash Thinking-Modus finden Sie auf unserer [Übersichtsseite](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=de).

## 11. Dezember 2024

**Modell-Updates**:

- [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-2.0-flash) für die öffentliche Vorschau veröffentlicht. Hier ist eine unvollständige Liste der Funktionen von Gemini 2.0 Flash Experimental:
  - Doppelt so schnell wie Gemini 1.5 Pro
  - Bidirektionales Streaming mit unserer Live API
  - Multimodale Antwortgenerierung in Form von Text, Bildern und Sprache
  - Integrierte Tool-Nutzung mit Mehrfachdialog-Schlussfolgerungen, um Funktionen wie Codeausführung, Suche und Funktionsaufrufe zu nutzen

[Weitere Informationen zu Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=de)

## 21. November 2024

**Modell-Updates**:

- Wir haben `gemini-exp-1121` veröffentlicht, ein noch leistungsstärkeres experimentelles Gemini API-Modell.

**Modell-Updates**:

- Die Modellaliase `gemini-1.5-flash-latest` und `gemini-1.5-flash` wurden aktualisiert, um `gemini-1.5-flash-002` zu verwenden.
  - Änderung des Parameters `top_k`: Das Modell `gemini-1.5-flash-002` unterstützt `top_k`-Werte zwischen 1 und 41 (exklusiv).
    Werte über 40 werden in 40 geändert.

## 14. November 2024

**Modell-Updates**:

- Wir haben `gemini-exp-1114` veröffentlicht, ein leistungsstarkes experimentelles Gemini API-Modell.

## 8. November 2024

**API-Updates:**

- [Unterstützung für Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=de) in den OpenAI-Bibliotheken / der REST API wurde hinzugefügt.

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

- Den Modellantworten wurden „Mag ich“- und „Mag ich nicht“-Buttons hinzugefügt, damit Nutzer Feedback zur Qualität einer Antwort geben können.

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

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-pro) (`gemini-1.5-pro-001`) ist allgemein verfügbar.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de#gemini-1.5-flash) (`gemini-1.5-flash-001`) ist allgemein verfügbar.

## 14. Mai 2024

**API-Updates:**

- Ein Kontextfenster von 2 Millionen Tokens für Gemini 1.5 Pro wurde eingeführt (Warteliste).
- Das [Abrechnungsmodell „Pay as you go“](https://ai.google.dev/gemini-api/docs/billing?hl=de) für Gemini 1.0 Pro wurde eingeführt. Die Abrechnung für Gemini 1.5 Pro und Gemini 1.5 Flash folgt in Kürze.
- Die Ratenbegrenzungen für die kommende kostenpflichtige Version von Gemini 1.5 Pro wurden erhöht.
- Der [File API](https://ai.google.dev/api/rest/v1beta/files?hl=de) wurde integrierte Videounterstützung hinzugefügt.
- Unterstützung für Nur-Text in der [File API](https://ai.google.dev/api/rest/v1beta/files?hl=de) hinzugefügt.
- Unterstützung für parallele Funktionsaufrufe hinzugefügt, bei denen mehrere Aufrufe gleichzeitig zurückgegeben werden.

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
- [Modus für Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de#function_calling_mode) hinzugefügt, der das Ausführungsverhalten für Funktionsaufrufe definiert.
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
- aqa: Ein neues, speziell abgestimmtes Modell, das darauf trainiert ist, Fragen mithilfe von Textpassagen zu beantworten, um generierte Antworten zu fundieren.

Weitere Informationen finden Sie unter [Gemini-Modelle](https://ai.google.dev/gemini-api/docs/models/gemini?hl=de).

**Updates der API-Version:**

- v1: Der stabile API-Channel.
- v1beta: Betaversion Dieser Kanal hat Funktionen, die sich möglicherweise noch in der Entwicklung befinden.

Weitere Informationen finden Sie im [Thema zu API-Versionen](https://ai.google.dev/gemini-api/docs/api-versions?hl=de).

**API-Updates:**

- `GenerateContent` ist ein einheitlicher Endpunkt für Chat und Text.
- Streaming über die Methode `StreamGenerateContent` verfügbar.
- Multimodale Funktion: Bilder sind ein neuer unterstützter Modus
- Neue Betafunktionen:
  - [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de)
  - Attributed Question Answering (AQA)
- Aktualisierte Anzahl der Kandidaten: Gemini-Modelle geben nur einen Kandidaten zurück.
- Unterschiedliche Sicherheitseinstellungen und Altersfreigabekategorien. Weitere Informationen finden Sie unter [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).
- Das Optimieren von Modellen wird für Gemini-Modelle noch nicht unterstützt (wird gerade entwickelt).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-01 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-01 (UTC)."],[],[]]
