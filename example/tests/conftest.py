from pathlib import Path
from typing import TYPE_CHECKING, Set

import pytest

if TYPE_CHECKING:
    from nonebot.plugin import Plugin


@pytest.fixture(autouse=True)
def add_path():
    """添加插件目录到环境变量"""
    import sys

    sys.path.append(str(Path(__file__).parent.parent))
