from tokenize import Token
from telebot import *
from random import randint
import token
token = "在这填上令牌"
pingList = ["喵喵喵","我还活着……","呜呜呜","挠挠挠","伸爪ing"]
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
@bot.message_handler(regexp='qaq')
def echo_Qaq(message):
    bot.reply_to(message,"喵！")
@bot.message_handler(regexp='紫砂')
def echo_紫砂(message):
    bot.reply_to(message,"不要！")
@bot.message_handler(regexp='Emo酱')
def echo_Emo酱(message):
    bot.reply_to(message,"Emo酱主义万岁！")
bot.infinity_polling()