---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=es-419
fetched_at: 2026-08-17T02:25:35.152183+00:00
title: "C\u00f3mo usar claves de API de Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Cómo usar claves de API de Gemini

Para usar la API de Gemini, debes autenticar tus solicitudes. Puedes autenticarte con una clave de API estándar o de autorización.

[Crea o visualiza una clave de API de Gemini](https://aistudio.google.com/apikey?hl=es-419)

## Tipos de claves de API: estándar versus autorización

Las claves de API proporcionan acceso a la API de Gemini, pero sus características de seguridad difieren. La API de Gemini está haciendo la transición de claves de API estándar a claves de autorización para mejorar la seguridad:

- **Claves de API estándar**: Asocian solicitudes con un proyecto de Google Cloud para
  fines de facturación y cuota. Las claves estándar no identifican a un llamador, lo que limita la granularidad de los permisos y el control de acceso que pueden admitir.
- **Claves de autorización (auth)**: Se vinculan directamente a una cuenta de servicio de Google Cloud. Cuando usas una clave de autorización, tus solicitudes se procesan con la identidad de esa cuenta de servicio vinculada, lo que permite un control de acceso detallado. De forma predeterminada, las claves de autorización están restringidas a la API de Generative Language (API de Gemini) y proporcionan una aplicación rápida de claves filtradas que detiene rápidamente el uso de claves filtradas detectadas por nuestros sistemas.

Para garantizar un uso seguro, la API de Gemini pasará de claves estándar a claves de autorización:

- **Claves de autorización predeterminadas**: Todas las claves de API nuevas creadas en Google AI Studio
  se crean automáticamente como claves de autorización.
- **Claves no restringidas rechazadas**: La API de Gemini rechaza las solicitudes
  de **claves estándar no restringidas**. Las claves de API estándar que tienen restricciones explícitas aplicadas siguen funcionando. Esta restricción evita el uso no autorizado de claves que podrían compartirse públicamente o vincularse a otros servicios.
- **En septiembre de 2026**: La API de Gemini rechazará las solicitudes de **claves
  estándar**. Debes [migrar a las claves de autorización](#migrate-to-auth-key)
  antes de esta fecha para evitar interrupciones en el servicio. Asegúrate de migrar a las claves de autorización antes de septiembre de 2026.

## Administra claves de API en Google AI Studio

Puedes administrar tus proyectos y claves directamente en [Google AI Studio](https://aistudio.google.com/apikey?hl=es-419).

### Proyectos de Google Cloud

Cada clave de API de Gemini está asociada con un [proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=es-419).
Los proyectos de Google Cloud administran la facturación, los colaboradores y los permisos. Google AI Studio proporciona una interfaz ligera para acceder a estos proyectos.

- **Proyecto predeterminado**: Si eres un usuario nuevo, Google AI Studio crea automáticamente
  un proyecto de Google Cloud y una clave de API predeterminados después de que aceptas las
  Condiciones del Servicio. Para cambiar el nombre de este proyecto, navega a la vista **Proyectos** en tu panel.
- **Proyectos existentes**: Si ya tienes una cuenta de Google Cloud, AI
  Studio no crea un proyecto predeterminado. En su lugar, debes importar tus proyectos existentes.

### Importa proyectos

De forma predeterminada, Google AI Studio no muestra todos tus proyectos de Google Cloud. Debes importar los proyectos que deseas usar:

1. Ve a [Google AI Studio](https://aistudio.google.com?hl=es-419).
2. Abre el **Panel** desde el panel izquierdo y selecciona **Proyectos**.
3. Haz clic en el botón **Importar proyectos**.
4. Busca y selecciona el proyecto de Google Cloud que deseas importar y, luego, haz clic en **Importar**.
5. Una vez importado, navega a la página **Claves de API** en el panel para crear una clave en ese proyecto.

### Soluciona problemas de permisos de creación de claves

Si el botón **Crear clave de API** no está disponible y muestra el mensaje:
*"No tienes permiso para crear una clave en este proyecto"*, significa que no tienes los
permisos de IAM necesarios.

Pídele al administrador de tu proyecto o de tu organización de Google Cloud que te otorgue un rol que contenga los siguientes permisos (como Editor de proyectos):

- `resourcemanager.projects.get`: Permite que AI Studio verifique el proyecto.
- `apikeys.keys.create`: Permite la generación de claves.
- `serviceusage.services.enable`: Garantiza que la API de Generative Language esté habilitada.
- `iam.serviceAccounts.create`: Es necesario para crear la cuenta de servicio vinculada.
- `iam.serviceAccountApiKeyBindings.create`: Vincula la cuenta de servicio a la clave de API.

Si no puedes obtener acceso administrativo, puedes crear un proyecto nuevo de Google Cloud que no esté asociado con una organización para generar tus claves.

## Configura tu entorno

Una vez que tengas una clave, configura tu entorno para usarla de forma segura en tus aplicaciones.

### Opción 1: Usa variables de entorno (recomendada)

Configura la variable de entorno `GEMINI_API_KEY` o `GOOGLE_API_KEY`. Las bibliotecas cliente de la API de Gemini detectan y usan automáticamente estas variables. Si se configuran ambas, `GOOGLE_API_KEY` tiene prioridad.

Selecciona tu sistema operativo para configurar la variable:

### Linux/macOS - Bash

Verifica si tienes un archivo de configuración de bash:

```
~/.bashrc
```

De no ser así, crea uno y ábrelo:

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

### macOS - Zsh

Verifica si tienes un archivo de configuración de zsh:

```
~/.zshrc
```

De no ser así, crea uno y ábrelo:

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
3. En **Variables de usuario** o **Variables del sistema**, haz clic en **Nueva...**.
4. Establece el nombre de la variable en `GEMINI_API_KEY` y el valor en tu clave de API.
5. Haz clic en **Aceptar** para guardar los cambios. Abre una nueva sesión de la terminal para cargar la variable.

### Opción 2: Proporciona la clave de API de forma explícita en el código

Puedes pasar la clave de API de forma explícita cuando inicializas el cliente. Solo haz esto si no puedes usar variables de entorno.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
        Model: "gemini-3.6-flash",
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
            .model("gemini-3.6-flash")
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
  -X POST \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Administración de seguridad y secretos

Trata tu clave de API de Gemini como una contraseña. Si se ve comprometida, otras personas pueden consumir la cuota de tu proyecto, generar cargos de facturación inesperados y acceder a recursos privados.

### Reglas de seguridad críticas

- **Mantén la confidencialidad de las claves**: Nunca registres claves de API en sistemas de control de código fuente
  como Git.
- **Nunca expongas claves del cliente en producción**: No codifiques de forma rígida claves de API
  directamente en apps para dispositivos móviles o web. Los usuarios pueden extraer las claves compiladas en el código del cliente. Para proteger las apps del cliente, ejecuta un servidor proxy de backend para realizar las llamadas a la API reales.

### Prácticas recomendadas para la administración de secretos

- **Variables de entorno**: Lee las claves de las variables de entorno en lugar de los archivos de
  configuración.
- **Secret Manager**: Para la producción, almacena tus claves en un almacén de secretos seguro
  como [Secret Manager de Google Cloud](https://cloud.google.com/secret-manager?hl=es-419).
- **Alertas de facturación**: Configura alertas de facturación en la consola de Google Cloud para que te
  notifiquen si el uso o los costos aumentan.

### Lista de tareas de respuesta a filtraciones

Si sospechas que se filtró tu clave de API, haz lo siguiente:

1. **Genera una clave nueva**: Crea una clave de reemplazo en Google AI Studio o en la
   consola de Cloud.
2. **Actualiza tu aplicación**: Implementa tu código con la clave nueva.
3. **Inhabilita o borra la clave comprometida**: Inhabilita la clave filtrada en la
   consola de Cloud una vez que se verifique la clave nueva. No borres la clave anterior hasta que la clave nueva esté completamente activa para evitar el tiempo de inactividad de la aplicación.
4. **Audita el uso**: Consulta los registros de facturación y el uso de la API en la consola de Google Cloud
   para identificar actividades no autorizadas.

## Restringe y protege tus claves

Agregar restricciones a tus claves de API minimiza el daño potencial si una clave se ve comprometida.

### Aplica restricciones de origen de la solicitud

Las restricciones de origen limitan qué direcciones IP, sitios web o aplicaciones pueden usar tu clave.

1. Ve a la [página Credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona tu proyecto y haz clic en el nombre de la clave de API que deseas restringir.
3. En **Restricciones de aplicaciones**, selecciona **Direcciones IP** (o el
   tipo de restricción adecuado para tu entorno).
4. Especifica las direcciones IP o los rangos permitidos y, luego, haz clic en **Guardar**.

### Protege las claves de API estándar no restringidas

Para seguir usando la API de Gemini, debes proteger las claves no restringidas.

#### Método A: Restringe la clave solo a la API de Gemini (AI Studio)

Si solo usas la clave para la API de Gemini, protégela directamente en AI Studio:

1. En la página **Claves de API** de [Google AI Studio](https://aistudio.google.com/api-keys?hl=es-419), busca las claves marcadas con la etiqueta
   **No restringida**.
2. Pasa el cursor sobre la etiqueta y haz clic en **Agregar restricciones** en el diálogo.
3. Selecciona **Restringir solo a la API de Gemini**.
4. Haz clic en **Restringir clave** para confirmar.

#### Método B: Restringe la clave para otros servicios (consola de Google Cloud)

Si la clave se comparte con otras APIs de Google (no recomendado), restringe en la consola de Cloud. **Nota: Las solicitudes de la API de Gemini que usen esta clave fallarán después de que se apliquen estas restricciones.**

1. Visita la [página Credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).
2. Selecciona el proyecto y la clave de API.
3. En **Restricciones de API**, usa el menú desplegable **Seleccionar restricciones de API** para
   seleccionar las APIs a las que deseas que acceda esta clave. No selecciones la **API de Generative Language**.
4. Haz clic en **Guardar**. Crea una clave independiente y restringida en AI Studio para seguir usando la API de Gemini.

### Claves inactivas bloqueadas

A partir del 7 de mayo de 2026, la API de Gemini bloqueará las claves de API no restringidas que hayan estado inactivas durante un período prolongado. Estas claves muestran una etiqueta **Bloqueada** en AI Studio. Debes generar una clave nueva o usar una clave restringida existente para continuar.

## Migra a una clave de autorización

Sigue estos pasos para crear una clave de API de autorización nueva y actualizar tus aplicaciones:

1. Ve a la página [Claves de API de AI Studio](https://aistudio.google.com/api-keys?hl=es-419).
2. Consulta la columna **Tipo de clave** para identificar las claves que aparecen como **Estándar**.
3. Haz clic en **Crear clave de API** para generar una clave nueva. Todas las claves nuevas creadas en AI Studio se crean automáticamente como claves de autorización.
4. Copia la nueva clave de API de autorización.
5. Actualiza el código de la aplicación, las variables de entorno y cualquier configuración de implementación para usar la nueva clave de API de Auth.
6. Prueba tu aplicación para confirmar que funciona correctamente con la clave nueva.
7. Una vez verificada, borra o revoca tu clave de tráfico anterior para evitar el uso inadecuado.

## Limitaciones

Google AI Studio impone las siguientes limitaciones de administración de proyectos y claves:

- Puedes crear un máximo de 10 proyectos a la vez desde la página **Proyectos** de Google AI Studio.
- Las páginas **Claves de API** y **Proyectos** muestran un máximo de 100 claves y 50 proyectos.
- Solo se muestran las claves de API que no están restringidas o que están restringidas específicamente a la API de Generative Language (API de Gemini).

Para la administración avanzada de proyectos o para modificar claves con otras restricciones, usa
la [página de credenciales de la consola de Google Cloud](https://console.cloud.google.com/apis/credentials?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
