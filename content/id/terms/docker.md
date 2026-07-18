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
  - /id/terms/docker/
date: "2026-07-18T15:34:15.539757Z"
lastmod: "2026-07-18T16:38:07.412652Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Docker adalah platform untuk mengembangkan, mengirimkan, dan menjalankan aplikasi dalam kontainer ringan yang portabel."
---

## Definition

Docker memungkinkan pengembang untuk membungkus aplikasi beserta semua dependensinya ke dalam satu unit standar untuk pengembangan perangkat lunak. Kontainer-kontainer ini mengisolasi perangkat lunak dari lingkungannya, memastikan konsistensi di berbagai lingkungan.

### Summary

Docker adalah platform untuk mengembangkan, mengirimkan, dan menjalankan aplikasi dalam kontainer ringan yang portabel.

## Key Concepts

- Kontainerisasi
- Image
- Isolasi
- Portabilitas

## Use Cases

- Menyebarkan model ML yang telah dilatih sebagai mikro layanan
- Menstandarkan lingkungan pengembangan untuk tim ilmu data
- Menskala beban kerja inferensi di infrastruktur cloud

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Orkestrasi kontainer)](/en/terms/kubernetes-orkestrasi-kontainer/)
- [Virtual Machine (Mesin virtual)](/en/terms/virtual-machine-mesin-virtual/)
- [CI/CD (Integrasi dan pengiriman berkelanjutan)](/en/terms/ci-cd-integrasi-dan-pengiriman-berkelanjutan/)
- [Microservices (Arsitektur mikro layanan)](/en/terms/microservices-arsitektur-mikro-layanan/)
