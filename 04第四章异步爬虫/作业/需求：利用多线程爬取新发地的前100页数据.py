import requests
from concurrent.futures import ThreadPoolExecutor

"""
    需求：利用多线程爬取新发地的前100页数据，保存在文件中
    要求：利用“多线程”，创建五个线程
    思路：
    1、打包返回源代码的函数
"""

url = "http://www.xinfadi.com.cn/getPriceData.html"



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
def socketor(url, data, charset='utf-8'):
    """
    发送一个get请求返回源代码
    :param url: url地址
    :return: source_code
    """
    resp = requests.post(url, headers=headers, data=data)
    resp.encoding = charset
    resp.close()
    return resp

def getdata():
    # 1、构造data
    for i in range(1,100):
        data = {
            "limit": 20,
            "current": i
        }
        # 2、构造一个resp
        resp = socketor(url,data=data)
        # 3、拿到数据
        dic =resp.json()
        itemlist = dic["list"]
        for item in itemlist: # item是每一个字典
            proname = item["prodName"]
            procat = item["prodCat"]
            avgprice = item["avgPrice"]
            highprice = item["highPrice"]
            lowprice = item["lowPrice"]

            with open("新发地菜市场价格表.txt", mode="a", encoding="utf-8") as f:
                # f.write("procat,proname,avgprice,highprice,lowprice")
                # f.write("\n")
                f.write(procat+","+proname+","+avgprice+"￥,"+highprice+"￥,"+lowprice+"￥")
                f.write("\n")
        print(f"第{i}页数据爬取完毕")

if __name__ == '__main__':

    with ThreadPoolExecutor(5) as t:
        t.submit(getdata())
        t.submit(getdata())
        t.submit(getdata())
        t.submit(getdata())
        t.submit(getdata())

