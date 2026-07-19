---
title: "최대 내적 검색"
term_id: "maximum_inner_product_search"
category: "application_paradigms"
subcategory: ""
tags: ["search", "algorithms", "recommendations"]
difficulty: 4
weight: 1
slug: "maximum_inner_product_search"
date: "2026-07-18T16:04:42.477683Z"
lastmod: "2026-07-18T16:38:06.883581Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "쿼리 벡터에 대해 가장 높은 내적(dot product) 값을 갖는 항목을 검색하는 특수화된 벡터 유사도 검색 기법입니다."
---
## Definition

최대 내적 검색(MIPS)은 정보 검색 및 머신 러닝, 특히 추천 시스템에서 근본적인 문제입니다. 표준 코사인 유사도 검색이 방향성만 고려하는 반면, MIPS는 벡터의 크기(magnitude)와 방향을 모두 고려하여 내적 값을 최대화하는 항목을 찾습니다. 이는 사용자 선호도와 아이템 특성 간의 절대적인 관련성 강도를 측정하는 데 유용하며, 바이어스 보정이 필요한 의미론적 검색이나 인기 기반 콘텐츠 랭킹에 널리 적용됩니다.

### Summary

쿼리 벡터에 대해 가장 높은 내적(dot product) 값을 갖는 항목을 검색하는 특수화된 벡터 유사도 검색 기법입니다.

## Key Concepts

- 내적
- 벡터 유사도
- 추천 시스템
- 근접 이웃 검색

## Use Cases

- 개인화된 제품 추천
- 인기도 기반 콘텐츠 랭킹
- 바이어스 보정이 있는 의미론적 검색

## Related Terms

- [cosine_similarity (코사인 유사도)](/en/terms/cosine_similarity-코사인-유사도/)
- [vector_database (벡터 데이터베이스)](/en/terms/vector_database-벡터-데이터베이스/)
- [nearest_neighbor_search (근접 이웃 검색)](/en/terms/nearest_neighbor_search-근접-이웃-검색/)
- [embedding (임베딩)](/en/terms/embedding-임베딩/)
