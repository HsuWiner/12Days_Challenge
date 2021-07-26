# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

import urllib.request as req
import json

        # "id": 1665148,

        # "name": "Taipei",
        # "state": "",
        # "country": "TW",
        # "coord": {
        #     "lon": 121.581749,
        #     "lat": 24.94702

url = 'https://api.openweathermap.org/data/2.5/forecast?id=1665148&units=metric&appid=a2c9084971421b5d6446fedbad7f3640'

# url = 'https://api.openweathermap.org/data/2.5/weather?id=7280289&units=metric&appid=a2c9084971421b5d6446fedbad7f3640'

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
# print(data['list'])
# list_data = data['list'][1]['main']

list_data = []
for item in data['list']:
    item['main']['dt_txt'] = item['dt_txt']
    # print(type(item['main'])
    list_data.append(item['main'])
# print(list_data)



sort_data = sorted(list_data,key=lambda k: k['temp_max'])
#
# print(sort_data)
for d in sort_data[::-1][:1]:
    # print(type(d))
    print('日期：',d['dt_txt'], '最高溫度：',d['temp_max'])
