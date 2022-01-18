# 测试命令

怎样才能保证在你不断给机器人添加新功能时不会出错呢？这个问题的答案显然是写测试。

`NoneBot2` 提供了一个名叫 `nonebug` 的测试框架。

接下来就让我们简单了解一下如何使用它吧。

## 安装依赖

```shell
poetry add -D nonebug
# 或者
pip install nonebug
```

## 创建测试文件

通常，我们会在根目录中创建 `tests` 文件夹，测试文件会以 `test_` 开头，例如 `test_send_message.py`

## 添加辅助工具

在 `tests` 文件夹下创建 [`conftest.py`](../../example/tests/conftest.py) 与 [`utils.py`](../../example/tests/utils.py) 文件。

此时目录结构为：

```plaintxt
example/
  tests/
    message/
        test_send_message.py
    conftest.py
    utils.py
```

## 编写测试

以测试 [发送消息](../message/send_message.md) 为例。一个最基本的测试如下。

```python
# 标志着这是一个异步测试。
@pytest.mark.asyncio
async def test_send_message(app: App):
    # 导入需要测试的 matcher
    from src.plugins.send_message import matcher
    from tests.utils import make_fake_event, make_fake_message

    # 此处的 make_fake_message() 可替换为你要发送的平台消息 Message 类型
    Message = make_fake_message()

    async with app.test_matcher(matcher) as ctx:
        bot = ctx.create_bot()

        msg = Message("/hello")
        # 此处的 make_fake_event() 可替换为你要发送的平台事件 Event 类型
        event = make_fake_event(_message=msg)()

        # 模拟机器人收到一个消息内容为 /hello 事件
        ctx.receive_event(bot, event)
        # 验证机器人会发送两次 hello world!
        ctx.should_call_send(event, "hello world!", True)
        ctx.should_call_send(event, "hello world!", True)
```

## 运行测试

测试编写完成后，只需要通过 `poetry run pytest` 或 `pytest` 命令，便可运行测试。

## 示例

详见 [文件夹](../../example/tests)
