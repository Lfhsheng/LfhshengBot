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
path = "./data.db"
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
    cursor.execute('''CREATE TABLE NOTE(
        TEXT TEXT
        );''')
    base.commit()
    base.close()
bot = telebot.TeleBot(config["token"],parse_mode="MarkdownV2")
@bot.message_handler(commands=["start","help"])
def send_help(message):
    bot.send_chat_action(message.chat.id,'typing')
    bot.reply_to(message,"试试女装吧, /wearskirt")
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
    for i in data:
        if id in i:
            flag = True
            if i[3] == str(datetime.date.today()):
                bot.edit_message_text("你今天已经女装过了||, 看的出来你真的很喜欢女装||",waiting.chat.id,waiting.message_id)
            else:
                score = i[2]
                newScore = score + randint(1,10)
                cursor.execute('''UPDATE WEARSKIRT SET SCORE = %d WHERE ID = %d''' % (newScore,id))
                base.commit()
                bot.edit_message_text("女装成功, 你目前有%d女装积分" % newScore,waiting.chat.id,waiting.message_id)
    if flag == False:
        newScore = randint(1,10)
        cursor.execute('''INSERT INTO WEARSKIRT (ID,USER,DATETIME,SCORE) VALUES (%d,"%s","%s",%d);''' % (id,user,datetime.date.today(),newScore))
        base.commit()
        bot.edit_message_text("女装成功, 你目前有%d女装积分" % newScore,waiting.chat.id,waiting.message_id)
@bot.message_handler(commands=["wearskirtboard"])
def send_wearskirtboard(message):
    bot.send_chat_action(message.chat.id,'typing')
    waiting = bot.reply_to(message,"查询中, 请稍等……")
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    result = ""
    for i in data:
        result += "[%s](tg://user?id=%d) 有 ``%d`` 女装积分\n" % (i[1],i[0],i[2])
    try:
        bot.edit_message_text(result,waiting.chat.id,waiting.message_id)
    except:
        bot.edit_message_text("目前无人女装（",waiting.chat.id,waiting.message_id)
''''
@bot.message_handler(commands=["ban_me"])
def send_ban_me(message):
    bot.send_chat_action(message.chat.id,'typing')
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot.restrict_chat_member(chat_id, user_id, can_send_messages=False, until_date=1800)
    bot.reply_to(message,"你已被禁言半小时||, 冷静一下吧 ~ ||")
'''
'''
@bot.message_handler(commands=["note"])
def send_note(message):
    bot.send_chat_action(message.chat.id,'typing')
    id = message.json["from"]["id"]
    if not id in config["admin"]:
        bot.reply_to(message,"你无权进行操作||, 你可以试试找管理滥权||")
        return 114
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from NOTE").fetchall()
    try:
        text = message.json["reply_to_message"]["text"]
    except KeyError:
        message_text = message.json["text"]
        try:
            message_int = int(message_text.split(" ")[1])
        except:
            bot.reply_to(message,"查询格式错误")
            return 514
        for i in data:
            if i[0] == message_int:
                bot.reply_to(message,i[1])
        return 1919
    index = []
    for i in data:
        index.append(i[0])
    newIndex = max(index) + 1
    cursor.execute(""INSERT INTO NOTE (ID,TEXT) VALUES (%d,"%s")"" % (newIndex, text))
    base.commit()
    bot.reply_to(message,"笔记记录完成")
    print(data)
'''
@bot.message_handler(commands=["note"])
def send_note(message):
    bot.send_chat_action(message.chat.id,'typing')
    id = message.json["from"]["id"]
    if not id in config["admin"]:
        bot.reply_to(message,"你无权进行操作||, 你可以试试找管理滥权||")
        return 114
    base = sqlite3.connect(path)
    cursor = base.cursor()
    data = cursor.execute("SELECT * from NOTE").fetchall()
    try:
        text = message.json["reply_to_message"]["text"]
    except KeyError:
        message_text = message.json["text"]
        try:
            message_int = int(message_text.split(" ")[1])
        except:
            result = ""
            index = 0
            for i in data:
                index += 1
                result += "%d \- %s\n" % (index,i[0])
            bot.reply_to(message,result)
            return
        try:
            bot.reply_to(message,data[message_int-1][0])
        except IndexError:
            bot.reply_to(message,"索引值错误")
        return
    cursor.execute('INSERT INTO NOTE (TEXT) VALUES ("%s")' % (text))
    base.commit()
    bot.reply_to(message,"笔记记录完成")
    print(data)
bot.infinity_polling()