from nonebot.adapters import Bot, Event
from nonebot.plugin import on_command

matcher = on_command("hello")


@matcher.handle()
async def handle_hello(bot: Bot, event: Event):
    # 发送信息
    await matcher.send("hello world!")
    # 或者通过 bot
    await bot.send(event, "hello world!")
