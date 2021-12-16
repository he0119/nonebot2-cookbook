# 发送消息

发送消息是机器人最基础的一个功能。

在事件响应器中，NoneBot2 提供了一些简单的方法来发送消息。

```python
matcher = on_command("hello")

@matcher.handle()
async def handle_hello(bot: Bot, event: Event, state: T_State):
    # 发送信息
    await matcher.send("hello world!")
    # 或者通过 bot
    await bot.send(event, "hello world!")
```

关于 `matcher` 的其他用法详见 [NoneBot 2 的不同事件处理/逻辑控制函数之间究竟有何区别？](https://github.com/nonebot/discussions/discussions/13#discussioncomment-1447083)

## 完整的例子

以下是一个完整的插件。

```python
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

```
