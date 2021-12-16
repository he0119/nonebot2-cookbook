# 发送图片

有时候仅发送文字是不够的，这时候发送图片就成了一个很好的选择。

适配器提供的 `MessageSegment` 类中，封装了很多消息相关的方法。如果要发送图片时，我们可以通过 `MessageSegment.image` 方法构造出一个图片消息段。

从 [这里](https://github.com/nonebot/nonebot2/blob/cfd992b6b11be61798bf95519e193d578b7efe01/packages/nonebot-adapter-cqhttp/nonebot/adapters/cqhttp/message.py#L86) 可以得知其支持的参数。

## 发送网络上的图片

直接发送网络上的图片。

```python
matcher = on_command("picture")

@matcher.handle()
async def handle_picture(bot: Bot, event: Event, state: T_State):
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await matcher.finish(image)
```

## 发送本地图片

```python
matcher = on_command("picture")

@matcher.handle()
async def handle_picture(bot: Bot, event: Event, state: T_State):
    # 本地图片位置
    path = Path("path/to/picture")
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await matcher.finish(image)
```

## [ding adapter](https://github.com/nonebot/nonebot2/tree/cfd992b6b11be61798bf95519e193d578b7efe01/packages/nonebot-adapter-ding)

如果是另外的适配器呢？通过查看 [文档](https://v2.nonebot.dev/guide/ding-guide.html#%E5%A4%9A%E7%A7%8D%E6%B6%88%E6%81%AF%E6%A0%BC%E5%BC%8F)
> 其他消息格式请查看 钉钉适配器的 MessageSegment，里面封装了很多有关消息的方法，比如 code、image、feedCard 等。

通过查看 [MessageSegment]((https://github.com/nonebot/nonebot2/blob/cfd992b6b11be61798bf95519e193d578b7efe01/packages/nonebot-adapter-ding/nonebot/adapters/ding/message.py#L66)) 类，我们可以从中得知，其 `image` 方法的参数支持图片网址。

```python
# 注意，此时的 MessageSegment 就应该从 ding adapter 中导入
from nonebot.adapters.ding import MessageSegment

matcher = on_command("picture")

@matcher.handle()
async def handle_picture(bot: Bot, event: Event, state: T_State):
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await matcher.finish(image)
```

## 例子

发送本地与网络图片。

```python
from pathlib import Path

from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State

local_picture = on_command("local_picture")


@local_picture.handle()
async def handle_local_picture(bot: Bot, event: Event, state: T_State):
    # 本地图片位置
    path = Path(__file__).parent / "logo.png"
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await local_picture.finish(image)


network_picture = on_command("network_picture")


@network_picture.handle()
async def handle_network_picture(bot: Bot, event: Event, state: T_State):
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await network_picture.finish(image)
```

如果是使用 钉钉 适配器

```python
from nonebot.adapters import Bot, Event
from nonebot.adapters.ding import MessageSegment
from nonebot.plugin import on_command
from nonebot.typing import T_State

matcher = on_command("picture")


@matcher.handle()
async def handle_picture(bot: Bot, event: Event, state: T_State):
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await matcher.finish(image)
```
