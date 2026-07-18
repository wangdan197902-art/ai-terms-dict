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
  - /th/terms/view/
date: "2026-07-18T15:31:38.957787Z"
lastmod: "2026-07-18T16:38:07.552866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ตารางเสมือนในฐานข้อมูลที่เกิดจากการสอบถามที่บันทึกไว้ นำเสนอข้อมูลจากหนึ่งตารางหรือมากกว่าโดยไม่จัดเก็บข้อมูลนั้นทางกายภาพ"
---

## Definition

ในการจัดการฐานข้อมูล View ทำหน้าที่เป็นการสอบถาม SQL ที่บันทึกไว้ซึ่งทำงานเหมือนตารางแต่ไม่เก็บข้อมูลเอง ให้มุมมองที่เรียบง่ายหรือปรับแต่งของข้อมูลพื้นฐาน ช่วยเพิ่มความปลอดภัย

### Summary

ตารางเสมือนในฐานข้อมูลที่เกิดจากการสอบถามที่บันทึกไว้ นำเสนอข้อมูลจากหนึ่งตารางหรือมากกว่าโดยไม่จัดเก็บข้อมูลนั้นทางกายภาพ

## Key Concepts

- ตารางเสมือน (Virtual Table)
- การสอบถาม SQL (SQL Query)
- นามธรรมของข้อมูล (Data Abstraction)
- ความปลอดภัย (Security)

## Use Cases

- สร้างรายงานที่เรียบง่ายสำหรับผู้ใช้งานทั่วไป
- จำกัดการเข้าถึงคอลัมน์ที่ละเอียดอ่อนในตาราง
- มาตรฐานตรรกะการเชื่อมต่อข้อมูลที่ซับซ้อนข้ามแอปพลิเคชัน

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (ตาราง)](/en/terms/table-ตาราง/)
- [Query (การสอบถาม)](/en/terms/query-การสอบถาม/)
- [Schema (แผนภาพฐานข้อมูล)](/en/terms/schema-แผนภาพฐานข-อม-ล/)
- [Materialized View (ตารางเสมือนแบบถาวร)](/en/terms/materialized-view-ตารางเสม-อนแบบถาวร/)
