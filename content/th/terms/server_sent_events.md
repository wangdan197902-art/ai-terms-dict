---
title: "เหตุการณ์ที่ส่งจากเซิร์ฟเวอร์"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
aliases:
  - /th/terms/server_sent_events/
date: "2026-07-18T16:15:04.371216Z"
lastmod: "2026-07-18T16:38:07.653640Z"
draft: false
source: "agnes_llm"
status: "published"
language: "th"
description: "โปรโตคอลมาตรฐานที่อนุญาตให้เซิร์ฟเวอร์เว็บส่งอัปเดตแบบเรียลไทม์ไปยังไคลเอนต์ผ่านการเชื่อมต่อ HTTP เดียว"
---

## Definition

เหตุการณ์ที่ส่งจากเซิร์ฟเวอร์ (SSE) เปิดใช้งานการสื่อสารทางเดียวจากเซิร์ฟเวอร์ไปยังไคลเอนต์ โดยที่เซิร์ฟเวอร์สามารถสตรีมข้อมูลอย่างต่อเนื่องโดยไม่ต้องให้ไคลเอนต์ทำการขอข้อมูลซ้ำๆ มันใช้ HTTP ธรรมดา ทำให้เป็นทางเลือกที่ง่ายกว่าสำหรับการอัปเดตแบบเรียลไทม์

### Summary

โปรโตคอลมาตรฐานที่อนุญาตให้เซิร์ฟเวอร์เว็บส่งอัปเดตแบบเรียลไทม์ไปยังไคลเอนต์ผ่านการเชื่อมต่อ HTTP เดียว

## Key Concepts

- สตรีมเหตุการณ์
- การสื่อสารทางเดียว
- การเชื่อมต่อใหม่โดยอัตโนมัติ
- บนพื้นฐาน HTTP

## Use Cases

- ข้อมูลราคาหุ้นแบบสด
- การแจ้งเตือนแบบเรียลไทม์
- การอัปเดตสถานะความคืบหน้า

## Related Terms

- [WebSockets (การสื่อสารสองทาง)](/en/terms/websockets-การส-อสารสองทาง/)
- [Long Polling (การขอข้อมูลระยะยาว)](/en/terms/long-polling-การขอข-อม-ลระยะยาว/)
- [Streaming API (API แบบสตรีม)](/en/terms/streaming-api-api-แบบสตร-ม/)
- [EventSource (ออบเจกต์ JavaScript สำหรับ SSE)](/en/terms/eventsource-ออบเจกต-javascript-สำหร-บ-sse/)
