---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:34:56.413668Z"
lastmod: "2026-07-18T17:15:09.243631Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Docker er en platform til udvikling, distribution og kørsel af applikationer i letvægts, bærbare containere."
---
## Definition

Docker gør det muligt for udviklere at pakke en applikation sammen med alle dens afhængigheder ind i en standardiseret enhed til softwareudvikling. Disse containere isolerer softwaren fra dens miljø, hvilket sikrer konsistens.

### Summary

Docker er en platform til udvikling, distribution og kørsel af applikationer i letvægts, bærbare containere.

## Key Concepts

- Containerisering
- Images
- Isolering
- Bæredygtighed

## Use Cases

- Udrulning af træningsmodeller som mikrotjenester
- Standardisering af udviklingsmiljøer for datavidenskabshold
- Skalering af inferensarbejdsbyrder i skyinfrastruktur

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orkestreringsplatform til containere)](/en/terms/kubernetes-orkestreringsplatform-til-containere/)
- [Virtual Machine (Virtuel maskine)](/en/terms/virtual-machine-virtuel-maskine/)
- [CI/CD (Continuous Integration/Continuous Deployment)](/en/terms/ci-cd-continuous-integration-continuous-deployment/)
- [Microservices (Mikrotjenestearkitektur)](/en/terms/microservices-mikrotjenestearkitektur/)
