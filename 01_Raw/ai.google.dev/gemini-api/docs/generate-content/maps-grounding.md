---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=de
fetched_at: 2026-08-17T02:20:26.652384+00:00
title: "Fundierung mit Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Fundierung mit Google Maps

Die Fundierung mit Google Maps verbindet die generativen Funktionen von Gemini mit den umfangreichen, faktischen und aktuellen Daten von Google Maps. Mit dieser Funktion können Entwickler standortbezogene Funktionen ganz einfach in ihre Anwendungen einbinden. Wenn eine Nutzeranfrage einen Kontext mit Bezug auf Google Maps-Daten hat, nutzt das Gemini-Modell Google Maps, um faktisch korrekte und aktuelle Antworten zu geben, die für den angegebenen Standort oder den ungefähren Ort des Nutzers relevant sind.

- **Genaue, standortbezogene Antworten**:Nutzen Sie die umfangreichen und aktuellen Daten von Google Maps für geografisch spezifische Anfragen.
- **Verbesserte Personalisierung**:Passen Sie Empfehlungen und Informationen an die vom Nutzer angegebenen Standorte an.

## Jetzt starten

In diesem Beispiel wird gezeigt, wie Sie die Fundierung mit Google Maps in Ihre Anwendung einbinden, um genaue, standortbezogene Antworten auf Nutzeranfragen zu geben. Der Prompt fragt nach lokalen Empfehlungen mit einem optionalen Nutzerstandort, sodass das Gemini-Modell Google Maps-Daten verwenden kann.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## So funktioniert die Fundierung mit Google Maps

Bei der Fundierung mit Google Maps wird die Gemini API in das Google Geo-Ökosystem eingebunden, indem die Maps API als Fundierungsquelle verwendet wird. Wenn die Anfrage eines Nutzers einen geografischen Kontext enthält, kann das Gemini-Modell das Tool „Fundierung mit Google Maps“ aufrufen. Das Modell kann dann Antworten generieren, die auf Google Maps-Daten basieren, die für den angegebenen Standort relevant sind.

Der Prozess umfasst in der Regel Folgendes:

1. **Nutzeranfrage**:Ein Nutzer sendet eine Anfrage an Ihre Anwendung, die möglicherweise einen geografischen Kontext enthält (z.B. „Cafés in meiner Nähe“ oder „Museen in San Francisco“).
2. **Toolaufruf**:Das Gemini-Modell erkennt die geografische Absicht und ruft das Tool „Fundierung mit Google Maps“ auf. Optional können diesem Tool die `latitude` und `longitude` des Nutzers übergeben werden. Das Tool ist ein Textsuchtool und verhält sich ähnlich wie die Suche in Google Maps. Bei lokalen Anfragen („in meiner Nähe“) werden die Koordinaten verwendet, während spezifische oder nicht lokale Anfragen wahrscheinlich nicht vom expliziten Standort beeinflusst werden.
3. **Datenabruf**:Der Dienst „Fundierung mit Google Maps“ fragt Google Maps nach relevanten Informationen ab (z.B. Orte, Rezensionen, Fotos, Adressen, Öffnungszeiten).
4. **Fundierte Generierung**:Die abgerufenen Google Maps-Daten werden verwendet, um die Antwort des Gemini-Modells zu informieren und so die faktische Richtigkeit und Relevanz zu gewährleisten.
5. **Antwort**:Das Modell gibt eine Textantwort zurück, die Zitate aus Google Maps-Quellen enthält.

## Gründe und Anwendungsfälle für die Fundierung mit Google Maps

Die Fundierung mit Google Maps ist ideal für Anwendungen, die genaue, aktuelle und standortspezifische Informationen erfordern. Sie verbessert die Nutzererfahrung, indem sie relevante und personalisierte Inhalte bereitstellt, die auf der umfangreichen Google Maps-Datenbank mit über 250 Millionen Orten weltweit basieren.

Sie sollten die Fundierung mit Google Maps verwenden, wenn Ihre Anwendung Folgendes tun muss:

- Vollständige und genaue Antworten auf geografisch spezifische Fragen geben
- Konversationelle Reiseplaner und lokale Reiseführer erstellen
- Sehenswürdigkeiten basierend auf dem Standort und den Nutzerpräferenzen wie Restaurants oder Geschäfte empfehlen
- Standortbezogene Funktionen für soziale Dienste, Einzelhandelsdienste oder Essenslieferdienste erstellen

