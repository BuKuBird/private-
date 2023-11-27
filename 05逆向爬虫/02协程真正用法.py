import asyncio

async def func1():
    print("I love func1")
    await asyncio.sleep(1)
    print("func1 close!")


async def func2():
    print("I love func2")
    await asyncio.sleep(2)
    print("func2 close!")


async def func3():
    print("I love func3")
    await asyncio.sleep(3)
    print("func3 close!")


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    # 把三个任务放在一起
    tasks = [
        f1,
        f2,
        f3,
    ]

    asyncio.run(asyncio.wait(tasks))