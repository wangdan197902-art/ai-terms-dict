---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:35:03.225260Z"
lastmod: "2026-07-18T17:15:08.831279Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Docker to platforma do tworzenia, dystrybucji i uruchamiania aplikacji w lekkich, przenośnych kontenerach."
---
## Definition

Docker umożliwia programistom pakowanie aplikacji wraz ze wszystkimi jej zależnościami do znormalizowanej jednostki służącej do rozwoju oprogramowania. Kontenery te izolują oprogramowanie od środowiska, zapewniając spójność działania na różnych maszynach.

### Summary

Docker to platforma do tworzenia, dystrybucji i uruchamiania aplikacji w lekkich, przenośnych kontenerach.

## Key Concepts

- Konteneryzacja
- Obrazy
- Izolacja
- Przenośność

## Use Cases

- Wdrażanie wytrenowanych modeli ML jako mikroserwisów
- Standaryzacja środowisk deweloperskich dla zespołów nauki o danych
- Skalowanie obciążeń wnioskowania (inference) w infrastrukturze chmurowej

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (platforma do automatyzacji wdrażania, skalowania i zarządzania konteneryzowanymi aplikacjami)](/en/terms/kubernetes-platforma-do-automatyzacji-wdrażania-skalowania-i-zarządzania-konteneryzowanymi-aplikacjami/)
- [Virtual Machine (wirtualna maszyna), VM (izolowane środowisko sprzętowe emulowane przez oprogramowanie)](/en/terms/virtual-machine-wirtualna-maszyna-vm-izolowane-środowisko-sprzętowe-emulowane-przez-oprogramowanie/)
- [CI/CD (ciągła integracja i ciągłe dostarczanie, proces automatyzacji wdrożeń)](/en/terms/ci-cd-ciągła-integracja-i-ciągłe-dostarczanie-proces-automatyzacji-wdrożeń/)
- [Microservices (architektura polegająca na budowaniu aplikacji jako zestawu małych, niezależnych usług)](/en/terms/microservices-architektura-polegająca-na-budowaniu-aplikacji-jako-zestawu-małych-niezależnych-usług/)
