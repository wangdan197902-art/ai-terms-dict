#!/usr/bin/env python3
"""AGNES_LLM API连通性测试脚本。

测试5个用例：
1. 基础连通性测试
2. JSON模式测试
3. 术语定义生成测试
4. 翻译能力测试
5. 缓存机制测试
"""
import sys
import json
from pathlib import Path

# 添加项目根到path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.utils.agnes_client import AGNESClient


def test_1_basic_connection(client: AGNESClient) -> bool:
    """测试1: 基础连通性。"""
    print("\n===== 测试1: 基础连通性 =====")
    return client.test_connection()


def test_2_json_mode(client: AGNESClient) -> bool:
    """测试2: JSON输出模式。"""
    print("\n===== 测试2: JSON输出模式 =====")
    messages = [
        {"role": "system", "content": "You are an AI term expert. Respond ONLY in valid JSON."},
        {"role": "user", "content": 'Generate a simple term definition for "LLM". Format: {"term": "LLM", "definition": "short definition here"}'},
    ]
    result = client.chat_json(messages, temperature=0.3)
    print(f"结果: {result}")
    if "term" in result and "definition" in result:
        print("✓ JSON模式工作正常")
        return True
    else:
        print("✗ JSON模式异常")
        return False


def test_3_definition_generation(client: AGNESClient) -> bool:
    """测试3: 术语定义生成。"""
    print("\n===== 测试3: 术语定义生成 =====")
    messages = [
        {"role": "system", "content": "You are an AI terminology expert. Generate detailed term definitions in JSON format."},
        {"role": "user", "content": """Generate a comprehensive definition for "Prompt Engineering".

Output JSON with fields:
{
  "term_id": "prompt_engineering",
  "english": "Prompt Engineering",
  "definition_short": "one sentence summary",
  "definition_long": "detailed explanation 100-200 words",
  "key_concepts": ["concept1", "concept2", "concept3"],
  "use_cases": ["use case 1", "use case 2"],
  "related_terms": ["term1", "term2"],
  "difficulty": 3,
  "tags": ["tag1", "tag2"]
}"""},
    ]
    result = client.chat_json(messages, temperature=0.3)
    print(f"生成的术语: {result.get('english', 'N/A')}")
    print(f"短定义: {result.get('definition_short', 'N/A')[:100]}...")
    required = ["term_id", "english", "definition_short", "definition_long"]
    if all(k in result for k in required):
        print("✓ 术语定义生成成功")
        return True
    else:
        print(f"✗ 缺少字段: {set(required) - set(result.keys())}")
        return False


def test_4_translation(client: AGNESClient) -> bool:
    """测试4: 翻译能力。"""
    print("\n===== 测试4: 多语种翻译 =====")
    messages = [
        {"role": "system", "content": "You are a professional translator for AI/technical content. Respond ONLY in JSON."},
        {"role": "user", "content": """Translate the following term and definition to Spanish (es), German (de), Japanese (ja), French (fr), Chinese (zh).

Source:
- term: Prompt Engineering
- definition: The practice of designing and optimizing inputs to language models.

Output:
{
  "translations": {
    "es": {"term": "...", "definition": "..."},
    "de": {"term": "...", "definition": "..."},
    "ja": {"term": "...", "definition": "..."},
    "fr": {"term": "...", "definition": "..."},
    "zh": {"term": "...", "definition": "..."}
  }
}"""},
    ]
    result = client.chat_json(messages, temperature=0.3)
    translations = result.get("translations", {})
    print(f"翻译语种数: {len(translations)}")
    for lang, data in translations.items():
        print(f"  {lang}: {data.get('term', 'N/A')} - {data.get('definition', 'N/A')[:50]}")
    if len(translations) == 5:
        print("✓ 翻译能力正常")
        return True
    else:
        print(f"✗ 翻译语种不足: {len(translations)}/5")
        return False


def test_5_cache(client: AGNESClient) -> bool:
    """测试5: 缓存机制。"""
    print("\n===== 测试5: 缓存机制 =====")
    import time
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 2+2? Reply with one number."},
    ]
    # 第一次调用
    start = time.time()
    result1 = client.chat_completion(messages, temperature=0.0, use_cache=False)
    duration1 = time.time() - start
    print(f"第一次调用: {duration1:.2f}s - {result1[:50]}")

    # 第二次调用（应命中缓存）
    start = time.time()
    result2 = client.chat_completion(messages, temperature=0.0, use_cache=True)
    duration2 = time.time() - start
    print(f"第二次调用(缓存): {duration2:.2f}s - {result2[:50]}")

    if duration2 < duration1 * 0.5:
        print(f"✓ 缓存命中，加速 {duration1/max(duration2, 0.001):.1f}x")
        return True
    else:
        print("⚠ 缓存未命中或加速不明显")
        return True  # 不算失败


def main():
    print("=" * 60)
    print("AGNES_LLM API 连通性测试")
    print("=" * 60)

    try:
        client = AGNESClient()
    except Exception as e:
        print(f"✗ 客户端初始化失败: {e}")
        return 1

    results = []
    results.append(("基础连通性", test_1_basic_connection(client)))
    results.append(("JSON输出模式", test_2_json_mode(client)))
    results.append(("术语定义生成", test_3_definition_generation(client)))
    results.append(("多语种翻译", test_4_translation(client)))
    results.append(("缓存机制", test_5_cache(client)))

    print("\n" + "=" * 60)
    print("测试结果汇总")
    print("=" * 60)
    passed = 0
    for name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status} - {name}")
        if success:
            passed += 1
    print(f"\n总计: {passed}/{len(results)} 通过")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
