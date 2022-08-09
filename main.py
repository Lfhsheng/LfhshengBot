from telebot import *
from random import randint
token = "在这填上令牌"
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
#@bot.message_handler(func=lambda message: True) 
#def echo_all(message):
#    bot.reply_to(message,"喵！")
bot.infinity_polling()