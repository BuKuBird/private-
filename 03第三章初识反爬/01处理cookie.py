# 登录 -> 得到一个cookie
# 带着cookie 去请求url
import requests

# 利用session




url = ""

session = requests.session(url)
session.get()
# session 类似一个会话，在会话中登陆之后，会保存你的cookie信息
# 类似于request夹带一个带有cookie的headers
