---
title: "تقطيع المعرفة"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /ar/terms/knowledge_distillation/
date: "2026-07-18T16:04:23.054370Z"
lastmod: "2026-07-18T17:15:08.518978Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "تقطيع المعرفة هو تقنية لضغط النموذج حيث يتعلم نموذج أصغر (طالب) محاكاة سلوك نموذج أكبر (معلّم)."
---

## Definition

تقطيع المعرفة هو طريقة في تعلم الآلة تُستخدم لضغط شبكة عصبية كبيرة ومعقدة (المعلّم) إلى شبكة أصغر وأكثر كفاءة (الطالب). يتم تدريب نموذج الطالب لمحاكاة مخرجات النموذج الأكبر.

### Summary

تقطيع المعرفة هو تقنية لضغط النموذج حيث يتعلم نموذج أصغر (طالب) محاكاة سلوك نموذج أكبر (معلّم).

## Key Concepts

- نموذج المعلّم والطالب
- ضغط النموذج
- الأهداف الناعمة
- الكفاءة

## Use Cases

- نشر النماذج على الأجهزة الطرفية
- تقليل زمن الاستجابة للاستنتاج
- خفض تكاليف الحوسبة السحابية

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (ضغط النموذج)](/en/terms/model-compression-ضغط-النموذج/)
- [Pruning (القص)](/en/terms/pruning-القص/)
- [Quantization (الكمّية)](/en/terms/quantization-الكم-ية/)
- [Neural Networks (الشبكات العصبية)](/en/terms/neural-networks-الشبكات-العصبية/)
