---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:36:50.390763Z"
lastmod: "2026-07-18T16:38:06.957605Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Docker er en plattform for å utvikle, levere og kjøre applikasjoner i lette, bærbara containere."
---
## Definition

Docker gjør det mulig for utviklere å pakke inn en applikasjon sammen med alle avhengighetene i en standardisert enhet for programvareutvikling. Disse containerne isolerer programvaren fra miljøet, noe som sikrer konsistens.

### Summary

Docker er en plattform for å utvikle, levere og kjøre applikasjoner i lette, bærbara containere.

## Key Concepts

- Containerisering
- Images
- Isolasjon
- Bærekraft

## Use Cases

- Utplassering av trent ML-modeller som mikrotjenester
- Standardisering av utviklingsmiljøer for datavitenskapsteam
- Skalering av inferensarbeidsbelastninger i skyinfrastruktur

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orkestreringsplattform for containere)](/en/terms/kubernetes-orkestreringsplattform-for-containere/)
- [Virtual Machine (Virtuell maskin)](/en/terms/virtual-machine-virtuell-maskin/)
- [CI/CD (Kontinuerlig integrasjon og levering)](/en/terms/ci-cd-kontinuerlig-integrasjon-og-levering/)
- [Microservices (Mikrotjenestearkitektur)](/en/terms/microservices-mikrotjenestearkitektur/)
