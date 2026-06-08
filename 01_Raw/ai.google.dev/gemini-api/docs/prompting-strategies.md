---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=pl
fetched_at: 2026-06-08T05:31:42.207511+00:00
title: "Strategie projektowania prompt\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Strategie projektowania promptów

*Projektowanie promptów* to proces tworzenia promptów, czyli zapytań w języku naturalnym, które pozwalają uzyskać dokładne i wysokiej jakości odpowiedzi od modelu językowego.

Na tej stronie znajdziesz podstawowe koncepcje, strategie i sprawdzone metody, które pomogą Ci zacząć projektować prompty, aby w pełni wykorzystać możliwości modeli AI Gemini.

## Przewodniki po promptach dotyczące konkretnych tematów

Szukasz bardziej konkretnych strategii dotyczących promptów? Zapoznaj się z naszymi innymi przewodnikami po tworzeniu promptów dotyczącymi:

- [Promptowanie za pomocą plików multimedialnych](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide)
- Promptowanie w celu generowania obrazów za pomocą [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pl#imagen-prompt-guide) i [natywnego generowania obrazów w Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#prompt-guide)
- [Prompty do generowania filmów](https://ai.google.dev/gemini-api/docs/video?hl=pl#prompt-guide)

Więcej przykładowych promptów znajdziesz w [galerii promptów](https://ai.google.dev/gemini-api/prompts?hl=pl), która w interaktywny sposób prezentuje wiele koncepcji przedstawionych w tym przewodniku.

## jasne i konkretne instrukcje,

Skutecznym i wydajnym sposobem dostosowywania działania modelu jest podawanie mu jasnych i konkretnych instrukcji. Instrukcje mogą mieć formę pytania, zadań krok po kroku lub bardziej złożoną, np. mapowania doświadczeń i nastawienia użytkownika.

### Dane wejściowe

Dane wejściowe to wymagany tekst w prompcie, na który model ma udzielić odpowiedzi. Dane wejściowe mogą być pytaniem, na które model odpowiada (dane wejściowe w postaci pytania), zadaniem, które model wykonuje (dane wejściowe w postaci zadania), obiektem, na którym model działa (dane wejściowe w postaci obiektu), lub częściowymi danymi wejściowymi, które model uzupełnia lub kontynuuje (dane wejściowe w postaci uzupełnienia).

| **Typ danych wejściowych** | **Prompt** | **Wygenerowane dane wyjściowe** |
| --- | --- | --- |
| Pytanie | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Zadanie | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Jednostka | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Częściowe uzupełnianie danych

Generatywne modele językowe działają jak zaawansowane narzędzie do autouzupełniania. Gdy podasz część treści, model może dostarczyć resztę treści lub to, co uważa za jej kontynuację, w odpowiedzi. Jeśli podasz przykłady lub kontekst, model może je uwzględnić.

Poniższy przykład zawiera prompt z instrukcją i danymi wejściowymi dotyczącymi podmiotu:

|  |
| --- |
| **Prompt:**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Odpowiedź:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Model wykonał zadanie zgodnie z instrukcjami, ale zapisanie ich w języku naturalnym może być czasami trudne i pozostawia wiele miejsca na interpretację przez model.
Na przykład menu restauracji może zawierać wiele pozycji. Aby zmniejszyć rozmiar odpowiedzi JSON, prawdopodobnie warto pominąć elementy, które nie zostały zamówione. W tym przypadku możesz podać przykład i prefiks odpowiedzi, a model dokończy resztę:

|  |
| --- |
| **Prompt:**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Odpowiedź:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Zwróć uwagę, że „cheeseburger” został wykluczony z danych wyjściowych, ponieważ nie był częścią zamówienia.

Format prostych obiektów odpowiedzi JSON możesz określać za pomocą promptów, ale w przypadku bardziej złożonego schematu JSON odpowiedzi zalecamy używanie funkcji [danych wyjściowych w formie strukturalnej](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl) interfejsu Gemini API.

### Ograniczenia

Określ wszelkie ograniczenia dotyczące odczytywania prompta lub generowania odpowiedzi. Możesz powiedzieć modelowi, co ma robić, a czego nie. Na przykład w prompcie możesz określić ograniczenie dotyczące długości podsumowania:

|  |
| --- |
| **Prompt:**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Odpowiedź:**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Format odpowiedzi

Możesz przekazać instrukcje określające format odpowiedzi. Możesz na przykład poprosić o sformatowanie odpowiedzi jako tabeli, listy punktowanej, krótkiej prezentacji, słów kluczowych, zdania lub akapitu. Poniższa instrukcja systemowa nakazuje modelowi udzielać bardziej konwersacyjnych odpowiedzi:

|  |
| --- |
| **Instrukcja systemowa**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Prompt**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Odpowiedź:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Formatowanie odpowiedzi za pomocą strategii uzupełniania

[Strategia uzupełniania](#completion) może też pomóc w formatowaniu odpowiedzi.
W tym przykładzie promptu model ma utworzyć konspekt eseju:

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. ```  **Odpowiedź:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

Prompt nie określał formatu konspektu, więc model wybrał go za Ciebie. Aby model zwrócił konspekt w określonym formacie, możesz dodać tekst, który reprezentuje początek konspektu, i pozwolić modelowi go dokończyć na podstawie wzorca, który został przez Ciebie zainicjowany.

|  |
| --- |
| **Prompt:**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Odpowiedź:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Prompty typu zero-shot a prompty typu few-shot

W prompcie możesz podać przykłady, które pokażą modelowi, jak wygląda prawidłowa odpowiedź. Model próbuje identyfikować wzorce i relacje na podstawie przykładów i stosuje je podczas generowania odpowiedzi. Prompty zawierające kilka przykładów to prompty *few-shot*, a prompty bez przykładów to prompty *zero-shot*. Prompty z kilkoma przykładami są często używane do regulowania formatowania, sformułowań, zakresu lub ogólnego wzorca odpowiedzi modelu. Korzystaj z konkretnych i zróżnicowanych przykładów, aby ukierunkować model i uzyskać dokładniejsze wyniki.

Zalecamy, aby w promptach zawsze uwzględniać przykłady few-shot. Prompty bez przykładów few-shot są zwykle mniej skuteczne. Jeśli przykłady wystarczająco jasno pokazują, jakie zadanie ma wykonać model, możesz usunąć instrukcje z promptu.

Poniższy prompt bez przykładów prosi model o wybranie najlepszego wyjaśnienia.

|  |
| --- |
| **Prompt:**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Odpowiedź:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Jeśli Twój przypadek użycia wymaga, aby model generował zwięzłe odpowiedzi, możesz uwzględnić w prompcie przykłady, które preferują zwięzłe odpowiedzi.

Poniższy prompt zawiera 2 przykłady, które pokazują preferencje dotyczące krótszych wyjaśnień. W odpowiedzi widać, że przykłady pomogły modelowi wybrać krótsze wyjaśnienie (`Explanation2`) zamiast dłuższego (`Explanation1`), jak to miało miejsce wcześniej.

|  |
| --- |
| **Prompt:**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Odpowiedź:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Optymalna liczba przykładów

Modele takie jak Gemini często potrafią wykrywać wzorce na podstawie kilku przykładów, ale aby uzyskać najlepsze wyniki, może być konieczne eksperymentowanie z liczbą przykładów podawanych w prompcie. Jeśli jednak podasz zbyt wiele przykładów, model może zacząć [nadmiernie dopasowywać](https://developers.google.com/machine-learning/glossary?hl=pl#overfitting) odpowiedź do przykładów.

### Spójny format

Upewnij się, że struktura i formatowanie przykładów z kilkoma próbkami są takie same, aby uniknąć odpowiedzi w niepożądanych formatach. Jednym z głównych celów dodawania przykładów w promptach jest pokazanie modelowi formatu odpowiedzi. Dlatego ważne jest, aby we wszystkich przykładach zachować spójny format, zwracając szczególną uwagę na tagi XML, spacje, znaki nowego wiersza i separatory przykładów.

## Dodaj kontekst

W prompcie możesz uwzględnić instrukcje i informacje, których model potrzebuje do rozwiązania problemu, zamiast zakładać, że ma on wszystkie wymagane dane. Te informacje kontekstowe pomagają modelowi zrozumieć ograniczenia i szczegóły tego, o co go prosisz.

W tym przykładzie model jest proszony o podanie wskazówek dotyczących rozwiązywania problemów z routerem:

|  |
| --- |
| **Prompt:**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Odpowiedź:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

Odpowiedź wygląda jak ogólne informacje dotyczące rozwiązywania problemów, które nie są specyficzne dla routera ani stanu diod LED.

Aby dostosować odpowiedź do konkretnego routera, możesz dodać do prompta przewodnik rozwiązywania problemów z routerem jako kontekst, do którego model będzie się odwoływać podczas udzielania odpowiedzi.

|  |
| --- |
| **Prompt:**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Odpowiedź:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Dzielenie promptów na komponenty

W przypadku zastosowań wymagających złożonych promptów możesz pomóc modelowi w zarządzaniu tą złożonością, dzieląc zadania na prostsze komponenty.

1. **Podziel instrukcje:** zamiast umieszczać wiele instrukcji w jednym promcie, utwórz po jednym promcie dla każdej instrukcji. Na podstawie danych wejściowych użytkownika możesz wybrać prompt do przetworzenia.
2. **Łączenie promptów:** w przypadku złożonych zadań, które obejmują wiele kolejnych kroków, utwórz prompt dla każdego takiego etapu, a potem powiąż prompty w sekwencję. W tym sekwencyjnym łańcuchu promptów dane wyjściowe jednego promptu w sekwencji stają się danymi wejściowymi następnego promptu. Wynik ostatniego prompta w sekwencji
   jest wynikiem końcowym.
3. **Agregowanie odpowiedzi:** agregacja polega na wykonywaniu różnych zadań równoległych na różnych częściach danych i agregowaniu wyników w celu uzyskania ostatecznego wyniku. Możesz na przykład polecić modelowi wykonanie jednej operacji na pierwszej części danych, a innej operacji na pozostałych danych i zagregowanie wyników.

## Eksperymentowanie z parametrami modelu

Każde wywołanie wysłane do modelu zawiera wartości parametrów, które określają, jak model wygeneruje odpowiedź. Model może generować różne wyniki w zależności od wartości parametrów. Wypróbuj różne wartości parametrów, aby uzyskać najlepsze wyniki w tym zadaniu. W różnych modelach dostępne są różne parametry. Najczęstsze parametry to:

1. **Maksymalna liczba tokenów wyjściowych**:określa maksymalną liczbę tokenów, które mogą zostać wygenerowane w odpowiedzi. Token ma około 4 znaków. 100 tokenów to około 60–80 słów.
2. **Temperatura:** temperatura decyduje o stopniu losowości wyboru tokenów. Temperatura jest używana do próbkowania podczas generowania odpowiedzi, co ma miejsce, gdy stosowane są wartości `topP` i `topK`. Niższe temperatury są przydatne w przypadku promptów, na które oczekuje się bardziej deterministycznej lub mniej otwartej odpowiedzi, a wyższe mogą prowadzić do bardziej różnorodnych lub kreatywnych wyników. Temperatura o wartości 0 jest deterministyczna, co oznacza, że zawsze jest wybierana najbardziej prawdopodobna odpowiedź.
3. **`topK`:** Parametr `topK` zmienia sposób, w jaki model wybiera tokeny w celu wygenerowania odpowiedzi. Wartość `topK` 1 oznacza, że wybierany jest najbardziej prawdopodobny token spośród wszystkich tokenów w słowniku modelu (jest to też nazywane dekodowaniem zachłannym), natomiast wartość `topK` 3 oznacza, że następny token jest wybierany spośród 3 najbardziej prawdopodobnych (z użyciem temperatury). Na każdym etapie wyboru tokena próbkowane są tokeny `topK` o najwyższym prawdopodobieństwie. Tokeny są następnie filtrowane na podstawie parametru `topP`, a ostateczny wybór tokena dokonywany jest przy pomocy próbkowania z użyciem temperatury.
4. **`topP`:** Parametr `topP` zmienia sposób, w jaki model wybiera tokeny w celu wygenerowania odpowiedzi. Tokeny są wybierane od najbardziej do najmniej prawdopodobnych, aż suma ich prawdopodobieństw będzie równa wartości `topP`. Jeśli na przykład tokeny A, B i C mają prawdopodobieństwa 0,3, 0,2 i 0,1, a wartością `topP` jest 0,5, jako kolejny token model wybierze A lub B (z użyciem temperatury), a token C zostanie wykluczony. Domyślna wartość `topP` to 0,95.
5. **`stop_sequences`:** ustaw sekwencję zatrzymania, aby poinformować model, że ma przestać generować treści. Sekwencja zatrzymania może być dowolną sekwencją znaków. Staraj się unikać używania sekwencji znaków, które mogą pojawić się w wygenerowanych treściach.

## Strategie iteracji promptów

Projektowanie promptów może czasami wymagać kilku iteracji, zanim zaczniesz otrzymywać oczekiwane odpowiedzi. W tej sekcji znajdziesz wskazówki dotyczące tego, co możesz zrobić, aby ulepszyć swoje prompty:

1. **Używaj różnych sformułowań:** używanie w promptach różnych słów lub sformułowań często daje różne odpowiedzi modelu, mimo że wszystkie oznaczają to samo. Jeśli prompt nie daje oczekiwanych wyników, spróbuj go przeformułować.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Przejdź do analogicznego zadania:** jeśli model nie wykonuje instrukcji dotyczących zadania, spróbuj podać instrukcje dotyczące analogicznego zadania, które daje ten sam wynik.

   Ten prompt nakazuje modelowi skategoryzowanie książki przy użyciu wstępnie zdefiniowanych kategorii:

   |  |
   | --- |
   | **Prompt:**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Odpowiedź:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   Odpowiedź jest prawidłowa, ale model nie zmieścił się w zakresie opcji. Chcesz też, aby model odpowiadał tylko jedną z opcji, a nie pełnym zdaniem. W takim przypadku możesz przeformułować instrukcje jako pytanie wielokrotnego wyboru i poprosić model o wybranie opcji.

   |  |
   | --- |
   | **Prompt:**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Odpowiedź:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Zmień kolejność treści prompta:** kolejność treści w prompcie może czasami wpływać na odpowiedź. Spróbuj zmienić kolejność treści i sprawdź, jak wpłynie to na odpowiedź.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Odpowiedzi zastępcze

Odpowiedź zastępcza to odpowiedź zwracana przez model, gdy prompt lub odpowiedź aktywuje filtr bezpieczeństwa. Przykładowa odpowiedź rezerwowa to: „Nie mogę w tym pomóc, ponieważ jestem tylko modelem językowym”.

Jeśli model odpowie odpowiedzią zastępczą, spróbuj zwiększyć temperaturę.

## Grounding i wykonywanie kodu

Gemini może korzystać z narzędzi, aby unikać halucynacji w sytuacjach, w których mogłoby udzielić nieprawidłowych odpowiedzi.

[Powiązanie ze źródłem informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl) łączy model Gemini z treściami z internetu w czasie rzeczywistym i powinno być włączone, gdy model może potrzebować wiedzy o mało znanych lub aktualnych faktach.

[Narzędzie do wykonywania kodu](https://ai.google.dev/gemini-api/docs/code-execution?hl=pl) w Gemini umożliwia modelowi generowanie i uruchamianie kodu w Pythonie. Należy je włączać, gdy model musi wykonać jakiekolwiek działania arytmetyczne, zliczyć coś lub przeprowadzić obliczenia.

## Gemini 3

[Modele Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-3) zostały zaprojektowane pod kątem zaawansowanego rozumowania i postępowania zgodnie z instrukcjami.
Najlepiej reagują na prompty, które są bezpośrednie, dobrze skonstruowane i jasno określają zadanie oraz wszelkie ograniczenia. Aby uzyskać optymalne wyniki w przypadku Gemini 3, zalecamy stosowanie tych metod:

### Podstawowe zasady dotyczące promptów

- **Bądź precyzyjny i bezpośredni:** jasno i zwięźle określ swój cel. Unikaj niepotrzebnego lub zbyt perswazyjnego języka.
- **Używaj spójnej struktury:** stosuj wyraźne ograniczniki, aby oddzielać różne części promptu. Skuteczne są tagi w stylu XML (np. `<context>`, `<task>`) lub nagłówki Markdown. Wybierz jeden format i używaj go konsekwentnie w ramach jednego prompta.
- **Określ parametry:** wyjaśnij w sposób jednoznaczny wszelkie niejasne terminy lub parametry.
- **Kontrolowanie szczegółowości danych wyjściowych:** modele Gemini 3 domyślnie udzielają bezpośrednich i zwięzłych odpowiedzi. Jeśli potrzebujesz bardziej konwersacyjnej lub szczegółowej odpowiedzi, musisz wyraźnie poprosić o to w instrukcjach.
- **Spójna obsługa danych wejściowych multimodalnych:** podczas korzystania z tekstu, obrazów, dźwięku lub wideo traktuj je jako dane wejściowe tej samej klasy. W razie potrzeby upewnij się, że instrukcje wyraźnie odnoszą się do każdego rodzaju.
- **Traktuj priorytetowo najważniejsze instrukcje:** umieść najważniejsze ograniczenia behawioralne, definicje ról (persona) i wymagania dotyczące formatu wyjściowego w instrukcji systemowej lub na samym początku promptu użytkownika.
- **Struktura długich kontekstów:** jeśli podajesz duże ilości kontekstu (np. dokumenty, kod), najpierw podaj cały kontekst. Umieść konkretne instrukcje lub pytania na samym *końcu* prompta.
- **Kontekst kotwicy:** po dużym bloku danych użyj jasnego zwrotu przejściowego, aby połączyć kontekst z zapytaniem, np. „Na podstawie powyższych informacji…”.

### Strategie Gemini 3 Flash

- **Dokładność w bieżącym dniu:** dodaj do instrukcji systemowych tę klauzulę, aby pomóc modelowi zwrócić uwagę na to, że bieżący dzień przypada w 2026 r.:

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Dokładność granicy wiedzy:** dodaj do instrukcji systemowych ten punkt, aby model wiedział o granicy wiedzy:

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Skuteczność ugruntowania:** dodaj do instrukcji systemowych poniższą klauzulę (w razie potrzeby zmodyfikuj ją), aby zwiększyć zdolność modelu do ugruntowania odpowiedzi w podanym kontekście:

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Ulepszone wnioskowanie i planowanie

Modele z serii Gemini 2.5 i 3 automatycznie generują wewnętrzny tekst „myślenia”, aby poprawić wydajność rozumowania. Dlatego zwykle nie jest konieczne, aby model przedstawiał zarys, plan ani szczegółowe kroki rozumowania w samej odpowiedzi. W przypadku problemów wymagających intensywnego rozumowania proste prośby, takie jak „Zanim odpowiesz, dobrze się zastanów”, mogą poprawić wydajność, ale kosztem dodatkowych tokenów myślenia.

Więcej informacji znajdziesz w dokumentacji [Gemini thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=pl).

### Przykłady promptów strukturalnych

Używanie tagów lub Markdownu pomaga modelowi odróżniać instrukcje, kontekst i zadania.

**Przykład w formacie XML:**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Przykład formatowania Markdown:**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Przykładowy szablon łączący sprawdzone metody

Ten szablon zawiera podstawowe zasady tworzenia promptów dla Gemini 3. Zawsze
dostosowuj je do swoich potrzeb.

**Instrukcja systemowa:**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Prompt użytkownika:**

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Przepływy pracy agenta

W przypadku zaawansowanych przepływów pracy opartych na agentach często wymagane są szczegółowe instrukcje, które określają, jak model ma wnioskować, planować i wykonywać zadania. Gemini zapewnia wysoką ogólną wydajność, ale w przypadku złożonych agentów często trzeba skonfigurować kompromis między kosztem obliczeniowym (opóźnieniem i tokenami) a dokładnością zadania.

Podczas projektowania promptów dla agentów weź pod uwagę te aspekty zachowań, na które możesz wpływać:

### Rozumowanie i strategia

Konfiguracja sposobu myślenia i planowania modelu przed podjęciem działania.

- **Rozkład logiczny:** określa, jak dokładnie model musi analizować ograniczenia, wymagania wstępne i kolejność operacji.
- **Diagnostyka problemów:** określa głębokość analizy podczas identyfikowania przyczyn i wykorzystywania przez model rozumowania abdukcyjnego. Określa, czy model powinien zaakceptować najbardziej oczywistą odpowiedź, czy też zbadać złożone, mniej prawdopodobne wyjaśnienia.
- **Wykorzystanie informacji:** kompromis między analizowaniem wszystkich dostępnych zasad i dokumentów a priorytetowym traktowaniem skuteczności i szybkości.

### Wykonanie i niezawodność

Konfiguracja sposobu autonomicznego działania agenta i radzenia sobie z przeszkodami.

- **Możliwość dostosowania:** jak model reaguje na nowe dane. Określa, czy ma się ściśle trzymać początkowego planu, czy natychmiast zmienić strategię, gdy obserwacje są sprzeczne z założeniami.
- **Wytrwałość i odzyskiwanie:** stopień, w jakim model próbuje samodzielnie korygować błędy. Wysoka trwałość zwiększa odsetek sukcesów, ale wiąże się z ryzykiem wyższych kosztów tokenów lub pętli.
- **Ocena ryzyka:** logika oceny konsekwencji. Wyraźnie rozróżnia działania eksploracyjne o niskim ryzyku (odczyty) i zmiany stanu o wysokim ryzyku (zapisy).

### Interakcja i dane wyjściowe

Konfiguracja sposobu komunikacji agenta z użytkownikiem i formatowania wyników.

- **Niejednoznaczność i obsługa uprawnień:** określa, kiedy model może przyjmować założenia, a kiedy musi wstrzymać działanie, aby poprosić użytkownika o wyjaśnienie lub pozwolenie.
- **Szczegółowość:** określa ilość tekstu generowanego wraz z wywołaniami narzędzi. Określa, czy model wyjaśnia użytkownikowi swoje działania, czy pozostaje cichy podczas wykonywania.
- **Precyzja i kompletność:** wymagana dokładność danych wyjściowych. Określa, czy model musi rozwiązywać każdy przypadek brzegowy i podawać dokładne dane, czy też dopuszczalne są przybliżone szacunki.

### Szablon instrukcji systemowej

Poniższa instrukcja systemowa to przykład, który został oceniony przez badaczy pod kątem poprawy wyników w testach porównawczych dotyczących agentów, w których model musi przestrzegać złożonych zasad i wchodzić w interakcje z użytkownikiem. Zachęca agenta do działania jako osoba, która potrafi dobrze uzasadniać i planować, wymusza określone zachowania w wymiarach wymienionych powyżej i wymaga od modelu proaktywnego planowania przed podjęciem jakiegokolwiek działania.

Możesz dostosować ten szablon do ograniczeń konkretnego przypadku użycia.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Dalsze kroki

- Teraz, gdy masz już większą wiedzę o projektowaniu promptów, spróbuj napisać własne prompty w [Google AI Studio](http://aistudio.google.com?hl=pl).
- Więcej informacji o tworzeniu promptów multimodalnych znajdziesz w artykule [Promptowanie za pomocą plików multimedialnych](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide).
- Więcej informacji o promptach do generowania obrazów znajdziesz w przewodnikach po promptach do [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=pl#prompt-guide) i [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=pl#imagen-prompt-guide).
- Więcej informacji o tworzeniu promptów wideo znajdziesz w [przewodniku po tworzeniu promptów Veo](https://ai.google.dev/gemini-api/docs/video?hl=pl#prompt-guide).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
