"""
NOTE: This solution does not work without the @cache function tool.
Without the @cache it gets TLE.

NOTE: Interesting fact, you can't use @cache if one of the parameters of a function is a list you get an error: unhashable type: 'list'.
So instead, you can use tuples, it works exactly the same here, calculating the length and splitting the tuple, the syntax is same as arrays.
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
