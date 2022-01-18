from typing import TYPE_CHECKING, Set

import pytest
from nonebug import App

if TYPE_CHECKING:
    from nonebot.plugin import Plugin


@pytest.mark.asyncio
async def test_send_message(app: App, load_plugin: Set["Plugin"]):
    from src.plugins.send_message import matcher
    from tests.utils import make_fake_event, make_fake_message

    Message = make_fake_message()

    async with app.test_matcher(matcher) as ctx:
        bot = ctx.create_bot()

        msg = Message("/hello")
        event = make_fake_event(_message=msg)()

        ctx.receive_event(bot, event)
        ctx.should_call_send(event, "hello world!", True)
        ctx.should_call_send(event, "hello world!", True)
