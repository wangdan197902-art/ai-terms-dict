---
title: ReLU
term_id: relu
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Activation Functions
- Deep Learning
difficulty: 3
weight: 1
slug: relu
date: '2026-07-18T15:38:23.148178Z'
lastmod: '2026-07-18T17:15:08.465346Z'
draft: false
source: agnes_llm
status: published
language: ar
description: وحدة خطية مستقيمة (Rectified Linear Unit) هي دالة تنشيط تُخرج المدخلات
  مباشرة إذا كانت موجبة، وإلا فإنها تصفرها.
---
## Definition

يُستخدم ReReLU على نطاق واسع في الشبكات العصبية للتعلم العميق بسبب كفاءته الحسابية وقدرته على التخفيف من مشكلة تلاشي التدرج. مُعرّف رياضياً كـ f(x) = max(0, x)، فإنه يقدم عدم خطية بسيطة.

### Summary

وحدة خطية مستقيمة (Rectified Linear Unit) هي دالة تنشيط تُخرج المدخلات مباشرة إذا كانت موجبة، وإلا فإنها تصفرها.

## Key Concepts

- عدم الخطية
- دالة التنشيط
- تلاشي التدرج
- خطي جزئي

## Use Cases

- الطبقات المخفية في شبكات CNN
- شبكات التغذية الأمامية العميقة
- نماذج التعرف على الصور

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (دالة سيجمويد)](/en/terms/sigmoid-دالة-سيجمويد/)
- [Tanh (دالة جيب التمام الزائدية)](/en/terms/tanh-دالة-جيب-التمام-الزائدية/)
- [Leaky ReLU (ReLU المتسرب)](/en/terms/leaky-relu-relu-المتسرب/)
- [Neural Network (الشبكة العصبية)](/en/terms/neural-network-الشبكة-العصبية/)
