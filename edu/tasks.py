import time


def timer(end_time):
    for t in range(1, end_time+1):
        print(f"🕐 {t}s")
        time.sleep(1)


def task(name, duration):
    print(f"[ Task: {name} ] -> Started")
    time.sleep(duration)
    print(f"[ Task: {name} ] -> Finished")