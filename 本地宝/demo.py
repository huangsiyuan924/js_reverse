'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 19/01/2021 9:32 PM
@Software: PyCharm
@File    : demo.py
@Email   : huangsiyuan924@gmail.com
'''
import requests
import json
url1 = 'http://m.baise.bendibao.com/news/gelizhengce/gl.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

}
data1 = {
    'a': 'k'
}
res1 = requests.post(url1, headers=headers, data=data1).text
enc_m = res1.split('"')[-2]
print(enc_m)
data = {
    'data': enc_m
}
dec_m = json.loads(requests.post('http://127.0.0.1:8000/get_sign', data=data).text)['result']
print(dec_m)
url3 = 'http://m.baise.bendibao.com/news/gelizhengce/gl.php?back=1&chufa_city=%E7%99%BE%E8%89%B2&mudi_city=%E5%B9%BF%E5%B7%9E&chufa_qu=&mudi_qu=&page=2'
data3 = {
    's': dec_m
}

res3 = requests.post(url3, data=data3).text
print(res3)
