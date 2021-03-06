import requests
from bs4 import BeautifulSoup
import os
import re
global filename

# 此函数输入需要爬取的虎扑湿乎乎话题的网址，返回一个由主楼文字、首页去除引用文字组成的字符串
def get_content(_url):
    res = requests.get(_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    # 设置主楼内容列表、回复列表
    main_floor_content = []
    reply_floor_content = []
  
    floor = soup.find_all('div', class_='floor')
    # 获取主楼内容
    main_floor_content.append(floor[0].find('div', class_='quote-content').get_text().split('发自')[0])
    # 获取首页回复内容
    for i in range(1, len(floor)):
        raw_content = floor[i].find('table', class_='case')
        [s.extract() for s in raw_content('blockquote')]
        reply_floor_content.append(raw_content.get_text().split('发自')[0].replace('\n', ''))

    string1 = main_floor_content[0]
    string2 = '\n'.join(reply_floor_content)
    return string1 + string2

# 在实际使用中，此处url应该由遍历搜索得到（从Crawl模块中）
url = 'https://bbs.hupu.com/21212310.html'
a = get_content(url)
if not os.path.exists('D:\py'):
    os.mkdir('D:\py')

numberID = re.search('\d+',url).group()
filename = 'D:\py\CrawlData-'+ numberID
with open(filename+'.txt', 'a', encoding='utf8') as f:
    f.truncate()
    f.write(a)
    f.close()
