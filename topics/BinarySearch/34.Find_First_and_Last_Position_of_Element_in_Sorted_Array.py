from typing import List


class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find left
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        left_ans = left

        # Find right
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        right_ans = left - 1

        if left_ans > right_ans or left_ans >= len(nums):
            return [-1, -1]

        return [left_ans, right_ans]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 0),
        ([5, 7, 7, 8, 8, 10], 5),
        ([8, 8, 8, 8, 8, 8], 8),
    ]

    for nums, target in q:
        print("arr: ", nums)
        print("target: ", target)
        print()
        answer = solution.searchRange(nums, target)
        print("answer: ", answer)
        print("=====================")
        print()
