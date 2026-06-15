---
source_url: https://ai.google.dev/gemini-api/docs/interactions/api-key?hl=es-419
fetched_at: 2026-06-15T06:24:57.523135+00:00
title: "C\u00f3mo usar claves de API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo usar claves de API de Gemini

Para usar la API de Gemini, debes autenticar tus solicitudes. Puedes autenticarte con una clave de API estándar o de autorización.

[Crea o visualiza una clave de API de Gemini](https://aistudio.google.com/apikey?hl=es-419)

## Tipos de claves de API: estándar y de autorización

Las claves de API proporcionan acceso a la API de Gemini, pero sus características de seguridad difieren. Para mejorar la seguridad, la API de Gemini está migrando de claves de API estándar a claves de autorización:

- **Claves de API estándar**: Asocian solicitudes con un proyecto de Google Cloud para fines de facturación y cuota. Las claves estándar no identifican a un llamador, lo que limita la granularidad de los permisos y el control de acceso que pueden admitir.
- **Claves de autorización (auth)**: Se vinculan directamente a una cuenta de servicio de Google Cloud. Cuando usas una clave de autorización, tus solicitudes se procesan con la identidad de esa cuenta de servicio vinculada, lo que permite un control de acceso detallado. De forma predeterminada, las claves de autorización están restringidas a la API de Generative Language (API de Gemini) y proporcionan una aplicación de claves filtradas de acción rápida que detiene rápidamente el uso de las claves filtradas que detectan nuestros sistemas.

Para garantizar un uso seguro, la API de Gemini pasará de las claves estándar a las claves de autenticación:

- **Claves de autorización predeterminadas**: Todas las claves de API nuevas que se crean en Google AI Studio se crean automáticamente como claves de autorización.
- **El 19 de junio de 2026**: La API de Gemini rechazará las solicitudes de **claves estándar sin restricciones**. Las claves de API estándar que tienen restricciones explícitas aplicadas seguirán funcionando. Esta restricción impide el uso no autorizado de claves que podrían compartirse públicamente o vincularse a otros servicios.
- **En septiembre de 2026**: La API de Gemini rechazará las solicitudes de las **claves estándar**. Debes [migrar a claves de autorización](#migrate-to-auth-key) antes de esta fecha para evitar la interrupción del servicio. Asegúrate de migrar a las claves de autorización antes de septiembre de 2026.

## Administra claves de API en Google AI Studio

Puedes administrar tus proyectos y claves directamente en [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).

### Proyectos de Google Cloud

Cada clave de la API de Gemini está asociada a un [proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419).
Los proyectos de Google Cloud administran la facturación, los colaboradores y los permisos. Google AI Studio proporciona una interfaz ligera para acceder a estos proyectos.

- **Proyecto predeterminado**: Si eres un usuario nuevo, Google AI Studio crea automáticamente un proyecto y una clave de API predeterminados de Google Cloud después de que aceptas las Condiciones del Servicio. Puedes cambiar el nombre de este proyecto en la vista **Proyectos** de tu panel.
- **Proyectos existentes**: Si ya tienes una cuenta de Google Cloud, AI Studio no crea un proyecto predeterminado. En cambio, debes importar tus proyectos existentes.

### Importación de proyectos

De forma predeterminada, Google AI Studio no muestra todos tus proyectos de Google Cloud. Debes importar los proyectos que quieras usar:

1. Ve a [Google AI Studio](https://aistudio.google.com?hl=es-419).
2. Abre el **Panel** desde el panel izquierdo y selecciona **Proyectos**.
3. Haz clic en el botón **Import projects**.
4. Busca y selecciona el proyecto de Google Cloud que deseas importar y, luego, haz clic en **Importar**.
5. Una vez que se haya importado, navega a la página **Claves de API** en el panel para crear una clave en ese proyecto.

### Soluciona problemas relacionados con los permisos de creación de claves

Si el botón **Crear clave de API** no está disponible y muestra el mensaje *"No tienes permiso para crear una clave en este proyecto"*, significa que no tienes los permisos de IAM necesarios.

Pídele al administrador de tu proyecto u organización de Google Cloud que te otorgue un rol que contenga los siguientes permisos (como el de editor del proyecto):

- `resourcemanager.projects.get`: Permite que AI Studio verifique el proyecto.
- `apikeys.keys.create`: Permite la generación de claves.
- `serviceusage.services.enable`: Garantiza que la API de Generative Language esté habilitada.
- `iam.serviceAccounts.create`: Se requiere para crear la cuenta de servicio vinculada.
- `iam.serviceAccountApiKeyBindings.create`: Vincula la cuenta de servicio a la clave de API.

Si no puedes obtener acceso administrativo, puedes crear un proyecto nuevo de Google Cloud que no esté asociado a una organización para generar tus claves.

## Configura tu entorno

Una vez que tengas una clave, configura tu entorno para usarla de forma segura en tus aplicaciones.

### Opción 1: Usa variables de entorno (recomendado)

Configura la variable de entorno `GEMINI_API_KEY` o `GOOGLE_API_KEY`. Las bibliotecas cliente de la API de Gemini detectan y usan automáticamente estas variables. Si se configuran ambos, `GOOGLE_API_KEY` tiene prioridad.

Selecciona tu sistema operativo para configurar la variable:

### Linux/macOS (Bash)

Verifica si tienes un archivo de configuración de bash:

```
~/.bashrc
```

De lo contrario, crea uno y ábrelo:

```
touch ~/.bashrc && open ~/.bashrc
```

Agrega el comando de exportación al final del archivo:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Guarda el archivo y, luego, aplica los cambios:

```
source ~/.bashrc
```

### macOS: Zsh

Verifica si tienes un archivo de configuración de zsh:

```
~/.zshrc
```

De lo contrario, crea uno y ábrelo:

```
touch ~/.zshrc && open ~/.zshrc
```

Agrega el comando de exportación:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Guarda el archivo y, luego, aplica los cambios:

```
source ~/.zshrc
```

### Windows

1. Busca "Variables de entorno" en la barra de búsqueda de Windows.
2. Haz clic en **Variables de entorno** en el diálogo Propiedades del sistema.
3. En **User variables** o **System variables**, haz clic en **New…**.
4. Establece el nombre de la variable en `GEMINI_API_KEY` y el valor en tu clave de API.
5. Haga clic en **Aceptar** para guardar los cambios. Abre una sesión de terminal nueva para cargar la variable.

### Opción 2: Proporciona la clave de API de forma explícita en el código

Puedes pasar la clave de API de forma explícita cuando inicializas el cliente. Hazlo solo si no puedes usar variables de entorno.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
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
    "google.golang.org/genai/interactions"
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

    interaction, err := client.Interactions.NewModel(ctx, interactions.NewModelParams{
        Model: "gemini-3.5-flash",
        Input: interactions.Input{
            String: "Explain how AI works in a few words",
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range interaction.Steps {
        if step.ModelOutput != nil {
            for _, content := range step.ModelOutput.Content {
                if content.Text != nil {
                    fmt.Println(content.Text.Text)
                }
            }
        }
    }
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.interactions.models.interactions.CreateModelInteractionParams;
import com.google.genai.interactions.models.interactions.Interaction;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    CreateModelInteractionParams params =
        CreateModelInteractionParams.builder()
            .input("Explain how AI works in a few words")
            .model("gemini-3.5-flash")
            .build();

    Interaction interaction = client.interactions.create(params);

    interaction.steps().forEach(step -> {
      if (step.isModelOutput()) {
        step.asModelOutput().content().ifPresent(contents -> {
          contents.forEach(content -> {
            content.text().ifPresent(text -> System.out.println(text.text()));
          });
        });
      }
    });
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -X POST \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Administración de seguridad y secretos

Trata tu clave de la API de Gemini como una contraseña. Si se ve comprometida, otras personas pueden consumir la cuota de tu proyecto, generar cargos inesperados en la facturación y acceder a recursos privados.

### Reglas de seguridad críticas

- **Mantén la confidencialidad de las claves**: Nunca registres claves de API en sistemas de control de código fuente como Git.
- **Nunca expongas claves del cliente en producción**: No codifiques de forma rígida las claves de API directamente en las apps web o para dispositivos móviles. Los usuarios pueden extraer las claves compiladas en el código del cliente. Para proteger las apps del cliente, ejecuta un servidor proxy de backend para realizar las llamadas a la API reales.

### Prácticas recomendadas para la administración de secretos

- **Variables de entorno**: Lee las claves de las variables de entorno en lugar de los archivos de configuración.
- **Secret Manager**: Para la producción, almacena tus claves en un almacén de secretos seguro, como [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=es-419).
- **Alertas de facturación**: Configura alertas de facturación en la consola de Google Cloud para recibir notificaciones si se produce un aumento repentino en el uso o los costos.

### Lista de tareas para la respuesta ante filtraciones

Si sospechas que se filtró tu clave de API, haz lo siguiente:

1. **Genera una clave nueva**: Crea una clave de reemplazo en Google AI Studio o en la consola de Cloud.
2. **Actualiza tu aplicación**: Implementa tu código con la clave nueva.
3. **Inhabilita o borra la clave comprometida**: Inhabilita la clave filtrada en Cloud Console una vez que se verifique la clave nueva. No borres la clave anterior hasta que la nueva esté completamente activa para evitar el tiempo de inactividad de la aplicación.
4. **Audita el uso**: Revisa los registros de facturación y el uso de la API en la consola de Google Cloud para identificar actividad no autorizada.

## Cómo restringir y proteger tus claves

Si agregas restricciones a tus claves de API, se minimizan los posibles daños en caso de que se vulnere una clave.

### Aplica restricciones de origen de la solicitud

Las restricciones de origen limitan qué direcciones IP, sitios web o aplicaciones pueden usar tu clave.

1. Ve a la [página Credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona tu proyecto y haz clic en el nombre de la clave de API que deseas restringir.
3. En **Restricciones de aplicaciones**, selecciona **Direcciones IP** (o el tipo de restricción adecuado para tu entorno).
4. Especifica los rangos o las direcciones IP permitidas y, luego, haz clic en **Guardar**.

### Cómo proteger las claves de API estándar no restringidas

Para seguir usando la API de Gemini después del 19 de junio de 2026, debes proteger las claves sin restricciones.

#### Método A: Restringe la clave solo a la API de Gemini (AI Studio)

Si solo usas la clave para la API de Gemini, protégela directamente en AI Studio:

1. En la página **Claves de API** de [Google AI Studio](https://aistudio.google.com/api-keys?hl=es-419), busca las claves marcadas con la etiqueta **Sin restricciones**.
2. Coloca el cursor sobre la etiqueta y haz clic en **Agregar restricciones** en el diálogo.
3. Selecciona **Restringir solo a la API de Gemini**.
4. Haz clic en **Restringir clave** para confirmar.

#### Método B: Restringe la clave para otros servicios (consola de Google Cloud)

Si la clave se comparte con otras APIs de Google (no se recomienda), restrínsela en la consola de Cloud. **Nota: Las solicitudes a la API de Gemini que usen esta clave fallarán después de que se apliquen estas restricciones.**

1. Visita la [página Credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona el proyecto y la clave de API.
3. En **API restrictions**, selecciona **Restrict key**.
4. En el menú desplegable, selecciona las APIs a las que quieres que acceda esta clave. No selecciones la **API de Generative Language**.
5. Haz clic en **Guardar**. Crea una clave independiente y restringida en AI Studio para seguir usando la API de Gemini.

### Claves inactivas bloqueadas

A partir del 7 de mayo de 2026, la API de Gemini bloqueará las claves de API sin restricciones que hayan estado inactivas durante un período prolongado. Estas claves muestran una etiqueta **Bloqueado** en AI Studio. Para continuar, debes generar una clave nueva o usar una clave restringida existente.

## Migra a una clave de autorización

Sigue estos pasos para crear una nueva clave de API de autorización y actualizar tus aplicaciones:

1. Ve a la [página Claves de API de AI Studio](https://aistudio.google.com/api-keys?hl=es-419).
2. Verifica la columna **Key Type** para identificar las claves que se indican como **Standard**.
3. Haz clic en **Crear clave de API** para generar una clave nueva. Todas las claves nuevas creadas en AI Studio se crean automáticamente como claves de autorización.
4. Copia la nueva clave de API de autorización.
5. Actualiza el código de tu aplicación, las variables de entorno y cualquier configuración de implementación para usar la nueva clave de API de autenticación.
6. Prueba tu aplicación para confirmar que funciona correctamente con la nueva clave.
7. Una vez que se verifique, borra o revoca tu clave de tráfico anterior para evitar el uso inadecuado.

## Limitaciones

Google AI Studio impone las siguientes limitaciones de administración de proyectos y claves:

- Puedes crear un máximo de 10 proyectos a la vez desde la página **Projects** de Google AI Studio.
- En las páginas **Claves de API** y **Proyectos**, se muestran un máximo de 100 claves y 50 proyectos.
- Solo se muestran las claves de API que no están restringidas o que están restringidas específicamente a la API de Generative Language (API de Gemini).

Para la administración avanzada de proyectos o para modificar claves con otras restricciones, usa la [página de credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-11 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-11 (UTC)"],[],[]]
