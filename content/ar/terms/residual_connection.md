---
title: "الاتصال المتبقي"
term_id: "residual_connection"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "optimization", "deep_learning"]
difficulty: 3
weight: 1
slug: "residual_connection"
aliases:
  - /ar/terms/residual_connection/
date: "2026-07-18T15:38:35.992645Z"
lastmod: "2026-07-18T17:15:08.465938Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "آلية تضيف المدخلات مباشرة إلى مخرج الطبقة لتسهيل تدفق التدرجات في الشبكات العميقة."
---

## Definition

تسمح الاتصالات المتبقية، المعروفة أيضاً بالاتصالات القافزة، للتدرجات بالتدفق عبر الشبكة عن طريق إضافة المدخلات مباشرة إلى مخرج طبقة لاحقة. تحل هذه البنية مشكلة تلاشي التدرج.

### Summary

آلية تضيف المدخلات مباشرة إلى مخرج الطبقة لتسهيل تدفق التدرجات في الشبكات العميقة.

## Key Concepts

- الاتصالات القافزة
- مشكلة تلاشي التدرج
- التعلم المتبقي العميق
- تدفق التدرج

## Use Cases

- تدريب شبكات عصبية تلافيفية عميقة
- بنية المحولات (Transformers)
- نماذج تصنيف الصور

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (اتصال قافز)](/en/terms/skip_connection-اتصال-قافز/)
- [vanishing_gradient (تلاشي التدرج)](/en/terms/vanishing_gradient-تلاشي-التدرج/)
- [deep_learning (تعلم عميق)](/en/terms/deep_learning-تعلم-عميق/)
- [resnet (شبكة عصبية متبقية)](/en/terms/resnet-شبكة-عصبية-متبقية/)
