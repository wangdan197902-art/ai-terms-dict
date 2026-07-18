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
  - /ro/terms/docker/
date: "2026-07-18T15:35:38.176632Z"
lastmod: "2026-07-18T17:15:09.613470Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Docker este o platformă pentru dezvoltarea, livrarea și rularea aplicațiilor în containere ușoare și portabile."
---

## Definition

Docker permite dezvoltatorilor să împacheteze o aplicație împreună cu toate dependențele sale într-o unitate standardizată pentru dezvoltarea software-ului. Aceste containere izolează software-ul de mediul său, asigurând consistența în diferite medii de execuție.

### Summary

Docker este o platformă pentru dezvoltarea, livrarea și rularea aplicațiilor în containere ușoare și portabile.

## Key Concepts

- Containerizare
- Imagini
- Izolare
- Portabilitate

## Use Cases

- Implementarea modelelor ML antrenate ca microservicii
- Standardizarea mediilor de dezvoltare pentru echipele de știință a datelor
- Scalarea sarcinilor de inferență în infrastructura cloud

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (orchestrare de containere)](/en/terms/kubernetes-orchestrare-de-containere/)
- [Virtual Machine (mașină virtuală)](/en/terms/virtual-machine-mașină-virtuală/)
- [CI/CD (integrare și livrare continue)](/en/terms/ci-cd-integrare-și-livrare-continue/)
- [Microservices (arhitectură de microservicii)](/en/terms/microservices-arhitectură-de-microservicii/)
