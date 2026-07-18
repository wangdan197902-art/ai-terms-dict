---
title: "Bảng nhìn (View)"
term_id: "view"
category: "basic_concepts"
subcategory: ""
tags: ["Database", "SQL", "Data Management"]
difficulty: 2
weight: 1
slug: "view"
aliases:
  - /vi/terms/view/
date: "2026-07-18T15:30:09.265248Z"
lastmod: "2026-07-18T16:38:07.699235Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một bảng ảo trong cơ sở dữ liệu, kết quả của một truy vấn đã lưu, hiển thị dữ liệu từ một hoặc nhiều bảng mà không lưu trữ vật lý."
---

## Definition

Trong quản lý cơ sở dữ liệu, một bảng nhìn hoạt động như một truy vấn SQL đã được lưu, hoạt động giống như một bảng nhưng không chứa dữ liệu thực tế. Nó cung cấp một góc nhìn đơn giản hóa hoặc tùy chỉnh đối với dữ liệu nền tảng, tăng cường bảo mật.

### Summary

Một bảng ảo trong cơ sở dữ liệu, kết quả của một truy vấn đã lưu, hiển thị dữ liệu từ một hoặc nhiều bảng mà không lưu trữ vật lý.

## Key Concepts

- Bảng ảo
- Truy vấn SQL
- Trừu tượng hóa dữ liệu
- Bảo mật

## Use Cases

- Tạo báo cáo đơn giản cho người dùng không kỹ thuật
- Hạn chế truy cập vào các cột nhạy cảm trong bảng
- Chuẩn hóa logic JOIN phức tạp xuyên suốt các ứng dụng

## Code Example

```python
CREATE VIEW ActiveUsers AS SELECT id, name FROM users WHERE status = 'active';
```

## Related Terms

- [Table (Bảng)](/en/terms/table-bảng/)
- [Query (Truy vấn)](/en/terms/query-truy-vấn/)
- [Schema (Cấu trúc dữ liệu)](/en/terms/schema-cấu-trúc-dữ-liệu/)
- [Materialized View (Bảng nhìn vật chất hóa)](/en/terms/materialized-view-bảng-nhìn-vật-chất-hóa/)
