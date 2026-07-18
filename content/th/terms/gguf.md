---
title: "GGUF"
term_id: "gguf"
category: "basic_concepts"
subcategory: ""
tags: ["format", "optimization", "local_llm"]
difficulty: 3
weight: 1
slug: "gguf"
aliases:
  - /th/terms/gguf/
date: "2026-07-18T15:55:27.193916Z"
lastmod: "2026-07-18T16:38:07.607975Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "รูปแบบไฟล์ที่พัฒนาโดยgger.ai สำหรับการจัดเก็บและโหลดโมเดลภาษาขนาดใหญ่ที่ถูกทำให้ลดขนาดลง (quantized) อย่างมีประสิทธิภาพบนฮาร์ดแวร์ท้องถิ่น"
---

## Definition

GGUF (GPT-Generated Unified Format) เป็นรูปแบบไฟล์แบบไบนารีที่ออกแบบมาโดยเฉพาะสำหรับการรันโมเดลภาษาขนาดใหญ่บนฮาร์ดแวร์ระดับผู้บริโภค รองรับเทคนิคการลดขนาด (quantization) หลายประเภท ทำให้โมเดลมีขนาดเล็กลงและทำงานได้เร็วขึ้นบนอุปกรณ์ทั่วไปโดยไม่สูญเสียความแม่นยำมากนัก

### Summary

รูปแบบไฟล์ที่พัฒนาโดยgger.ai สำหรับการจัดเก็บและโหลดโมเดลภาษาขนาดใหญ่ที่ถูกทำให้ลดขนาดลง (quantized) อย่างมีประสิทธิภาพบนฮาร์ดแวร์ท้องถิ่น

## Key Concepts

- การลดขนาดโมเดล (Quantization)
- การเก็บรักษารูปแบบโมเดล (Model Serialization)
- การอนุมานแบบท้องถิ่น (Local Inference)
- การเพิ่มประสิทธิภาพหน่วยความจำ

## Use Cases

- การรัน LLMs บนแล็ปท็อปหรือเดสก์ท็อปส่วนตัว
- การปรับใช้โมเดลในอุปกรณ์ขอบ (edge devices) ที่มีทรัพยากรจำกัด
- การแบ่งปันน้ำหนักโมเดลที่ผ่านการปรับแต่งแล้วในชุมชนโอเพนซอร์ส

## Related Terms

- [LLAMA.cpp (ไลบรารีสำหรับรันโมเดล LLAMA)](/en/terms/llama-cpp-ไลบราร-สำหร-บร-นโมเดล-llama/)
- [Quantization (การลดขนาดโมเดล)](/en/terms/quantization-การลดขนาดโมเดล/)
- [ONNX (Open Neural Network Exchange)](/en/terms/onnx-open-neural-network-exchange/)
- [Model Weights (น้ำหนักโมเดล)](/en/terms/model-weights-น-ำหน-กโมเดล/)
