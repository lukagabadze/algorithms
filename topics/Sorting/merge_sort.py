import time
from tools import generate_large_list


def merge_sort(arr):
    # Base Case: an array with  0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    size = len(arr)
    mid = size // 2

    # You can make an improvement here arr[:mid]
    first_half_sorted = merge_sort(arr[0:mid])
    second_half_sorted = merge_sort(arr[mid:size])  # Here as well arr[mid:]

    # Combine this two arrays
    return merge(first_half_sorted, second_half_sorted)


def merge(arr1, arr2):
    merged_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    # NOTE: now one of the arrays is empty and other one still has elements
    # push the rest of the elements in the merged_arr
    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])

    return merged_arr


if __name__ == "__main__":
    list_size = 1000
    arr = generate_large_list(list_size)

    # arr = [6, 8, 5, 2, 7, 1, 9]
    # list_size = len(arr)

    # print('arr: ', arr)
    # print()
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    # print()
    # print('sorted_arr: ', sorted_arr)

    print(
        f"Time taken to sort a list of {list_size} elements: {
          end_time - start_time:.6f} seconds"
    )
