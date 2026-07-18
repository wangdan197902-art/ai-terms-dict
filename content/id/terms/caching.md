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
  - /id/terms/caching/
date: "2026-07-18T15:41:31.890521Z"
lastmod: "2026-07-18T16:38:07.435269Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Caching adalah teknik menyimpan data yang sering diakses dalam lapisan penyimpanan sementara berkecepatan tinggi untuk mengurangi latensi dan menurunkan beban pada sumber data utama."
---

## Definition

Dalam rekayasa AI, caching mengoptimalkan kinerja dengan menyimpan hasil kueri terbaru atau sering, prediksi model, atau komputasi perantara dalam memori cepat (seperti RAM). Hal ini mengurangi kebutuhan untuk melakukan perhitungan ulang atau akses ke penyimpanan lambat, sehingga meningkatkan kecepatan respons sistem secara signifikan.

### Summary

Caching adalah teknik menyimpan data yang sering diakses dalam lapisan penyimpanan sementara berkecepatan tinggi untuk mengurangi latensi dan menurunkan beban pada sumber data utama.

## Key Concepts

- pengurangan latensi
- optimasi memori
- kebijakan penghapusan (eviction policies)
- tingkat kecocokan (hit rate)

## Use Cases

- Menyimpan hasil inferensi model
- Menyimpan keluaran kueri basis data
- Pra-menghitung embedding fitur

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

- [Redis (struktur data jaringan)](/en/terms/redis-struktur-data-jaringan/)
- [memcached (sistem caching memori)](/en/terms/memcached-sistem-caching-memori/)
- [performance tuning (penyetelan kinerja)](/en/terms/performance-tuning-penyetelan-kinerja/)
- [database indexing (indeks basis data)](/en/terms/database-indexing-indeks-basis-data/)
