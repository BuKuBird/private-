from concurrent.futures import ThreadPoolExecutor
import time
def func(name, t):
    time.sleep(t)
    for i in range(10):
        print(name,i)

def fn(res):
    print(res.result())

if __name__ == '__main__':
    # with ThreadPoolExecutor(3) as t:
    #     t.submit(func, "周杰伦", 2).add_done_callback(fn)
    #     t.submit(func, "王力宏", 1).add_done_callback(fn)
    #     t.submit(func, "林俊杰", 3).add_done_callback(fn)
    #     .add_done_callback 返回就执行callback函数
    #       线程同时在进行，所以返回的顺序是不固定的

    #-----------------
    # 顺序的返回值
    # result = t.map(func, ["周杰伦","王力宏","王富贵"],[2,1,3])
    # map进行两两配对之后放进参数
    # 这个返回值是有顺序的，返回的数据和写入的参数顺序一致
    # result 是一个生成器类型的数据，用fori






# if __name__ == '__main__':
#     with ThreadPoolExecutor(10) as t:
#         for i in range(100):
#             t.submit(func, f"周杰伦{i}")