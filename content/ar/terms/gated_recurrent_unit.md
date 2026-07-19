---
title: "الوحدة المتكررة ذات البوابات"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T15:58:50.894932Z"
lastmod: "2026-07-18T17:15:08.507000Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "نوع من بنية الشبكات العصبية المتكررة يستخدم آليات بوابة للتحكم في تدفق المعلومات، ويعتبر بديلاً مبسطاً لشبكة الذاكرة طويلة وقصيرة المدى (LSTM)."
---
## Definition

الوحدة المتكررة ذات البوابات (GRU) هي خلية متخصصة في الشبكات العصبية المتكررة (RNN) مصممة لالتقاط التبعيات طويلة المدى في البيانات التسلسلية. تقوم بتبسيط بنية شبكة الذاكرة طويلة وقصيرة المدى (LSTM) من خلال دمج بوابتي التحديث وإعادة التعيين في بنية واحدة أكثر كفاءة وأقل تعقيداً.

### Summary

نوع من بنية الشبكات العصبية المتكررة يستخدم آليات بوابة للتحكم في تدفق المعلومات، ويعتبر بديلاً مبسطاً لشبكة الذاكرة طويلة وقصيرة المدى (LSTM).

## Key Concepts

- الشبكة العصبية المتكررة
- بوابة التحديث
- بوابة إعادة التعيين
- نمذجة التسلسل

## Use Cases

- معالجة اللغة الطبيعية
- التنبؤ بالسلاسل الزمنية
- التعرف على الكلام

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM (شبكة الذاكرة طويلة وقصيرة المدى)](/en/terms/lstm-شبكة-الذاكرة-طويلة-وقصيرة-المدى/)
- [RNN (الشبكة العصبية المتكررة)](/en/terms/rnn-الشبكة-العصبية-المتكررة/)
- [Deep Learning (التعلم العميق)](/en/terms/deep-learning-التعلم-العميق/)
- [Sequence-to-Sequence (من تسلسل إلى تسلسل)](/en/terms/sequence-to-sequence-من-تسلسل-إلى-تسلسل/)
