'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 16/01/2021 5:11 PM
@Software: PyCharm
@File    : demo.py
@Email   : huangsiyuan924@gmail.com
'''
import time

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
des_url = "http://127.0.0.1:8000/get_data"
for i in range(30):
    data_url = f'http://jzsc.mohurd.gov.cn/api/webApi/asite/credit/record/query?pg={i}&pgsz=15'

    enc_data = requests.get(data_url, headers=headers).text
    # 需启动node服务
    data = {
        'enc_data': enc_data
    }
    des_data = json.loads(requests.post(des_url, data=data).text)['result']
    # open('data.json', 'w', encoding='utf-8').write(des_data)
    print(des_data)
    time.sleep(1)