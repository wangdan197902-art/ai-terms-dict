---
title: "服务器发送事件"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
aliases:
  - /zh/terms/server_sent_events/
date: "2026-07-18T11:33:18.814254Z"
lastmod: "2026-07-18T11:44:45.553529Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种标准协议，允许Web服务器通过单个HTTP连接向客户端推送实时更新。"
---

## Definition

服务器发送事件（SSE）实现了从服务器到客户端的单向通信，服务器可以持续流式传输数据，而无需客户端反复轮询。它使用纯HTTP协议，使其易于实现且兼容防火墙。

### Summary

一种标准协议，允许Web服务器通过单个HTTP连接向客户端推送实时更新。

## Key Concepts

- 事件流
- 单向通信
- 自动重连
- 基于HTTP

## Use Cases

- 实时股票价格行情
- 实时通知
- 进度跟踪更新

## Related Terms

- [WebSockets (WebSocket)](/en/terms/websockets-websocket/)
- [Long Polling (长轮询)](/en/terms/long-polling-长轮询/)
- [Streaming API (流式API)](/en/terms/streaming-api-流式api/)
- [EventSource (事件源接口)](/en/terms/eventsource-事件源接口/)
