---
title: "דיסטילציה של ידע"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /he/terms/knowledge_distillation/
date: "2026-07-18T16:08:25.091907Z"
lastmod: "2026-07-18T17:15:09.553828Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "דיסטילציה של ידע היא טכניקה לדחיסת מודל שבה מודל תלמיד קטן לומד לחקות את התנהגותו של מודל מורה גדול יותר."
---

## Definition

דיסטילציה של ידע היא שיטה למידת מכונה המשמשת לדחוס רשת נוירונים גדולה ומורכבת (המורה) לתוך רשת קטנה ויעילה יותר (התלמיד). מודל התלמיד מאומן כדי

### Summary

דיסטילציה של ידע היא טכניקה לדחיסת מודל שבה מודל תלמיד קטן לומד לחקות את התנהגותו של מודל מורה גדול יותר.

## Key Concepts

- מודל מורה-תלמיד
- דחיסת מודל
- יעדים רכים (Soft Targets)
- יעילות

## Use Cases

- הטמעת מודלים במכשירי קצה
- הפחתת זמן השהייה בהסקה
- הפחתת עלויות מחשוב בענן

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

- [Model Compression (דחיסת מודל)](/en/terms/model-compression-דחיסת-מודל/)
- [Pruning (גיזום)](/en/terms/pruning-גיזום/)
- [Quantization (כמותנות)](/en/terms/quantization-כמותנות/)
- [Neural Networks (רשתות נוירונים)](/en/terms/neural-networks-רשתות-נוירונים/)
