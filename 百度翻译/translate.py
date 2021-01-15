'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 12/01/2021 3:53 PM
@Software: PyCharm
@File    : translate.py
@Email   : huangsiyuan924@gmail.com
'''
import requests
import execjs
with open('./js/get_sign.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'cookie': 'BAIDUID_BFESS=AC0379850370D46A3F574F7B8642EC55:FG=1;'
}

word = input("要翻译的单词:")
sign = ctx.call('get_sign', word)
print(sign)
data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'simple_means_flag': '3',
    'sign': sign,
    'token': '3af88f0a16d9527eef97f88dda38e492',
    'domain': 'common'
}


res = requests.post(url, headers=headers, data=data).text

# open('data.json', 'w', encoding='utf-8').write(res)
print(res)