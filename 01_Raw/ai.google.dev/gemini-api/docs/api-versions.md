---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=es-419
fetched_at: 2026-07-06T05:10:31.026505+00:00
title: "Explicaci\u00f3n de las versiones de la API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Referencia de la API](https://ai.google.dev/api?hl=es-419)

Enviar comentarios

# Explicación de las versiones de la API

En este documento, se proporciona una descripción general de alto nivel de las diferencias entre las versiones `v1` y `v1beta` de la API de Gemini.

- **v1**: Es la versión estable de la API. Las funciones de la versión estable son totalmente compatibles durante el ciclo de vida de la versión principal. Si hay cambios que interrumpen la compatibilidad, se creará la próxima versión principal de la API y la versión existente se marcará como obsoleta después de un período razonable.
  Se pueden introducir cambios no rotundos en la API sin cambiar la versión principal. A partir de junio de 2026, la **API de Interactions** estará disponible de forma general y se admitirá en `v1`.
- **v1beta**: Esta versión incluye funciones y capacidades iniciales que se encuentran en desarrollo activo. Si bien las funciones en `v1beta` pueden estar sujetas a cambios a medida que las perfeccionamos en función de los comentarios, te permite probar nuevas capacidades antes de que se promuevan a estables.

| Función | v1 | v1beta |
| --- | --- | --- |
| API de Interactions |  |  |
| Genera contenido: entrada de solo texto |  |  |
| Generar contenido: entrada de texto e imagen |  |  |
| Generar contenido: salida de texto |  |  |
| Generar contenido: conversaciones de varios turnos (chat) |  |  |
| Genera contenido: Llamadas a funciones |  |  |
| Generar contenido: transmisión |  |  |
| Incorpora contenido: entrada de solo texto |  |  |
| Generar respuesta |  |  |
| Recuperador semántico |  |  |

- : Compatible
- : Nunca será compatible

## Cómo configurar la versión de la API en un SDK

Los SDK de la API de Gemini usan `v1beta` de forma predeterminada, pero puedes especificar versiones de forma explícita configurando la versión de la API como se muestra en la siguiente muestra de código:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Explain how AI works",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works"
  }'
```

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-22 (UTC)"],[],[]]
