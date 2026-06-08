---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419
fetched_at: 2026-06-08T05:38:15.688436+00:00
title: "Implementaci\u00f3n desde Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Implementación desde Google AI Studio

Google AI Studio te permite implementar tus aplicaciones de full stack directamente desde el modo de compilación. Esto proporciona una ruta rápida desde el prototipo hasta un entorno de producción administrado y escalable.

## Opciones de implementación

Para implementar tu aplicación desde el modo de compilación de AI Studio, los requisitos dependen del nivel que uses:

- [**Nivel inicial de Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=es-419):
  Te permite publicar hasta 2 aplicaciones de full stack sin configurar un
  proyecto de Google Cloud ni una cuenta de facturación.
- **Implementación estándar**: Requiere un proyecto de Google Cloud vinculado a tu
  cuenta de AI Studio y la facturación habilitada en ese proyecto.

## Acerca del nivel inicial

El nivel inicial de Google Cloud proporciona una ruta optimizada para implementar aplicaciones en Google Cloud directamente desde Google AI Studio sin configurar un entorno completo de Google Cloud ni una cuenta de facturación.

Cada implementación de Google AI Studio crea un servicio correspondiente en Cloud Run. Para los servicios implementados en Google AI Studio con el nivel inicial, se aplican las siguientes limitaciones:

- Puedes implementar hasta dos servicios.
- Tus servicios se implementan en una
  [sola región de Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=es-419).

## Pasos de implementación del nivel inicial

Después de diseñar tu app en el modo de compilación, impleméntala con el nivel inicial:

1. Haz clic en el botón **Publicar** en la esquina superior derecha.
2. Haz clic en **Comenzar**.
3. Haz clic en **Publicar app**.

Una vez que se complete la implementación, AI Studio proporcionará una URL de Cloud Run en la que podrás acceder a tu aplicación en vivo.

## Implementación estándar

A medida que evolucionan tus aplicaciones, es posible que necesites capacidades más allá del nivel inicial, como cuotas más altas o mayores recursos de procesamiento, o bien otros productos de Google Cloud que no estén disponibles en el nivel inicial. Para desbloquear estas capacidades, puedes convertir tu proyecto de nivel inicial completamente administrado en un proyecto estándar de Google Cloud.

Esto garantiza que puedas escalar sin problemas sin perder tu progreso. Sigue los pasos para
[crear una cuenta de Facturación de Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=es-419#create-new-billing-account),
aceptar formalmente las Condiciones del Servicio estándar de Google Cloud y
[actualizar a un proyecto estándar de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=es-419#upgradee).
Para obtener más información, consulta
[Configuración de cuentas pagas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=es-419#paid-setup).

Para obtener más información sobre los niveles de facturación, consulta [Facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419).

## Borra tu aplicación

Si ya no necesitas tu app, puedes borrarla en Google AI Studio siguiendo estas instrucciones:

1. En Google AI Studio, ve a la página
   [Apps](https://aistudio.google.com/app/apps?hl=es-419).
2. En el menú de la izquierda, selecciona **Apps**.
3. Mantén el puntero sobre la app que deseas borrar.
4. Haz clic en el ícono de la papelera en el lado derecho de la fila para borrar la app.

## ¿Qué sigue?

- Obtén más información sobre el
  [nivel inicial de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=es-419).
- Lee sobre [la facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419) en la API de Gemini.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-16 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-16 (UTC)"],[],[]]
