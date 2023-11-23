from bs4 import BeautifulSoup

html = """
<ul>
<li><a href="zhangwuii. com">张无忌</a></li>
<li id="abc"><a href="zhouxingchi.com">周星驰</a></li><li><a href="zhubajie.com">猪八戒</a></li>
<li><a>href="wuzetian.com">武则天</a></li>
</ul>
"""

# 初始化BeautifulSoup对象
page = BeautifulSoup(html, "html.parser")

li = page.find("li", attrs={"id": "abc"})

a = li.find("a")
print(li)
print(a)
print(a.text)
print(a.get("href"))