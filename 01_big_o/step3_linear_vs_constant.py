# Big O = count operations.
# Linear time O(n): work grows with n.   Constant time O(1): work stays the same.
import time

def up_to_n(n):            # O(n)
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(f"Linear time: when n is {n} sum is {total}")
    return total

def up_to_n_2(n):          # O(1)
    total = n * (n + 1) // 2
    print(f"Constant time: when n is {n} sum is {total}")
    return total

n = 200000

start = time.perf_counter()
up_to_n_2(n)
print(f"Execution time: {(time.perf_counter() - start) * 1000} ms\n")

start = time.perf_counter()
up_to_n(n)
print(f"Execution time: {(time.perf_counter() - start) * 1000} ms")
