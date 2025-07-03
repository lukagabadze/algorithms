from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 1),
    ]

    for nums, target in q:
        print("nums: ", nums)
        print("target: ", target)
        print()
        answer = solution.searchInsert(nums, target)
        print("answer: ", answer)
        print("=====================")
        print()
