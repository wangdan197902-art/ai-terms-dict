---
title: "도커"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:34:04.841951Z"
lastmod: "2026-07-18T16:38:06.794286Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "경량이고 이식 가능한 컨테이너 내에서 애플리케이션을 개발, 배포 및 실행하기 위한 플랫폼입니다."
---
## Definition

도커는 개발자가 애플리케이션과 모든 의존성을 소프트웨어 개발을 위한 표준화된 단위인 컨테이너로 패키징할 수 있게 합니다. 이러한 컨테이너는 소프트웨어를 환경으로부터 격리시켜 일관성을 보장합니다.

### Summary

경량이고 이식 가능한 컨테이너 내에서 애플리케이션을 개발, 배포 및 실행하기 위한 플랫폼입니다.

## Key Concepts

- 컨테이너화
- 이미지
- 격리
- 이식성

## Use Cases

- 학습된 ML 모델을 마이크로서비스로 배포
- 데이터 사이언스 팀을 위한 개발 환경 표준화
- 클라우드 인프라에서 추론 부하 확장

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (쿠버네티스)](/en/terms/kubernetes-쿠버네티스/)
- [Virtual Machine (가상 머신)](/en/terms/virtual-machine-가상-머신/)
- [CI/CD (지속적 통합/지속적 배포)](/en/terms/ci-cd-지속적-통합-지속적-배포/)
- [Microservices (마이크로서비스)](/en/terms/microservices-마이크로서비스/)
