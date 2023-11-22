from lxml import etree
import requests

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)

et = etree.HTML(resp.text)
# search-result-list-service
divs = et.xpath("//div[@class='service-card-wrap']/div")
for div in divs:
    # 此时div对应一个商品信息
    price = div.xpath("./div[@class='bot-content']/div[@class='price']/span/text()")[0]
    name = div.xpath("./a/div[@class='shop-box']/div[@class='shop-detail']/div/text()")[0]
    print(name,":",price)
