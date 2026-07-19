---
title: "모델 서빙"
term_id: "model_serving"
category: "engineering_practice"
subcategory: ""
tags: ["MLOps", "Infrastructure"]
difficulty: 3
weight: 1
slug: "model_serving"
date: "2026-07-18T15:35:24.509663Z"
lastmod: "2026-07-18T16:38:06.797337Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "훈련된 머신러닝 모델을 프로덕션 환경에 배포하여 최종 사용자에게 예측 또는 출력을 제공하는 과정입니다."
---
## Definition

모델 서빙은 정적으로 훈련된 모델을 가져와 확장 가능한 인프라로 감싸는 작업을 포함합니다. 이 인프라는 들어오는 요청을 처리하고 추론(Inference)을 수행한 후 결과를 반환합니다. 주요 과제에는 관리(문단이 잘려 있어 완전한 번역은 생략됨)가 포함됩니다.

### Summary

훈련된 머신러닝 모델을 프로덕션 환경에 배포하여 최종 사용자에게 예측 또는 출력을 제공하는 과정입니다.

## Key Concepts

- 추론(Inference)
- 지연 시간 최적화(Latency Optimization)
- 확장성(Scalability)
- 배포(Deployment)

## Use Cases

- 실시간 추천 엔진
- 이미지 분류 API
- 자연어 처리 서비스

## Related Terms

- [Inference (추론)](/en/terms/inference-추론/)
- [Deployment (배포)](/en/terms/deployment-배포/)
- [Microservices (마이크로서비스)](/en/terms/microservices-마이크로서비스/)
- [Load Balancing (부하 분산)](/en/terms/load-balancing-부하-분산/)
