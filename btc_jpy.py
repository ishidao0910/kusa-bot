import datetime
import ssl
from bs4 import BeautifulSoup
import urllib.request as req

# ssl certificate expiration policy
ssl._create_default_https_context = ssl._create_unverified_context

d_today = datetime.date.today()
dt_now = datetime.datetime.now()
print("Run time: ", dt_now)


# 通貨設定
crypto = 'BTC'
currency = 'JPY'

# スクレイピングページ
url = 'https://coinyep.com/ja/ex/' + crypto + '-' + currency

# 取得結果
current_value = ''

# 取得先URLにアクセス
res = req.urlopen(url)

# 対象を抽出
soup = BeautifulSoup(res, 'html.parser')
values = soup.select_one("#coinyep-reverse1").findAll(text=True)
current_value = str(''.join(values))
current_value = current_value.replace('1 ' + crypto + ' = ', '')
current_value = current_value.replace(' ' + currency, '')

# 取得結果
add_txt = '<br>' + str(d_today) + ' 1' + crypto + '(' + currency + '): ' + str(current_value)

file_path = "README.md"
 
with open(file_path, "r") as file:
    txt = file.read()
    txt = txt + add_txt
    print(txt)

with open(file_path, 'w') as file:
    file.write(txt)
