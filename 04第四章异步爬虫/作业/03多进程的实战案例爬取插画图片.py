"""
    分析：
    1、访问首页，进到详情页
        url = "http://www.yuanhua.org/yuanhua.php?hid=3&indexkey=%C6%E6%BB%C3%B2%E5%BB%AD&page=1"
    2、得到下载链接，进行下载


"""
import requests
import urllib
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
def socketor(url, charset='gbk'):
    """
    发送一个get请求返回源代码
    :param url: url地址
    :return: source_code
    """
    resp = requests.get(url, headers=headers)
    resp.encoding = charset
    resp.close()
    return resp

def get_src():
    mainurl = f"http://www.yuanhua.org/yuanhua.php?hid=3&indexkey=%C6%E6%BB%C3%B2%E5%BB%AD&page=1"
    resp = socketor(url=mainurl)
    # print(resp.text)
    tree = etree.HTML(resp.text)
    page_num = tree.xpath('//tr[@bgcolor="#F8F8F8"]/td/text()')[1]

    # table_body = tree.xpath("//table")[2]

    print(page_num)
def down_load_img():
    pass

if __name__ == '__main__':
    get_src()