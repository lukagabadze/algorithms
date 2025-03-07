"""
NOTE: This solution does not work without the @cache function tool.
Without the @cache it gets TLE.

NOTE: Interesting fact, you can't use @cache if one of the parameters of a function is a list you get an error: unhashable type: 'list'.
So instead, you can use tuples, it works exactly the same here, calculating the length and splitting the tuple, the syntax is same as arrays.

NOTE: This was my solution, but you can solve this much more simply without the @cache by using dynamic programming.
Check out niits solution (https://leetcode.com/problems/house-robber/solutions/6147042/2-solutions-o-n-space-and-o-1-space)
Time complexity is O(n), you can not go shorte than that, but you can optimize memeory by only saving last to values of the dynamic calculations.
"""

from typing import List, Tuple
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_tuple(nums: Tuple[int]) -> int:
            if len(nums) <= 1:
                return sum(nums)

            return max(nums[0] + rob_tuple(nums[2:]), nums[1] + rob_tuple(nums[3:]))

        return rob_tuple(tuple(nums))


if __name__ == "__main__":
    solution = Solution()

    # nums = [1, 2, 3, 1]

    nums = [2, 7, 9, 3, 1]

    # nums = [5]

    # nums = [2, 5]

    print("nums: ", nums)
    print("\n")
    answer = solution.rob(nums)
    print("answer: ", answer)
