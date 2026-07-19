---
title: Címkézett adatok
term_id: labeled_data
category: basic_concepts
subcategory: ''
tags:
- data
- Supervised Learning
- fundamentals
difficulty: 1
weight: 1
slug: labeled_data
date: '2026-07-18T16:09:44.820218Z'
lastmod: '2026-07-18T17:15:09.801064Z'
draft: false
source: agnes_llm
status: published
language: hu
description: Adatok, ahol a helyes kimenet vagy célérték meg van adva a bemeneti jellemzők
  mellett.
---
## Definition

A címkézett adatok olyan bemeneti mintákból állnak, amelyek párosítva vannak a megfelelő valós értékkel (ground truth) címkékkel, és ezeket a felügyelt gépi tanulás alapjaként használják. Lehetővé teszik az algoritmusok számára, hogy megtanulják a leképezést a bemenet és a kimenet között.

### Summary

Adatok, ahol a helyes kimenet vagy célérték meg van adva a bemeneti jellemzők mellett.

## Key Concepts

- Felügyelt tanulás
- Valós érték (Ground Truth)
- Címkézés (Annotation)
- Célváltozó

## Use Cases

- Képosztályozók képzése
- Beszédfelismerő rendszerek fejlesztése
- Prediktív modellezés a pénzügyi szektorban

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (címkézetlen adatok)](/en/terms/unlabeled_data-címkézetlen-adatok/)
- [supervised_learning (felügyelt tanulás)](/en/terms/supervised_learning-felügyelt-tanulás/)
- [data_annotation (adatcímkézés)](/en/terms/data_annotation-adatcímkézés/)
- [training_set (tanítóhalmaz)](/en/terms/training_set-tanítóhalmaz/)
