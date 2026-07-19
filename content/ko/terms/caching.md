---
title: 캐싱
term_id: caching
category: engineering_practice
subcategory: ''
tags:
- Optimization
- engineering
- performance
difficulty: 2
weight: 1
slug: caching
date: '2026-07-18T15:44:39.805502Z'
lastmod: '2026-07-18T16:38:06.815610Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 캐싱은 지연 시간을 줄이고 주요 데이터 소스의 부하를 감소시키기 위해 자주 접근하는 데이터를 임시 고속 저장 계층에 저장하는
  기술입니다.
---
## Definition

AI 엔지니어링에서 캐싱은 최근 또는 빈번하게 쿼리된 결과, 모델 예측값 또는 중간 연산 결과를 빠른 메모리(RAM 등)에 유지하여 성능을 최적화합니다. 이는 고비용의 원본 데이터 소스 재조회나 복잡한 연산을 반복 수행해야 하는 필요성을 줄여줍니다.

### Summary

캐싱은 지연 시간을 줄이고 주요 데이터 소스의 부하를 감소시키기 위해 자주 접근하는 데이터를 임시 고속 저장 계층에 저장하는 기술입니다.

## Key Concepts

- 지연 시간 감소
- 메모리 최적화
- 퇴거 정책(Eviction Policies)
- 히트 레이트(Hit Rate)

## Use Cases

- 모델 추론 결과 저장
- 데이터베이스 쿼리 출력 캐싱
- 특징 임베딩 사전 계산

## Code Example

```python
import redis

# Simple caching example
r = redis.Redis(host='localhost', port=6379, db=0)

def get_prediction(model_id, input_data):
    cache_key = f"pred_{model_id}_{hash(str(input_data))}"
    result = r.get(cache_key)
    if result:
        return result.decode('utf-8')
    # Compute if not cached
    prediction = model.predict(input_data)
    r.setex(cache_key, 3600, str(prediction))
    return prediction
```

## Related Terms

- [Redis (인메모리 데이터 구조 저장소)](/en/terms/redis-인메모리-데이터-구조-저장소/)
- [memcached (분산 메모리 캐싱 시스템)](/en/terms/memcached-분산-메모리-캐싱-시스템/)
- [performance tuning (성능 튜닝)](/en/terms/performance-tuning-성능-튜닝/)
- [database indexing (데이터베이스 인덱싱)](/en/terms/database-indexing-데이터베이스-인덱싱/)
