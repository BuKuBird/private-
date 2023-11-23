from pyquery import PyQuery

html = """
    <li><a href="http://www.baidu.com">百度</a></li>
"""

# 加载html的内容
p = PyQuery(html)
li = p("li a")

print(li)