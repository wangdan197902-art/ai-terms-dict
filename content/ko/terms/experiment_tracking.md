---
title: "실험 추적"
term_id: "experiment_tracking"
category: "engineering_practice"
subcategory: ""
tags: ["MLOps", "Engineering", "Best Practices"]
difficulty: 2
weight: 1
slug: "experiment_tracking"
date: "2026-07-18T15:55:04.752715Z"
lastmod: "2026-07-18T16:38:06.838732Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "재현성을 보장하고 비교를 용이하게 하기 위해 머신러닝 실험에서 메타데이터, 지표 및 아티팩트를 체계적으로 기록하는 과정."
---
## Definition

이 관행은 훈련 실행 중 하이퍼파라미터, 데이터셋 버전, 모델 아키텍처 및 성능 지표를 로깅하는 것을 포함합니다. 이를 통해 데이터 과학자들은 서로 다른 실험 구성을 비교하고, 가장 우수한 모델을 선별하며, 실험 결과를 재현할 수 있습니다.

### Summary

재현성을 보장하고 비교를 용이하게 하기 위해 머신러닝 실험에서 메타데이터, 지표 및 아티팩트를 체계적으로 기록하는 과정.

## Key Concepts

- 재현성
- 하이퍼파라미터 로깅
- 아티팩트 관리
- 버전 관리

## Use Cases

- 서로 다른 하이퍼파라미터 설정 간 모델 성능 비교
- 로깅된 지표를 검토하여 훈련 실패 원인 디버깅
- 공유 실험을 통해 팀원들과 협업

## Related Terms

- [MLflow (MLflow 도구)](/en/terms/mlflow-mlflow-도구/)
- [Model Registry (모델 레지스트리)](/en/terms/model-registry-모델-레지스트리/)
- [Hyperparameter Tuning (하이퍼파라미터 튜닝)](/en/terms/hyperparameter-tuning-하이퍼파라미터-튜닝/)
- [Data Versioning (데이터 버전 관리)](/en/terms/data-versioning-데이터-버전-관리/)
