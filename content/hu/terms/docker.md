---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:37:49.779304Z"
lastmod: "2026-07-18T17:15:09.739906Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A Docker egy platform alkalmazások fejlesztésére, terjesztésére és futtatására könnyűsúlyú, hordozható konténerekben."
---
## Definition

A Docker lehetővé teszi a fejlesztők számára, hogy az alkalmazást minden függőségével együtt szabványosított egységbe csomagolják a szoftverfejlesztéshez. Ezek a konténerek elszigetelik a szoftvert a környezetétől, biztosítva a konzisztenciát.

### Summary

A Docker egy platform alkalmazások fejlesztésére, terjesztésére és futtatására könnyűsúlyú, hordozható konténerekben.

## Key Concepts

- Konténerizáció
- Képek (Images)
- Elzárás (Isolation)
- Hordozhatóság

## Use Cases

- Betanított gépi tanulási modellek mikroszolgáltatásként történő telepítése
- Fejlesztői környezetek standardizálása adat tudományi csapatok számára
- Inferencia terhelések skálázása felhőinfrastruktúrában

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (konténer-orchestráció)](/en/terms/kubernetes-konténer-orchestráció/)
- [Virtual Machine (virtuális gép)](/en/terms/virtual-machine-virtuális-gép/)
- [CI/CD (folyamatos integráció és folyamatos kiszállítás)](/en/terms/ci-cd-folyamatos-integráció-és-folyamatos-kiszállítás/)
- [Microservices (mikroszolgáltatások)](/en/terms/microservices-mikroszolgáltatások/)
