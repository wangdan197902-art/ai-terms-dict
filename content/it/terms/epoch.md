---
title: Epoch
term_id: epoch
category: training_techniques
subcategory: ''
tags:
- training
- Neural Networks
- basics
difficulty: 2
weight: 1
slug: epoch
date: '2026-07-18T15:58:32.403076Z'
lastmod: '2026-07-18T17:15:08.623621Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un passaggio completo del dataset di addestramento attraverso l'algoritmo
  di apprendimento automatico durante l'addestramento del modello.
---
## Definition

Nell'apprendimento automatico, un epoch rappresenta una singola iterazione sull'intero dataset di addestramento. Durante ogni epoch, il modello elabora tutti gli esempi di addestramento, aggiorna i suoi pesi tramite backpropagation e calcola la perdita. Il numero di epoch è un iperparametro critico che influenza la convergenza del modello e il rischio di overfitting.

### Summary

Un passaggio completo del dataset di addestramento attraverso l'algoritmo di apprendimento automatico durante l'addestramento del modello.

## Key Concepts

- Iterazione di addestramento
- Backpropagation
- Convergenza
- Ottimizzazione degli iperparametri

## Use Cases

- Configurazione dei loop di addestramento delle reti neurali
- Monitoraggio della perdita di validazione per ciclo
- Implementazione di strategie di early stopping

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Batch Size (Dimensione del batch)](/en/terms/batch-size-dimensione-del-batch/)
- [Iteration (Iterazione)](/en/terms/iteration-iterazione/)
- [Learning Rate (Tasso di apprendimento)](/en/terms/learning-rate-tasso-di-apprendimento/)
- [Overfitting (Sovradattamento)](/en/terms/overfitting-sovradattamento/)
