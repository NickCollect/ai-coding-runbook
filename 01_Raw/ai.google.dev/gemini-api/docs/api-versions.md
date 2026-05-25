---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=es-419
fetched_at: 2026-05-25T05:22:36.597528+00:00
title: "Explicaci\u00f3n de las versiones de la API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Referencia de la API](https://ai.google.dev/api?hl=es-419)

Enviar comentarios

# Explicación de las versiones de la API

En este documento, se proporciona una descripción general de alto nivel sobre las diferencias entre las versiones `v1`
y `v1beta` de la API de Gemini.

- **v1**: Versión estable de la API. Las funciones de la versión estable son totalmente compatibles durante el ciclo de vida de la versión principal. Si hay algún cambio rotundo, se creará la próxima versión principal de la API y la versión existente dejará de estar disponible después de un período razonable.
  Se pueden introducir cambios no rotundos en la API sin cambiar la versión principal.
- **v1beta**: Esta versión incluye funciones tempranas que pueden estar en desarrollo y están sujetas a cambios rotundos. Tampoco se garantiza que las funciones de la versión Beta pasen a la versión estable. **Si necesitas estabilidad en tu entorno de producción y no puedes arriesgarte a cambios rotundos, no debes usar esta versión en producción.**

| Función | v1 | v1beta |
| --- | --- | --- |
| Generar contenido: Entrada de solo texto |  |  |
| Generar contenido: Entrada de texto e imagen |  |  |
| Generar contenido: Salida de texto |  |  |
| Generar contenido: Conversaciones de varios turnos (chat) |  |  |
| Generar contenido: Llamadas a funciones |  |  |
| Generar contenido: Transmisión |  |  |
| Incorporar contenido: Entrada de solo texto |  |  |
| Generar respuesta |  |  |
| Recuperador semántico |  |  |
| API de interacciones |  |  |

- - Compatible
- - Nunca será compatible

## Configura la versión de la API en un SDK

Los SDK de la API de Gemini usan `v1beta` de forma predeterminada, pero puedes especificar versiones de forma explícita configurando la versión de la API como se muestra en la siguiente muestra de código:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
