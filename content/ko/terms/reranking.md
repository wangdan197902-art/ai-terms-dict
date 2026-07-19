---
title: "재랭킹(Reranking)"
term_id: "reranking"
category: "application_paradigms"
subcategory: ""
tags: ["search", "recommendations", "architecture"]
difficulty: 2
weight: 1
slug: "reranking"
date: "2026-07-18T16:13:33.742976Z"
lastmod: "2026-07-18T16:38:06.904425Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "초기 coarse ranking을 더 계산 비용이 큰 모델로 정제하여 결과의 관련성을 향상시키는 두 단계 검색 프로세스입니다."
---
## Definition

재랭킹은 정보 검색 및 추천 시스템에서 정확도를 높이기 위해 사용되는 전략입니다. 먼저 빠르지만 정확도가 낮은 모델이 대규모 후보 집합을 검색합니다. 그런 다음 더 느리지만 정교한 모델이 이 후보들을 재순위 매겨 최종 결과를 최적화합니다.

### Summary

초기 coarse ranking을 더 계산 비용이 큰 모델로 정제하여 결과의 관련성을 향상시키는 두 단계 검색 프로세스입니다.

## Key Concepts

- 이층 검색(Two-Tier Retrieval)
- 후보 생성(Candidate Generation)
- 크로스 어텐션(Cross-Attention)
- 정밀도 최적화(Precision Optimization)

## Use Cases

- 검색 엔진(Search Engines)
- 추천 시스템(Recommendation Systems)
- 검색 증강 생성(Retrieval-Augmented Generation, RAG)

## Related Terms

- [Vector Search (벡터 검색)](/en/terms/vector-search-벡터-검색/)
- [BM25 (BM25 알고리즘)](/en/terms/bm25-bm25-알고리즘/)
- [Cross-Encoder (크로스 인코더)](/en/terms/cross-encoder-크로스-인코더/)
- [Information Retrieval (정보 검색)](/en/terms/information-retrieval-정보-검색/)
