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
  - /pt/terms/docker/
date: "2026-07-18T14:43:55.449200Z"
lastmod: "2026-07-18T15:51:59.449012Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "O Docker é uma plataforma para desenvolver, enviar e executar aplicativos em contêineres leves e portáteis."
---

## Definition

O Docker permite que os desenvolvedores empacotem um aplicativo com todas as suas dependências em uma unidade padronizada para desenvolvimento de software. Esses contêineres isolam o software de seu ambiente, garantindo consistência entre diferentes sistemas.

### Summary

O Docker é uma plataforma para desenvolver, enviar e executar aplicativos em contêineres leves e portáteis.

## Key Concepts

- Contêinerização
- Imagens
- Isolamento
- Portabilidade

## Use Cases

- Implantação de modelos de ML treinados como microsserviços
- Padronização de ambientes de desenvolvimento para equipes de ciência de dados
- Escalonamento de cargas de trabalho de inferência na infraestrutura em nuvem

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orquestração de contêineres)](/en/terms/kubernetes-orquestração-de-contêineres/)
- [Virtual Machine (Máquina Virtual)](/en/terms/virtual-machine-máquina-virtual/)
- [CI/CD (Integração Contínua/Entrega Contínua)](/en/terms/ci-cd-integração-contínua-entrega-contínua/)
- [Microservices (Microsserviços)](/en/terms/microservices-microsserviços/)
