from typing import List
from collections import defaultdict

"""
TIME: 3ms (Beats 72.87%)
NOTE: By counting the frequency of each element and summing the prefixes in sorted order
you get the result straight away. But my implementation is a lil dogshit, that's why i got 3ms instead of 1ms.
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for i, num in enumerate(nums):
            freq[num] += 1

        sorted_nums = sorted(nums)
        ans_map = {}
        ans_map[sorted_nums[0]] = 0
        for i, num in enumerate(sorted_nums):
            if i == 0:
                continue

            if num in ans_map:
                continue

            prev_num = sorted_nums[i - 1]
            ans_map[num] = ans_map[prev_num] + freq[prev_num]

        ans = []
        for nums in nums:
            ans.append(ans_map[nums])

        return ans


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([8, 1, 2, 2, 3]),
        ([6, 5, 4, 8]),
        ([7, 7, 7, 7]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.smallerNumbersThanCurrent(nums)
        print("answer: ", answer)
        print("=====================")
        print()
