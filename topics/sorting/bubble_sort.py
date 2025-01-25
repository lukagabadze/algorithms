"""
  What's the complexity of this?
  - I think it is O(n^2)
"""

def bubble_sort(arr):
  sorted_arr = list(arr)
  n = len(arr)
  
  for i in range(n):
    swapped = False
    for j in range(n - i - 1):
      if sorted_arr[j] > sorted_arr[j + 1]:
        sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
        swapped = True
      
    if not swapped:
      break
  
  return sorted_arr


import time
from tools import generate_large_list

if __name__ == "__main__":

  list_size = 1000
  arr = generate_large_list(list_size)
  
  # arr = [2, 3, 4, 5, 6, 7, 1]
  # list_size = len(arr)

  # print('arr: ', arr)
  # print()
  start_time = time.time()
  sorted_arr = bubble_sort(arr)
  end_time = time.time()
  # print()
  # print('sorted_arr: ', sorted_arr)

  print(f"Time taken to sort a list of {list_size} elements: {end_time - start_time:.6f} seconds")