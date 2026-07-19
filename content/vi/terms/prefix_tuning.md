---
title: Điều chỉnh tiền tố
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T16:08:01.903080Z'
lastmod: '2026-07-18T16:38:07.794022Z'
draft: false
source: agnes_llm
status: published
language: vi
description: Một phương pháp tinh chỉnh hiệu quả về tham số, thêm các vectơ liên tục
  có thể huấn luyện vào đầu vào của các lớp biến đổi.
---
## Definition

Điều chỉnh tiền tố là một kỹ thuật thích ứng hiệu quả về tham số cho các mô hình biến đổi đã được tiền huấn luyện. Thay vì cập nhật tất cả các trọng số của mô hình, phương pháp này thêm một chuỗi các vectơ liên tục có thể huấn luyện (tiền tố) vào phía trước đầu vào của mỗi lớp biến đổi. Điều này cho phép mô hình thích nghi với các nhiệm vụ cụ thể mà chỉ cần cập nhật một lượng nhỏ tham số.

### Summary

Một phương pháp tinh chỉnh hiệu quả về tham số, thêm các vectơ liên tục có thể huấn luyện vào đầu vào của các lớp biến đổi.

## Key Concepts

- Điều chỉnh hiệu quả tham số
- Lời nhắc mềm
- Các lớp biến đổi
- Khung xương đóng băng

## Use Cases

- Thích ứng học ít mẫu
- Học đa nhiệm với nguồn lực hạn chế
- Tùy chỉnh các mô hình ngôn ngữ lớn cho các lĩnh vực chuyên biệt

## Related Terms

- [prompt_tuning (điều chỉnh lời nhắc)](/en/terms/prompt_tuning-điều-chỉnh-lời-nhắc/)
- [p_tuning (điều chỉnh P-tuning)](/en/terms/p_tuning-điều-chỉnh-p-tuning/)
- [adapter_modules (các mô-đun bộ điều hợp)](/en/terms/adapter_modules-các-mô-đun-bộ-điều-hợp/)
- [peft (kỹ thuật tinh chỉnh hiệu quả tham số)](/en/terms/peft-kỹ-thuật-tinh-chỉnh-hiệu-quả-tham-số/)
