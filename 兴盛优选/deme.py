'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 19/01/2021 3:19 PM
@Software: PyCharm
@File    : deme.py
@Email   : huangsiyuan924@gmail.com
'''
import json
import time
from urllib.parse import urlencode

import requests
import execjs


def download_data(data):
    url = "https://mall.xsyxsc.com/user/window/getProducts/v3"
    (timestamp, sign) = get_sign(data)
    headers = {
        'api-version': 'V3',
        'content-type': 'application/json',
        'version': '1.10.54',
        'userkey': '',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/5496 MicroMessenger/7.0.17.1720(0x27001134) Process/appbrand0 WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32',
        'api-timestamp': timestamp,
        'api-sign': sign,
    }
    res = requests.post(url, headers=headers, data=data, verify=False, proxies=proxies)
    # open('data.json', 'w', encoding='utf-8').write(res.text)
    print(res.text)
    res_data = json.loads(res.text)
    records = res_data['data']['records']
    spuSns = res_data['data']['spuSns'][:8]
    print(spuSns)
    for record in records:
        print(record['prName'])
    next_data ='{"userKey":"","windowId":2435,"areaId":105,"storeId":66880000717369,"excludeAct":"N","windowType":"BRAND_HOUSE","spuSns":' + str(spuSns).replace(' ', '').replace('\'', '"') + ',"isFirstRefresh":"FALSE"}'
    return next_data

def get_sign(data):
    timestamp = str(int(time.time() * 1000) + 32)
    n = data.replace(' ', '') + timestamp + "v9P3t$Zvl6"
    sign = ctx.call('get_api_sign', n)

    return (timestamp, sign)


proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

with open('./js/get_sign.js', 'r') as f:
    ctx = execjs.compile(f.read())

data = '{"windowId":2003,"areaId":105,"storeId":66880000717369,"excludeAct":"N","windowType":"BRAND_HOUSE","pageSize":8,"spuSns":[],"isFirstRefresh":"TRUE"}'




data = download_data(data)






