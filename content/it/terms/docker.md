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
  - /it/terms/docker/
date: "2026-07-18T15:35:19.962961Z"
lastmod: "2026-07-18T17:15:08.584840Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Docker è una piattaforma per sviluppare, distribuire ed eseguire applicazioni in contenitori leggeri e portatili."
---

## Definition

Docker consente agli sviluppatori di impacchettare un'applicazione con tutte le sue dipendenze in un'unità standardizzata per lo sviluppo software. Questi contenitori isolano il software dall'ambiente circostante, garantendo coerenza

### Summary

Docker è una piattaforma per sviluppare, distribuire ed eseguire applicazioni in contenitori leggeri e portatili.

## Key Concepts

- Containerizzazione
- Immagini
- Isolamento
- Portabilità

## Use Cases

- Distribuzione di modelli ML addestrati come microservizi
- Standardizzazione degli ambienti di sviluppo per team di data science
- Scalabilità dei carichi di lavoro di inferenza nell'infrastruttura cloud

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (orchestrazione di container)](/en/terms/kubernetes-orchestrazione-di-container/)
- [Virtual Machine (macchina virtuale)](/en/terms/virtual-machine-macchina-virtuale/)
- [CI/CD (integrazione e consegna continue)](/en/terms/ci-cd-integrazione-e-consegna-continue/)
- [Microservices (microservizi)](/en/terms/microservices-microservizi/)
