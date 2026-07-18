---
title: "Görünüm (View)"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /tr/terms/view/
date: "2026-07-18T15:30:49.875104Z"
lastmod: "2026-07-18T16:38:07.247907Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Bir veya daha fazla tablodan veri sunan ancak bunları fiziksel olarak depolamayan, saklı bir sorgudan kaynaklanan sanal bir tablo."
---

## Definition

Veritabanı yönetiminde bir görünüm, kendisi veri içermeyen ancak bir tablo gibi davranan kaydedilmiş bir SQL sorgusu olarak hareket eder. Altta yatan verilere basitleştirilmiş veya özelleştirilmiş bir bakış açısı sağlayarak güvenliği artırır.

### Summary

Bir veya daha fazla tablodan veri sunan ancak bunları fiziksel olarak depolamayan, saklı bir sorgudan kaynaklanan sanal bir tablo.

## Key Concepts

- Sanal Tablo
- SQL Sorgusu
- Veri Soyutlama
- Güvenlik

## Use Cases

- Teknik olmayan kullanıcılar için basitleştirilmiş raporlar oluşturma
- Bir tabloda hassas sütunlara erişimi kısıtlama
- Uygulamalar arasında karmaşık birleştirme mantığını standartlaştırma

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (Tablo)](/en/terms/table-tablo/)
- [Query (Sorgu)](/en/terms/query-sorgu/)
- [Schema (Şema)](/en/terms/schema-şema/)
- [Materialized View (Matrice Görünüm)](/en/terms/materialized-view-matrice-görünüm/)
