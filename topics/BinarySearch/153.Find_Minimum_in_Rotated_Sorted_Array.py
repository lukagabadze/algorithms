"""
NOTE: HUGE thanks to water1111 for an amazing explanation!
(https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation)
"""

from typing import List


class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([3, 4, 5, 1, 2]),
        ([4, 5, 6, 7, 0, 1, 2]),
        ([11, 13, 15, 17]),
        ([1]),
        ([2, 1]),
        ([2, 3, 4, 5, 1]),
        ([3, 1, 2]),
        ([3, 4, 5, 6, 1, 2]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.findMin(nums)
        print("answer: ", answer)
        print("=====================")
        print()
