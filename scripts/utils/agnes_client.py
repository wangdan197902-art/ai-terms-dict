#!/usr/bin/env python3
"""AGNES_LLM API客户端封装。

使用openai SDK通过base_url方式接入AGNES_LLM。
支持三层缓存（内存LRU + 本地文件 + Mock兜底）和重试机制。
"""
import os
import json
import time
import hashlib
import functools
from pathlib import Path
from typing import Any, Optional
from dotenv import load_dotenv

# 加载环境变量
load_dotenv(".env.local")

# 导入openai SDK
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None
    print("警告: openai SDK未安装，请运行 pip install openai")


class AGNESClient:
    """AGNES_LLM API客户端。

    特性：
    - OpenAI兼容协议（通过base_url）
    - 三层缓存：内存LRU + 本地文件 + Mock兜底
    - 自动重试（3次，指数退避1s/2s/4s）
    - JSON模式探测与降级
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        cache_dir: Optional[str] = None,
        enable_cache: bool = True,
        enable_mock_fallback: bool = True,
    ):
        self.api_key = api_key or os.getenv("AGNES_LLM_API_KEY")
        self.base_url = base_url or os.getenv("AGNES_LLM_BASE_URL", "https://apihub.agnes-ai.com/v1")
        self.model = model or os.getenv("AGNES_LLM_MODEL", "agnes-2.0-flash")
        self.cache_dir = Path(cache_dir or os.getenv("CACHE_DIR", ".cache/agnes"))
        self.enable_cache = enable_cache
        self.enable_mock_fallback = enable_mock_fallback

        if not self.api_key:
            raise ValueError("AGNES_LLM_API_KEY 未设置，请检查 .env.local")

        # 创建缓存目录
        if self.enable_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        # 初始化OpenAI客户端
        self.client = None
        if OpenAI:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
            )

        # JSON模式支持标志（首次调用后确定）
        self._json_mode_supported: Optional[bool] = None

        # 内存LRU缓存
        self._memory_cache: dict = {}

    def _cache_key(self, messages: list, **kwargs) -> str:
        """生成缓存键。"""
        content = json.dumps({
            "messages": messages,
            "model": self.model,
            **kwargs,
        }, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def _get_from_memory(self, key: str) -> Optional[Any]:
        """从内存缓存读取。"""
        return self._memory_cache.get(key)

    def _set_to_memory(self, key: str, value: Any) -> None:
        """写入内存缓存（简单LRU，限制1000条）。"""
        if len(self._memory_cache) >= 1000:
            # 简单策略：删除最早的1条
            self._memory_cache.pop(next(iter(self._memory_cache)))
        self._memory_cache[key] = value

    def _get_from_file(self, key: str) -> Optional[Any]:
        """从本地文件缓存读取。"""
        if not self.enable_cache:
            return None
        cache_file = self.cache_dir / f"{key}.json"
        if cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return None
        return None

    def _set_to_file(self, key: str, value: Any) -> None:
        """写入本地文件缓存。"""
        if not self.enable_cache:
            return
        cache_file = self.cache_dir / f"{key}.json"
        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(value, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"警告: 写入缓存失败: {e}")

    def _get_mock_response(self, messages: list) -> Optional[str]:
        """Mock兜底响应。"""
        # 简单Mock：返回占位JSON
        return json.dumps({
            "term_id": "mock_term",
            "term_name": "Mock Term",
            "definition_short": "[Mock] This is a fallback response due to API failure.",
            "definition_long": "[Mock] AGNES_LLM API调用失败，已降级到Mock响应。请检查API连接或额度。",
            "source": "mock_fallback",
        }, ensure_ascii=False)

    def _call_api_with_retry(
        self,
        messages: list,
        temperature: float = 0.3,
        response_format: Optional[dict] = None,
        max_retries: int = 3,
    ) -> Optional[str]:
        """带重试的API调用。"""
        if not self.client:
            print("错误: OpenAI客户端未初始化")
            return None

        last_error = None
        for attempt in range(max_retries):
            try:
                kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                }
                if response_format and self._json_mode_supported is not False:
                    kwargs["response_format"] = response_format

                response = self.client.chat.completions.create(**kwargs)
                content = response.choices[0].message.content

                # 如果使用了response_format且成功，标记JSON模式支持
                if response_format and self._json_mode_supported is None:
                    self._json_mode_supported = True
                    print("✓ AGNES_LLM 支持 response_format JSON模式")

                return content

            except Exception as e:
                last_error = e
                error_str = str(e)
                print(f"警告: API调用失败(第{attempt+1}次): {error_str[:200]}")

                # 如果是response_format不支持，降级
                if response_format and ("response_format" in error_str or "invalid" in error_str.lower()):
                    self._json_mode_supported = False
                    print("⚠ AGNES_LLM 不支持 response_format，降级为Prompt内few-shot模式")
                    return self._call_api_with_retry(messages, temperature, None, max_retries - attempt)

                # 指数退避
                if attempt < max_retries - 1:
                    wait = 2 ** attempt
                    print(f"等待 {wait}s 后重试...")
                    time.sleep(wait)

        print(f"错误: API调用全部失败: {last_error}")
        return None

    def chat_completion(
        self,
        messages: list,
        temperature: float = 0.3,
        response_format: Optional[dict] = None,
        use_cache: bool = True,
    ) -> str:
        """调用AGNES_LLM chat completion。

        参数:
            messages: OpenAI格式消息列表
            temperature: 温度参数
            response_format: 响应格式（如 {"type": "json_object"}）
            use_cache: 是否使用缓存

        返回:
            模型响应文本。API失败时返回Mock响应。
        """
        # 生成缓存键
        cache_key = self._cache_key(messages, temperature=temperature, response_format=response_format)

        # L1: 内存缓存
        if use_cache:
            cached = self._get_from_memory(cache_key)
            if cached is not None:
                return cached

        # L2: 文件缓存
        if use_cache:
            cached = self._get_from_file(cache_key)
            if cached is not None:
                self._set_to_memory(cache_key, cached)
                return cached

        # L3: 实际API调用
        content = self._call_api_with_retry(messages, temperature, response_format)

        if content is None:
            # L4: Mock兜底
            if self.enable_mock_fallback:
                print("⚠ 降级到Mock响应")
                content = self._get_mock_response(messages)
            else:
                raise RuntimeError(f"AGNES_LLM API调用失败，且Mock兜底未启用")

        # 写入缓存
        if use_cache and content:
            self._set_to_memory(cache_key, content)
            self._set_to_file(cache_key, content)

        return content

    def chat_json(
        self,
        messages: list,
        temperature: float = 0.3,
    ) -> dict:
        """调用AGNES_LLM并返回JSON对象。

        优先使用response_format={"type": "json_object"}，
        失败时降级为Prompt内few-shot + 正则提取。
        """
        # 尝试JSON模式
        content = self.chat_completion(
            messages=messages,
            temperature=temperature,
            response_format={"type": "json_object"},
        )

        # 解析JSON
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # 降级：正则提取JSON
            print("⚠ 响应不是有效JSON，尝试正则提取...")
            import re
            match = re.search(r'\{[\s\S]*\}', content)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    pass
            print(f"错误: 无法解析为JSON: {content[:200]}")
            return {"error": "invalid_json", "raw_content": content[:500]}

    def test_connection(self) -> bool:
        """测试API连通性。

        Returns:
            True如果连通，False否则。
        """
        print(f"测试AGNES_LLM API连通性...")
        print(f"  Base URL: {self.base_url}")
        print(f"  Model: {self.model}")
        print(f"  API Key: {self.api_key[:10]}...{self.api_key[-4:]}")

        test_messages = [
            {"role": "system", "content": "You are a helpful assistant. Respond in JSON."},
            {"role": "user", "content": 'Respond with: {"status": "ok", "message": "connection successful"}'},
        ]

        try:
            result = self.chat_json(test_messages, temperature=0.0)
            if "status" in result:
                print(f"✓ API连通成功！响应: {result}")
                return True
            else:
                print(f"✗ API响应异常: {result}")
                return False
        except Exception as e:
            print(f"✗ API连通失败: {e}")
            return False


# 单例模式
_client_instance: Optional[AGNESClient] = None

def get_client() -> AGNESClient:
    """获取AGNESClient单例。"""
    global _client_instance
    if _client_instance is None:
        _client_instance = AGNESClient()
    return _client_instance


if __name__ == "__main__":
    client = AGNESClient()
    success = client.test_connection()
    exit(0 if success else 1)
