'''
-*- coding: utf-8 -*-
@Author  : Haxp
@Time    : 30/01/2021 11:14 PM
@Software: PyCharm
@File    : demo.py
@Email   : huangsiyuan924@gmail.com
'''
import json
import random
import requests
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["驾考宝典"]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


qs_data = json.loads(requests.post('http://127.0.0.1:8000/get_qs').text)['qs']
qs_data = json.loads(qs_data)
for chexing in qs_data['data']:
    for kemu in qs_data['data'][chexing]:
        for num in qs_data['data'][chexing][kemu]:
            qs = qs_data['data'][chexing][kemu][str(num)]
            mycol = mydb[f"{chexing}_{kemu}"]
            for i in range(0, len(qs), 20):
                questionIds = qs[i: i + 20]
                questionIds = ','.join(questionIds)
                print(questionIds)
                r = json.loads(requests.get('http://127.0.0.1:8000/get_r').text)['r']
                url = "https://api2.jiakaobaodian.com/api/open/question/question-list.htm"
                formdata = {
                    '_r': r,
                    'questionIds': questionIds,
                    '_': random.random()
                }
                question_res = requests.get(url, headers=headers, params=formdata)
                question_json = json.loads(question_res.text)
                question_data = question_json['data']
                mycol.insert_many(question_data)
            print(f"{chexing}_{kemu}  over")



