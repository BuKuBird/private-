import requests

url = "https://movie.douban.com/j/chart/top_list"
data = {
    'type': '13',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

resp = requests.get(url, params=data, headers=headers)

print(resp.json())