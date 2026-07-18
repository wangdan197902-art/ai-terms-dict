---
title: "Khả năng quan sát AI"
term_id: "ai_observability"
category: "engineering_practice"
subcategory: ""
tags: ["mlops", "monitoring", "engineering"]
difficulty: 4
weight: 1
slug: "ai_observability"
aliases:
  - /vi/terms/ai_observability/
date: "2026-07-18T15:38:31.999798Z"
lastmod: "2026-07-18T16:38:07.721751Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Thực tiễn giám sát và hiểu trạng thái bên trong của các hệ thống học máy thông qua nhật ký (logs), chỉ số (metrics) và dấu vết (traces)."
---

## Definition

Khả năng quan sát AI mở rộng việc giám sát phần mềm truyền thống để giải quyết các thách thức độc đáo của các hệ thống học máy. Nó liên quan đến việc theo dõi hiệu suất mô hình, sự trôi dạt dữ liệu và độ trễ suy luận theo thời gian thực, cho phép các nhà phát triển hiểu rõ hơn về hành vi của mô hình trong môi trường sản xuất.

### Summary

Thực tiễn giám sát và hiểu trạng thái bên trong của các hệ thống học máy thông qua nhật ký (logs), chỉ số (metrics) và dấu vết (traces).

## Key Concepts

- Sự trôi dạt dữ liệu (Data drift)
- Giám sát mô hình
- Dữ liệu telemetery
- Gỡ lỗi

## Use Cases

- Phát hiện sự trôi dạt khái niệm trong các mô hình sản xuất
- Khắc phục sự cố các dự đoán có độ tin cậy thấp
- Đảm bảo tuân thủ các thỏa thuận mức dịch vụ (SLA) cho các dịch vụ AI

## Code Example

```python
import mlflow

# Log metrics during training
mlflow.log_metric('accuracy', 0.95)
mlflow.log_metric('loss', 0.05)

# Track model parameters
mlflow.log_param('learning_rate', 0.01)
mlflow.log_param('epochs', 10)
```

## Related Terms

- [MLOps (Vận hành học máy)](/en/terms/mlops-vận-hành-học-máy/)
- [Model Drift (Sự trôi dạt mô hình)](/en/terms/model-drift-sự-trôi-dạt-mô-hình/)
- [System Monitoring (Giám sát hệ thống)](/en/terms/system-monitoring-giám-sát-hệ-thống/)
- [Telemetry (Dữ liệu telemetery)](/en/terms/telemetry-dữ-liệu-telemetery/)
