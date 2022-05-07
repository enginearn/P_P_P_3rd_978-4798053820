import json

DATA_FLE = "norilog.json"

def save_data(start, finish, memo, created_at):
    """記録データを保存
    :param start: 乗った駅
    :type start: str
    :param finish: 降りた駅
    :type finish: str
    :param memo: 乗り降りのメモ
    :type memo: str
    :param created_at: 乗り降りの日付
    :type created_at: datetime.datetime
    :return: None
    """

    try:
        # jsonモジュールでデータベースファイルを開く
        database = json.load(open(DATA_FLE, mode="r", encoding="utf-8"))
    
    except FileNotFoundError:
        database = []

    database.insert(0,{
        "start": start,
        'finish': finish,
        "memo": memo,
        "created_at": created_at.strftime("%Y-%m-%d %H:%M")
    })

    json.dump(database, open(DATA_FLE,mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)

def load_data():
    """記録データを返す"""
    try:
        # jsonモジュールでデータベースファイルを開く
        database = json.load(open(DATA_FLE, mode="r", encoding="utf-8"))
    
    except FileNotFoundError:
        database = []

    return database