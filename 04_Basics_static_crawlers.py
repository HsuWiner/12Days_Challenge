# -*- coding: utf-8 -*-

import urllib.request as req , bs4

url = 'https://movies.yahoo.com.tw/movie_thisweek.html' #（資料來源：Yahoo 奇摩電影 ）

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0"
})
with req.urlopen(request) as target:
    data=target.read().decode("utf-8")

    pass

# print(data)

root = bs4.BeautifulSoup(data,"html.parser")#讓beautifulSoup協助我們解析html格式文件

# 輸出排版後的 HTML 程式碼
# print(root.prettify())

movie_name_ch = root.find_all('div' , class_="release_movie_name")
movie_name_en = root.find_all('div' , class_="en")
movie_level = root.find_all('div' , class_="leveltext")
movie_time = root.find_all('div' , class_="release_movie_time")
# print(movie_name_ch)
# print('------------------------------------------------')
# print(movie_name_en)
# print('------------------------------------------------')
# print(movie_level)
# print('------------------------------------------------')
# print(movie_time)
#

index = 0

for name in movie_name_ch:
    text = name.text[20:40]
    print('電影中文名:',text[0:20])
    text = movie_name_en[index].text[22:50]
    print('電影英文名:',text)
    text = movie_level[index].text[0:5]
    print('網友期待度:',text)
    text = movie_time[index].string
    print(text)
    index += 1
#
# for name in movie_name_en:
#     print('------------------------------------------------')
#     print(name.text[22:50])
#
# for name in movie_level:
#     print('------------------------------------------------')
#     print(name.text[0:5])
#
# for name in movie_time:
#     print('------------------------------------------------')
#     print(name.string)

# for a_href in a_hrefs:
#     print('------------------------------------------------')
#     print(a_href.text)
    # print('電影中文名:',a_href.text[20:50])
    # print("標題：" + a_href.text)
    #
    # if a_href.get('href') != None:
    #     print("網址：" + a_href.get('href'))
    #     pass
    # pass



# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html5lib')
#
# infos = []
#
# for d in soup.find_all('div', class_='release_info'):
#   infos.append({
#     '中文名稱': d.find('div', class_='release_movie_name').find('a').text.strip(),
#     '英文名稱': d.find('div', class_='release_movie_name').find('div', class_='en').text.strip(),
#     '上映日期': d.find('div', class_='release_movie_time').text.strip(),
#     '期待度': d.find('div', class_='leveltext').span.text.strip() if d.find('div', class_='leveltext') else ''
#   })
#
# import pandas as pd
# df = pd.DataFrame(infos)
# print(df)
