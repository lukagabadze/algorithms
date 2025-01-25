"""
You can't find the j and than swap, you have to swap each step of the way
example: [6, 8, 5, 2, 9]

TODO: Improve this algorithm with binary search
turn it into O(n*log(n))
"""

import time
from tools import generate_large_list

def insertion_sort(arr):
  sorted_arr = list(arr)
  n = len(arr)
  
  for i in range(n):
    j = i
    while j > 0 and sorted_arr[j - 1] > sorted_arr[j]:
      sorted_arr[j - 1], sorted_arr[j] = sorted_arr[j], sorted_arr[j - 1]
      j -= 1

  return sorted_arr


if __name__ == '__main__':

  list_size = 1000
  arr = generate_large_list(list_size)

  # arr = [6, 8, 5, 2, 7, 1, 9]

  # print('arr: ', arr)
  # print()
  start_time = time.time()
  sorted_arr = insertion_sort(arr)
  end_time = time.time()
  # print()
  # print('sorted_arr: ', sorted_arr)

  print(f"Time taken to sort a list of {list_size} elements: {end_time - start_time:.6f} seconds")