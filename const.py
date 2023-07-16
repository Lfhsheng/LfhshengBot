BASE_PATH = './data.db'
INIT_BASE_WEARSKIRT = '''CREATE TABLE WEARSKIRT(
        ID       INT  NOT NULL,
        USER     TEXT NOT NULL,
        SCORE    INT,
        DATETIME TEXT
        );'''
RE_WEARSKIRT = '你今天已经女装过了||, 看的出来你真的很喜欢女装||'
WEARSKIRT_SUCCESS = '女装成功, 你已女装 %d 天'
FIRST_WEARSKIRT_SUCCESS = '女装成功, 你已女装 1 天'
NOT_CONTINUOUS_WEARSKIRT = '未连续女装, 你已女装 1 天||, 女装需要坚持||'