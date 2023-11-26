import requests

url = "http://jwxt.fjjxu.edu.cn:81/jwglxt/xtgl/index_initMenu.html?jsdm=&_t=1700937397428"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Cookie": "JSESSIONID=AF0939BD64C83C57C403FFAD567454FD",
    "Referer": "http://jwxt.fjjxu.edu.cn:81/jwglxt/xtgl/login_slogin.html?language=zh_CN&login_type=undefined"
}

resp = requests.get(url, headers=headers)
print(resp.text)
