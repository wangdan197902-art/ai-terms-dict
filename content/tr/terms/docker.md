---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:34:19.689881Z"
lastmod: "2026-07-18T16:38:07.256575Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Docker, uygulamaları hafif, taşınabilir konteynerler içinde geliştirmek, dağıtmak ve çalıştırmak için bir platformdur."
---
## Definition

Docker, geliştiricilerin bir uygulamayı tüm bağımlılıklarıyla birlikte yazılım geliştirme için standartlaştırılmış bir birime paketlemesini sağlar. Bu konteynerler, tutarlılığı sağlarken yazılımı ortamından izole eder.

### Summary

Docker, uygulamaları hafif, taşınabilir konteynerler içinde geliştirmek, dağıtmak ve çalıştırmak için bir platformdur.

## Key Concepts

- Konteynerleştirme
- İmajlar
- İzolasyon
- Taşınabilirlik

## Use Cases

- Eğitilmiş ML modellerinin mikroservis olarak dağıtılması
- Veri bilimi ekipleri için geliştirme ortamlarının standartlaştırılması
- Bulut altyapısında çıkarım (inference) iş yüklerinin ölçeklendirilmesi

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Kümeleme yönetimi)](/en/terms/kubernetes-kümeleme-yönetimi/)
- [Virtual Machine (Sanal Makine)](/en/terms/virtual-machine-sanal-makine/)
- [CI/CD (Sürekli Entegrasyon/Sürekli Dağıtım)](/en/terms/ci-cd-sürekli-entegrasyon-sürekli-dağıtım/)
- [Microservices (Mikroservisler)](/en/terms/microservices-mikroservisler/)
