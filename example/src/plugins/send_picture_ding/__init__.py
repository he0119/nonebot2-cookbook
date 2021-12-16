from nonebot.adapters import Bot, Event
from nonebot.adapters.ding import MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State

matcher = on_command("picture_ding")


@matcher.handle()
async def handle_picture(bot: Bot, event: Event, state: T_State):
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await matcher.finish(image)
