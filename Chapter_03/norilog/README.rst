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
    $ . ./venv/Source/activate
    (venv) $ pip install -e .
    (venv) $ pip freeze > requirements.txt

3. setup.pyとrequirements.txtをGitリポジトリにコミットする

開発用インストール
-------------

1. チェックアウトする
2. 以下の手順でインストールする::

    (venv)$ pip install -e .

配布パッケージの作り方
-------------

1. ``pip`` で ``wheel`` をインストール::

    (venv) $ pip install wheel

2. wheelパッケージを作成::

    (venv) $ python setup.py bdist_wheel
    (venv) $ ls dist/
    norilog-1.0.0-py3-none-any.whl norilog-1.0.0.tar.gz

PyPI公開前のリリースチェックを ``alias`` 登録
-------------
::
    (venv) $ python setup.py alias release check -r -s sdist bdist_wheel --universal
    (venv) $ python setup.py release
    