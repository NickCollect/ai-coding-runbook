---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=es-419
fetched_at: 2026-05-05T20:10:01.094675+00:00
title: "Bibliotecas de la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Bibliotecas de la API de Gemini

Cuando crees con la API de Gemini, te recomendamos que uses el **SDK de IA generativa de Google**.
Estas son las bibliotecas oficiales listas para producción que desarrollamos y mantenemos para los lenguajes más populares. Están en [disponibilidad general](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419#new-libraries) y se usan en toda nuestra documentación y ejemplos oficiales.

Si no tienes experiencia con la API de Gemini, sigue nuestra [guía de inicio rápido](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419) para comenzar.

## Compatibilidad con idiomas e instalación

El SDK de IA generativa de Google está disponible para los lenguajes Python, JavaScript/TypeScript, Go y Java. Puedes instalar la biblioteca de cada lenguaje con administradores de paquetes o visitar sus repositorios de GitHub para obtener más información:

### Python

- Biblioteca: [`google-genai`](https://pypi.org/project/google-genai)
- Repositorio de GitHub: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Instalación: `pip install google-genai`

### JavaScript

- Biblioteca: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- Repositorio de GitHub: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Instalación: `npm install @google/genai`

### Go

- Biblioteca: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- Repositorio de GitHub: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Instalación: `go get google.golang.org/genai`

### Java

- Biblioteca: `google-genai`
- Repositorio de GitHub: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Instalación: Si usas Maven, agrega lo siguiente a tus dependencias:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Biblioteca: `Google.GenAI`
- Repositorio de GitHub: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Instalación: `dotnet add package Google.GenAI`

## Disponibilidad general

A partir de mayo de 2025, el SDK de IA generativa de Google alcanzó la disponibilidad general (GA) en todas las plataformas compatibles y son las bibliotecas recomendadas para acceder a la API de Gemini.
Son estables, tienen compatibilidad total para su uso en producción y se mantienen de forma activa.
Proporcionan acceso a las funciones más recientes y ofrecen el mejor rendimiento cuando se trabaja con Gemini.

Si usas una de nuestras bibliotecas heredadas, te recomendamos que migres para que puedas acceder a las funciones más recientes y obtener el mejor rendimiento cuando trabajes con Gemini. Consulta la sección sobre [bibliotecas heredadas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419#previous-sdks) para obtener más información.

## Bibliotecas heredadas y migración

Si usas una de nuestras bibliotecas heredadas, te recomendamos que [migres a las nuevas bibliotecas](https://ai.google.dev/gemini-api/docs/migrate?hl=es-419).

Las bibliotecas heredadas no brindan acceso a funciones recientes (como la [API de Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419) y [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419)) y están obsoletas desde el 30 de noviembre de 2025.

El estado de compatibilidad de cada biblioteca heredada varía, como se detalla en la siguiente tabla:

| Idioma | Biblioteca heredada | Estado de compatibilidad | Biblioteca recomendada |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Sin mantenimiento activo | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Sin mantenimiento activo | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Sin mantenimiento activo | `google.golang.org/genai` |
| **Dart y Flutter** | `google_generative_ai` | Sin mantenimiento activo | Usa [Genkit Dart](https://genkit.dev/docs/dart/get-started/) o [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | Sin mantenimiento activo | Usa [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=es-419) |
| **Android** | `generative-ai-android` | Sin mantenimiento activo | Usa [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=es-419) |

**Nota para desarrolladores de Java:** No había un SDK de Java heredado proporcionado por Google para la API de Gemini, por lo que no se requiere ninguna migración desde una biblioteca anterior de Google. Puedes comenzar directamente con la nueva biblioteca en la sección [Compatibilidad con idiomas y la instalación](#install).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
