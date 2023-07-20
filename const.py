CONFIG_PATH = './config.yml'
DATA_BASE_PATH = './data.db'
CONFIG_LIST = ['token', 'admin']
CONFIG_NOT_FOUND = '未找到配置文件, 在 3 秒后自动生成配置文件.'
DATA_BASE_NOT_FOUND = '未找到数据库, 在 3 秒后自动生成数据库.'
INIT_START = '正在初始化…'
INIT_WEAR_SKIRT_BASE = '''
    CREATE TABLE WEAR_SKIRT(
        ID       INT  NOT NULL,
        NAME     TEXT NOT NULL,
        DAY      INT,
        DATETIME TEXT
);'''
INIT_WEAR_SKIRT_RECORD_BASE = '''
    CREATE TABLE WEAR_SKIRT_RECORD(
        TEXT     TEXT
);'''
INIT_SUCCESS = '初始化成功, 请填写配置后重启机器人.'
START_SUCCESS = '机器人启动成功! 使用 Ctrl + C 键停止机器人.'
EXIT = '正在停止机器人…'

PING_REPLY = '还活着呢喵. '
HELP_TEXT = '文档: https://github.com/Lfhsheng/LfhshengBot/blob/main/README.md'

WEAR_SKIRT_WAITING = '正在女装中, 请稍等…'
LOG_WEARING_SKIRT = '{user_name} 正在女装.'
WEAR_SKIRT_INSERT = 'INSERT INTO WEAR_SKIRT (ID, NAME, DAY, DATETIME) VALUES (?, ?, ?, ?) '
WEAR_SKIRT_UPDATE_DAY = 'UPDATE WEAR_SKIRT SET DAY = ? WHERE ID = ? '
WEAR_SKIRT_UPDATE_DATETIME = 'UPDATE WEAR_SKIRT SET DATETIME = ? WHERE ID = ? '
WEAR_SKIRT_SUCCESS = '女装成功, 你已女装 {wear_skirt_day} 天.'
REPEAT_WEAR_SKIRT = '你今天已经女装过了qwq<tg-spoiler>, 看的出来你真的很爱女装</tg-spoiler>.'
NOT_CONTINUOUS_WEAR_SKIRT = '未连续女装, 你已女装 {wear_skirt_day} 天<s>, 女装需要坚持</s>.'

WEAR_SKIRT_BOARD_WAITING = '正在加载女装龙虎榜, 请稍等…'
LOG_WEARING_SKIRT_BOARD = '{user_name} 正在查看女装龙虎榜中…'
NOBODY_WEAR_SKIRT = '目前无人女装<tg-spoiler> ,快使用 <code>/wear_skirt</code> 女装吧 </tg-spoiler>!'
WEAR_SKIRT_BOARD_INFO = '<a href="tg://user?id={user_id}" >{user_name}</a> 女装了 {day} 天.\n'

WEAR_SKIRT_RECORD_WAITING = '正在记录女装语句中, 请稍等…'
WEAR_SKIRT_CAN_NOT_RECORD = '只有管理员才能记录女装语录的<s>, 叫可爱 (?) 的管理员滥权一下吧qwq</s>.'
WEAR_SKIRT_RECORD_NO_REPLY = '请用这个指令回复要记录的女装语句.'
WEAR_SKIRT_RECORD_INSERT = 'INSERT INTO WEAR_SKIRT_RECORD VALUES (?) '
WEAR_SKIRT_RECORD_SUCCESS = '记录成功.'
WEAR_SKIRT_SAYINGS_EMPTY = '当前没有女装语录<s>, 管理女装后就有了</s>!'
WEAR_SKIRT_SAYINGS_DROP_TABLE = 'DROP TABLE WEAR_SKIRT_RECORD;'
WEAR_SKIRT_SAYINGS_DROP_TABLE_SUCCESS = '删表跑路成功.'
