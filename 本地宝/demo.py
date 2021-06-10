'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 19/01/2021 9:32 PM
@Software: PyCharm
@File    : demo.py
@Email   : huangsiyuan924@gmail.com
'''
import time

import requests
import json


def get_proxie():
    data = requests.get("http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=1&pack=134600&ts=1&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=320000,330000,340000,360000,370000&gm=4").text
    data = json.loads(data)
    print(data)
    if data['success'] == True:
        proxies = "http://" + data['data'][0]['ip'] + ":" + str(data['data'][0]['port'])
        print('获取代理成功')
        return proxies
    print('获取代理失败')

def main():
    url1 = 'http://m.baise.bendibao.com/news/gelizhengce/gl.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

    }
    prox = get_proxie()
    print(prox)
    proxies = {
        'http': prox,
        'https': prox
    }

    data1 = {
        'a': 'k'
    }
    res1 = requests.post(url1, headers=headers, data=data1, proxies=proxies).text
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

    res3 = requests.post(url3, data=data3, proxies=proxies).text
    # print(res3)

if __name__ == '__main__':
    success_count = 0
    error_count = 0
    for i in range(100):
        try:
            main()
            success_count += 1
            print("success")
        except:
            error_count += 1
            print("error")
        time.sleep(3)
    print("=" * 70)
    print(f"success_count={success_count}, error_count={error_count}")







