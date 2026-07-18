---
title: "Date etichetate"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /ro/terms/labeled_data/
date: "2026-07-18T16:07:50.474990Z"
lastmod: "2026-07-18T17:15:09.673093Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Date pentru care valoarea corectă de ieșire sau țintă este furnizată alături de caracteristicile de intrare."
---

## Definition

Datele etichetate constau în eșantioane de intrare asociate cu etichetele de adevăr corespunzătoare, servind ca fundament pentru învățarea automată supravegheată. Ele permit algoritmilor să învețe maparea dintre intrare și ieșirea dorită.

### Summary

Date pentru care valoarea corectă de ieșire sau țintă este furnizată alături de caracteristicile de intrare.

## Key Concepts

- Învățare supravegheată
- Adevăr de bază
- Anotare
- Variabilă țintă

## Use Cases

- Antrenarea clasificatoarelor de imagini
- Construirea sistemelor de recunoaștere vocală
- Modelarea predictivă în finanțe

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (date neetichetate)](/en/terms/unlabeled_data-date-neetichetate/)
- [supervised_learning (învățare supravegheată)](/en/terms/supervised_learning-învățare-supravegheată/)
- [data_annotation (anotarea datelor)](/en/terms/data_annotation-anotarea-datelor/)
- [training_set (set de antrenament)](/en/terms/training_set-set-de-antrenament/)
