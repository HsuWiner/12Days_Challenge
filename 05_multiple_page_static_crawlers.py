# -*- coding: utf-8 -*-

import urllib.request as req , bs4

def get_html(input):
    request = req.Request(input,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0"
    })

    with req.urlopen(request) as target:
        data = target.read().decode("utf-8")
        pass

    loc_root = bs4.BeautifulSoup(data,"html.parser")
    return(loc_root)#讓beautifulSoup協助我們解析html格式文件

    pass

def Prt_Movie():
    movie_info = root.find_all('div',class_="release_info")
    for movie in movie_info:

        print('電影中文名:',movie.find(class_="release_movie_name").find("a").text.strip())
        print('電影英文名:',movie.find(class_="en").find("a").text.strip())
        print('期待度:',movie.find("span").text)
        print(movie.find(class_="release_movie_time").text.strip())
        print("============================================================")

        pass
    pass

url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
# root = get_html(url)
# Prt_Movie()
# link_tag = root.find('li',class_="nexttxt")
# url = link_tag.find("a").get("href")


while type(url) == str:
    root = get_html(url)
    Prt_Movie()

    link_tag = root.find('li',class_="nexttxt")

    try:
        url = link_tag.find("a").get("href")
    except:
        print("已無下一頁資訊")
        break
