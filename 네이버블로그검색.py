import requests
from bs4 import BeautifulSoup
import time
import openpyxl

# Function to fetch HTML content from a URL
def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

# Function to parse the HTML and extract the desired information
def parse_naver_search(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    # Locate the container elements for blog posts
    for item in soup.select('.list_item'):
        blog_name = item.select_one('.source .name').get_text(strip=True)
        blog_url = item.select_one('.source a')['href']
        title = item.select_one('.title').get_text(strip=True)
        post_date = item.select_one('.date').get_text(strip=True)

        results.append({
            'blog_name': blog_name,
            'blog_url': blog_url,
            'title': title,
            'post_date': post_date,
        })

    return results

# Function to scrape multiple pages
def scrape_multiple_pages(query, start_page, end_page):
    all_results = []
    base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}&start={start}"

    for page in range(start_page, end_page + 1):
        start = (page - 1) * 10 + 1
        url = base_url.format(query=query, start=start)
        html_content = fetch_html(url)
        page_results = parse_naver_search(html_content)
        all_results.extend(page_results)
        time.sleep(1)  # Be respectful and avoid making requests too quickly

    return all_results

# Function to save results to an Excel file
def save_to_excel(data, filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Blog Posts"
    
    # Adding header
    headers = ["Blog Name", "Blog URL", "Title", "Post Date"]
    sheet.append(headers)

    # Adding data
    for entry in data:
        sheet.append([entry['blog_name'], entry['blog_url'], entry['title'], entry['post_date']])
    
    workbook.save(filename)

# Main execution
if __name__ == "__main__":
    query = "맥북에어"
    start_page = 1
    end_page = 100
    blog_posts = scrape_multiple_pages(query, start_page, end_page)
    
    save_to_excel(blog_posts, "result.xlsx")
    print(f"Saved {len(blog_posts)} blog posts to result.xlsx")
