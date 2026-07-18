---
title: "어댑터"
term_id: "adapter"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers", "optimization"]
difficulty: 4
weight: 1
slug: "adapter"
aliases:
  - /ko/terms/adapter/
date: "2026-07-18T15:33:36.473810Z"
lastmod: "2026-07-18T16:38:06.792707Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "사전 학습된 모델에 삽입되어 특정 하류 작업을 위해 효율적인 파인튜닝을 가능하게 하는 경량 모듈입니다."
---

## Definition

어댑터는 주로 대규모 언어 모델과 트랜스포머에서 사용되는 매개변수 효율적인 파인튜닝 기법입니다. 계산 비용이 많이 드는 모든 모델 가중치를 업데이트하는 대신, 어댑터는 고정된 사전 학습된 모델의 일부 레이어 사이에 작은 신경망 모듈을 삽입하여 새로운 작업에 맞게 미세 조정합니다. 이를 통해 전체 모델을 재학습하지 않고도 효율적으로 도메인 특화 성능을 향상시킬 수 있습니다.

### Summary

사전 학습된 모델에 삽입되어 특정 하류 작업을 위해 효율적인 파인튜닝을 가능하게 하는 경량 모듈입니다.

## Key Concepts

- 매개변수 효율적 파인튜닝
- 전이 학습
- 모듈형 아키텍처
- 파괴적 망각

## Use Cases

- 고객 서비스 챗봇을 위한 LLM 파인튜닝
- 의료 영상 분석을 위한 비전 모델 적응
- 여러 도메인별 모델을 효율적으로 배포

## Related Terms

- [LoRA (저랭크 어댑션)](/en/terms/lora-저랭크-어댑션/)
- [프롬프트 튜닝](/en/terms/프롬프트-튜닝/)
- [파인튜닝](/en/terms/파인튜닝/)
- [트랜스포머](/en/terms/트랜스포머/)
