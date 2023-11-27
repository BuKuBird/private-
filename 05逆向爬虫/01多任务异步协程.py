"""
    在一整个爬虫执行流程中：
        需要：准备访问数据->等待服务器返回数据->写入文件
    其中：等待IO操作（->阻塞）是最费时间的

    在之前：
    资源浪费1：每个进程会产生大量的IO阻塞，造成的资源浪费
    资源浪费2：CPU在每个线程之间切换的时候也会很耗资源

    于是，产生了一个模型 -> 使用程序完成：
        在主线程执行的时候，发现任务是阻塞状态，就会放一边
            #感觉类似于单片机里面的中断系统#

    总结：协程效率是最高的，协程和线程结合效率反而低了



"""
import asyncio
# 协程的基本语法
async def func():
    print("我是函数")



if __name__ == '__main__':
    # 协程对象想要执行必须借助于工event_loop(事件循环)
    # result = func() # result 是一个协程对象
    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(result)# 传入一个携程对象，到结束为止

    # 也可以直接用asyncio.run(func())
    asyncio.run(func())