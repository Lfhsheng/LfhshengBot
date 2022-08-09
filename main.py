from telebot import *
from random import randint
bot = TeleBot("在这填上令牌", parse_mode=None)
@bot.message_handler(commands=['tosscoin'])
def send_coin(message):
    if randint(0,1) == 0:
        bot.reply_to(message,"硬币是反面喵！")
    else:
        bot.reply_to(message,"硬币是正面喵！")
bot.infinity_polling()
