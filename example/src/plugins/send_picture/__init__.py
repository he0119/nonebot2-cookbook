from pathlib import Path

from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import on_command

local_picture = on_command("local_picture")


@local_picture.handle()
async def handle_local_picture():
    # 本地图片位置
    path = Path(__file__).parent / "logo.png"
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await local_picture.finish(image)


network_picture = on_command("network_picture")


@network_picture.handle()
async def handle_network_picture():
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await network_picture.finish(image)
