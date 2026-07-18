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
  - /de/terms/docker/
date: "2026-07-18T10:58:02.422361Z"
lastmod: "2026-07-18T11:44:44.894022Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Docker ist eine Plattform zur Entwicklung, Verteilung und Ausführung von Anwendungen in leichtgewichtigen, portablen Containern."
---

## Definition

Docker ermöglicht es Entwicklern, eine Anwendung zusammen mit allen ihren Abhängigkeiten in einer standardisierten Einheit für die Softwareentwicklung zu verpacken. Diese Container isolieren die Software von ihrer Umgebung und gewährleisten so konsistente

### Summary

Docker ist eine Plattform zur Entwicklung, Verteilung und Ausführung von Anwendungen in leichtgewichtigen, portablen Containern.

## Key Concepts

- Containerisierung
- Images
- Isolierung
- Portabilität

## Use Cases

- Bereitstellung trainierter ML-Modelle als Microservices
- Standardisierung von Entwicklungsumgebungen für Data-Science-Teams
- Skalierung von Inferenzlasten in der Cloud-Infrastruktur

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orchestrierungsplattform für Container)](/en/terms/kubernetes-orchestrierungsplattform-für-container/)
- [Virtual Machine (Virtuelle Maschine)](/en/terms/virtual-machine-virtuelle-maschine/)
- [CI/CD (Continuous Integration/Continuous Deployment)](/en/terms/ci-cd-continuous-integration-continuous-deployment/)
- [Microservices (Architekturstil)](/en/terms/microservices-architekturstil/)
