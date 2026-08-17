---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=ar
fetched_at: 2026-08-17T02:22:23.343522+00:00
title: "\u062a\u0646\u0638\u064a\u0645 \u0627\u0644\u0645\u0647\u0627\u0645 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تنظيم المهام

يمكن لنماذج Gemini Robotics ER التخطيط للمهام والاستدلال المنطقي بشأن المساحة، ما يتيح لها تحديد الإجراءات التي يجب اتخاذها والأشياء التي يجب نقلها لتحقيق هدف معيّن. تعرض هذه الصفحة مثالاً على [تنفيذ عملية التقاط ووضع](#calling-custom-robot-api) من خلال واجهة برمجة تطبيقات مخصّصة للروبوتات لتنظيم مهمة وضع عنصر في وعاء.

للاطّلاع على الرمز الكامل القابل للتنفيذ، راجِع
[كتاب وصفات الروبوتات](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb).

## استخدام واجهة برمجة تطبيقات مخصّصة للروبوت

يوضّح هذا المثال تنسيق المهام باستخدام واجهة برمجة تطبيقات مخصّصة للروبوت. وتتضمّن واجهة برمجة تطبيقات وهمية مصمَّمة لتنفيذ عملية الالتقاط والوضع. المهمة هي التقاط مكعّب أزرق ووضعه في وعاء برتقالي:

![صورة للكتلة والوعاء](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png?hl=ar)

يستخدم هذا المثال تعريفات واجهة برمجة التطبيقات والأدوات الوهمية التالية الخاصة بالروبوت:

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

يرسل المثال التالي الطلب والصورة إلى النموذج مع تعريفات الأدوات. بعد ذلك، يتم تشغيل حلقة وكيل: بعد كل ردّ من النموذج، يتم تنفيذ أي طلبات لاستدعاء الدوال (`move`، `setGripperState`)، ويتم إرجاع النتائج إلى النموذج، وتتكرر العملية إلى أن يتوقف النموذج عن استدعاء الدوال أو يتم بلوغ الحد الأقصى لعدد الخطوات.

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

يوضّح ما يلي ناتجًا محتملاً للنموذج استنادًا إلى الطلب وواجهة برمجة التطبيقات الوهمية الخاصة بالروبوت. يتضمّن الإخراج نتائج استدعاءات دالة الروبوت التي رتّبها النموذج معًا.

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

## الخطوات التالية

- [الروبوتات مع البث](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=ar): البث في الوقت الفعلي مع ميزة استدعاء الدوال (إصدار Gemini Robotics ER 2 فقط)
- [فهم الفيديو](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=ar): تتبُّع مستوى تقدّم المهمة من الفيديو (الإصدار 2 من ER فقط)
- [الاستدلال المكاني](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=ar): أمثلة على التأشير والتتبُّع ومربّع الإحاطة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
