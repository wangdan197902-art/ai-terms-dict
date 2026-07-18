---
title: "ฮิสโตแกรมของการกระจัดตามทิศทาง"
term_id: "histogram_of_oriented_displacements"
category: "basic_concepts"
subcategory: ""
tags: ["computer_vision", "video_analysis", "features"]
difficulty: 4
weight: 1
slug: "histogram_of_oriented_displacements"
aliases:
  - /th/terms/histogram_of_oriented_displacements/
date: "2026-07-18T15:58:46.421045Z"
lastmod: "2026-07-18T16:38:07.615218Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "ตัวบรรยายลักษณะ (feature descriptor) ที่ใช้ในคอมพิวเตอร์วิทัศน์ เพื่อจับรูปแบบการเคลื่อนไหวโดยการวิเคราะห์ฮิสโตแกรมของการกระจัดในลำดับวิดีโอ"
---

## Definition

ฮิสโตแกรมของการกระจัดตามทิศทาง (Histogram of Oriented Displacements - HOD) เป็นวิธีการสกัดคุณลักษณะสำหรับการวิเคราะห์วิดีโอ ซึ่งขยายแนวคิดของ HOG (Histogram of Oriented Gradients) ไปสู่มิติเวลา โดยคำนวณฮิสโตแกรมของเวกเตอร์โฟลว์เชิงแสง (optical flow vectors) ภายในหน้าต่างเวลา HOD จับภาพทั้งโครงสร้างเชิงพื้นที่และการเปลี่ยนแปลงของวัตถุเมื่อเวลาผ่านไป ทำให้มีประสิทธิภาพสูงในการระบุกิจกรรมหรือการกระทำต่างๆ ในวิดีโอ

### Summary

ตัวบรรยายลักษณะ (feature descriptor) ที่ใช้ในคอมพิวเตอร์วิทัศน์ เพื่อจับรูปแบบการเคลื่อนไหวโดยการวิเคราะห์ฮิสโตแกรมของการกระจัดในลำดับวิดีโอ

## Key Concepts

- โฟลว์เชิงแสง (Optical Flow)
- ตัวบรรยายลักษณะ (Feature Descriptor)
- การวิเคราะห์การเคลื่อนไหว (Motion Analysis)
- การประมวลผลวิดีโอ (Video Processing)

## Use Cases

- การรู้จำการกระทำ (Action recognition)
- การวิเคราะห์กิจกรรมของมนุษย์ (Human activity analysis)
- การเฝ้าระวังด้วยวิดีโอ (Video surveillance)

## Related Terms

- [HOG (Histogram of Oriented Gradients)](/en/terms/hog-histogram-of-oriented-gradients/)
- [Optical Flow (โฟลว์เชิงแสง)](/en/terms/optical-flow-โฟลว-เช-งแสง/)
- [SIFT (Scale-Invariant Feature Transform)](/en/terms/sift-scale-invariant-feature-transform/)
