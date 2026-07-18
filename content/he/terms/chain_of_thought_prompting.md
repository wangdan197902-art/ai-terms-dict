---
title: "הנחיה בשרשרת מחשבות (Chain-of-Thought Prompting)"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /he/terms/chain_of_thought_prompting/
date: "2026-07-18T15:35:46.694071Z"
lastmod: "2026-07-18T17:15:09.497156Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "זוהי טכניקה המעודדת מודלי שפה גדולים (LLMs) לייצר שלבי הסקה ביניים לפני הצגת התשובה הסופית."
---

## Definition

הנחיה בשרשרת מחשבות (CoT) משפרת את הביצועים של מודלי שפה גדולים במשימות הסקה מורכבות על ידי בקשה מפורשת מהמודל לנסח את הלוגיקה צעד אחר צעד. במקום לקפוץ ישירות לתשובה, המודל מפרט את תהליך החשיבה.

### Summary

זוהי טכניקה המעודדת מודלי שפה גדולים (LLMs) לייצר שלבי הסקה ביניים לפני הצגת התשובה הסופית.

## Key Concepts

- הסקה צעד אחר צעד
- למידה בכמה דוגמאות (Few-Shot)
- הסקה לוגית
- שלבים ביניים

## Use Cases

- פתרון בעיות מילוליות במתמטיקה
- משימות הסקה לוגית מורכבות
- ניפוי באגים בטעויות יצירת קוד

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [הנחיה ללא דוגמאות (Zero-Shot Prompting)](/en/terms/הנחיה-ללא-דוגמאות-zero-shot-prompting/)
- [הנחיה עם מספר דוגמאות (Few-Shot Prompting)](/en/terms/הנחיה-עם-מספר-דוגמאות-few-shot-prompting/)
- [עקביות עצמית (Self-Consistency)](/en/terms/עקביות-עצמית-self-consistency/)
- [הסקה (Reasoning)](/en/terms/הסקה-reasoning/)
