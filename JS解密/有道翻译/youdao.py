# -*- coding: utf-8 -*-

import requests
import hashlib, time, random


# md5 加密
def make_md5(word):
    word = word.encode()
    result = hashlib.md5(word)
    return result.hexdigest()


def youdao(word):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    t = make_md5(
        "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36")
    r = str(time.time() * 1000)
    i = r + str(random.randint(0, 9))

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "242",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1725511675@10.108.160.19; JSESSIONID=aaaMux7IyByBRgWacOEax; OUTFOX_SEARCH_USER_ID_NCOO=1781822059.0974677; ___rl__test__cookies=1581062027134",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    datas = {
        "i": word,  # 接收需要翻译的内容
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": i,  # 时间戳 + random.randint(0, 9)
        "sign": make_md5("fanyideskweb" + word + i + "n%A-rKaT5fb[Gy?;N5@Tj"),
        "ts": r,  # 时间戳
        "bv": t,  # md5加密的请求头
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
    }
    response = requests.post(url, headers=headers, data=datas)
    print(response.text)


if __name__ == '__main__':
    while True:
        word = input("请输入需要翻译的词汇:")
        youdao(word)
