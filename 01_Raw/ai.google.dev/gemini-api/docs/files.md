---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=pl
fetched_at: 2026-08-31T06:35:13.027631+00:00
title: "Interfejs API plik\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Interfejs API plików

Model Gemini może jednocześnie przetwarzać różne typy danych wejściowych, w tym tekst, obrazy i dźwięk.

Z tego przewodnika dowiesz się, jak korzystać z plików multimedialnych za pomocą interfejsu Files API. Podstawowe operacje są takie same w przypadku plików audio, obrazów, filmów, dokumentów i innych obsługiwanych typów plików.

Wskazówki dotyczące tworzenia promptów do plików znajdziesz w sekcji [Przewodnik po tworzeniu promptów do plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide).

## Prześlij plik

Aby przesłać plik multimedialny, możesz użyć interfejsu Files API. Zawsze używaj interfejsu Files API, gdy łączny rozmiar żądania (w tym plików, promptu tekstowego, instrukcji systemowych itp.) przekracza 100 MB. W przypadku plików PDF limit wynosi 50 MB.

Poniższy kod przesyła plik, a następnie używa go w wywołaniu funkcji `interactions.create`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.7-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File file = client.files.upload(
    new java.io.File("path/to/sample.txt"),
    UploadFileConfig.builder().mimeType("text/plain").build()
);

System.out.println("Uploaded file URI: " + file.uri().orElse(""));
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

interaction, err := client.Interactions.Create(ctx, "gemini-3.7-flash", &genai.InteractionRequest{
    Input: []interface{}{
        genai.NewPartFromFile(*file),
        genai.NewPartFromText("Describe this audio clip"),
    },
}, nil)

if err != nil {
    log.Fatal(err)
}

// Print the model's text response
for _, step := range interaction.Steps {
    if step.Type == "model_output" {
        for _, part := range step.Content {
            if part.Type == "text" {
                fmt.Println(part.Text)
            }
        }
    }
}
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.7-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Pobieranie metadanych pliku

Możesz sprawdzić, czy interfejs API zapisał przesłany plik, i pobrać jego metadane, wywołując funkcję `files.get`.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File file = client.files.upload(
    new java.io.File("path/to/sample.txt"),
    UploadFileConfig.builder().mimeType("text/plain").build()
);

