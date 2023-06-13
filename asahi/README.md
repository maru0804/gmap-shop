# 使い方
0. rootのreadmeで開発環境を構築する
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
python3 asahi/main.py
```
4. 結果の確認
result.txt:全ての出力結果
result_limit:口コミが20件未満の結果

# 参考
- [20件以上の検索結果を取得する](https://developers.google.com/maps/documentation/places/web-service/search?hl=ja)