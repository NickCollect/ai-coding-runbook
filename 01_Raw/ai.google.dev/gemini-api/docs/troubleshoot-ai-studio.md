---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=es-419
fetched_at: 2026-08-03T04:37:34.184262+00:00
title: "Solucionar problemas de Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Solucionar problemas de Google AI Studio

En esta página, se ofrecen sugerencias para solucionar problemas de Google AI Studio si tienes algún inconveniente.

## Información sobre los errores 403 Access Restricted

Si ves un error 403 Access Restricted, significa que estás usando Google AI Studio de una
manera que no cumple con las [Condiciones del Servicio](https://ai.google.dev/terms?hl=es-419). Una razón común es
que no te encuentras en una [región admitida](https://ai.google.dev/available_regions?hl=es-419).

## Cómo resolver las respuestas No Content en Google AI Studio

Si el contenido está bloqueado por algún motivo, aparecerá un mensaje de warning **No Content** en
Google AI Studio. Para ver más detalles,
mantén el puntero sobre **No Content** y haz clic
warning **Safety**.

Si la respuesta se bloqueó debido a la [configuración de seguridad](https://ai.google.dev/docs/safety_setting?hl=es-419) y
consideraste los [riesgos de seguridad](https://ai.google.dev/docs/safety_guidance?hl=es-419) para tu caso de uso, puedes
modificar la
[configuración de seguridad](https://ai.google.dev/docs/safety_setting?hl=es-419#safety_settings_in_makersuite)
para influir en la respuesta que se muestra.

Si la respuesta se bloqueó, pero no debido a la configuración de seguridad, es posible que la consulta o la
respuesta infrinjan las [Condiciones del Servicio](https://ai.google.dev/terms?hl=es-419) o no sean compatibles.

## Cómo verificar el uso y los límites de tokens

Cuando tienes un mensaje abierto, el botón **Text Preview** en la parte inferior de la pantalla muestra los tokens actuales que se usan para el contenido de tu mensaje y el recuento máximo de tokens para el modelo que se usa.

## Permisos de Cloud IAM de Google Cloud para AI Studio

Los miembros de un proyecto de Google Cloud necesitan permisos específicos de Identity and Access Management (IAM) para realizar acciones en Google AI Studio. Para obtener más información sobre estas identidades, consulta la [descripción general de las principales de IAM](https://cloud.google.com/iam/docs/principals?hl=es-419).

Los usuarios con los roles de **Editor** o **Owner** en el proyecto de Google Cloud asociado tienen permisos completos para ver los paneles y administrar las claves de API de Gemini. Los usuarios con el rol de **Viewer** pueden ver los paneles y las claves de API, pero no pueden crearlos, actualizarlos ni borrarlos.

Para obtener un control más detallado, consulta la siguiente tabla para conocer los permisos específicos que se requieren para cada función de AI Studio. Si quieres obtener instrucciones para otorgar estos permisos, consulta [Otorga, cambia y revoca el acceso a los recursos](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=es-419) en la documentación de Google Cloud.

| Función de AI Studio | Permisos de IAM obligatorios | Requisitos adicionales |
| --- | --- | --- |
| **Search project** (importar proyectos) | `resourcemanager.projects.get` |  |
| **Rename project** | `resourcemanager.projects.update` |  |
| **Display quota tier** | N/A |  |
| **Create API key** | Tener permisos de **Search project** y lo siguiente:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **List API keys** | Tener permisos de **Search project** y lo siguiente:  `apikeys.keys.list` `serviceusage.services.get` | El proyecto de Google Cloud debe tener habilitada la [API de Generative Language](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=es-419). |
| **Rename API keys** | `apikeys.keys.update` |  |
| **Delete API keys** | `apikeys.keys.delete` |  |
| **Panel Uso de** | Tener permisos de **Search project** y lo siguiente:  `monitoring.timeSeries.list` |  |
| **Panel de límites de frecuencia** | Tener permisos de **Panel Uso de** y lo siguiente:  `cloudquotas.quotas.get` |  |
| **Inversión (límite de facturación)** | `billing.resourceCosts.get` (para ver la inversión) `billing.resourcebudgets.read` (para ver el límite) `billing.resourcebudgets.write` (para establecer el límite) |  |
| **Panel de facturación** | `billing.accounts.get` |  |

### Otras verificaciones de acceso

Además de los permisos de IAM de Google Cloud, AI Studio también realiza verificaciones de seguridad y cumplimiento. Es posible que encuentres un error `PERMISSION_DENIED` o de restricción de acceso en la interfaz de AI Studio o en las respuestas de la API si no cumples con los siguientes requisitos:

- **Verificaciones de seguridad:** Tu solicitud debe pasar las verificaciones de seguridad automatizadas.
- **Condiciones del Servicio:** Debes aceptar las Condiciones del Servicio de Google y las Condiciones del Servicio Adicionales para IA Generativas.
- **Región admitida:** Debes encontrarte en una [región admitida](https://ai.google.dev/gemini-api/docs/available-regions?hl=es-419).
- **Confianza y seguridad:** El proyecto de Google Cloud no debe estar marcado por abuso.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-29 (UTC)"],[],[]]
