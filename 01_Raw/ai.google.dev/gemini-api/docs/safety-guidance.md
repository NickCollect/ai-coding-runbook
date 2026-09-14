---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=de
fetched_at: 2026-09-14T05:45:02.466264+00:00
title: "Richtlinien zu Sicherheit und Faktualit\u00e4t \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Richtlinien zu Sicherheit und Faktualität

Modelle, die auf generativer künstlicher Intelligenz basieren, sind leistungsstarke Tools, haben aber auch ihre Grenzen. Ihre Vielseitigkeit und Anwendbarkeit können manchmal zu unerwarteten Ausgaben führen, z. B. zu Ausgaben, die ungenau, voreingenommen oder anstößig sind. Nachbearbeitung und strenge manuelle Bewertung sind unerlässlich, um das Risiko von Schäden durch solche Ausgaben zu begrenzen.

Die von der Gemini API bereitgestellten Modelle können für eine Vielzahl von Anwendungen für generative KI und Verarbeitung natürlicher Sprache (Natural Language Processing, NLP) verwendet werden. Die Nutzung dieser Funktionen ist nur über die Gemini API oder die Google AI Studio Web-App möglich. Ihre Nutzung der Gemini API unterliegt außerdem der [Richtlinie zur unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de) und den [Nutzungsbedingungen für die Gemini API](https://ai.google.dev/terms?hl=de).

Large Language Models (LLMs) sind unter anderem deshalb so nützlich, weil sie kreative Tools sind, die viele verschiedene sprachliche Aufgaben bewältigen können. Leider bedeutet das auch, dass Large Language Models unerwartete Ausgaben generieren können, einschließlich Text, der beleidigend, grob oder tatsächlich falsch ist.
Außerdem ist es durch die unglaubliche Vielseitigkeit dieser Modelle schwierig, vorherzusagen, welche Art unerwünschter Ausgaben sie erzeugen könnten. Die Gemini API wurde unter Berücksichtigung der [KI-Grundsätze von Google](https://ai.google/principles/?hl=de) entwickelt. Es liegt jedoch in der Verantwortung der Entwickler, diese Modelle verantwortungsbewusst einzusetzen. Um Entwickler bei der Erstellung sicherer und verantwortungsbewusster Anwendungen zu unterstützen, bietet die Gemini API eine integrierte Inhaltsfilterung sowie anpassbare Sicherheitseinstellungen für vier Arten von schädlichen Inhalten. Weitere Informationen finden Sie im Leitfaden zu den [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de). Außerdem ist die Verknüpfung mit der Google Suche aktiviert, um die Faktizität zu verbessern. Diese Funktion kann jedoch für Entwickler deaktiviert werden, deren Anwendungsfälle eher kreativ sind und nicht auf die Suche nach Informationen ausgerichtet sind.

In diesem Dokument werden einige Sicherheitsrisiken vorgestellt, die bei der Verwendung von LLMs auftreten können. Außerdem werden neue Empfehlungen für das Sicherheitsdesign und die Sicherheitsentwicklung gegeben. Gesetze und Verordnungen können ebenfalls Einschränkungen auferlegen. Diese werden in dieser Anleitung jedoch nicht berücksichtigt.

Wir empfehlen die folgenden Schritte beim Erstellen von Anwendungen mit LLMs:

- Sicherheitsrisiken Ihrer Anwendung
- Anpassungen zur Minimierung von Sicherheitsrisiken
- Für Ihren Anwendungsfall geeignete Sicherheitstests durchführen
- Nutzerfeedback einholen und Nutzung überwachen

Die Anpassungs- und Testphasen sollten iterativ durchlaufen werden, bis Sie eine für Ihre Anwendung geeignete Leistung erzielen.

![Zyklus der Modellimplementierung](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=de)

## Sicherheitsrisiken Ihrer Anwendung verstehen

In diesem Zusammenhang wird Sicherheit als die Fähigkeit eines LLM definiert, seinen Nutzern keinen Schaden zuzufügen, z. B. durch die Generierung von toxischen Formulierungen oder Inhalten, die Stereotype fördern. Die über die Gemini API verfügbaren Modelle wurden unter Berücksichtigung der [KI-Grundsätze von Google](https://ai.google/principles/?hl=de) entwickelt und Ihre Nutzung unterliegt der [Richtlinie zu verbotenen Anwendungsfällen für generative KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de). Die API bietet integrierte Sicherheitsfilter, um einige häufige Probleme mit Sprachmodellen wie toxische Formulierungen und Hassreden zu beheben und Inklusivität und die Vermeidung von Stereotypen zu fördern. Jede Anwendung kann jedoch unterschiedliche Risiken für ihre Nutzer bergen. Als Anwendungsentwickler sind Sie daher dafür verantwortlich, Ihre Nutzer und die potenziellen Schäden zu kennen, die Ihre Anwendung verursachen kann, und dafür zu sorgen, dass Ihre Anwendung LLMs sicher und verantwortungsbewusst verwendet.

Im Rahmen dieser Bewertung sollten Sie die Wahrscheinlichkeit eines Schadens, dessen Schweregrad und die Maßnahmen zur Risikominderung berücksichtigen. Eine App, die beispielsweise Essays auf der Grundlage von Fakten erstellt, muss sorgfältiger darauf achten, Falschinformationen zu vermeiden, als eine App, die fiktive Geschichten zur Unterhaltung generiert. Eine gute Möglichkeit, potenzielle Sicherheitsrisiken zu untersuchen, besteht darin, Ihre Endnutzer und andere Personen, die von den Ergebnissen Ihrer Anwendung betroffen sein könnten, zu befragen. Das kann viele Formen annehmen, z. B. die Recherche nach dem aktuellen Stand der Forschung in Ihrer App-Domain, die Beobachtung, wie Nutzer ähnliche Apps verwenden, oder die Durchführung einer Nutzerstudie, Umfrage oder informeller Interviews mit potenziellen Nutzern.

### Weitere Tipps

- Sprechen Sie mit einer vielfältigen Gruppe potenzieller Nutzer aus Ihrer Zielgruppe über Ihre Anwendung und ihren beabsichtigten Zweck, um eine breitere Perspektive auf potenzielle Risiken zu erhalten und die Diversitätskriterien bei Bedarf anzupassen.
- Das [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) des National Institute of Standards and Technology (NIST) der US-Regierung bietet detailliertere Anleitungen und zusätzliche Lernressourcen für das Risikomanagement im Bereich KI.
- In der [Publikation von DeepMind zu den ethischen und sozialen Risiken von Language Models](https://arxiv.org/abs/2112.04359) wird detailliert beschrieben, wie Anwendungen von Language Models Schaden anrichten können.

## Anpassungen vornehmen, um Risiken in Bezug auf Sicherheit und Faktualität zu minimieren

Nachdem Sie die Risiken kennen, können Sie entscheiden, wie Sie sie minimieren. Die Entscheidung, welche Risiken priorisiert werden sollen und wie viel Sie tun sollten, um sie zu vermeiden, ist von entscheidender Bedeutung. Sie ähnelt der Priorisierung von Fehlern in einem Softwareprojekt. Nachdem Sie die Prioritäten festgelegt haben, können Sie überlegen, welche Arten von Maßnahmen am besten geeignet wären. Oft können schon einfache Änderungen einen Unterschied machen und Risiken verringern.

Berücksichtigen Sie beispielsweise beim Entwerfen einer Anwendung Folgendes:

- **Modellausgabe anpassen**, damit sie besser widerspiegelt, was in Ihrem Anwendungskontext akzeptabel ist. Durch die Abstimmung kann die Ausgabe des Modells vorhersehbarer und konsistenter werden, was dazu beitragen kann, bestimmte Risiken zu mindern.
- **Eine Eingabemethode, die sicherere Ausgaben ermöglicht**: Die genaue Eingabe, die Sie einem LLM geben, kann sich auf die Qualität der Ausgabe auswirken.
  Es lohnt sich, mit Eingabeaufforderungen zu experimentieren, um herauszufinden, was in Ihrem Anwendungsfall am sichersten funktioniert. So können Sie eine UX bereitstellen, die dies erleichtert. Sie können beispielsweise festlegen, dass Nutzer nur aus einer Drop-down-Liste mit Eingabeaufforderungen auswählen dürfen, oder Pop-up-Vorschläge mit beschreibenden Formulierungen anbieten, die in Ihrem Anwendungskontext sicher sind.
- **Blockieren unsicherer Eingaben und Filtern der Ausgabe, bevor sie dem Nutzer angezeigt wird**: In einfachen Fällen können Sperrlisten verwendet werden, um unsichere Wörter oder Formulierungen in Prompts oder Antworten zu identifizieren und zu blockieren.Alternativ können menschliche Prüfer solche Inhalte manuell ändern oder blockieren.
- **Verwendung trainierter Klassifikatoren, um jedem Prompt Tags für mögliche schädliche Inhalte oder bösartige Signale hinzuzufügen.** Je nach der Art des erkannten schädlichen Inhalts können dann verschiedene Strategien für den Umgang mit der Anfrage angewendet werden. Wenn die Eingabe beispielsweise offensichtlich bösartig oder missbräuchlich ist, kann sie blockiert und stattdessen eine vordefinierte Antwort ausgegeben werden.
  **Erweiterter Tipp**:Wenn Signale darauf hindeuten, dass die Ausgabe schädlich ist, kann die Anwendung die folgenden Optionen verwenden:

  - Eine Fehlermeldung oder eine vordefinierte Ausgabe zurückgeben
  - Versuchen Sie es noch einmal mit dem Prompt. Möglicherweise wird eine alternative, sichere Ausgabe generiert, da derselbe Prompt manchmal zu unterschiedlichen Ausgaben führt.
- **Schutzmaßnahmen gegen vorsätzlichen Missbrauch**, z. B. durch Zuweisen einer eindeutigen ID für jeden Nutzer und Festlegen eines Limits für die Anzahl der Nutzeranfragen, die in einem bestimmten Zeitraum gesendet werden können. Eine weitere Schutzmaßnahme ist der Schutz vor möglichen Prompt Injections. Prompt-Injection ist wie SQL-Injection eine Methode, mit der böswillige Nutzer einen Eingabe-Prompt erstellen, der die Ausgabe des Modells manipuliert. Sie können beispielsweise einen Eingabe-Prompt senden, der das Modell anweist, alle vorherigen Beispiele zu ignorieren. Weitere Informationen zum vorsätzlichen Missbrauch finden Sie in der [Richtlinie zur unzulässigen Nutzung von generativer KI](https://policies.google.com/terms/generative-ai/use-policy?hl=de).
- **Funktionen anpassen, um das Risiko zu senken**
  Aufgaben mit einem engeren Umfang (z.B. das Extrahieren von Keywords aus Textpassagen) oder mit einer stärkeren menschlichen Aufsicht (z.B. das Generieren von Kurzvideos, die von einem Menschen überprüft werden) bergen oft ein geringeres Risiko. Anstatt eine Anwendung zu erstellen, die eine E‑Mail-Antwort von Grund auf neu schreibt, könnten Sie sie beispielsweise darauf beschränken, eine Gliederung zu erweitern oder alternative Formulierungen vorzuschlagen.
- **Sicherheitseinstellungen für schädliche Inhalte anpassen, um die Wahrscheinlichkeit zu verringern, dass Antworten angezeigt werden, die möglicherweise schädlich sind**: Die Gemini API bietet Sicherheitseinstellungen, die Sie während der Prototyping-Phase anpassen können, um festzustellen, ob Ihre Anwendung eine mehr oder weniger restriktive Sicherheitskonfiguration erfordert. Sie können diese Einstellungen in fünf Filterkategorien anpassen, um bestimmte Arten von Inhalten zuzulassen oder zu beschränken. Weitere Informationen zu den über die Gemini API verfügbaren anpassbaren Sicherheitseinstellungen finden Sie im [Leitfaden zu Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).
- **Potenzielle sachliche Ungenauigkeiten oder Halluzinationen verringern, indem Sie Fundierung mit der Google Suche aktivieren**. Viele KI-Modelle sind experimentell und können faktisch ungenaue Informationen liefern, halluzinieren oder auf andere Weise problematische Ausgaben erzeugen. Durch die Funktion „Fundierung mit der Google Suche“ wird das Gemini-Modell in Echtzeit mit Webinhalten verbunden und kann mit allen verfügbaren Sprachen genutzt werden. So kann Gemini genauere Antworten geben und überprüfbare Quellen zitieren, die über den Wissensstichtag des Modells hinausgehen.

## Führen Sie für Ihren Anwendungsfall geeignete Sicherheitstests durch.

Tests sind ein wichtiger Bestandteil der Entwicklung robuster und sicherer Anwendungen. Umfang, Geltungsbereich und Strategien für Tests variieren jedoch. Ein Haiku-Generator, der nur zum Spaß verwendet wird, birgt wahrscheinlich weniger schwerwiegende Risiken als eine Anwendung, die für Anwaltskanzleien entwickelt wurde, um juristische Dokumente zusammenzufassen und Verträge zu entwerfen. Der Haiku-Generator kann jedoch von einer Vielzahl von Nutzern verwendet werden, was bedeutet, dass das Potenzial für feindselige Versuche oder sogar unbeabsichtigte schädliche Eingaben größer sein kann. Auch der Implementierungskontext ist wichtig. So kann beispielsweise eine Anwendung, deren Ausgaben vor dem Ergreifen von Maßnahmen von menschlichen Experten überprüft werden, als weniger wahrscheinlich eingestuft werden, dass sie schädliche Ausgaben erzeugt, als die identische Anwendung ohne diese Aufsicht.

Es ist nicht ungewöhnlich, dass Sie mehrere Iterationen durchlaufen, in denen Sie Änderungen vornehmen und testen, bevor Sie sich sicher fühlen, dass Sie bereit für die Veröffentlichung sind. Das gilt auch für Anwendungen mit relativ geringem Risiko. Für KI-Anwendungen sind zwei Arten von Tests besonders nützlich:

- Beim **Sicherheits-Benchmarking** werden Sicherheitsmesswerte entwickelt, die widerspiegeln, wie Ihre Anwendung im Kontext der wahrscheinlichen Nutzung unsicher sein könnte. Anschließend wird anhand von Bewertungs-Datasets getestet, wie gut Ihre Anwendung bei den Messwerten abschneidet. Es empfiehlt sich, vor dem Testen über die minimal akzeptablen Werte für Sicherheitsmesswerte nachzudenken, damit Sie 1) die Testergebnisse anhand dieser Erwartungen bewerten und 2) das Bewertungs-Dataset basierend auf den Tests zusammenstellen können, mit denen die Messwerte bewertet werden, die Ihnen am wichtigsten sind.

  **Tipps für Fortgeschrittene:**

  - Verlassen Sie sich nicht zu sehr auf Standardansätze, da Sie wahrscheinlich eigene Testdatensätze mit menschlichen Ratern erstellen müssen, um den Kontext Ihrer Anwendung vollständig zu berücksichtigen.
  - Wenn Sie mehrere Messwerte haben, müssen Sie entscheiden, wie Sie vorgehen, wenn eine Änderung zu Verbesserungen bei einem Messwert führt, aber sich negativ auf einen anderen auswirkt. Wie bei anderen Leistungsoptimierungen sollten Sie sich eher auf die Worst-Case-Leistung in Ihrem Auswertungsset als auf die durchschnittliche Leistung konzentrieren.
- Beim **Adversarial Testing** wird proaktiv versucht, Ihre Anwendung zu manipulieren. Ziel ist es, Schwachstellen zu identifizieren, damit Sie geeignete Maßnahmen ergreifen können, um sie zu beheben. Für Adversarial Testing sind möglicherweise erhebliche Zeit und Mühe von Prüfern mit Fachwissen in Ihrer Anwendung erforderlich. Je mehr Sie jedoch testen, desto größer ist die Wahrscheinlichkeit, Probleme zu erkennen, insbesondere solche, die selten oder erst nach wiederholten Ausführungen der Anwendung auftreten.

  - Adversarial Testing ist ein Verfahren zur systematischen Bewertung eines ML-Modells, um zu ermitteln, wie es sich bei beabsichtigten oder unbeabsichtigten schädlichen Eingaben verhält:
    - Eine Eingabe kann absichtlich schädlich sein, wenn sie eindeutig darauf abzielt, eine sicherheitsrelevante oder schädliche Ausgabe zu erzeugen. Ein Beispiel: Ein Modell zur Textgenerierung wird aufgefordert, eine Hassrede über eine bestimmte Religion zu generieren.
    - Eine Eingabe ist unbeabsichtigt schädlich, wenn die Eingabe selbst zwar harmlos ist, aber eine schädliche Ausgabe erzeugt. Ein Beispiel: Ein Modell zur Textgenerierung wird durch eine Eingabe aufgefordert, eine Person mit einer bestimmten ethnischen Zugehörigkeit zu beschreiben. Es gibt anschließend eine rassistische Ausgabe zurück.
  - Ein Adversarial Test unterscheidet sich von einer Standardauswertung durch die Zusammensetzung der für den Test verwendeten Daten. Wählen Sie für Adversarial Testing Testdaten aus, die mit hoher Wahrscheinlichkeit problematische Ausgaben des Modells hervorrufen. Das bedeutet, dass das Verhalten des Modells in Bezug auf alle Arten von möglichen Schäden untersucht wird, einschließlich seltener oder ungewöhnlicher Beispiele und Grenzfälle, die für Sicherheitsrichtlinien relevant sind. Außerdem sollte es Vielfalt in den verschiedenen Dimensionen eines Satzes wie Struktur, Bedeutung und Länge geben. Weitere Informationen dazu, was beim Erstellen eines Testdatensatzes zu beachten ist, finden Sie unter [Google's Responsible AI practices in fairness](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=de).
    **Tipps für Fortgeschrittene:**
  - Verwenden Sie [automatisierte Tests](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=de) anstelle der herkömmlichen Methode, bei der Personen in „Red Teams“ eingesetzt werden, um zu versuchen, Ihre Anwendung zu manipulieren. Beim automatisierten Testen ist das „Red Team“ ein weiteres Language Model, das Eingabetext findet, der schädliche Ausgaben des zu testenden Modells hervorruft.

## Auf Probleme achten

Egal wie viel Sie testen und wie viele Maßnahmen Sie ergreifen, Sie können nie Perfektion garantieren. Planen Sie daher im Voraus, wie Sie auftretende Probleme erkennen und beheben. Gängige Ansätze sind das Einrichten eines überwachten Kanals, über den Nutzer Feedback geben können (z. B. „Gefällt mir“-Bewertung), und das Durchführen einer Nutzerstudie, um proaktiv Feedback von einer vielfältigen Gruppe von Nutzern einzuholen. Das ist besonders wertvoll, wenn die Nutzungsmuster von den Erwartungen abweichen.

### Weitere Tipps

- Wenn Nutzer Feedback zu KI-Produkten geben, kann dies die KI-Leistung und die Nutzerfreundlichkeit im Laufe der Zeit erheblich verbessern. So können Sie beispielsweise bessere Beispiele für die Optimierung von Prompts auswählen. Im [Kapitel „Feedback und Kontrolle“](https://pair.withgoogle.com/chapter/feedback-controls/) im [Leitfaden „Menschen und KI“ von Google](https://pair.withgoogle.com/guidebook/chapters) finden Sie wichtige Aspekte, die Sie bei der Entwicklung von Feedbackmechanismen berücksichtigen sollten.

## Nächste Schritte

- Im [Leitfaden zu Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de) finden Sie Informationen zu den anpassbaren Sicherheitseinstellungen, die über die Gemini API verfügbar sind.
- [Hier finden Sie eine Einführung in das Verfassen von Prompts](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-06-05 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-06-05 (UTC)."],[],[]]
