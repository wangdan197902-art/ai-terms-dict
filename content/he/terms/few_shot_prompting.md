---
title: הנחיה בדוגמאות מועטות
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T15:36:37.477637Z'
lastmod: '2026-07-18T17:15:09.499372Z'
draft: false
source: agnes_llm
status: published
language: he
description: הנחיה בדוגמאות מועטות היא טכניקה שבה ניתנים למודלי שפה גדולים (LLMs)
  מספר קטן של דוגמאות קלט-פלט בתוך ההנחיה כדי להנחות את התנהגותם.
---
## Definition

שיטה זו מנצלת את יכולות הלמידה בהקשר (In-context learning) של מודלי שפה גדולים על ידי מתן מספר דוגמאות מדגמות ישירות בהנחיה. בניגוד להתאמה עדינה (Fine-tuning) הדורשת עדכון משקלות המודל, גישה זו משתמשת רק בטקסט ההנחיה כדי להראות למודל את הפורמט הרצוי.

### Summary

הנחיה בדוגמאות מועטות היא טכניקה שבה ניתנים למודלי שפה גדולים (LLMs) מספר קטן של דוגמאות קלט-פלט בתוך ההנחיה כדי להנחות את התנהגותם.

## Key Concepts

- למידה בהקשר
- הנדסת הנחיות
- הנחיה מבוססת דוגמאות
- השוואה לאפס דוגמאות

## Use Cases

- עיצוב ניתוח רגשות
- התאמת סגנון כתיבת קוד
- חילוץ נתונים מבניים

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (ללא דוגמאות)](/en/terms/zero_shot-ללא-דוגמאות/)
- [prompt_engineering (הנדסת הנחיות)](/en/terms/prompt_engineering-הנדסת-הנחיות/)
- [in_context_learning (למידה בהקשר)](/en/terms/in_context_learning-למידה-בהקשר/)
- [llm (מודל שפה גדול)](/en/terms/llm-מודל-שפה-גדול/)
