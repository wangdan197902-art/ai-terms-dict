---
title: כוונון קידומת
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T16:18:27.730786Z'
lastmod: '2026-07-18T17:15:09.574751Z'
draft: false
source: agnes_llm
status: published
language: he
description: שיטת כוונון עדיף לפרמטרים המוסיפה וקטורים רציפים ניתנים לאימון לקלט של
  שכבות טרנספורמר.
---
## Definition

כוונון קידומת הוא טכניקה להתאמה חסכונית בפרמטרים עבור טרנספורמרים מאומנים מראש. במקום לעדכן את כל משקולות המודל, השיטה מוסיפה רצף של וקטורים רציפים ניתנים לאימון (הקידומת) לפני הקלט של כל שכבת טרנספורמר, מה שמאפשר התאמה יעילה של המודל למשימות ספציפיות.

### Summary

שיטת כוונון עדיף לפרמטרים המוסיפה וקטורים רציפים ניתנים לאימון לקלט של שכבות טרנספורמר.

## Key Concepts

- כוונון חסכוני בפרמטרים
- הנחיות רכות (Soft Prompts)
- שכבות טרנספורמר
- שלד קפוא

## Use Cases

- התאמה ללמידה במספר דוגמאות מועטות (Few-shot)
- למידה רב-משימתית עם משאבים מוגבלים
- התאמה אישית של מודלי שפה גדולים לתחומים נישתיים

## Related Terms

- [prompt_tuning (כוונון הנחיות)](/en/terms/prompt_tuning-כוונון-הנחיות/)
- [p_tuning (כוונון P)](/en/terms/p_tuning-כוונון-p/)
- [adapter_modules (מודולי מתאם)](/en/terms/adapter_modules-מודולי-מתאם/)
- [peft (טכניקות הכשרה חסכוניות בפרמטרים)](/en/terms/peft-טכניקות-הכשרה-חסכוניות-בפרמטרים/)
