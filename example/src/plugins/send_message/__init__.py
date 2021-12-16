from nonebot.adapters import Bot, Event
from nonebot.plugin import on_command
from nonebot.typing import T_State

matcher = on_command("hello")


@matcher.handle()
async def handle_hello(bot: Bot, event: Event, state: T_State):
    # 发送信息
    await matcher.send("hello world!")
    # 或者通过 bot
    await bot.send(event, "hello world!")
