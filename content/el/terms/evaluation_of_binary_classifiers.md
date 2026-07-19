---
title: Αξιολόγηση δυαδικών ταξινομητών
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T16:06:03.427400Z'
lastmod: '2026-07-18T17:15:09.905997Z'
draft: false
source: agnes_llm
status: published
language: el
description: Η διαδικασία αξιολόγησης της απόδοσης μοντέλων μηχανικής μάθησης που
  προβλέπουν μία από δύο πιθανές εκβάλλσεις.
---
## Definition

Αυτό το πεδίο περιλαμβάνει την ανάλυση δεικτών όπως η ακρίβεια, η προληπτικότητα, η ανακάλυψη (recall), ο συντελεστής F1 και το Εμβαδόν κάτω από την Καμπύλη ROC (AUC-ROC). Βοηθά στον προσδιορισμό του πόσο καλά ένα μοντέλο διαχωρίζει τις κατηγορίες.

### Summary

Η διαδικασία αξιολόγησης της απόδοσης μοντέλων μηχανικής μάθησης που προβλέπουν μία από δύο πιθανές εκβάλλσεις.

## Key Concepts

- Πίνακας Σύγχυσης
- Εμπορική Ισορροπία Προληπτικότητας-Ανακάλυψης
- Καμπύλη ROC
- Συντελεστής F1

## Use Cases

- Ιατρικός έλεγχος ασθενειών
- Φιλτράρισμα spam email
- Αξιολόγηση πιστωτικού κινδύνου

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (πίνακας σύγχυσης)](/en/terms/confusion_matrix-πίνακας-σύγχυσης/)
- [roc_auc (εμβαδόν κάτω από την καμπύλη ROC)](/en/terms/roc_auc-εμβαδόν-κάτω-από-την-καμπύλη-roc/)
- [precision_recall (προληπτικότητα και ανακάλυψη)](/en/terms/precision_recall-προληπτικότητα-και-ανακάλυψη/)
- [cross_validation (διασταυρούμενη επικύρωση)](/en/terms/cross_validation-διασταυρούμενη-επικύρωση/)
