---
title: "الطبقة الناعمة (Softmax)"
term_id: "softmax"
category: "basic_concepts"
subcategory: ""
tags: ["math", "neural-networks", "classification"]
difficulty: 2
weight: 1
slug: "softmax"
aliases:
  - /ar/terms/softmax/
date: "2026-07-18T15:38:49.559217Z"
lastmod: "2026-07-18T17:15:08.466706Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "دالة رياضية تحول متجهًا من القيم الحقيقية إلى توزيع احتمالي."
---

## Definition

تُستخدم الطبقة الناعمة على نطاق واسع في طبقة الإخراج للشبكات العصبية لمهام التصنيف متعدد الفئات. تأخذ متجهًا من القيم الخام (logits) وتطبيعها بحيث يمثل كل عنصر احتمالًا.

### Summary

دالة رياضية تحول متجهًا من القيم الحقيقية إلى توزيع احتمالي.

## Key Concepts

- التوزيع الاحتمالي
- القيم الخام (Logits)
- التطبيع
- التصنيف متعدد الفئات

## Use Cases

- طبقات إخراج تصنيف الصور
- توقع الرموز في نماذج اللغة
- التصنيف متعدد الوسوم

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (اختيار القيمة القصوى)](/en/terms/argmax-اختيار-القيمة-القصوى/)
- [Cross-Entropy Loss (خسارة الانتروبيا المتقاطعة)](/en/terms/cross-entropy-loss-خسارة-الانتروبيا-المتقاطعة/)
- [Logits (القيم الخام)](/en/terms/logits-القيم-الخام/)
- [Neural Network (الشبكة العصبية)](/en/terms/neural-network-الشبكة-العصبية/)
