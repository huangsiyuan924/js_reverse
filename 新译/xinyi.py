'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 2021/5/24 16:17
@Software: PyCharm
@File    : xinyi.py
@Email   : huangsiyuan924@gmail.com
'''
import requests

url = "https://fanyi.newtranx.com/xy/admin/translate"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
data = {
    'text': 'dog',
    'direction': 'en-zh',
    'common': 'common',
    'glossaryLibs': '',
    'memoryLibs': ''
}


text = "dog"
data['text'] = text
res = requests.post(url, headers=headers, data=data)
print(res.text)
