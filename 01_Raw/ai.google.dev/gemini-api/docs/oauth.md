---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=pl
fetched_at: 2026-07-06T05:08:56.170290+00:00
title: "Kr\u00f3tkie wprowadzenie do uwierzytelniania z protoko\u0142em OAuth \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Krótkie wprowadzenie do uwierzytelniania z protokołem OAuth

Najłatwiejszym sposobem uwierzytelniania w Gemini API jest skonfigurowanie klucza API
zgodnie z instrukcjami w [przewodniku dla początkujących](https://ai.google.dev/gemini-api/docs/get-started?hl=pl). Jeśli potrzebujesz bardziej rygorystycznych kontroli dostępu, możesz zamiast tego użyć OAuth. Ten przewodnik pomoże Ci skonfigurować uwierzytelnianie za pomocą OAuth.

Ten przewodnik zawiera uproszczoną metodę uwierzytelniania, która jest odpowiednia dla środowiska testowego. W przypadku środowiska produkcyjnego zapoznaj się
z informacjami
[o uwierzytelnianiu i autoryzacji](https://developers.google.com/workspace/guides/auth-overview?hl=pl)
przed
[wybraniem danych logowania](https://developers.google.com/workspace/guides/create-credentials?hl=pl#choose_the_access_credential_that_is_right_for_you)
odpowiednich dla Twojej aplikacji.

## Cele

- Skonfiguruj projekt w chmurze na potrzeby OAuth.
- Skonfiguruj domyślne dane logowania aplikacji.
- Zarządzaj danymi logowania w programie zamiast używać `gcloud auth`.

## Wymagania wstępne

Aby uruchomić ten samouczek, musisz mieć:

- [projekt Google Cloud,](https://developers.google.com/workspace/guides/create-project?hl=pl)
- [lokalną instalację gcloud CLI.](https://cloud.google.com/sdk/docs/install?hl=pl)

## Konfigurowanie projektu w chmurze

Aby wykonać zadania z tego samouczka, musisz najpierw skonfigurować projekt w chmurze.

### 1. Włącz API

Zanim zaczniesz korzystać z interfejsów API Google, musisz je włączyć w projekcie w chmurze Google.

- W konsoli Google Cloud włącz Google Generative Language API.

  [Włącz API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=pl)

### 2. Konfigurowanie ekranu zgody OAuth

Następnie skonfiguruj ekran zgody OAuth w projekcie i dodaj siebie jako użytkownika testowego. Jeśli ten krok został już wykonany w przypadku projektu w chmurze, przejdź do następnej sekcji.

1. W konsoli Google Cloud kliknij **Menu** > **Platforma uwierzytelniania Google** > **Przegląd**.

   [Otwórz platformę uwierzytelniania Google](https://console.developers.google.com/auth/overview?hl=pl)
2. Wypełnij formularz konfiguracji projektu i w sekcji **Odbiorcy** ustaw typ użytkownika na **Zewnętrzny**.
3. Wypełnij pozostałą część formularza, zaakceptuj warunki zasad dotyczących danych użytkownika, a następnie kliknij **Utwórz**.
4. Na razie możesz pominąć dodawanie zakresów i kliknąć **Zapisz i kontynuuj**. W przyszłości, gdy będziesz tworzyć aplikację do użytku poza organizacją Google Workspace, musisz dodać i zweryfikować zakresy autoryzacji wymagane przez aplikację.
5. Dodaj użytkowników testowych:

   1. Otwórz stronę
      [Odbiorcy](https://console.developers.google.com/auth/audience?hl=pl) na
      platformie uwierzytelniania Google.
   2. W sekcji **Użytkownicy testowi** kliknij **Dodaj użytkowników**.
   3. Wpisz swój adres e-mail i adresy e-mail innych autoryzowanych użytkowników testowych, a następnie kliknij **Zapisz**.

### 3. Autoryzowanie danych logowania aplikacji na komputer

Aby uwierzytelnić się jako użytkownik końcowy i uzyskać dostęp do danych użytkownika w aplikacji, musisz utworzyć co najmniej 1 identyfikator klienta OAuth 2.0. Identyfikator klienta wskazuje konkretną aplikację na serwerach OAuth Google. Jeśli Twoja aplikacja działa na kilku platformach, musisz utworzyć osobny identyfikator klienta dla każdej z nich.

1. W konsoli Google Cloud kliknij **Menu** > **Platforma uwierzytelniania Google** > **Klienci**.

   [Otwórz dane logowania](https://console.developers.google.com/auth/clients?hl=pl)
2. Kliknij **Utwórz klienta**.
3. Kliknij **Typ aplikacji** > **Aplikacja na komputer**.
4. W polu **Nazwa** wpisz nazwę danych logowania. Ta nazwa jest widoczna tylko w konsoli Google Cloud.
5. Kliknij **Utwórz**. Wyświetli się ekran Utworzono klienta OAuth z nowym identyfikatorem klienta i tajnym kluczem klienta.
6. Kliknij **OK**. Nowo utworzone dane logowania pojawią się w sekcji **Identyfikatory klientów OAuth 2.0**.
7. Kliknij przycisk pobierania, aby zapisać plik JSON. Zostanie on zapisany jako
   `client_secret_<identifier>.json`. Zmień jego nazwę na `client_secret.json`
   i przenieś go do katalogu roboczego.

## Konfigurowanie domyślnych danych logowania aplikacji

Aby przekonwertować plik `client_secret.json` na dane logowania, które można wykorzystać, przekaż jego lokalizację do argumentu `--client-id-file` polecenia `gcloud auth application-default login`.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

Uproszczona konfiguracja projektu w tym samouczku powoduje wyświetlenie okna **"Google nie
zweryfikowało tej aplikacji"**. To normalne. Kliknij **„Kontynuuj”**.

Spowoduje to umieszczenie wygenerowanego tokena w dobrze znanej lokalizacji, dzięki czemu będzie on dostępny dla `gcloud` lub bibliotek klienta.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Gdy skonfigurujesz domyślne uwierzytelnianie aplikacji (ADC), biblioteki klienta w większości języków nie będą potrzebować pomocy w ich znalezieniu.

### curl

Najszybszym sposobem na sprawdzenie, czy wszystko działa, jest użycie curl do uzyskania dostępu do REST API:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

W Pythonie biblioteki klienta powinny znaleźć je automatycznie:

```
pip install google-genai
```

Minimalny skrypt do testowania może wyglądać tak:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Dalsze kroki

Jeśli wszystko działa, możesz wypróbować
[wyszukiwanie semantyczne na danych tekstowych](https://ai.google.dev/docs/semantic_retriever?hl=pl).

## Samodzielne zarządzanie danymi logowania [Python]

W wielu przypadkach nie będziesz mieć dostępu do polecenia `gcloud`, aby utworzyć token dostępu na podstawie identyfikatora klienta (`client_secret.json`). Google udostępnia biblioteki w wielu językach, które umożliwiają zarządzanie tym procesem w aplikacji. W tej sekcji pokazujemy, jak to zrobić w Pythonie. Odpowiednie przykłady tej procedury w innych językach znajdziesz w
[dokumentacji Drive API](https://developers.google.com/drive/api/quickstart/python?hl=pl).

### 1. Zainstaluj niezbędne biblioteki

Zainstaluj bibliotekę klienta Google dla Pythona i bibliotekę klienta Gemini.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Napisz menedżera danych logowania

Aby zminimalizować liczbę kliknięć na ekranach autoryzacji, utwórz w katalogu roboczym plik o nazwie `load_creds.py`, który będzie buforować plik `token.json`, aby można go było później użyć ponownie lub odświeżyć, jeśli wygaśnie.

Zacznij od tego kodu, aby przekonwertować plik `client_secret.json` na token, którego można używać z `genai.configure`:

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

### 3. Napisz program

Teraz utwórz plik `script.py`:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Uruchom program

W katalogu roboczym uruchom przykład:

```
python script.py
```

Gdy uruchomisz skrypt po raz pierwszy, otworzy się okno przeglądarki z prośbą o autoryzację dostępu.

1. Jeśli nie jesteś zalogowany(-a) na konto Google, pojawi się prośba o zalogowanie się. Jeśli korzystasz z kilku kont, **pamiętaj, aby podczas konfigurowania projektu wybrać konto, które zostało ustawione jako „Konto testowe”**.
2. Informacje o autoryzacji są przechowywane w systemie plików, więc przy następnym uruchomieniu przykładowego kodu nie pojawi się prośba o autoryzację.

Udało Ci się skonfigurować uwierzytelnianie.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-01 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-01 UTC."],[],[]]
