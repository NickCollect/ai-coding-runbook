---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=es-419
fetched_at: 2026-05-05T20:05:48.754014+00:00
title: "C\u00f3mo usar claves de API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo usar claves de API de Gemini

Para usar la API de Gemini, necesitas una clave de API. En esta página, se describe cómo crear y administrar tus claves en Google AI Studio, así como configurar tu entorno para usarlas en tu código.

[Cómo crear o ver una clave de API de Gemini](https://aistudio.google.com/app/apikey?hl=es-419)

## Claves de API

Puedes crear y administrar todas tus claves de API de Gemini desde la
[página](https://aistudio.google.com/app/apikey?hl=es-419) **Claves de API** de Google AI Studio.

Una vez que tengas una clave de API, tendrás las siguientes opciones para conectarte a la API de Gemini:

- [Establecer tu clave de API como una variable de entorno](#set-api-env-var)
- [Proporcionar tu clave de API de forma explícita](#provide-api-key-explicitly)

Para las pruebas iniciales, puedes codificar de forma rígida una clave de API, pero esto solo debe ser temporal, ya que no es seguro. Puedes encontrar ejemplos para codificar de forma rígida la clave de API
en la sección [Proporciona la clave de API de forma explícita](#provide-api-key-explicitly).

## Proyectos de Google Cloud

Los [proyectos de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419)
son fundamentales para usar los servicios de Google Cloud (como la API de Gemini),
administrar la facturación y controlar los colaboradores y los permisos. Google AI Studio proporciona una interfaz ligera para tus proyectos de Google Cloud.

Si aún no creaste ningún proyecto, debes crear uno nuevo o importar uno de Google Cloud a Google AI Studio. En la página **Proyectos** de Google AI Studio, se mostrarán todas las claves que tengan permisos suficientes para usar la API de Gemini. Consulta la sección [Importar proyectos](#import-projects) para obtener instrucciones.

### Proyecto predeterminado

Para los usuarios nuevos, después de aceptar las Condiciones del Servicio, Google AI Studio crea un proyecto de Google Cloud y una clave de API predeterminados para facilitar el uso. Para cambiar el nombre de este
proyecto en Google AI Studio, navega a la vista **Proyectos** en el
**Panel**, haz clic en el botón de configuración de 3 puntos junto a un proyecto y
elige **Cambiar nombre del proyecto**. Los usuarios existentes o los que ya tienen cuentas de Google Cloud no tendrán un proyecto predeterminado creado.

## Importar proyectos

Cada clave de API de Gemini está asociada a un proyecto de Google Cloud. De forma predeterminada, Google AI Studio no muestra todos tus proyectos de Cloud. Debes importar los proyectos que desees buscando el nombre o el ID del proyecto en el diálogo **Importar proyectos**. Para ver una lista completa de los proyectos a los que tienes acceso, visita Cloud Console.

Si aún no importaste ningún proyecto, sigue estos pasos para importar un proyecto de Google Cloud y crear una clave:

1. Ve a [Google AI Studio](https://aistudio.google.com?hl=es-419).
2. Abre el **Panel** desde el panel lateral izquierdo.
3. Selecciona **Proyectos**.
4. Selecciona el botón **Importar proyectos** en la página **Proyectos**.
5. Busca y selecciona el proyecto de Google Cloud que deseas importar y selecciona el botón **Importar**.

Una vez que se importe un proyecto, ve a la página **Claves de API** desde el menú **Panel** y crea una clave de API en el proyecto que acabas de importar.

## Limitaciones

Las siguientes son limitaciones de la administración de claves de API y proyectos de Google Cloud en Google AI Studio.

- Puedes crear un máximo de 10 proyectos a la vez desde la página **Proyectos** de Google AI Studio.
- Puedes asignar nombres a proyectos y claves, y cambiarles el nombre.
- En las páginas **Claves de API** y **Proyectos** , se muestran un máximo de 100 claves y 50 proyectos.
- Solo se muestran las claves de API que no tienen restricciones o que están restringidas a la API de Generative Language.

Para obtener acceso de administración adicional a tus proyectos, lo que incluye modificar y
restringir claves de API, visita la
[página de credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
En Cloud Console, puedes seleccionar tu proyecto, hacer clic en una clave de API existente y, luego, restringirla a la **API de Generative Language**.

## Cómo establecer la clave de API como una variable de entorno

Si estableces la variable de entorno `GEMINI_API_KEY` o `GOOGLE_API_KEY`, la
clave de API se recuperará automáticamente por el cliente cuando uses una de las
[bibliotecas de la API de Gemini](https://ai.google.dev/gemini-api/docs/libraries?hl=es-419). Te recomendamos que establezcas solo una de esas variables, pero, si se establecen ambas, `GOOGLE_API_KEY` tiene prioridad.

Si usas la API de REST o JavaScript en el navegador, deberás proporcionar la clave de API de forma explícita.

A continuación, se explica cómo puedes establecer tu clave de API de forma local como la variable de entorno `GEMINI_API_KEY` con diferentes sistemas operativos.

### Linux/macOS - Bash

Bash es una configuración de terminal común de Linux y macOS. Para verificar si tienes un archivo de configuración, ejecuta el siguiente comando:

```
~/.bashrc
```

Si la respuesta es "No existe ese archivo o directorio", deberás crear este archivo y abrirlo ejecutando los siguientes comandos o usar `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

A continuación, debes establecer tu clave de API agregando el siguiente comando de exportación:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Después de guardar el archivo, ejecuta lo siguiente para aplicar los cambios:

```
source ~/.bashrc
```

### macOS - Zsh

Zsh es una configuración de terminal común de Linux y macOS. Para verificar si tienes un archivo de configuración, ejecuta el siguiente comando:

```
~/.zshrc
```

Si la respuesta es "No existe ese archivo o directorio", deberás crear este archivo y abrirlo ejecutando los siguientes comandos o usar `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

A continuación, debes establecer tu clave de API agregando el siguiente comando de exportación:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Después de guardar el archivo, ejecuta lo siguiente para aplicar los cambios:

```
source ~/.zshrc
```

### Windows

1. Busca "Variables de entorno" en la barra de búsqueda.
2. Elige modificar la **Configuración del sistema**. Es posible que debas confirmar que deseas hacerlo.
3. En el diálogo de configuración del sistema, haz clic en el botón etiquetado como **Variables de entorno**.
4. En **Variables de usuario** (para el usuario actual) o **Variables del sistema** (se aplica a todos los usuarios que usan la máquina), haz clic en **Nueva…**
5. Especifica el nombre de la variable como `GEMINI_API_KEY`. Especifica tu clave de API de Gemini como el valor de la variable.
6. Haz clic en **Aceptar** para aplicar los cambios.
7. Abre una nueva sesión de terminal (cmd o Powershell) para obtener la variable nueva.

## Cómo proporcionar la clave de API de forma explícita

En algunos casos, es posible que desees proporcionar una clave de API de forma explícita. Por ejemplo:

- Estás realizando una llamada a la API simple y prefieres codificar de forma rígida la clave de API.
- Quieres un control explícito sin tener que depender de la detección automática de variables de entorno por parte de las bibliotecas de la API de Gemini.
- Usas un entorno en el que no se admiten variables de entorno (p. ej., la Web) o realizas llamadas a REST.

A continuación, se muestran ejemplos de cómo puedes proporcionar una clave de API de forma explícita:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Protege tu clave de API

Trata tu clave de API de Gemini como una contraseña. Si se vulnera, otras personas pueden usar la cuota de tu proyecto, generar cargos (si la facturación está habilitada) y acceder a tus datos privados, como archivos.

### Reglas de seguridad críticas

- **Mantén la confidencialidad de las claves**: Las claves de API de Gemini pueden acceder a datos sensibles de los que depende tu
  aplicación.

  - **Nunca confirmes las claves de API en el control de versiones.** No registres tu clave de API en sistemas de control de versiones como Git.
  - **Nunca expongas las claves de API en el cliente.** No uses tu clave de API directamente en apps web o para dispositivos móviles en producción. Se pueden extraer claves en el código del cliente (incluidas nuestras bibliotecas de JavaScript/TypeScript y las llamadas a REST).
- **Restringe el acceso**: Cuando sea posible, restringe el uso de la clave de API a direcciones IP, URLs de referencia HTTP
  o apps para Android o iOS específicas.
- **Restringe el uso**: Habilita solo las APIs necesarias para cada clave.
- **Realiza auditorías periódicas**: Audita tus claves de API con regularidad y rótalas
  de forma periódica.

### Prácticas recomendadas

- **Usa llamadas del servidor con claves de API** : La forma más segura de usar tu clave de API es llamar a la API de Gemini desde una aplicación del servidor en la que la clave se pueda mantener confidencial.
- **Usa tokens efímeros para el acceso del cliente (solo API en vivo):** Para el acceso directo del cliente a la API en vivo, puedes usar tokens efímeros. Tienen riesgos de seguridad más bajos y pueden ser adecuados para el uso en producción. Consulta la guía de
  [tokens efímeros](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=es-419) para obtener más
  información.
- **Considera agregar restricciones a tu clave:** Puedes limitar los permisos de una clave
  agregando [restricciones de clave de API](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=es-419#add-api-restrictions).
  Esto minimiza el daño potencial si la clave se filtra.

Para conocer algunas prácticas recomendadas generales, también puedes consultar este
[artículo de asistencia](https://support.google.com/googleapi/answer/6310037?hl=es-419).

## Solución de problemas de creación de claves de API

En Google AI Studio, es posible que el botón **Crear clave de API** no esté disponible y aparezca
el mensaje: "*No tienes permiso para crear una clave en este proyecto*".

Esto ocurre cuando no tienes los permisos necesarios en el proyecto para generar una clave nueva:

- **`resourcemanager.projects.get`**: Permite que AI Studio verifique la existencia del proyecto.
- **`apikeys.keys.create`**: Permite la generación de la clave de API.
- **`serviceusage.services.enable`**: Es necesario para garantizar que la API de Gemini esté activa en el proyecto.

Para corregir tus permisos, pídele al administrador del proyecto o al administrador de tu organización (si el proyecto pertenece a una [organización](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=es-419)) que te otorgue un rol con los permisos mencionados anteriormente (como Editor del proyecto o un rol personalizado).

Si no tienes acceso administrativo a un proyecto, puedes crear uno nuevo que no esté asociado con una organización para generar tus claves.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-04-29 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-04-29 (UTC)"],[],[]]
