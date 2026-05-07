import threading
import time
#---------------Unsynchronized Counter------------------- 
class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        temp = self.value
        time.sleep(0.00005)
        self.value = temp + 1

#-----------Synchronized Counter -------------- 
class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            temp = self.value
            time.sleep(0.00005)
            self.value = temp + 1


#------------Worker Function------------------------
def worker(counter, increments):
    for _ in range(increments):
        counter.increment()

#------------Helper------------------------
def run_threads(counter, num_threads=3, increments=1000):
    threads = [
        threading.Thread(target=worker, args=(counter, increments))
        for _ in range(num_threads)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

#------------Main-------------------------
NUM_THREADS  = 3
INCREMENTS   = 1000
EXPECTED     = NUM_THREADS * INCREMENTS   # 3000

print("WITHOUT LOCK:")
unsafe = UnsafeCounter()
run_threads(unsafe, NUM_THREADS, INCREMENTS)
print(f"Final counter value: {unsafe.value} (WRONG!)")

print("\nWITH LOCK:")
safe = SafeCounter()
run_threads(safe, NUM_THREADS, INCREMENTS)
print(f"Final counter value: {safe.value} (CORRECT!)")