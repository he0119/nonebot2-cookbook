# 发送图片

有时候仅发送文字是不够的，这时候发送图片就成了一个很好的选择。

适配器提供的 `MessageSegment` 类中，封装了许多消息相关的方法。如果要发送图片时，我们可以通过 `MessageSegment.image` 方法构造出一个图片消息段。

从 [这里](https://github.com/nonebot/adapter-onebot/blob/999c5c0a58d0a05165562d542a81c903014f614b/nonebot/adapters/onebot/v11/message.py#L87-L110) 可以得知其支持的参数。

## 发送网络上的图片

直接发送网络上的图片。

```python
matcher = on_command("picture")

@matcher.handle()
async def handle_picture():
    # 构造图片消息段
    image = MessageSegment.image("https://v2.nonebot.dev/logo.png")
    # 发送图片
    await matcher.finish(image)
```

## 发送本地图片

```python
matcher = on_command("picture")

@matcher.handle()
async def handle_picture():
    # 本地图片位置
    path = Path("path/to/picture")
    # 构造图片消息段
    image = MessageSegment.image(path)
    # 发送图片
    await matcher.finish(image)
```

## 例子

发送本地与网络图片。

```python
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
```
