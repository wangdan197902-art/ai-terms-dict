---
title: Webhook
term_id: webhook
category: engineering_practice
subcategory: ''
tags:
- Integration
- API
- Automation
difficulty: 3
weight: 1
slug: webhook
date: '2026-07-18T16:16:23.163061Z'
lastmod: '2026-07-18T16:38:07.816976Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một lệnh gọi lại HTTP do người dùng xác định, được kích hoạt bởi các
  sự kiện cụ thể, cho phép các hệ thống đẩy thông báo thời gian thực đến các ứng dụng
  khác.
---
## Definition

Webhook là một cơ chế cho phép một dịch vụ cung cấp thông tin thời gian thực cho một dịch vụ khác khi một sự kiện xảy ra. Thay vì phải liên tục truy vấn (polling) để kiểm tra các thay đổi, hệ thống nguồn sẽ gửi một yêu cầu HTTP POST đến một URL cụ thể mà hệ thống đích đã đăng ký trước đó. Điều này giúp tiết kiệm tài nguyên và đảm bảo dữ liệu được cập nhật ngay lập tức khi có sự kiện mới.

### Summary

Một lệnh gọi lại HTTP do người dùng xác định, được kích hoạt bởi các sự kiện cụ thể, cho phép các hệ thống đẩy thông báo thời gian thực đến các ứng dụng khác.

## Key Concepts

- Theo hướng sự kiện
- Yêu cầu HTTP POST
- URL gọi lại
- Thông báo đẩy

## Use Cases

- Triển khai tự động CI/CD
- Thông báo cổng thanh toán
- Tích hợp bot Slack

## Related Terms

- [API (Giao diện lập trình ứng dụng)](/en/terms/api-giao-diện-lập-trình-ứng-dụng/)
- [Event-driven architecture (Kiến trúc hướng sự kiện)](/en/terms/event-driven-architecture-kiến-trúc-hướng-sự-kiện/)
- [REST (Kiến trúc truyền trạng thái đại diện)](/en/terms/rest-kiến-trúc-truyền-trạng-thái-đại-diện/)
- [Integration (Tích hợp)](/en/terms/integration-tích-hợp/)
