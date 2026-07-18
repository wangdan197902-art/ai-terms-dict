---
title: "Caching"
term_id: "caching"
category: "engineering_practice"
subcategory: ""
tags: ["optimization", "engineering", "performance"]
difficulty: 2
weight: 1
slug: "caching"
aliases:
  - /en/terms/caching/
date: "2026-07-18T09:48:49.841942Z"
lastmod: "2026-07-18T11:44:44.649866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Caching is a technique of storing frequently accessed data in a temporary, high-speed storage layer to reduce latency and decrease load on primary data sources."
---

## Definition

In AI engineering, caching optimizes performance by keeping recent or frequent query results, model predictions, or intermediate computations in fast memory (like RAM). This reduces the need for expensive recomputation or repeated database queries. Effective cache management strategies, such as Least Recently Used (LRU) eviction policies, ensure that memory usage remains efficient while maximizing throughput for inference engines and data pipelines.

### Summary

Caching is a technique of storing frequently accessed data in a temporary, high-speed storage layer to reduce latency and decrease load on primary data sources.

## Key Concepts

- latency reduction
- memory optimization
- eviction policies
- hit rate

## Use Cases

- Storing model inference results
- Caching database query outputs
- Pre-computing feature embeddings

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

- [Redis](/en/terms/redis/)
- [memcached](/en/terms/memcached/)
- [performance tuning](/en/terms/performance-tuning/)
- [database indexing](/en/terms/database-indexing/)
