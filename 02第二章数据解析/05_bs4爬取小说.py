from bs4 import BeautifulSoup

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

url = "http://www.umeituku.com/bizhitupian/"

main_page = BeautifulSoup(socketor(url, "utf-8"), "html.parser")

a_list = main_page.find_all("a", attrs={"class": "TypeBigPics"})
for a in a_list:
    print(a.text)
    # print(a.get("href"))
    child_page = socketor(url=a.get("href"), charset="utf-8")
    child_bs = BeautifulSoup(child_page, "html.parser")
    div = child_bs.find("div", attrs={"class": "ImageBody"})
    child_imgsrc = div.find("img")
    print(child_imgsrc)
