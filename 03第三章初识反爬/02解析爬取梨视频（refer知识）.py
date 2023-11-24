import requests
from lxml import etree
# 改进：爬取网页的十八个视频
 # 思路：1、在梨视频首页找到各个视频的入口（把所有的url一次性提取出来）
 #      2、编写一个摘取视频的函数，传入参数可以是contid
# 注意在创建连接的时候不能开代理，不然会报错



# videoname  = ""
# contId = 1789267
# url1 = "https://www.pearvideo.com/video_1789267"
# url = f"https://www.pearvideo.com/videoStatus.jsp?contId='{contId}'&mrd=0.6269419464271935"
# print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    # "Referer": url1
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
    return resp

# 需要的url
# https://video.pearvideo.com/mp4/short/20231115/cont-1789267-16008473-hd.mp4
# https://video.pearvideo.com/mp4/short/20231115/cont-1789267--16008473-hd.mp4
# https://video.pearvideo.com/mp4/short/20231115/1700794587154-16008473-hd.mp4
# 获得的url
# https://video.pearvideo.com/mp4/short/20231115/ 1700793758721-16008473-hd.mp4




# print(inst[0])
# ['https://video.pearvideo.com/mp4/short/20231115/', '-16008473-hd.mp4']

# print(provideosrc)
# print(srcUrl)

# 编写一个直接获取mp4的方法
def getMp4(url,charset,contId,videoname):
    """

    :param url: 传入的url
    :param charset: 编码格式
    :param contId: 视频页面的id
    :param videoname: 视频的名字
    :return: None
    """

    resp = socketor(url, charset)
    dic = resp.json()
    print(dic)
    srcurl = str(resp.json()["videoInfo"]["videos"]["srcUrl"])
    systemtime = dic["systemTime"]
    inst = srcurl.split(f"{systemtime}")
    provideosrc = inst[0] + f'cont-{contId}' + inst[1]
    with open(f"{videoname}.mp4", mode="wb") as f:  # 在wb模式下不能用encoding
        f.write(requests.get(provideosrc).content)

mainpageurl = "https://www.pearvideo.com/"
resp = socketor(mainpageurl, "utf-8")
et = etree.HTML(resp.text)
# print(resp.text)
divs = et.xpath('//a[@class="actwapslide-link"]/@href')

names = et.xpath('//div[@class="actwapslide-title"]/text()')

# https://www.pearvideo.com/videoStatus.jsp?contId=1789640&mrd=0.9323776141614404
for i in range(len(divs)):
    div = str(divs[i])
    contId = div.split("_")[1]
    print(names[i])
    print(contId)
    url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.9323776141614404"
    print(url)
    getMp4(url, 'utf-8', contId, names[i])
    print(f'{names[i]}下载完毕')



