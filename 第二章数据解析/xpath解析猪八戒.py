from lxml import etree
import requests

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)

et = etree.HTML(resp.text)
# search-result-list-service
divs = et.xpath("//div[@class='search-result-list-service']/div")
for div in divs:
    # 此时div对应一个商品信息
    div.xpath("./")