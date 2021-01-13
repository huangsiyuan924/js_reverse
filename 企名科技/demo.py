'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 12/01/2021 3:20 PM
@Software: PyCharm
@File    : demo.py
@Email   : huangsiyuan924@gmail.com
'''
import json

import execjs
import requests

url = 'https://vipapi.qimingpian.com/DataList/productListVip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': ''
}


res = requests.post(url, headers=headers, data=data).text
enc_data = json.loads(res)['encrypt_data']

with open('./js/decode.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
dec_data = ctx.call('my_decode', enc_data)

# open('data.json', 'w', encoding='utf-8').write(json.dumps(dec_data))
for data in dec_data['list']:
    print(data['product'])