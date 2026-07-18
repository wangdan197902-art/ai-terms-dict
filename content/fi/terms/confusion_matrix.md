---
title: "Sekavuusmatriisi"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /fi/terms/confusion_matrix/
date: "2026-07-18T15:49:17.573599Z"
lastmod: "2026-07-18T17:15:09.393844Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Taulukko, jota käytetään luokittelumallin suorituskyvyn kuvaamiseen testidatajoukossa."
---

## Definition

Sekavuusmatriisi on tietty taulukkorytymä, joka mahdollistaa algoritmin (yleensä valvotun oppimisen mallin) suorituskyvyn visualisoinnin. Se näyttää todellisten positiivisten, todellisten negatiivisten, väärien positiivisten ja väärien negatiivisten tulosten lukumäärät.

### Summary

Taulukko, jota käytetään luokittelumallin suorituskyvyn kuvaamiseen testidatajoukossa.

## Key Concepts

- Todelliset positiiviset
- Väärät negatiiviset
- Tarkkuus
- Kutaisuus (Recall)

## Use Cases

- Binääristen luokittelijoiden arviointi
- Moniluokkaisten luokittelumenetelmien analysointi
- Mallin harhan debuggaaminen epätasapainoisissa aineistoissa

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (tarkkuus)](/en/terms/precision-tarkkuus/)
- [recall (kutaisu)](/en/terms/recall-kutaisu/)
- [F1 score (F1-pisteet)](/en/terms/f1-score-f1-pisteet/)
- [ROC curve (ROC-käyrä)](/en/terms/roc-curve-roc-käyrä/)
