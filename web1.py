# web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 소프객체 생성
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
# print(soup.find_all("p"))
# print(soup.find("p"))
# print(soup.find_all("p", class_="outer-text"))
# print(soup.find_all("p", attrs={"class":"outer-text"}))
# print(soup.find_all("p", attrs={"id":"first"}))
# 내부에 컨텐츠를 추출
for tag in soup.find_all("p"):
    title = tag.text.replace("\n", "")
    title = title.strip()
    print(title)
