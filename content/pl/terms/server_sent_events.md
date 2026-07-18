---
title: "Serwer wysyła zdarzenia"
term_id: "server_sent_events"
category: "engineering_practice"
subcategory: ""
tags: ["Web Development", "Real-time", "API Design"]
difficulty: 2
weight: 1
slug: "server_sent_events"
aliases:
  - /pl/terms/server_sent_events/
date: "2026-07-18T16:16:17.214054Z"
lastmod: "2026-07-18T17:15:08.916971Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Standardowy protokół pozwalający serwerom internetowym na przesyłanie aktualizacji w czasie rzeczywistym do klientów przez pojedyncze połączenie HTTP."
---

## Definition

Serwer-Sent Events (SSE) umożliwiają jednokierunkową komunikację od serwera do klienta, gdzie serwer może strumieniować dane ciągle bez konieczności wielokrotnego odpytywania przez klienta. Wykorzystuje zwykłe HTTP, co sprawia, że jest prostszy w implementacji niż WebSockets w przypadkach wymagających tylko pushu danych.

### Summary

Standardowy protokół pozwalający serwerom internetowym na przesyłanie aktualizacji w czasie rzeczywistym do klientów przez pojedyncze połączenie HTTP.

## Key Concepts

- Strumień zdarzeń
- Jednokierunkowa komunikacja
- Automatyczne ponowne łączenie
- Oparte na HTTP

## Use Cases

- Ceny akcji na żywo
- Powiadomienia w czasie rzeczywistym
- Aktualizacje postępu zadań

## Related Terms

- [WebSockets](/en/terms/websockets/)
- [Długie odpytywanie](/en/terms/długie-odpytywanie/)
- [API strumieniowe](/en/terms/api-strumieniowe/)
- [EventSource](/en/terms/eventsource/)
