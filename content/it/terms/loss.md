---
title: Funzione di perdita
term_id: loss
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
difficulty: 3
weight: 1
slug: loss
date: '2026-07-18T15:26:24.456784Z'
lastmod: '2026-07-18T17:15:08.569343Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un valore numerico che quantifica l'errore tra le previsioni di un modello
  e i valori target effettivi.
---
## Definition

Le funzioni di perdita, note anche come funzioni di costo, misurano quanto bene le previsioni di un modello di apprendimento automatico corrispondono alla verità fondamentale durante l'addestramento. L'obiettivo dell'algoritmo di ottimizzazione è minimizzare questo

### Summary

Un valore numerico che quantifica l'errore tra le previsioni di un modello e i valori target effettivi.

## Key Concepts

- Funzione di costo
- Ottimizzazione
- Discesa del gradiente
- Metrica di errore

## Use Cases

- Addestramento di classificatori di immagini
- Ottimizzazione di modelli di regressione
- Valutazione della convergenza del modello

## Code Example

```python
import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(outputs, targets)
```

## Related Terms

- [Accuracy (Accuratezza)](/en/terms/accuracy-accuratezza/)
- [Gradient Descent (Discesa del gradiente)](/en/terms/gradient-descent-discesa-del-gradiente/)
- [Cross-Entropy (Entropia incrociata)](/en/terms/cross-entropy-entropia-incrociata/)
- [Overfitting (Overfitting o sovradattamento)](/en/terms/overfitting-overfitting-o-sovradattamento/)
