---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=es-419
fetched_at: 2026-07-27T04:46:52.210879+00:00
title: "Bibliotecas de la API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Bibliotecas de la API de Gemini

Cuando compiles con la API de Gemini, te recomendamos que uses el **SDK de IA generativa de Google**.
Estas son las bibliotecas oficiales listas para producción que desarrollamos y mantenemos para los lenguajes más populares. [Están disponibles para el público general y se usan en toda nuestra documentación y ejemplos oficiales.](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419#new-libraries)

Si no conoces la API de Gemini, sigue nuestra [guía de introducción](https://ai.google.dev/gemini-api/docs/get-started?hl=es-419) para comenzar.

## Compatibilidad con lenguajes e instalación

El SDK de IA generativa de Google está disponible para los lenguajes Python, JavaScript/TypeScript, Go y Java. Puedes instalar la biblioteca de cada lenguaje con los administradores de paquetes o visitar sus repositorios de GitHub para obtener más información:

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
Son estables, totalmente compatibles para el uso en producción y se mantienen de forma activa.
Proporcionan acceso a las funciones más recientes y ofrecen el mejor rendimiento cuando se trabaja con Gemini.

Si usas una de nuestras bibliotecas heredadas, te recomendamos que migres para que puedas acceder a las funciones más recientes y obtener el mejor rendimiento cuando trabajes con Gemini. Consulta la sección de [bibliotecas heredadas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419#previous-sdks) para obtener más información.

## Bibliotecas heredadas y migración

Si usas una de nuestras bibliotecas heredadas, te recomendamos que
[migres a las bibliotecas nuevas](https://ai.google.dev/gemini-api/docs/migrate?hl=es-419).

Las bibliotecas heredadas no proporcionan acceso a funciones recientes (como
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=es-419) y [Veo](https://ai.google.dev/gemini-api/docs/video?hl=es-419)) y dejaron de estar disponibles el 30 de noviembre de 2025.

El estado de compatibilidad de cada biblioteca heredada varía, como se detalla en la siguiente tabla:

| Idioma | Biblioteca heredada | Estado de compatibilidad | Biblioteca recomendada |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | No se mantiene de forma activa | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | No se mantiene de forma activa | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | No se mantiene de forma activa | `google.golang.org/genai` |
| **Dart y Flutter** | `google_generative_ai` | No se mantiene de forma activa | Usa [Genkit Dart](https://genkit.dev/docs/dart/get-started/) o [Firebase AI Logic](https://pub.dev/packages/firebase_ai) |
| **Swift** | `generative-ai-swift` | No se mantiene de forma activa | Usa [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=es-419) |
| **Android** | `generative-ai-android` | No se mantiene de forma activa | Usa [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=es-419) |

**Nota para desarrolladores de Java:** No había un SDK de Java heredado proporcionado por Google para la API de Gemini, por lo que no se requiere ninguna migración desde una biblioteca anterior de Google. Puedes comenzar directamente con la biblioteca nueva en la
[sección Compatibilidad con lenguajes e instalación](#install).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-22 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-22 (UTC)"],[],[]]
