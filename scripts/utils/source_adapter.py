#!/usr/bin/env python3
"""数据源适配器。

抽象数据源接口，支持本地Mock和云端API两种模式。
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pathlib import Path
import json


class BaseSourceAdapter(ABC):
    """数据源适配器基类。"""

    @abstractmethod
    def fetch_terms(self) -> List[Dict[str, Any]]:
        """获取术语列表。"""
        pass

    @abstractmethod
    def fetch_term_detail(self, term_id: str) -> Optional[Dict[str, Any]]:
        """获取术语详情。"""
        pass

    @abstractmethod
    def search_terms(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """搜索术语。"""
        pass


class LocalSourceAdapter(BaseSourceAdapter):
    """本地数据源适配器（从种子库读取）。"""

    def __init__(self, seed_file: Path):
        self.seed_file = seed_file
        self._cache: Optional[List[Dict[str, Any]]] = None

    def fetch_terms(self) -> List[Dict[str, Any]]:
        if self._cache is None:
            with open(self.seed_file, "r", encoding="utf-8") as f:
                self._cache = json.load(f)
        return self._cache

    def fetch_term_detail(self, term_id: str) -> Optional[Dict[str, Any]]:
        terms = self.fetch_terms()
        for term in terms:
            if term.get("term_id") == term_id:
                return term
        return None

    def search_terms(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        terms = self.fetch_terms()
        query_lower = query.lower()
        results = [
            term for term in terms
            if query_lower in term.get("english", "").lower()
            or query_lower in term.get("term_id", "").lower()
        ]
        return results[:limit]


class CloudSourceAdapter(BaseSourceAdapter):
    """云端数据源适配器（预留接口，未来对接Wikipedia/arXiv等）。

    注意：当前用户无法访问国外网站，此适配器仅作为接口预留，
    实际功能待云端迁移时实现。
    """

    def __init__(self, api_endpoints: Dict[str, str]):
        self.api_endpoints = api_endpoints
        raise NotImplementedError(
            "CloudSourceAdapter 暂未实现。"
            "原因：用户当前无法访问国外API。"
            "请在云端迁移阶段实现此适配器。"
        )

    def fetch_terms(self) -> List[Dict[str, Any]]:
        raise NotImplementedError("CloudSourceAdapter.fetch_terms 未实现")

    def fetch_term_detail(self, term_id: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError("CloudSourceAdapter.fetch_term_detail 未实现")

    def search_terms(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        raise NotImplementedError("CloudSourceAdapter.search_terms 未实现")


def get_source_adapter(env_mode: str = "local") -> BaseSourceAdapter:
    """根据环境模式获取数据源适配器。"""
    if env_mode == "local":
        from scripts.config import config
        return LocalSourceAdapter(seed_file=config.paths.seed_file)
    elif env_mode == "cloud":
        raise NotImplementedError("云端模式暂未实现")
    else:
        raise ValueError(f"未知环境模式: {env_mode}")
