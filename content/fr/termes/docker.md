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
  - /fr/terms/docker/
date: "2026-07-18T10:59:31.646555Z"
lastmod: "2026-07-18T11:44:45.183697Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "Docker est une plateforme pour développer, distribuer et exécuter des applications dans des conteneurs légers et portables."
---

## Definition

Docker permet aux développeurs d'emballer une application avec toutes ses dépendances dans une unité standardisée pour le développement logiciel. Ces conteneurs isolent le logiciel de son environnement, garantissant une cohérence.

### Summary

Docker est une plateforme pour développer, distribuer et exécuter des applications dans des conteneurs légers et portables.

## Key Concepts

- Conteneurisation
- Images
- Isolation
- Portabilité

## Use Cases

- Déploiement de modèles ML entraînés en tant que microservices
- Standardisation des environnements de développement pour les équipes de data science
- Mise à l'échelle des charges de travail d'inférence dans l'infrastructure cloud

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orchestration de conteneurs)](/en/terms/kubernetes-orchestration-de-conteneurs/)
- [Machine Virtuelle (VM)](/en/terms/machine-virtuelle-vm/)
- [CI/CD (Intégration et déploiement continus)](/en/terms/ci-cd-intégration-et-déploiement-continus/)
- [Microservices](/en/terms/microservices/)
