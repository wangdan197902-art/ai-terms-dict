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
  - /cs/terms/docker/
date: "2026-07-18T15:35:06.072730Z"
lastmod: "2026-07-18T17:15:09.088705Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Docker je platforma pro vývoj, distribuci a spouštění aplikací v lehkých, přenosných kontejnerech."
---

## Definition

Docker umožňuje vývojářům zabalit aplikaci se všemi jejími závislostmi do standardizované jednotky pro softwarový vývoj. Tyto kontejnery izolují software od jeho prostředí, což zajišťuje konzistentní chování napříč různými systémy.

### Summary

Docker je platforma pro vývoj, distribuci a spouštění aplikací v lehkých, přenosných kontejnerech.

## Key Concepts

- Kontejnerizace
- Obrazy
- Izolace
- Přenositelnost

## Use Cases

- Nasazování natrénovaných ML modelů jako mikroslužeb
- Standardizace vývojových prostředí pro týmy datové vědy
- Škálování zátěže při inferenci v cloudu

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (orchestrace kontejnerů)](/en/terms/kubernetes-orchestrace-kontejnerů/)
- [Virtual Machine (virtuální stroj)](/en/terms/virtual-machine-virtuální-stroj/)
- [CI/CD (nepřetržitá integrace a dodávka)](/en/terms/ci-cd-nepřetržitá-integrace-a-dodávka/)
- [Microservices (mikroslužby)](/en/terms/microservices-mikroslužby/)
