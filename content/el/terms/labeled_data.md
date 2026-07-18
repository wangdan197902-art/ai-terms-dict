---
title: "Επισημασμένα δεδομένα"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /el/terms/labeled_data/
date: "2026-07-18T16:17:36.301612Z"
lastmod: "2026-07-18T17:15:09.924835Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Δεδομένα στα οποία παρέχεται η σωστή έξοδος ή τιμή στόχος μαζί με τα χαρακτηριστικά εισόδου."
---

## Definition

Τα επισημασμένα δεδομένα αποτελούνται από δείγματα εισόδου ζευγαρωμένα με αντίστοιχες ετικέτες πραγματικής κατάστασης (ground truth), λειτουργώντας ως θεμέλιο για την εποπτευόμενη μηχανική μάθηση. Επιτρέπουν στους αλγορίθμους να μάθουν τον χάρτη αντιστοίχισης μεταξύ εισόδου και εξόδου.

### Summary

Δεδομένα στα οποία παρέχεται η σωστή έξοδος ή τιμή στόχος μαζί με τα χαρακτηριστικά εισόδου.

## Key Concepts

- Εποπτευόμενη Μάθηση
- Πραγματική Κατάσταση (Ground Truth)
- Επισήμανση
- Μεταβλητή Στόχος

## Use Cases

- Εκπαίδευση ταξινομητών εικόνων
- Κατασκευή συστημάτων αναγνώρισης ομιλίας
- Προβλεπτική μοντελοποίηση στον τομέα των χρηματοοικονομικών

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (μη επισημασμένα δεδομένα)](/en/terms/unlabeled_data-μη-επισημασμένα-δεδομένα/)
- [supervised_learning (εποπτευόμενη μάθηση)](/en/terms/supervised_learning-εποπτευόμενη-μάθηση/)
- [data_annotation (επισήμανση δεδομένων)](/en/terms/data_annotation-επισήμανση-δεδομένων/)
- [training_set (σύνολο εκπαίδευσης)](/en/terms/training_set-σύνολο-εκπαίδευσης/)
