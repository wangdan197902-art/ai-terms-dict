---
title: "Selitettävyys"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
aliases:
  - /fi/terms/explainability/
date: "2026-07-18T15:36:04.965379Z"
lastmod: "2026-07-18T17:15:09.369931Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Selitettävyys viittaa siihen, missä määrin ihminen voi ymmärtää tekoälymallin tekemän päätöksen syyn."
---

## Definition

Tämä käsite käsittelee monimutkaisten tekoälyjärjestelmien 'mustan laatikon' ongelmaa tarjoamalla oivalluksia siitä, miten mallit saavuttavat tiettyjä ennusteita. Tekniikat kuten SHAP tai LIME auttavat visualisoimaan ominaisuuksien merkitystä.

### Summary

Selitettävyys viittaa siihen, missä määrin ihminen voi ymmärtää tekoälymallin tekemän päätöksen syyn.

## Key Concepts

- Tulkittavuus
- Mustan laatikon ongelma
- Luottamus
- Vaikeuden havaitseminen

## Use Cases

- Luotonmyöntöpäätösalgoritmien auditointi oikeudenmukaisuuden varmistamiseksi
- Lääketieteellisten kuvantamismallien diagnosointi lääkäreille
- Säädösten noudattaminen rahoituksen riskinarvioinnissa

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
- [Teoälyn etiikka (AI Ethics)](/en/terms/teoälyn-etiikka-ai-ethics/)
- [Läpinäkyvyys (Transparency)](/en/terms/läpinäkyvyys-transparency/)
