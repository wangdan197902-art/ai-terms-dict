---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:35:52.087297Z"
lastmod: "2026-07-18T17:15:08.703517Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Docker is een platform voor het ontwikkelen, distribueren en uitvoeren van applicaties in lichte, draagbare containers."
---
## Definition

Docker stelt ontwikkelaars in staat om een applicatie samen met alle afhankelijkheden te verpakken in een gestandaardiseerde eenheid voor softwareontwikkeling. Deze containers isoleren software van de omgeving, wat zorgt voor consistentie.

### Summary

Docker is een platform voor het ontwikkelen, distribueren en uitvoeren van applicaties in lichte, draagbare containers.

## Key Concepts

- Containerisatie
- Afbeeldingen
- Isolatie
- Draagbaarheid

## Use Cases

- Het implementeren van getrainde ML-modellen als microservices
- Het standaardiseren van ontwikkelomgevingen voor datascience-teams
- Het schalen van inferentiewerklasten in cloud-infrastructuur

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (container-orkestratieplatform)](/en/terms/kubernetes-container-orkestratieplatform/)
- [Virtual Machine (virtuele machine)](/en/terms/virtual-machine-virtuele-machine/)
- [CI/CD (Continuous Integration/Continuous Delivery)](/en/terms/ci-cd-continuous-integration-continuous-delivery/)
- [Microservices (architectuurstijl)](/en/terms/microservices-architectuurstijl/)
