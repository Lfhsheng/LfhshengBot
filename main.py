from telebot import *
from random import randint
token = "在这填上令牌"
pingList = ["喵喵喵","我还活着……","呜呜呜","挠挠挠","伸爪ing"]
wordList = ["人生无常，大肠包小肠","喵你喵！","我在這裡下詛咒，病夫在30歲以前一定會結婚","有時間催促女裝不如寫一兩篇稿子"]
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
    bot.reply_to(message,"喵")
@bot.message_handler(commands=["ping"])
def send_ping(message):
    bot.reply_to(message,pingList[randint(0,len(pingList)-1)])
@bot.message_handler(commands=["word"])
def send_word(message):
    bot.reply_to(message,wordList[randint(0,len(wordList)-1)])
@bot.message_handler(func=lambda message: True)
def checkKeyWord(message):
    print(message.text)
    if "qwq" in message.text:
        bot.reply_to(message,"awa")
    elif "喵" in message.text:
        bot.reply_to(message,"喵！")
    elif "紫砂" in message.text:
        bot.reply_to(message,"不要！")
    elif "Emo酱" in message.text:
        bot.reply_to(message,"Emo酱主义万岁！")
    elif "咕谷酱" in message.text:
        bot.reply_to(message,"咕咕咕！")
bot.infinity_polling()