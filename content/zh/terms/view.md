---
title: "视图（View）"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /zh/terms/view/
date: "2026-07-18T10:55:52.609817Z"
lastmod: "2026-07-18T11:44:45.388537Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "数据库中由存储查询生成的虚拟表，展示来自一个或多个表的数据，但不物理存储这些数据。"
---

## Definition

在数据库管理中，视图表现为一个保存的 SQL 查询，其行为像表一样，但本身不包含数据。它为底层数据提供简化或定制的视角，从而增强安全性并简化复杂查询。

### Summary

数据库中由存储查询生成的虚拟表，展示来自一个或多个表的数据，但不物理存储这些数据。

## Key Concepts

- 虚拟表
- SQL 查询
- 数据抽象
- 安全性

## Use Cases

- 为非技术用户创建简化的报表
- 限制对表中敏感列的访问
- 在应用程序间标准化复杂的连接逻辑

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (表)](/en/terms/table-表/)
- [Query (查询)](/en/terms/query-查询/)
- [Schema (模式/架构)](/en/terms/schema-模式-架构/)
- [Materialized View (物化视图)](/en/terms/materialized-view-物化视图/)
