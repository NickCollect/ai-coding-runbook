---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419
fetched_at: 2026-06-01T06:09:33.287199+00:00
title: "Crea apps para Android en Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Crea apps para Android en Google AI Studio

Google AI Studio te permite crear apps nativas para Android a partir de una instrucción en lenguaje natural. Describe la app que quieres y el [agente Antigravity](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419#antigravity-agent) generará un proyecto completo en Kotlin y [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=es-419). Desde tu navegador, puedes obtener una vista previa de tu app en un emulador de Android basado en el navegador, instalarla en un dispositivo físico y publicarla para realizar pruebas.

## Comenzar

Para comenzar a compilar una app para Android, haz lo siguiente:

1. Ve al [modo de compilación](https://aistudio.google.com/apps?hl=es-419) en Google AI Studio con el panel de navegación de la izquierda.
2. Selecciona **Android** en el selector de plataformas.
3. Ingresa una instrucción que describa la app que quieres crear (por ejemplo, *"Crea una tabla de seguimiento de tareas diarias con almacenamiento local"* o *"Crea una calculadora simple"*).
4. El agente genera el proyecto y lo inicia en el emulador de Android basado en el navegador.

Luego, puedes iterar en tu app con el panel de chat, al igual que en la experiencia web. El agente administra todos los archivos de tu proyecto de Android y propaga los cambios en toda la base de código.

## Emulador de Android basado en el navegador

El emulador de Android se ejecuta por completo en la nube y se transmite a tu navegador.
No es necesario que instales el SDK de Android, Android Studio ni un emulador local.

El emulador proporciona lo siguiente:

- **Simulación de dispositivos similar a Pixel**: Presiona, desplázate e interactúa con tu app como lo harías en un dispositivo real.
- **Compatibilidad con la rotación**: Cambia entre la orientación vertical y horizontal.
- **Vista previa en vivo**: Cuando el agente realiza cambios en el código, la app se vuelve a compilar y el emulador se actualiza automáticamente.

### Limitaciones del emulador

El emulador basado en el navegador no admite todas las funciones de hardware. Los siguientes elementos no están disponibles en el emulador:

- Captura de fotos y cámaras
- NFC y Bluetooth
- GPS (se simula la ubicación)
- Servicios de Google Play (Acceso con Google, Maps y otras funciones de los Servicios de Play que funcionan en un dispositivo real, pero no en el emulador)

## Instala en un dispositivo con ADB

Puedes instalar el APK compilado directamente en un dispositivo Android físico conectado a tu computadora a través de USB. Esto usa [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=es-419) para comunicarse con tu dispositivo a través del navegador. No se requiere instalación local de ADB.

### Requisitos previos

- Un navegador Chrome o Edge que admita WebUSB
- Un dispositivo Android con las [Opciones para desarrolladores y la depuración por USB](https://developer.android.com/studio/debug/dev-options?hl=es-419) habilitadas
- Un cable USB que conecte tu dispositivo a la computadora

### Instala la app en tu dispositivo

1. Haz clic en **Install on Device** en el panel de vista previa.
2. Selecciona tu dispositivo Android en el selector de dispositivos USB del navegador.
3. El APK se transfiere y se instala en tu dispositivo.
4. La app se iniciará automáticamente.

## Publica en Play Store

Puedes publicar tu app para Android en el segmento de pruebas internas de [Google Play Console](https://play.google.com/console?hl=es-419), que te permite distribuir la app a un máximo de 100 verificadores.

### Requisitos previos

- Una [cuenta de desarrollador de Google Play](https://play.google.com/console/signup?hl=es-419) (se requiere una tarifa de registro única de USD 25)
- Un perfil de desarrollador completo en Play Console

### Cómo publicar tu app

1. Abre **Settings > Publish** en Google AI Studio.
2. Haz clic en **Publicar en Play Store**.
3. Autentícate con tu cuenta de desarrollador de Google Play.
4. AI Studio firma el APK, crea la ficha de Play Store (o sube una versión nueva) y publica en el segmento de pruebas internas.
5. Recibirás un vínculo para compartir con los verificadores.

AI Studio administra la firma de APK automáticamente con un almacén de claves administrado. Puedes personalizar la ficha de Play Store (ícono, capturas de pantalla, descripción) más adelante en Play Console.

## Qué se genera

Cuando compilas una app para Android, el agente genera un proyecto estándar basado en Gradle con la siguiente estructura:

- **Configuración de compilación**: Archivos `build.gradle.kts` (a nivel del proyecto y de la app) con el DSL de Kotlin
- **Capa de la IU**: Componentes de [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=es-419) con temas de [Material 3](https://m3.material.io/)
- **Arquitectura**: Arquitectura de actividad única con ViewModels y clases de datos.
- **Recursos**: `AndroidManifest.xml`, elementos de diseño, cadenas y otros recursos de Android

El agente administra automáticamente las dependencias de Gradle y agrega paquetes de los repositorios de Maven y Google según sea necesario.

Puedes ver y editar el código generado en la pestaña **Código** del panel de vista previa. Para continuar el desarrollo en Android Studio, descarga el proyecto como un **archivo ZIP**.

## Limitaciones

La compilación de apps para Android en AI Studio tiene las siguientes limitaciones:

### Limitaciones de la plataforma

- **Solo del cliente**: Las apps para Android no incluyen un componente del servidor.
  No están disponibles las funciones que requieren un tiempo de ejecución del servidor (administración de secretos, multijugador, Firebase, APIs de Google Workspace).
- **Arquitectura de actividad única**: Solo se admiten proyectos de actividad única y módulo único.
- **Solo Jetpack Compose**: Las apps usan Kotlin y Jetpack Compose. No se admiten diseños de Java ni XML.
- **No hay NDK ni código nativo**: No se admite código C ni C++.
- **Sin Wear OS ni Android TV**: Solo se admiten los factores de forma de teléfonos y tablets.

### Exporta limitaciones

- **Solo descarga en ZIP**: Puedes descargar el proyecto como un archivo ZIP. La exportación a GitHub aún no está disponible para proyectos de Android.

## ¿Qué sigue?

- [Crea apps en Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419)
- [Cómo desarrollar apps de pila completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419) (web)
- Consulta ejemplos en la [Galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-05-19 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-05-19 (UTC)"],[],[]]
