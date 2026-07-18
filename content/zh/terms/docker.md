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
  - /zh/terms/docker/
date: "2026-07-18T10:59:51.920710Z"
lastmod: "2026-07-18T11:44:45.398963Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "Docker 是一个用于在轻量级、可移植的容器中开发、分发和运行应用程序的平台。"
---

## Definition

Docker 使开发人员能够将应用程序及其所有依赖项打包成一个标准化的软件开发单元。这些容器将软件与其运行环境隔离开来，确保了一致性。

### Summary

Docker 是一个用于在轻量级、可移植的容器中开发、分发和运行应用程序的平台。

## Key Concepts

- 容器化
- 镜像
- 隔离
- 可移植性

## Use Cases

- 作为微服务部署经过训练的机器学习模型
- 为数据科学团队标准化开发环境
- 在云基础设施中扩展推理工作负载

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (K8s，容器编排引擎)](/en/terms/kubernetes-k8s-容器编排引擎/)
- [Virtual Machine (虚拟机，提供硬件级隔离)](/en/terms/virtual-machine-虚拟机-提供硬件级隔离/)
- [CI/CD (持续集成与持续交付)](/en/terms/ci-cd-持续集成与持续交付/)
- [Microservices (微服务架构)](/en/terms/microservices-微服务架构/)
