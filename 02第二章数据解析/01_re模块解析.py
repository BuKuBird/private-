import re


# findall 查找所有返回列表
# finditer 查找所有，返回迭代器
# match 从开头开始匹配，类似于正则前面加个^
# search 匹配到了之后，直接返回第一个

# 预加载 ：提前把加载对象加载完毕
# obj = re.compile(r"\d+")
# result = obj.findall("我今年18岁，我有2090块钱")
#
# print(result)



# result = re.findall(r'\d+', '我今年十八岁，我有2090块钱')
#
# print(result)

# result = re.finditer(r'\d+', '我今年十八岁，我有2090块钱')
#
# for i in result:
#     print(i.group())

s = """
<div class="西游记"><span id='10010'>中国联通</span></div>    
<div class="西游记"><span id='10086'>中国移动</span></div>   
"""
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")

result = obj.finditer(s)
for i in result:
    id = i.group("id")
    print(id)
    name = i.group("name")
    print(name)