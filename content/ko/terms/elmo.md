---
title: "ELMo(Embeddings from Language Models)"
term_id: "elmo"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "Embeddings", "History"]
difficulty: 3
weight: 1
slug: "elmo"
date: "2026-07-18T15:53:50.594643Z"
lastmod: "2026-07-18T16:38:06.834870Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "양방향 LSTM을 사용하여 심층 문맥 기반 단어 표현을 생성하는 임베딩 방법."
---
## Definition

ELMo는 대규모 코퍼스에서 훈련된 양방향 LSTM을 통해 입력 텍스트를 처리하여 문맥 민감한 단어 임베딩을 생성합니다. Word2Vec과 같은 정적 임베딩과 달리, ELMo는 단어가 사용되는 문맥에 따라 다른 표현을 생성함으로써 다의성(polysemy) 문제를 해결합니다.

### Summary

양방향 LSTM을 사용하여 심층 문맥 기반 단어 표현을 생성하는 임베딩 방법.

## Key Concepts

- 문맥 기반 임베딩(Contextual Embeddings)
- 양방향 LSTM(Bidirectional LSTM)
- 사전 훈련(Pre-training)
- 다의성(Polysemy)

## Use Cases

- 감성 분석(Sentiment Analysis)
- 고유명사 식별(Named Entity Recognition)
- 코레퍼런스 해결(Coreference Resolution)

## Related Terms

- [Word2Vec - 단어의 정적 벡터 표현을 학습하는 대표적인 알고리즘](/en/terms/word2vec-단어의-정적-벡터-표현을-학습하는-대표적인-알고리즘/)
- [BERT - 문맥 기반 언어 모델을 활용한 트랜스포머 아키텍처](/en/terms/bert-문맥-기반-언어-모델을-활용한-트랜스포머-아키텍처/)
- [트랜스포머(Transformer) - 어텐션 메커니즘을 기반으로 하는 신경망 아키텍처](/en/terms/트랜스포머-transformer-어텐션-메커니즘을-기반으로-하는-신경망-아키텍처/)
- [언어 모델링(Language Modeling) - 텍스트의 다음 단어를 예측하거나 확률을 계산하는 작업](/en/terms/언어-모델링-language-modeling-텍스트의-다음-단어를-예측하거나-확률을-계산하는-작업/)
