---
title: "API"
term_id: "api"
category: "engineering_practice"
subcategory: ""
tags: ["Development", "Integration", "Infrastructure"]
difficulty: 1
weight: 1
slug: "api"
date: "2026-07-18T15:22:07.926577Z"
lastmod: "2026-07-18T16:38:06.765049Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "서로 다른 소프트웨어 시스템 간에 통신하고 데이터를 교환할 수 있게 하는 애플리케이션 프로그래밍 인터페이스입니다."
---
## Definition

API는 소프트웨어 및 애플리케이션을 구축하기 위한 일련의 프로토콜과 도구를 정의합니다. AI에서 API를 사용하면 개발자가 대규모 언어 모델(LLM)이나 이미지 생성기 같은 강력한 모델을 로컬에서 호스팅하지 않고도 접근할 수 있습니다.

### Summary

서로 다른 소프트웨어 시스템 간에 통신하고 데이터를 교환할 수 있게 하는 애플리케이션 프로그래밍 인터페이스입니다.

## Key Concepts

- 엔드포인트
- REST
- 인증
- 페이로드

## Use Cases

- 웹사이트에 챗봇 통합
- 클라우드 기반 머신러닝 모델 접근
- AI 서비스로부터 데이터 검색

## Code Example

```python
import requests
response = requests.get('https://api.ai.com/v1/generate', headers={'Authorization': 'Bearer token'})
```

## Related Terms

- [REST (상태 부재 전송 프로토콜)](/en/terms/rest-상태-부재-전송-프로토콜/)
- [SDK (소프트웨어 개발 키트)](/en/terms/sdk-소프트웨어-개발-키트/)
- [Webhook (웹훅)](/en/terms/webhook-웹훅/)
- [Integration (통합)](/en/terms/integration-통합/)
