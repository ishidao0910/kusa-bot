# Welcome to kusa-bot
このレポジトリでは、github actionsを用いてpushを定期実行します。

# Actions Flow
- 10:00(JST) cronジョブ起動
- pythonの実行環境構築
- pythonファイル(btc_jpy.py)実行
- サイトスクレイピング
- 取得した値段をREADME.mdに書き込み保存
- README.mdの編集差分をコミット
- push

# Everyday BTC/JPY at 10:00(JST)
<br>2022-05-28 1BTC(JPY): 3691661<br>2022-05-28 1BTC(JPY): 3691661
<br>2022-05-29 1BTC(JPY): 3688129<br>2022-05-29 1BTC(JPY): 3664470
