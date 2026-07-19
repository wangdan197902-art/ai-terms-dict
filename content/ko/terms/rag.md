---
title: 검색 증강 생성
term_id: rag
category: application_paradigms
subcategory: ''
tags:
- architecture
- Knowledge Management
difficulty: 4
weight: 1
slug: rag
date: '2026-07-18T15:28:25.409722Z'
lastmod: '2026-07-18T16:38:06.782698Z'
draft: false
source: agnes_llm
status: published
language: ko
description: RAG는 응답을 생성하기 전에 외부 지식 베이스에서 관련 정보를 검색하여 생성형 AI 모델을 보완하는 프레임워크입니다.
---
## Definition

검색 증강 생성(Retrieval-Augmented Generation, RAG)은 검색 기반 AI 시스템과 생성 기반 AI 시스템의 강점을 결합합니다. 사전 훈련된 언어 모델의 파라미터에만 의존하는 대신, RAG는 먼저 사용자의 쿼리와 관련된 외부 데이터 소스(예: 벡터 데이터베이스)에서 정보를 검색한 후, 이를 컨텍스트로 활용하여 생성 모델을 통해 정확하고 최신의 응답을 만들어냅니다.

### Summary

RAG는 응답을 생성하기 전에 외부 지식 베이스에서 관련 정보를 검색하여 생성형 AI 모델을 보완하는 프레임워크입니다.

## Key Concepts

- 벡터 데이터베이스(Vector Database)
- 임베딩(Embeddings)
- 컨텍스트 윈도우(Context Window)
- 시맨틱 검색(Semantic Search)

## Use Cases

- 기업용 지식 베이스(Enterprise knowledge bases)
- 고객 지원 봇(Customer support bots)
- 연구 보조 도구(Research assistants)

## Related Terms

- [벡터 검색(Vector Search, 의미적 유사성을 기반으로 한 데이터 검색)](/en/terms/벡터-검색-vector-search-의미적-유사성을-기반으로-한-데이터-검색/)
- [지식 그래프(Knowledge Graph, 엔티티 간 관계를 구조화한 데이터 모델)](/en/terms/지식-그래프-knowledge-graph-엔티티-간-관계를-구조화한-데이터-모델/)
- [LLM(Large Language Model, 대규모 언어 모델)](/en/terms/llm-large-language-model-대규모-언어-모델/)
