---
title: two-stage
term_id: two_stage
category: basic_concepts
subcategory: ''
tags:
- architecture
- Computer Vision
difficulty: 3
weight: 1
slug: two_stage
date: '2026-07-18T15:33:17.801038Z'
lastmod: '2026-07-18T16:38:07.253534Z'
draft: false
source: agnes_llm
status: published
language: tr
description: İşlemin distinct (belirgin), ardışık fazlarda gerçekleştiği bir boru
  hattı mimarisi.
---
## Definition

İki aşamalı mimariler, karmaşık bir görevi iki ayrı adıma böler; genellikle tespit (detection) ardından sınıflandırma veya iyileştirme gelir. Bilgisayarlı görüde, nesne algılayıcılar (örneğin Faster R-CNN) ilk aşamada olası nesne bölgelerini önerir, ikinci aşamada ise bu bölgeleri sınıflandırır.

### Summary

İşlemin distinct (belirgin), ardışık fazlarda gerçekleştiği bir boru hattı mimarisi.

## Key Concepts

- Ardışık işleme
- Bölge önerisi
- Modülerlik
- Boru hattı (Pipeline)

## Use Cases

- Nesne tespiti (örn. Faster R-CNN)
- Yüz tanıma boru hatları
- LLM'lerde çok adımlı akıl yürütme

## Related Terms

- [single_stage (tek aşamalı)](/en/terms/single_stage-tek-aşamalı/)
- [object_detection (nesne tespiti)](/en/terms/object_detection-nesne-tespiti/)
- [pipeline (boru hattı/iş akışı)](/en/terms/pipeline-boru-hattı-iş-akışı/)
