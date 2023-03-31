import telebot
import yaml
import os
import sqlite3
import datetime
from random import randint
from loguru import logger
if os.path.exists("./config.yml"):
    configText = open("./config.yml", 'r', encoding='utf-8')
    config = yaml.safe_load(configText)
else:
    raise Exception("Config not found")
path = "./wearskirt.db"
if not os.path.exists(path):
    base = sqlite3.connect(path)
    cursor = base.cursor()
    cursor.execute('''CREATE TABLE WEARSKIRT(
        ID       INT  NOT NULL,
        USER     TEXT NOT NULL,
        SCORE    INT,
        DATETIME TEXT
        );''')
    base.commit()
    base.close()
bot = telebot.TeleBot(config["token"],parse_mode="markdown")
@bot.message_handler(commands=["ping"])
def send_ping(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.reply_to(message,"还活着呢")
    logger.info("回复ping成功")
@bot.message_handler(commands=["wearskirt"])
def send_wearskirt(message):
    bot.send_chat_action(message.chat.id,'typing')
    waiting = bot.reply_to(message,"正在女装中, 请稍等……")
    id = message.json["from"]["id"]
    user = message.json["from"]["first_name"]
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    flag = False
    score = i[2]
    for i in data:
        if id in i:
            flag = True
            if i[3] == str(datetime.date.today()):
                bot.edit_message_text("你今天已经女装过了", waiting.chat.id, waiting.message_id)
            else:
                newScore = score + randint(1,10)
                cursor.execute('''UPDATE WEARSKIRT SET SCORE = %d WHERE ID = %d''' % (newScore,id))
                base.commit()
                bot.edit_message_text("女装成功, 你目前有%d女装积分" % newScore, waiting.chat.id, waiting.message_id)
    if flag == False:
        newScore = score + randint(1,10)
        cursor.execute('''INSERT INTO WEARSKIRT (ID,USER,DATETIME,SCORE) VALUES (%d,"%s","%s",%d);''' % (id,user,datetime.date.today(),newScore))
        base.commit()
        bot.edit_message_text("女装成功, 你目前有%d女装积分" % newScore, waiting.chat.id, waiting.message_id)
@bot.message_handler(commands=["wearskirtboard"])
def send_wearskirtboard(message):
    bot.send_chat_action(message.chat.id,'typing')
    waiting = bot.reply_to(message,"查询中, 请稍等……")
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    result = ""
    for i in data:
        result += "[%s](tg://user?id=%d) 有 ``%d`` 女装积分" % (i[1],i[0],i[2])
    bot.edit_message_text(result, waiting.chat.id, waiting.message_id)
@bot.message_handler(commands=["ban_me"])
def send_ban_me(message):
    pass # To Do
bot.infinity_polling()