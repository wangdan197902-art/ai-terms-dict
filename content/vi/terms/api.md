---
title: "API"
term_id: "api"
category: "engineering_practice"
subcategory: ""
tags: ["Development", "Integration", "Infrastructure"]
difficulty: 1
weight: 1
slug: "api"
aliases:
  - /vi/terms/api/
date: "2026-07-18T15:22:23.225760Z"
lastmod: "2026-07-18T16:38:07.677340Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Giao diện Lập trình Ứng dụng cho phép các hệ thống phần mềm khác nhau giao tiếp và trao đổi dữ liệu."
---

## Definition

API xác định một bộ các giao thức và công cụ để xây dựng phần mềm và ứng dụng. Trong AI, API cho phép các nhà phát triển truy cập vào các mô hình mạnh mẽ như LLM hoặc trình tạo hình ảnh mà không cần lưu trữ chúng cục bộ.

### Summary

Giao diện Lập trình Ứng dụng cho phép các hệ thống phần mềm khác nhau giao tiếp và trao đổi dữ liệu.

## Key Concepts

- Điểm cuối (Endpoints)
- REST
- Xác thực (Authentication)
- Dữ liệu tải trọng (Payload)

## Use Cases

- Tích hợp chatbot vào trang web
- Truy cập các mô hình ML trên đám mây
- Truy xuất dữ liệu từ các dịch vụ AI

## Code Example

```python
import requests
response = requests.get('https://api.ai.com/v1/generate', headers={'Authorization': 'Bearer token'})
```

## Related Terms

- [REST (Kiến trúc truyền tải trạng thái đại diện)](/en/terms/rest-kiến-trúc-truyền-tải-trạng-thái-đại-diện/)
- [SDK (Bộ công cụ phát triển phần mềm)](/en/terms/sdk-bộ-công-cụ-phát-triển-phần-mềm/)
- [Webhook (Cổng kết nối web)](/en/terms/webhook-cổng-kết-nối-web/)
- [Integration (Tích hợp)](/en/terms/integration-tích-hợp/)
