# web1.py 
#웹 크롤링을 위한 연습 
from bs4 import BeautifulSoup

#파일을 로딩:메서드체인, 함수체인 
page = open("test.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

