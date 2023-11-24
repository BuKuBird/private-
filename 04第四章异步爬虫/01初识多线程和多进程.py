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


