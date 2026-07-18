#!/usr/bin/env python3
"""统一配置管理模块。

所有路径和环境变量通过此模块集中管理，支持ENV_MODE切换。
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass, field
from typing import Optional


# 项目根目录（aiterms-dictionary/）
PROJECT_ROOT = Path(__file__).parent.parent

# 加载环境变量
ENV_MODE = os.getenv("ENV_MODE", "local")
if ENV_MODE == "local":
    load_dotenv(PROJECT_ROOT / ".env.local")
else:
    load_dotenv(PROJECT_ROOT / ".env.cloud")


@dataclass
class SiteConfig:
    """站点配置。"""
    base_url: str = field(default_factory=lambda: os.getenv("SITE_BASE_URL", "http://localhost:1313/"))
    env_mode: str = field(default_factory=lambda: ENV_MODE)
    title: str = "AI Terms Dictionary"
    description: str = "Comprehensive multilingual AI terminology dictionary"


@dataclass
class AGNESConfig:
    """AGNES_LLM配置。"""
    api_key: str = field(default_factory=lambda: os.getenv("AGNES_LLM_API_KEY", ""))
    base_url: str = field(default_factory=lambda: os.getenv("AGNES_LLM_BASE_URL", "https://apihub.agnes-ai.com/v1"))
    model: str = field(default_factory=lambda: os.getenv("AGNES_LLM_MODEL", "agnes-2.0-flash"))
    temperature: float = 0.3
    max_retries: int = 3
    cache_enabled: bool = True


@dataclass
class DataPaths:
    """数据路径配置。"""
    project_root: Path = PROJECT_ROOT
    seeds_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "seeds")
    queue_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "queue")
    mock_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "mock")
    golden_samples_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "golden_samples")
    translations_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "translations")
    progress_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "data" / "progress")
    cache_dir: Path = field(default_factory=lambda: PROJECT_ROOT / os.getenv("CACHE_DIR", ".cache/agnes").lstrip("./"))
    logs_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "logs")
    reports_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "reports")

    @property
    def seed_file(self) -> Path:
        return self.seeds_dir / "seed_terms.json"

    @property
    def pending_terms_file(self) -> Path:
        return self.queue_dir / "pending_terms.json"

    @property
    def generated_definitions_file(self) -> Path:
        return self.queue_dir / "generated_definitions.json"

    @property
    def translated_terms_file(self) -> Path:
        return self.queue_dir / "translated_terms.json"

    @property
    def progress_file(self) -> Path:
        return self.progress_dir / "progress.json"

    @property
    def failed_terms_file(self) -> Path:
        return self.queue_dir / "failed_terms.json"

    @property
    def glossary_file(self) -> Path:
        return self.translations_dir / "glossary.json"


@dataclass
class HugoConfig:
    """Hugo配置。"""
    project_root: Path = PROJECT_ROOT
    config_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "config")
    content_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "content")
    layouts_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "layouts")
    static_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "static")
    themes_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "themes")
    public_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "public")
    i18n_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "i18n")


class Config:
    """统一配置单例。"""

    _instance: Optional["Config"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.site = SiteConfig()
        self.agnes = AGNESConfig()
        self.paths = DataPaths()
        self.hugo = HugoConfig()

        # 创建必要目录
        for path in [
            self.paths.seeds_dir, self.paths.queue_dir, self.paths.mock_dir,
            self.paths.golden_samples_dir, self.paths.translations_dir,
            self.paths.progress_dir, self.paths.cache_dir,
            self.paths.logs_dir, self.paths.reports_dir,
        ]:
            path.mkdir(parents=True, exist_ok=True)

    def get_supported_languages(self) -> list:
        """获取支持的语种列表。"""
        return ["en", "es", "de", "ja", "fr", "zh"]

    def get_target_languages(self) -> list:
        """获取目标翻译语种（不含英文）。"""
        return ["es", "de", "ja", "fr", "zh"]

    def is_local(self) -> bool:
        """是否本地模式。"""
        return self.site.env_mode == "local"

    def is_cloud(self) -> bool:
        """是否云端模式。"""
        return self.site.env_mode == "cloud"

    def print_summary(self) -> None:
        """打印配置摘要。"""
        print("=" * 60)
        print("配置摘要")
        print("=" * 60)
        print(f"  ENV_MODE: {self.site.env_mode}")
        print(f"  SITE_BASE_URL: {self.site.base_url}")
        print(f"  AGNES_LLM_API_KEY: {self.agnes.api_key[:10]}...{self.agnes.api_key[-4:] if len(self.agnes.api_key) > 14 else '***'}")
        print(f"  AGNES_LLM_BASE_URL: {self.agnes.base_url}")
        print(f"  AGNES_LLM_MODEL: {self.agnes.model}")
        print(f"  CACHE_DIR: {self.paths.cache_dir}")
        print(f"  PROJECT_ROOT: {self.paths.project_root}")
        print(f"  Supported Languages: {', '.join(self.get_supported_languages())}")
        print("=" * 60)


# 全局单例
config = Config()


if __name__ == "__main__":
    config.print_summary()
