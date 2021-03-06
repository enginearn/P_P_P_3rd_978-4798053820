from distutils.log import debug
import json
from datetime import datetime

from flask import Flask, render_template, redirect, request, Markup, escape

application = Flask(__name__)

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

@application.route("/")
def index():
    """"トップページテンプレートを使用してページを表示"""
    # 記録データを読み込み
    rides = load_data()
    return render_template("index.html", rides=rides)

@application.route("/save", methods=["POST"])
def save():
    """"記録用URL"""
    # 記録されたデータを取得
    
    # 出発
    start = request.form.get("start")
    
    # 到着
    finish = request.form.get("finish")
    
    # メモ
    memo = request.form.get("memo")
    
    # 登録日時（現在時間）データを保存
    created_at = datetime.now()
    
    save_data(start, finish, memo, created_at)

    # 保存後はトップページへリダイレクト
    return redirect("/")

@application.template_filter("nl2br")
def nl2br_filter(s):
    """"改行文字をbrタグに置き換えるテンプレートフィルター"""
    return escape(s).replace("\n", Markup("<br>"))

if __name__ == "__main__":
    # IPアドレス 0.0.0.0:8000でアプリケーションを実行
    application.run("0.0.0.0", 8000, debug=True)

def main():
    application.run("127.0.0.1", 8000)

if __name__ == "__main__":
    # IPアドレス127.0.0.1/8000ポートでアプリケーションを実行
    application.run("127.0.0.1", 8000, debug=True)
