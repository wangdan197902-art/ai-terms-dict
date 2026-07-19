---
title: קצב למידה
term_id: learning_rate
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
- hyperparameters
difficulty: 3
weight: 1
slug: learning_rate
date: '2026-07-18T15:37:11.364274Z'
lastmod: '2026-07-18T17:15:09.500722Z'
draft: false
source: agnes_llm
status: published
language: he
description: פרמטר היפר-פרמטרי השולט בגודל הצעד במהלך אופטימיזציה של המודל כדי למזער
  את פונקציית האובדן.
---
## Definition

קצב הלמידה קובע כמה משקולות המודל מתעדכנות ביחס לגרדיאנט המחושב בכל איטרציית אימון. קצב גבוה מדי עלול לגרום למודל "להחטיא" את הנקודה האופטימלית (Overshooting), בעוד שקצב נמוך מדי מאריך את זמן האימון.

### Summary

פרמטר היפר-פרמטרי השולט בגודל הצעד במהלך אופטימיזציה של המודל כדי למזער את פונקציית האובדן.

## Key Concepts

- ירידת גרדיאנט
- כוונון היפר-פרמטרים
- התכנסות
- אופטימייזר

## Use Cases

- אימון רשתות נוירונים
- אופטימיזציה של מודלי למידה עמוקה
- עדכוני מדיניות בלמידה מחזקת

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent (ירידת גרדיאנט)](/en/terms/gradient_descent-ירידת-גרדיאנט/)
- [optimizer (אופטימייזר)](/en/terms/optimizer-אופטימייזר/)
- [hyperparameter (היפר-פרמטר)](/en/terms/hyperparameter-היפר-פרמטר/)
- [convergence (התכנסות)](/en/terms/convergence-התכנסות/)
