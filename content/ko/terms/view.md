---
title: "뷰(가상 테이블)"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
date: "2026-07-18T15:31:05.711712Z"
lastmod: "2026-07-18T16:38:06.787526Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "저장된 쿼리의 결과인 데이터베이스의 가상 테이블로, 물리적으로 저장하지 않고 하나 이상의 테이블에서 데이터를 제시합니다."
---
## Definition

데이터베이스 관리에서 뷰는 테이블처럼 동작하지만 자체 데이터는 포함하지 않는 저장된 SQL 쿼리입니다. 이는 기본 데이터에 대한 단순화되거나 사용자 정의된 관점을 제공하여 보안을 강화합니다.

### Summary

저장된 쿼리의 결과인 데이터베이스의 가상 테이블로, 물리적으로 저장하지 않고 하나 이상의 테이블에서 데이터를 제시합니다.

## Key Concepts

- 가상 테이블
- SQL 쿼리
- 데이터 추상화
- 보안

## Use Cases

- 비기술적 사용자를 위한 간소화된 보고서 생성
- 테이블의 민감한 열에 대한 접근 제한
- 애플리케이션 전반에 복잡한 조인 로직 표준화

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (테이블)](/en/terms/table-테이블/)
- [Query (쿼리)](/en/terms/query-쿼리/)
- [Schema (스키마)](/en/terms/schema-스키마/)
- [Materialized View (물리화 뷰)](/en/terms/materialized-view-물리화-뷰/)
