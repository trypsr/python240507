import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹서버에 요청
# 당근마켓 크롤링
import requests
from bs4 import BeautifulSoup
import time


# 디자인파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# class DemoForm(QDialog, form_class):
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.label.setText("첫번째 PyQt데모")
    #슬롯메서드
    def fstClick (self) :
        self.label.setText("당근마켓 크롤링 시작")
        url = "https://www.daangn.com/fleamarket/"
        response =requests.get(url)
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        f = open("daangn2.txt", "a+", encoding="utf-8")
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
        self.label.setText("당근마켓 크롤링 완료")
    def scdClick(self) :
        self.label.setText("2 click")
    def thdClick(self) : 
        self.label.setText("3 click")

## 직접 진입한 경우
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()

