from threading import Thread

# 创建任务
def func(name):
    for i in range(100):
        print(name,i)

# if __name__ == '__main__':
#     # 创建线程
#     t1 = Thread(target=func, args=("张佳宾",))
#     t2 = Thread(target=func, args=("郑语烨",))
#     t3 = Thread(target=func, args=("小来福",))
#
#     t1.start()
#     t2.start()
#     t3.start()

# 多线程写法，面向对象
# class MyThread(Thread):
#     def __init__(self, name):


# 总结：多进程和多线程的用途对照记忆
"""
    多线程：业务逻辑基本一致，可以用同一个函数来进行描述
    多进程：业务逻辑不一致，要用多个函数
"""