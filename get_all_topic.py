#!/usr/bin/env python
#pip install requests beautifulsoup4
import requests
import bs4
from bs4 import BeautifulSoup
url = 'http://192.168.5.135:8100/rmq/topic/list.do'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
topic_list = []
for item in soup.find_all('td')[::2]:
        topic_list.append(item.get_text().encode("utf-8"))

for topic in topic_list[:]: 
    if topic.startswith('%'): 
        topic_list.remove(topic)
print topic_list


