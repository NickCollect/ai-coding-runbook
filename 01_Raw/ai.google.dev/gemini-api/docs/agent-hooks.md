---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=ar
fetched_at: 2026-10-05T06:50:19.422896+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Hooks

تتيح لك الخطّافات تشغيل نصوص برمجية مخصّصة أو طلبات HTTP خارجية قبل أن ينفّذ الوكيل الرمز البرمجي أو يعدّل الملفات داخل البيئة التجريبية المعزولة عن بُعد أو بعدها مباشرةً. استخدِم الخطافات لتوسيع حلقة الوكيل باستخدام ضوابط الحماية وسير العمل في الخلفية، مثل:

- **فرض ضوابط الأمان والوصول** قبل تنفيذ أوامر shell عالية الخطورة أو عمليات قراءة الملفات المحظورة
- **أتمتة عمليات تحويل مسار البيانات** بعد أن ينشئ أحد العملاء ملفات أو يعدّلها مباشرةً
- **بث بيانات قياس تدقيق المؤسسة عن بُعد** إلى أنظمة المراقبة الخارجية بعد تنفيذ الأداة

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
            },
        ],
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
    },
});
console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

String gateScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "cmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\n"
    + "if \"rm -rf\" in cmd:\n"
    + "    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\n"
    + "else:\n"
    + "    print(json.dumps({\"decision\": \"allow\"}))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/gate.py")
            .content(gateScript)
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run `rm -rf /tmp/forbidden` using code_execution."))
    .tools(List.of(CodeExecution.builder().build()))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "security-gate": {
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    gateScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/gate.py"),
                Content: genai.Ptr(gateScript),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run `rm -rf /tmp/forbidden` using code_execution."),
            Tools:       []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})},
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## أحداث مراحل النشاط المتوافقة

تتيح خطافات الأحداث حدثَين داخل وضع الحماية:

| الحدث | وقت تنشيطه | وظيفتها |
| --- | --- | --- |
| `pre_tool_execution` | قبل تشغيل أداة مباشرةً | يمكنك الموافقة على الأداة (`allow`) أو حظرها (`deny`) قبل تنفيذها. عند الحظر، يطّلع النموذج على سبب الرفض ويتكيّف معه. |
| `post_tool_execution` | مباشرةً بعد انتهاء أداة | تنفيذ مهام المتابعة، مثل تنسيق الرمز أو إجراء اختبارات الوحدات أو تسجيل بيانات القياس عن بُعد لا يمكن حظر الإجراءات المكتملة أو التراجع عنها. |

### `pre_tool_execution`

يتم تنشيط هذا المشغّل قبل تنفيذ إحدى الأدوات مباشرةً. يقرأ النص البرمجي تفاصيل طلب الأداة من `stdin` ويعرض قرار JSON (`allow` أو `deny`) في `stdout`.

