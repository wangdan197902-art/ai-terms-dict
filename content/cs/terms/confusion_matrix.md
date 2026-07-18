---
title: "Záměnová matice"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /cs/terms/confusion_matrix/
date: "2026-07-18T15:49:20.444244Z"
lastmod: "2026-07-18T17:15:09.112754Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Tabulka používaná k popisu výkonu klasifikačního modelu na sadě testovacích dat."
---

## Definition

Záměnová matice je specifické rozložení tabulky, které umožňuje vizualizaci výkonu algoritmu, obvykle učení s dozorem. Zobrazuje počty pravých pozitivních, pravých negativních, falešně pozitivních a falešně negativních výsledků.

### Summary

Tabulka používaná k popisu výkonu klasifikačního modelu na sadě testovacích dat.

## Key Concepts

- Pravá pozitiva
- Falešná negativa
- Přesnost
- Citlivost

## Use Cases

- Vyhodnocování binárních klasifikátorů
- Analýza výkonu víceklasové klasifikace
- Ladění zkreslení modelu na nevyvážených datech

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (přesnost)](/en/terms/precision-přesnost/)
- [recall (citlivost)](/en/terms/recall-citlivost/)
- [F1 score (F1 skóre)](/en/terms/f1-score-f1-skóre/)
- [ROC curve (ROC křivka)](/en/terms/roc-curve-roc-křivka/)
