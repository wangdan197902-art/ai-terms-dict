---
title: ExBERT
term_id: exbert
category: basic_concepts
subcategory: ''
tags:
- NLP
- interpretability
- transformers
difficulty: 4
weight: 1
slug: exbert
date: '2026-07-18T15:55:04.752691Z'
lastmod: '2026-07-18T16:38:06.838385Z'
draft: false
source: agnes_llm
status: published
language: ko
description: BERT의 예측을 설명하기 위해 특정 출력에 가장 기여하는 어텐션 헤드와 레이어를 식별하는 방법론.
---
## Definition

ExBERT는 서로 다른 레이어에 걸쳐 개별 어텐션 헤드의 중요성을 분석하여 BERT 트랜스포머 모델에 대한 해석 가능성을 제공합니다. 이는 그래디언트 기반 귀속 기법 등을 사용하여 모델의 내부 작동 원리를 이해하는 데 도움을 줍니다.

### Summary

BERT의 예측을 설명하기 위해 특정 출력에 가장 기여하는 어텐션 헤드와 레이어를 식별하는 방법론.

## Key Concepts

- 어텐션 헤드
- 모델 해석 가능성
- 그래디언트 귀속
- 트랜스포머 아키텍처

## Use Cases

- NLP 모델 디버깅
- 구문 처리 대 의미 처리 이해
- 의료 텍스트 분석에서의 설명 가능한 AI(XAI)

## Related Terms

- [bert (BERT 모델)](/en/terms/bert-bert-모델/)
- [attention_mechanism (어텐션 메커니즘)](/en/terms/attention_mechanism-어텐션-메커니즘/)
- [explainable_ai (설명 가능한 AI)](/en/terms/explainable_ai-설명-가능한-ai/)
- [transformer_models (트랜스포머 모델)](/en/terms/transformer_models-트랜스포머-모델/)
