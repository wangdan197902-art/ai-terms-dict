---
title: "Kỹ thuật Prompt"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T15:22:23.225697Z"
lastmod: "2026-07-18T16:38:07.677109Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Thực hành thiết kế và tối ưu hóa văn bản đầu vào để hướng các mô hình ngôn ngữ lớn (LLM) tạo ra kết quả mong muốn."
---
## Definition

Kỹ thuật prompt liên quan đến việc tạo ra các đầu vào cụ thể, được gọi là prompt, nhằm khơi gợi các phản hồi chính xác, phù hợp và chất lượng cao từ các mô hình AI sinh tạo. Nó đòi hỏi sự hiểu biết về cách các mô hình diễn giải ngữ cảnh và yêu cầu.

### Summary

Thực hành thiết kế và tối ưu hóa văn bản đầu vào để hướng các mô hình ngôn ngữ lớn (LLM) tạo ra kết quả mong muốn.

## Key Concepts

- Khung cảnh ngữ nghĩa
- Học ít ví dụ (Few-shot learning)
- Điều chỉnh chỉ dẫn (Instruction tuning)
- Tối ưu hóa token

## Use Cases

- Chatbot hỗ trợ khách hàng tự động
- Trợ lý tạo mã nguồn
- Công cụ hỗ trợ sáng tác văn học

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (Mô hình ngôn ngữ lớn)](/en/terms/llm-mô-hình-ngôn-ngữ-lớn/)
- [Chain-of-Thought (Chuỗi suy nghĩ)](/en/terms/chain-of-thought-chuỗi-suy-nghĩ/)
- [RAG (Tìm kiếm và sinh lại)](/en/terms/rag-tìm-kiếm-và-sinh-lại/)
- [Fine-tuning (Huấn luyện tinh chỉnh)](/en/terms/fine-tuning-huấn-luyện-tinh-chỉnh/)
