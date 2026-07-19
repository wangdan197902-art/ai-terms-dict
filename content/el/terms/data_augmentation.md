---
title: Data Augmentation
term_id: data_augmentation
category: training_techniques
subcategory: ''
tags:
- Machine Learning
- preprocessing
- cv
difficulty: 2
weight: 1
slug: data_augmentation
date: '2026-07-18T15:58:51.268244Z'
lastmod: '2026-07-18T17:15:09.894257Z'
draft: false
source: agnes_llm
status: published
language: el
description: Η ενίσχυση δεδομένων είναι μια τεχνική που χρησιμοποιείται για την αύξηση
  της ποικιλίας και του μεγέθους των συνόλων εκπαίδευσης εφαρμόζοντας μετασχηματισμούς
  στα υπάρχοντα σημεία δεδομένων.
---
## Definition

Αυτή η μέθοδος επεκτείνει τεχνητά το σύνολο εκπαίδευσης δημιουργώντας τροποποιημένες εκδόσεις υφιστάμενων δειγμάτων, όπως περιστροφή εικόνων, προσθήκη θορύβου σε ήχο ή αντικατάσταση συνωνύμων σε κείμενο. Βοηθά στην πρόληψη

### Summary

Η ενίσχυση δεδομένων είναι μια τεχνική που χρησιμοποιείται για την αύξηση της ποικιλίας και του μεγέθους των συνόλων εκπαίδευσης εφαρμόζοντας μετασχηματισμούς στα υπάρχοντα σημεία δεδομένων.

## Key Concepts

- Πρόληψη Υπερπροσαρμογής
- Επέκταση Συνόλου Δεδομένων
- Γενίκευση
- Μετασχηματισμοί

## Use Cases

- Βελτίωση της ανθεκτικότητας μοντέλων όρασης υπολογιστή
- Βελτίωση της απόδοσης μοντέλων Επεξεργασίας Φυσικής Γλώσσας με περιορισμένο κείμενο
- Ισορροπία ανισορροπημένων συνόλων δεδομένων

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (Κανονικοποίηση)](/en/terms/regularization-κανονικοποίηση/)
- [Synthetic Data (Συνθετικά Δεδομένα)](/en/terms/synthetic-data-συνθετικά-δεδομένα/)
- [Transfer Learning (Μεταφορική Μάθηση)](/en/terms/transfer-learning-μεταφορική-μάθηση/)
- [Overfitting (Υπερπροσαρμογή)](/en/terms/overfitting-υπερπροσαρμογή/)
