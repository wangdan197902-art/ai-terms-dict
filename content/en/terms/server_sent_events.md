---
title: "Server-Sent Events"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
date: "2026-07-18T10:15:20.591877Z"
lastmod: "2026-07-18T11:44:44.720747Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A standard protocol allowing web servers to push real-time updates to clients over a single HTTP connection."
---
## Definition

Server-Sent Events (SSE) enable one-way communication from the server to the client, where the server can stream data continuously without the client repeatedly polling. It uses plain HTTP, making it simpler to implement than WebSockets, especially when firewalls block non-HTTP protocols. SSE automatically handles reconnection logic and ensures message ordering, making it ideal for live feeds, notifications, and dashboards where the client does not need to send frequent data back to the server.

### Summary

A standard protocol allowing web servers to push real-time updates to clients over a single HTTP connection.

## Key Concepts

- Event stream
- One-way communication
- Automatic reconnection
- HTTP-based

## Use Cases

- Live stock price feeds
- Real-time notifications
- Progress tracking updates

## Related Terms

- [WebSockets](/en/terms/websockets/)
- [Long Polling](/en/terms/long-polling/)
- [Streaming API](/en/terms/streaming-api/)
- [EventSource](/en/terms/eventsource/)