**حمولة الإدخال (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**ردّ الإخراج (`stdout`):**

للموافقة على طلب استخدام الأداة، اتّبِع الخطوات التالية:

```
{
  "decision": "allow"
}
```

لحظر طلب استخدام الأداة وإرسال ملاحظات إلى النموذج:

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

عندما يرفض خطاف أمرًا، يتم تخطّي استدعاء الأداة على الفور. يظهر للوكيل نتيجة خطأ تتضمّن سبب الرفض مباشرةً في دوره الحالي. يمكن للنموذج بعد ذلك تصحيح نفسه من خلال اختيار أمر بديل أو شرح سبب الحظر للمستخدم.

إذا كان البرنامج النصي يعرض JSON غير معروف أو نصًا عاديًا أو أي شيء آخر غير `{"decision": "deny"}`، سيتعامل وقت التشغيل مع الردّ على أنّه موافقة (`allow`).

### `post_tool_execution`

يتم تشغيله بعد اكتمال أداة مباشرةً. يقرأ النص البرمجي تفاصيل التنفيذ وحالة أي خطأ من `stdin`.

**حمولة الإدخال (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

إذا عرض أمر shell أخطاء في الخطأ العادي (`stderr`) أو تعذّرت عملية نظام ملفات، يتم تضمين حقل `"error"` يحتوي على نص الخطأ في الحمولة. عندما ينجح الأمر بدون أخطاء، يتم حذف الحقل `"error"` بالكامل.

**ردّ الإخراج (`stdout`):**

```
{}
```

بما أنّ عمليات الربط بعد الأداة يتم تنفيذها بشكل صارم للمهام التي تتم في الخلفية، مثل تنسيق الرموز أو التسجيل، يتجاهل وقت التشغيل أي قيم قرار يتم إرجاعها في `stdout`.

## اكتشاف الإعدادات

يكتشف وقت التشغيل تلقائيًا تعريفات الدوال البرمجية من `.agents/hooks.json` أو `/.agents/hooks.json` داخل بيئة وضع الحماية. يمكنك توفير `hooks.json` إلى جانب النصوص البرمجية المخصّصة باستخدام أي [مصدر بيئة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#mount_from_a_source) متوافق:

- **تثبيت المستودع**: مستودع Git يحتوي على `.agents/hooks.json` بالإضافة إلى `AGENTS.md`.
- **Cloud Storage (`gcs`)**: حزمة GCS تحتوي على `hooks.json` تم نسخها إلى البيئة.
- **المصادر المضمّنة**: سلسلة JSON غير مُعالَجة ومحتوى النص البرمجي يتم تمريرهما في `environment.sources` عند استدعاء `client.interactions.create`.

### `hooks.json` مخطط

يجمع ملف `hooks.json` تعريفات الأحداث (`pre_tool_execution` أو `post_tool_execution`) ضمن أسماء مخصّصة. يمكنك تفعيل كل مجموعة أو إيقافها بشكل مستقل:

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### بنية المطابقة وقواعدها

تحدّد كل مجموعة قواعد في `hooks.json` وقت وكيفية تشغيل المعالجات باستخدام السمتَين `matcher` و`hooks`:

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `enabled` | `boolean` | اختيارية: اضبط القيمة على `false` لإيقاف المجموعة (`true` تلقائيًا). |
| `matcher` | `string` | مطابقة أنماط التعبيرات العادية لأسماء الأدوات المستهدَفة داخل الحاوية |
| `hooks` | `array` | قائمة مرتّبة بتعريفات المعالجات (`command` أو `http`). يتم تشغيل المعالجات بالتسلسل حسب ترتيب التعريف. |

#### طريقة عمل تقييم التعبيرات العادية

عندما يستدعي الوكيل أداة داخل وضع الحماية، يقيّم وقت التشغيل اسم حاوية الأداة مقارنةً بنمط `matcher` باستخدام التعبيرات العادية RE2 القياسية. إذا كانت العبارة العادية تطابق اسم الأداة، سيتم تنفيذ جميع المعالِجات في مصفوفة `hooks` بالترتيب. إذا تطابقت عدة مجموعات قواعد مع الأداة نفسها، سيتم تشغيل جميع مصفوفات المعالجات المتطابقة.

يمكنك استهداف أي اسم أداة حاوية مضمّنة: تطبيق الرموز البرمجية (`code_execution`) أو عمليات نظام الملفات (`view_file` و`write_to_file` و`replace_file_content` و`list_dir` و`delete_file`).

#### عبارات المطابقة الشائعة

- `"code_execution"`: تطابق السلسلة التام لأوامر shell وعمليات تنفيذ النصوص البرمجية
- ‫`"write_to_file"`: مطابقة تامة لإنشاء ملفات نظام الملفات وعمليات الكتابة على القرص
- `"view_file|write_to_file"`: يتيح الفصل باستخدام علامة الأنابيب مطابقة أسماء أدوات محدّدة متعددة في قاعدة واحدة.
- ‫`".*_file"`: تعبير عادي يتضمّن حرف بدل يطابق أي أداة تنتهي بـ `_file` (مثل `view_file` أو `write_to_file` أو `delete_file`). يشمل ذلك جزءًا فقط من مجموعة أدوات نظام الملفات، ولا تنتهي `replace_file_content` و`list_dir` بـ `_file`، لذا يجب تسميتهما بشكل صريح عند الحاجة إليهما. تتطلّب التعبيرات العادية القياسية RE2 استخدام `.*`، بينما تكون صيغ shell globs البسيطة مثل `*_file` غير صالحة كصيغة تعبير عادي ولن تتم مطابقتها.
- ‫`".*"` أو `"*"` أو `""`: نمط شامل يعترض كل طلب أداة داخل الحاوية.

## أنواع المعالجات

### خطافات الأوامر

تنفِّذ خطافات الأوامر أمرًا أو نصًا برمجيًا في Shell داخل البيئة التجريبية. يتلقّى النص البرمجي ملف JSON الخاص بالحدث على `stdin` ويعرض ملف JSON الخاص بالقرار على `stdout`.

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `type` | `string` | يجب أن تكون `"command"`. |
| `command` | `string` | سطر الأوامر الذي سيتم تنفيذه داخل وضع الحماية (على سبيل المثال، `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | المهلة بالثواني القيمة التلقائية: `30` |

### خطافات HTTP

ترسل خطّافات HTTP ملف JSON الخاص بالحدث كطلب POST إلى عنوان URL خارجي يستخدم HTTPS مباشرةً من داخل شبكة وضع الحماية. يعرض الخادم المستهدف قراره في نص استجابة HTTP باستخدام تنسيق JSON نفسه تمامًا (`{"decision": "allow"}` أو `{"decision": "deny", "reason": "..."}`).

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `type` | `string` | يجب أن تكون `"http"`. |
| `url` | `string` | نقطة نهاية HTTPS خارجية لإرسال حمولة الحدث إليها باستخدام POST. |
| `headers` | `object` | أزواج المفتاح/القيمة الاختيارية للعناوين المخصّصة غير الحسّاسة (مثل `{"X-Event-Source": "agent-sandbox"}`). للمصادقة، استخدِم [بيانات اعتماد](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ar) في قائمة السماح بالشبكة بدلاً من ذلك. |
| `timeout` | `integer` | المهلة بالثواني القيمة التلقائية: `30` |

#### الخادم الوكيل للخروج وتحويل الرموز المميزة

بما أنّ عمليات ربط HTTP يتم تنفيذها مباشرةً من داخل مساحة اسم شبكة وضع الحماية، تمر الطلبات الصادرة عبر الخادم الوكيل الشفاف للخروج. تمنحك هذه البنية ميزتَين مهمتَين للأمان:

- **إضافة الشبكة إلى القائمة المسموح بها:** يجب السماح صراحةً بنقاط النهاية المستهدَفة في `network.allowlist` ببيئتك. يحظر الخادم الوكيل حركة بيانات العودة الحلقية (`127.0.0.1` أو `localhost`)، لذا استهدف دائمًا نقاط النهاية الخارجية المُدرَجة في القائمة المسموح بها.
- **إدخال بيانات الاعتماد:** ليس عليك تخزين مفاتيح واجهة برمجة التطبيقات أو رموز الدخول السرية لحاملها داخل `.agents/hooks.json` أو ربطها بالحاوية. يمكنك تخزين كلمة المرور مرة واحدة [كبيانات اعتماد](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ar) والإشارة إليها باستخدام المعرّف من `network.allowlist` في بيئتك. يعترض خادم وكيل الخروج تلقائيًا على زيارات HTTP الواردة إلى الخطاف ويُدرج عنوان مصادقة حقيقيًا على الشبكة قبل مغادرة البيئة التجريبية. تضبط قواعد `transform` المضمّنة العناوين بالطريقة نفسها على الشبكة، وبيانات الاعتماد هي البيانات التي يجب استخدامها عندما تريد إعادة استخدام كلمة المرور في المشروع وتغييرها في مكان واحد. اطّلِع على [إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration).

## كيفية تعامل وقت التشغيل مع القرارات والأخطاء

- **الانتظار المتزامن:** يتوقّف الوكيل مؤقتًا وينتظر انتهاء عمليات الربط قبل المتابعة.
- **حظر تنفيذ الأداة:** إذا عرضت الدالة الخطافية السابقة للأداة القيمة `{"decision": "deny", "reason": "<your reason>"}`، تلغي بيئة التشغيل طلب استخدام الأداة على الفور. يطلع النموذج على سبب رفضك في سجلّ المحادثات ويتكيّف من خلال اختيار بديل آمن أو شرح سبب الحظر للمستخدم.
- **التعامل مع أعطال البرامج النصية وأخطاء HTTP وانتهاء المهلة:** في حال تعذُّر تنفيذ برنامج نصي للأوامر (حالة الخروج غير صفرية)، أو إذا عرض خطاف HTTP رمز حالة غير 2xx (مثل خطأ في الخادم 4xx أو 5xx)، أو إذا انتهت مهلة عملية أو عرضت JSON غير معروف، سيتعامل وقت التشغيل معها على أنّها موافقة (`allow`). يستمر تنفيذ الأداة بشكلٍ طبيعي، لذا لن يؤدي البرنامج النصي المعطّل أو خادم القياس عن بُعد الذي لا يمكن الوصول إليه إلى توقّف تطبيقك عن العمل.

## حالات الاستخدام الشائعة

### استرداد البيانات المتعدد المراحل لضمان خصوصية البيانات والامتثال للسياسات

عندما يمنع خطاف الوصول إلى الموارد المحظورة، مثل الأدلة التي تحتوي على معلومات تكشف الهوية الشخصية أو السجلات المالية السرية، يمكنك تمرير `previous_interaction_id` في المكالمة التالية لمواصلة عملية التسليم في البيئة نفسها. يقرأ الوكيل شرح الرفض ويستردّ البيانات تلقائيًا من خلال طلب البحث عن الجداول العامة الموافق عليها بدلاً من ذلك.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "view_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "view_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

String hooksConfig = """
{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
""";

String checkPrivacyScript = "#!/usr/bin/env python3\n"
    + "import sys, json\n"
    + "data = json.load(sys.stdin)\n"
    + "path = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\n"
    + "if \"/private/\" in path:\n"
    + "    resp = {\n"
    + "        \"decision\": \"deny\",\n"
    + "        \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"\n"
    + "    }\n"
    + "else:\n"
    + "    resp = {\"decision\": \"allow\"}\n"
    + "print(json.dumps(resp))\n";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks-scripts/check_privacy.py")
            .content(checkPrivacyScript)
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/private/employees.json")
            .content("{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target("workspace/public/summary.json")
            .content("{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}")
            .build()
    ))
    .build();

// Step 1: Agent attempts to read confidential PII records and is intercepted
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction int1 = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(int1.outputText().orElse(""));

// Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."))
    .environment(CreateAgentInteractionEnvironment.of(int1.environmentId().orElse("")))
    .previousInteractionId(int1.id().orElse(""))
    .build();

Interaction int2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println(int2.outputText().orElse(""));
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    hooksConfig := `{
  "privacy-gate": {
    "pre_tool_execution": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/check_privacy.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}`

    checkPrivacyScript := `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))
if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential '/private/' records is blocked by PII compliance policy. Query approved '/public/' summary tables instead."
    }
else:
    resp = {"decision": "allow"}
print(json.dumps(resp))
`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks-scripts/check_privacy.py"),
                Content: genai.Ptr(checkPrivacyScript),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/private/employees.json"),
                Content: genai.Ptr(`{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}`),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("workspace/public/summary.json"),
                Content: genai.Ptr(`{"department": "Engineering", "team_size": 42, "status": "active"}`),
            },
        },
    }

    // Step 1: Agent attempts to read confidential PII records and is intercepted
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    int1 := res1.Interaction
    if int1.OutputText != nil {
        fmt.Println(*int1.OutputText)
    }

    // Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*int1.EnvironmentID)),
            PreviousInteractionID: int1.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res2.Interaction.OutputText != nil {
        fmt.Println(*res2.Interaction.OutputText)
    }
}
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"view_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-09-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### تسجيل أحداث التدقيق والقياس عن بُعد خارجيًا

إرسال أحداث التدقيق في الوقت الفعلي من داخل وضع الحماية إلى خادم مراقبة خارجي كلّما تمّت قراءة الملفات أو تعديلها

- **مطابقة أدوات متعددة:** بما أنّ أدوات المطابقة تستخدم التعبيرات العادية القياسية، يمكنك دمج أدوات متعددة في قاعدة واحدة باستخدام علامات الأنابيب (`view_file|write_to_file|replace_file_content`) أو أحرف البدل (`.*_file`).
- **عدم تضمين الأسرار في الإعدادات:** خزِّن رمز المصادقة المميز [كبيانات اعتماد](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ar) وأشِر إليه باستخدام رقم التعريف من [إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration) في بيئتك (`network.allowlist.credential`). يضيف وكيل الخروج رمز المصادقة المميز الفعلي إلى الطلبات الصادرة. يضبط هذا المثال العنوان مضمّنًا مع `transform` بدلاً من ذلك، وهو محمي بالخادم الوكيل نفسه ويتناسب عندما تكون الرمز المميز تابعًا لعملية الضبط هذه.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "view_file|write_to_file|replace_file_content",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
                {"domain": "*"},
            ]
        },
    },
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "view_file|write_to_file|replace_file_content",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
    },
});
console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// Define hook without secrets; the egress proxy injects headers dynamically
String hooksConfig = """
{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
""";

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/hooks.json")
            .content(hooksConfig)
            .build()
    ))
    .network(Network.of(EnvironmentNetworkEgressAllowlist.of(
        Allowlist.builder()
            .allowlist(List.of(
                AllowlistEntry.builder()
                    .domain("telemetry.example.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer telemetry_secret_token_123"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("*").build()
            ))
            .build()
    )))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // Define hook without secrets; the egress proxy injects headers dynamically
    hooksConfig := `{
  "audit-logging": {
    "post_tool_execution": [
      {
        "matcher": "read_file|write_file",
        "hooks": [
          {
            "type": "http",
            "url": "https://telemetry.example.com/api/v1/agent-events",
            "timeout": 10
          }
        ]
      }
    ]
  }
}`

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/hooks.json"),
                Content: genai.Ptr(hooksConfig),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
            Allowlist: []interactions.AllowlistEntry{
                {
                    Domain: "telemetry.example.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer telemetry_secret_token_123",
                    })),
                },
                {
                    Domain: "*",
                },
            },
        }))),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"view_file|write_to_file|replace_file_content\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## القيود

- **نطاق أداة وضع الحماية:** تعترض الخطافات الأدوات المضمّنة داخل وضع الحماية: تطبيق الرموز البرمجية (`code_execution`) وعمليات نظام الملفات (`view_file` و`write_to_file` و`replace_file_content` و`list_dir` و`delete_file`). ولا يتم تشغيلها عند استدعاء الدوال المخصّصة (`function`) أو أدوات بروتوكول سياق النموذج (`mcp_server`) الخارجية التي تتم معالجتها خارج الحاوية.
- **قوائم السماح بالشبكة:** يتم تنفيذ خطافات HTTP داخل شبكة الحاوية. يجب السماح بعناوين URL المستهدَفة بشكل صريح في `network.allowlist` لبيئتك. يحظر الخادم الوكيل عناوين الاسترجاع (`localhost` و`127.0.0.1`).
- **الموافقة التلقائية عند حدوث أخطاء:** إذا تعذّر تنفيذ نص برمجي للربط (حالة الخروج غير صفرية) أو انتهت مهلته أو تعذّر تنفيذه، يسجّل وقت التشغيل الخطأ ويسمح بمتابعة استدعاء الأداة. يضمن ذلك ألا تؤدي النصوص البرمجية المعطّلة أو العمليات المعلقة إلى توقّف تطبيقاتك عن العمل.
- **حماية إعدادات وضع الحماية:** بما أنّ عمليات الربط يتم تنفيذها داخل وضع الحماية للحاوية، يمكن للوكلاء الذين لديهم أدوات كتابة في نظام الملفات أو أذونات تطبيق الرموز البرمجية لـ shell تعديل `.agents/hooks.json` أو النصوص البرمجية المحلية داخل مساحات العمل القابلة للكتابة. استخدِم خطافات الحاوية كإرشادات مبرمَجة للسياسات ووسائل حماية تشغيلية. إذا كانت هناك حاجة إلى مقاومة صارمة للتلاعب في عمليات تنفيذ النماذج غير الموثوق بها، يمكنك تحميل مصادر الإعدادات من مستودعات للقراءة فقط.

## الخطوات التالية

- تعرَّف على كيفية ضبط [بيئات ومساحات معزولة عن بُعد مستمرة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar).
- استكشاف إمكانات وأدوات [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar) المضمّنة
- راجِع [نظرة عامة على Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) للاطّلاع على جلسات المحادثة المترابطة والبث.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
