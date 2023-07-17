import telebot
import yaml
import const
import os
from time import sleep
from loguru import logger
import sys
import sqlite3
import wear_skirt

if os.path.exists(const.CONFIG_PATH) is False:
    logger.info(const.CONFIG_NOT_FOUND)
    sleep(3)
    logger.info(const.INIT_START)
    with open('./config.yml', 'w') as f:
        config_result = ''
        for config_item in const.CONFIG_LIST:
            config_result += (config_item + ': \n')
        f.write(config_result)
    logger.info(const.INIT_SUCCESS)
    sys.exit()
if os.path.exists(const.DATA_BASE_PATH) is False:
    logger.info(const.DATA_BASE_NOT_FOUND)
    sleep(3)
    base = sqlite3.connect(const.DATA_BASE_PATH)
    cursor = base.cursor()
    cursor.execute(const.INIT_BASE)
    base.commit()
    base.close()
with open('./config.yml', 'r') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
bot = telebot.TeleBot(config['token'], parse_mode='HTML')


@bot.message_handler(commands=['ping'])
def bot_ping(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, const.PING_REPLY)


@bot.message_handler(commands=['start', 'help'])
def bot_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, const.HELP_TEXT)


@bot.message_handler(commands=['wear_skirt'])
def bot_wear_skirt(message):
    bot.send_chat_action(message.chat.id, 'typing')
    waiting = bot.reply_to(message, const.WEAR_SKIRT_WAITING)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logger.info(const.LOG_WEARING_SKIRT.format(user_name=user_name))
    bot.edit_message_text(wear_skirt.wear_skirt(user_id, user_name), waiting.chat.id, waiting.message_id)


@bot.message_handler(commands=['wear_skirt_board'])
def bot_wear_skirt_board(message):
    bot.send_chat_action(message.chat.id, 'typing')
    waiting = bot.reply_to(message, const.WEAR_SKIRT_BOARD_WAITING)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logger.info(const.LOG_WEARING_SKIRT_BOARD.format(user_name=user_name))
    for admin_id in config['admin']:
        if user_id == admin_id:
            bot.edit_message_text(wear_skirt.wear_skirt_board(),
                                  waiting.chat.id,
                                  waiting.message_id)
            return 114514
    bot.edit_message_text('只有管理员才能查看女装榜的qwq<tg-spoiler> ,要不让叫管理滥权一下? </tg-spoiler>',
                          waiting.chat.id,
                          waiting.message_id)


if __name__ == '__main__':
    logger.info(const.START_SUCCESS)
    bot.infinity_polling()
