---
title: "لورا (LoRA)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /ar/terms/lora/
date: "2026-07-18T15:27:20.092684Z"
lastmod: "2026-07-18T17:15:08.441965Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "التكيف منخفض الرتبة هو طريقة ضبط دقيق كفؤة من حيث المعلمات تقوم بحقن مصفوفات تحلل الرتبة القابلة للتدريب في أوزان النموذج الموجودة."
---

## Definition

تجمّد لورا أوزان النموذج المدربة مسبقاً وتدخل مصفوفات تحلل قابلة للتدريب في كل طبقة من بنية المحول. من خلال تحسين هذه المصفوفات منخفضة الرتبة فقط، تقلل لورا بشكل كبير

### Summary

التكيف منخفض الرتبة هو طريقة ضبط دقيق كفؤة من حيث المعلمات تقوم بحقن مصفوفات تحلل الرتبة القابلة للتدريب في أوزان النموذج الموجودة.

## Key Concepts

- الضبط الدقيق الكفء من حيث المعلمات
- تحلل الرتبة
- تجميد الأوزان
- وحدات المحول

## Use Cases

- تخصيص النماذج اللغوية الكبيرة
- التكيف مع المجال المحدد
- التدريب مقيد الموارد

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (التكيف الكفء من حيث المعلمات)](/en/terms/peft-التكيف-الكفء-من-حيث-المعلمات/)
- [الضبط الدقيق](/en/terms/الضبط-الدقيق/)
- [الكمّ](/en/terms/الكم/)
