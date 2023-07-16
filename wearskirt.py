import sqlite3
import datetime
import const
def wearskirt(id ,user):
    base = sqlite3.connect(const.BASE_PATH)
    cursor = base.cursor()
    wearskirt_data = cursor.execute("SELECT * from WEARSKIRT").fetchall()
    flag = False
    for wearskirt_user in wearskirt_data:
        if id in wearskirt_user:
            flag = True
            if wearskirt_user[3] == str(datetime.date.today()):
                return const.RE_WEARSKIRT
            else:
                if wearskirt_user[3] == str(datetime.date.today() - datetime.timedelta(days=1)):
                    day = wearskirt_user[2]
                    new_day = day + 1
                    cursor.execute('''UPDATE WEARSKIRT SET SCORE = %d WHERE ID = %d''' % (new_day, id))
                    cursor.execute(
                            '''UPDATE WEARSKIRT SET DATETIME = "%s" WHERE ID = %d''' % (datetime.date.today(), id))
                    base.commit()
                    return const.WEARSKIRT_SUCCESS % new_day
                else:
                    cursor.execute('''UPDATE WEARSKIRT SET SCORE = %d WHERE ID = %d''' % (1, id))
                    return const.NOT_CONTINUOUS_WEARSKIRT
    if not flag:
        cursor.execute('''INSERT INTO WEARSKIRT (ID,USER,DATETIME,SCORE) VALUES (%d,"%s","%s",%d);''' % (
            id, user, datetime.date.today(), 1))
        base.commit()
        return const.FIRST_WEARSKIRT_SUCCESS