# 在定时任务中发送消息

当你想定时发送消息时，会发现在事件响应器外的函数中，matcher 或者 bot 和 event 是不存在的，无法通过上述方法快捷发送消息。

此时，NoneBot 提供了 `get_bots` 与 `get_bot` 方法，方便开发者在事件响应器外获取 bot 实例。

## get_bot

获取一个 bot 实例。

```python
@scheduler.scheduled_job("cron", hour=8, minute=0, second=0)
async def send_message():
    bot = get_bot()

    # 发送消息，以 onebot 为例
    # API 详见 https://docs.go-cqhttp.org/api/#%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF
    await bot.send_group_msg(group_id==10000, message="hello world!")
```

或者你也可以通过传入 `self_id`，获取指定 bot 实例。

```python
@scheduler.scheduled_job("cron", hour=8, minute=0, second=0)
async def send_message():
    # 获取 self_id 为 12345 的 bot 实例
    bot = get_bot("12345")

    await bot.send_group_msg(group_id=10000, message="hello world!")
```

## get_bots

获取所有连接 NoneBot 的 bot 实例。

```python
@scheduler.scheduled_job("cron", hour=8, minute=0, second=0)
async def send_message():
    # 获取 self_id 为 12345 的 bot 实例
    bots = get_bots()

    # 所有机器人都向群 ID 为 10000 的群发送消息
    for bot in bots:
        await bot.send_group_msg(group_id=10000, message="hello world!")
```

## 示例

以下是一个完整的插件。

每天早晨 8 点发送 `hello world!` 到群号 `10000`。

```python
from nonebot import get_bot, require

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", hour=8, minute=0, second=0)
async def send_message():
    bot = get_bot()

    # 发送消息，以 onebot 为例
    # API 详见 https://docs.go-cqhttp.org/api/#%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF
    await bot.send_group_msg(group_id=10000, message="hello world!")
```
