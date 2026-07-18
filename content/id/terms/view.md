---
title: "Tampilan"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /id/terms/view/
date: "2026-07-18T15:30:47.227138Z"
lastmod: "2026-07-18T16:38:07.406751Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Tabel virtual dalam basis data yang dihasilkan dari kueri yang disimpan, menyajikan data dari satu atau lebih tabel tanpa menyimpannya secara fisik."
---

## Definition

Dalam manajemen basis data, tampilan bertindak sebagai kueri SQL yang disimpan yang berperilaku seperti tabel tetapi tidak berisi data itu sendiri. Ini memberikan perspektif yang disederhanakan atau disesuaikan atas data dasar, meningkatkan keamanan.

### Summary

Tabel virtual dalam basis data yang dihasilkan dari kueri yang disimpan, menyajikan data dari satu atau lebih tabel tanpa menyimpannya secara fisik.

## Key Concepts

- Tabel Virtual
- Kueri SQL
- Abstraksi Data
- Keamanan

## Use Cases

- Membuat laporan sederhana untuk pengguna non-teknis
- Membatasi akses ke kolom sensitif dalam tabel
- Menstandarkan logika penggabungan kompleks di seluruh aplikasi

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (Tabel fisik)](/en/terms/table-tabel-fisik/)
- [Query (Kueri)](/en/terms/query-kueri/)
- [Schema (Skema)](/en/terms/schema-skema/)
- [Materialized View (Tampilan termaterialisasi)](/en/terms/materialized-view-tampilan-termaterialisasi/)
