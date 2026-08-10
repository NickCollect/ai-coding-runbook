---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=es-419
fetched_at: 2026-08-10T03:14:27.682874+00:00
title: "Gu\u00eda de inicio r\u00e1pido de Authentication con OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Guía de inicio rápido de Authentication con OAuth

La forma más sencilla de autenticarse en la API de Gemini es configurar una clave de API, como se describe en la [guía de inicio rápido de la API de Gemini](https://ai.google.dev/gemini-api/docs/get-started?hl=es-419). Si necesitas controles de acceso más estrictos, puedes usar OAuth en su lugar. Esta guía te ayudará a configurar la autenticación con OAuth.

En esta guía, se usa un enfoque de autenticación simplificado que es adecuado para un entorno de pruebas. En el caso de un entorno de producción, obtén información sobre la [autenticación y la autorización](https://developers.google.com/workspace/guides/auth-overview?hl=es-419) antes de [elegir las credenciales de acceso](https://developers.google.com/workspace/guides/create-credentials?hl=es-419#choose_the_access_credential_that_is_right_for_you) adecuadas para tu app.

## Objetivos

- Configura tu proyecto de Cloud para OAuth
- Configura las credenciales predeterminadas de la aplicación
- Administra las credenciales en tu programa en lugar de usar `gcloud auth`

## Requisitos previos

Para ejecutar esta guía de inicio rápido, necesitas lo siguiente:

- [Un proyecto de Google Cloud](https://developers.google.com/workspace/guides/create-project?hl=es-419)
- [Una instalación local de la CLI de gcloud](https://cloud.google.com/sdk/docs/install?hl=es-419)

## Configura tu proyecto de Cloud

Para completar esta guía de inicio rápido, primero debes configurar tu proyecto de Cloud.

### 1. Habilita la API

Antes de usar las APIs de Google, debes activarlas en un proyecto de Google Cloud.

- En la consola de Google Cloud, habilita la API de Google Generative Language.

  [Habilitar la API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=es-419)

### 2. Cómo configurar la pantalla de consentimiento de OAuth

A continuación, configura la pantalla de consentimiento de OAuth del proyecto y agrégate como usuario de prueba. Si ya completaste este paso para tu proyecto de Cloud, ve a la siguiente sección.

1. En la consola de Google Cloud, ve a **Menú** > **Plataforma de Google Auth** > **Descripción general**.

   [Ir a Google Auth Platform](https://console.developers.google.com/auth/overview?hl=es-419)
2. Completa el formulario de configuración del proyecto y establece el tipo de usuario como **Externo** en la sección **Público**.
3. Completa el resto del formulario, acepta las condiciones de la Política de Datos del Usuario y, luego, haz clic en **Crear**.
4. Por ahora, puedes omitir la adición de permisos y hacer clic en **Guardar y continuar**. En el futuro, cuando crees una app para usarla fuera de tu organización de Google Workspace, deberás agregar y verificar los alcances de autorización que requiere tu app.
5. Agrega usuarios de prueba:

   1. Navega a la [página Audience](https://console.developers.google.com/auth/audience?hl=es-419) de la plataforma de autenticación de Google.
   2. En **Usuarios de prueba**, haz clic en **Agregar usuarios**.
   3. Ingresa tu dirección de correo electrónico y los demás usuarios de prueba autorizados, y haz clic en **Guardar**.

### 3. Autoriza credenciales para una aplicación de escritorio

Para autenticarte como usuario final y acceder a los datos del usuario en tu app, debes crear uno o más IDs de cliente de OAuth 2.0. Un ID de cliente se usa con el fin de identificar una sola app para los servidores de OAuth de Google. Si tu app se ejecuta en varias plataformas, debes crear un ID de cliente independiente para cada una de ellas.

1. En el menú de navegación de la consola de Google Cloud, ve a **Menú** > **Plataforma de Google Auth** > **Clientes**.

   [Ir a Credenciales](https://console.developers.google.com/auth/clients?hl=es-419)
2. Haz clic en **Crear cliente**.
3. Haz clic en **Tipo de aplicación** > **App de escritorio**.
4. En el campo **Nombre**, escribe un nombre para la credencial. Este nombre solo se muestra en la consola de Google Cloud.
5. Haz clic en **Crear**. Aparecerá la pantalla Cliente de OAuth creado, que muestra tu nuevo ID de cliente y secreto de cliente.
6. Haz clic en **Aceptar**. La credencial recién creada aparecerá en **IDs de cliente de OAuth 2.0.**
7. Haz clic en el botón de descarga para guardar el archivo JSON. Se guardará como `client_secret_<identifier>.json`. Cámbiale el nombre a `client_secret.json` y muévelo a tu directorio de trabajo.

## Configura credenciales predeterminadas de la aplicación

Para convertir el archivo `client_secret.json` en credenciales utilizables, pasa su ubicación al argumento `--client-id-file` del comando `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

La configuración simplificada del proyecto en este instructivo activa un diálogo **"Google no verificó esta app"**. Esto es normal. Elige **“Continuar”**.

Esto coloca el token resultante en una ubicación conocida para que `gcloud` o las bibliotecas cliente puedan acceder a él.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Una vez que configures las credenciales predeterminadas de la aplicación (ADC), las bibliotecas cliente en la mayoría de los lenguajes necesitarán poca o ninguna ayuda para encontrarlas.

### Curl

La forma más rápida de probar que esto funciona es usarlo para acceder a la API de REST con curl:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

En Python, las bibliotecas cliente deberían encontrarlas automáticamente:

```
pip install google-genai
```

Una secuencia de comandos mínima para probarlo podría ser la siguiente:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Próximos pasos

Si funciona, puedes probar la [recuperación semántica en tus datos de texto](https://ai.google.dev/docs/semantic_retriever?hl=es-419).

## Administra las credenciales por tu cuenta [Python]

En muchos casos, no tendrás disponible el comando `gcloud` para crear el token de acceso a partir del ID de cliente (`client_secret.json`). Google proporciona bibliotecas en muchos lenguajes para que puedas administrar ese proceso dentro de tu app. En esta sección, se muestra el proceso en Python. En la [documentación de la API de Drive](https://developers.google.com/drive/api/quickstart/python?hl=es-419), hay ejemplos equivalentes de este tipo de procedimiento para otros lenguajes.

### 1. Instala las bibliotecas necesarias

Instala la biblioteca cliente de Google para Python y la biblioteca cliente de Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Escribe el administrador de credenciales

Para minimizar la cantidad de veces que debes hacer clic en las pantallas de autorización, crea un archivo llamado `load_creds.py` en tu directorio de trabajo para almacenar en caché un archivo `token.json` que se pueda reutilizar más adelante o actualizar si vence.

Comienza con el siguiente código para convertir el archivo `client_secret.json` en un token que se pueda usar con `genai.configure`:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Escribe tu programa

Ahora crea tu `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Ejecuta tu programa

En tu directorio de trabajo, ejecuta la muestra:

```
python script.py
```

La primera vez que ejecutes la secuencia de comandos, se abrirá una ventana del navegador y se te solicitará que autorices el acceso.

1. Si aún no accediste a tu Cuenta de Google, se te solicitará que lo hagas. Si accediste a varias cuentas, **asegúrate de seleccionar la cuenta que configuraste como "Cuenta de prueba" cuando configuraste tu proyecto.**
2. La información de autorización se almacena en el sistema de archivos, por lo que la próxima vez que ejecutes el código de muestra, no se te solicitará la autorización.

Configuraste correctamente la autenticación.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-01 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-01 (UTC)"],[],[]]
