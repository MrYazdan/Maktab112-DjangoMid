import time
from functools import cache, lru_cache

caches = {}


# @cache
@lru_cache(maxsize=4)
def factorial(n):
    time.sleep(0.2)
    return n * factorial(n - 1) if n else 1


def power(a, b):
    if not (data := caches.get(f"{a}**{b}")):
        data = a ** b
        time.sleep(3)
        caches[f"{a}**{b}"] = data

    return data


start = time.perf_counter()
# print(power(8, 100))
print(factorial(9))
print("[9] Time: ", time.perf_counter() - start)

start = time.perf_counter()
print(factorial(8))
print("[8] Time: ", time.perf_counter() - start)

start = time.perf_counter()
print(factorial(7))
print("[7] Time: ", time.perf_counter() - start)

start = time.perf_counter()
print(factorial(9))
print("[9] Time: ", time.perf_counter() - start)

start = time.perf_counter()
print(factorial(8))
print("[8] Time: ", time.perf_counter() - start)

start = time.perf_counter()
print(factorial(7))
print("[7] Time: ", time.perf_counter() - start)
