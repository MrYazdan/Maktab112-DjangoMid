import asyncio


async def timer(end_time):
    for t in range(1, end_time+1):
        print(f"🕐 {t}s")
        await asyncio.sleep(1)


async def task(name, duration):
    print(f"[ Task: {name} ] -> Started")
    await asyncio.sleep(duration)
    print(f"[ Task: {name} ] -> Finished")


async def main():
    await asyncio.gather(timer(10),task("One",7), task("Two",3))


asyncio.run(main())