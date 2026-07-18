---
title: "View"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /en/terms/view/
date: "2026-07-18T09:37:52.960858Z"
lastmod: "2026-07-18T11:44:44.614589Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A virtual table in a database resulting from a stored query, presenting data from one or more tables without storing it physically."
---

## Definition

In database management, a view acts as a saved SQL query that behaves like a table but contains no data itself. It provides a simplified or customized perspective of underlying data, enhancing security by restricting access to specific columns. Views simplify complex joins and aggregations for users, allowing them to interact with structured data representations without needing to understand the base schema's complexity.

### Summary

A virtual table in a database resulting from a stored query, presenting data from one or more tables without storing it physically.

## Key Concepts

- Virtual Table
- SQL Query
- Data Abstraction
- Security

## Use Cases

- Creating simplified reports for non-technical users
- Restricting access to sensitive columns in a table
- Standardizing complex join logic across applications

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table](/en/terms/table/)
- [Query](/en/terms/query/)
- [Schema](/en/terms/schema/)
- [Materialized View](/en/terms/materialized-view/)
