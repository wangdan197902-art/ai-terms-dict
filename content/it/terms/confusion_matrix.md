---
title: "Matrice di confusione"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /it/terms/confusion_matrix/
date: "2026-07-18T15:52:46.934656Z"
lastmod: "2026-07-18T17:15:08.609330Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Una tabella utilizzata per descrivere le prestazioni di un modello di classificazione su un insieme di dati di test."
---

## Definition

Una matrice di confusione è una specifica disposizione tabellare che consente la visualizzazione delle prestazioni di un algoritmo, tipicamente di apprendimento supervisionato. Mostra i conteggi dei veri positivi, veri negativi, falsi positivi e falsi negativi, fornendo una panoramica dettagliata della capacità del modello di distinguere tra le diverse classi.

### Summary

Una tabella utilizzata per descrivere le prestazioni di un modello di classificazione su un insieme di dati di test.

## Key Concepts

- Veri Positivi
- Falsi Negativi
- Precisione
- Richiamo (Recall)

## Use Cases

- Valutazione di classificatori binari
- Analisi delle prestazioni nella classificazione multiclasse
- Debug del bias del modello in dataset sbilanciati

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precisione (misura dell'accuratezza delle previsioni positive)](/en/terms/precisione-misura-dell-accuratezza-delle-previsioni-positive/)
- [richiamo (capacità di trovare tutti i casi rilevanti)](/en/terms/richiamo-capacità-di-trovare-tutti-i-casi-rilevanti/)
- [Punteggio F1 (media armonica di precisione e richiamo)](/en/terms/punteggio-f1-media-armonica-di-precisione-e-richiamo/)
- [Curva ROC (grafico delle prestazioni del classificatore)](/en/terms/curva-roc-grafico-delle-prestazioni-del-classificatore/)
