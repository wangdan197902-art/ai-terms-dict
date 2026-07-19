---
title: 프롬프트 튜닝(Prompt Tuning)
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T16:10:59.879444Z'
lastmod: '2026-07-18T16:38:06.899629Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 모델 가중치 전체를 업데이트하는 대신 연속적인 입력 임베딩을 최적화하는 매개변수 효율적인 파인튜닝 방법입니다.
---
## Definition

프롬프트 튜닝은 사전 훈련된 언어 모델의 입력 레이어에 학습 가능한 소프트 프롬프트(연속 벡터)를 추가하고, 기본 모델 파라미터는 고정된 상태로 유지합니다. 이 접근 방식은

### Summary

모델 가중치 전체를 업데이트하는 대신 연속적인 입력 임베딩을 최적화하는 매개변수 효율적인 파인튜닝 방법입니다.

## Key Concepts

- 소프트 프롬프트(soft prompts)
- 매개변수 효율성(parameter efficiency)
- 고정 가중치(frozen weights)
- 소수 학습(few-shot learning)

## Use Cases

- 특정 도메인에 맞춰 대규모 언어 모델(LLM) 적응
- 저자원 파인튜닝(Low-resource fine-tuning)
- 멀티태스크 학습 최적화

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning, 매개변수 효율적 파인튜닝)](/en/terms/peft-parameter-efficient-fine-tuning-매개변수-효율적-파인튜닝/)
- [LoRA (Low-Rank Adaptation, 저랭크 적응)](/en/terms/lora-low-rank-adaptation-저랭크-적응/)
- [in-context learning (컨텍스트 내 학습)](/en/terms/in-context-learning-컨텍스트-내-학습/)
- [fine-tuning (파인튜닝)](/en/terms/fine-tuning-파인튜닝/)
