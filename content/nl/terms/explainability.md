---
title: "Uitlegbaarheid"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
date: "2026-07-18T15:35:52.087393Z"
lastmod: "2026-07-18T17:15:08.704339Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Uitlegbaarheid verwijst naar de mate waarin een mens de oorzaak kan begrijpen van een beslissing genomen door een AI-model."
---
## Definition

Dit concept adresseert het 'black box'-probleem in complexe AI-systemen door inzicht te bieden in hoe modellen tot specifieke voorspellingen komen. Technieken zoals SHAP of LIME helpen bij het visualiseren van functiebelangrijkheid.

### Summary

Uitlegbaarheid verwijst naar de mate waarin een mens de oorzaak kan begrijpen van een beslissing genomen door een AI-model.

## Key Concepts

- Interpreteerbaarheid
- Black Box Probleem
- Vertrouwen
- Detectie van Bias

## Use Cases

- Het controleren van hypotheekaanvraatalgoritmen op eerlijkheid
- Het diagnosticeren van medische beeldverwerkingsmodellen voor klinici
- Naleving van regelgeving bij financiële risicobeoordeling

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
- [AI Ethiek (morele richtlijnen voor AI)](/en/terms/ai-ethiek-morele-richtlijnen-voor-ai/)
- [Transparantie (openheid van processen)](/en/terms/transparantie-openheid-van-processen/)
