import sqlite3
import const
import datetime


def wear_skirt(user_id, user_name):
    base_connect = sqlite3.connect(const.DATA_BASE_PATH)
    cursor = base_connect.cursor()
    already_wear_skirt_id = base_connect.execute('SELECT * FROM WEAR_SKIRT').fetchall()
    for user in already_wear_skirt_id:
        if user_id == user[0]:
            yesterday = datetime.date.today() - datetime.timedelta(days=1)
            if user[3] == str(yesterday):
                wear_skirt_day = user[2] + 1
                cursor.execute(const.WEAR_SKIRT_UPDATE_DAY, (wear_skirt_day, user[0]))
                cursor.execute(const.WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                base_connect.commit()
                return const.WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
            elif user[3] == str(datetime.date.today()):
                return const.REPEAT_WEAR_SKIRT
            else:
                wear_skirt_day = 1
                cursor.execute(const.WEAR_SKIRT_UPDATE_DAY, (1, user[0]))
                cursor.execute(const.WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                base_connect.commit()
                return const.NOT_CONTINUOUS_WEAR_SKIRT.format(wear_skirt_day=wear_skirt_day)
    wear_skirt_day = 1
    cursor.execute(const.WEAR_SKIRT_INSERT, (user_id, user_name, 1, datetime.date.today()))
    base_connect.commit()
    return const.WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)


def wear_skirt_board():
    base_connect = sqlite3.connect(const.DATA_BASE_PATH)
    already_wear_skirt_id = base_connect.execute('SELECT ID,NAME,DAY FROM WEAR_SKIRT').fetchall()
    result = ''
    for user in already_wear_skirt_id:
        result += const.WEAR_SKIRT_BOARD_INFO.format(
            user_id=str(user[0]), user_name=user[1], day=user[2])
    if result == '':
        return const.NOBODY_WEAR_SKIRT
    return result
