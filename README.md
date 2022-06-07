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

<img width="703" alt="スクリーンショット 2022-05-29 13 18 11" src="https://user-images.githubusercontent.com/73809994/170851996-7b6fa57d-9448-48b2-92b5-25197f6f1dce.png">


# Everyday BTC/JPY at 10:00(JST)
<br>2022-05-28 1BTC(JPY): 3691661
<br>2022-05-29 1BTC(JPY): 3672404
<br>2022-05-30 1BTC(JPY): 3812789<br>2022-05-31 1BTC(JPY): 4044251<br>2022-06-01 1BTC(JPY): 4096657<br>2022-06-02 1BTC(JPY): 3864097<br>2022-06-03 1BTC(JPY): 3971973<br>2022-06-04 1BTC(JPY): 3894198<br>2022-06-05 1BTC(JPY): 3887994<br>2022-06-06 1BTC(JPY): 4033669<br>2022-06-07 1BTC(JPY): 3900584