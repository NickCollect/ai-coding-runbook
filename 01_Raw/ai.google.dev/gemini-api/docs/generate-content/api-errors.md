---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=de
fetched_at: 2026-08-17T02:30:24.722560+00:00
title: "API-Fehler \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# API-Fehler

Auf dieser Seite finden Sie eine Referenz zu Backend-Fehlercodes, die von der `GenerateContent` API zurückgegeben werden. Außerdem wird das gRPC-Fehlerantwortformat beschrieben und es werden Schritte zur Fehlerbehebung bereitgestellt.

## HTTP-Fehlercodes

In der folgenden Tabelle sind häufige Backend-Fehlercodes, Erklärungen zu ihren Ursachen und empfohlene Lösungen aufgeführt:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP-Code** | **Status** | **Beschreibung** | **Beispiel** | **Lösung** |
| 400 | INVALID\_ARGUMENT | Der Anfragetext ist fehlerhaft. | Ihre Anfrage enthält einen Tippfehler oder ein erforderliches Feld fehlt. | In der [API-Referenz](https://ai.google.dev/api?hl=de) finden Sie Informationen zum Anfrageformat, Beispiele und unterstützte Versionen. Die Verwendung von Funktionen aus einer neueren API-Version mit einem älteren Endpunkt kann zu Fehlern führen. |
| 400 | FAILED\_PRECONDITION | Die kostenlose Stufe der Gemini API ist in Ihrem Land nicht verfügbar. Aktivieren Sie die Abrechnung für Ihr Projekt in Google AI Studio. | Sie senden eine Anfrage in einer Region, in der die kostenlose Stufe nicht unterstützt wird, und Sie haben die Abrechnung für Ihr Projekt in Google AI Studio nicht aktiviert. | Wenn Sie die Gemini API verwenden möchten, müssen Sie in [Google AI Studio](https://aistudio.google.com/apikey?hl=de) einen kostenpflichtigen Plan einrichten. |
| 403 | PERMISSION\_DENIED | Ihr API-Schlüssel hat nicht die erforderlichen Berechtigungen. | Sie verwenden den falschen API-Schlüssel oder versuchen, ein optimiertes Modell zu verwenden, ohne die [entsprechende Authentifizierung](https://ai.google.dev/gemini-api/docs/model-tuning?hl=de) durchzuführen. | Prüfen Sie, ob Ihr API-Schlüssel festgelegt ist und die richtigen Zugriffsberechtigungen hat. Außerdem müssen Sie die entsprechende Authentifizierung durchführen, um optimierte Modelle zu verwenden. |
| 404 | NOT\_FOUND | Die angeforderte Ressource wurde nicht gefunden. | Eine in Ihrer Anfrage referenzierte Bild-, Audio- oder Videodatei wurde nicht gefunden. | Prüfen Sie, ob alle Parameter in Ihrer Anfrage für Ihre API-Version gültig sind. |
| 429 | RESOURCE\_EXHAUSTED | Sie haben eines der Ratenlimits der API überschritten (Anfragen pro Minute, Tokens pro Minute, Anfragen pro Tag, Ausgaben usw.). | Sie senden zu viele Anfragen, verwenden zu viele Tokens oder überschreiten ausgabenbasierte Limits für den Abrechnungsverlauf und die Stufe Ihres Kontos. | Prüfen Sie, ob Sie die [Ratenlimits](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de) des Modells einhalten. Warten Sie kurz und versuchen Sie es dann noch einmal. Reduzieren Sie die Rate oder Größe Ihrer Anfragen. [Fordern Sie bei Bedarf eine Erhöhung des Ratenlimits an](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de#request-rate-limit-increase). |
| 499 | CANCELLED | Der Vorgang wurde abgebrochen, üblicherweise vom Aufrufer. | Der Client hat die Verbindung geschlossen, bevor die API die Antwort senden konnte. | Prüfen Sie, ob Ihre Client- oder Netzwerkinfrastruktur die Verbindung vorzeitig schließt (z.B. aufgrund eines clientseitigen Timeouts). |
| 500 | INTERN | Bei Google ist ein unerwarteter Fehler aufgetreten. | Ihr Eingabekontext ist zu lang. | Auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de) finden Sie Informationen zu laufenden Vorfällen. Reduzieren Sie den Eingabekontext oder wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob das Problem dadurch behoben wird. Alternativ können Sie auch etwas warten und die Anfrage noch einmal senden. Wenn das Problem nach dem Wiederholen weiterhin besteht, melden Sie es über die Schaltfläche **Feedback senden** in Google AI Studio. |
| 503 | UNAVAILABLE | Der Dienst ist möglicherweise vorübergehend überlastet oder nicht verfügbar. | Der Dienst hat vorübergehend nicht genügend Kapazität. | Auf der [Statusseite der Gemini API](https://aistudio.google.com/status?hl=de) finden Sie Informationen zu laufenden Vorfällen. Wechseln Sie vorübergehend zu einem anderen Modell (z.B. von Gemini 2.5 Pro zu Gemini 2.5 Flash) und prüfen Sie, ob das Problem dadurch behoben wird. Alternativ können Sie auch etwas warten und die Anfrage noch einmal senden. Wenn das Problem nach dem Wiederholen weiterhin besteht, melden Sie es über die Schaltfläche **Feedback senden** in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Der Dienst kann die Verarbeitung nicht innerhalb der Frist abschließen. | Ihr Prompt (oder Kontext) ist zu groß, um rechtzeitig verarbeitet zu werden. | Legen Sie in Ihrer Clientanfrage einen längeren Timeout fest, um diesen Fehler zu vermeiden. |

## Format der Fehlerantwort

Wenn eine `GenerateContent`-Anfrage fehlschlägt, legt die API den HTTP-Statuscode fest (z. B. `400 Bad Request`, `403 Forbidden` oder `429 Too Many Requests`) und gibt einen JSON-Antworttext mit gRPC-Statusdetails zurück:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Feld | Typ | Beschreibung |
| --- | --- | --- |
| `code` | integer | Der HTTP-Statuscode. |
| `message` | String | Eine für Menschen lesbare Beschreibung des Fehlers. |
| `status` | String | Der gRPC-Statuscode in `SCREAMING_CASE`. |
| `details` | Array | Zusätzlicher Fehlerkontext, z. B. `ErrorInfo` oder `LocalizedMessage`. |

## Nächste Schritte

- [Fehlerbehebung bei der API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=de): Häufige Probleme und Fehlerszenarien beheben
- [Ratenlimits](https://ai.google.dev/gemini-api/docs/rate-limits?hl=de): Informationen zu Anfragelimits und Kontingentverwaltung

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
