---
title: "วาเชอร์สไตน์"
term_id: "wasserstein"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "gan", "probability"]
difficulty: 4
weight: 1
slug: "wasserstein"
aliases:
  - /th/terms/wasserstein/
date: "2026-07-18T15:31:52.827114Z"
lastmod: "2026-07-18T16:38:07.553124Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "เมตริกที่ใช้วัดระยะห่างระหว่างการแจกแจงความน่าจะเป็น โดยคำนวณจากต้นทุนขั้นต่ำในการแปลงการแจกแจงหนึ่งไปเป็นอีกการแจกแจงหนึ่ง"
---

## Definition

ระยะทางวาเชอร์สไตน์ (Wasserstein distance) หรือที่รู้จักกันในชื่อ ระยะทางคนยกดิน (Earth Mover's Distance) ใช้วัดความแตกต่างระหว่างการแจกแจงความน่าจะเป็นสองแบบ โดยการคำนวณ "งาน" ขั้นต่ำที่ต้องใช้ในการเคลื่อนย้ายมวลจากความน่าจะเป็นหนึ่งไปยังอีกความน่าจะเป็นหนึ่ง

### Summary

เมตริกที่ใช้วัดระยะห่างระหว่างการแจกแจงความน่าจะเป็น โดยคำนวณจากต้นทุนขั้นต่ำในการแปลงการแจกแจงหนึ่งไปเป็นอีกการแจกแจงหนึ่ง

## Key Concepts

- ระยะทางคนยกดิน
- การแจกแจงความน่าจะเป็น
- การขนส่งที่เหมาะสม
- ความเสถียรของเกรเดียนต์

## Use Cases

- การฝึก GAN ให้มีความเสถียร
- การปรับโดเมน (Domain Adaptation)
- การวัดความคล้ายคลึงของการแจกแจง

## Related Terms

- [KL Divergence (ค่าเบี่ยงเบนเคล์ล-ไลบ์เลอร์)](/en/terms/kl-divergence-ค-าเบ-ยงเบนเคล-ล-ไลบ-เลอร/)
- [Generative Adversarial Networks (เครือข่ายปฏิปักษ์เชิงกำเนิด)](/en/terms/generative-adversarial-networks-เคร-อข-ายปฏ-ป-กษ-เช-งกำเน-ด/)
- [Optimal Transport (การขนส่งที่เหมาะสม)](/en/terms/optimal-transport-การขนส-งท-เหมาะสม/)
- [Distribution Matching (การจับคู่การแจกแจง)](/en/terms/distribution-matching-การจ-บค-การแจกแจง/)
