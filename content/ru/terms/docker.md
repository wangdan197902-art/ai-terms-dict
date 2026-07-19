---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:33:45.940842Z"
lastmod: "2026-07-18T16:38:07.101076Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ru"
description: "Docker — это платформа для разработки, развертывания и запуска приложений в легких переносимых контейнерах."
---
## Definition

Docker позволяет разработчикам упаковывать приложение со всеми его зависимостями в стандартизированный модуль для разработки программного обеспечения. Эти контейнеры изолируют программное обеспечение от окружающей среды, обеспечивая согласованность работы на разных машинах.

### Summary

Docker — это платформа для разработки, развертывания и запуска приложений в легких переносимых контейнерах.

## Key Concepts

- Контейнеризация
- Образы (Images)
- Изоляция
- Переносимость

## Use Cases

- Развертывание обученных моделей машинного обучения в виде микросервисов
- Стандартизация сред разработки для команд специалистов по данным
- Масштабирование нагрузок при выводе моделей (inference) в облачной инфраструктуре

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (система оркестрации контейнеров)](/en/terms/kubernetes-система-оркестрации-контейнеров/)
- [Virtual Machine (виртуальная машина)](/en/terms/virtual-machine-виртуальная-машина/)
- [CI/CD (непрерывная интеграция и непрерывная доставка)](/en/terms/ci-cd-непрерывная-интеграция-и-непрерывная-доставка/)
- [Microservices (микросервисная архитектура)](/en/terms/microservices-микросервисная-архитектура/)
