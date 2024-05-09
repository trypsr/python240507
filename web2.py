# web2.py
# 웹서버에 요청
# 당근마켓 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response =requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

f = open("daangn.txt", "wt", encoding="utf-8")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    f.write(f"{title}, {price}, {addr}\n")

f.close()



# <div class="card-desc">
# <h2 class="card-title">에어팟 프로1 팔.아요</h2>
# <div class="card-price ">
# 110,000원
# </div>
# <div class="card-region-name">
# 경남 김