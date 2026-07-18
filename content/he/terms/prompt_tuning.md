---
title: "כוונון הנחיות (Prompt Tuning)"
term_id: "prompt_tuning"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "optimization", "efficiency"]
difficulty: 3
weight: 1
slug: "prompt_tuning"
aliases:
  - /he/terms/prompt_tuning/
date: "2026-07-18T16:20:23.435304Z"
lastmod: "2026-07-18T17:15:09.576356Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "שיטת דיוק יעילה מבחינת פרמטרים הממקסמת הטבעות קלט רציפות במקום לעדכן את כל משקולות המודל."
---

## Definition

כוונון הנחיות כולל הוספת הנחיות רכות ניתנות לאימון (וקטורים רציפים) לשכבת הקלט של מודל שפה מאומן מראש, תוך שמירה על פרמטרי המודל הבסיסיים קפואים. גישה זו מאפשרת התאמה יעילה.

### Summary

שיטת דיוק יעילה מבחינת פרמטרים הממקסמת הטבעות קלט רציפות במקום לעדכן את כל משקולות המודל.

## Key Concepts

- הנחיות רכות
- יעילות פרמטרית
- משקולות קפואות
- למידה בדוגמה בודדת/מעטה

## Use Cases

- התאמת מודלי שפה גדולים (LLMs) לתחומים ספציפיים
- דיוק במשאבים מועטים
- אופטימיזציה של למידה רב-משימתית

## Related Terms

- [PEFT (טכניקות דיוק יעילות מבחינת פרמטרים)](/en/terms/peft-טכניקות-דיוק-יעילות-מבחינת-פרמטרים/)
- [LoRA (התאמה מקומית נמוכה)](/en/terms/lora-התאמה-מקומית-נמוכה/)
- [in-context learning (למידה בהקשר)](/en/terms/in-context-learning-למידה-בהקשר/)
- [fine-tuning (דיוק עדין)](/en/terms/fine-tuning-דיוק-עדין/)
