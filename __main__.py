import time
from algorithms.bruteforce import bruteforce
from algorithms.optimized import optimized
from utils import get_shares
import tracemalloc

max_expenses = 500
csvfile = 'dataset1.csv'
names, costs, profits = get_shares(csvfile,20)

print("\n--- Bruteforce (20) ---")
start_time = time.time()
tracemalloc.start()
result = bruteforce(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("\x1b[36m--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB\x1b[0m")


print("\n--- Optimized (20) ---")
start_time = time.time()
tracemalloc.start()
result = optimized(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("\x1b[36m--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB\x1b[0m")


names, costs, profits = get_shares(csvfile,25)

print("\n--- Bruteforce (25) ---")
start_time = time.time()
tracemalloc.start()
result = bruteforce(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")


print("\n--- Optimized (25) ---")
start_time = time.time()
tracemalloc.start()
result = optimized(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")

names, costs, profits = get_shares(csvfile,30)

print("\n--- Bruteforce (30) ---")
start_time = time.time()
tracemalloc.start()
result = bruteforce(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")


print("\n--- Optimized (30) ---")
start_time = time.time()
tracemalloc.start()
result = optimized(names,costs,profits,max_expenses)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time() - start_time
print(result)
print("--- Résultat obtenu en %s seconds ---" % (end_time))
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
