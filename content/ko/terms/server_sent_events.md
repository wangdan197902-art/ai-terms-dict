---
title: "서버 전송 이벤트"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
aliases:
  - /ko/terms/server_sent_events/
date: "2026-07-18T16:15:05.442385Z"
lastmod: "2026-07-18T16:38:06.907426Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "웹 서버가 단일 HTTP 연결을 통해 클라이언트에 실시간 업데이트를 푸시할 수 있게 하는 표준 프로토콜입니다."
---

## Definition

서버 전송 이벤트(SSE)는 서버에서 클라이언트로의 단방향 통신을 가능하게 하며, 서버는 클라이언트가 반복적으로 폴링하지 않고도 데이터를 지속적으로 스트리밍할 수 있습니다. 일반 HTTP를 사용하므로 방화벽 통과가 용이하고 구현이 간단합니다.

### Summary

웹 서버가 단일 HTTP 연결을 통해 클라이언트에 실시간 업데이트를 푸시할 수 있게 하는 표준 프로토콜입니다.

## Key Concepts

- 이벤트 스트림
- 단방향 통신
- 자동 재연결
- HTTP 기반

## Use Cases

- 실시간 주식 가격 피드
- 실시간 알림
- 진행 상황 추적 업데이트

## Related Terms

- [WebSockets (웹소켓)](/en/terms/websockets-웹소켓/)
- [Long Polling (롱 폴링)](/en/terms/long-polling-롱-폴링/)
- [Streaming API (스트리밍 API)](/en/terms/streaming-api-스트리밍-api/)
- [EventSource (이벤트 소스)](/en/terms/eventsource-이벤트-소스/)
