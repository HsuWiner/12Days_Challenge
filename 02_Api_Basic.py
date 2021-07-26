# -*- coding: utf-8 -*-



import urllib.request as req
import json

# #抓取伊莉網頁
url = 'https://www.dcard.tw/_api/forums'
#建立一個Request物件，附加RequestHeaders的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0"
})
with req.urlopen(request) as target:
    data=target.read().decode("utf-8")

    pass
#
# print(data)
#
data =json.loads(data) #把原始JSON的資料解析成字典或列表的表式形式

data = sorted(data, key=lambda k: k['subscriptionCount'])
# print(data)

for d in data[::-1][:5]:
    print('版塊名稱：',d['name'], '筆數：',d['subscriptionCount'])
