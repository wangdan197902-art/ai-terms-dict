---
title: "Εποπτευόμενη Μάθηση"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /el/terms/supervised_learning/
date: "2026-07-18T15:45:07.264168Z"
lastmod: "2026-07-18T17:15:09.871519Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Ένα παράδειγμα μηχανικής μάθησης όπου ένα μοντέλο μαθαίνει να χαρτογραφεί εισόδους σε εξόδους με βάση παραδείγματα εκπαίδευσης με ετικέτες."
---

## Definition

Στην εποπτευόμενη μάθηση, ο αλγόριθμος εκπαιδεύεται σε ένα σύνολο δεδομένων με ετικέτες, δηλαδή κάθε παράδειγμα εισόδου συνοδεύεται από την σωστή έξοδο. Ο στόχος είναι το μοντέλο να μάθει τη θεμελιώδη σχέση μεταξύ εισόδου και εξόδου.

### Summary

Ένα παράδειγμα μηχανικής μάθησης όπου ένα μοντέλο μαθαίνει να χαρτογραφεί εισόδους σε εξόδους με βάση παραδείγματα εκπαίδευσης με ετικέτες.

## Key Concepts

- Δεδομένα με Ετικέτες
- Χαρτογράφηση Εισόδου-Εξόδου
- Ταξινόμηση
- Παλινδρόμηση

## Use Cases

- Ανίχνευση ανεπιθύμητου email
- Πρόβλεψη τιμών ακινήτων
- Αναγνώριση εικόνας

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (Μη εποπτευόμενη μάθηση)](/en/terms/unsupervised-learning-μη-εποπτευόμενη-μάθηση/)
- [Training Set (Σύνολο εκπαίδευσης)](/en/terms/training-set-σύνολο-εκπαίδευσης/)
- [Validation Set (Σύνολο επικύρωσης)](/en/terms/validation-set-σύνολο-επικύρωσης/)
- [Model Accuracy (Ακρίβεια μοντέλου)](/en/terms/model-accuracy-ακρίβεια-μοντέλου/)
