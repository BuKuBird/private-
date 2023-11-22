import requests

content = input("请输入你想要检索的内容：")
url = f"https://cn.bing.com/search?q={content}"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
resp = requests.get(url)

print(resp.request.headers)