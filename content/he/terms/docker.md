---
title: "דוקר (Docker)"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
aliases:
  - /he/terms/docker/
date: "2026-07-18T15:36:22.156371Z"
lastmod: "2026-07-18T17:15:09.498316Z"
draft: false
source: "agnes_llm"
status: "published"
language: "he"
description: "דוקר היא פלטפורמה לפיתוח, הפצה והרצת יישומים בתוך מיכלים קלים וניידים."
---

## Definition

דוקר מאפשרת למפתחים לארוז יישום יחד עם כל התלויות שלו ליחידה סטנדרטית לפיתוח תוכנה. מיכלים אלה מבודדים את התוכנה מהסביבה שלה, ובכך מבטיחים עקביות בהרצה.

### Summary

דוקר היא פלטפורמה לפיתוח, הפצה והרצת יישומים בתוך מיכלים קלים וניידים.

## Key Concepts

- מיכליות (Containerization)
- תמונות (Images)
- בידוד (Isolation)
- ניידות (Portability)

## Use Cases

- הפצת מודלי ML מאומנים כשירותים זעירים (microservices)
- סטנדרטיזציה של סביבות פיתוח לצוותי מדעי נתונים
- הרחבת עומסי הסקה (inference) בתשתיות ענן

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (ניהול מיכלים)](/en/terms/kubernetes-ניהול-מיכלים/)
- [Virtual Machine (מכונה וירטואלית)](/en/terms/virtual-machine-מכונה-וירטואלית/)
- [CI/CD (אינטגרציה ומשלוח מתמשכים)](/en/terms/ci-cd-אינטגרציה-ומשלוח-מתמשכים/)
- [Microservices (ארכיטקטורת שירותים זעירים)](/en/terms/microservices-ארכיטקטורת-שירותים-זעירים/)
