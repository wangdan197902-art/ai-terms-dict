---
title: "Explainability"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
date: "2026-07-18T15:34:15.539817Z"
lastmod: "2026-07-18T16:38:07.413192Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Explainability mengacu pada tingkat di mana manusia dapat memahami penyebab keputusan yang dibuat oleh model AI."
---
## Definition

Konsep ini mengatasi masalah 'kotak hitam' dalam sistem AI kompleks dengan memberikan wawasan tentang bagaimana model mencapai prediksi tertentu. Teknik seperti SHAP atau LIME membantu memvisualisasikan pentingnya fitur dalam pengambilan keputusan.

### Summary

Explainability mengacu pada tingkat di mana manusia dapat memahami penyebab keputusan yang dibuat oleh model AI.

## Key Concepts

- Interpretabilitas
- Masalah Kotak Hitam
- Kepercayaan
- Deteksi Bias

## Use Cases

- Mengevaluasi algoritmo persetujuan pinjaman untuk keadilan
- Mendiagnosis model pencitraan medis bagi klinisi
- Kepatuhan regulasi dalam penilaian risiko keuangan

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
- [AI Ethics (Etika AI)](/en/terms/ai-ethics-etika-ai/)
- [Transparency (Transparansi)](/en/terms/transparency-transparansi/)
