#!/usr/bin/env python3
"""数据源抓取器基类。

定义统一的抓取接口，所有具体抓取器（Wikipedia/HuggingFace/arXiv）继承此类。
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pathlib import Path
import json
import os
import time
import urllib.request
import urllib.error
import ssl


# 系统代理（已验证 127.0.0.1:7897 可用）
_PROXY_HOST = os.environ.get("PROXY_HOST", "127.0.0.1")
_PROXY_PORT = os.environ.get("PROXY_PORT", "7897")
_PROXY_URL = f"http://{_PROXY_HOST}:{_PROXY_PORT}"

# SSL上下文（不验证证书，因代理可能MitM）
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

# 默认User-Agent
DEFAULT_USER_AGENT = "AITermsDictionary/1.0 (educational project; contact@example.com)"


def get_proxied_opener() -> urllib.request.OpenerDirector:
    """获取带代理的URL opener。"""
    proxy_handler = urllib.request.ProxyHandler({
        "http": _PROXY_URL,
        "https": _PROXY_URL,
    })
    https_handler = urllib.request.HTTPSHandler(context=_SSL_CTX)
    opener = urllib.request.build_opener(proxy_handler, https_handler)
    return opener


def fetch_url(
    url: str,
    timeout: int = 30,
    retries: int = 3,
    delay: float = 2.0,
    user_agent: str = DEFAULT_USER_AGENT,
) -> Optional[str]:
    """通过代理抓取URL内容。

    Args:
        url: 目标URL
        timeout: 单次请求超时秒数
        retries: 重试次数
        delay: 重试间隔秒数
        user_agent: User-Agent字符串

    Returns:
        响应文本，失败返回None
    """
    opener = get_proxied_opener()
    last_error = None

    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": user_agent,
                "Accept": "application/json,text/xml,*/*",
                "Accept-Language": "en-US,en;q=0.9",
            })
            resp = opener.open(req, timeout=timeout)
            content = resp.read().decode("utf-8", errors="replace")
            return content
        except urllib.error.HTTPError as e:
            last_error = f"HTTPError {e.code}: {e.reason}"
            if e.code in (404, 403):
                # 这些错误不重试
                break
        except urllib.error.URLError as e:
            last_error = f"URLError: {e.reason}"
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"

        if attempt < retries - 1:
            time.sleep(delay)

    print(f"  ✗ 抓取失败 {url}: {last_error}")
    return None


class BaseFetcher(ABC):
    """数据源抓取器基类。"""

    name: str = "base"

    @abstractmethod
    def fetch_terms(self, limit: int = 500) -> List[Dict[str, Any]]:
        """抓取术语列表。

        Args:
            limit: 最大抓取数量

        Returns:
            术语字典列表，每个字典包含：
            - term_id: str (slug格式)
            - english: str (英文术语名)
            - category: str (5大类之一)
            - subcategory: str
            - source: str (数据源标识)
            - source_url: str
            - aliases: List[str]
            - importance: int (1-5)
        """
        pass

    def normalize_term(self, name: str) -> str:
        """将术语名归一化为title case。"""
        name = name.strip()
        # 去除括号内容
        if " (" in name:
            name = name.split(" (")[0].strip()
        # 去除disambiguation后缀
        if name.endswith(" (disambiguation)"):
            name = name[:-15].strip()
        return name

    def slugify(self, name: str) -> str:
        """将术语名转为slug格式term_id。"""
        import re
        s = name.lower().strip()
        s = re.sub(r"[^\w\s-]", "", s)
        s = re.sub(r"[\s_-]+", "_", s)
        s = s.strip("_")
        return s

    def categorize(self, name: str, description: str = "") -> str:
        """根据术语名和描述推断分类。

        返回5大类之一：
        - basic_concepts
        - training_techniques
        - application_paradigms
        - engineering_practice
        - ethics_safety
        """
        text = (name + " " + description).lower()

        # 关键词匹配（按优先级）
        ethics_keywords = ["ethic", "safety", "fairness", "bias", "privacy",
                          "alignment", "responsible", "trustworthy", "governance",
                          "transparency", "accountab", "consent", "gdpr", "harm",
                          "toxic", "jailbreak", "deepfake", "misinformation",
                          "watermark", "red team", "safety"]
        if any(kw in text for kw in ethics_keywords):
            return "ethics_safety"

        training_keywords = ["training", "learning", "optimization", "gradient",
                            "backprop", "loss", "regulariz", "dropout", "epoch",
                            "fine-tun", "fine_tun", "pretrain", "pre-train",
                            "reinforcement", "supervised", "unsupervised",
                            "transfer learn", "federated", "quantiz", "pruning",
                            "distill", "batch norm", "layer norm", "activation"]
        if any(kw in text for kw in training_keywords):
            return "training_techniques"

        app_keywords = ["agent", "rag", "retrieval", "prompt", "chain of thought",
                       "reason", "planning", "tool use", "function call",
                       "chatbot", "assistant", "generation", "summariz",
                       "translation", "embed", "search", "recommend",
                       "vision", "image", "video", "speech", "nlp",
                       "language model", "llm", "multimodal", "dialogue"]
        if any(kw in text for kw in app_keywords):
            return "application_paradigms"

        eng_keywords = ["api", "server", "deploy", "docker", "kubernetes",
                       "microservice", "latency", "throughput", "cach",
                       "scalab", "monitor", "observ", "log", "trace",
                       "inference", "serv", "endpoint", "rest", "graphql",
                       "webhook", "sdk", "cli", "framework", "library"]
        if any(kw in text for kw in eng_keywords):
            return "engineering_practice"

        # 默认分类
        return "basic_concepts"

    def save_raw(self, terms: List[Dict[str, Any]], filename: str) -> Path:
        """保存原始抓取结果到data/raw/。"""
        project_root = Path(__file__).parent.parent.parent
        raw_dir = project_root / "data" / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        filepath = raw_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(terms, f, ensure_ascii=False, indent=2)
        return filepath
