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
  - /es/terms/docker/
date: "2026-07-18T10:30:15.631887Z"
lastmod: "2026-07-18T11:44:44.761726Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores ligeros y portátiles."
---

## Definition

Docker permite a los desarrolladores empaquetar una aplicación junto con todas sus dependencias en una unidad estandarizada para el desarrollo de software. Estos contenedores aíslan el software de su entorno, asegurando consistencia en diferentes entornos de ejecución.

### Summary

Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores ligeros y portátiles.

## Key Concepts

- Contenedorización
- Imágenes
- Aislamiento
- Portabilidad

## Use Cases

- Despliegue de modelos de ML entrenados como microservicios
- Estandarización de entornos de desarrollo para equipos de ciencia de datos
- Escalado de cargas de trabajo de inferencia en infraestructura en la nube

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (orquestación de contenedores)](/en/terms/kubernetes-orquestación-de-contenedores/)
- [Máquina Virtual (entorno virtualizado completo)](/en/terms/máquina-virtual-entorno-virtualizado-completo/)
- [CI/CD (integración y entrega continuas)](/en/terms/ci-cd-integración-y-entrega-continuas/)
- [Microservicios (arquitectura de software)](/en/terms/microservicios-arquitectura-de-software/)