Die Fundierung mit Google Maps eignet sich besonders für Anwendungsfälle, in denen Nähe und aktuelle faktische Daten entscheidend sind, z. B. wenn Sie nach dem „besten Café in meiner Nähe“ suchen oder eine Wegbeschreibung abrufen möchten.

## API-Methoden und -Parameter

Die Fundierung mit Google Maps wird über die Gemini API als Tool in
der [`generateContent`](https://ai.google.dev/api/generate-content?hl=de) Methode bereitgestellt. Sie aktivieren und konfigurieren
die Fundierung mit Google Maps, indem Sie ein
[`googleMaps`](https://ai.google.dev/api/caching?hl=de#GoogleMaps)-Objekt in den `tools`-Parameter Ihrer
Anfrage einfügen.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Außerdem unterstützt das Tool die Übergabe des Kontextstandorts als `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Informationen zur Fundierungsantwort

Wenn eine Antwort erfolgreich mit Google Maps-Daten fundiert wurde, enthält sie das Feld [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=de#GroundingMetadata).
Diese strukturierten Daten sind wichtig, um Behauptungen zu überprüfen und eine umfassende Zitatfunktion in Ihrer Anwendung zu erstellen sowie die Anforderungen an die Dienstnutzung zu erfüllen.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Die Gemini API gibt die folgenden Informationen mit der
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=de#GroundingMetadata) zurück:

- `groundingChunks`: Array von Objekten, die die `maps`-Quellen (`uri`, `placeId` und `title`) enthalten.
- `groundingSupports`: Array von Chunks, um den Antworttext des Modells mit den Quellen in `groundingChunks` zu verknüpfen. Jeder Chunk verknüpft einen Textbereich (definiert durch `startIndex` und `endIndex`) mit einem oder mehreren `groundingChunkIndices`. Dies ist der Schlüssel zum Erstellen von Inline-Zitaten.

Ein Code-Snippet zum Rendern von Inline-Zitaten in Text finden Sie im [the
example](https://ai.google.dev/gemini-api/docs/google-search?hl=de#attributing_sources_with_inline_citations)
in der Dokumentation zur Fundierung mit der Google Suche.

## Anwendungsfälle

Die Fundierung mit Google Maps unterstützt eine Vielzahl von standortbezogenen Anwendungsfällen. Die folgenden Beispiele zeigen, wie verschiedene Prompts und Parameter die Fundierung mit Google Maps nutzen können. Informationen in den fundierten Google Maps-Ergebnissen können von den tatsächlichen Gegebenheiten abweichen.

### Ortsbezogene Fragen beantworten

Stellen Sie detaillierte Fragen zu einem bestimmten Ort, um Antworten zu erhalten, die auf Google-Nutzerrezensionen und anderen Google Maps-Daten basieren.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Standortbezogene Personalisierung bereitstellen

Erhalten Sie Empfehlungen, die auf die Vorlieben eines Nutzers und eine bestimmte geografische Region zugeschnitten sind.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Bei der Reiseplanung helfen

Erstellen Sie mehrtägige Pläne mit Wegbeschreibungen und Informationen zu verschiedenen Orten, die sich perfekt für Reiseanwendungen eignen.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Anforderungen an die Dienstnutzung

In diesem Abschnitt werden die Anforderungen an die Dienstnutzung für die Fundierung mit Google Maps beschrieben.

### Nutzer über die Verwendung von Google Maps-Quellen informieren

Mit jedem fundierten Google Maps-Ergebnis erhalten Sie in `groundingChunks` Quellen, die die jeweilige Antwort unterstützen. Außerdem werden die folgenden Metadaten zurückgegeben:

- Quell-URI
- Titel
- ID

Wenn Sie Ergebnisse aus der Fundierung mit Google Maps präsentieren, müssen Sie die zugehörigen Google Maps-Quellen angeben und Ihre Nutzer über Folgendes informieren:

- Die Google Maps-Quellen müssen direkt auf den generierten Inhalt folgen, den sie unterstützen. Dieser generierte Inhalt wird auch als fundiertes Google Maps-Ergebnis bezeichnet.
- Die Google Maps-Quellen müssen innerhalb einer Nutzerinteraktion sichtbar sein.

### Google Maps-Quellen mit Google Maps-Links anzeigen

Für jede Quelle in `groundingChunks` und in `grounding_chunks.maps.placeAnswerSources.reviewSnippets` muss eine Linkvorschau gemäß den folgenden Anforderungen generiert werden:

- Weisen Sie jede Quelle Google Maps gemäß den Richtlinien für die Quellenangabe als Text
  [zu](#maps-attribution-guidelines).
- Zeigen Sie den in der Antwort angegebenen Quelltitel an.
- Verlinken Sie die Quelle mit der `uri` oder `googleMapsUri` aus der Antwort.

Diese Bilder zeigen die Mindestanforderungen für die Anzeige der Quellen und Google Maps-Links.

![Prompt mit Antwort, in der Quellen angegeben sind](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=de)

Sie können die Ansicht der Quellen minimieren.

![Prompt mit zusammengefasster Antwort und Quellen](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=de)

Optional: Erweitern Sie die Linkvorschau mit zusätzlichen Inhalten, z. B.:

- Vor der Quellenangabe als Text wird ein [Google Maps-Favicon](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=de)
  eingefügt.
- Ein Foto aus der Quell-URL (`og:image`).

Weitere Informationen zu einigen unserer Google Maps-Datenanbieter und ihren
Lizenzbedingungen finden Sie in den [rechtlichen Hinweisen zu Google Maps und Google Earth](https://www.google.com/help/legalnotices_maps/?hl=de).

### Richtlinien für die Quellenangabe als Text für Google Maps

Wenn Sie Quellen in Text Google Maps zuweisen, beachten Sie diese Richtlinien:

- Ändern Sie den Text „Google Maps“ in keiner Weise:
  - Ändern Sie die Groß- und Kleinschreibung von „Google Maps“ nicht.
  - Fügen Sie keinen Zeilenumbruch in „Google Maps“ ein.
  - Lokalisieren Sie „Google Maps“ nicht in eine andere Sprache.
  - Verhindern Sie, dass Browser Google Maps übersetzen, indem Sie das HTML-Attribut „translate="no"“ verwenden.
- Formatieren Sie den Text „Google Maps“ wie in der folgenden Tabelle beschrieben:

| Attribut | Stil |
| --- | --- |
| `Font family` | Roboto. Das Laden der Schriftart ist optional. |
| `Fallback font family` | Eine beliebige serifenlose Schriftart, die bereits in Ihrem Produkt verwendet wird, oder „Sans-Serif“, um die Standardsystemschriftart aufzurufen |
| `Font style` | Normal |
| `Font weight` | 400 |
| `Font color` | Weiß, Schwarz (#1F1F1F) oder Grau (#5E5E5E). Achten Sie auf einen barrierefreien Kontrast von 4,5:1 zum Hintergrund. |
| `Font size` | - Mindestschriftgröße: 12 sp - Maximale Schriftgröße: 16 sp - Weitere Informationen zu „sp“ finden Sie unter Schriftgrößeneinheiten auf der [Material Design-Website](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Normal |

#### Beispiel-CSS

Mit dem folgenden CSS wird „Google Maps“ mit dem entsprechenden typografischen Stil und der entsprechenden Farbe auf einem weißen oder hellen Hintergrund gerendert.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### Orts-ID und Rezensions-ID

Die Google Maps-Daten enthalten die Orts-ID und die Rezensions-ID. Sie können die folgenden Antwortdaten im Cache speichern, speichern und exportieren:

- `placeId`
- `reviewId`

Die Einschränkungen für das Caching in den Nutzungsbedingungen für die Fundierung mit Google Maps gelten nicht.

### Unzulässige Aktivitäten und Gebiete

Für die Fundierung mit Google Maps gelten zusätzliche Einschränkungen für bestimmte Inhalte und Aktivitäten, um eine sichere und zuverlässige Plattform zu gewährleisten. Zusätzlich zu den Nutzungs
beschränkungen in den [Nutzungsbedingungen](https://ai.google.dev/gemini-api/terms?hl=de#grounding-with-google-maps) gilt Folgendes:

- Sie verwenden die Fundierung mit Google Maps nicht für hochriskante Aktivitäten, einschließlich Notfalleinsätze.
- Sie vertreiben oder bewerben Ihre Anwendung, die die Fundierung mit Google Maps bietet, nicht in einem verbotenen Gebiet. Weitere Informationen finden Sie unter
  [Verbotene Gebiete der Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=de).
  Die Liste der verbotenen Gebiete wird gelegentlich aktualisiert.

## Best Practices

- **Nutzerstandort angeben**:Um die relevantesten und personalisierten Antworten zu erhalten, geben Sie in Ihrer `googleMapsGrounding`-Konfiguration immer den `user_location` (Breiten- und Längengrad) an, wenn der Standort des Nutzers bekannt ist.
- **Endnutzer informieren**:Informieren Sie Ihre Endnutzer deutlich darüber, dass Google Maps-Daten verwendet werden, um ihre Anfragen zu beantworten, insbesondere wenn das Tool aktiviert ist.
- **Latenz überwachen**:Bei konversationellen Anwendungen muss die P95-Latenz für fundierte Antworten innerhalb akzeptabler Grenzwerte bleiben, um eine reibungslose Nutzererfahrung zu gewährleisten.
- **Deaktivieren, wenn nicht erforderlich**:Die Fundierung mit Google Maps ist standardmäßig deaktiviert. Aktivieren Sie sie nur (`"tools": [{"googleMaps": {}}]`), wenn eine Anfrage einen
  klaren geografischen Kontext hat, um Leistung und Kosten zu optimieren.

## Beschränkungen

- **Geografischer Umfang**:Die Fundierung mit Google Maps ist weltweit verfügbar.
- **Modellunterstützung:** Weitere Informationen finden Sie im Abschnitt [Unterstützte Modelle](#supported-models).
- **Multimodale Eingaben/Ausgaben**:Die Fundierung mit Google Maps unterstützt derzeit keine multimodalen Eingaben oder Ausgaben über Text hinaus.
- **Standardstatus**:Das Tool „Fundierung mit Google Maps“ ist standardmäßig deaktiviert.
  Sie müssen es in Ihren API-Anfragen explizit aktivieren.

## Preise und Ratenlimits

Die Preise für die Fundierung mit Google Maps basieren auf Anfragen. Der aktuelle Preis beträgt **25 $ pro 1.000 fundierte Prompts**. Im kostenlosen Kontingent sind außerdem bis zu 500 Anfragen pro Tag verfügbar. Eine Anfrage wird nur auf das Kontingent angerechnet, wenn ein Prompt mindestens ein fundiertes Google Maps-Ergebnis zurückgibt (d.h. Ergebnisse, die mindestens eine Google Maps-Quelle enthalten). Wenn mehrere Anfragen aus einer einzelnen Anfrage an Google Maps gesendet werden, zählt dies als eine Anfrage für das Ratenlimit.

Ausführliche Preisinformationen finden Sie auf der Seite [Gemini API-Preise](https://ai.google.dev/gemini-api/docs/pricing?hl=de).

## Unterstützte Modelle

Die folgenden Modelle unterstützen die Fundierung mit Google Maps:

| Modell | Fundierung mit Google Maps |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=de) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=de) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=de) | ✔️ |
| [Gemini 3.1 Pro (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=de) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=de) | ✔️ |
| [Gemini 3 Flash (Vorabversion)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=de) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=de) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=de) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=de) | ✔️ |

## Unterstützte Toolkombinationen

Gemini 3-Modelle unterstützen die Kombination von integrierten Tools (z. B. Fundierung mit Google Maps) mit benutzerdefinierten Tools (Funktionsaufruf). Weitere Informationen finden Sie auf der
[Seite Toolkombinationen](https://ai.google.dev/gemini-api/docs/tool-combination?hl=de).

## Nächste Schritte

- Probieren Sie die [Fundierung mit der Google Suche in der Gemini API
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=de) aus.
- Weitere Informationen zu anderen [verfügbaren Tools](https://ai.google.dev/gemini-api/docs/tools?hl=de).
- Weitere Informationen zu Best Practices für die verantwortungsbewusste Anwendung von KI und den Sicherheitsfiltern der Gemini API finden Sie unter [Sicherheitseinstellungen](https://ai.google.dev/gemini-api/docs/safety-settings?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
