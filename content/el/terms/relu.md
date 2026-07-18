---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /el/terms/relu/
date: "2026-07-18T15:44:09.922162Z"
lastmod: "2026-07-18T17:15:09.870174Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Η Rectified Linear Unit είναι μια συνάρτηση ενεργοποίησης που επιστρέφει την είσοδο απευθείας αν είναι θετική, διαφορετικά μηδέν."
---

## Definition

Η ReLU χρησιμοποιείται ευρέως στα νευρωνικά δίκτυα βαθιάς μάθησης λόγω της υπολογιστικής της αποδοτικότητας και της ικανότητάς της να μετριάζει το πρόβλημα της εξαφανιζόμενης παραγώγου. Ορίζεται μαθηματικά ως f(x) = max(0, x), εισάγοντας μη γραμμικότητα στο δίκτυο.

### Summary

Η Rectified Linear Unit είναι μια συνάρτηση ενεργοποίησης που επιστρέφει την είσοδο απευθείας αν είναι θετική, διαφορετικά μηδέν.

## Key Concepts

- Μη Γραμμικότητα
- Συνάρτηση Ενεργοποίησης
- Εξαφανιζόμενη Παράγωγος
- Κομματιαστή Γραμμική Συνάρτηση

## Use Cases

- Κρυφές στρώσεις σε CNNs
- Βαθιά Δίκτυα Προώθησης
- Μοντέλα Αναγνώρισης Εικόνας

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Σιγμοειδής συνάρτηση)](/en/terms/sigmoid-σιγμοειδής-συνάρτηση/)
- [Tanh (Υπερβολική εφαπτομένη)](/en/terms/tanh-υπερβολική-εφαπτομένη/)
- [Leaky ReLU (Διαρροή ReLU)](/en/terms/leaky-relu-διαρροή-relu/)
- [Neural Network (Νευρωνικό Δίκτυο)](/en/terms/neural-network-νευρωνικό-δίκτυο/)
