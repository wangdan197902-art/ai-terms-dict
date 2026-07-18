---
title: "למידה בהקשר"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /he/terms/in_context_learning/
date: "2026-07-18T15:23:00.631904Z"
lastmod: "2026-07-18T17:15:09.471868Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "טכניקה שבה מודלים לומדים לבצע משימות על ידי התבוננות בדוגמאות המסופרות בהנחיה."
---

## Definition

למידה בהקשר (ICL) מאפשרת למודלי שפה גדולים להסתגל למשימות חדשות ללא עדכון המשקלים שלהם. על ידי מתן זוגות קלט-פלט בתוך הקשר ההנחיה, המודל מסיק את הדפוס ו-

### Summary

טכניקה שבה מודלים לומדים לבצע משימות על ידי התבוננות בדוגמאות המסופרות בהנחיה.

## Key Concepts

- למידה עם מעט דוגמאות (Few-Shot)
- אפס דוגמאות (Zero-Shot)
- עיצוב הנחיה
- הסתגלות ללא משקלים

## Use Cases

- בדיקה מהירה של יכולות המודל על מערכי נתונים חדשים
- החלפת משימות דינמית בסוכנים קונברסטיביים
- פיתוח אב טיפוס ליישומי AI ללא אימון מחדש

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (הנדסת הנחיות)](/en/terms/prompt-engineering-הנדסת-הנחיות/)
- [Few-Shot (למידה עם מעט דוגמאות)](/en/terms/few-shot-למידה-עם-מעט-דוגמאות/)
- [Zero-Shot (למידה עם אפס דוגמאות)](/en/terms/zero-shot-למידה-עם-אפס-דוגמאות/)
- [Meta-Learning (למידה על למידה)](/en/terms/meta-learning-למידה-על-למידה/)
