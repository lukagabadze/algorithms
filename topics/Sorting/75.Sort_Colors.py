from typing import List


class Solution(object):
    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, arr: List[int], low: int, high: int):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr: List[int], low: int, high: int):
        pivot = arr[high]
        pivot_ind = high

        while low <= high:
            if arr[low] <= pivot:
                low += 1

            if arr[high] >= pivot:
                high -= 1

            if low <= high and arr[low] >= pivot and arr[high] <= pivot:
                arr[low], arr[high] = arr[high], arr[low]

        # Put the pivot in it's place
        arr[pivot_ind], arr[low] = arr[low], arr[pivot_ind]

        # Return the new index of the pivot
        return low


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([10, 7, 8, 9, 1, 5]),
        ([2, 0, 2, 1, 1, 0]),
        ([2, 0, 1]),
    ]

    for arr in q:
        print("arr: ", arr)
        print()
        solution.sortColors(arr)
        print("answer: ", arr)
        print("=====================")
        print()
