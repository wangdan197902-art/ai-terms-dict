---
title: "عرض"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /ar/terms/view/
date: "2026-07-18T15:32:03.809898Z"
lastmod: "2026-07-18T17:15:08.452504Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "جدول افتراضي في قاعدة البيانات ناتج عن استعلام محفوظ، يعرض البيانات من جدول واحد أو أكثر دون تخزينها فعلياً."
---

## Definition

في إدارة قواعد البيانات، يعمل العرض كاستعلام SQL محفوظ يتصرف كجدول ولكنه لا يحتوي على بيانات بحد ذاته. ويوفر منظوراً مبسطاً أو مخصصاً للبيانات الأساسية، مما يعزز الأمان وسهولة الاستخدام.

### Summary

جدول افتراضي في قاعدة البيانات ناتج عن استعلام محفوظ، يعرض البيانات من جدول واحد أو أكثر دون تخزينها فعلياً.

## Key Concepts

- جدول افتراضي
- استعلام SQL
- مجردية البيانات
- الأمان

## Use Cases

- إنشاء تقارير مبسطة للمستخدمين غير الفنيين
- تقييد الوصول إلى أعمدة حساسة في الجدول
- توحيد منطق الانضمام المعقد عبر التطبيقات

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (جدول)](/en/terms/table-جدول/)
- [Query (استعلام)](/en/terms/query-استعلام/)
- [Schema (مخطط)](/en/terms/schema-مخطط/)
- [Materialized View (عرض مادي)](/en/terms/materialized-view-عرض-مادي/)
