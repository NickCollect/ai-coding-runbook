---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=es-419
fetched_at: 2026-10-19T05:43:52.318126+00:00
title: "C\u00f3mo usar claves de API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo usar claves de API de Gemini

Para usar la API de Gemini, debes autenticar tus solicitudes. Puedes autenticarte con una clave de API estándar o de autorización.

[Cómo crear o ver una clave de API de Gemini](https://aistudio.google.com/apikey?hl=es-419)

## Tipos de claves de API: estándar y de autorización

Las claves de API proporcionan acceso a la API de Gemini, pero sus características de seguridad difieren. Para mejorar la seguridad, la API de Gemini está realizando una transición de las claves de API estándar a las claves de autorización:

- **Claves de API estándar**: Asocian solicitudes con un proyecto de Google Cloud para fines de facturación y cuota. Las claves estándar no identifican a un llamador, lo que limita la granularidad de los permisos y el control de acceso que pueden admitir.
- **Claves de autorización (auth)**: Se vinculan directamente a una cuenta de servicio de Google Cloud. Cuando usas una clave de autorización, tus solicitudes se procesan con la identidad de esa cuenta de servicio vinculada, lo que permite un control de acceso detallado. De forma predeterminada, las claves de autorización están restringidas a la API de Generative Language (API de Gemini) y proporcionan una aplicación de claves filtradas de acción rápida que detiene rápidamente el uso de las claves filtradas detectadas por nuestros sistemas.

Para garantizar un uso seguro, la API de Gemini pasará de las claves estándar a las claves de autorización:

- **Valores predeterminados de las claves de autorización**: A partir del 28 de mayo de 2026, todas las claves de API nuevas que se creen en Google AI Studio se crearán automáticamente como claves de autorización.
- **Se rechazan las claves sin restricciones**: La API de Gemini rechaza las solicitudes de **claves estándar sin restricciones**. Las claves de API estándar que tienen restricciones explícitas aplicadas siguen funcionando. Esta restricción impide el uso no autorizado de claves que podrían compartirse públicamente o vincularse a otros servicios.

## Administra claves de API en Google AI Studio

Puedes administrar tus proyectos y claves directamente en [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).

### Proyectos de Google Cloud

Cada clave de la API de Gemini está asociada a un [proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419).
Los proyectos de Google Cloud administran la facturación, los colaboradores y los permisos. Google AI Studio proporciona una interfaz ligera para acceder a estos proyectos.

- **Proyecto predeterminado**: Si eres un usuario nuevo, Google AI Studio crea automáticamente un proyecto predeterminado de Google Cloud y una clave de API después de que aceptas las Condiciones del Servicio. Para cambiarle el nombre a este proyecto, navega a la vista **Projects** en tu panel.
- **Proyectos existentes**: Si ya tienes una cuenta de Google Cloud, AI Studio no crea un proyecto predeterminado. En su lugar, debes importar tus proyectos existentes.

### Cómo importar proyectos

De forma predeterminada, Google AI Studio no muestra todos tus proyectos de Google Cloud. Debes importar los proyectos que quieras usar:

1. Ve a [Google AI Studio](https://aistudio.google.com?hl=es-419).
2. Abre el **Panel** en el panel izquierdo y selecciona **Proyectos**.
3. Haz clic en el botón **Importar proyectos**.
4. Busca y selecciona el proyecto de Google Cloud que deseas importar y, luego, haz clic en **Importar**.
5. Una vez que se haya importado, navega a la página **Claves de API** en el panel para crear una clave en ese proyecto.

### Soluciona problemas relacionados con los permisos de creación de llaves

Si el botón **Crear clave de API** no está disponible y muestra el mensaje *"No tienes permiso para crear una clave en este proyecto"*, significa que no tienes los permisos de IAM necesarios.

Pídele al administrador de tu organización o proyecto de Google Cloud que te otorgue un rol que contenga los siguientes permisos (como el de editor del proyecto):

- `resourcemanager.projects.get`: Permite que AI Studio verifique el proyecto.
- `apikeys.keys.create`: Permite la generación de claves.
- `serviceusage.services.enable`: Garantiza que la API de Generative Language esté habilitada.
- `iam.serviceAccounts.create`: Se requiere para crear la cuenta de servicio vinculada.
- `iam.serviceAccountApiKeyBindings.create`: Vincula la cuenta de servicio a la clave de API.

Si no puedes obtener acceso administrativo, puedes crear un proyecto nuevo de Google Cloud que no esté asociado a una organización para generar tus claves.

## Crea claves en la consola de Google Cloud

Google AI Studio solo muestra las claves que no están restringidas o que están restringidas a la API de Gemini. Si no puedes usar AI Studio o quieres administrar todas tus claves de API en un solo lugar, sigue la documentación de Cloud para [crear una clave de API](https://cloud.google.com/docs/authentication/api-keys?hl=es-419#create). Para crear una clave de la API de Gemini, debes vincularla a una [cuenta de servicio](https://cloud.google.com/iam/docs/service-account-overview?hl=es-419).

## Configura tu entorno

Una vez que tengas una clave, configura tu entorno para usarla de forma segura en tus aplicaciones.

### Opción 1: Usa variables de entorno (recomendado)

Establece la variable de entorno `GEMINI_API_KEY` o `GOOGLE_API_KEY`. Las bibliotecas cliente de la API de Gemini detectan y usan automáticamente estas variables. Si se configuran ambos, `GOOGLE_API_KEY` tiene prioridad.

Selecciona tu sistema operativo para establecer la variable:

### Linux/macOS - Bash

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
3. En **Variables del usuario** o **Variables del sistema**, haz clic en **Nueva…**.
4. Establece el nombre de la variable en `GEMINI_API_KEY` y el valor en tu clave de API.
5. Haga clic en **Aceptar** para guardar los cambios. Abre una sesión de terminal nueva para cargar la variable.

### Opción 2: Proporciona la clave de API de forma explícita en el código

Puedes pasar la clave de API de forma explícita cuando inicialices el cliente. Solo hazlo si no puedes usar variables de entorno.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few sentences."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Administración de seguridad y secretos

Trata tu clave de API de Gemini como una contraseña. Si se ve comprometida, otras personas pueden consumir la cuota de tu proyecto, generar cargos de facturación inesperados y acceder a recursos privados.

### Reglas de seguridad críticas

- **Mantén la confidencialidad de las claves**: Nunca registres claves de API en sistemas de control de código fuente como Git.
- **Nunca expongas claves del cliente en producción**: No codifiques de forma rígida las claves de API directamente en las apps web o para dispositivos móviles. Los usuarios pueden extraer las claves compiladas en el código del cliente. Para proteger las apps del cliente, ejecuta un servidor proxy de backend para realizar las llamadas a la API reales.

### Prácticas recomendadas para la administración de secretos

- **Variables de entorno**: Lee las claves de las variables de entorno en lugar de los archivos de configuración.
- **Secret Manager**: Para la producción, almacena tus claves en un almacén de secretos seguro, como [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=es-419).
- **Alertas de facturación**: Configura alertas de facturación en la consola de Google Cloud para recibir notificaciones si se produce un aumento repentino en el uso o los costos.

### Lista de tareas de respuesta ante filtraciones

Si sospechas que se filtró tu clave de API, haz lo siguiente:

1. **Genera una clave nueva**: Crea una clave de reemplazo en Google AI Studio o en la consola de Cloud.
2. **Actualiza tu aplicación**: Implementa tu código con la clave nueva.
3. **Inhabilita o borra la clave comprometida**: Inhabilita la clave filtrada en la consola de Cloud una vez que se verifique la clave nueva. No borres la clave anterior hasta que la nueva esté completamente activa para evitar el tiempo de inactividad de la aplicación.
4. **Audita el uso**: Revisa los registros de facturación y el uso de la API en la consola de Google Cloud para identificar actividad no autorizada.

## Cómo restringir y proteger tus claves

Si agregas restricciones a tus claves de API, se minimizan los posibles daños en caso de que se vulnere una clave.

### Aplica restricciones de origen de la solicitud

Las restricciones de origen limitan qué direcciones IP, sitios web o aplicaciones pueden usar tu clave.

1. Ve a la [página Credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona tu proyecto y haz clic en el nombre de la clave de API que deseas restringir.
3. En **Restricciones de aplicaciones**, selecciona **Direcciones IP** (o el tipo de restricción adecuado para tu entorno).
4. Especifica los rangos o las direcciones IP permitidos y, luego, haz clic en **Guardar**.

### Cómo proteger las claves de API estándar sin restricciones

Para seguir usando la API de Gemini, debes proteger todas las claves no restringidas.

#### Método A: Restringe la clave solo a la API de Gemini (AI Studio)

Si solo usas la clave para la API de Gemini, protégela directamente en AI Studio:

1. En la página **Claves de API** de [Google AI Studio](https://aistudio.google.com/api-keys?hl=es-419), busca las claves marcadas con la etiqueta **Sin restricciones**.
2. Coloca el cursor sobre la etiqueta y haz clic en **Agregar restricciones** en el diálogo.
3. Selecciona **Restringir solo a la API de Gemini**.
4. Haz clic en **Restringir clave** para confirmar.

#### Método B: Restringe la clave para otros servicios (consola de Google Cloud)

Si la clave se comparte con otras APIs de Google (no se recomienda), restrínsela en la consola de Cloud. **Nota: Las solicitudes a la API de Gemini que usen esta clave fallarán después de que se apliquen estas restricciones.**

1. Visita la [página de credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona el proyecto y la clave de API.
3. En **Restricciones de API**, usa el menú desplegable **Elige las restricciones de API** para seleccionar las APIs a las que deseas que acceda esta clave. No selecciones la **API de Generative Language**.
4. Haz clic en **Guardar**. Crea una clave independiente y restringida en AI Studio para seguir usando la API de Gemini.

### Claves inactivas bloqueadas

A partir del 7 de mayo de 2026, la API de Gemini bloqueará las claves de API sin restricciones que hayan estado inactivas durante un período prolongado. Estas claves muestran una etiqueta **Bloqueado** en AI Studio. Para continuar, debes generar una clave nueva o usar una clave restringida existente.

## Migra a una clave de autorización

Sigue estos pasos para crear una nueva clave de API de autenticación y actualizar tus aplicaciones:

1. Ve a la [página Claves de API de AI Studio](https://aistudio.google.com/api-keys?hl=es-419).
2. Revisa la columna **Tipo de clave** para identificar las claves que se indican como **Estándar**.
3. Haz clic en **Crear clave de API** para generar una clave nueva. Todas las claves nuevas creadas en AI Studio se crean automáticamente como claves de autorización.
4. Copia la nueva clave de API de autenticación.
5. Actualiza el código de tu aplicación, las variables de entorno y cualquier configuración de implementación para usar la nueva clave de API de autenticación.
6. Prueba tu aplicación para confirmar que funciona correctamente con la nueva clave.
7. Una vez que se verifique, borra o revoca tu clave de tráfico anterior para evitar un uso inadecuado.

## Limitaciones

Google AI Studio impone las siguientes limitaciones de administración de proyectos y claves:

- Puedes crear un máximo de 10 proyectos a la vez desde la página **Projects** de Google AI Studio.
- En las páginas **Claves de API** y **Proyectos**, se muestran un máximo de 100 claves y 50 proyectos.
- Solo se muestran las claves de API que no están restringidas o que están restringidas específicamente a la API de Generative Language (API de Gemini).

Para la administración avanzada de proyectos o para modificar claves con otras restricciones, usa la [página de credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-06 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-06 (UTC)"],[],[]]
