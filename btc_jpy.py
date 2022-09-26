import datetime
import requests
from bs4 import BeautifulSoup

# 時間帯取得
d_today = datetime.date.today()
dt_now = datetime.datetime.now()
print("Run time: ", dt_now)

# 通貨設定
crypto = 'BTC'
currency = 'JPY'

def getprice(url):
    HTML = requests.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        },
    )
    soup = BeautifulSoup(HTML.text, "lxml")
    text = soup.find("span", attrs={"class": "pclqee"}).text.split(".")[0]
    return text


if __name__ == "__main__":
    url = "https://www.google.com/search?q=bitcoin+price"
    file_path = "README.md"

    btc_price = getprice(url)
    add_txt = '<br>' + str(d_today) + ' 1' + crypto + '(' + currency + '): ' + str(btc_price)

    with open(file_path, "r") as file:
        txt = file.read()
        txt = txt + add_txt
        print(txt)

    with open(file_path, 'w') as file:
        file.write(txt)