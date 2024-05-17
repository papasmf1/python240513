# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#0페이지에서 9페이지까지 10개 
for n in range(0,10):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(url, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        
        # <span class="subject_fixed" data-role="list-title-text" title="갤럭시탭 S8 울트라 5G 256기가 박스 풀셋, 키보드 커버, 북커버 팝니다.">
	# 	갤럭시탭 S8 울트라 5G 256기가 박스 풀셋, 키보드 커버, 북커버 팝니다.
	# </span>
        for item in list:
                try:
                        title = item.text.strip() 
                        #필터링 
                        if (re.search('아이패드', title)):
                                print(title.strip())
                except:
                        pass
        
