# web2.py 
#당근마켓 데이터 크롤링 
#웹서버에 요청할 경우 사용 
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/" 
page = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(page, "html.parser")

#파일로 저장
f = open("daagn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    #f-string:포맷 스트링
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close() 

    # <div class="card-desc">
    #   <h2 class="card-title">LG티비 55인치</h2>
    #   <div class="card-price ">
    #     100,000원
    #   </div>
    #   <div class="card-region-name">
    #     전남 광양시 광양읍
    #   </div>