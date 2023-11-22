"""
可以定义一个访问函数，返回值是源代码
"""
import requests
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

url = "https://dy2018.com/"
print(socketor(url, "utf-8"))