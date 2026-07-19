---
title: "وكيل ذكي"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
date: "2026-07-18T15:22:23.284401Z"
lastmod: "2026-07-18T17:15:08.431028Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نظام ذكاء اصطناعي قادر على إدراك بيئته، والاستدلال، واتخاذ إجراءات لتحقيق أهداف محددة بشكل مستقل."
---
## Definition

في الذكاء الاصطناعي، الوكيل هو كيان يعمل نيابة عن مستخدم أو نظام لإكمال المهام. وعلى عكس النماذج السلبية التي تستجيب فقط للأوامر، يمكن للوكلاء التخطيط، واستخدام الأدوات، والتكرار في إجراءاتهم لتحقيق النتائج المرجوة.

### Summary

نظام ذكاء اصطناعي قادر على إدراك بيئته، والاستدلال، واتخاذ إجراءات لتحقيق أهداف محددة بشكل مستقل.

## Key Concepts

- الاستقلالية
- استخدام الأدوات
- التخطيط
- حلقة رد الفعل

## Use Cases

- مساعدو البحث الآليون
- برمجيات كتابة الأكواد ذاتية التشغيل
- أنظمة التحكم في المنزل الذكي

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (نموذج لغوي كبير)](/en/terms/llm-نموذج-لغوي-كبير/)
- [Orchestration (التنسيق)](/en/terms/orchestration-التنسيق/)
- [Tool Calling (استدعاء الأدوات)](/en/terms/tool-calling-استدعاء-الأدوات/)
- [ReAct (التفكير والفعل)](/en/terms/react-التفكير-والفعل/)
