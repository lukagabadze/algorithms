from typing import List


class Solution(object):
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2

            if arr[mid - 1] > arr[mid]:
                right = mid
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([0, 1, 0]),
        ([0, 2, 1, 0]),
        ([0, 10, 5, 2]),
        ([0, 1, 2, 3, 0]),
    ]

    for arr in q:
        print("arr: ", arr)
        print()
        answer = solution.peakIndexInMountainArray(arr)
        print("answer: ", answer)
        print("=====================")
        print()
