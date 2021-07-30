# -*- coding: utf-8 -*-

import urllib.request as req , bs4

url = 'https://hiskio.com/'

response = req.urlopen(url)
html = response.read()
text = html.decode("utf-8")

root = bs4.BeautifulSoup(text,"html.parser")#讓beautifulSoup協助我們解析html格式文件

# 輸出排版後的 HTML 程式碼
print(root.prettify())
