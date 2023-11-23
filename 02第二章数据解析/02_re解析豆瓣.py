import re

import requests



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}


def getter(url):
    f = open("top250.csv", mode="a", encoding='utf-8')
    resp = requests.get(url, headers=headers)

    print(resp.text)

    # 编写正则
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</sp'
                     r'an>.*?<p class="">.*?导演:(?P<daoyan>.*?)&nbsp.*?<br>'
                     r'(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<commit>.*?)</span>', re.S)

    result = obj.finditer(resp.text)

    for item in result:
        name = item.group('name')
        daoyan = item.group('daoyan')
        year = item.group('year').strip()
        score = item.group('score')
        commit = item.group('commit')
        f.write(f"{name},{daoyan},{year},{score},{commit}\n")
    f.close()
    resp.close()


for i in range(1, 11):
    url = f"https://movie.douban.com/top250?start={(i - 1) * 25}"
    getter(url)
print("db250 done!")
