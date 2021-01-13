'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 12/01/2021 2:08 PM
@Software: PyCharm
@File    : login.py
@Email   : huangsiyuan924@gmail.com
'''
import requests
import execjs


with open('./js/enc_pwd.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())

login_url = 'https://passport.fang.com/login.api'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f'
}
username = '13460533910'
password = 'asd1196039325'
enc_password = ctx.call('getPwd', password)
print(enc_password)
data = {
    'uid': username,
    'pwd': enc_password,
    'Service': 'soufun-passport-web',
    'AutoLogin': '1'
}

session = requests.session()

res = session.post(login_url, headers=headers, data=data).text
print(res)
