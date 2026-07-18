---
title: "الاختبار"
term_id: "testing"
category: "engineering_practice"
subcategory: ""
tags: ["engineering", "quality-assurance", "deployment"]
difficulty: 2
weight: 1
slug: "testing"
aliases:
  - /ar/terms/testing/
date: "2026-07-18T15:38:49.559247Z"
lastmod: "2026-07-18T17:15:08.467200Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "العملية المنهجية لتقييم أداء وموثوقية نموذج الذكاء الاصطناعي على بيانات غير مرئية لضمان الجودة والسلامة."
---

## Definition

يتضمن الاختبار في هندسة الذكاء الاصطناعي تقييم النماذج بدقة ضد مجموعات بيانات متنوعة لتحديد التحيزات والأخطاء وقضايا المتانة. يشمل ذلك اختبارات الوحدة لمكونات الكود، واختبارات التكامل، وغيرها.

### Summary

العملية المنهجية لتقييم أداء وموثوقية نموذج الذكاء الاصطناعي على بيانات غير مرئية لضمان الجودة والسلامة.

## Key Concepts

- مقاييس التقييم
- كشف التحيز
- المتانة
- جاهزية الإنتاج

## Use Cases

- التحقق من دقة النموذج قبل النشر
- كشف نقاط الضعف الهجائية
- ضمان الامتثال للمبادئ التوجيهية الأخلاقية

## Code Example

```python
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
assert accuracy > 0.9, "Model accuracy below threshold"
```

## Related Terms

- [Validation (التحقق)](/en/terms/validation-التحقق/)
- [Benchmarking (المعايرة/المقارنة المرجعية)](/en/terms/benchmarking-المعايرة-المقارنة-المرجعية/)
- [CI/CD (التكامل المستمر/التسليم المستمر)](/en/terms/ci-cd-التكامل-المستمر-التسليم-المستمر/)
- [Model Evaluation (تقييم النموذج)](/en/terms/model-evaluation-تقييم-النموذج/)
