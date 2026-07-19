---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T09:40:59.276999Z"
lastmod: "2026-07-18T11:44:44.623644Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Docker is a platform for developing, shipping, and running applications in lightweight, portable containers."
---
## Definition

Docker enables developers to package an application with all its dependencies into a standardized unit for software development. These containers isolate software from its environment, ensuring consistent performance across different computing environments. By abstracting away the underlying infrastructure, Docker simplifies deployment, scaling, and management of AI models and services, reducing the 'it works on my machine' problem common in complex machine learning pipelines.

### Summary

Docker is a platform for developing, shipping, and running applications in lightweight, portable containers.

## Key Concepts

- Containerization
- Images
- Isolation
- Portability

## Use Cases

- Deploying trained ML models as microservices
- Standardizing development environments for data science teams
- Scaling inference workloads in cloud infrastructure

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes](/en/terms/kubernetes/)
- [Virtual Machine](/en/terms/virtual-machine/)
- [CI/CD](/en/terms/ci-cd/)
- [Microservices](/en/terms/microservices/)
