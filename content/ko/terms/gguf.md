---
title: GGUF
term_id: gguf
category: basic_concepts
subcategory: ''
tags:
- format
- Optimization
- Local LLM
difficulty: 3
weight: 1
slug: gguf
date: '2026-07-18T15:56:26.472598Z'
lastmod: '2026-07-18T16:38:06.842737Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 로컬 하드웨어에서 양자화된 대형 언어 모델을 효율적으로 저장하고 로드하기 위해gger.ai가 개발한 파일 형식.
---
## Definition

GGUF(GPT-Generated Unified Format)는 소비자용 하드웨어에서 대형 언어 모델을 실행하도록 특별히 설계된 바이너리 파일 형식입니다. 다양한 양자화 기법을 지원하여 모델의 메모리 사용량을 줄이고 추론 속도를 높이며, 로컬 환경에서도 고성능의 LLM을 원활하게 구동할 수 있게 합니다.

### Summary

로컬 하드웨어에서 양자화된 대형 언어 모델을 효율적으로 저장하고 로드하기 위해gger.ai가 개발한 파일 형식.

## Key Concepts

- 양자화 (Quantization)
- 모델 직렬화 (Model Serialization)
- 로컬 추론 (Local Inference)
- 메모리 최적화 (Memory Optimization)

## Use Cases

- 노트북이나 데스크탑에서 LLM 로컬 실행
- 자원이 제한된 엣지 디바이스에 모델 배포
- 오픈소스 커뮤니티에서 최적화된 모델 가중치 공유

## Related Terms

- [LLAMA.cpp (GGUF 형식을 주로 사용하는 C++ 라이브러리)](/en/terms/llama-cpp-gguf-형식을-주로-사용하는-c-라이브러리/)
- [양자화 (Quantization)](/en/terms/양자화-quantization/)
- [ONNX (Open Neural Network Exchange)](/en/terms/onnx-open-neural-network-exchange/)
- [모델 가중치 (Model Weights)](/en/terms/모델-가중치-model-weights/)
