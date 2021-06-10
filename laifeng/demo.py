import requests
import execjs


with open('./js/get_sign.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())

sign = ctx.call('test', '{"startTime":"2021-05-16","endTime":"2021-05-23","isReplied":0,"rateType":0,"rateContentType":0,"rateSourceType":1,"curPage":1,"perPage":20}'
            , "1621758270675")
print(sign)


