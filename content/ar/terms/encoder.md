---
title: "المُشفِّر (Encoder)"
term_id: "encoder"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Network Architecture", "Feature Engineering", "Transformers"]
difficulty: 3
weight: 1
slug: "encoder"
aliases:
  - /ar/terms/encoder/
date: "2026-07-18T15:36:46.347189Z"
lastmod: "2026-07-18T17:15:08.460828Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "المُشفِّر هو مكون في الشبكة العصبية يحول بيانات الإدخال إلى تمثيل مضغوط وذو معنى."
---

## Definition

تعالج المشفرات تسلسلات الإدخال الخام أو هياكل البيانات وتحولها إلى تمثيلات في الفضاء الكامن (Latent Space)، وغالباً ما تسمى تضمينات أو رموزاً. وهي مركزية في معماريات مثل المحولات (Transformers) والمشفرات التلقائية.

### Summary

المُشفِّر هو مكون في الشبكة العصبية يحول بيانات الإدخال إلى تمثيل مضغوط وذو معنى.

## Key Concepts

- استخراج الميزات (Feature Extraction)
- الفضاء الكامن (Latent Space)
- معالجة التسلسل (Sequence Processing)
- الضغط (Compression)

## Use Cases

- معالجة النص المدخل في نماذج المحولات
- ضغط الصور في المشفرات التلقائية لإزالة الضوضاء
- استخراج ميزات المشاعر من المراجعات النصية

## Code Example

```python
import torch.nn as nn

class SimpleEncoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, hidden_dim)
    
    def forward(self, x):
        return torch.relu(self.fc(x))
```

## Related Terms

- [المُفسِّر (Decoder)](/en/terms/الم-فس-ر-decoder/)
- [المحول (Transformer)](/en/terms/المحول-transformer/)
- [المُشفِّر التلقائي (Autoencoder)](/en/terms/الم-شف-ر-التلقائي-autoencoder/)
- [المتغير الكامن (Latent Variable)](/en/terms/المتغير-الكامن-latent-variable/)
