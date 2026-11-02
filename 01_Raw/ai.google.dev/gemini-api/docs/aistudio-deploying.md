---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419
fetched_at: 2026-11-02T07:15:07.236508+00:00
title: "Implementaci\u00f3n desde Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Implementación desde Google AI Studio

Google AI Studio te permite implementar tus aplicaciones de pila completa directamente desde el modo de compilación. Esto proporciona una ruta rápida desde el prototipo hasta un entorno de producción administrado y escalable.

## Opciones de implementación

Para implementar tu aplicación desde el modo de compilación de AI Studio, los requisitos dependen del nivel que uses:

- [**Nivel básico de Google Cloud**](https://docs.cloud.google.com/docs/starter-tier?hl=es-419):
  Permite que las cuentas aptas publiquen hasta 2 aplicaciones de pila completa sin configurar un proyecto de Google Cloud ni una cuenta de facturación.
- **Implementación estándar**: Requiere un proyecto de Google Cloud vinculado a tu cuenta de AI Studio y la facturación habilitada en ese proyecto.

## Acerca del nivel Starter

El nivel Inicial de Google Cloud proporciona una ruta optimizada para que las cuentas aptas implementen aplicaciones en Google Cloud directamente desde Google AI Studio. No es necesario que configures un entorno de Google Cloud completo ni una cuenta de facturación.

Cada implementación de Google AI Studio crea un servicio correspondiente en Cloud Run. Para los servicios implementados en Google AI Studio con el nivel Básico, se aplican las siguientes limitaciones:

- Puedes implementar hasta dos servicios.
- Tus servicios se implementan en una [sola región de Cloud Run](https://docs.cloud.google.com/run/docs/locations?hl=es-419).

### Elegibilidad para el nivel Starter

No todas las cuentas son aptas para el nivel básico de Google Cloud. Es posible que tu cuenta no sea apta si se aplica alguna de las siguientes opciones:

- Accediste con una cuenta de Google Workspace (incluidas las suscripciones pagadas o gratuitas de Google Workspace, Google Workspace for Education o Google para organizaciones sin fines de lucro).
- Tienes una cuenta de facturación de Google Cloud pagada activa o anterior.
- En este momento, no tenemos suficientes pruebas de la actividad de tu cuenta para otorgarte acceso al nivel básico.

El equipo de asistencia al cliente de Google AI Studio no puede anular la elegibilidad para el nivel inicial. Si tu cuenta no cumple con los requisitos, adjunta una cuenta de facturación y usa la [implementación estándar](#standard-deployment) para publicar apps.

## Implementa con el nivel Starter

Después de diseñar tu app en el modo de compilación, impleméntala con el nivel básico:

1. Haz clic en el botón **Publicar** en la esquina superior derecha.
2. Haz clic en **Comenzar**.
3. Haz clic en **Publicar app**.

Una vez que se complete la implementación, AI Studio proporcionará una URL de Cloud Run en la que podrás acceder a tu aplicación en vivo.

## URLs personalizadas para AI Studio

Cuando publicas una aplicación desde Google AI Studio, puedes establecer un subdominio personalizado y fácil de recordar en `ai.studio` (por ejemplo, `https://your-app-name.ai.studio`).

Google AI Studio requiere que los subdominios sean únicos a nivel global en todos los proyectos y los asigna por orden de llegada. Si otro proyecto ya usa un nombre, AI Studio te pedirá que elijas uno diferente. Si anulas la publicación o borras una aplicación, se libera su URL personalizada y otros usuarios pueden reclamarla.

### Cómo establecer una URL personalizada

Para establecer o actualizar una URL personalizada para tu aplicación, haz lo siguiente:

1. Abre tu aplicación en Google AI Studio en el modo **Compilación**.
2. Haz clic en **Publicar** en la esquina superior derecha.
3. En la configuración de la implementación, ingresa el subdominio que prefieras en el campo **URL personalizada** o acepta la URL sugerida.
4. Haz clic en **Publicar app**.

Para transferir una URL personalizada existente a otra aplicación, primero debes anular la publicación o borrar la aplicación a la que se le asignó esa URL personalizada y, luego, publicar tu nueva aplicación con el subdominio elegido.

### Cómo denunciar problemas de derechos de autor o marcas

Los subdominios personalizados deben cumplir con las [Condiciones del Servicio de Google](https://policies.google.com/terms?hl=es-419). Si observas una URL personalizada que infringe una marca comercial o usa un nombre protegido por derechos de autor sin permiso, puedes denunciarla con el [Solucionador de Problemas Legales de Google](https://support.google.com/legal/troubleshooter/1114905?hl=es-419).

## Implementación estándar

A medida que evolucionen tus aplicaciones, es posible que necesites capacidades más allá del nivel Básico, como cuotas más altas, más recursos de procesamiento o más productos de Google Cloud que no estén disponibles en el nivel Básico. Para desbloquear estas capacidades, puedes convertir tu proyecto del nivel básico completamente administrado en un proyecto estándar de Google Cloud.

Esto garantiza que puedas escalar sin problemas y sin perder tu progreso. Sigue los pasos para [crear una cuenta de Facturación de Cloud](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account?hl=es-419#create-new-billing-account), aceptar formalmente las Condiciones del Servicio estándar de Google Cloud y [actualizar a un proyecto estándar de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=es-419#upgradee).
Para obtener más información, consulta [Configuración de cuentas pagadas](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=es-419#paid-setup).

Para obtener más información sobre los niveles de facturación, consulta [Facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419).

## Borra tu solicitud

Si ya no necesitas tu app, puedes borrarla en Google AI Studio siguiendo estas instrucciones:

1. En Google AI Studio, ve a tu [página de Apps](https://aistudio.google.com/app/apps?hl=es-419).
2. En el menú de la izquierda, selecciona **Apps**.
3. Mantén el puntero sobre la app que quieres borrar.
4. Haz clic en el ícono de papelera que se encuentra en el lado derecho de la fila para borrar la app.

## ¿Qué sigue?

- Obtén más información sobre el [nivel Inicial de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=es-419).
- Obtén más información sobre la [facturación](https://ai.google.dev/gemini-api/docs/billing?hl=es-419) en la API de Gemini.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-28 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-28 (UTC)"],[],[]]
