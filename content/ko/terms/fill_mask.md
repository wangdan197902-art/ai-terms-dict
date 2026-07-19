---
title: 마스크 채우기
term_id: fill_mask
category: basic_concepts
subcategory: ''
tags:
- NLP
- pretraining
- transformers
difficulty: 2
weight: 1
slug: fill_mask
date: '2026-07-18T15:55:47.592325Z'
lastmod: '2026-07-18T16:38:06.840796Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 모델이 문장 내 주변 맥락을 바탕으로 누락된 토큰을 예측하는 자연어 처리 작업입니다.
---
## Definition

마스크 채우기는 BERT와 같은 트랜스포머 기반 모델에서 사용되는 기본 사전 학습 목적 함수입니다. 이 과정은 텍스트 시퀀스에서 무작위 토큰을 마스킹하고 모델이 원래 토큰을 예측하도록 훈련시키는 것을 포함합니다.

### Summary

모델이 문장 내 주변 맥락을 바탕으로 누락된 토큰을 예측하는 자연어 처리 작업입니다.

## Key Concepts

- 마스킹 언어 모델링
- 맥락 이해
- 자기 지도 학습
- 토큰 예측

## Use Cases

- 텍스트 완성
- 의미적 역할 레이블링
- 사전 학습의 기초

## Related Terms

- [BERT (바이디렉셔널 인코더 레프리젠테이션 from 트랜스포머)](/en/terms/bert-바이디렉셔널-인코더-레프리젠테이션-from-트랜스포머/)
- [Masked Language Model (마스킹 언어 모델)](/en/terms/masked-language-model-마스킹-언어-모델/)
- [Transformer (트랜스포머)](/en/terms/transformer-트랜스포머/)
- [Tokenization (토큰화)](/en/terms/tokenization-토큰화/)
