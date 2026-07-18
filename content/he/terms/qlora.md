---
title: "QLoRA"
term_id: "qlora"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "fine-tuning", "efficiency"]
difficulty: 4
weight: 1
slug: "qlora"
aliases:
  - /he/terms/qlora/
date: "2026-07-18T15:37:58.967373Z"
lastmod: "2026-07-18T17:15:09.502953Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "התאמה מדורגת נמוכה מקוונטזת (Quantized Low-Rank Adaptation), שיטה לכוונון עדין יעיל של מודלי שפה גדולים באמצעות קוונטיזציה ל-4 סיביות ומתאמים מדורגים נמוכים."
---

## Definition

QLoRA משלבת התאמה מדורגת נמוכה (LoRA) עם קוונטיזציה ל-4 סיביות כדי להפחיש משמעותית את נפח הזיכרון הנדרש לכוונון עדין של מודלים ענקיים. על ידי אחסון המשקלים בפורמט 4 סיביות והוספת מתאמים קטנים.

### Summary

התאמה מדורגת נמוכה מקוונטזת (Quantized Low-Rank Adaptation), שיטה לכוונון עדין יעיל של מודלי שפה גדולים באמצעות קוונטיזציה ל-4 סיביות ומתאמים מדורגים נמוכים.

## Key Concepts

- התאמה מדורגת נמוכה
- קוונטיזציה ל-4 סיביות
- יעילות זיכרון
- כוונון עדין

## Use Cases

- כוונון עדין עם כרטיסי מסך צרכניים
- סביבות עם משאבים מוגבלים
- איטרציה מהירה של מודלים

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base_model, config)
```

## Related Terms

- [LoRA (התאמה מדורגת נמוכה)](/en/terms/lora-התאמה-מדורגת-נמוכה/)
- [PEFT (טכניקות כוונון עדין יעילות פרמטרית)](/en/terms/peft-טכניקות-כוונון-עדין-יעילות-פרמטרית/)
- [Quantization (קוונטיזציה)](/en/terms/quantization-קוונטיזציה/)
- [Parameter-Efficient Fine-Tuning (כוונון עדין יעיל פרמטרית)](/en/terms/parameter-efficient-fine-tuning-כוונון-עדין-יעיל-פרמטרית/)
