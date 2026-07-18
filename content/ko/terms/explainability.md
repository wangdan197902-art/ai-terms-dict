---
title: "설명 가능성"
term_id: "explainability"
category: "ethics_safety"
subcategory: ""
tags: ["AI Ethics", "Model Interpretation", "Safety"]
difficulty: 4
weight: 1
slug: "explainability"
aliases:
  - /ko/terms/explainability/
date: "2026-07-18T15:34:19.126506Z"
lastmod: "2026-07-18T16:38:06.794834Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "설명 가능성은 인간이 AI 모델이 내린 결정의 원인을 이해할 수 있는 정도를 의미합니다."
---

## Definition

이 개념은 SHAP이나 LIME과 같은 기법을 통해 모델이 특정 예측에 도달하는 방식을 시각화함으로써 복잡한 AI 시스템의 '블랙박스' 문제를 해결합니다. 이는 모델의 의사결정 과정을 투명하게 만들어 신뢰를 높이는 데 기여합니다.

### Summary

설명 가능성은 인간이 AI 모델이 내린 결정의 원인을 이해할 수 있는 정도를 의미합니다.

## Key Concepts

- 해석 가능성
- 블랙박스 문제
- 신뢰
- 편향 감지

## Use Cases

- 대출 승인 알고리즘의 공정성 감사
- 임상가를 위한 의료 영상 모델 진단
- 금융 위험 평가에서의 규제 준수

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
- [AI Ethics (AI 윤리)](/en/terms/ai-ethics-ai-윤리/)
- [Transparency (투명성)](/en/terms/transparency-투명성/)
