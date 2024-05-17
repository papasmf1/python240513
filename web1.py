# web1.py 
#웹 크롤링을 위한 연습 
from bs4 import BeautifulSoup

#파일을 로딩:메서드체인, 함수체인 
page = open("test.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<p>전체를 검색
#print(soup.find_all("p"))
#첫번째 <p>를 검색
#print(soup.find("p"))
#<p class="outer-text"> 조건이 있는 경우 
#print(soup.find_all("p", class_="outer-text"))
# attrs(속성들)
#print(soup.find_all("p", attrs={"class":"outer-text"}))
# id = first 
#print(soup.find_all(id="first"))
#검색한 태그 안쪽에 컨텐츠: .text 속성명 
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)




