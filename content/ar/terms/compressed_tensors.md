---
title: "الموترات المضغوطة"
term_id: "compressed_tensors"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "hardware", "performance"]
difficulty: 4
weight: 1
slug: "compressed_tensors"
aliases:
  - /ar/terms/compressed_tensors/
date: "2026-07-18T15:49:17.003815Z"
lastmod: "2026-07-18T17:15:08.486063Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "موترات تم تقليل دقة بياناتها أو حجمها لتحسين كفاءة التخزين والحساب."
---

## Definition

الموترات المضغوطة هي مصفوفات متعددة الأبعاد تُستخدم في التعلم العميق، حيث تم تقليل الدقة العددية (على سبيل المثال، من float32 إلى int8) أو الكثافة (Sparsity). تُعرف هذه التقنية باسم التكميم (Quantization) أو...

### Summary

موترات تم تقليل دقة بياناتها أو حجمها لتحسين كفاءة التخزين والحساب.

## Key Concepts

- التكميم
- الكثافة المنخفضة (Sparsity)
- تحسين الذاكرة
- سرعة الاستدلال

## Use Cases

- نشر تطبيقات الذكاء الاصطناعي على الهواتف المحمولة
- معالجة الأجهزة الطرفية (Edge devices)
- تحسين استضافة النماذج اللغوية الكبيرة

## Code Example

```python
import torch
# Example of converting a tensor to half precision
x = torch.randn(10, 10)
x_compressed = x.half()
```

## Related Terms

- [التكميم (Quantization)](/en/terms/التكميم-quantization/)
- [القص (Pruning)](/en/terms/القص-pruning/)
- [تقطير النماذج (Model Distillation)](/en/terms/تقطير-النماذج-model-distillation/)
- [عائم 16 بت (Float16)](/en/terms/عائم-16-بت-float16/)
