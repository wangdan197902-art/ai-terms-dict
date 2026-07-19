---
title: "AI 관측 가능성"
term_id: "ai_observability"
category: "engineering_practice"
subcategory: ""
tags: ["mlops", "monitoring", "engineering"]
difficulty: 4
weight: 1
slug: "ai_observability"
date: "2026-07-18T15:39:27.677233Z"
lastmod: "2026-07-18T16:38:06.804164Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "로그, 메트릭, 트레이스를 통해 머신러닝 시스템의 내부 상태를 모니터링하고 이해하는 관행."
---
## Definition

AI 관측 가능성은 전통적인 소프트웨어 모니터링을 확장하여 머신러닝 시스템의 고유한 도전 과제에 대응합니다. 이는 실시간으로 모델 성능, 데이터 드리프트, 추론 지연 시간 등을 추적하여 시스템의 건강 상태와 예측 신뢰도를 파악하는 것을 포함합니다.

### Summary

로그, 메트릭, 트레이스를 통해 머신러닝 시스템의 내부 상태를 모니터링하고 이해하는 관행.

## Key Concepts

- 데이터 드리프트
- 모델 모니터링
- 텔레메트리
- 디버깅

## Use Cases

- 운영 중인 모델의 컨셉 드리프트 감지
- 낮은 신뢰도의 예측 결과 문제 해결
- AI 서비스의 SLA(서비스 수준 계약) 준수 보장

## Code Example

```python
import mlflow

# Log metrics during training
mlflow.log_metric('accuracy', 0.95)
mlflow.log_metric('loss', 0.05)

# Track model parameters
mlflow.log_param('learning_rate', 0.01)
mlflow.log_param('epochs', 10)
```

## Related Terms

- [MLOps (머신러닝 운영: 머신러닝 모델의 배포 및 유지 관리 프로세스)](/en/terms/mlops-머신러닝-운영-머신러닝-모델의-배포-및-유지-관리-프로세스/)
- [Model Drift (모델 드리프트: 시간이 지남에 따라 모델 성능이 저하되는 현상)](/en/terms/model-drift-모델-드리프트-시간이-지남에-따라-모델-성능이-저하되는-현상/)
- [System Monitoring (시스템 모니터링: IT 인프라 및 애플리케이션의 상태 관찰)](/en/terms/system-monitoring-시스템-모니터링-it-인프라-및-애플리케이션의-상태-관찰/)
- [Telemetry (텔레메트리: 원격 측정 데이터 수집 및 전송 기술)](/en/terms/telemetry-텔레메트리-원격-측정-데이터-수집-및-전송-기술/)
