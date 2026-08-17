---
source_url: https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=pl
fetched_at: 2026-08-17T02:28:08.194676+00:00
title: "Rozpoznawanie film\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozpoznawanie filmów

Model Gemini Robotics ER 2 może śledzić postępy w realizacji zadań na podstawie ciągłych strumieni wideo dzięki 2 funkcjom:

- Wyszukiwanie momentów: identyfikuje dokładny znacznik czasu, w którym występuje kluczowe zdarzenie.
- Klasyfikacja postępów: przypisuje każdy film do jednego z 5 przedziałów ukończenia (0–20%, 20–40%, 40–60%, 60–80%, 80–100%).

## Wyszukiwanie momentów

Wyszukiwanie momentów identyfikuje dokładną klatkę wideo, w której występuje krytyczne zdarzenie, np. gdy kubek jest pełny lub gdy zawiązany jest węzeł. Roboty używają tej funkcji do weryfikowania powodzenia, sekwencji kroków i wywoływania korekt.

Poniższy przykładowy prompt prosi model o zidentyfikowanie momentu ukończenia danego zadania w filmie:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
At what timestamp (in seconds) does the task reach successful completion?
Return a JSON object: {"completion_time_seconds": <float>}.
If the task is not completed, return {"completion_time_seconds": null}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Poniżej przedstawiamy przykładowe klatki z filmu, w którym wyszukiwane są momenty. Model identyfikuje znacznik czasu ukończenia zadania:

![Przykładowe klatki filmu pokazujące moment znalezienia wyniku z nałożoną sygnaturą czasową](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-moment-finding.png?hl=pl)

## Klasyfikacja postępów

Klasyfikacja postępów przypisuje film do jednego z 5 przedziałów ukończenia: 0–20%, 20–40%, 40–60%, 60–80% lub 80–100%. Dzięki temu roboty mają świadomość sytuacji w czasie rzeczywistym, co pozwala im dostosowywać działania lub ponawiać nieudane kroki bez konieczności ponownego uruchamiania całego procesu.

Poniższy przykładowy prompt prosi model o sklasyfikowanie bieżącego poziomu postępu na podstawie filmu:

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="task_video.mp4")

prompt = """
Watch this video and classify the task progress level at the final frame.
Return a JSON object with the progress bracket:
{"progress_level": "0-20" | "20-40" | "40-60" | "60-80" | "80-100"}.
"""

interaction = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "video",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": prompt}
    ],
)

print(interaction.output_text)
```

Poniżej przedstawiamy przykładowe klatki z filmu, w którym klasyfikowane są postępy. Model przypisuje przedział postępu:

![Przykładowe klatki filmu pokazujące wynik klasyfikacji postępu z etykietą przedziału postępu](https://ai.google.dev/static/gemini-api/docs/images/robotics/video-progress-classification.png?hl=pl)

## Przykłady

Pełne przykłady, które można uruchomić, w tym śledzenie zadań wieloetapowych, znajdziesz w
[przewodniku Robotics](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## Co dalej?

- [Interfejs Live API dla robotyki](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=pl) – dwukierunkowe przesyłanie strumieniowe w czasie rzeczywistym.
- [Orkiestracja zadań](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=pl) – zadania długoterminowe z rozumowaniem przestrzennym.
- [Omówienie modelu Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=pl) – porównanie modeli i możliwości.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
