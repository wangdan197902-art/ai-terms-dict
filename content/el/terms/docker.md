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
  - /el/terms/docker/
date: "2026-07-18T15:40:28.391093Z"
lastmod: "2026-07-18T17:15:09.865538Z"
draft: false
source: "agnes_llm"
status: "published"
language: "el"
description: "Το Docker είναι μια πλατφόρμα για την ανάπτυξη, τη διανομή και την εκτέλεση εφαρμογών σε ελαφριές, φορητές δοκούς (containers)."
---

## Definition

Το Docker επιτρέπει στους προγραμματιστές να συσκευάζουν μια εφαρμογή μαζί με όλες τις εξαρτήσεις της σε ένα τυποποιημένο μοντέλο για την ανάπτυγμα λογισμικού. Αυτές οι δοκοί απομονώνουν το λογισμικό από το περιβάλλον του, διασφαλίζοντας συνεπή συμπεριφορά σε διαφορετικά περιβάλλοντα.

### Summary

Το Docker είναι μια πλατφόρμα για την ανάπτυξη, τη διανομή και την εκτέλεση εφαρμογών σε ελαφριές, φορητές δοκούς (containers).

## Key Concepts

- Δοκοποίηση (Containerization)
- Εικόνες (Images)
- Απομόνωση
- Φορητότητα

## Use Cases

- Ανάπτυξη εκπαιδευμένων μοντέλων ML ως μικροϋπηρεσιών
- Τυποποίηση περιβαλλόντων ανάπτυξης για ομάδες επιστήμης δεδομένων
- Κλιμάκωση φορτίων συμπερασματολογίας (inference) σε υποδομές cloud

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (Ορχηστρωτής containers)](/en/terms/kubernetes-ορχηστρωτής-containers/)
- [Virtual Machine (Εικονική μηχανή)](/en/terms/virtual-machine-εικονική-μηχανή/)
- [CI/CD (Συνεχής Ολοκλήρωση/Παράδοση)](/en/terms/ci-cd-συνεχής-ολοκλήρωση-παράδοση/)
- [Microservices (Μικροϋπηρεσίες)](/en/terms/microservices-μικροϋπηρεσίες/)
