---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=ar
fetched_at: 2026-08-24T02:20:58.656341+00:00
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

تتيح لك الخطافات تشغيل نصوص برمجية مخصّصة أو طلبات HTTP خارجية قبل أن ينفّذ الوكيل الرمز البرمجي أو يعدّل الملفات داخل البيئة التجريبية المعزولة عن بُعد أو بعدها مباشرةً. استخدام خطافات لتوسيع حلقة الوكيل باستخدام ضوابط تلقائية ومسارات عمل في الخلفية، مثل:

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
    agent="antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
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

تتيح خطافات الويب حدثَين داخل وضع الحماية:

| الحدث | وقت تنشيطه | وظيفتها |
| --- | --- | --- |
| `pre_tool_execution` | قبل تشغيل أداة مباشرةً | يمكنك الموافقة على الأداة (`allow`) أو حظرها (`deny`) قبل تنفيذها. عند حظر النموذج، يرى سبب الرفض ويتكيّف معه. |
| `post_tool_execution` | مباشرةً بعد انتهاء أداة | تنفيذ مهام المتابعة، مثل تنسيق الرمز أو إجراء اختبارات الوحدات أو تسجيل بيانات القياس عن بُعد لا يمكن حظر الإجراءات المكتملة أو التراجع عنها. |

### `pre_tool_execution`

يتم تنشيط هذا الحدث قبل تنفيذ أي أداة مباشرةً. يقرأ النص البرمجي تفاصيل طلب الأداة من `stdin` ويعرض قرار JSON (`allow` أو `deny`) في `stdout`.

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

عندما يرفض أحد الخطافات تنفيذ أمر، يتم تخطّي استدعاء الأداة على الفور. يظهر للوكيل نتيجة خطأ تتضمّن سبب الرفض مباشرةً في دوره الحالي. يمكن للنموذج بعد ذلك تصحيح نفسه من خلال اختيار أمر بديل أو شرح سبب الحظر للمستخدم.

إذا كان النص البرمجي يعرض تنسيق JSON غير معروف أو نصًا عاديًا أو أي شيء آخر غير `{"decision": "deny"}`، سيتعامل وقت التشغيل مع الردّ على أنّه موافقة (`allow`).

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

- **ربط المستودع**: مستودع Git يحتوي على `.agents/hooks.json` بالإضافة إلى `AGENTS.md`.
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

### بنية وقواعد أداة المطابقة

تحدّد كل مجموعة قواعد في `hooks.json` وقت وكيفية تشغيل المعالجات باستخدام السمتَين `matcher` و`hooks`:

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `enabled` | `boolean` | اختياريّ. اضبط القيمة على `false` لإيقاف المجموعة (`true` تلقائيًا). |
| `matcher` | `string` | مطابقة أنماط التعبيرات العادية لأسماء الأدوات المستهدَفة داخل الحاوية |
| `hooks` | `array` | قائمة مرتّبة بتعريفات المعالجات (`command` أو `http`). يتم تشغيل المعالجات بالتسلسل حسب ترتيب التعريف. |

#### طريقة عمل تقييم التعابير العادية

عندما يستدعي الوكيل أداة داخل وضع الحماية، يقيّم وقت التشغيل اسم حاوية الأداة مقارنةً بنمط `matcher` باستخدام التعبيرات العادية RE2 القياسية. إذا كان التعبير العادي يطابق اسم الأداة، سيتم تنفيذ جميع معالجات مصفوفة `hooks` بالترتيب. إذا تطابقت عدة مجموعات قواعد مع الأداة نفسها، سيتم تشغيل جميع مصفوفات المعالجات المتوافقة.

يمكنك استهداف أي اسم أداة حاوية مدمجة: تطبيق الرموز البرمجية (`code_execution`) أو عمليات نظام الملفات (`read_file` و`write_file` و`list_files` و`delete_file`).

#### عبارات المطابقة الشائعة

- `"code_execution"`: تطابق تام للسلسلة مع أوامر shell وعمليات تنفيذ النصوص البرمجية
- ‫`"write_file"`: مطابقة تامة لإنشاء ملفات نظام الملفات وعمليات الكتابة على القرص
- `"read_file|write_file"`: يتيح الفصل باستخدام علامة الأنابيب مطابقة أسماء أدوات محدّدة متعددة في قاعدة واحدة.
- `".*_file"`: حرف بدل للتعبير العادي يطابق أي أداة تنتهي بـ `_file` (مثل `read_file` أو `write_file` أو `delete_file`). تتطلّب التعبيرات العادية القياسية RE2 استخدام `.*`، بينما تكون التعبيرات العامة البسيطة مثل `*_file` غير صالحة كبنية تعبير عادي ولن تتم مطابقتها.
- ‫`".*"` أو `"*"` أو `""`: نمط شامل يعترض كل طلب أداة داخل الحاوية.

