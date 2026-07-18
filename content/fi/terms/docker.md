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
  - /fi/terms/docker/
date: "2026-07-18T15:36:04.965350Z"
lastmod: "2026-07-18T17:15:09.369391Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Docker on alusta sovellusten kehittämiseen, jakeluun ja suorittamiseen kevyissä, kannettavissa konteissa."
---

## Definition

Docker mahdollistaa kehittäjien pakata sovellus sen kaikkien riippuvuuksien kanssa standardoiduksi yksiköksi ohjelmistokehitystä varten. Nämä kontit eristävät ohjelmiston ympäristöstään, varmistaen johdonmukaisuuden eri ympäristöissä.

### Summary

Docker on alusta sovellusten kehittämiseen, jakeluun ja suorittamiseen kevyissä, kannettavissa konteissa.

## Key Concepts

- Konttiteknologia
- Kuvat (Images)
- Eristäminen
- Kannettavuus

## Use Cases

- Koulutettujen koneoppimismallien käyttöönotto mikropalveluina
- Data science -tiimien kehitysympäristöjen standardointi
- Johtopäätösten teon (inference) kuormien skaalaus pilviinfrastruktuurissa

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (konttien orkesterointialusta)](/en/terms/kubernetes-konttien-orkesterointialusta/)
- [Virtual Machine (virtuaalikone)](/en/terms/virtual-machine-virtuaalikone/)
- [CI/CD (jatkuva integraatio ja toimittaminen)](/en/terms/ci-cd-jatkuva-integraatio-ja-toimittaminen/)
- [Microservices (mikropalveluarkkitehtuuri)](/en/terms/microservices-mikropalveluarkkitehtuuri/)
