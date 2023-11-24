import requests

# 注意在创建连接的时候不能开代理，不然会报错


contId = 1789267
url1 = "https://www.pearvideo.com/video_1789267"
url = f"https://www.pearvideo.com/videoStatus.jsp?contId=1789267&mrd=0.6269419464271935"
print(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Referer": url1
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

resp = socketor(url, "utf-8")
dic = resp.json()
srcUrl = str(resp.json()["videoInfo"]["videos"]["srcUrl"])

systemTime = dic["systemTime"]
inst = srcUrl.split(f"{systemTime}")
# print(inst[0])
# ['https://video.pearvideo.com/mp4/short/20231115/', '-16008473-hd.mp4']
provideosrc = inst[0] + f'cont-{1789267}' + inst[1]
# print(provideosrc)
# print(srcUrl)
with open("1.mp4",mode="wb") as f: # 在wb模式下不能用encoding
    f.write(requests.get(provideosrc).content)
