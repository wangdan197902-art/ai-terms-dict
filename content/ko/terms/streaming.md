---
title: 스트리밍
term_id: streaming
category: engineering_practice
subcategory: ''
tags:
- Data Engineering
- Real Time
- infrastructure
difficulty: 2
weight: 1
slug: streaming
date: '2026-07-18T16:17:21.908058Z'
lastmod: '2026-07-18T16:38:06.911668Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 정보를 대규모의 정적 배치(batch)로 처리하는 대신, 도착하는 대로 작은 단위로 지속적으로 처리하는 데이터 처리 패러다임.
---
## Definition

스트리밍은 데이터가 생성되는 실시간 또는 준실시간으로 데이터를 지속적으로 흡수하고 처리하는 것을 의미합니다. 고정된 데이터셋을 처리하는 배치 처리와 달리, 스트리밍 시스템은 무한한 데이터 흐름을 관리하며, 낮은 지연 시간과 증분 업데이트를 통해 즉각적인 인사이트를 제공합니다.

### Summary

정보를 대규모의 정적 배치(batch)로 처리하는 대신, 도착하는 대로 작은 단위로 지속적으로 처리하는 데이터 처리 패러다임.

## Key Concepts

- 실시간 처리
- 증분 업데이트
- 낮은 지연 시간(Low latency)
- 무한 데이터(Unbounded data)

## Use Cases

- 금융 거래의 실시간 사기 탐지
- IoT 시스템의 실시간 센서 데이터 모니터링
- 동적 콘텐츠 추천 피드 제공

## Related Terms

- [배치 처리 (Batch processing): 일괄 처리 방식](/en/terms/배치-처리-batch-processing-일괄-처리-방식/)
- [Apache Kafka: 분산 이벤트 스트리밍 플랫폼](/en/terms/apache-kafka-분산-이벤트-스트리밍-플랫폼/)
- [이벤트 기반 아키텍처 (Event-driven architecture): 이벤트 발생 시 반응하는 시스템 설계](/en/terms/이벤트-기반-아키텍처-event-driven-architecture-이벤트-발생-시-반응하는-시스템-설계/)
- [스트림 처리 (Stream processing): 데이터 스트림을 실시간으로 처리하는 기술](/en/terms/스트림-처리-stream-processing-데이터-스트림을-실시간으로-처리하는-기술/)
