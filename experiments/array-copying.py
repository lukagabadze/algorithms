import time

arr = list(range(1000000))  # Large list for testing

# Timing list()
start = time.time()
copy_list = list(arr)
end = time.time()
print(f"list() time: {end - start:.10f} seconds")

# Timing .copy()
start = time.time()
copy_copy = arr.copy()
end = time.time()
print(f"copy() time: {end - start:.10f} seconds")

# Timing .copy()
start = time.time()
copy_copy = arr[:]
end = time.time()
print(f"arr[:] time: {end - start:.10f} seconds")