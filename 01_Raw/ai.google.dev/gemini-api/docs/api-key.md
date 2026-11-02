---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=pl
fetched_at: 2026-11-02T07:04:57.560023+00:00
title: "Korzystanie z kluczy interfejsu Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Korzystanie z kluczy interfejsu Gemini API

Aby korzystać z interfejsu Gemini API, musisz uwierzytelniać swoje żądania. Możesz uwierzytelniać się za pomocą standardowego klucza interfejsu API lub klucza autoryzacji.

[Tworzenie i wyświetlanie klucza interfejsu Gemini API](https://aistudio.google.com/apikey?hl=pl)

## Typy kluczy interfejsu API: standardowe i autoryzacyjne

Klucze interfejsu API zapewniają dostęp do interfejsu Gemini API, ale ich charakterystyka bezpieczeństwa jest różna. Aby zwiększyć bezpieczeństwo, interfejs Gemini API przechodzi ze standardowych kluczy interfejsu API na klucze autoryzacji:

- **Standardowe klucze interfejsu API:** powiąż żądania z projektem Google Cloud na potrzeby rozliczeń i limitów. Klucze standardowe nie identyfikują elementu wywołującego, co ogranicza szczegółowość uprawnień i kontroli dostępu, które mogą obsługiwać.
- **Klucze autoryzacji**: są powiązane bezpośrednio z kontem usługi Google Cloud. Gdy używasz klucza autoryzacji, Twoje żądania są przetwarzane przy użyciu tożsamości powiązanego konta usługi, co umożliwia szczegółową kontrolę dostępu. Klucze autoryzacji są domyślnie ograniczone do interfejsu Generative Language API (Gemini API) i zapewniają szybkie egzekwowanie zasad dotyczących wycieku kluczy, co pozwala na natychmiastowe zaprzestanie używania kluczy, które wyciekły, wykrytych przez nasze systemy.

Aby zapewnić bezpieczne korzystanie, interfejs Gemini API przejdzie ze standardowych kluczy na klucze autoryzacji:

- **Domyślne klucze uwierzytelniania:** od 28 maja 2026 r. wszystkie nowe klucze interfejsu API utworzone w Google AI Studio będą automatycznie tworzone jako klucze uwierzytelniania.
- **Odrzucanie kluczy bez ograniczeń:** interfejs Gemini API odrzuca żądania z **kluczy standardowych bez ograniczeń**. Standardowe klucze interfejsu API, które mają zastosowane wyraźne ograniczenia, nadal działają. To ograniczenie zapobiega nieautoryzowanemu użyciu kluczy, które mogą być udostępniane publicznie lub połączone z innymi usługami.

## Zarządzanie kluczami interfejsu API w Google AI Studio

Możesz zarządzać swoimi projektami i kluczami bezpośrednio w [Google AI Studio](https://aistudio.google.com/apikey?hl=pl).

### projekty Google Cloud,

Każdy klucz interfejsu Gemini API jest powiązany z [projektem Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=pl).
Projekty Google Cloud zarządzają płatnościami, współpracownikami i uprawnieniami. Google AI Studio udostępnia lekki interfejs umożliwiający dostęp do tych projektów.

- **Projekt domyślny:** jeśli jesteś nowym użytkownikiem, Google AI Studio automatycznie utworzy domyślny projekt w chmurze Google Cloud i klucz interfejsu API po zaakceptowaniu przez Ciebie Warunków korzystania z usługi. Możesz zmienić nazwę tego projektu, przechodząc do widoku **Projekty** w panelu.
- **Istniejące projekty:** jeśli masz już konto Google Cloud, AI Studio nie utworzy domyślnego projektu. Zamiast tego musisz zaimportować istniejące projekty.

### Importowanie projektów

Domyślnie Google AI Studio nie wyświetla wszystkich Twoich projektów Google Cloud. Musisz zaimportować projekty, których chcesz używać:

1. Otwórz [Google AI Studio](https://aistudio.google.com?hl=pl).
2. W panelu po lewej stronie otwórz **Panel** i wybierz **Projekty**.
3. Kliknij przycisk **Importuj projekty**.
4. Wyszukaj i wybierz projekt w chmurze Google Cloud, który chcesz zaimportować, a następnie kliknij **Importuj**.
5. Po zaimportowaniu otwórz stronę **Klucze interfejsów API** w panelu, aby utworzyć klucz w tym projekcie.

### Rozwiązywanie problemów z uprawnieniami do tworzenia kluczy

Jeśli przycisk **Utwórz klucz interfejsu API** jest niedostępny i wyświetla się komunikat *„Nie masz uprawnień do utworzenia klucza w tym projekcie”*, oznacza to, że nie masz wymaganych uprawnień.

Poproś administratora projektu w chmurze lub administratora organizacji Google Cloud o przypisanie Ci roli zawierającej te uprawnienia (np. edytującego projekt):

- `resourcemanager.projects.get`: umożliwia AI Studio weryfikację projektu.
- `apikeys.keys.create`: umożliwia generowanie kluczy.
- `serviceusage.services.enable`: sprawdza, czy interfejs Generative Language API jest włączony.
- `iam.serviceAccounts.create`: wymagana do utworzenia połączonego konta usługi.
- `iam.serviceAccountApiKeyBindings.create`: wiąże konto usługi z kluczem interfejsu API.

Jeśli nie możesz uzyskać dostępu administracyjnego, możesz utworzyć nowy projekt Google Cloud, który nie jest powiązany z organizacją, aby wygenerować klucze.

### Nieznane klucze na stronie Użycie

[Strona Wykorzystanie](https://aistudio.google.com/usage?hl=pl) w Google AI Studio grupuje żądania, których nie może dopasować do nazwanego klucza interfejsu API w projekcie, w sekcji **(nieznane klucze)**. Obejmuje to klucze usunięte ponad 30 dni temu, klucze bez wyświetlanej nazwy i żądania wysłane z innymi danymi logowania, takimi jak OAuth.

## Tworzenie kluczy w konsoli Google Cloud

Google AI Studio wyświetla tylko klucze, które nie są ograniczone lub są ograniczone do interfejsu Gemini API. Jeśli nie możesz używać AI Studio lub chcesz zarządzać wszystkimi kluczami interfejsu API w jednym miejscu, postępuj zgodnie z dokumentacją Cloud dotyczącą [tworzenia klucza interfejsu API](https://cloud.google.com/docs/authentication/api-keys?hl=pl#create). Utworzenie klucza interfejsu API Gemini wymaga powiązania go z [kontem usługi](https://cloud.google.com/iam/docs/service-account-overview?hl=pl).

## Konfiguruję środowisko

Gdy masz już klucz, skonfiguruj środowisko, aby bezpiecznie używać go w aplikacjach.

### Opcja 1. Użyj zmiennych środowiskowych (zalecane)

Ustaw zmienną środowiskową `GEMINI_API_KEY` lub `GOOGLE_API_KEY`. Biblioteki klienta Gemini API automatycznie wykrywają i używają tych zmiennych. Jeśli skonfigurowane są obie zasady, pierwszeństwo ma `GOOGLE_API_KEY`.

Wybierz system operacyjny, aby ustawić zmienną:

### Linux/macOS – Bash

Sprawdź, czy masz plik konfiguracji basha:

```
~/.bashrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.bashrc && open ~/.bashrc
```

Dodaj polecenie eksportu na końcu pliku:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a następnie zastosuj zmiany:

```
source ~/.bashrc
```

### macOS – Zsh

Sprawdź, czy masz plik konfiguracji zsh:

```
~/.zshrc
```

Jeśli nie, utwórz go i otwórz:

```
touch ~/.zshrc && open ~/.zshrc
```

Dodaj polecenie eksportu:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Zapisz plik, a następnie zastosuj zmiany:

```
source ~/.zshrc
```

### Windows

1. Na pasku wyszukiwania systemu Windows wyszukaj „Zmienne środowiskowe”.
2. W oknie dialogowym Właściwości systemu kliknij **Zmienne środowiskowe**.
3. W sekcji **Zmienne użytkownika** lub **Zmienne systemowe** kliknij **Nowa…**.
4. Ustaw nazwę zmiennej na `GEMINI_API_KEY`, a wartość na klucz interfejsu API.
5. Kliknij **OK**, aby zapisać zmiany. Otwórz nową sesję terminala, aby wczytać zmienną.

### Opcja 2. Podaj klucz interfejsu API bezpośrednio w kodzie

Klucz interfejsu API możesz przekazać bezpośrednio podczas inicjowania klienta. Zrób to tylko wtedy, gdy nie możesz użyć zmiennych środowiskowych.

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

## Bezpieczeństwo i zarządzanie obiektami tajnymi

Traktuj klucz interfejsu Gemini API jak hasło. Jeśli zostanie przejęty, inne osoby mogą wykorzystać limit projektu, spowodować nieoczekiwane opłaty i uzyskać dostęp do zasobów prywatnych.

### Krytyczne reguły zabezpieczeń

- **Zachowaj poufność kluczy:** nigdy nie zapisuj kluczy interfejsu API w systemach kontroli źródła, takich jak Git.
- **Nigdy nie ujawniaj kluczy po stronie klienta w środowisku produkcyjnym:** nie koduj kluczy interfejsu API na stałe bezpośrednio w aplikacjach internetowych ani mobilnych. Klucze skompilowane w kodzie po stronie klienta mogą zostać wyodrębnione przez użytkowników. Aby zabezpieczyć aplikacje po stronie klienta, uruchom serwer proxy backendu, który będzie wykonywać rzeczywiste wywołania interfejsu API.

### Sprawdzone metody zarządzania obiektami tajnymi

- **Zmienne środowiskowe:** odczytuj klucze ze zmiennych środowiskowych, a nie z plików konfiguracji.
- **Secret Manager:** w środowisku produkcyjnym przechowuj klucze w bezpiecznym magazynie obiektów tajnych, takim jak [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=pl).
- **Alerty rozliczeniowe:** skonfiguruj alerty rozliczeniowe w konsoli Google Cloud, aby otrzymywać powiadomienia o nagłym wzroście wykorzystania lub kosztów.

### Lista kontrolna dotycząca reagowania na wycieki

Jeśli podejrzewasz, że klucz interfejsu API został ujawniony:

1. **Wygeneruj nowy klucz:** utwórz klucz zastępczy w Google AI Studio lub konsoli Cloud.
2. **Zaktualizuj aplikację:** wdróż kod, używając nowego klucza.
3. **Wyłącz lub usuń klucz, który został przejęty:** po zweryfikowaniu nowego klucza wyłącz klucz, który wyciekł, w konsoli Cloud. Aby uniknąć przestojów w działaniu aplikacji, nie usuwaj starego klucza, dopóki nowy nie będzie w pełni aktywny.
4. **Sprawdź wykorzystanie:** sprawdź logi rozliczeniowe i wykorzystanie interfejsu API w konsoli Google Cloud, aby zidentyfikować nieautoryzowane działania.

## Ograniczanie i zabezpieczanie kluczy

Dodanie ograniczeń do kluczy interfejsu API minimalizuje potencjalne szkody w przypadku naruszenia bezpieczeństwa klucza.

### Stosowanie ograniczeń dotyczących źródła żądania

Ograniczenia dotyczące pochodzenia określają, które adresy IP, witryny lub aplikacje mogą używać Twojego klucza.

1. Otwórz [stronę Dane logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i kliknij nazwę klucza interfejsu API, który chcesz ograniczyć.
3. W sekcji **Ograniczenia aplikacji** wybierz **Adresy IP** (lub odpowiedni typ ograniczenia dla Twojego środowiska).
4. Określ dozwolone adresy lub zakresy adresów IP, a następnie kliknij **Zapisz**.

### Zabezpieczanie standardowych kluczy interfejsu API bez ograniczeń

Aby nadal korzystać z Gemini API, musisz zabezpieczyć wszystkie klucze bez ograniczeń.

#### Metoda A. Ogranicz klucz tylko do interfejsu Gemini API (AI Studio)

Jeśli używasz klucza tylko do Gemini API, zabezpiecz go bezpośrednio w AI Studio:

1. Na stronie **Klucze interfejsów API** w [Google AI Studio](https://aistudio.google.com/api-keys?hl=pl) znajdź klucze oznaczone etykietą **Bez ograniczeń**.
2. Najedź kursorem na etykietę i w oknie kliknij **Dodaj ograniczenia**.
3. Wybierz **Ogranicz tylko do Gemini API**.
4. Kliknij **Ogranicz klucz**, aby potwierdzić.

#### Metoda B. Ograniczanie klucza w przypadku innych usług (konsola Google Cloud)

Jeśli klucz jest udostępniany innym interfejsom API Google (niezalecane), ogranicz go w konsoli Cloud. **Uwaga: po zastosowaniu tych ograniczeń żądania do interfejsu Gemini API wysyłane przy użyciu tego klucza będą kończyć się niepowodzeniem.**

1. Otwórz [stronę danych logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).
2. Wybierz projekt i klucz interfejsu API.
3. W sekcji **Ograniczenia interfejsów API** użyj menu **Wybierz ograniczenia interfejsu API**, aby wybrać interfejsy API, do których ten klucz ma mieć dostęp. Nie wybieraj **Generative Language API**.
4. Kliknij **Zapisz**. Aby nadal korzystać z interfejsu Gemini API, utwórz w AI Studio osobny klucz z ograniczonym dostępem.

### Zablokowane nieaktywne klucze

Od 7 maja 2026 r. interfejs Gemini API będzie blokować klucze interfejsu API bez ograniczeń, które były nieaktywne przez dłuższy czas. Te klucze mają w AI Studio tag **Zablokowane**. Aby kontynuować, musisz wygenerować nowy klucz lub użyć istniejącego klucza z ograniczeniami.

## Migracja do klucza uwierzytelniania

Aby utworzyć nowy klucz interfejsu API do autoryzacji i zaktualizować aplikacje:

1. Otwórz [stronę kluczy interfejsów API w AI Studio](https://aistudio.google.com/api-keys?hl=pl).
2. Sprawdź kolumnę **Typ klucza**, aby znaleźć klucze oznaczone jako **Standardowy**.
3. Kliknij **Utwórz klucz interfejsu API**, aby wygenerować nowy klucz. Wszystkie nowe klucze utworzone w AI Studio są automatycznie tworzone jako klucze uwierzytelniania.
4. Skopiuj nowy klucz interfejsu API do autoryzacji.
5. Zaktualizuj kod aplikacji, zmienne środowiskowe i konfiguracje wdrożenia, aby używać nowego klucza interfejsu API do uwierzytelniania.
6. Przetestuj aplikację, aby sprawdzić, czy działa prawidłowo z nowym kluczem.
7. Po zweryfikowaniu usuń lub unieważnij stary klucz ruchu, aby zapobiec nadużyciom.

## Ograniczenia

Google AI Studio nakłada te ograniczenia dotyczące zarządzania projektami i kluczami:

- Na stronie **Projekty** w Google AI Studio możesz utworzyć maksymalnie 10 projektów jednocześnie.
- Na stronach **Klucze interfejsu API** i **Projekty** wyświetla się maksymalnie 100 kluczy i 50 projektów.
- Wyświetlane są tylko klucze interfejsu API, które nie mają ograniczeń lub są ograniczone do interfejsu Generative Language API (Gemini API).

Aby uzyskać dostęp do zaawansowanego zarządzania projektami lub zmodyfikować klucze z innymi ograniczeniami, użyj [strony danych logowania w konsoli Google Cloud](https://console.cloud.google.com/apis/credentials?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-27 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-27 UTC."],[],[]]
