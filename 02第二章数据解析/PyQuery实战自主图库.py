from pyquery import PyQuery
import requests
# 利用PyQuery 爬取图片

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
def socketor(url, charset):
    """
    发送一个get请求返回源代码
    :param url: url地址
    :return: source_code
    """
    resp = requests.get(url, headers=headers)
    resp.encoding = charset
    resp.close()
    return resp.text

url = "https://www.58pic.com/tupian/qinglv.html"
resp = socketor(url, 'gbk')
print(resp)

p = PyQuery(resp)
p("")