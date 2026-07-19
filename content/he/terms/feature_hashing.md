---
title: הדמיית תכונות
term_id: feature_hashing
category: basic_concepts
subcategory: ''
tags:
- preprocessing
- Text Mining
- Optimization
difficulty: 3
weight: 1
slug: feature_hashing
date: '2026-07-18T15:57:27.420399Z'
lastmod: '2026-07-18T17:15:09.540155Z'
draft: false
source: agnes_llm
status: published
language: he
description: טכניקה הממפה תכונות דלילות רבות-ממד למערך בגודל קבוע באמצעות פונקציית
  גיבוב.
---
## Definition

הדמיית תכונות, הידועה גם כ'מלכודת הגיבוב' (hashing trick), מאפשרת למודלי למידת מכונה לטפל במרחבי תכונות גדולים ודלילים ללא צורך בשמירה על מיפוי מפורש בין התכונות לאינדקסים שלהן. על ידי שימוש בפונקציית גיבוב, המערכת ממפה כל תכונה לערך יחיד במערך קבוע, מה שמפחית משמעותית את צריכת הזיכרון ומאפשר סקאלביליות גבוהה בעיבוד נתונים ענקיים.

### Summary

טכניקה הממפה תכונות דלילות רבות-ממד למערך בגודל קבוע באמצעות פונקציית גיבוב.

## Key Concepts

- פונקציית גיבוב
- וקטורים דלילים
- הפחתת מימד
- יעילות זיכרון

## Use Cases

- מיון טקסט עם אוצר מילים גדול
- מערכות המלצה עם מאגר פריטים עצום
- עיבוד נתמים בזמן אמת

## Code Example

```python
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# Example: Hashing text features
hasher = FeatureHasher(n_features=10, input_type='string')
docs = ['hello world', 'hello python', 'world python']
hashed = hasher.transform(docs)
print(hashed.toarray())
```

## Related Terms

- [One-hot encoding (קידוד חם-אחד)](/en/terms/one-hot-encoding-קידוד-חם-אחד/)
- [Bag of Words (שקית מילים)](/en/terms/bag-of-words-שקית-מילים/)
- [Dimensionality reduction (הפחתת מימד)](/en/terms/dimensionality-reduction-הפחתת-מימד/)
- [Sparse matrix (מטריצה דלילה)](/en/terms/sparse-matrix-מטריצה-דלילה/)
