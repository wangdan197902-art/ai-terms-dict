---
title: "ELMo"
term_id: "elmo"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "Embeddings", "History"]
difficulty: 3
weight: 1
slug: "elmo"
aliases:
  - /th/terms/elmo/
date: "2026-07-18T15:51:15.443307Z"
lastmod: "2026-07-18T16:38:07.600933Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "Embeddings from Language Models วิธีการแสดงแทนคำที่มีบริบทเชิงลึก โดยใช้ LSTM แบบสองทิศทาง"
---

## Definition

ELMo สร้างเวกเตอร์แทนคำที่ไวต่อบริบท (context-sensitive word embeddings) โดยประมวลผลข้อความผ่าน LSTM แบบสองทิศทาง (bidirectional LSTM) ที่ได้รับการฝึกฝนจากคลังข้อความขนาดใหญ่ ต่างจากเวกเตอร์คงที่เช่น Word2Vec ELMo สามารถจับความหมายหลายประการของคำ (polysemy) ได้โดยการสร้างเวกเตอร์ที่แตกต่างกันขึ้นอยู่กับบริบทของประโยค

### Summary

Embeddings from Language Models วิธีการแสดงแทนคำที่มีบริบทเชิงลึก โดยใช้ LSTM แบบสองทิศทาง

## Key Concepts

- เวกเตอร์แทนคำเชิงบริบท (Contextual Embeddings)
- LSTM แบบสองทิศทาง (Bidirectional LSTM)
- การฝึกฝนล่วงหน้า (Pre-training)
- ความหมายหลายประการของคำ (Polysemy)

## Use Cases

- การวิเคราะห์ความรู้สึก (Sentiment analysis)
- การระบุชื่อเฉพาะ (Named entity recognition)
- การแก้ความกำกวมของการอ้างอิงกลับ (Coreference resolution)

## Related Terms

- [Word2Vec (เวกเตอร์แทนคำแบบคงที่)](/en/terms/word2vec-เวกเตอร-แทนคำแบบคงท/)
- [BERT (แบบจำลองภาษาแบบบิเดอเรกชันนัลจากผู้พัฒนาทั้งสองด้าน)](/en/terms/bert-แบบจำลองภาษาแบบบ-เดอเรกช-นน-ลจากผ-พ-ฒนาท-งสองด-าน/)
- [Transformer (สถาปัตยกรรมทรานส์ฟอร์มเมอร์)](/en/terms/transformer-สถาป-ตยกรรมทรานส-ฟอร-มเมอร/)
- [Language Modeling (การสร้างแบบจำลองภาษา)](/en/terms/language-modeling-การสร-างแบบจำลองภาษา/)
