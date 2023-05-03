# gmap-shop

Google mapから特定の情報を取得するAPI

# 開発環境
- Python 3.8.5

0. ファイルをローカルに用意
```zsh
git clone https://github.com/maru0804/gmap-shop.git
cd gmap-shop
```
1. venvで仮想環境を作成し有効化
```zsh
python3 -m venv [newenvname]
source [newenvname]/bin/activate
```
2. 必要なパッケージをインストール
```zsh
pip install -r requirements.txt
```
3. 仮想環境の修了
```zsh
deactivate
```

# 使い方
1. api keyの取得
[参考リンク](https://www.zenrin-datacom.net/solution/gmapsapi/api_key)

2. 取得したkeyを設定
以下の "your api key"にgoogle map api keyを入力
```conf.ini
[api-settings]
apiKey = "your api key"
```
3. 実行
```zsh
python3 main.py
```
4. 結果の確認
result.txt:全ての出力結果
result_limit:口コミが20件未満の結果

# 参考
- [20件以上の検索結果を取得する](https://developers.google.com/maps/documentation/places/web-service/search?hl=ja)