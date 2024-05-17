import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    #<div class="fds-ugc-block-mod-list D1LBvY2e8wjQ7CXzSwLa"><div v></div></div>
    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list D1LBvY2e8wjQ7CXzSwLa'})
    for post in posts:
        try:
            #<a nocr="1"  class="yz1I0On180p7Dx1HGomQ fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035491916.90000003_0000000000000033FF207857'" data-cb-trigger="true"><span class="Q1IHZg5jGcHwK32ErglP"><mark>맥북 에어</mark> 15인치 실버 구매 후기</span></a>
            #<span class="Q1IHZg5jGcHwK32ErglP"><mark>맥북 에어</mark> 15인치 실버 구매 후기</span></a>
            blog_address_elem = post.find("a", 
                attrs={"class":"yz1I0On180p7Dx1HGomQ fds-comps-right-image-text-title"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"Q1IHZg5jGcHwK32ErglP"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        #<span class="fds-info-sub-inner-text Q1IHZg5jGcHwK32ErglP">2024.04.12.</span>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text Q1IHZg5jGcHwK32ErglP'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"yz1I0On180p7Dx1HGomQ fds-comps-right-image-text-title"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)