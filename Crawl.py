from bs4 import BeautifulSoup
import requests
import Crawl_test


url = 'https://bbs.hupu.com/vote'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) \
Gecko/20100101 Firefox/57.0'}
try:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'lxml')
        son_html = soup.find_all('a', class_='truetit')
        for html in son_html:
            forum_url = 'https://bbs.hupu.com' + html
            # 使用get_content(url)获取主楼和首页无引用回复的文字

    else:
        print('Status Code is not 200!')
except requests.HTTPError as e:
    print('Http Error!')
