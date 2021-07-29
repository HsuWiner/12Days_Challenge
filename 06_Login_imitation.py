# -*- coding: utf-8 -*-

import urllib.request as req , bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #（資料來源：Yahoo 奇摩電影 ）

request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
    "cookie":"over18=1"
    })
with req.urlopen(request) as target:
    data=target.read().decode("utf-8")

    pass

# print(data)

root = bs4.BeautifulSoup(data,"html.parser")#讓beautifulSoup協助我們解析html格式文件

# 輸出排版後的 HTML 程式碼
# print(root.prettify())

ppt_ents = root.find_all('div',class_="r-ent")
# print(ppt_ents)

for ppt_ent in ppt_ents:
    print("============================================================")
    print('文章標題:',ppt_ent.find(class_="title").find("a").text.strip())
    print('文章時間:',ppt_ent.find(class_="date").text)
    pass
