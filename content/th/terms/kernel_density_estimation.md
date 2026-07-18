---
title: "การประมาณความหนาแน่นแบบเคอร์เนล (Kernel density estimation)"
term_id: "kernel_density_estimation"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "probability", "data-analysis"]
difficulty: 3
weight: 1
slug: "kernel_density_estimation"
aliases:
  - /th/terms/kernel_density_estimation/
date: "2026-07-18T16:01:09.548753Z"
lastmod: "2026-07-18T16:38:07.621114Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "วิธีการแบบไม่ใช้พารามิเตอร์ (non-parametric) ใช้เพื่อประมาณฟังก์ชันความหนาแน่นของความน่าจะเป็นของตัวแปรสุ่ม โดยอาศัยตัวอย่างข้อมูลที่จำกัด"
---

## Definition

การประมาณความหนาแน่นแบบเคอร์เนล (KDE) เป็นเทคนิคทางสถิติพื้นฐานที่ใช้ทำให้ข้อมูลแบบไม่ต่อเนื่องมีความเรียบเนียนเพื่อสร้างเส้นโค้งการแจกแจงความน่าจะเป็นแบบต่อเนื่อง โดยจะวางฟังก์ชันเคอร์เนล (โดยทั่วไปคือฟังก์ชันเกาส์เซียน) ไว้ที่แต่ละจุดข้อมูล

### Summary

วิธีการแบบไม่ใช้พารามิเตอร์ (non-parametric) ใช้เพื่อประมาณฟังก์ชันความหนาแน่นของความน่าจะเป็นของตัวแปรสุ่ม โดยอาศัยตัวอย่างข้อมูลที่จำกัด

## Key Concepts

- ฟังก์ชันความหนาแน่นของความน่าจะเป็น (Probability Density Function)
- สถิติแบบไม่ใช้พารามิเตอร์ (Non-parametric Statistics)
- การทำให้เรียบ (Smoothing)
- เคอร์เนลเกาส์เซียน (Gaussian Kernel)

## Use Cases

- การวิเคราะห์ข้อมูลเชิงสำรวจ (EDA)
- การตรวจจับค่าผิดปกติในข้อมูลหนึ่งมิติ
- การแสดงผลการแจกแจงของคุณลักษณะ (features) ในชุดข้อมูล

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram (ฮิสโตแกรม)](/en/terms/histogram-ฮ-สโตแกรม/)
- [Parzen Window (หน้าต่างพาเซน)](/en/terms/parzen-window-หน-าต-างพาเซน/)
- [Bandwidth Selection (การเลือกค่าแบนด์วิดธ์)](/en/terms/bandwidth-selection-การเล-อกค-าแบนด-ว-ดธ/)
- [Scipy Stats (ไลบรารีสถิติใน Scipy)](/en/terms/scipy-stats-ไลบราร-สถ-ต-ใน-scipy/)
