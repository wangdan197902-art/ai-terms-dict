---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:44.166144Z"
lastmod: "2026-07-18T17:15:09.481001Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "הסתגלות דרגה נמוכה היא שיטת עיבוד עדין חסכונית בפרמטרים המחדירה מטריצות פירוק דרגה ניתנות לאימון לתוך משקלי המודל הקיימים."
---
## Definition

LoRA מקפיאה את משקלי המודל המאומנים מראש ומכניסה מטריצות פירוק ניתנות לאימון לכל שכבה בארכיטקטורת הטרנספורמר. על ידי אופטימיזציה רק של מטריצות הדרגה הנמוכה הללו, LoRA מפחיתה משמעותית

### Summary

הסתגלות דרגה נמוכה היא שיטת עיבוד עדין חסכונית בפרמטרים המחדירה מטריצות פירוק דרגה ניתנות לאימון לתוך משקלי המודל הקיימים.

## Key Concepts

- עיבוד עדין חסכוני בפרמטרים
- פירוק דרגה
- הקפאת משקלים
- מודולי מתאם

## Use Cases

- התאמה אישית של מודלי שפה גדולים
- התאמה לדומיין ספציפי
- אימון עם משאבים מוגבלים

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (טכניקות עיבוד עדין חסכוניות)](/en/terms/peft-טכניקות-עיבוד-עדין-חסכוניות/)
- [עיבוד עדין](/en/terms/עיבוד-עדין/)
- [כמותיות](/en/terms/כמותיות/)
