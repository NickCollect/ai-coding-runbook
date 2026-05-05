---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=es-419
fetched_at: 2026-05-05T20:42:21.410433+00:00
title: "Configura tu asistente de programaci\u00f3n con Gemini MCP y Skills \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Configura tu asistente de programación con Gemini MCP y Skills

Los asistentes de programación con IA son potentes, pero tienen limitaciones: los datos de entrenamiento se cortan en una fecha específica y faltan nuevas funciones y cambios en la API. Sin acceso a la documentación específica de Gemini, los agentes pueden sugerir patrones genéricos en lugar de enfoques optimizados.

Para mantener tu asistente de programación actualizado con la API de Gemini en constante evolución y su uso recomendado, te sugerimos que configures el **MCP de la documentación de Gemini** y que mejores tu entorno con las **habilidades de la API de Gemini**. Si bien estas herramientas se pueden usar de forma independiente, están diseñadas para funcionar en conjunto y brindar una cobertura completa.

## Conecta el MCP de Gemini Docs

Gemini aloja un servidor público del Protocolo de contexto del modelo (MCP) en `https://gemini-api-docs-mcp.dev`. Conectar tu agente de programación a este servidor garantiza que todas las consultas tengan acceso a las APIs más recientes, las actualizaciones de código y los ejemplos de configuración óptima.

Ejecuta el siguiente comando en la terminal o la raíz del proyecto de tu agente para instalar el servidor:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Este servidor agrega una función `search_documentation` que tu agente puede usar para recuperar definiciones de API y patrones de integración en tiempo real de los archivos de documentación oficiales de Gemini.

## Add API Development Skills

Las habilidades proporcionan **reglas y prácticas recomendadas integradas** (como aplicar las versiones correctas del SDK y del modelo actual) directamente en el contexto de tu asistente. La habilidad funciona en conjunto con el servicio de MCP de la documentación de Gemini: Si tienes ambos instalados, la habilidad usa el servicio de MCP para la documentación, pero incluso sin el MCP instalado, recuperará `llms.txt` de `ai.google.dev` como alternativa.

Para instalar estas habilidades, puedes usar una de las siguientes herramientas compatibles. A continuación, se proporcionan las instrucciones de instalación para ambos módulos de habilidad:

- **[skills.sh](https://skills.sh)**: Se recomienda. Es el estándar abierto para los comportamientos portátiles de los agentes.
- **[Context7](https://context7.com)**: Se admite para los usuarios que ya utilizan el ecosistema de Context7.

### gemini-api-dev

Es la habilidad fundamental para el desarrollo de Gemini de uso general. Esta habilidad proporciona documentación y prácticas recomendadas para lo siguiente:

- Enrutamiento de instrucciones a los modelos actuales (p.ej., Gemini 3.1 Pro/Flash) y evitación de modelos obsoletos
- Instrucciones multimodales, llamadas a funciones, resultados estructurados y patrones de integración comunes

#### Instala con skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Instalación con Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Habilidad para compilar aplicaciones de IA conversacional en tiempo real con la API de Gemini Live. Esta habilidad proporciona documentación y prácticas recomendadas para lo siguiente:

- Conexiones WebSocket para la transmisión de baja latencia
- Transmisión de audio, video y texto
- Detección de actividad de voz y compatibilidad con la interrupción

#### Instala con skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Instalación con Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Habilidad para compilar apps con la [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419). La API de Interactions es una interfaz unificada para interactuar con modelos y agentes de Gemini, diseñada para aplicaciones basadas en agentes. En este curso, se abordan los siguientes temas:

- Generación de texto, chat de varios turnos y transmisión
- Llamadas a funciones, resultados estructurados y generación de imágenes
- Ejecución en segundo plano y agentes de Deep Research
- Administración del estado de la conversación del servidor
- Patrones de SDK de Python y TypeScript

#### Instala con skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Instalación con Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Verifica la instalación

Después de la instalación, confirma que tu asistente de programación pueda conectarse al servidor de MCP de la documentación de Gemini y usar las habilidades instaladas.

### 1. Verifica el comportamiento del agente

La forma más confiable de verificarlo es hacerle a tu agente una pregunta técnica sobre la API de Gemini.

**Instrucción:** "¿Cómo uso el almacenamiento de contexto en caché con la API de Gemini?"

Una configuración exitosa tendrá las siguientes características:

- **Proporciona código preciso**: Haz referencia a métodos específicos de Gemini, como `cacheContent` o `cachedContents.create`, desde los extremos más recientes.
- **Usa la herramienta de MCP**: Demuestra que está conectada al **servidor de MCP de Gemini Docs** o que utiliza la herramienta de `search_documentation` para recuperar datos.
- **Invocar habilidades cargadas**: Mostrar un indicador de que se está "Usando la habilidad: gemini-api-dev" (si se depende de un wrapper secundario).

### 2. Verifica las manifestaciones y las herramientas

Si el agente da una respuesta general o genérica, usa los comandos específicos de Discovery o Status para tu entorno y verifica que el MCP o la habilidad de Docs se hayan cargado en la memoria.

| Entorno | Verificación del MCP | Verificación de habilidades |
| --- | --- | --- |
| **Claude Code** | Escribe `/mcp` en la terminal para ver los servidores activos y las herramientas de `search_documentation`. | Escribe `/skills` en la terminal para enumerar todos los manifiestos activos. |
| **Cursor** | Navega a **Configuración > Funciones > MCP**. Asegúrate de que el servidor esté “Conectado”. | Abre **Configuración > Reglas**. Verifica que la habilidad aparezca en "El agente decide". |
| **Antigravity** | Consulta el estado del MCP en la barra lateral **Personalizaciones > Conexiones**. | Escribe `/skills list` o consulta la barra lateral **Personalizaciones > Reglas**. |
| **CLI de Gemini** | Ejecuta `gemini mcp list` o usa `/mcp list`. | Ejecuta `gemini skills list` o usa el comando de barra `/skills` durante la sesión. |
| **Copilot** | Escribe `@gemini /mcp` para enumerar los conectores de datos activos. | Escribe `@gemini /skills` (o `/skills`) para ver las extensiones activas. |

## Solución de problemas

Si tu agente solo proporciona información general o no reconoce los métodos específicos de Gemini, verifica lo siguiente:

### El agente no descubrió la skill

La mayoría de los agentes indexan las habilidades solo al inicio.

**Solución:** Reinicia por completo tu IDE (Cursor/VS Code) o sal de tu agente basado en terminal (Claude Code) y vuelve a abrirlo.

### Conflictos globales y locales

Si realizaste la instalación con la marca `--global`, es posible que tu agente la ignore y prefiera las reglas específicas del proyecto.

**Solución:** Intenta instalar la habilidad directamente en la raíz de tu proyecto sin la marca global:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Recursos

- [Habilidades de la API de Gemini en GitHub](https://github.com/google-gemini/gemini-skills)
- [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions?hl=es-419)
- [Guía de inicio rápido](https://ai.google.dev/gemini-api/docs/quickstart?hl=es-419)
- [Bibliotecas](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
