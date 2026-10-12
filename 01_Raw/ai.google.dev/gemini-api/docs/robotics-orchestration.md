---
source_url: https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=tr
fetched_at: 2026-10-12T07:01:48.573785+00:00
title: "G\u00f6rev d\u00fczenleme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Görev düzenleme

Gemini Robotics ER modelleri, görevleri planlayabilir ve hangi işlemleri yapıp hangi nesneleri taşıyarak bir hedefi tamamlayacağını çıkararak alan hakkında akıl yürütebilir. Bu sayfada, bir öğeyi kaseye yerleştirme görevini düzenlemek için özel bir robot API'si aracılığıyla [alma ve yerleştirme işleminin nasıl yapılacağına](#calling-custom-robot-api) dair bir örnek gösterilmektedir. Bu örnekte standart Gemini ER 2 modeli kullanılmaktadır. Akış örneği için [Gemini ER 2 Akış Kılavuzu](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr)'na bakın.

Çalıştırılabilir kodun tamamı için [Robotics cookbook](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)'a (Robotik yemek kitabı) bakın.

## Özel bir robot API'si kullanma

Bu örnekte, özel bir robot API'si ile görev düzenleme gösterilmektedir. Bu kitapta, seçme ve yerleştirme işlemi için tasarlanmış bir sahte API tanıtılmaktadır. Görev, mavi bir bloğu alıp turuncu bir kaseye yerleştirmektir:

![Blok ve kase resmi](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=tr)

Bu örnekte aşağıdaki sahte robot API'si kullanılmaktadır:

### Python

```
def move(x, y, high):
  print(f"Mock Robot: Moving to coordinates: {x}, {y}, {'high above table' if high else 'down at table level'}")

def setGripperState(opened):
  print(f"Mock Robot: {'Opening gripper' if opened else 'Closing gripper'}")

robot_origin_y = 300
robot_origin_x = 500

move_function = {
    "type": "function",
    "name": "move",
    "description": "Moves the arm to the given coordinates.",
    "parameters": {
        "type": "object",
        "properties": {
            "x": {"type": "integer", "description": "X coordinate relative to the origin"},
            "y": {"type": "integer", "description": "Y coordinate relative to the origin"},
            "high": {"type": "boolean", "description": "Set to True to lift the robot arm above the scene for avoiding obstacles. Set to False to place the gripper on the surface."}
        },
        "required": ["x", "y", "high"]
    }
}

set_gripper_state_function = {
    "type": "function",
    "name": "setGripperState",
    "description": "Opens or closes the robot's gripper.",
    "parameters": {
        "type": "object",
        "properties": {
            "opened": {"type": "boolean", "description": "True opens the gripper, False closes the gripper."}
        },
        "required": ["opened"]
    }
}
```

Aşağıdaki örnekte, istem ve resim, araç tanımlarıyla birlikte modele gönderilir. Ardından, bir aracı döngüsü çalıştırır: Her model yanıtından sonra, istenen işlev çağrılarını (`move`, `setGripperState`) yürütür, sonuçları `previous_interaction_id` kullanarak modele geri döndürür ve model işlev çağırmayı durdurana veya adım sınırına ulaşılana kadar tekrarlar.

### Python

```
prompt = (
    "You are a robotic arm with six degrees-of-freedom. "
    f"The origin point for calculating the moves is at normalized point y={robot_origin_y}, x={robot_origin_x}. "
    "Use this as the new (0,0) for calculating moves, allowing x and y to be negative.\n\n"
    "Find the blue block and the orange bowl. Calculate their coordinates relative to the origin.\n"
    "Perform a pick and place operation where you pick up the blue block and place it into the orange bowl. "
    "Call the appropriate sequence of functions to complete this operation."
)

# 1. Initial Interaction
interaction = client.interactions.create(
    model=MODEL_ID,
    input=[{"type": "user_input", "content": [
        {"type": "image", "data": img_b64, "mime_type": "image/png"},
        {"type": "text", "text": prompt}
    ]}],
    tools=[move_function, set_gripper_state_function],
    generation_config={"thinking_level": "low"}
)

print("\n--- Executing Orchestrated Plan ---")

max_steps = 15 # Safety limit to prevent infinite loops
step_count = 0

# 2. The Agentic Loop
while step_count < max_steps:
    step_count += 1

    # Check if the model wants to call any functions
    tool_calls = [step for step in interaction.steps if step.type == "function_call"]

    if not tool_calls:
        # If no tools were called, the model is finished with the sequence
        print("Sequence complete.")
        if interaction.output_text:
            print(f"Model Summary: {interaction.output_text}")
        break

    function_results = []

    for step in tool_calls:
        function_name = step.name
        arguments = step.arguments

        # Execute the mock function
        if function_name == "move":
            move(**arguments)
        elif function_name == "setGripperState":
            setGripperState(**arguments)
        else:
            print(f"Unknown function: {function_name}")

        # 3. Create a result object to tell the model the function succeeded
        function_results.append({
            "type": "function_result",
            "name": step.name,
            "call_id": step.id,
            "result": [{"type": "text", "text": '{"status": "success"}'}]
        })

    # 4. Send the results back to the model, passing previous_interaction_id
    # so it remembers the conversation history and generates the NEXT step
    interaction = client.interactions.create(
        model=MODEL_ID,
        previous_interaction_id=interaction.id,
        tools=[move_function, set_gripper_state_function],
        input=function_results
    )
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
- [Video anlama](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=tr): Video görevindeki ilerlemeyi takip edin (yalnızca ER 2).
- [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=tr): İşaretleme, izleme ve sınırlayıcı kutu örnekleri.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-01 UTC."],[],[]]
