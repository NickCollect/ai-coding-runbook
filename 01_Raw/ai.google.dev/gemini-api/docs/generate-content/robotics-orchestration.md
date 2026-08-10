---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=tr
fetched_at: 2026-08-10T03:27:15.361499+00:00
title: "G\u00f6rev d\u00fczenleme \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Görev düzenleme

Gemini Robotics ER modelleri, görevleri planlayabilir ve uzayla ilgili akıl yürütebilir. Bu sayede, bir hedefi tamamlamak için hangi işlemlerin yapılacağını ve hangi nesnelerin taşınacağını çıkarabilir. Bu sayfada, bir öğeyi kaseye yerleştirme görevini düzenlemek için özel bir robot API'si aracılığıyla [alma ve yerleştirme işleminin nasıl yapılacağına](#calling-custom-robot-api) dair bir örnek gösterilmektedir.

Çalıştırılabilir kodun tamamı için [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)'a (Robotik yemek kitabı) bakın.

## Özel bir robot API'si kullanma

Bu örnekte, özel bir robot API'si ile görev düzenleme gösterilmektedir. Bu kitapta, seçme ve yerleştirme işlemi için tasarlanmış bir sahte API tanıtılmaktadır. Görev, mavi bir bloğu alıp turuncu bir kaseye yerleştirmektir:

![Blok ve kase resmi](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=tr)

Bu örnekte aşağıdaki sahte robot API'si ve araç tanımları kullanılmaktadır:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

def move(x, y, high):
    print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
    print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_declaration = types.FunctionDeclaration(
    name="move",
    description="Moves the arm to the given coordinates.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "x": types.Schema(type=types.Type.INTEGER, description="X coordinate relative to the origin"),
            "y": types.Schema(type=types.Type.INTEGER, description="Y coordinate relative to the origin"),
            "high": types.Schema(type=types.Type.BOOLEAN, description="Set to True to lift the robot arm above the scene. Set to False to place the gripper on the surface."),
        },
        required=["x", "y", "high"],
    ),
)

set_gripper_state_declaration = types.FunctionDeclaration(
    name="setGripperState",
    description="Opens or closes the robot's gripper.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "opened": types.Schema(type=types.Type.BOOLEAN, description="True opens the gripper, False closes the gripper."),
        },
        required=["opened"],
    ),
)

robot_tools = types.Tool(function_declarations=[move_declaration, set_gripper_state_declaration])
```

Aşağıdaki örnekte, istem ve resim, araç tanımlarıyla birlikte modele gönderilir. Ardından, her model yanıtından sonra istenen işlev çağrılarını (`move`, `setGripperState`) yürüten, sonuçları modele geri döndüren ve model işlev çağırmayı durdurana veya adım sınırına ulaşılana kadar tekrarlayan bir aracı döngüsü çalıştırır.

### Python

```
with open("robot-api-example.png", "rb") as f:
    img_bytes = f.read()

prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

contents = [
    types.Content(role="user", parts=[
        types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
        types.Part(text=prompt),
    ])
]

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15  # Safety limit to prevent infinite loops
step_count = 0

# The Agentic Loop
while step_count < max_steps:
    step_count += 1

    response = client.models.generate_content(
        model="gemini-robotics-er-2-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=[robot_tools],
            thinking_config=types.ThinkingConfig(thinking_level="low"),
        ),
    )

    # Add model response to conversation history
    contents.append(response.candidates[0].content)

    # Check for function calls
    function_calls = [part for part in response.candidates[0].content.parts if part.function_call]

    if not function_calls:
        # Model is done calling functions
        print("Sequence complete.")
        print(f"Model Summary: {response.text}")
        break

    # Execute function calls and collect results
    function_response_parts = []
    for part in function_calls:
        fc = part.function_call
        if fc.name == "move":
            move(**fc.args)
        elif fc.name == "setGripperState":
            setGripperState(**fc.args)

        function_response_parts.append(
            types.Part.from_function_response(
                name=fc.name,
                response={"status": "success"},
            )
        )

    # Send function results back to model
    contents.append(types.Content(role="user", parts=function_response_parts))
```

Aşağıda, isteme ve sahte robot API'sine dayalı olarak modelin olası bir çıkışı gösterilmektedir. Çıkış, modelin birlikte sıraladığı robot işlevi çağrılarının çıkışını içerir.

```
--- Executing Orchestrated Plan ---
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: 160, 440, down at table level
Mock Robot: Closing gripper
Mock Robot: Moving to coordinates: 160, 440, high above table
Mock Robot: Moving to coordinates: -250, 60, high above table
Mock Robot: Moving to coordinates: -250, 60, down at table level
Mock Robot: Opening gripper
Mock Robot: Moving to coordinates: -250, 60, high above table
Sequence complete.
Model Summary: I have completed the task of picking up the blue block and placing it into the orange bowl.
```

## Sırada ne var?

- [Akışlı robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): İşlev çağrısıyla gerçek zamanlı akış (yalnızca Gemini Robotics ER 2).
- [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr): Yalnızca ER 2'de video üzerinden görev ilerlemesini takip edin.
- [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=tr): İşaretleme, izleme ve sınırlayıcı kutu örnekleri.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
