---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=es-419
fetched_at: 2026-10-26T05:58:33.879098+00:00
title: "Crea apps en Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Crea apps en Google AI Studio

En esta página, se describe cómo usar Google AI Studio para compilar (o "programar
por intuición") e implementar rápidamente apps que prueben las funciones más recientes de Gemini, como
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=es-419) y la [API de
Live](https://ai.google.dev/gemini-api/docs/live?hl=es-419). Google AI Studio admite la creación de **apps web**
con entornos de ejecución full stack y **apps nativas para Android** con Kotlin y Jetpack
Compose, todo a través de instrucciones en lenguaje natural.

## Comenzar

Comienza a usar el vibe coding en el [modo de compilación](https://aistudio.google.com/apps?hl=es-419) de Google AI Studio. Puedes
comenzar a compilar de las siguientes maneras:

- **Comienza con una instrucción**: En el modo de compilación, usa el cuadro de entrada para ingresar una
  descripción de lo que quieres compilar. Selecciona chips de IA para agregar funciones específicas,
  como la generación de imágenes o datos de Google Maps, a tu instrucción. Incluso puedes
  decir lo que quieres con el botón de voz a texto.
- **Botón "Voy a tener suerte"**: Si necesitas una chispa creativa, usa el botón "Voy a tener suerte" y Gemini generará una instrucción con una idea de proyecto para que comiences.
- **Remezcla un proyecto de la galería**: Abre un proyecto de la [galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419) y selecciona **Copiar app**.
- **Importa un proyecto desde GitHub**: En el modo de compilación, selecciona
  **Importar desde GitHub** en el menú **Agregar archivos** (ícono de signo más) en el cuadro de entrada de la instrucción
  para importar tu código existente.

Una vez que ejecutes la instrucción, verás que se generan el código y los archivos necesarios,
con una vista previa en vivo de tu app que aparece en el lado derecho.

## ¿Qué se crea?

Cuando ejecutas la instrucción, AI Studio crea una aplicación completa. Puedes
elegir compilar una **app web** o una **app nativa para Android** con el selector de
plataforma.

Para las **apps web** (predeterminadas), AI Studio crea un entorno de pila completa que
incluye lo siguiente:

- **Del cliente**: Un frontend web (React es el valor predeterminado).
- **Del lado del servidor**: Es un entorno de ejecución de Node.js que permite realizar llamadas a la API,
  conexiones de bases de datos y uso de paquetes de npm de forma segura.

En el caso de las **apps para Android**, AI Studio genera un proyecto de Kotlin y Jetpack Compose
que puedes obtener una vista previa en un emulador basado en el navegador, instalar en un dispositivo físico
y publicar en Play Store para realizar pruebas. [Obtén más información para compilar apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419).

Para ver el código que se genera, selecciona la pestaña **Código** en el
panel de vista previa de la derecha. El **agente de Antigravity** administra de forma inteligente
varios archivos en tu pila, lo que garantiza que los cambios se propaguen
correctamente.

### El agente de Antigravity

El **agente de Antigravity** es la principal función IA dentro de [Google Antigravity](https://antigravity.google?hl=es-419) y, ahora, los componentes principales del arnés del agente potencian la experiencia del modo de compilación en Google AI Studio. Va
más allá de la simple generación de código, ya que mantiene el contexto de todo tu proyecto,
administra varios archivos y comprende instrucciones complejas para compilar aplicaciones sólidas
y de pila completa.

Las siguientes son algunas de las funciones clave:

- **Reconocimiento del contexto**: Mantiene el contexto de las instrucciones y los estados de los archivos anteriores.
- **Administración de varios archivos**: Controla las dependencias en varios archivos.
- **Ejecución verificada**: Verifica las actualizaciones de código para reducir las alucinaciones.

## Capacidades full-stack

Google AI Studio libera el poder del ecosistema web moderno, lo que te permite
crear más que solo prototipos del lado del cliente.

- **Entorno de ejecución del servidor y npm**: Usa la amplia biblioteca de paquetes de npm. El
  agente identificará e instalará automáticamente los paquetes que necesite tu
  app (p.ej., bibliotecas específicas para la visualización de datos o clientes de API). También
  puedes solicitar paquetes específicos si lo deseas.
- **Administración de secretos**: Almacena de forma segura claves de API y secretos en el menú **Configuración**. Se puede acceder a ellas en tu código del servidor, lo que las mantiene
  a salvo de la exposición del cliente.
- **Multijugador**: Crea experiencias colaborativas en tiempo real directamente en
  AI Studio. El entorno de ejecución del servidor administra el estado y las conexiones
  necesarias para que los usuarios interactúen entre sí.
- **Firebase Firestore y Authentication**: Aprovisiona y configura Firebase de forma automática, incluida la base de datos de Firestore (almacenamiento de datos persistente) y Firebase Authentication (flujos de acceso, específicamente "Acceder con Google"). El agente controla todo el proceso de configuración y hasta escribe el
  código en tu app para estos servicios.
- **Integraciones de Google Workspace**: Conecta tu app a las APIs de Google Workspace, como Gmail, Hojas de cálculo, Documentos, Drive, Calendario y muchas más. AI Studio controla
  toda la configuración de OAuth automáticamente.

[Más información para desarrollar apps de pila completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419)

### Apps para Android

También puedes compilar apps para Android nativas con Kotlin y Jetpack Compose.
Obtén una vista previa de tu app en un Android Emulator basado en el navegador, instálala en un dispositivo físico con adb en el navegador y publícala en Play Store para realizar pruebas internas.

AI Studio también se integra en
[Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=es-419)
para que las apps para Android aprovisionen automáticamente **Firebase AI Logic** y la **Verificación de aplicaciones de Firebase** (para realizar llamadas seguras a la API de Gemini del cliente sin exponer claves de API sin procesar), así como **Cloud Firestore** y **Firebase Authentication**.

[Más información para compilar apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419)

## Continúa con la compilación

Una vez que Google AI Studio genere el código inicial para tu aplicación, podrás
seguir perfeccionándolo:

### Compila en Google AI Studio

- **Itera con Gemini**: Usa el panel de chat en el **modo de compilación** para pedirle a Gemini
  que realice modificaciones, agregue funciones nuevas o cambie el diseño.
- **Edita el código directamente**: Abre la **pestaña Código** en el panel de vista previa para realizar ediciones en vivo.

### Desarrollar externamente

Para flujos de trabajo más avanzados, puedes sincronizar o exportar el código para trabajar en tu
entorno preferido:

- **Sincronizar con GitHub**: Conecta tu app a un repositorio de GitHub para habilitar
  la sincronización bidireccional. Puedes enviar los cambios que se solicitan en AI Studio directamente a tu
  repositorio con mensajes de confirmación generados por IA o extraer los cambios realizados de forma local
  en tu IDE o por tus compañeros de equipo de vuelta a AI Studio. Administra el estado de sincronización
  en cualquier momento en la pestaña **GitHub** de Configuración.
- **Descarga y desarrolla de forma local**: Exporta el código generado como un **archivo ZIP** y, luego, impórtalo a tu editor de código.

## Características clave

Google AI Studio incluye varias funciones para que el proceso de compilación sea
intuitivo y visual:

- **Crea apps full stack y realiza iteraciones en ellas**: Crea apps full stack con solo
  una instrucción y realiza iteraciones a través del chat o el **modo de anotación**. El modo de anotación
  te permite destacar cualquier parte de la IU de tu app y describir el
  cambio que quieres realizar.
- **Comparte e implementa tu app**: Puedes compartir tus creaciones con otras personas para
  colaborar o mostrar tu trabajo. Cuando compartes, las llamadas a la API se consideran en tus límites de uso. Si usas modelos pagados, es posible que se apliquen costos. Luego, cuando tu app esté lista,
  implementa en Cloud Run.
- **Galería de apps**: La galería de apps proporciona una biblioteca visual de ideas para proyectos.
  Puedes explorar lo que es posible con Gemini, obtener una vista previa de las aplicaciones al instante
  y modificarlas para personalizarlas.

## Implementa o archiva tu app

Cuando tu aplicación esté lista, puedes implementarla de la siguiente manera:

- **Cloud Run**: Implementa tu aplicación como un servicio escalable.
  Es posible que se apliquen precios de [Google Cloud Run](https://cloud.google.com/run?hl=es-419) según
  el uso. Para obtener más información sobre la implementación, consulta
  [Implementa desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419).
- **GitHub**: Sincroniza tu proyecto con un repositorio de GitHub nuevo o existente
  para administrar el código fuente o colaborar con tus compañeros de equipo.

## Limitaciones

En esta sección, se enumeran las limitaciones actuales del modo de compilación en Google AI Studio.

### Administración de claves de API

Cuando creas una app web nueva que usa la API de Gemini, AI Studio configura automáticamente
tu clave de API de Gemini como un secreto en el entorno del servidor de la app.
Puedes ver y administrar esta clave en el panel **Secrets**.

- **Configuración automática**: Tu `GEMINI_API_KEY` se configura automáticamente, por lo que no se requiere
  ninguna configuración manual para comenzar a compilar.
- **Solo del servidor**: Las claves de API se insertan en el entorno de ejecución del servidor y
  nunca se incluyen en el código del cliente.
- **Apps existentes**: En el caso de las apps creadas antes del 14 de mayo de 2026, el agente
  actualizará automáticamente tu integración de la API de Gemini al enfoque recomendado
  del servidor la próxima vez que modifiques las funciones de Gemini de la app.

#### Apps para Android

Cuando se compilan apps para Android, AI Studio usa
[Firebase AI Logic y Verificación de aplicaciones de Firebase](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419#firebase-integration) en lugar de una clave de API sin procesar, por lo que las credenciales nunca se incorporan en tu APK.

### Implementación fuera de Google AI Studio

- **Cloud Run**: Cuando implementas en Cloud Run desde AI Studio, tu clave de API se
  incluye de forma segura en el entorno del servidor. La app implementada usará
  tu clave de API para todas las llamadas a la API de Gemini de los usuarios.
- **Descarga de ZIP**: Si descargas tu app como un archivo ZIP para ejecutarla
  en otro lugar, deberás configurar la variable de entorno `GEMINI_API_KEY`
  en tu entorno de hosting. Como las llamadas a la API de Gemini de tu app se realizan desde
  el código del servidor, la clave no se expone a los usuarios finales.

### Error cuando se comparten apps

Si compartes tu app y el usuario final se encuentra con un error **403 Access Restricted**
cuando usa la URL compartida, puede deberse a uno de los siguientes motivos:

- **Extensiones del navegador**: Es posible que las extensiones de privacidad, como Privacy Badger, bloqueen la app. Inhabilita la extensión para evitar el error.
- **Problemas de compilación**: Es posible que haya problemas con el código actual. Pídele al
  agente que "solucione cualquier problema de compilación con el código actual" y, luego, vuelve a compartir la
  URL.

## Preguntas frecuentes

### ¿Qué es Build in AI Studio?

AI Studio Build es una plataforma diseñada para llevarte de una instrucción simple a una
aplicación potenciada por IA lista para producción con Gemini. Describe lo que
quieres compilar con una instrucción y Gemini generará una app para ti. También
puedes explorar nuestra galería para ver qué es posible con la API de Gemini
y hacer remixes de apps para personalizarlas.

### ¿Cómo controla Build mi clave de API de Gemini?

Cuando creas una app web que usa la API de Gemini, AI Studio configura automáticamente
tu clave de API de Gemini como un secreto del servidor. Las llamadas a la API de Gemini de tu app
se realizan desde el código del servidor con esta clave, por lo que nunca se expone
en el navegador. Puedes ver tu clave de API en el panel **Secrets** en
Configuración. En el caso de las apps para Android, AI Studio usa [Firebase AI Logic y la Verificación de aplicaciones de Firebase](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419#firebase-integration) para realizar llamadas seguras del cliente sin incorporar una clave de API en el objeto binario de la app.

### ¿Se expone mi clave de API cuando comparto apps?

No. Tu clave de API se almacena como un secreto del servidor y nunca se incluye en el código del cliente. Cuando compartes tu app, otros usuarios pueden usarla, pero no pueden ver tu clave de API.

Cuando compartes tus apps con otras personas, las llamadas a la API se tienen en cuenta para tus límites de uso.
Si usas modelos pagados, es posible que se apliquen costos. AI Studio te avisará
durante la configuración y antes de compartir si tu app podría generar costos.

### ¿Quién puede ver mis apps?

De forma predeterminada, tu app es privada. Puedes compartir tu app con otros usuarios para
que la usen. Los usuarios con los que compartes tu app pueden ver su código y bifurcarlo
para sus propios fines. Si compartes tu app con permiso de edición, los
demás usuarios podrán editar el código de tu app.

### ¿Puedo ejecutar apps fuera de AI Studio?

Sí. Puedes implementar tu app en
[Cloud Run](https://cloud.google.com/run?hl=es-419) desde AI Studio, lo que
le otorga una URL pública con tu clave de API configurada de forma segura en el
entorno del servidor. También puedes descargar tu app como un archivo ZIP y
alojarla en otro lugar. Deberás establecer la variable de entorno `GEMINI_API_KEY`
en tu entorno de hosting. Como las llamadas a la API de Gemini se realizan desde
el código del servidor, tu clave se mantiene segura.

Para obtener más información sobre las opciones de implementación, consulta [Implementa desde Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=es-419).

### ¿Puedo desarrollar apps de forma local con mis propias herramientas y, luego, compartirlas aquí?

Sí. Puedes conectar tu app de AI Studio a un repositorio de GitHub para desarrollarla
de forma local con tu editor de código o herramientas de CLI preferidos, enviar los cambios a
GitHub y, luego, extraer esas actualizaciones directamente a AI Studio con la
pestaña **GitHub** en Configuración.

### ¿Cómo puedo usar una base de datos o algún otro tipo de almacenamiento con mis apps?

Las apps de AI Studio son apps estándar que se ejecutan en un contenedor de Cloud Run. Puedes
usar cualquier solución de almacenamiento a la que puedas conectarte a través de una red, siempre
y cuando no haya un firewall que impida el acceso desde un rango de IP dinámico.

Estamos trabajando para agregar compatibilidad directa con el almacenamiento en el futuro, que
podrás configurar directamente en AI Studio.

### ¿Cómo puedo acceder al micrófono, la cámara web y otras APIs de Navigator?

Para garantizar que los usuarios sepan que una app usa su cámara web o algún otro dispositivo, solicitamos una confirmación adicional antes de que la app pueda acceder a estas [APIs de Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator).
Los creadores de apps pueden agregar estas solicitudes de permiso al archivo `metadata.json` de su app. Por ejemplo:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Los valores admitidos para `requestFramePermissions` son un subconjunto de las
[funciones estándar controladas por políticas](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### ¿Cómo puedo usar GitHub con mis apps?

AI Studio admite la sincronización bidireccional con GitHub:

- **Importa un repositorio**: En el modo de compilación, selecciona **Importar desde GitHub**
  en el menú **Agregar archivos** (ícono de signo más) del cuadro de entrada de instrucciones para importar
  código existente.
- **Vincula un repositorio**: En Configuración, abre la pestaña **GitHub** para crear un repositorio de GitHub nuevo desde tu app o vincularlo a uno existente.
- **Sincronización bidireccional**: Envía los cambios solicitados en AI Studio directamente a tu
  repositorio con mensajes de confirmación generados por IA o extrae los cambios realizados
  de forma externa (como ediciones locales del IDE o solicitudes de extracción de compañeros de equipo) de vuelta a AI
  Studio.
- **Resuelve conflictos de combinación**: Si los cambios entran en conflicto cuando se sincronizan con
  GitHub, AI Studio proporciona un diálogo **Resolver conflictos** con un
  visor de diferencias en paralelo, lo que te permite revisar las diferencias y elegir
  si deseas conservar la versión de AI Studio o de GitHub para cada archivo en conflicto.

### ¿Puedo otorgar acceso de edición a mi app a otros usuarios?

AI Studio no admite la edición colaborativa directa en tiempo real.
Sin embargo, puedes colaborar con tus compañeros de equipo vinculando tu app a un repositorio de GitHub compartido. Los miembros del equipo pueden enviar cambios o abrir solicitudes de extracción en GitHub,
y tú puedes incorporar esas actualizaciones en AI Studio.

### ¿Por qué se marcó mi app por incumplimiento de política?

Contamos con sistemas que revisan automáticamente las apps para garantizar que cumplan con nuestras políticas. Si descubrimos que una app incumple nuestras políticas, se quitará
de AI Studio. Los incumplimientos de política pueden incluir, entre otros, los siguientes:

- Apps que contienen software malicioso, phishing o suplantación de identidad
- Apps que muestran o distribuyen contenido que infringe la política sobre imágenes de abuso sexual infantil
- Apps que muestran o distribuyen contenido que infringe la política de hostigamiento
- Apps que muestran o distribuyen contenido que incumple la política sobre la incitación al odio o a la violencia
- Apps que muestran o distribuyen contenido que incumple la política de trata de personas
- Aplicaciones que muestran o distribuyen contenido que infringe la política de contenido sexual explícito
- Apps que muestren o distribuyan contenido que infrinja la política de contenido violento y sangriento
- Apps que muestran o distribuyen contenido que infringe la política de contenido dañino o peligroso

Si se marcó tu app por un incumplimiento de política y crees que se trata de un error, puedes enviar una apelación. Los incumplimientos reiterados de nuestras políticas pueden
ocasionar la rescisión de tu acceso a AI Studio.

### ¿Cuáles son mis responsabilidades como desarrollador de apps?

Como recordatorio, como propietario de tu aplicación, eres responsable de
su comportamiento y de todos los datos que maneja. Esto incluye lo siguiente:

- **Cumplimiento de los requisitos legales y derechos de terceros:** Asegurarte de que tu app cumpla con todas las leyes y reglamentaciones aplicables, y no infrinja los derechos de otras personas, incluidos los derechos de propiedad intelectual y privacidad
- **Supervisión de contenido:** Es posible que se aplique el cumplimiento de condiciones adicionales a
  otros servicios que use tu app. Por ejemplo,
  las [Condiciones del Servicio de Google Cloud](https://cloud.google.com/terms?hl=es-419),
  aplicables a Firestore, requieren que los clientes que alojan contenido de terceros
  publiquen políticas que definan qué contenido está prohibido (p.ej., contenido
  ilegal) y supervisen la presencia de ese contenido ilegal.
- **Implementación segura:** Implementa las protecciones y herramientas de moderación necesarias para evitar que se use tu aplicación de forma inadecuada.

Ten en cuenta las [restricciones de uso](https://ai.google.dev/gemini-api/terms?hl=es-419#use-restrictions)
en las Condiciones del Servicio.

### ¿Qué condiciones se aplican a las apps de la galería de apps en AI Studio?

Las [Condiciones del Servicio Adicionales de la API de Gemini](https://ai.google.dev/gemini-api/terms?hl=es-419)
se aplican al uso de las apps que se muestran en la galería de apps de AI Studio, a menos que
se indique lo contrario.

## ¿Qué sigue?

- [Desarrolla apps de pila completa](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=es-419) (web)
- [Compila apps para Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=es-419)
- Consulta ejemplos en la [Galería de apps](https://aistudio.google.com/apps?source=showcase&hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-20 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-20 (UTC)"],[],[]]
