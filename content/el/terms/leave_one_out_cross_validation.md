---
title: "Διασταυρούμενη Επαλήθευση Ένα-Προς-Ένα (Leave-One-Out Cross-Validation)"
term_id: "leave_one_out_cross_validation"
category: "basic_concepts"
subcategory: ""
tags: ["machine_learning", "evaluation", "statistics"]
difficulty: 3
weight: 1
slug: "leave_one_out_cross_validation"
aliases:
  - /el/terms/leave_one_out_cross_validation/
date: "2026-07-18T16:18:19.714370Z"
lastmod: "2026-07-18T17:15:09.925955Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Μια αυστηρή τεχνική δειγματοληψίας επαναχρησιμοποίησης όπου το μοντέλο εκπαιδεύεται σε όλα τα δείγματα εκτός από ένα και δοκιμάζεται σε αυτό το μεμονωμένο δείγμα που κρατήθηκε εκτός, επαναλαμβανόμενο "
---

## Definition

Η διασταυρούμενη επαλήθευση ένα-προς-ένα (LOOCV) είναι μια ειδική περίπτωση της διασταυρούμενης επαλήθεσης k-fold όπου το k ισούται με τον αριθμό των δειγμάτων στο σύνολο δεδομένων. Παρέχει μια σχεδόν αμερόληπτη εκτίμηση της απόδοσης του μοντέλου.

### Summary

Μια αυστηρή τεχνική δειγματοληψίας επαναχρησιμοποίησης όπου το μοντέλο εκπαιδεύεται σε όλα τα δείγματα εκτός από ένα και δοκιμάζεται σε αυτό το μεμονωμένο δείγμα που κρατήθηκε εκτός, επαναλαμβανόμενο για κάθε σημείο δεδομένων.

## Key Concepts

- Δειγματοληψία Επαναχρησιμοποίησης
- Αξιολόγηση Μοντέλου
- Εμπόριο Μεταξύ Πλαγίου και Διακύμανσης
- Υπολογιστικό Κόστος

## Use Cases

- Αξιολόγηση μοντέλων σε μικρά ιατρικά σύνολα δεδομένων
- Βελτιστοποίηση υπερπαραμέτρων όταν τα δεδομένα είναι σπάνια
- Στερεή σύγκριση απόδοσης αλγορίθμων

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (διασταυρούμενη επαλήθευση k-fold)](/en/terms/k-fold-cross-validation-διασταυρούμενη-επαλήθευση-k-fold/)
- [train_test_split (διαχωρισμός σε σύνολα εκπαίδευσης και δοκιμής)](/en/terms/train_test_split-διαχωρισμός-σε-σύνολα-εκπαίδευσης-και-δοκιμής/)
- [bootstrap (bootstrap sampling)](/en/terms/bootstrap-bootstrap-sampling/)
- [cross_validation_score (βαθμολογία διασταυρούμενης επαλήθευσης)](/en/terms/cross_validation_score-βαθμολογία-διασταυρούμενης-επαλήθευσης/)
