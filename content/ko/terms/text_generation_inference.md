---
title: 텍스트 생성 추론
term_id: text_generation_inference
category: application_paradigms
subcategory: ''
tags:
- inference
- Optimization
- deployment
difficulty: 4
weight: 1
slug: text_generation_inference
date: '2026-07-18T16:18:17.756923Z'
lastmod: '2026-07-18T16:38:06.914468Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 대규모 언어 모델을 효율적으로 대규모로 텍스트를 생성하기 위해 특별히 최적화된 고성능 서빙 엔진입니다.
---
## Definition

텍스트 생성 추론(TGI)은 낮은 지연 시간과 높은 처리량을 위해 대규모 언어 모델(LLM)을 서빙하도록 설계된 전용 소프트웨어 프레임워크입니다. 이 프레임워크는 텍스트 생성 추론 프로세스를 최적화하여

### Summary

대규모 언어 모델을 효율적으로 대규모로 텍스트를 생성하기 위해 특별히 최적화된 고성능 서빙 엔진입니다.

## Key Concepts

- 연속 배치(Continuous Batching)
- 텐서 병렬화(Tensor Parallelism)
- 저지연 서빙(Low Latency Serving)
- LLM 배포(LLM Deployment)

## Use Cases

- 프로덕션 수준의 챗봇 API
- 실시간 콘텐츠 생성 서비스
- 고처리량 텍스트 분석 플랫폼

## Related Terms

- [llm_serving (LLM 서빙)](/en/terms/llm_serving-llm-서빙/)
- [continuous_batching (연속 배치)](/en/terms/continuous_batching-연속-배치/)
- [huggingface_tgi (허깅페이스 TGI)](/en/terms/huggingface_tgi-허깅페이스-tgi/)
- [model_optimization (모델 최적화)](/en/terms/model_optimization-모델-최적화/)
