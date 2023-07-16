import log
import requests
import telebot
import sqlite3
import const
import os
import yaml
import wearskirt

log.logger.info(requests.get('https://v1.hitokoto.cn/?encode=text').text + ' - 一言')

path = "./data.db"
if not os.path.exists(path):
    base = sqlite3.connect(path)
    cursor = base.cursor()
    cursor.execute(const.INIT_BASE_WEARSKIRT)
    base.commit()
    base.close()
if os.path.exists("./config.yml"):
    configText = open("./config.yml", 'r', encoding='utf-8')
    config = yaml.safe_load(configText)
else:
    raise Exception("Config not found")
bot = telebot.TeleBot(config['token'], parse_mode='MarkdownV2')
log.logger.info('bot运行中……')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, 'To Do')
    # print(message)


@bot.message_handler(commands=["wearskirt"])
def send_wearskirt(message):
    bot.send_chat_action(message.chat.id, 'typing')
    waiting = bot.reply_to(message, "正在女装中, 请稍等……")
    id = message.json["from"]["id"]
    user = message.json["from"]["first_name"]
    log.logger.info('%s正在尝试女装' % user)
    bot.edit_message_text(wearskirt.wearskirt(id, user), waiting.chat.id, waiting.message_id)
@bot.message_handler(commands=["wearskirtboard"])
def send_wearskirtboard(message):
    bot.send_chat_action(message.chat.id,'typing')
    waiting = bot.reply_to(message,"查询中, 请稍等……")
    id = message.json["from"]["id"]
    if not id in config['admin']:
        bot.edit_message_text('只有管理员才能查看女装榜的qwq|| ,要不让叫管理滥权一下? ||', waiting.chat.id, waiting.message_id)
        return 114514
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    result = ""
    for i in data:
        result += "[%s](tg://user?id=%d) 女装了 %d 天\n" % (i[1],i[0],i[2])
    try:
        bot.edit_message_text(result,waiting.chat.id,waiting.message_id)
    except:
        bot.edit_message_text("目前无人女装|| ,快使用 `/wearskirt` 女装吧\! ||",waiting.chat.id,waiting.message_id)
@bot.message_handler(commands=["del"])
def del_wearskirt(message):
    bot.send_chat_action(message.chat.id, 'typing')
    waiting = bot.reply_to(message, "删除中, 请稍等……")
    id = message.json["from"]["id"]
    if not id in config['admin']:
        bot.edit_message_text('只有管理员才能删除的qwq|| ,要不让叫管理滥权一下? ||', waiting.chat.id,
                              waiting.message_id)
        return 1919
    try:
        del_id = message.json["text"].split(' ')[1]
    except IndexError:
        bot.edit_message_text('格式错误', waiting.chat.id,
                              waiting.message_id)
        return 810
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    for i in data:
        if i[0] == int(del_id):
            cursor.execute('''DELETE FROM WEARSKIRT WHERE ID = %d''' % id)
            bot.edit_message_text('删除成功', waiting.chat.id,
                                  waiting.message_id)
            base.commit()
    else:
        bot.edit_message_text('删除失败', waiting.chat.id,
                                  waiting.message_id)
        base.commit()
bot.infinity_polling()
