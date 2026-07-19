---
title: "LoRA(저랭크 어댑테이션)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:28.689538Z"
lastmod: "2026-07-18T16:38:06.777597Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "기존 모델 가중치에 학습 가능한 저랭크 분해 행렬을 주입하여 파라미터 효율적인 파인튜닝을 수행하는 방법입니다."
---
## Definition

LoRA는 사전 학습된 모델 가중치를 고정하고 트랜스포머 아키텍처의 각 레이어에 학습 가능한 분해 행렬을 삽입합니다. 이러한 저랭크 행렬만 최적화함으로써 LoRA는 계산 비용과 메모리 사용량을 크게 줄입니다.

### Summary

기존 모델 가중치에 학습 가능한 저랭크 분해 행렬을 주입하여 파라미터 효율적인 파인튜닝을 수행하는 방법입니다.

## Key Concepts

- 파라미터 효율적 파인튜닝(Parameter-Efficient Fine-Tuning)
- 랭크 분해(Rank Decomposition)
- 가중치 고정(Freezing Weights)
- 어댑터 모듈(Adapter Modules)

## Use Cases

- 대규모 언어 모델(LLM) 사용자 정의(Customizing LLMs)
- 도메인 특화 적응(Domain-Specific Adaptation)
- 자원 제약 환경에서의 훈련(Resource-Constrained Training)

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (파라미터 효율적 파인튜닝 기법)](/en/terms/peft-파라미터-효율적-파인튜닝-기법/)
- [Fine-Tuning (미세 조정: 사전 학습 모델을 특정 작업에 맞게 조정)](/en/terms/fine-tuning-미세-조정-사전-학습-모델을-특정-작업에-맞게-조정/)
- [Quantization (양자화: 모델 정밀도를 낮춰 효율성 향상)](/en/terms/quantization-양자화-모델-정밀도를-낮춰-효율성-향상/)
