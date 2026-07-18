---
title: "모델 압축"
term_id: "model_compression"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Deployment", "Efficiency"]
difficulty: 3
weight: 1
slug: "model_compression"
aliases:
  - /ko/terms/model_compression/
date: "2026-07-18T16:06:06.322184Z"
lastmod: "2026-07-18T16:38:06.886052Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델 압축은 머신러닝 모델의 크기와 계산 요구 사항을 줄이는 기법을 의미합니다."
---

## Definition

이 범주에는 모델의 용량을 줄이면서도 성능을 유지하는 것을 목표로 하는 가지치기(Pruning), 양자화(Quantization), 지식 증류(Knowledge Distillation) 등의 방법이 포함됩니다. 이는 복잡한 AI 모델을 배포하는 데 필수적입니다.

### Summary

모델 압축은 머신러닝 모델의 크기와 계산 요구 사항을 줄이는 기법을 의미합니다.

## Key Concepts

- 양자화
- 가지치기
- 지식 증류
- 추론 속도

## Use Cases

- 모바일 기기에서 모델 배포
- 클라우드 추론 비용 절감
- 실시간 비디오 처리 가속화

## Code Example

```python
import torch.quantization as quant
model = quant.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
```

## Related Terms

- [Quantization (양자화)](/en/terms/quantization-양자화/)
- [Pruning (가지치기)](/en/terms/pruning-가지치기/)
- [Distillation (지식 증류)](/en/terms/distillation-지식-증류/)
- [Edge AI (엣지 AI)](/en/terms/edge-ai-엣지-ai/)
