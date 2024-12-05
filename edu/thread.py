import threading
from tasks import task, timer

# Create Threads
t1 = threading.Thread(target=timer, args=(10,))
t2 = threading.Thread(target=task, args=("One", 3))
t3 = threading.Thread(target=task, args=("Two", 8))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# timer(10)

print("All tasks completed!")