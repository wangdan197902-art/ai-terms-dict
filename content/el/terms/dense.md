---
title: "Πυκνό"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /el/terms/dense/
date: "2026-07-18T16:02:25.191479Z"
lastmod: "2026-07-18T17:15:09.900300Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένα στρώμα ή τανυστής όπου κάθε στοιχείο συνδέεται με κάθε στοιχείο του προηγούμενου στρώματος ή διάστασης."
---

## Definition

Στα νευρωνικά δίκτυα, ο όρος «πυκνό» αναφέρεται σε πλήρως συνδεδεμένα στρώματα όπου κάθε νευρώνας λαμβάνει είσοδο από όλους τους νευρώνες του προηγούμενου στρώματος. Αυτό αντιτίθεται στις αραιές συνδέσεις που βρίσκονται στα κυψελωτά ή άλλα ειδικά αρχιτεκτονικά σχήματα.

### Summary

Ένα στρώμα ή τανυστής όπου κάθε στοιχείο συνδέεται με κάθε στοιχείο του προηγούμενου στρώματος ή διάστασης.

## Key Concepts

- Πλήρως Συνδεδεμένο
- Μήτρα Βαρών
- Συνάρτηση Ενεργοποίησης
- Ολοκλήρωση Χαρακτηριστικών

## Use Cases

- Τελικά στρώματα ταξινόμησης σε Πολυεπίπεδα Δίκτυα (MLPs)
- Συγχώνευση χαρακτηριστικών σε υβριδικά μοντέλα
- Απλές εργασίες παλινδρόμησης

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Νευρωνικό Δίκτυο Προσαγωγής)](/en/terms/feedforward-neural-network-νευρωνικό-δίκτυο-προσαγωγής/)
- [Backpropagation (Ανάδραση Πίσω)](/en/terms/backpropagation-ανάδραση-πίσω/)
- [ReLU (Γραμμική Μονάδα Βελτιστοποίησης)](/en/terms/relu-γραμμική-μονάδα-βελτιστοποίησης/)
- [Bias Term (Όρος Μετατόπισης)](/en/terms/bias-term-όρος-μετατόπισης/)
