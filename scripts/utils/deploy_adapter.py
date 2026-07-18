#!/usr/bin/env python3
"""部署适配器。

抽象部署接口，支持本地hugo server和云端部署。
"""
from abc import ABC, abstractmethod
from pathlib import Path
import subprocess
import shutil
from typing import Optional


class BaseDeployAdapter(ABC):
    """部署适配器基类。"""

    @abstractmethod
    def build(self, project_root: Path) -> bool:
        """构建站点。"""
        pass

    @abstractmethod
    def serve(self, project_root: Path, port: int = 1313) -> bool:
        """启动服务。"""
        pass

    @abstractmethod
    def deploy(self, project_root: Path) -> bool:
        """部署到目标环境。"""
        pass


class LocalDeployAdapter(BaseDeployAdapter):
    """本地部署适配器（hugo server）。"""

    def build(self, project_root: Path) -> bool:
        print(f"[Local] 构建Hugo站点: {project_root}")
        result = subprocess.run(
            ["hugo", "--gc", "--minify"],
            cwd=str(project_root),
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✓ Hugo构建成功")
            return True
        else:
            print(f"✗ Hugo构建失败: {result.stderr}")
            return False

    def serve(self, project_root: Path, port: int = 1313) -> bool:
        print(f"[Local] 启动Hugo服务: http://localhost:{port}/")
        # 非阻塞启动
        proc = subprocess.Popen(
            ["hugo", "server", "--bind", "0.0.0.0", "--port", str(port), "--buildDrafts"],
            cwd=str(project_root),
        )
        print(f"  PID: {proc.pid}")
        return True

    def deploy(self, project_root: Path) -> bool:
        print("[Local] 本地模式无需部署，使用 hugo serve")
        return self.serve(project_root)


class CloudflarePagesDeployAdapter(BaseDeployAdapter):
    """Cloudflare Pages部署适配器（预留）。

    注意：当前用户无法访问Cloudflare，此适配器仅作为接口预留。
    """

    def __init__(self, api_token: str, account_id: str, project_name: str):
        self.api_token = api_token
        self.account_id = account_id
        self.project_name = project_name
        raise NotImplementedError(
            "CloudflarePagesDeployAdapter 暂未实现。"
            "原因：用户当前无法访问Cloudflare。"
            "请在云端迁移阶段实现此适配器。"
        )

    def build(self, project_root: Path) -> bool:
        raise NotImplementedError("CloudflarePagesDeployAdapter.build 未实现")

    def serve(self, project_root: Path, port: int = 1313) -> bool:
        raise NotImplementedError("CloudflarePagesDeployAdapter.serve 未实现")

    def deploy(self, project_root: Path) -> bool:
        raise NotImplementedError("CloudflarePagesDeployAdapter.deploy 未实现")


class GitHubPagesDeployAdapter(BaseDeployAdapter):
    """GitHub Pages部署适配器（预留）。

    注意：当前用户无法访问GitHub，此适配器仅作为接口预留。
    """

    def __init__(self, repo: str, branch: str = "gh-pages"):
        self.repo = repo
        self.branch = branch
        raise NotImplementedError(
            "GitHubPagesDeployAdapter 暂未实现。"
            "原因：用户当前无法访问GitHub。"
            "请在云端迁移阶段实现此适配器。"
        )

    def build(self, project_root: Path) -> bool:
        raise NotImplementedError("GitHubPagesDeployAdapter.build 未实现")

    def serve(self, project_root: Path, port: int = 1313) -> bool:
        raise NotImplementedError("GitHubPagesDeployAdapter.serve 未实现")

    def deploy(self, project_root: Path) -> bool:
        raise NotImplementedError("GitHubPagesDeployAdapter.deploy 未实现")


def get_deploy_adapter(env_mode: str = "local") -> BaseDeployAdapter:
    """根据环境模式获取部署适配器。"""
    if env_mode == "local":
        return LocalDeployAdapter()
    elif env_mode == "cloud":
        raise NotImplementedError("云端部署模式暂未实现")
    else:
        raise ValueError(f"未知环境模式: {env_mode}")
