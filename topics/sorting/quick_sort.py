"""
Cool findings:
1) comments are cool in functions
2) arr[-1] returns the last element
"""


import time
from tools import generate_large_list

def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  pivot_ind = len(arr) // 2
  final_pivot_ind = sort_by_pivot(arr, pivot_ind)

  left_part = quick_sort(arr[0:final_pivot_ind])
  right_part = quick_sort(arr[final_pivot_ind + 1:])

  return left_part + [arr[final_pivot_ind]] + right_part

def sort_by_pivot(arr, pivot_ind):
  """
  Changes the array around the pivot.
  Elements less than the pivot are moved to the left.
  Elements larger than the pivot are moved to the right.
  Modifies the array and returns the final index of the pivot.
  """

  pivot = arr[pivot_ind]

  # Move pivot to the end
  arr[pivot_ind], arr[-1] = arr[-1], arr[pivot_ind]
  
  left_ind = 0
  right_ind = len(arr) - 2

  while(left_ind <= right_ind):
    if arr[left_ind] <= pivot:
        left_ind += 1
        
    if arr[right_ind] >= pivot:
      right_ind -= 1
      
    if left_ind <= right_ind and arr[left_ind] >= pivot and arr[right_ind] <= pivot:
      arr[left_ind], arr[right_ind] = arr[right_ind], arr[left_ind]

  # Pivot is in the end
  # swap the pivot with its new ind (left_ind)
  arr[left_ind], arr[-1] = arr[-1], arr[left_ind]

  return left_ind




if __name__ == '__main__':

  list_size = 50
  arr = generate_large_list(list_size)

  # arr = [6, 8, 5, 2, 7, 1, 9]
  # list_size = len(arr)

  # arr = [3, 2, 1, 2]
  # list_size = len(arr)
  
  # print('arr: ', arr)
  # print('pivot_ans_ind: ', sort_by_pivot(arr, 1))
  # print('arr: ', arr)


  print('arr: ', arr)
  print()
  start_time = time.time()
  sorted_arr = quick_sort(arr)
  end_time = time.time()
  print()
  print('sorted_arr: ', sorted_arr)

  print(f"Time taken to sort a list of {list_size} elements: {end_time - start_time:.6f} seconds")