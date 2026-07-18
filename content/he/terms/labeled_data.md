---
title: "נתונים מסומנים"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /he/terms/labeled_data/
date: "2026-07-18T16:09:15.066629Z"
lastmod: "2026-07-18T17:15:09.556497Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "נתונים בהם ערך הפלט או המטרה הנכון מסופקים לצד תכונות הקלט."
---

## Definition

נתונים מסומנים מורכבים מדגימות קלט המצורפות לתוויות אמת יסוד מתאימות, ומשמשים כבסיס ללמידת מכונה סופרתית. הם מאפשרים לאלגוריתמים ללמוד את ההתאמה בין קלט לפלט.

### Summary

נתונים בהם ערך הפלט או המטרה הנכון מסופקים לצד תכונות הקלט.

## Key Concepts

- למידה סופרתית
- אמת יסוד
- סימון נתונים
- משתנה מטרה

## Use Cases

- אימון ממייני תמונות
- בניית מערכות להכרת דיבור
- מודלים חיזויים במימון

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (נתונים לא מסומנים)](/en/terms/unlabeled_data-נתונים-לא-מסומנים/)
- [supervised_learning (למידה סופרתית)](/en/terms/supervised_learning-למידה-סופרתית/)
- [data_annotation (סימון נתונים)](/en/terms/data_annotation-סימון-נתונים/)
- [training_set (ערכת אימון)](/en/terms/training_set-ערכת-אימון/)
