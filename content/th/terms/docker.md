---
title: "ด็อกเกอร์ (Docker)"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T15:35:22.605694Z"
lastmod: "2026-07-18T16:38:07.559909Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ด็อกเกอร์เป็นแพลตฟอร์มสำหรับการพัฒนา จัดส่ง และรันแอปพลิเคชันในคอนเทนเนอร์ที่เบาและพกพาได้"
---
## Definition

ด็อกเกอร์ช่วยให้ผู้พัฒนาสามารถแพ็กเกจแอปพลิเคชันพร้อมกับส่วนประกอบทั้งหมด (dependencies) เข้าไปในหน่วยมาตรฐานสำหรับการพัฒนาซอฟต์แวร์ คอนเทนเนอร์เหล่านี้แยกซอฟต์แวร์ออกจากสภาพแวดล้อมภายนอก เพื่อให้มั่นใจว่าการทำงานจะสอดคล้องกัน

### Summary

ด็อกเกอร์เป็นแพลตฟอร์มสำหรับการพัฒนา จัดส่ง และรันแอปพลิเคชันในคอนเทนเนอร์ที่เบาและพกพาได้

## Key Concepts

- การทำให้เป็นคอนเทนเนอร์ (Containerization)
- อิมเมจ (Images)
- การแยกส่วน (Isolation)
- ความสามารถในการพกพา (Portability)

## Use Cases

- การปรับใช้โมเดล ML ที่ฝึกแล้วเป็นไมโครเซอร์วิส
- การทำมาตรฐานสภาพแวดล้อมการพัฒนาสำหรับทีมวิทยาศาสตร์ข้อมูล
- การขยายขนาดงานอนุมาน (inference) ในโครงสร้างพื้นฐานคลาวด์

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (ระบบจัดการคอนเทนเนอร์)](/en/terms/kubernetes-ระบบจ-ดการคอนเทนเนอร/)
- [Virtual Machine (เครื่องเสมือน)](/en/terms/virtual-machine-เคร-องเสม-อน/)
- [CI/CD (กระบวนการส่งมอบซอฟต์แวร์อย่างต่อเนื่อง)](/en/terms/ci-cd-กระบวนการส-งมอบซอฟต-แวร-อย-างต-อเน-อง/)
- [Microservices (สถาปัตยกรรมไมโครเซอร์วิส)](/en/terms/microservices-สถาป-ตยกรรมไมโครเซอร-ว-ส/)
