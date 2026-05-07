import threading
import time
import queue

BASKET_MAX = 5
ITEMS_EACH = 6
basket = queue.Queue(maxsize=BASKET_MAX)

# Producer
def baker(name):
    for i in range(ITEMS_EACH):
        bread = f"Bread-{i} by {name}"
        basket.put(bread)
        print(f"{name} made {bread} (size ≈ {basket.qsize()})")
        time.sleep(0.4)
    print(f"{name} finished baking")

# Consumer
def customer(name, items_to_eat):
    for _ in range(items_to_eat):
        bread = basket.get()
        print(f"{name} ate {bread}")
        basket.task_done()
        time.sleep(0.7)
    print(f"{name} finished eating")

# Threads
b1 = threading.Thread(target=baker, args=("Baker-1",))
b2 = threading.Thread(target=baker, args=("Baker-2",))
c1 = threading.Thread(target=customer, args=("Customer-1", ITEMS_EACH))
c2 = threading.Thread(target=customer, args=("Customer-2", ITEMS_EACH))

# Run
for t in [b1, b2, c1, c2]:
    t.start()

for t in [b1, b2, c1, c2]:
    t.join()

basket.join()  # ensure all items processed
print("All tasks completed. Basket empty:", basket.empty())