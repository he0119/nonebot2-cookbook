from nonebot import get_bot, require

scheduler = require("nonebot_plugin_apscheduler").scheduler


@scheduler.scheduled_job("cron", hour=8, minute=0, second=0)
async def send_message():
    bot = get_bot()

    # 发送消息，以 onebot v11 为例
    # API 详见 https://docs.go-cqhttp.org/api/#%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF
    await bot.send_group_msg(group_id=10000, message="hello world!")
