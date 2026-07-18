---
title: "문장 트랜스포머"
term_id: "sentence_transformers"
category: "training_techniques"
subcategory: ""
tags: ["Deep Learning", "NLP", "Architectures"]
difficulty: 3
weight: 1
slug: "sentence_transformers"
aliases:
  - /ko/terms/sentence_transformers/
date: "2026-07-18T16:15:05.442336Z"
lastmod: "2026-07-18T16:38:06.907065Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "임의의 텍스트 문장에 대해 고정 크기의 벡터 임베딩을 생성하도록 특별히 설계된 신경망 아키텍처입니다."
---

## Definition

문장 트랜스포머는 전통적인 트랜스포머 모델(예: BERT)의 확장으로, 전체 문장에 대해 의미 있는 밀집 벡터 표현을 생성하도록 미세 조정됩니다. 표준 토큰 수준 모델과 달리, 문장 트랜스포머는 문장 전체의 의미를 포착하기 위해 풀링 레이어 등을 사용합니다.

### Summary

임의의 텍스트 문장에 대해 고정 크기의 벡터 임베딩을 생성하도록 특별히 설계된 신경망 아키텍처입니다.

## Key Concepts

- 풀링 레이어
- 대조 학습
- 밀집 임베딩
- 트랜스포머 아키텍처

## Use Cases

- 의미 기반 검색 엔진
- 텍스트 데이터 클러스터링
- 검색 증강 생성(RAG) 파이프라인

## Related Terms

- [BERT (비트)](/en/terms/bert-비트/)
- [Embeddings (임베딩)](/en/terms/embeddings-임베딩/)
- [Sentence Similarity (문장 유사도)](/en/terms/sentence-similarity-문장-유사도/)
- [Contrastive Loss (대조 손실)](/en/terms/contrastive-loss-대조-손실/)
