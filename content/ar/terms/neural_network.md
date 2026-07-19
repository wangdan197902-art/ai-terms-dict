---
title: "الشبكة العصبية"
term_id: "neural_network"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Architecture", "AI"]
difficulty: 4
weight: 1
slug: "neural_network"
date: "2026-07-18T15:28:58.920516Z"
lastmod: "2026-07-18T17:15:08.444068Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نظام حاسوبي مستوحى من الأدمغة البيولوجية، يتكون من عقد أو خلايا عصبية متصلة مرتبة في طبقات."
---
## Definition

الشبكة العصبية هي سلسلة من الخوارزميات التي تسعى إلى التعرف على العلاقات الكامنة في مجموعة من البيانات من خلال عملية تحاكي طريقة عمل الدماغ البشري. تتكون من طبقات من الخلايا العصبية المتصلة.

### Summary

نظام حاسوبي مستوحى من الأدمغة البيولوجية، يتكون من عقد أو خلايا عصبية متصلة مرتبة في طبقات.

## Key Concepts

- المستقبل (Perceptron)
- الانتشار العكسي (Backpropagation)
- دوال التنشيط (Activation Functions)
- الأوزان والانحيازات (Weights and Biases)

## Use Cases

- التعرف على الصور
- التعرف على الكلام
- التحليلات التنبؤية

## Code Example

```python
import torch.nn as nn
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layer = nn.Linear(10, 1)
    def forward(self, x):
        return self.layer(x)
```

## Related Terms

- [deep_learning (التعلم العميق)](/en/terms/deep_learning-التعلم-العميق/)
- [artificial_intelligence (الذكاء الاصطناعي)](/en/terms/artificial_intelligence-الذكاء-الاصطناعي/)
- [machine_learning (تعلم الآلة)](/en/terms/machine_learning-تعلم-الآلة/)
- [convolutional_neural_network (الشبكة العصبية التلافيفية)](/en/terms/convolutional_neural_network-الشبكة-العصبية-التلافيفية/)
