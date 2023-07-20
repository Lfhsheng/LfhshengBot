# 关于这个~~破~~机器人

## 功能：

- [x] 赛博女装
- [x] 女装龙虎榜
- [ ] 随机输出女装语录
- [ ] 自定义女装语录
- [ ] 二维码生成
- [ ] 增加更多管理~~滥权~~功能

## 配置与运行

将本仓库 `clone` 到本地：

```sh
$ git clone https://github.com/Lfhsheng/LfhshengBot
```

安装所需模块：

```sh
$ pip install -r requirements.txt
```

初始化：

```sh
$ python3 main.py
```

配置 `config.yml`

重启机器人：

```sh
$ python3 main.py
```

## 指令列表

| 指令名称         | 描述                     |
| ---------------- | ------------------------ |
| wear_skirt       | 女装                     |
| wear_skirt_board | 女装龙虎榜               |
| record           | 记录女装语录（仅管理员） |
| sayings          | 获取女装语录             |
| help             | 获取帮助                 |

## 配置文件

| 配置项名称 | 描述                | 类型   |
| ---------- | ------------------- | ------ |
| token      | Telegram机器人token | string |
| admin      | 机器人管理员列表    | list   |

## 其他项目

[coinBOt - A simple Telegram bot flipping coins](https://github.com/Emojigit/coinBot)

[Gugumoe-bot](https://github.com/GooGuJiang/Gugumoe-bot)
