from telebot import *
from random import randint,choice
from json import loads
from requests import get
from zhconv import convert
token = "在这填上令牌"
pingList = ["喵喵喵","我还活着……","呜呜呜","挠挠挠","伸爪ing"]
keyWordList = [
    ["qwq","awa"],
    ["qaq","quq"],
    ["ava","qwq"],
    ["喵","喵！"],
    ["紫砂","不要！"],
    ["Emo酱","Emo酱主义万岁！"],
    ["EMO酱","黄豆酱真好吃😋"],
    ["咕谷酱","咕咕咕！"],
    ["泠风寒声","泠风寒声翻车车~"],
    ["冷风寒声","是泠风寒声！"],
    ["他妈","他爸"],
    ["泠风寒声酱","谁在叫我（"]
    ]
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
@bot.message_handler(func=lambda message: True)
def checkKeyWord(message):
    for listNum in range(0,len(keyWordList)-1):
        messageText = convert(message.text,"zh-cn")
        if keyWordList[listNum][0] in messageText:
            bot.reply_to(message,keyWordList[listNum][1])
            print("关键字已回复")
bot.infinity_polling()