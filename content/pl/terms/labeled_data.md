---
title: Dane oznaczone
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
date: '2026-07-18T16:03:21.970383Z'
lastmod: '2026-07-18T17:15:08.890215Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Dane, w których prawidłowy wynik lub wartość docelowa jest podawana wraz
  z cechami wejściowymi.
---
## Definition

Dane oznaczone składają się z próbek wejściowych sparowanych z odpowiadającymi im etykietami prawdziwymi (ground truth), stanowiąc fundament uczenia nadzorowanego w uczeniu maszynowym. Pozwalają one algorytmom nauczyć się mapowania między wejściem a wyjściem.

### Summary

Dane, w których prawidłowy wynik lub wartość docelowa jest podawana wraz z cechami wejściowymi.

## Key Concepts

- Uczenie nadzorowane
- Prawda ziemska (Ground Truth)
- Adnotacja
- Zmienna docelowa

## Use Cases

- Szkolenie klasyfikatorów obrazu
- Budowanie systemów rozpoznawania mowy
- Modelowanie predykcyjne w finansach

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (dane nieoznaczone)](/en/terms/unlabeled_data-dane-nieoznaczone/)
- [supervised_learning (uczenie nadzorowane)](/en/terms/supervised_learning-uczenie-nadzorowane/)
- [data_annotation (adnotacja danych)](/en/terms/data_annotation-adnotacja-danych/)
- [training_set (zbiór treningowy)](/en/terms/training_set-zbiór-treningowy/)
