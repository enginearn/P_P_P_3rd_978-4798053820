=============
乗りログアプリ
=============

目的
=============

Webブラウザーでコメントを投稿するWebアプリケーションの練習

ツールのバージョン
=============

:Python: 3.10.4
:pip:    22.0.4

インストールと起動方法
=============

Gitリポジトリからコードを取得し、その下にvenv環境を用意する::

    $ git clone https://github.com/enginearn/P_P_P_3rd_978-4798053820.git
    $ cd /P_P_P_3rd_978-4798053820/Capter_03/norilog
    $ python -m venv venv
    $ . ./env/Source/activate
    (venv) $ pip install .
    (venv) $ ./venv/Script/norilog.exe
    * Running on http://127.0.0.1:8000/

開発手順
=============

依存ライブラリ変更時
-------------

1. ``setup.py`` の ``install_requires`` を更新する
2. 以下の手順で環境を更新する::

    (venv) $ deactivate
    $ python -m venv --clear venv
    . ./venv/Source/activate
    (venv) $ pip install -e .

3. setup.pyをGitリポジトリにコミットする

開発用インストール
-------------

1. チェックアウトする
2. 以下の手順でインストールすｒ::

    (venv)$ pip install -e .