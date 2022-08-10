# 关于这个~~破~~机器人
实例：**泠风寒声の小机器人：[@Lfhsheng_bot](https://t.me/Lfhsheng_bot)**

**欢迎~~调戏~~**
## 使用
```python
python main.py
```
记得在`main.py`里填上机器人的令牌😏
## 配置自定义词语回复
在`bot.infinity_polling()`上方添加如下代码：
```python
@bot.message_handler(regexp='<需要检测的词语>')
def echo_<需要检测的词语>(message):
    bot.reply_to(message,"<需要回复的词语>")
```
## 命令
`/tosscoin`：抛硬币

`/meow`：喵

`/ping`：检测机器人状态
## 其他
可在`main.py`的`pingList`里按[Python List格式](https://www.w3school.com.cn/python/python_lists.asp)修改`ping`随机返回词语

### 其他项目

[coinBOt - A simple Telegram bot flipping coins](https://github.com/Emojigit/coinBot)

[Gugumoe-bot](https://github.com/GooGuJiang/Gugumoe-bot)