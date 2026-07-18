---
title: "재모수화 트릭"
term_id: "reparameterization_trick"
category: "basic_concepts"
subcategory: ""
tags: ["deep_learning", "probabilistic_models", "optimization"]
difficulty: 4
weight: 1
slug: "reparameterization_trick"
aliases:
  - /ko/terms/reparameterization_trick/
date: "2026-07-18T16:13:19.672922Z"
lastmod: "2026-07-18T16:38:06.904162Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "확률 변수를 학습 가능한 매개변수와 분리하여 변분 추론에서 그래디언트 기반 최적화를 가능하게 하는 기법."
---

## Definition

재모수화 트릭은 변분 오토인코더 및 기타 확률적 모델에서 사용되는 근본적인 방법입니다. 이는 무작위 변수를 결정론적 매개변수와 독립적인 확률 변수의 곱으로 표현함으로써, 확률적 노드를 통해 그래디언트가 흐를 수 있게 합니다.

### Summary

확률 변수를 학습 가능한 매개변수와 분리하여 변분 추론에서 그래디언트 기반 최적화를 가능하게 하는 기법.

## Key Concepts

- 변분 추론
- 그래디언트 추정
- 확률적 노드
- 미분 가능 시뮬레이션

## Use Cases

- 변분 오토인코더(VAE) 학습
- 베이지안 신경망
- 확률적 그래픽 모델

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO (엘보)](/en/terms/elbo-엘보/)
- [Latent Variables (잠재 변수)](/en/terms/latent-variables-잠재-변수/)
- [Backpropagation (역전파)](/en/terms/backpropagation-역전파/)
- [Monte Carlo Estimation (몬테카를로 추정)](/en/terms/monte-carlo-estimation-몬테카를로-추정/)
