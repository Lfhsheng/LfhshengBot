# 关于这个~~破~~机器人
实例：**泠风寒声酱！：[@Lfhsheng_bot](https://t.me/Lfhsheng_bot)**

主人：[@Lfhsheng](https://t.me/Lfhsheng)

**欢迎~~调戏~~**
## 使用
```shell
pip install pyTelegramBotAPI
pip install zhconv
```
```python
sudo python main.py
```
新建`config.py`，复制`config.example.py`里的内容，根据需求修改
## 配置自定义词语回复
按[Python List格式](https://www.w3school.com.cn/python/python_lists.asp)修改`keyWordList`即可。
## 一言api
可在`jsonWord`中修改，可参考[Python Json解析](https://www.runoob.com/python/python-json.html)和[Python字典](https://www.runoob.com/python/python-json.html)进行修改

提示：解析后的`Json`为字典形式，不是`List`形式
## 命令
`/tosscoin`：抛硬币

`/meow`：喵

`/ping`：检测机器人状态

`/word`：随机一言

`/wearskirt`：女装一下！
## 其他
可在`config.py`的`pingList`里按[Python List格式](https://www.w3school.com.cn/python/python_lists.asp)修改`ping`随机返回词语
### Todo
* 女装龙虎榜
### Tip
如果出现bug欢迎[issue](https://github.com/Lfhsheng/LfhshengBot/issues/new)，请提供运行系统与Python版本等信息
### 其他项目

[coinBOt - A simple Telegram bot flipping coins](https://github.com/Emojigit/coinBot)

[Gugumoe-bot](https://github.com/GooGuJiang/Gugumoe-bot)