## أنواع المعالجات

### خطافات الأوامر

تنفِّذ خطافات الأوامر أمرًا أو نصًا برمجيًا في Shell داخل وضع الحماية. يتلقّى النص البرمجي ملف JSON الخاص بالحدث على `stdin` ويعرض ملف JSON الخاص بالقرار على `stdout`.

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `type` | `string` | يجب أن تكون `"command"`. |
| `command` | `string` | سطر الأوامر الذي سيتم تنفيذه داخل وضع الحماية (على سبيل المثال، `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | مهلة بالثواني القيمة التلقائية: `30` |

### خطافات HTTP

ترسل خطّافات HTTP ملف JSON الخاص بالحدث كطلب POST إلى عنوان URL خارجي بتنسيق HTTPS مباشرةً من داخل شبكة وضع الحماية. يعرض الخادم المستهدف قراره في نص استجابة HTTP باستخدام تنسيق JSON نفسه تمامًا (`{"decision": "allow"}` أو `{"decision": "deny", "reason": "..."}`).

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `type` | `string` | يجب أن تكون `"http"`. |
| `url` | `string` | نقطة نهاية HTTPS خارجية لإرسال حمولة الحدث إليها باستخدام POST. |
| `headers` | `object` | أزواج المفتاح/القيمة الاختيارية للعناوين المخصّصة غير الحسّاسة (مثل `{"X-Event-Source": "agent-sandbox"}`). لاستخدام بيانات اعتماد المصادقة، استخدِم خادم وكيل الشبكة بدلاً من ذلك. |
| `timeout` | `integer` | مهلة بالثواني القيمة التلقائية: `30` |

#### الخادم الوكيل للخروج وتحويل الرموز المميزة

بما أنّ عمليات ربط HTTP يتم تنفيذها مباشرةً من داخل مساحة اسم شبكة وضع الحماية، تمر الطلبات الصادرة عبر الخادم الوكيل الشفاف للخروج. تمنحك هذه البنية ميزتَين مهمتَين للأمان:

- **إضافة الشبكة إلى القائمة المسموح بها:** يجب السماح بنقاط النهاية المستهدَفة بشكل صريح في `network.allowlist` لبيئتك. يحظر الخادم الوكيل حركة بيانات العودة الحلقية (`127.0.0.1` أو `localhost`)، لذا استهدف دائمًا نقاط النهاية الخارجية المُدرَجة في القائمة المسموح بها.
- **تحويل الرموز المميزة:** ليس عليك تخزين مفاتيح واجهة برمجة التطبيقات أو الرموز المميزة السرية لحاملها داخل `.agents/hooks.json` أو ربطها بالحاوية. بدلاً من ذلك، يمكنك ضبط قواعد تحويل الرموز المميزة في [إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration) (`network.allowlist.transform`). يعترض الخادم الوكيل الصادر تلقائيًا على زيارات HTTP الواردة من الخطاف ويُدرج عناوين المصادقة الحقيقية على الشبكة قبل مغادرة وضع الحماية.

## كيفية تعامل وقت التشغيل مع القرارات والأخطاء

- **الانتظار المتزامن:** يتوقّف الوكيل مؤقتًا وينتظر انتهاء عمليات الربط قبل المتابعة.
- **حظر تنفيذ الأداة:** إذا عرضت خطاف ما قبل الأداة القيمة `{"decision": "deny", "reason": "<your reason>"}`، تلغي بيئة التشغيل طلب استخدام الأداة على الفور. يطلع النموذج على سبب رفضك في سجلّ المحادثات ويتكيّف من خلال اختيار بديل آمن أو شرح سبب الحظر للمستخدم.
- **التعامل مع أعطال البرامج النصية وأخطاء HTTP وانتهاء المهلة:** إذا تعذّر تنفيذ برنامج نصي للأوامر (حالة الخروج غير صفرية)، أو عرض خطاف HTTP لرمز حالة غير 2xx (مثل خطأ في الخادم 4xx أو 5xx)، أو انتهت مهلة عملية أو عرض JSON غير معروف، سيتعامل وقت التشغيل معها على أنّها موافقة (`allow`). يستمر تنفيذ الأداة بشكل طبيعي، لذا لن يؤدي البرنامج النصي المعطّل أو خادم القياس عن بُعد الذي لا يمكن الوصول إليه إلى توقّف تطبيقك عن العمل.

## حالات الاستخدام الشائعة

### استرداد البيانات المتعدد المراحل لضمان خصوصية البيانات والامتثال للسياسات

عندما يمنع خطاف الوصول إلى الموارد المحظورة، مثل الأدلة التي تحتوي على معلومات تكشف الهوية الشخصية أو السجلات المالية السرية، يمكنك تمرير `previous_interaction_id` في المكالمة التالية لمواصلة الجلسة في البيئة نفسها. يقرأ الوكيل شرح الرفض ويستردّ البيانات تلقائيًا من خلال طلب البحث عن الجداول العامة التي تمت الموافقة عليها بدلاً من ذلك.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
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
    agent="antigravity-preview-05-2026",
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
    agent="antigravity-preview-05-2026",
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
                matcher: "read_file",
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
    agent: "antigravity-preview-05-2026",
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
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
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
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### تسجيل أحداث التدقيق والقياس عن بُعد خارجيًا

إرسال أحداث التدقيق في الوقت الفعلي من داخل وضع الحماية إلى خادم مراقبة خارجي كلما تمّت قراءة الملفات أو تعديلها

- **مطابقة أدوات متعددة:** بما أنّ أدوات المطابقة تستخدم تعبيرًا عاديًا موحّدًا، يمكنك دمج أدوات متعددة في قاعدة واحدة باستخدام علامات الأنابيب (`read_file|write_file`) أو أحرف البدل (`.*_file`).
- **عدم تضمين الأسرار في إعداداتك:** حدِّد رموز المصادقة المميزة في [إعدادات الشبكة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar#network-configuration) (`network.allowlist.transform`) لبيئتك. يضيف الخادم الوكيل الصادر تلقائيًا رموز المصادقة المميزة الحقيقية إلى الطلبات الصادرة.

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
                "matcher": "read_file|write_file",
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
    agent="antigravity-preview-05-2026",
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
                matcher: "read_file|write_file",
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
    agent: "antigravity-preview-05-2026",
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

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
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

- **نطاق أداة وضع الحماية:** تعترض الخطافات الأدوات المضمّنة داخل وضع الحماية: تنفيذ الرمز (`code_execution`) وعمليات نظام الملفات (`read_file` و`write_file` و`list_files` و`delete_file`). ولا يتم تشغيلها عند استدعاء الدوال المخصّصة (`function`) أو أدوات بروتوكول سياق النموذج الخارجي (`mcp_server`) التي تتم معالجتها خارج الحاوية.
- **قوائم السماح بالشبكة:** يتم تنفيذ خطافات HTTP داخل شبكة الحاوية. يجب السماح بعناوين URL المستهدَفة بشكل صريح في `network.allowlist` لبيئتك. يتم حظر عناوين الاسترجاع (`localhost` و`127.0.0.1`) بواسطة الخادم الوكيل.
- **الموافقة التلقائية عند حدوث أخطاء:** إذا تعذّر تنفيذ نص برمجي للربط (حالة الخروج غير صفرية) أو انتهت مهلته أو حدث خطأ فيه، يسجّل وقت التشغيل الخطأ ويسمح بمواصلة تنفيذ استدعاء الأداة. يضمن ذلك عدم توقّف تطبيقاتك بشكل تام بسبب نصوص برمجية غير صالحة أو عمليات معلّقة.
- **حماية إعدادات وضع الحماية:** بما أنّ عمليات الربط يتم تنفيذها داخل وضع الحماية للحاوية، يمكن للوكلاء الذين لديهم أدوات كتابة في نظام الملفات أو أذونات تطبيق الرموز البرمجية لـ shell تعديل `.agents/hooks.json` أو النصوص البرمجية المحلية داخل مساحات العمل القابلة للكتابة. استخدِم خطافات الحاوية كإرشادات مبرمَجة للسياسات ووسائل حماية تشغيلية. إذا كانت هناك حاجة إلى مقاومة صارمة للتلاعب في عمليات تنفيذ النماذج غير الموثوق بها، يمكنك تحميل مصادر الإعدادات من مستودعات للقراءة فقط.

## الخطوات التالية

- [كيفية ضبط بيئات ومساحات اختبار عن بُعد دائمة](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar)
- استكشِف إمكانات وأدوات [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar) المضمّنة.
- راجِع [نظرة عامة على Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) بشأن محادثة مترابطة والبث.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
