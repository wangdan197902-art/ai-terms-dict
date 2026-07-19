---
title: Матрица ошибок
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T15:46:12.165974Z'
lastmod: '2026-07-18T16:38:07.133824Z'
draft: false
source: agnes_llm
status: published
language: ru
description: Таблица, используемая для описания качества работы модели классификации
  на наборе тестовых данных.
---
## Definition

Матрица ошибок — это специфическая табличная структура, позволяющая визуализировать производительность алгоритма, как правило, алгоритма обучения с учителем. Она показывает количество истинно положительных, истинно отрицательных, ложноположительных и ложноотрицательных результатов.

### Summary

Таблица, используемая для описания качества работы модели классификации на наборе тестовых данных.

## Key Concepts

- Истинно положительные (True Positives)
- Ложно отрицательные (False Negatives)
- Точность (Precision)
- Полнота (Recall)

## Use Cases

- Оценка бинарных классификаторов
- Анализ производительности многоклассовой классификации
- Отладка смещения модели на несбалансированных наборах данных

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (точность)](/en/terms/precision-точность/)
- [recall (полнота)](/en/terms/recall-полнота/)
- [F1 score (метрика F1)](/en/terms/f1-score-метрика-f1/)
- [ROC curve (ROC-кривая)](/en/terms/roc-curve-roc-кривая/)
