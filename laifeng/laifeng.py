'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 2021/5/23 10:47
@Software: PyCharm
@File    : laifeng.py
@Email   : huangsiyuan924@gmail.com
'''
from urllib.parse import urlencode

import execjs
import requests
with open('./js/get_sign.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())




data = {
    'roomId': "98912",
    'content': '123123'
}
data1 = '{"roomId":"98912","content":"123123"}'
stmp1 = ctx.call("get_stmp")


sign = ctx.call('test', data1, stmp1)

url = f"https://acs.laifeng.com/h5/mtop.youku.live.platform.chat/1.0/?jsv=2.6.1&appKey=24679788&t={stmp1}&sign={sign}&type=originaljson&dataType=json&api=mtop.youku.live.platform.chat&v=1.0&ecode=1"

print(url)
headers = {
    # 'accept': 'application/json',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cache-control': 'no-cache',
    # # 'content-length': '68',
    # 'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mk=e653b7be13d943ee978a2fdfb2106aac; cna=ExIpGUEQPCsCAdocO1PfQ5ss; xlly_s=1; fansTuan-tips=vistived; anchor-task-tips=vistived; P_gck=NA%7CL5rZj%2BNsKmkUIl3A0UEayA%3D%3D%7CNA%7C1621739450836; disrd=58134; uk=391258134; P_sck=CU%2Bf8D%2FjpDm3f8T2O2USkwTfTJqYF16fd0vfNoS2yb4rdsGcX9kUFkNrDDg2yv45liWMWczDpYkNui41AgxL695BPcWwx%2BXLDSuWNxRfQZN1uJC%2F1xxviPTu%2B8P3zBtmctYdIIQ3pT6Of9Dy2nkOuA%3D%3D; P_pck_rm=vL2fqMhz3885981fb82f06ZBxkAE05jURmyqbCO%2Fm%2FhOlGYLbp1FIW3X71t8nT9Cva5da9ib%2B%2FRKDVJ%2BDdKiVhoDCRJwuAjCYcIt9YCPE5%2B%2F%2BU4CXBSCWRuDjO7tfpFoyM2kCti5bLs%2BNUiL%2BF4FTuqm4YqpkoY3%2F%2BN5zA%3D%3D_V2; __ysuid=1621751748715nDY; imk=MzkxMjU4MTM0LTEtMTYyMTc1NDY3NjAwNi0xNjIxODQxMDc2MDA2-A4D33C1E52D0E0F024503C45C795D7B7; _m_h5_tk=4d00f3740883b815a7e50b29fa772a13_1621759411565; _m_h5_tk_enc=3a4e95602510fc1d24f5861ad8a05f88; isg=BISEeHf9uN0ekgwS8nIV6zDuVQJ2nagHgr-yzZ4p_8_1yQ2Tvahnl-MjCWERUeBf',
    # 'origin': 'https://v.laifeng.com',
    # 'pragma': 'no-cache',
    # 'referer': 'https://v.laifeng.com/',
    # 'sec-ch-ua': ': " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',

}

user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

session = requests.Session()

req = session.post(url, headers=headers, data=data, verify=False)
print(req.text)
print(req.headers)
# req = requests.post(url, headers=headers, data=urlencode(data))
# print(req.text)


