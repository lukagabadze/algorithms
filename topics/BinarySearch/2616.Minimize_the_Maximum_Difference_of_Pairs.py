"""
NOTE: Thanks to Sung Jinwoo for the solution!
(https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solutions/6833834/binary-search-on-answer-with-images-example-walkthrough-c-python-java)
"""

from typing import List


class Solution(object):
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        n = len(nums)
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2
            pairs = 0

            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    pairs += 1
                    i += 1
                i += 1

            if pairs >= p:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        # ([10, 1, 2, 7, 1, 3], 2),
        # ([4, 2, 1, 2], 1),
        # ([8, 9, 1, 5, 4, 3, 6, 4, 3, 7], 4),
        ([2, 6, 2, 4, 2, 2, 0, 2], 4)
    ]

    for nums, p in q:
        print("nums: ", nums)
        print("p: ", p)
        print()
        answer = solution.minimizeMax(nums, p)
        print("answer: ", answer)
        print("=====================")
        print()
