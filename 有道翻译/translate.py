'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 15/01/2021 1:02 PM
@Software: PyCharm
@File    : translate.py
@Email   : huangsiyuan924@gmail.com
'''
import requests
import execjs

with open('./js/get_datas.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# {'ts': '1610687020824', 'bv': '4f7ca50d9eda878f3f40fb696cce4d6d', 'salt': '16106870208242', 'sign': '16f25fdc8c675da5b4b5987e28ed6f46'}
translate_word = input("请输入要翻译的单词")
datas = ctx.call("generateSaltSign")
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '237',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': f'OUTFOX_SEARCH_USER_ID=211572624@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=134111340.54657455; JSESSIONID=aaafeQIOua05ieXVmweCx; ___rl__test__cookies={int(datas["ts"]) - 2}',
    'Origin': 'http://fanyi.youdao.com',
    'Pragma': 'no-cache',
    'Referer': 'http://fanyi.youdao.com',
    'Host': 'fanyi.youdao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'i': translate_word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': datas['salt'],
    'sign': datas['sign'],
    'lts': datas['ts'],
    'bv': datas['bv'],
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
print(data)
res = requests.post(url, headers=headers, data=data).text
print(res)
