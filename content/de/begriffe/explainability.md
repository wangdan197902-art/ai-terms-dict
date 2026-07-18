---
title: "Erklärbarkeit"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
aliases:
  - /de/terms/explainability/
date: "2026-07-18T10:58:02.422470Z"
lastmod: "2026-07-18T11:44:44.894534Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Erklärbarkeit bezieht sich auf das Ausmaß, in dem ein Mensch die Ursache einer Entscheidung eines KI-Modells verstehen kann."
---

## Definition

Dieses Konzept adressiert das 'Black-Box'-Problem in komplexen KI-Systemen, indem es Einblicke darin bietet, wie Modelle zu bestimmten Vorhersagen gelangen. Techniken wie SHAP oder LIME helfen dabei, die Wichtigkeit von Merkmalen zu visualisieren

### Summary

Erklärbarkeit bezieht sich auf das Ausmaß, in dem ein Mensch die Ursache einer Entscheidung eines KI-Modells verstehen kann.

## Key Concepts

- Interpretierbarkeit
- Black-Box-Problem
- Vertrauen
- Bias-Erkennung

## Use Cases

- Prüfung von Kreditgenehmigungsalgorithmen auf Fairness
- Diagnose medizinischer Bildgebungsmodelle durch Kliniker
- Einhaltung regulatorischer Vorschriften bei der Finanzrisikobewertung

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

- [SHAP (SHapley Additive exPlanations)](/en/terms/shap-shapley-additive-explanations/)
- [LIME (Local Interpretable Model-agnostic Explanations)](/en/terms/lime-local-interpretable-model-agnostic-explanations/)
- [KI-Ethik (Ethische Richtlinien für KI)](/en/terms/ki-ethik-ethische-richtlinien-für-ki/)
- [Transparenz (Offenlegung von Prozessen)](/en/terms/transparenz-offenlegung-von-prozessen/)
