import threading
import time
import random

# Three forks represented as mutex locks.
NUM_PHILOSOPHERS = 3
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

#  Deadlock prevention strategy 
# OPTION A – "Resource Ordering":
#   Always acquire the LOWER-numbered fork first.
#   This breaks the circular-wait condition that causes deadlock.
#
#   Without ordering every philosopher picks left then right:
#     Ph-0 holds fork-0, waits for fork-1
#     Ph-1 holds fork-1, waits for fork-2
#     Ph-2 holds fork-2, waits for fork-0   ← circular wait!
#
#   With ordering the highest philosopher (Ph-2) must pick
#   fork-0 before fork-2, so it competes with Ph-0 instead
#   of forming the cycle.  Deadlock is impossible.


def philosopher(phil_id, meals=3):
    left  = phil_id
    right = (phil_id + 1) % NUM_PHILOSOPHERS

    # --- Resource ordering: always lock lower index first ---
    first, second = (left, right) if left < right else (right, left)

    for meal in range(1, meals + 1):
        # Think
        think_time = random.uniform(0.5, 1.5)
        print(f"Philosopher-{phil_id} is thinking "
              f"(meal {meal}/{meals})...")
        time.sleep(think_time)

        # Get hungry
        print(f"Philosopher-{phil_id} is hungry – "
              f"wants fork-{first} then fork-{second}")

        # Pick up forks in ordered sequence
        forks[first].acquire()
        print(f"  🍴 Philosopher-{phil_id} picked up fork-{first}")

        # Small delay to make the race more visible in output
        time.sleep(0.05)

        forks[second].acquire()
        print(f"  🍴 Philosopher-{phil_id} picked up fork-{second} "
              f"– now eating!")

        # Eat
        eat_time = random.uniform(0.5, 1.5)
        time.sleep(eat_time)
        print(f"Philosopher-{phil_id} finished eating "
              f"(meal {meal}/{meals}), putting down forks.")

        # Put down both forks
        forks[second].release()
        forks[first].release()

    print(f"Philosopher-{phil_id} has finished all meals.")


#  Main 
print("=" * 55)
print("  PART 3 – Dining Philosophers")
print(f"  {NUM_PHILOSOPHERS} philosophers, {NUM_PHILOSOPHERS} forks, 3 meals each")
print("  Deadlock prevention: Resource Ordering (Option A)")
print("=" * 55)

threads = [
    threading.Thread(target=philosopher, args=(i,), name=f"Ph-{i}")
    for i in range(NUM_PHILOSOPHERS)
]

start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()

print("-" * 55)
print(f"  All philosophers finished in {time.time()-start:.1f}s – no deadlock!")
print("=" * 55)
print("""
EXPLANATION
  Deadlock requires four conditions to hold simultaneously:
    1. Mutual exclusion   – forks can only be held by one philosopher
    2. Hold and wait      – a philosopher holds one fork while waiting
    3. No preemption      – forks cannot be forcibly taken
    4. Circular wait      – each philosopher waits for the next

  Resource Ordering eliminates condition 4 (circular wait).
  By always acquiring the lower-numbered fork first, no cycle
  can form in the wait-for graph, so deadlock is impossible.
""")
