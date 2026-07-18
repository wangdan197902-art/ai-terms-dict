---
title: "Explainability"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
aliases:
  - /el/terms/explainability/
date: "2026-07-18T15:40:28.391158Z"
lastmod: "2026-07-18T17:15:09.865996Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Η Explainability (Εξηγησιμότητα) αναφέρεται στο βαθμό στον οποίο ένας άνθρωπος μπορεί να κατανοήσει την αιτία μιας απόφασης που λαμβάνεται από ένα μοντέλο Τεχνητής Νοημοσύνης."
---

## Definition

Αυτή η έννοια αντιμετωπίζει το πρόβλημα του «μαύρου κουτιού» στα σύνθετα συστήματα ΤΝ, παρέχοντας όραση στο πώς τα μοντέλα καταλήγουν σε συγκεκριμένες προβλέψεις. Τεχνικές όπως οι SHAP ή LIME βοηθούν στην οπτικοποίηση της σημασίας των χαρακτηριστικών, επιτρέποντας στους ανθρώπους να επαληθεύσουν τη λογική πίσω από τις αποφάσεις του αλγορίθμου και να εντοπίσουν πιθανές προκαταλήψεις.

### Summary

Η Explainability (Εξηγησιμότητα) αναφέρεται στο βαθμό στον οποίο ένας άνθρωπος μπορεί να κατανοήσει την αιτία μιας απόφασης που λαμβάνεται από ένα μοντέλο Τεχνητής Νοημοσύνης.

## Key Concepts

- Ερμηνευσιμότητα
- Πρόβλημα Μαύρου Κουτιού
- Εμπιστοσύνη
- Ανίχνευση Προκατάληψης

## Use Cases

- Έλεγχος αλγορίθμων έγκρισης δανείων για δικαιοσύνη
- Διάγνωση μοντέλων ιατρικής απεικόνισης από κλινικούς γιατρούς
- Ρυθμιστική συμμόρφωση στην αξιολόγηση οικονομικού κινδύνου

## Code Example

```python
import shap
import numpy as np

# Assuming model is a trained scikit-learn model
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## Related Terms

- [SHAP (Shapley Additive exPlanations)](/en/terms/shap-shapley-additive-explanations/)
- [LIME (Local Interpretable Model-agnostic Explanations)](/en/terms/lime-local-interpretable-model-agnostic-explanations/)
- [AI Ethics (Ηθική Τεχνητής Νοημοσύνης)](/en/terms/ai-ethics-ηθική-τεχνητής-νοημοσύνης/)
- [Transparency (Διαφάνεια)](/en/terms/transparency-διαφάνεια/)
