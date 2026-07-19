---
title: "دوكر"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:36:46.347121Z"
lastmod: "2026-07-18T17:15:08.460326Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ar"
description: "دوكر هو منصة لتطوير وتشغيل وتوزيع التطبيقات داخل حاويات خفيفة الوزن وقابلة للنقل."
---
## Definition

يتيح دوكر للمطورين حزم التطبيق مع جميع تبعياته في وحدة قياسية لتطوير البرمجيات. تعزل هذه الحاويات البرنامج عن بيئته، مما يضمن اتساق الأداء عبر مختلف البيئات.

### Summary

دوكر هو منصة لتطوير وتشغيل وتوزيع التطبيقات داخل حاويات خفيفة الوزن وقابلة للنقل.

## Key Concepts

- الحاويات (Containerization)
- الصور (Images)
- العزل (Isolation)
- القابلية للنقل (Portability)

## Use Cases

- نشر نماذج التعلم الآلي المدربة كخدمات مصغرة
- توحيد بيئات التطوير لفرق علم البيانات
- توسيع نطاق أعباء عمل الاستدلال في البنية التحتية السحابية

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [كوبيرنتيز (إدارة الحاويات والمجموعات)](/en/terms/كوبيرنتيز-إدارة-الحاويات-والمجموعات/)
- [الآلة الافتراضية (بيئة تشغيل معزولة بالكامل)](/en/terms/الآلة-الافتراضية-بيئة-تشغيل-معزولة-بالكامل/)
- [التكامل والنشر المستمر (CI/CD)](/en/terms/التكامل-والنشر-المستمر-ci-cd/)
- [الخدمات المصغرة (Microservices)](/en/terms/الخدمات-المصغرة-microservices/)
