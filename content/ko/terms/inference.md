---
title: "추론 (Inference)"
term_id: "inference"
category: "engineering_practice"
subcategory: ""
tags: ["Deployment", "Production", "Performance"]
difficulty: 2
weight: 1
slug: "inference"
date: "2026-07-18T15:22:46.628559Z"
lastmod: "2026-07-18T16:38:06.767440Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "훈련된 모델이 새로운 데이터를 처리하여 예측 또는 출력을 생성하는 단계."
---
## Definition

추론은 완성된 모델을 사용하여 보지 못한 데이터에 대해 결정을 내리거나 예측을 수행하는 배포 단계를 의미합니다. 가중치를 업데이트하는 훈련과 달리, 추론은 계산 자원을 소비하며 실시간 응답을 생성합니다.

### Summary

훈련된 모델이 새로운 데이터를 처리하여 예측 또는 출력을 생성하는 단계.

## Key Concepts

- 예측 (Prediction)
- 지연 시간 (Latency)
- 처리량 (Throughput)
- 배포 (Deployment)

## Use Cases

- 은행 거래에서의 실시간 사기 탐지
- 실시간 챗봇 상호작용에서의 응답 생성
- 자율주행 시스템에서의 이미지 분류

## Code Example

```python
import torch
model.eval()
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1)
```

## Related Terms

- [Training (훈련)](/en/terms/training-훈련/)
- [Latency Optimization (지연 시간 최적화)](/en/terms/latency-optimization-지연-시간-최적화/)
- [Batching (배치 처리)](/en/terms/batching-배치-처리/)
- [Model Serving (모델 서빙)](/en/terms/model-serving-모델-서빙/)
