from telebot import *
from random import randint,choice
from json import loads,dumps,load
from requests import get
from zhconv import convert
import os
from config import *

jsonPath = "./wearSkirt.json"
if not os.path.exists(jsonPath):
    initDict = {"user":[],"day":[],"count":[]}
    initJson = dumps(initDict)
    print("正在生成用于存储女装次数的json")
    openInitJson = open(jsonPath,"w")
    openInitJson.write(initJson)
    openInitJson.close()
def word():
    jsonWord = get("https://v1.hitokoto.cn/")
    text = loads(jsonWord.text)
    return text["hitokoto"]+"--"+text["from"]
bot = TeleBot(token, parse_mode=None)
@bot.message_handler(commands=["tosscoin"])
def send_coin(message):
    print("有人在抛硬币喵")
    if randint(0,1) == 0:
        bot.reply_to(message,"硬币是反面喵！")
    else:
        bot.reply_to(message,"硬币是正面喵！")
@bot.message_handler(commands=["meow"])
def send_meow(message):
    print("喵")
    bot.reply_to(message,"喵")
@bot.message_handler(commands=["ping"])
def send_ping(message):
    print("有人在ping喵")
    bot.reply_to(message,choice(pingList))
@bot.message_handler(commands=["word"])
def send_word(message):
    print("有人在看一言喵")
    bot.reply_to(message,word())
@bot.message_handler(commands=["wearskirt"])
def wearskirt(message):
    bot.send_chat_action(message.chat.id,'typing')
    messagejson = loads(dumps(message.json))
    try:
        messagejson["reply_to_message"]
    except:
        bot.reply_to(message,"请使用此命令回复一个人的消息喵！")
        return None
    replyMessageFirstName = messagejson["reply_to_message"]["from"]["first_name"]
    if messagejson["reply_to_message"]["from"]["is_bot"] == True:
        bot.reply_to(message,choice(botWearskirt))
        return None
    readJson = open(jsonPath,"r")
    jsonDict = load(readJson)
    userList = jsonDict["user"]
    countList = jsonDict["count"]
    readJson.close()
    try:
        index = userList.index(messagejson["reply_to_message"]["from"]["id"])
        countList[index] += 1
        createJson = {"user":userList,"count":countList}
        newJson = dumps(createJson)
        openJson = open(jsonPath,"w")
        openJson.write(newJson)
        openJson.close()
        bot.reply_to(message,"%s成功女装, 次数%d次" % (replyMessageFirstName,countList[index]))
        print("%s成功女装, 次数%d次" % (replyMessageFirstName,countList[index]))
    except ValueError:
        userList.append(messagejson["reply_to_message"]["from"]["id"])
        countList.append(1)
        createJson = {"user":userList,"count":countList}
        newJson = dumps(createJson)
        openJson = open(jsonPath,"w")
        openJson.write(newJson)
        openJson.close()
        bot.reply_to(message,"%s成功女装, 次数1次" % replyMessageFirstName)
        print("%s成功女装, 次数1次" % replyMessageFirstName)
@bot.message_handler(func=lambda message: True)
def checkKeyWord(message):
    messagejson = loads(dumps(message.json))
    if messagejson["from"]["is_bot"] == True:
        return None
    for listNum in range(0,len(keyWordList)-1):
        messageText = convert(message.text,"zh-cn")
        if keyWordList[listNum][0] in messageText:
            bot.reply_to(message,keyWordList[listNum][1])
            print("关键字已回复")
bot.infinity_polling()