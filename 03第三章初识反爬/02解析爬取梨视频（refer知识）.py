import requests

contId = 1730846
url1 = "https://www.pearvideo.com/video_1730846"
url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.11070613714328803"

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

resp = socketor(url, "utf-8")
srcUrl = str(resp.json()["videoInfo"]["videos"]["srcUrl"])
srcUrl.strip("-",)
print(srcUrl)