System.out.println("Uploaded file URI: " + file.uri().orElse(""));
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
echo file_uri=$file_uri
```

## Wyświetlanie listy przesłanych plików

Poniższy kod pobiera listę wszystkich przesłanych plików:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File file = client.files.upload(
    new java.io.File("path/to/sample.txt"),
    UploadFileConfig.builder().mimeType("text/plain").build()
);

System.out.println("Uploaded file URI: " + file.uri().orElse(""));
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Usuwanie przesłanych plików

Pliki są automatycznie usuwane po 48 godzinach. Możesz też ręcznie usunąć przesłany plik:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;

Client client = new Client();

File file = client.files.upload(
    new java.io.File("path/to/sample.txt"),
    UploadFileConfig.builder().mimeType("text/plain").build()
);

System.out.println("Uploaded file URI: " + file.uri().orElse(""));
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## informacje o korzystaniu z usługi,

Interfejs Files API umożliwia przesyłanie plików multimedialnych i korzystanie z nich. Interfejs Files API umożliwia przechowywanie do 20 GB plików na projekt, przy czym maksymalny rozmiar pojedynczego pliku to 2 GB. Pliki są przechowywane przez 48 godzin.

W tym czasie możesz używać interfejsu API do pobierania metadanych plików. Nie możesz jednak pobierać plików przesłanych przez użytkowników. Pliki wygenerowane przez modele, takie jak filmy, możesz pobrać za pomocą metody `files.download`. Interfejs Files API jest dostępny bezpłatnie we wszystkich regionach, w których dostępny jest interfejs Gemini API.

## Strategie dotyczące promptów w plikach

W tej sekcji znajdziesz wskazówki i sprawdzone metody dotyczące używania plików multimedialnych z promptami w interfejsie Gemini API.

Możliwość używania w promptach różnych typów danych zapewnia większą elastyczność w zakresie zadań, które możesz wykonywać za pomocą interfejsu Gemini API. Możesz na przykład wysłać modelowi zdjęcie pysznego posiłku i poprosić go o napisanie krótkiego bloga na jego temat.

|  |  |
| --- | --- |
| **Prompt** | **Odpowiedź** |
| Napisz krótki, angażujący post na bloga na podstawie tego zdjęcia. Powinien zawierać opis posiłku na zdjęciu i opowiadać o mojej przygodzie z przygotowywaniem posiłków.   Pliki cookie | Przygotowywanie posiłków z wyprzedzeniem to świetny sposób na oszczędzanie czasu i pieniędzy, a także na zdrowsze odżywianie. Ten posiłek to świetny przykład zdrowego i smacznego dania, które można przygotować z wyprzedzeniem.  Posiłek składa się z brązowego ryżu, pieczonych warzyw i kurczaka teriyaki. Brązowy ryż to zdrowy i złożony węglowodan, który zapewni Ci energię na dłużej. Pieczone warzywa to świetny sposób na dostarczenie organizmowi codziennej dawki witamin i minerałów, a kurczak teriyaki to pyszna i bogata w białko opcja.  To danie jest też proste w przygotowaniu. Wystarczy ugotować brązowy ryż, upiec warzywa i przygotować kurczaka teriyaki. Gdy wszystko będzie gotowe, podziel danie na porcje i umieść je w pojemnikach, a następnie przechowuj w lodówce. W zajęte poranki możesz po prostu wziąć pojemnik i wyjść z domu.  Jeśli szukasz zdrowego i pysznego posiłku, który można przygotować wcześniej, to danie będzie świetnym wyborem. Jest pełna składników odżywczych i smaku, a do tego zaspokaja głód i daje uczucie sytości.  Życzymy zdrowego i smacznego przygotowywania posiłków! |

Jeśli masz problem z uzyskaniem oczekiwanych wyników z promptów, które wykorzystują pliki multimedialne, możesz zastosować kilka strategii, które pomogą Ci osiągnąć zamierzony efekt. W kolejnych sekcjach znajdziesz podejścia do projektowania i wskazówki dotyczące rozwiązywania problemów, które pomogą Ci ulepszyć prompty korzystające z danych wejściowych w różnych formatach.

Aby ulepszyć prompty multimodalne, postępuj zgodnie z tymi sprawdzonymi metodami:

- ### [Podstawy projektowania promptów](#specific-instructions)

  - **Podawaj konkretne instrukcje:** twórz jasne i zwięzłe instrukcje, które pozostawiają jak najmniej miejsca na błędną interpretację.
  - **Dodaj do prompta kilka przykładów few-shot:** użyj realistycznych przykładów few-shot, aby zilustrować, co chcesz osiągnąć.
  - **Podziel zadanie na mniejsze części:** podziel złożone zadania na łatwe do wykonania podcele, prowadząc model przez cały proces.
  - **Określ format wyjściowy:** w prompcie poproś o wygenerowanie danych wyjściowych w wybranym formacie, np. Markdown, JSON, HTML itp.
  - **W przypadku promptów z jednym obrazem umieszczaj go na pierwszym miejscu:** Gemini może przetwarzać dane wejściowe w postaci obrazów i tekstu w dowolnej kolejności, ale w przypadku promptów zawierających jeden obraz może działać lepiej, jeśli ten obraz (lub film) zostanie umieszczony przed promptem tekstowym. W przypadku promptów, które wymagają, aby obrazy były ściśle powiązane z tekstem, użyj kolejności, która jest najbardziej naturalna.
- ### [Rozwiązywanie problemów z promptem multimodalnym](#troubleshooting)

  - **Jeśli model nie pobiera informacji z odpowiedniej części obrazu:** podaj wskazówki dotyczące aspektów obrazu, z których prompt ma pobierać informacje.
  - **Jeśli dane wyjściowe modelu są zbyt ogólne (niedostosowane do danych wejściowych obrazu/filmu):**  na początku prompta poproś model o opisanie obrazów lub filmu przed podaniem instrukcji zadania albo poproś model o odniesienie się do tego, co znajduje się na obrazie.
  - **Aby sprawdzić, która część zawiodła:** poproś model o opisanie obrazu lub wyjaśnienie jego rozumowania, aby ocenić wstępne zrozumienie modelu.
  - **Jeśli prompt spowoduje wygenerowanie halucynacji:** spróbuj zmniejszyć ustawienie temperatury lub poproś model o krótsze opisy, aby zmniejszyć prawdopodobieństwo ekstrapolacji dodatkowych szczegółów.
  - **Dostrajanie parametrów próbkowania:** eksperymentuj z różnymi ustawieniami temperatury i wyborami Top-K, aby dostosować kreatywność modelu.

### Podawaj szczegółowe instrukcje

Prompty są najbardziej skuteczne, gdy są jasne i szczegółowe. Jeśli masz na myśli konkretny wynik, lepiej uwzględnić to wymaganie w prompcie, aby mieć pewność, że uzyskasz oczekiwany rezultat.

W przypadku tego zdjęcia tablicy na lotnisku poproszenie modelu o „opisanie tego obrazu” może wygenerować ogólny opis. Jeśli chcesz, aby model przeanalizował czas i miasto na obrazie, możesz uwzględnić to żądanie bezpośrednio w prompcie.

| Prompt | Odpowiedź modelu |
| --- | --- |
| Opisz ten obraz. | Obraz przedstawia tablicę przylotów i odlotów na lotnisku. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Rozkład podróży Przeanalizuj czas i miasto z tablicy lotniska widocznej na tym obrazie i utwórz z nich listę. | - 10:50 Moskwa - 11:05 Edynburg - 11:05 Londyn - 11:10 Bukareszt - 11:30 Kijów - 11:35 Dublin - 11:45 East Midlands - 12:15 Sofia - 12:30 Londyn - 12:30 Newcastle - 12:40 St Petersburg - 12:40 Londyn - 12:45 Manchester |

### Dodaj kilka przykładów

Model Gemini może akceptować wiele danych wejściowych, których może używać jako przykładów, aby zrozumieć, jakich danych wyjściowych oczekujesz. Dodanie tych przykładów może pomóc modelowi w identyfikowaniu wzorców i stosowaniu relacji między podanymi obrazami a odpowiedziami do nowego przykładu. Jest to tzw. uczenie „few-shot”.

W poniższym przykładzie początkowy wynik jest zapisany w formie zdania i zawiera też nazwę kraju (Brazylia). Załóżmy, że chcesz uzyskać dane wyjściowe w innym formacie lub stylu i potrzebujesz tylko nazwy miasta, a nie kraju. Dodanie do promptu przykładów few-shot może nakierować model na udzielenie odpowiedzi w sposób, w jaki chcesz.

| **Prompt** | **Odpowiedź modelu** |
| --- | --- |
| Rozkład podróży Określ miasto, w którym znajduje się punkt orientacyjny. | Jest to statua Chrystusa Zbawiciela w Rio de Janeiro w Brazylii. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Określ miasto wraz z punktem orientacyjnym. Koloseum | miasto: Rzym, punkt orientacyjny: Koloseum. |
| Zakazane Miasto | miasto: Pekin, punkt orientacyjny: Zakazane Miasto |
| zakazane-miasto | miasto: Rio de Janeiro, punkt orientacyjny: Statua Chrystusa Zbawiciela |

### Szczegółowe instrukcje

W przypadku złożonych zadań, takich jak te, które wymagają zarówno zrozumienia wizualnego, jak i rozumowania, warto podzielić zadanie na mniejsze, prostsze etapy. Możesz też bezpośrednio poprosić model, aby „myślał krok po kroku”.

| Prompt | Odpowiedź modelu |
| --- | --- |
| Kiedy skończy mi się papier toaletowy? | Wkrótce zostaną Ci tylko 3 rolki. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| 1. Najpierw policz, ile rolek papieru toaletowego znajduje się na tym zdjęciu. 2. Następnie określ, ile papieru toaletowego zużywa przeciętna osoba w ciągu dnia. 3. Oblicz, na jak długo wystarczą te rolki papieru toaletowego. | 1. Na tym zdjęciu są 3 rolki papieru toaletowego. 2. Przeciętna osoba zużywa około 20 arkuszy papieru toaletowego dziennie. 3. Jeśli każda rolka zawiera 200 arkuszy, wystarczy na około 10 dni. Dlatego 3 rolki wystarczą na około miesiąc. |

Zadania matematyczne i inne zadania tekstowe to świetne przykłady, w przypadku których warto poprosić model o rozwiązanie krok po kroku.

| **Prompt** | **Odpowiedź** |
| --- | --- |
| Jaki jest czwarty wyraz w ciągu? | -135 |

Odpowiedź modelu jest nieprawidłowa. Aby to poprawić, możesz poprosić model o przeanalizowanie problemu przed udzieleniem odpowiedzi na prompt.

| **Prompt** | **Odpowiedź** |
| --- | --- |
| Najpierw przeanalizuj formułę na obrazie.  Następnie na podstawie wzoru odpowiedz na pytanie „Jaki jest czwarty wyraz ciągu?”. | *Kliknij, aby rozwinąć wynik* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Podstaw n = 4 do wzoru: $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. Nie znamy wartości b(3), więc podstawiamy n = 3 do wzoru: $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. Nie znamy wartości b(2), więc wstawiamy n = 2 do wzoru: $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. Wiemy, że wartość b(1) wynosi 15, więc podstawiamy ją do wzoru: $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. Znamy już wartość b(2), więc możemy ją podstawić do wzoru na b(3): $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Teraz, gdy znamy wartość b(3), podstawmy ją do wzoru na b(4): $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Czwarty wyraz ciągu to zatem -405. |

Odpowiedź modelu jest prawidłowa. Aby ją jeszcze bardziej usprawnić, możesz poprosić model o przemyślenie krok po kroku.

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Jaki jest czwarty wyraz w ciągu? Myśl krok po kroku. | Pierwszy wyraz to 15.  Drugi wyraz to b(1) \* (-3) = 15 \* (-3) = -45.  Trzeci wyraz to b(2) \* (-3) = -45 \* (-3) = 135.  Czwarty wyraz to b(3) \* (-3) = 135 \* (-3) = -405. |

### Określanie formatu wyjściowego

Częstym problemem jest konieczność generowania danych wyjściowych modelu w określonym formacie (np. Markdown, JSON, HTML), zwłaszcza jeśli dane wyjściowe modelu mają być wykorzystywane w dalszych zadaniach. Możesz spróbować uzyskać dane wyjściowe w tym formacie, instruując model w prompcie. Oto 2 przykłady:

| Prompt | Odpowiedź modelu |
| --- | --- |
| Przekształć tabelę na tym obrazie w format Markdown | ```none | Przedmiot | Stan | Czas | Data rozpoczęcia | Termin | | ------- | ------ | ---- | ---------- | ------ | | Matematyka | Gotowe | 1,5 godz. | 29.11.2023 | 1.12.2023 | | Geografia | Gotowe | 30 min | 2.12.2023 | 4.12.2023 | | Fizyka | W trakcie | 2 godz. | 3.12.2023 | 5.12.2023 | | Biologia | Nierozpoczęte | 6 godz. | 2.11.2016 | 6.12.2023 | ``` |

| **Prompt** | **Odpowiedź modelu** |
| --- | --- |
| Podaj listę wszystkich tych atrybutów:  składniki, rodzaj kuchni, czy danie jest wegetariańskie, w formacie JSON. | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### W przypadku promptów z pojedynczym obrazem umieść obraz na pierwszym miejscu.

Gemini może interpretować obraz i tekst w dowolnej kolejności w prompcie, ale umieszczenie jednego obrazu przed promptem tekstowym może przynieść lepsze wyniki.
W poniższych przykładach obraz jest zawsze podany przed tekstem w każdym promcie.

### Rozwiązywanie problemów z promptem multimodalnym

Jeśli nie otrzymujesz pomocnej odpowiedzi, może być konieczne rozwiązanie problemu z promptem. Oto kilka strategii, które możesz wypróbować.

#### Jeśli model nie pobiera informacji z odpowiedniej części obrazu

Aby uzyskać bardziej szczegółową odpowiedź, możesz wskazać, z których aspektów obrazu ma czerpać informacje prompt, aby na ich podstawie udzielić odpowiedzi.

| Prompt | Odpowiedź modelu |
| --- | --- |
| Na ile dni wystarczą te pieluszki dla dziecka? | Pieluchy wystarczą na 198 dni. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Na jak długo wystarczą mi te pieluszki?  Na podstawie wagi podanej na opakowaniu określ wiek dziecka, a następnie podaj łączną liczbę pieluszek w opakowaniu.  Podziel łączną liczbę pieluch przez liczbę pieluch zużywanych przez dziecko dziennie. | Pudełko zawiera 198 pieluszek. Na opakowaniu jest napisane, że pieluszki są przeznaczone dla dziecka o wadze 10–17 kg.  Średnie dziecko w tym przedziale wagowym ma prawdopodobnie od 1 do 2 lat.  2-letnie dziecko zużywa zwykle 6 pieluszek dziennie, więc wystarczą one na około 33 dni (198/6). |

#### Jeśli dane wyjściowe modelu są zbyt ogólne i niedostosowane do obrazu wejściowego.

Aby pomóc modelowi dostosować odpowiedź do obrazów, poproś go o ich opisanie przed wykonaniem zadania związanego z rozumowaniem.

| Prompt | Odpowiedź modelu |
| --- | --- |
| Co łączy te obrazy? | Wszystkie 4 obrazy to przykłady fotografii krajobrazowej. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Najpierw szczegółowo opisz, co znajduje się na każdym obrazie. Co łączy te obrazy? | Pierwszy obraz przedstawia osobę pakującą walizkę. Drugi obraz przedstawia pusty korytarz w centrum handlowym. Trzeci obraz przedstawia rolkę papieru toaletowego. Czwarty obraz przedstawia ciemne i sztormowe morze.  Wspólną cechą tych obrazów jest to, że wszystkie są przykładami przestrzeni liminalnych. Przestrzenie liminalne to miejsca lub sytuacje, które znajdują się pomiędzy dwoma innymi miejscami lub sytuacjami. Często charakteryzują się poczuciem niepewności lub niejednoznaczności.  Pierwszy obraz przedstawia osobę, która jest w domu i w podróży. Drugi obraz przedstawia korytarz między dwoma sklepami. Trzeci obraz przedstawia papier toaletowy, który może symbolizować łazienkę. Łazienka to przestrzeń przejściowa między strefą prywatną a publiczną. To miejsce, w którym przygotowujemy się do wejścia do świata zewnętrznego lub wyjścia z niego.  Czwarty obraz przedstawia morze w stanie między spokojnym a sztormowym.  Przestrzenie liminalne mogą być zarówno ekscytujące, jak i niepokojące. Mogą być miejscem nowego początku lub zakończenia. Mogą być miejscem refleksji lub miejscem działania. |

Możesz też wyraźnie poprosić model o odniesienie się do tego, co znajduje się na obrazie.

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Co łączy te obrazy? Odwołuj się do tego, co znajduje się na obrazach. | Wszystkie obrazy są związane z podróżami. Pierwsze zdjęcie przedstawia osobę pakującą walizkę, drugie – pusty korytarz w centrum handlowym, trzecie – stos papieru toaletowego, a czwarte – ciemne i burzliwe morze.  Wszystkie te obrazy są związane z podróżami, ponieważ przedstawiają rzeczy, których ludzie potrzebują lub używają podczas podróży. Pierwsze zdjęcie przedstawia osobę pakującą walizkę, co robią ludzie, gdy wybierają się w podróż. Drugie zdjęcie przedstawia pusty korytarz w centrum handlowym, czyli miejscu, do którego ludzie często chodzą, aby kupić rzeczy na wyjazdy. Trzeci obraz przedstawia stos papieru toaletowego, którego ludzie często używają w podróży. Czwarty obraz przedstawia ciemne i sztormowe morze, które często można spotkać podczas podróży. |

Te same wskazówki dotyczą wyników kreatywnych z obrazów. W tym przykładzie z królikiem wyraźne poproszenie modelu o uwzględnienie aspektów obrazu może poprawić wynik.

| Prompt | Odpowiedź modelu |
| --- | --- |
| Czy możesz napisać wiersz o tym obrazie? | Mały króliczku, tak miękki i brązowy,  skaczący po polu w górę i w dół.  Uszy masz długie, ogon krótki,  Jesteś najsłodszym stworzeniem ze wszystkich.  Skubiesz trawę, tak zieloną i słodką,  I odskakujesz, gdy mnie widzisz.  Ale zawsze będę Twoim przyjacielem,  Króliczku, aż do samego końca. |

| **Zaktualizowany prompt** | **Ulepszona odpowiedź** |
| --- | --- |
| Napisz opisowy i dramatyczny wiersz o tym obrazie, podając lokalizację. | Mały króliczek na zielonej łące,  Uszy takie długie, takie bystre.  Co widzisz tam,  W oddali, gdzie wpatrujesz się?  Czy jest niebieskie jak ocean,  Błyszczące w słońcu?  A może szum fal,  Rytm, który uwielbiasz?  Króliczku, powiedz mi,  Co tak bardzo przyciąga Twoją uwagę?  Czy to słona bryza,  Czy krzyk mew sprawia Ci przyjemność?  Może to ogrom wszystkiego,  Świat tak wielki i mały.  Miejsce, gdzie marzenia mogą się spełniać,  A przygody – rodzić.  Mały króliczku, co Ci się śni,  Gdy siedzisz na trawie, taki spokojny.  Czy chcesz odkrywać głębiny,  Czy wolisz zostać na lądzie, gdzie możesz skakać?  Cokolwiek to będzie, mały króliczku,  niech ta iskra ciekawości płonie jasno.  Bo w Twoich marzeniach i aspiracjach  tkwi świat czekający na Twoje stworzenie. |

#### Rozwiązywanie problemów z nieudaną częścią prompta

Trudno stwierdzić, czy prompt nie zadziałał, ponieważ model nie **zrozumiał obrazu**, czy też zrozumiał obraz, ale nie wykonał prawidłowych **kroków rozumowania**.
Aby odróżnić te powody, poproś model o opisanie, co znajduje się na obrazie.

Jeśli na przykład model zaproponuje przekąskę, która wydaje się zaskakująca w połączeniu z herbatą (np. popcorn), możesz najpierw sprawdzić, czy model prawidłowo rozpoznał, że na obrazie jest herbata.

| Prompt | Prompt do rozwiązywania problemów |
| --- | --- |
| Jaką przekąskę mogę przygotować w 1 minutę, która będzie do tego pasować? | Opisz, co jest na tym obrazie. |

Inną strategią jest poproszenie modelu o wyjaśnienie jego rozumowania. Może to pomóc w określeniu, która część rozumowania zawiodła, jeśli w ogóle.

| Prompt | Prompt do rozwiązywania problemów |
| --- | --- |
| Jaką przekąskę mogę przygotować w 1 minutę, która będzie do tego pasować? | Jaką przekąskę mogę przygotować w 1 minutę, która będzie do tego pasować? W jaki sposób? |

## Co dalej?

- Spróbuj napisać własne prompty multimodalne, korzystając z [Google AI Studio](http://aistudio.google.com?hl=pl).
- Informacje o korzystaniu z interfejsu Gemini Files API do przesyłania plików multimedialnych i dołączania ich do promptów znajdziesz w przewodnikach dotyczących [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=pl), [dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl) i [przetwarzania dokumentów](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl).
- Więcej wskazówek dotyczących projektowania promptów, np. dostrajania parametrów próbkowania, znajdziesz na stronie [Strategie dotyczące promptów](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-08-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-08-30 UTC."],[],[]]
