---
title: "가지치기(Pruning)"
term_id: "pruning"
category: "training_techniques"
subcategory: ""
tags: ["compression", "efficiency", "deployment"]
difficulty: 3
weight: 1
slug: "pruning"
date: "2026-07-18T16:11:35.913373Z"
lastmod: "2026-07-18T16:38:06.899901Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델의 크기를 줄이고 추론 속도를 향상시키기 위해 중복되거나 중요도가 낮은 매개변수를 제거하는 모델 압축 기술입니다."
---
## Definition

가지치기는 신경망에서 출력 정확도에 거의 기여하지 않는 뉴런, 연결 또는 필터를 식별하고 제거하는 과정입니다. 이러한 중복 요소를 제거함으로써 모델의 파라미터 수와 계산량을 대폭 줄일 수 있으며, 이는 모델의 경량화와 추론 속도 향상에 직접적으로 기여합니다. 밀집된(dense) 모델을 희소한(sparse) 구조로 변환하여 효율성을 높이는 것이 핵심 목표입니다.

### Summary

모델의 크기를 줄이고 추론 속도를 향상시키기 위해 중복되거나 중요도가 낮은 매개변수를 제거하는 모델 압축 기술입니다.

## Key Concepts

- 모델 압축(Model Compression)
- 중복 제거(Redundancy Removal)
- 추론 가속(Inference Acceleration)
- 희소성(Sparsity)

## Use Cases

- 모바일 AI 배포(Mobile AI Deployment)
- 엣지 컴퓨팅 최적화(Edge Computing Optimization)
- 클라우드 추론 비용 절감(Reducing Cloud Inference Costs)

## Related Terms

- [양자화(Quantization) (정밀도를 낮춰 메모리 사용량 감소)](/en/terms/양자화-quantization-정밀도를-낮춰-메모리-사용량-감소/)
- [지식 증류(Knowledge Distillation) (큰 모델의 지식을 작은 모델로 전달)](/en/terms/지식-증류-knowledge-distillation-큰-모델의-지식을-작은-모델로-전달/)
- [모델 압축(Model Compression) (모델 크기와 복잡도 줄이는 기술)](/en/terms/모델-압축-model-compression-모델-크기와-복잡도-줄이는-기술/)
- [희소 네트워크(Sparse Networks) (많은 가중치가 0인 신경망)](/en/terms/희소-네트워크-sparse-networks-많은-가중치가-0인-신경망/)
