---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
aliases:
  - /vi/terms/docker/
date: "2026-07-18T15:34:34.619218Z"
lastmod: "2026-07-18T16:38:07.708144Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Docker là một nền tảng để phát triển, phân phối và chạy các ứng dụng trong các container nhẹ và di động."
---

## Definition

Docker cho phép các nhà phát triển đóng gói một ứng dụng cùng với tất cả các phụ thuộc của nó vào một đơn vị chuẩn hóa cho phát triển phần mềm. Các container này cô lập phần mềm khỏi môi trường của nó, đảm bảo tính nhất quán.

### Summary

Docker là một nền tảng để phát triển, phân phối và chạy các ứng dụng trong các container nhẹ và di động.

## Key Concepts

- Container hóa
- Hình ảnh (Images)
- Cô lập
- Khả năng di động

## Use Cases

- Triển khai các mô hình ML đã huấn luyện dưới dạng vi dịch vụ (microservices)
- Chuẩn hóa môi trường phát triển cho các nhóm khoa học dữ liệu
- Mở rộng quy mô tải lượng suy luận (inference) trên cơ sở hạ tầng đám mây

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Hệ thống điều khiển container)](/en/terms/kubernetes-hệ-thống-điều-khiển-container/)
- [Virtual Machine (Máy ảo)](/en/terms/virtual-machine-máy-ảo/)
- [CI/CD (Tích hợp liên tục/Giới thiệu liên tục)](/en/terms/ci-cd-tích-hợp-liên-tục-giới-thiệu-liên-tục/)
- [Microservices (Kiến trúc vi dịch vụ)](/en/terms/microservices-kiến-trúc-vi-dịch-vụ/)
