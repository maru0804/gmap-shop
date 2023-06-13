import requests
from bs4 import BeautifulSoup

# WikipediaのURL
url = 'https://www.japanese.hostelworld.com/st/hosuteru/p/272463/hosuterubetsudogazumu/'

# requestsを使ってウェブサイトからHTMLを取得する
response = requests.get(url)
# BeautifulSoupでHTMLをパースする
soup = BeautifulSoup(response.text, 'html.parser')

title = "test"
name = soup.find_all("div", class_="score orange big")

for i in name:
    print(i.text)
    if i.text != "":
        break