---
title: עץ כדורי
term_id: ball_tree
category: basic_concepts
subcategory: ''
tags:
- Data Structures
- algorithms
- Machine Learning
difficulty: 4
weight: 1
slug: ball_tree
date: '2026-07-18T15:45:52.895219Z'
lastmod: '2026-07-18T17:15:09.515843Z'
draft: false
source: agnes_llm
status: published
language: he
description: מבנה נתונים של עץ בינארי המשמש לארגון נקודות במרחב, ומאפשר אופטימיזציה
  לחיפושי שכנים קרובים בקבוצות נתונים רב-ממדיות.
---
## Definition

עץ כדורי מחלק נקודות נתונים לכדורים היפר-ספריים (hyperspheres) מקוננים, במקום לתיבות היפר-מרובעות. מבנה זה מאפשר גיזום יעיל במהלך שאילתות שכנים קרובים על ידי חישוב מרחקים בין כדורים.

### Summary

מבנה נתונים של עץ בינארי המשמש לארגון נקודות במרחב, ומאפשר אופטימיזציה לחיפושי שכנים קרובים בקבוצות נתונים רב-ממדיות.

## Key Concepts

- חלוקת היפר-כדורים
- חיפוש שכנים קרובים
- נתונים רב-ממדיים
- עבור עץ (Tree traversal)

## Use Cases

- K-Nearest Neighbors (KNN) - שכנים קרובים
- ניתוח אשכולות (Clustering)
- זיהוי חריגות

## Code Example

```python
from sklearn.neighbors import BallTree
import numpy as np
X = np.random.rand(100, 5)
tree = BallTree(X, metric='euclidean')
```

## Related Terms

- [KD-tree (עץ KD)](/en/terms/kd-tree-עץ-kd/)
- [K-Nearest Neighbors (שכנים קרובים)](/en/terms/k-nearest-neighbors-שכנים-קרובים/)
- [Curse of Dimensionality (קללת הממדיות)](/en/terms/curse-of-dimensionality-קללת-הממדיות/)
