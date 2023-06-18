from pathlib import Path

import nonebot
import pytest

# 导入适配器
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter
from nonebot.adapters.onebot.v12 import Adapter as OneBotV12Adapter


@pytest.fixture(scope="session", autouse=True)
def load_bot():
    # 加载适配器
    driver = nonebot.get_driver()
    driver.register_adapter(OneBotV11Adapter)
    driver.register_adapter(OneBotV12Adapter)

    # 加载插件
    nonebot.load_from_toml("pyproject.toml")


@pytest.fixture(autouse=True)
def add_path():
    """添加插件目录到环境变量"""
    import sys

    sys.path.append(str(Path(__file__).parent.parent))
