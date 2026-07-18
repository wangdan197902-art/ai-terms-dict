---
title: "缓存"
term_id: "caching"
category: "engineering_practice"
subcategory: ""
tags: ["optimization", "engineering", "performance"]
difficulty: 2
weight: 1
slug: "caching"
aliases:
  - /zh/terms/caching/
date: "2026-07-18T11:09:42.288234Z"
lastmod: "2026-07-18T11:44:45.453941Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "缓存是一种将频繁访问的数据存储在临时高速存储层中的技术，旨在降低延迟并减少主数据源的负载。"
---

## Definition

在AI工程中，缓存通过将最近或频繁的查询结果、模型预测或中间计算保留在快速内存（如RAM）中来优化性能。这减少了昂贵的主数据存储访问需求，从而显著提升系统响应速度。

### Summary

缓存是一种将频繁访问的数据存储在临时高速存储层中的技术，旨在降低延迟并减少主数据源的负载。

## Key Concepts

- 延迟降低
- 内存优化
- 驱逐策略
- 命中率

## Use Cases

- 存储模型推理结果
- 缓存数据库查询输出
- 预计算特征嵌入

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

- [Redis (内存数据结构存储)](/en/terms/redis-内存数据结构存储/)
- [memcached (分布式内存缓存系统)](/en/terms/memcached-分布式内存缓存系统/)
- [performance tuning (性能调优)](/en/terms/performance-tuning-性能调优/)
- [database indexing (数据库索引)](/en/terms/database-indexing-数据库索引/)
