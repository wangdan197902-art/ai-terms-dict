---
title: "الاستدلال"
term_id: "inference"
category: "engineering_practice"
subcategory: ""
tags: ["Deployment", "Production", "Performance"]
difficulty: 2
weight: 1
slug: "inference"
date: "2026-07-18T15:22:59.170228Z"
lastmod: "2026-07-18T17:15:08.433144Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "المرحلة التي يعالج فيها النموذج المُدرَّب بيانات جديدة لتوليد تنبؤات أو مخرجات."
---
## Definition

يشير الاستدلال إلى مرحلة النشر حيث يُستخدم النموذج النهائي لاتخاذ قرارات أو تقديم تنبؤات على بيانات غير مرئية. على عكس التدريب الذي يحدث الأوزان، يستهلك الاستدلال موارد حاسوبية لتقديم النتائج.

### Summary

المرحلة التي يعالج فيها النموذج المُدرَّب بيانات جديدة لتوليد تنبؤات أو مخرجات.

## Key Concepts

- التنبؤ
- زمن الاستجابة (Latency)
- الإنتاجية (Throughput)
- النشر

## Use Cases

- الكشف عن الاحتيال في الوقت الفعلي في المعاملات المصرفية
- توليد الردود في تفاعلات روبوتات الدردشة الحية
- تصنيف الصور في أنظمة المركبات ذاتية القيادة

## Code Example

```python
import torch
model.eval()
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1)
```

## Related Terms

- [Training (التدريب)](/en/terms/training-التدريب/)
- [Latency Optimization (تحسين زمن الاستجابة)](/en/terms/latency-optimization-تحسين-زمن-الاستجابة/)
- [Batching (التجميع)](/en/terms/batching-التجميع/)
- [Model Serving (خدمة النماذج)](/en/terms/model-serving-خدمة-النماذج/)
