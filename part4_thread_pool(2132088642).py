import concurrent.futures
import threading
import time
import random
import math

# ---------------- Task Definition ----------------
def process_task(task_id):
    """Simulate work"""
    thread_name = threading.current_thread().name

    print(f"Task {task_id} starting on {thread_name}")

    # CPU work (lighter for safety)
    _ = math.factorial(1000)

    # Simulate I/O wait
    sleep_time = random.uniform(0.5, 2)
    time.sleep(sleep_time)

    print(f"Task {task_id} completed on {thread_name}")
    return task_id


NUM_TASKS = 10
MAX_WORKERS = 4

# ---------------- Sequential Execution ----------------
print("\nSequential Execution:")
seq_start = time.time()

for i in range(NUM_TASKS):
    process_task(i)

seq_time = time.time() - seq_start
print(f"\nTime: {seq_time:.2f} seconds")

# ---------------- Parallel Execution ----------------
print("\nParallel Execution:")

par_start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    results = list(executor.map(process_task, range(NUM_TASKS)))

par_time = time.time() - par_start

print(f"\nTime: {par_time:.2f} seconds")

# ---------------- Comparison ----------------
print("\nResults:")
print(f"Sequential: {seq_time:.2f} seconds")
print(f"Parallel:   {par_time:.2f} seconds")
print(f"Speedup:    {seq_time/par_time:.2f}x")