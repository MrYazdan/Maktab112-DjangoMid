import multiprocessing
from tasks import task, timer

# Create Process
p1 = multiprocessing.Process(target=timer, args=(100,))
p2 = multiprocessing.Process(target=task, args=("One", 10))
p3 = multiprocessing.Process(target=task, args=("Two", 5))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

# timer(10)

print("All tasks completed!")