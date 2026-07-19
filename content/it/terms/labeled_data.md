---
title: Dati etichettati
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
date: '2026-07-18T16:07:27.100059Z'
lastmod: '2026-07-18T17:15:08.641686Z'
draft: false
source: agnes_llm
status: published
language: it
description: Dati in cui il valore di output o target corretto è fornito insieme alle
  caratteristiche di input.
---
## Definition

I dati etichettati consistono in campioni di input accoppiati con le relative etichette di verità fondamentale (ground truth), fungendo da base per l'apprendimento supervisionato. Consentono agli algoritmi di apprendere la mappatura tra l'input e l'output desiderato.

### Summary

Dati in cui il valore di output o target corretto è fornito insieme alle caratteristiche di input.

## Key Concepts

- Apprendimento Supervisionato
- Verità Fondamentale
- Annotazione
- Variabile Target

## Use Cases

- Addestramento di classificatori di immagini
- Costruzione di sistemi di riconoscimento vocale
- Modellazione predittiva in ambito finanziario

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (dati non etichettati)](/en/terms/unlabeled_data-dati-non-etichettati/)
- [supervised_learning (apprendimento supervisionato)](/en/terms/supervised_learning-apprendimento-supervisionato/)
- [data_annotation (annotazione dei dati)](/en/terms/data_annotation-annotazione-dei-dati/)
- [training_set (insieme di addestramento)](/en/terms/training_set-insieme-di-addestramento/)
