'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 14/01/2021 1:56 PM
@Software: PyCharm
@File    : login.py
@Email   : huangsiyuan924@gmail.com
'''
import json
import time

import requests
import execjs
with open('./js/get_enc_passwd.js', 'r', encoding='utf-8') as f:
    login_ctx = execjs.compile(f.read())
with open('./js/pojie.js', 'r', encoding='utf-8') as f:
    pojie_ctx = execjs.compile(f.read())
username = '13460533910'
password = 'Ww.1367039668'
enc_pass = login_ctx.call('encodePassword', password)
print(enc_pass)
login_url = "https://account.court.gov.cn/api/login"
data_url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

data = {
    'username': '13460533910',
    'password': enc_pass,
    'appDomain': 'wenshu.court.gov.cn'
}
session = requests.session()
session.headers = headers
res = session.post(login_url, data=data)

pageId = pojie_ctx.call("uuid")
ciphertext = pojie_ctx.call("cipher")
__RequestVerificationToken = pojie_ctx.call("__RequestVerificationToken")

formdata = {
    'pageId': pageId,
    's21': "阿里巴巴",
    'cfg': 'com.lawyee.wbsttools.web.parse.dto.AppUserDTO@currentUser',
    '__RequestVerificationToken': __RequestVerificationToken
}

autho = session.post(data_url, data=formdata)

# status = session.get('https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=f0d30970a53a7ea1e2f7a72a087c6cdc&s21=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4', headers=headers)
# print(status.cookies)
# print(autho.text)
# list_data = {
#     'pageId': pageId,
#     's17': '阿里巴巴',
#     'sortFields': 's50:desc',
#     'ciphertext': ciphertext,
#     'pageNum': '1',
#     'queryCondition': json.dumps([{"key": "s21", "value": "阿里巴巴"}]),
#     'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
#     '__RequestVerificationToken': __RequestVerificationToken
# }
#
# list_res = session.post(url=data_url, data=list_data)
# print(list_res.text)



